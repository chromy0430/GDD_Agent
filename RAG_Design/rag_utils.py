import os
import shutil
import time
import glob
from google import genai
from langchain_google_genai import GoogleGenerativeAIEmbeddings
# 최신 패키지 호환성 (구버전/신버전 모두 대응)
try:
    from langchain_chroma import Chroma
except ImportError:
    from langchain_community.vectorstores import Chroma

from langchain_community.document_loaders import DirectoryLoader, TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.documents import Document
from utils import load_config

# 설정
DB_PATH = "./db/chroma_db"
KNOWLEDGE_PATH = "./knowledge_base"
MODEL_NAME = "gemini-3.1-flash-lite-preview" 

class UnityRAG:
    def __init__(self, api_key_input=None):
        # 1. API 키 로드
        self.api_key = api_key_input
        if not self.api_key:
            config = load_config()
            self.api_key = config.get("api_key", "")
        
        if not self.api_key:
            self.client = None
            self.embedding_model = None
            self.vector_db = None
            return

        # 2. 클라이언트 초기화
        self.client = genai.Client(api_key=self.api_key)
        self.embedding_model = GoogleGenerativeAIEmbeddings(
            model="models/gemini-embedding-001", 
            google_api_key=self.api_key
        )
        self.vector_db = None
        self._load_db()

    def _load_db(self):
        """기존 DB 로드"""
        if os.path.exists(DB_PATH) and os.listdir(DB_PATH):
            self.vector_db = Chroma(persist_directory=DB_PATH, embedding_function=self.embedding_model)
        else:
            self.vector_db = None

    def _parse_pdf_with_gemini(self, file_path):
        """Gemini를 이용한 PDF 파싱"""
        try:
            with open(file_path, "rb") as f:
                file_ref = self.client.files.upload(file=f, config={'mime_type': 'application/pdf'})

            # 처리 대기
            while file_ref.state.name == "PROCESSING":
                time.sleep(1)
                file_ref = self.client.files.get(name=file_ref.name)
            
            if file_ref.state.name != "ACTIVE": return None

            prompt = "이 문서의 내용을 마크다운 형식으로 상세히 추출해줘. 텍스트, 표, 이미지 설명을 모두 포함해."
            response = self.client.models.generate_content(
                model=MODEL_NAME, contents=[file_ref, prompt]
            )
            return response.text
            
        except Exception as e:
            error_msg = str(e)
            # [수정] 할당량 초과(429) 에러 감지 시 특수 시그널 반환
            if "429" in error_msg or "ResourceExhausted" in error_msg or "quota" in error_msg.lower():
                print(f"🛑 할당량 초과 감지 ({os.path.basename(file_path)}): 분석 중단 요청.")
                return "QUOTA_EXCEEDED"
            
            print(f"⚠️ PDF 파싱 오류 ({os.path.basename(file_path)}): {e}")
            return None

    def ingest_knowledge(self):
        """
        문서를 메모리에 로드 후 DB 구축 (할당량 초과 시 중단 후 저장 기능 추가)
        """
        if not self.embedding_model: return "❌ API Key가 설정되지 않았습니다."
        if not os.path.exists(KNOWLEDGE_PATH): return "지식 베이스 폴더가 없습니다."

        documents = []

        # 1. 텍스트/마크다운 파일 로드
        txt_files = []
        for ext in ["**/*.md", "**/*.txt"]:
            txt_files.extend(glob.glob(os.path.join(KNOWLEDGE_PATH, ext), recursive=True))
            
        print(f"📂 텍스트 파일 {len(txt_files)}개 처리 중...")
        for fp in txt_files:
            try:
                loader = TextLoader(fp, encoding='utf-8')
                documents.extend(loader.load())
            except:
                try: 
                    loader = TextLoader(fp, encoding='cp949')
                    documents.extend(loader.load())
                except: pass

        # 2. PDF 파일 처리 (Loop)
        pdf_files = glob.glob(os.path.join(KNOWLEDGE_PATH, "**/*.pdf"), recursive=True)
        print(f"📄 PDF 파일 {len(pdf_files)}개 분석 시작...")
        
        for i, pdf_path in enumerate(pdf_files):
            print(f"   [{i+1}/{len(pdf_files)}] PDF 처리: {os.path.basename(pdf_path)}")
            parsed_text = self._parse_pdf_with_gemini(pdf_path)
            
            # [수정] 할당량 초과 시그널을 받으면 루프를 즉시 멈춤
            if parsed_text == "QUOTA_EXCEEDED":
                print("🛑 API 할당량 소진으로 인해 PDF 분석을 조기 종료합니다. (현재까지 확보된 데이터로 DB를 구축합니다.)")
                break 
            
            if parsed_text:
                doc = Document(page_content=parsed_text, metadata={"source": pdf_path})
                documents.append(doc)
            
            time.sleep(2)

        if not documents:
            return "처리할 문서가 없습니다 (또는 모든 PDF 분석 실패)."

        # 3. 청크 분할 및 저장
        print(f"💾 벡터 DB 생성 시작... (문서 {len(documents)}개)")
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=1500, chunk_overlap=200)
        chunks = text_splitter.split_documents(documents)

        # [수정] DB 파일 잠금 해제 (Error Code 14 방지)
        self.vector_db = None 

        # 기존 DB 폴더 삭제
        if os.path.exists(DB_PATH):
            try:
                shutil.rmtree(DB_PATH)
            except Exception as e:
                print(f"⚠️ 기존 DB 삭제 실패 (잠금 문제일 수 있음, 덮어쓰기 시도): {e}")

        # DB 저장
        try:
            # 먼저 빈 DB 구조를 초기화합니다.
            self.vector_db = Chroma(
                embedding_function=self.embedding_model,
                persist_directory=DB_PATH
            )
            
            total_chunks = len(chunks)
            batch_size = 80 # 분당 제한(100회) 대비 안전 마진 설정
            
            # 청크 리스트를 batch_size만큼 잘라서 순차 처리
            for i in range(0, total_chunks, batch_size):
                batch_chunks = chunks[i : i + batch_size]
                
                # 내부 재시도 로직 (순간적인 네트워크 오류 방어)
                max_retries = 3
                for attempt in range(max_retries):
                    try:
                        self.vector_db.add_documents(batch_chunks)
                        print(f"✅ DB 배치 : {i + len(batch_chunks)} / {total_chunks}")
                        break # 성공 시 재시도 루프 탈출
                    except Exception as batch_e:
                        if attempt == max_retries - 1:
                            return f"❌ DB 저장 중 치명적 오류 발생 (Batch {i}): {batch_e}"
                        print(f"⚠️ 배치 저장 실패. 10초 대기 후 재시도... ({batch_e})")
                        time.sleep(10)

                # 마지막 배치가 아니라면 Rate Limit(429) 회피를 위해 카운트 리셋 시간(1분) 강제 대기
                if i + batch_size < total_chunks:
                    print(f"⏳ RPM 회피를 위해 62초 대기 중... (현재 진행률: {((i + len(batch_chunks)) / total_chunks) * 100:.1f}%)")
                    time.sleep(62) 

            return f"✅ 지식 베이스 구축 완료! (총 {len(chunks)} 청크 / 배치 처리 완료)"

        except Exception as e:
            return f"❌ DB 생성 중 오류 발생: {e}"

    # [복구됨] 검색 기능
    def retrieve_context(self, query, k=3):
        if not self.vector_db: self._load_db()
        if not self.vector_db: return ""
        try:
            docs = self.vector_db.similarity_search(query, k=k)
            return "\n\n".join([f"--- [참고: {d.metadata.get('source','Unknown')}] ---\n{d.page_content}" for d in docs])
        except Exception as e:
            return f"검색 오류: {e}"