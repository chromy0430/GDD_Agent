import os
import re
import json
import time
import glob
import math
import shutil
import random
import hashlib
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

def retry_with_backoff(func, *args, max_retries=6, initial_delay=3.0, backoff_factor=2.0, jitter=1.0, **kwargs):
    delay = initial_delay
    for attempt in range(1, max_retries + 1):
        try:
            return func(*args, **kwargs)
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

    def _extract_media_text(self, file_path: str) -> str:
        try:
            print(f"📡 멀티모달 파일 전송 및 분석 중: {os.path.basename(file_path)}")
            uploaded_file = self.client.files.upload(file=file_path)
            
            while uploaded_file.state.name == "PROCESSING":
                time.sleep(2)
                uploaded_file = self.client.files.get(name=uploaded_file.name)
            
            if uploaded_file.state.name == "FAILED":
                return ""

            prompt = (
                "이 미디어 파일의 내용을 RAG 지식 검색에 완벽하게 활용할 수 있도록 텍스트로 상세히 변환해줘. "
                "1. 동영상/오디오인 경우: 대화 내용 전체를 전사(Transcript)하고, 화면에 보이는 시각적 상황이나 이펙트를 묘사할 것. "
                "2. 이미지인 경우: 포함된 텍스트를 OCR처럼 모두 추출하고, 구조와 시각적 요소(다이어그램, 차트 등)를 상세히 설명할 것."
            )

            response = self.client.models.generate_content(
                model='gemini-3.1-flash-lite-preview',
                contents=[uploaded_file, prompt]
            )
            
            self.client.files.delete(name=uploaded_file.name)
            return normalize_text(response.text)
        except Exception as e:
            print(f"❌ 멀티모달 분석 실패: {e}")
            return ""

    def _load_document_text(self, file_path: str) -> str:
        ext = os.path.splitext(file_path)[1].lower()

        if ext in SUPPORTED_TEXT_EXTS:
            return self._load_text_file(file_path)

        if ext in SUPPORTED_PDF_EXTS:
            text = self._parse_pdf_pymupdf(file_path)
            if len(text) >= 50: return text
            return self._parse_pdf_pypdf(file_path)
            
        if ext in SUPPORTED_IMAGE_EXTS | SUPPORTED_VIDEO_EXTS | SUPPORTED_AUDIO_EXTS:
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

    # 타겟 확장자(target_exts) 파라미터 추가
    def ingest_knowledge(self, full_rebuild: bool = False, only_failed: bool = False, target_exts: set = None):
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

        # 삭제된 파일 동기화 (전체 파일 기준)
        current_relpaths = {safe_relpath(p, KNOWLEDGE_PATH) for p in files}
        manifest_relpaths = set(manifest.keys())

        deleted_files = sorted(list(manifest_relpaths - current_relpaths))
        if deleted_files:
            for rel in deleted_files:
                self._delete_ids_if_exist(manifest.get(rel, {}).get("chunk_ids", []))
                manifest.pop(rel, None)
                failed_files.discard(rel)

        # target_exts가 있을 경우, 작업 대상 큐를 해당 확장자 파일로만 축소
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
        return f"✅ 완료 [{target_info}] (대상: {len(files_to_process)}, 처리: {processed}, 스킵: {skipped}, 실패: {failed}, 청크: {total_new_chunks})"

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