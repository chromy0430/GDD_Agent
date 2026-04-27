import os
import re
import json
import time
import glob
import math
import shutil
import random
import hashlib
import tempfile
from collections import deque
from datetime import datetime
import gc
import fitz  # PyMuPDF
from pypdf import PdfReader
from google import genai
from langchain_google_genai import GoogleGenerativeAIEmbeddings

try:
    from langchain_chroma import Chroma
except ImportError:
    from langchain_community.vectorstores import Chroma

from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.documents import Document
from utils import load_config
try:
    from pydub import AudioSegment
except ImportError:
    pass

# =========================
# 경로 / 설정
# =========================
DB_PATH = "./db/chroma_db"
KNOWLEDGE_PATH = "./knowledge_base"
CACHE_DIR = "./db/cache"
MANIFEST_PATH = os.path.join(CACHE_DIR, "manifest.json")
FAILED_PATH = os.path.join(CACHE_DIR, "failed_files.json")

EMBED_MODEL_NAME = "models/gemini-embedding-2-preview"

SUPPORTED_TEXT_EXTS = {".md", ".txt"}
SUPPORTED_PDF_EXTS = {".pdf"}
SUPPORTED_IMAGE_EXTS = {".png", ".jpg", ".jpeg"}
SUPPORTED_VIDEO_EXTS = {".mp4", ".mpeg"}
SUPPORTED_AUDIO_EXTS = {".mp3", ".wav"}

ALL_SUPPORTED_EXTS = SUPPORTED_TEXT_EXTS | SUPPORTED_PDF_EXTS | SUPPORTED_IMAGE_EXTS | SUPPORTED_VIDEO_EXTS | SUPPORTED_AUDIO_EXTS

DEFAULT_CHUNK_SIZE = 2200
DEFAULT_CHUNK_OVERLAP = 120
MIN_CHUNK_LENGTH = 80
DEFAULT_EMBED_RPM = 90
DEFAULT_BATCH_SIZE = 64


# =========================
# 유틸
# =========================
def ensure_dir(path: str):
    os.makedirs(path, exist_ok=True)

def now_iso() -> str:
    return datetime.now().isoformat(timespec="seconds")

def sha256_of_file(file_path: str) -> str:
    h = hashlib.sha256()
    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()

def sha256_of_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8", errors="ignore")).hexdigest()

def safe_relpath(path: str, start: str) -> str:
    return os.path.relpath(path, start).replace("\\", "/")

def normalize_text(text: str) -> str:
    text = text.replace("\x00", " ")
    text = text.replace("\u200b", " ")
    text = re.sub(r"\r\n?", "\n", text)
    text = re.sub(r"[ \t]+", " ", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()

def load_json(path: str, default):
    if not os.path.exists(path):
        return default
    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return default

def save_json(path: str, data):
    ensure_dir(os.path.dirname(path))
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def is_quota_error(exc: Exception) -> bool:
    s = str(exc).lower()
    return (
        "429" in s or "resourceexhausted" in s or "quota" in s or "rate limit" in s or "too many requests" in s
    )


# =========================
# Rate Limiter
# =========================
class RateLimiter:
    def __init__(self, rpm: int, safety_margin: float = 0.9):
        self.limit = max(1, int(rpm * safety_margin))
        self.calls = deque()

    def wait(self):
        now = time.time()
        while self.calls and now - self.calls[0] >= 60:
            self.calls.popleft()

        if len(self.calls) >= self.limit:
            sleep_for = 60 - (now - self.calls[0]) + 0.3
            if sleep_for > 0:
                print(f"⏳ RPM 보호 대기: {sleep_for:.1f}초")
                time.sleep(sleep_for)
        self.calls.append(time.time())

def retry_with_backoff(
    func,
    max_retries: int = 6,
    initial_delay: float = 3.0,
    backoff_factor: float = 2.0,
    jitter: float = 1.0
):
    delay = initial_delay
    for attempt in range(1, max_retries + 1):
        try:
            return func()  # 불필요한 가변 인자(*args, kwargs) 제거 및 직관적 호출로 변경
        except Exception as e:
            if not is_quota_error(e):
                raise

            if attempt >= max_retries:
                raise

            sleep_time = delay + random.uniform(0, jitter)
            print(f"⚠️ 429/Quota 감지. {sleep_time:.1f}초 후 재시도 ({attempt}/{max_retries})")
            time.sleep(sleep_time)
            delay *= backoff_factor

            
# =========================
# 본체
# =========================
class UnityRAG:
    def __init__(self, api_key_input=None, embed_rpm: int = DEFAULT_EMBED_RPM, batch_size: int = DEFAULT_BATCH_SIZE, chunk_size: int = DEFAULT_CHUNK_SIZE, chunk_overlap: int = DEFAULT_CHUNK_OVERLAP):
        self.api_key = api_key_input
        if not self.api_key:
            config = load_config()
            self.api_key = config.get("api_key", "")

        self.client = None
        self.embedding_model = None
        self.vector_db = None

        self.embed_rpm = embed_rpm
        self.batch_size = batch_size
        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap
        self.rate_limiter = RateLimiter(rpm=self.embed_rpm, safety_margin=0.9)

        ensure_dir(CACHE_DIR)

        if not self.api_key:
            return

        self.client = genai.Client(api_key=self.api_key)
        self.embedding_model = GoogleGenerativeAIEmbeddings(
            model=EMBED_MODEL_NAME,
            google_api_key=self.api_key
        )
        self.vector_db = None

    def _load_db(self):
        if self.embedding_model is None:
            return
        ensure_dir(DB_PATH)
        self.vector_db = Chroma(persist_directory=DB_PATH, embedding_function=self.embedding_model)

    def _recreate_db(self):
        self._safe_delete_db_dir()
        ensure_dir(DB_PATH)
        self.vector_db = Chroma(persist_directory=DB_PATH, embedding_function=self.embedding_model)

    def _collect_files(self):
        all_files = []
        for root, _, files in os.walk(KNOWLEDGE_PATH):
            for name in files:
                ext = os.path.splitext(name)[1].lower()
                if ext in ALL_SUPPORTED_EXTS:
                    all_files.append(os.path.join(root, name))
        all_files.sort()
        return all_files

    def _load_text_file(self, file_path: str) -> str:
        encodings = ["utf-8", "utf-8-sig", "cp949", "euc-kr", "latin-1"]
        for enc in encodings:
            try:
                with open(file_path, "r", encoding=enc) as f:
                    return normalize_text(f.read())
            except Exception:
                continue
        return ""

    def _parse_pdf_pymupdf(self, file_path: str) -> str:
        text_parts = []
        try:
            doc = fitz.open(file_path)
            for page in doc:
                text_parts.append(page.get_text("text"))
            doc.close()
        except Exception: return ""
        return normalize_text("\n".join(text_parts))

    def _parse_pdf_pypdf(self, file_path: str) -> str:
        text_parts = []
        try:
            reader = PdfReader(file_path)
            for page in reader.pages:
                text_parts.append(page.extract_text() or "")
        except Exception: return ""
        return normalize_text("\n".join(text_parts))

    # [일반] 미디어 추출 함수
    def _extract_media_text(self, file_path: str) -> str:
        tmp_path = None
        try:
            print(f"📡 멀티모달 파일 전송 및 분석 중: {os.path.basename(file_path)}")
            ext = os.path.splitext(file_path)[1]
            with tempfile.NamedTemporaryFile(delete=False, suffix=ext) as tmp_file:
                tmp_path = tmp_file.name
            
            shutil.copy2(file_path, tmp_path)
            uploaded_file = self.client.files.upload(file=tmp_path)
            
            while uploaded_file.state.name == "PROCESSING":
                time.sleep(2)
                uploaded_file = self.client.files.get(name=uploaded_file.name)
            
            if uploaded_file.state.name == "FAILED": return ""

            prompt = (
                "이 미디어 파일의 내용을 RAG 지식 검색에 완벽하게 활용할 수 있도록 텍스트로 상세히 변환해줘. "
                "1. 동영상/오디오인 경우: 대화 내용 전체를 전사(Transcript)하고, 화면에 보이는 시각적 상황이나 이펙트를 묘사할 것. "
                "2. 이미지인 경우: 포함된 텍스트를 OCR처럼 모두 추출하고, 구조와 시각적 요소(다이어그램, 차트 등)를 상세히 설명할 것."
            )

            response = self.client.models.generate_content(model='gemini-3.1-flash-lite-preview', contents=[uploaded_file, prompt])
            self.client.files.delete(name=uploaded_file.name)
            return normalize_text(response.text)
        except Exception as e:
            print(f"❌ 멀티모달 분석 실패: {e}")
            return ""
        finally:
            if tmp_path and os.path.exists(tmp_path):
                try: os.remove(tmp_path)
                except Exception: pass

    # [신규] 기술/개발/노드 전용 팩트 기반 추출 함수 (추론 엄격 차단 + 검색 맥락 보존)
    def _extract_technical_media(self, file_path: str) -> str:
        tmp_path = None
        try:
            print(f"📡 [기술/노드 전용] 멀티모달 파일 분석 중: {os.path.basename(file_path)}")
            ext = os.path.splitext(file_path)[1]
            filename = os.path.basename(file_path) # 파일명 추출
            
            with tempfile.NamedTemporaryFile(delete=False, suffix=ext) as tmp_file:
                tmp_path = tmp_file.name
            
            shutil.copy2(file_path, tmp_path)
            uploaded_file = self.client.files.upload(file=tmp_path)
            
            while uploaded_file.state.name == "PROCESSING":
                time.sleep(2)
                uploaded_file = self.client.files.get(name=uploaded_file.name)
            
            if uploaded_file.state.name == "FAILED": return ""

            # [CRITICAL FIX] 검색용 요약(허용)과 노드 추출(엄격 통제)의 분리
            prompt = (
                f"이 미디어 파일(이름: {filename})은 유니티 셰이더 그래프, 블루프린트 등 비주얼 스크립팅/코딩 작업 화면입니다. "
                "RAG 검색 시스템이 이 영상의 목적을 찾을 수 있도록 다음 두 가지 지침을 엄격히 분리해서 작성해줘:\n\n"
                "1. [목적 요약]: 파일명과 영상 초반/후반의 결과물(시각적 형태)을 바탕으로, 이 영상이 '어떤 기능이나 이펙트(예: 실루엣, 포탈 등)'를 다루는지 1~2줄로 요약할 것.\n"
                "2. [노드 팩트 나열 - 절대 준수 사항]: 구현 세부 로직을 설명할 때는 절대로 작동 원리를 스스로 유추하여 지어내지 마십시오. "
                "오직 화면에 명확히 보이는 노드의 이름(Text)과 값, 연결선(Link) 상태만 팩트 기반으로 나열하십시오. "
                "화면에 명시적으로 적혀있지 않은 연산 노드(예: Subtract, Add 등)를 임의로 추가하면 치명적인 오류가 발생합니다."
            )

            response = self.client.models.generate_content(model='gemini-3.1-flash-lite-preview', contents=[uploaded_file, prompt])
            self.client.files.delete(name=uploaded_file.name)
            return normalize_text(response.text)
        except Exception as e:
            print(f"❌ 기술 미디어 분석 실패: {e}")
            return ""
        finally:
            if tmp_path and os.path.exists(tmp_path):
                try: os.remove(tmp_path)
                except Exception: pass
# [신규] 긴 오디오 파일을 70초 단위로 분할하여 텍스트를 추출하고 병합하는 함수
    def _extract_long_audio(self, file_path: str) -> str:
        try:
            from pydub import AudioSegment
        except ImportError:
            print("❌ pydub 라이브러리가 설치되지 않아 오디오 분할이 불가능합니다. (pip install pydub)")
            return ""

        try:
            print(f"🔊 긴 오디오 파일 분석 준비 중: {os.path.basename(file_path)}")
            audio = AudioSegment.from_file(file_path)
            chunk_length_ms = 70 * 1000  # API 제한(80초)을 고려하여 안전하게 70초 단위로 분할
            chunks = [audio[i:i + chunk_length_ms] for i in range(0, len(audio), chunk_length_ms)]

            full_transcripts = []
            print(f"총 {len(audio)/1000:.1f}초의 오디오를 {len(chunks)}개의 조각으로 분할하여 분석합니다.")

            for idx, chunk in enumerate(chunks, start=1):
                tmp_path = None
                try:
                    ext = os.path.splitext(file_path)[1]
                    with tempfile.NamedTemporaryFile(delete=False, suffix=ext) as tmp_file:
                        tmp_path = tmp_file.name
                    
                    # 조각난 오디오를 임시 파일로 내보내기
                    chunk.export(tmp_path, format=ext.replace(".", ""))
                    
                    print(f"  -> 📡 [{idx}/{len(chunks)}] 번째 조각 전송 및 묘사 추출 중...")
                    uploaded_file = self.client.files.upload(file=tmp_path)
                    
                    while uploaded_file.state.name == "PROCESSING":
                        time.sleep(2)
                        uploaded_file = self.client.files.get(name=uploaded_file.name)
                    
                    if uploaded_file.state.name == "FAILED":
                        continue

                    prompt = (
                        "이 오디오 조각을 RAG 지식 검색에 활용할 수 있도록 텍스트로 상세히 분석해줘. "
                        "1. 대화가 있다면 전사(Transcript)할 것. "
                        "2. [음악/BGM인 경우 절대 준수]: 단순히 '평화롭다'는 식의 묘사를 넘어, 수석 음악 감독의 시각으로 기술적 분석을 수행할 것. "
                        "사용된 메인 악기(Lead Instruments), 대략적인 템포(BPM), 리듬의 질감, 장르(예: 판타지 오케스트라, 칩튠, 로파이 등), "
                        "그리고 곡을 구성하는 지배적인 음향적 특징(Acoustic features)을 매우 구체적인 영문 음악 용어를 섞어서 묘사하라."
                    )

                    response = self.client.models.generate_content(model='gemini-3.1-flash-lite-preview', contents=[uploaded_file, prompt])
                    self.client.files.delete(name=uploaded_file.name)
                    
                    # 각 조각의 텍스트를 리스트에 누적
                    full_transcripts.append(f"--- [오디오 파트 {idx}] ---\n{response.text.strip()}")

                except Exception as e:
                    print(f"❌ 오디오 조각 {idx} 분석 실패: {e}")
                finally:
                    if tmp_path and os.path.exists(tmp_path):
                        try: os.remove(tmp_path)
                        except Exception: pass
            
            # 모든 조각의 텍스트를 하나의 거대한 텍스트로 병합하여 반환
            return normalize_text("\n\n".join(full_transcripts))

        except Exception as e:
            print(f"❌ 긴 오디오 처리 실패: {e}")
            return ""


    def _load_document_text(self, file_path: str) -> str:
            ext = os.path.splitext(file_path)[1].lower()

            if ext in SUPPORTED_TEXT_EXTS:
                return self._load_text_file(file_path)

            if ext in SUPPORTED_PDF_EXTS:
                text = self._parse_pdf_pymupdf(file_path)
                if len(text) >= 50:
                    return text
                text = self._parse_pdf_pypdf(file_path)
                if len(text) >= 50:
                    return text
                # 두 방법 모두 실패 → 스캔본으로 간주, Gemini OCR fallback
                print(f"⚠️ 텍스트 추출 실패, Gemini OCR로 재시도: {os.path.basename(file_path)}")
                return self._extract_pdf_via_gemini_ocr(file_path)

            '''if ext in SUPPORTED_PDF_EXTS:
                text = self._parse_pdf_pymupdf(file_path)
                if len(text) >= 50: return text
                return self._parse_pdf_pypdf(file_path)'''
                
            # 👇 오디오 파일 전용 라우팅 추가
            if ext in SUPPORTED_AUDIO_EXTS:
                return self._extract_long_audio(file_path)
                
            if ext in SUPPORTED_IMAGE_EXTS | SUPPORTED_VIDEO_EXTS:
                tech_keywords = ["ase", "셰이더", "이펙트", "코드", "노드", "블루프린트", "shader", "code", "node", "개발"]
                filename_lower = os.path.basename(file_path).lower()
                
                if any(kw in filename_lower for kw in tech_keywords):
                    return self._extract_technical_media(file_path)
                else:
                    return self._extract_media_text(file_path)

            return ""

    def _split_document(self, doc: Document):
        splitter = RecursiveCharacterTextSplitter(
            chunk_size=self.chunk_size,
            chunk_overlap=self.chunk_overlap,
            separators=["\n## ", "\n### ", "\n#### ", "\n\n", "\n", ". ", " ", ""]
        )
        return splitter.split_documents([doc])

    def _dedupe_chunks(self, chunks):
        seen, result = set(), []
        for chunk in chunks:
            text = normalize_text(chunk.page_content)
            if len(text) < MIN_CHUNK_LENGTH: continue
            text_hash = sha256_of_text(text)
            if text_hash in seen: continue
            seen.add(text_hash)
            chunk.page_content = text
            result.append(chunk)
        return result

    def _make_chunk_ids(self, source_rel: str, chunks):
        base = hashlib.md5(source_rel.encode("utf-8")).hexdigest()
        return [f"{base}:{i}" for i in range(len(chunks))]

    def _load_manifest(self): return load_json(MANIFEST_PATH, {})
    def _save_manifest(self, manifest): save_json(MANIFEST_PATH, manifest)
    def _load_failed_files(self): return set(load_json(FAILED_PATH, {"failed_files": []}).get("failed_files", []))
    def _save_failed_files(self, failed_files_set): save_json(FAILED_PATH, {"failed_files": sorted(list(failed_files_set))})

    def _delete_ids_if_exist(self, ids):
        if not ids or self.vector_db is None: return
        try: self.vector_db.delete(ids=ids)
        except Exception as e: print(f"⚠️ 기존 ID 삭제 스킵: {e}")

    def _add_documents_in_batches(self, docs, ids):
        if not docs: return
        total = len(docs)
        batches = math.ceil(total / self.batch_size)
        for batch_idx in range(batches):
            start = batch_idx * self.batch_size
            end = min(start + self.batch_size, total)
            batch_docs, batch_ids = docs[start:end], ids[start:end]
            self.rate_limiter.wait()
            def _add(): self.vector_db.add_documents(batch_docs, ids=batch_ids)
            retry_with_backoff(_add)
            print(f"✅ 임베딩 저장 완료: {end}/{total}")

    def _build_file_documents(self, file_path: str):
        source_rel = safe_relpath(file_path, KNOWLEDGE_PATH)
        text = self._load_document_text(file_path)
        if not text: return [], []

        doc = Document(page_content=text, metadata={"source": source_rel, "source_path": file_path, "indexed_at": now_iso()})
        chunks = self._dedupe_chunks(self._split_document(doc))
        for idx, chunk in enumerate(chunks): chunk.metadata["chunk_index"] = idx
        return chunks, self._make_chunk_ids(source_rel, chunks)

    # [수정됨] rebuild_type 파라미터 추가
    def ingest_knowledge(self, full_rebuild: bool = False, only_failed: bool = False, target_exts: set = None, rebuild_type: bool = False):
        if not self.embedding_model: return "❌ API Key가 설정되지 않았습니다."
        if not os.path.exists(KNOWLEDGE_PATH): return "❌ knowledge_base 폴더가 없습니다."

        files = self._collect_files()
        if not files: return "❌ 처리할 파일이 없습니다."

        manifest = self._load_manifest()
        failed_files = self._load_failed_files()

        if full_rebuild:
            print("🧨 전체 재구축 시작")
            self._recreate_db()
            manifest, failed_files = {}, set()
        else:
            if self.vector_db is None: self._load_db()
            if self.vector_db is None: self._recreate_db()

        # [핵심 로직] 특정 유형만 초기화(백지화) 후 진행
        if rebuild_type and target_exts and not full_rebuild:
            print(f"🧨 부분 유형 완전 초기화 시작: {target_exts}")
            relpaths_to_delete = []
            for rel, item in manifest.items():
                ext = os.path.splitext(rel)[1].lower()
                if ext in target_exts:
                    relpaths_to_delete.append(rel)
            
            for rel in relpaths_to_delete:
                self._delete_ids_if_exist(manifest.get(rel, {}).get("chunk_ids", []))
                manifest.pop(rel, None)
                failed_files.discard(rel)
                
            self._save_manifest(manifest)
            self._save_failed_files(failed_files)
            print(f"✅ DB에서 해당 유형 기록 삭제 완료: {len(relpaths_to_delete)}건")

        # 삭제된 파일 동기화
        current_relpaths = {safe_relpath(p, KNOWLEDGE_PATH) for p in files}
        manifest_relpaths = set(manifest.keys())

        deleted_files = sorted(list(manifest_relpaths - current_relpaths))
        if deleted_files:
            for rel in deleted_files:
                self._delete_ids_if_exist(manifest.get(rel, {}).get("chunk_ids", []))
                manifest.pop(rel, None)
                failed_files.discard(rel)

        if target_exts:
            files_to_process = [f for f in files if os.path.splitext(f)[1].lower() in target_exts]
        else:
            files_to_process = files

        targets, skipped = [], 0
        for file_path in files_to_process:
            rel = safe_relpath(file_path, KNOWLEDGE_PATH)
            if only_failed and rel not in failed_files:
                skipped += 1; continue

            file_hash = sha256_of_file(file_path)
            old = manifest.get(rel)
            
            if not full_rebuild and not only_failed and old and old.get("sha256") == file_hash:
                skipped += 1; continue
                
            targets.append((file_path, rel, file_hash))

        if only_failed and not targets: return "✅ 실패 파일 재시도 대상이 없습니다."
        if not targets: return "✅ 모든 파일이 최신 상태입니다. (업데이트할 대상 없음)"

        processed, failed, total_new_chunks = 0, 0, 0

        for idx, (file_path, rel, file_hash) in enumerate(targets, start=1):
            print(f"\n[{idx}/{len(targets)}] 처리 중: {rel}")
            try:
                old_ids = manifest.get(rel, {}).get("chunk_ids", [])
                if old_ids: self._delete_ids_if_exist(old_ids)

                chunks, chunk_ids = self._build_file_documents(file_path)
                if not chunks: raise ValueError("유효한 텍스트/데이터 추출 실패")

                self._add_documents_in_batches(chunks, chunk_ids)

                manifest[rel] = {"sha256": file_hash, "chunk_ids": chunk_ids, "chunk_count": len(chunk_ids), "updated_at": now_iso()}
                failed_files.discard(rel)
                processed += 1
                total_new_chunks += len(chunk_ids)
                self._save_manifest(manifest)
                self._save_failed_files(failed_files)
                print(f"✅ 완료: {rel} / 청크 {len(chunk_ids)}개")

            except Exception as e:
                failed += 1
                failed_files.add(rel)
                self._save_failed_files(failed_files)
                print(f"❌ 실패: {rel}\n   사유: {e}")
                if is_quota_error(e):
                    self._save_manifest(manifest)
                    self._save_failed_files(failed_files)
                    return f"⚠️ API 제한 중단됨. (성공: {processed}, 신규 청크: {total_new_chunks})"

        self._save_manifest(manifest)
        self._save_failed_files(failed_files)
        
        target_info = "전체" if not target_exts else "부분 유형"
        return f"✅ 완료 [{target_info}] (대상: {len(targets)}, 처리: {processed}, 스킵: {skipped}, 실패: {failed}, 청크: {total_new_chunks})"

    def retrieve_context(self, query, k=3):
        if not self.vector_db: self._load_db()
        if not self.vector_db: return ""
        try:
            docs = self.vector_db.similarity_search(query, k=k)
            return "\n\n".join([f"--- [참고: {d.metadata.get('source', 'Unknown')}] ---\n{d.page_content}" for d in docs])
        except Exception as e: return f"검색 오류: {e}"

    def get_status(self):
        manifest = self._load_manifest()
        failed_files = self._load_failed_files()
        total_chunk_count = sum(int(item.get("chunk_count", 0)) for item in manifest.values())
        return {
            "db_exists": os.path.exists(os.path.join(DB_PATH, "chroma.sqlite3")),
            "indexed_files": len(manifest),
            "failed_files": len(failed_files),
            "total_chunks": total_chunk_count,
            "knowledge_files": len(self._collect_files()),
        }   

    def _close_db(self):
        try:
            if self.vector_db is not None: self.vector_db = None
        except Exception: pass
        gc.collect()
        time.sleep(0.5)

    def _safe_delete_db_dir(self, retries=5, delay=1.0):
        self._close_db()
        if not os.path.exists(DB_PATH): return
        last_error = None
        for attempt in range(retries):
            try:
                shutil.rmtree(DB_PATH)
                return
            except Exception as e:
                last_error = e
                time.sleep(delay)
        raise last_error
    
    def _extract_pdf_via_gemini_ocr(self, file_path: str) -> str:
        try:
            doc = fitz.open(file_path)
            all_text = []

            for page_num, page in enumerate(doc):
                mat = fitz.Matrix(2.0, 2.0)
                pix = page.get_pixmap(matrix=mat)
                img_bytes = pix.tobytes("png")

                import base64
                img_b64 = base64.standard_b64encode(img_bytes).decode("utf-8")

                try:
                    response = self.client.models.generate_content(
                        model='gemini-3.1-flash-lite-preview',
                        contents=[
                            {
                                "parts": [
                                    {
                                        "inline_data": {
                                            "mime_type": "image/png",
                                            "data": img_b64
                                        }
                                    },
                                    {
                                        "text": (
                                            "이 PDF 페이지에서 텍스트를 그대로 추출해줘 (OCR). "
                                            "원본 구조(제목, 단락, 코드블록 등)를 최대한 유지하고, "
                                            "설명이나 요약 없이 텍스트만 출력해."
                                        )
                                    }
                                ]
                            }
                        ]
                    )

                    # ✅ response.text가 None일 경우 candidates에서 직접 추출
                    page_text = None
                    if response.text is not None:
                        page_text = response.text.strip()
                    elif response.candidates:
                        parts = response.candidates[0].content.parts
                        page_text = "".join(p.text for p in parts if hasattr(p, "text") and p.text).strip()

                    if page_text:
                        all_text.append(f"--- [페이지 {page_num + 1}] ---\n{page_text}")
                    else:
                        print(f"⚠️ 페이지 {page_num + 1}: 텍스트 없음 (이미지만 있는 페이지일 수 있음)")

                except Exception as e:
                    print(f"⚠️ 페이지 {page_num + 1} OCR 실패, 스킵: {e}")
                    continue

                self.rate_limiter.wait()

            doc.close()
            result = normalize_text("\n\n".join(all_text))
            print(f"✅ Gemini OCR 완료: 총 {len(all_text)}페이지 추출")
            return result

        except Exception as e:
            print(f"❌ Gemini OCR 실패: {e}")
            return ""
        