import os
import shutil
import time
from google import genai
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_community.document_loaders import DirectoryLoader, TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.documents import Document

# 설정
DB_PATH = "./db/chroma_db"
KNOWLEDGE_PATH = "./knowledge_base"
MODEL_NAME = "gemini-2.5-flash" # 파싱용 모델

class UnityRAG:
    def __init__(self, api_key):
        self.api_key = api_key
        self.client = genai.Client(api_key=api_key) # Gemini 클라이언트 초기화
        self.embedding_model = GoogleGenerativeAIEmbeddings(
            model="models/embedding-001", 
            google_api_key=api_key
        )
        self.vector_db = None
        self._load_db()

    def _load_db(self):
        """기존 DB가 있으면 로드"""
        if os.path.exists(DB_PATH) and os.listdir(DB_PATH):
            self.vector_db = Chroma(persist_directory=DB_PATH, embedding_function=self.embedding_model)
        else:
            self.vector_db = None

    # [핵심 기능] Gemini를 이용해 PDF를 고품질 텍스트로 변환
    def _parse_pdf_with_gemini(self, file_path):
        """
        로컬 PDF를 Gemini에 업로드하고, 그 내용을 상세한 텍스트로 변환받습니다.
        이미지, 도표 분석이 포함됩니다.
        """
        try:
            # 1. 파일 업로드 (SDK v2 방식)
            print(f"📡 Gemini에 업로드 중: {file_path}")
            file_ref = self.client.files.upload(file=file_path)

            # 2. 처리 대기 (Active 상태 확인)
            while file_ref.state.name == "PROCESSING":
                time.sleep(1)
                file_ref = self.client.files.get(name=file_ref.name)
            
            if file_ref.state.name != "ACTIVE":
                print(f"❌ 파일 처리 실패: {file_path}")
                return None

            # 3. 텍스트 추출 요청
            prompt = """
            이 문서의 모든 내용을 매우 상세하게 텍스트로 추출해줘.
            특히 포함된 이미지, 도표, 그래프가 있다면 그 내용과 수치를 빠짐없이 묘사해줘.
            Markdown 형식으로 정리해줘.
            """
            response = self.client.models.generate_content(
                model=MODEL_NAME,
                contents=[file_ref, prompt]
            )
            
            # 4. 리소스 정리 (서버 파일 삭제) - 중요!
            # self.client.files.delete(name=file_ref.name) 
            # (필요시 주석 해제하여 사용, 쿼터 관리를 위해 삭제 권장)

            return response.text

        except Exception as e:
            print(f"⚠️ Gemini 파싱 중 오류 ({file_path}): {e}")
            return None

    def ingest_knowledge(self):
        """knowledge_base 폴더 처리"""
        if not os.path.exists(KNOWLEDGE_PATH):
            os.makedirs(KNOWLEDGE_PATH)
            return "지식 베이스 폴더가 비어있습니다."

        documents = []

        # 1. 텍스트/마크다운 처리 (기존 방식 유지 - 속도 빠름)
        txt_loaders = {
            ".md": DirectoryLoader(KNOWLEDGE_PATH, glob="**/*.md", loader_cls=TextLoader),
            ".txt": DirectoryLoader(KNOWLEDGE_PATH, glob="**/*.txt", loader_cls=TextLoader),
        }
        for ext, loader in txt_loaders.items():
            try:
                documents.extend(loader.load())
            except Exception as e:
                print(f"{ext} 로드 실패: {e}")

        # 2. PDF 처리 (Gemini 업로드 방식으로 변경)
        # 폴더 내의 모든 PDF를 찾습니다.
        import glob
        pdf_files = glob.glob(os.path.join(KNOWLEDGE_PATH, "**/*.pdf"), recursive=True)
        
        print(f"🔍 발견된 PDF 파일: {len(pdf_files)}개 (Gemini 정밀 분석 시작)")

        for pdf_path in pdf_files:
            # Gemini에게 내용을 읽어달라고 요청
            parsed_text = self._parse_pdf_with_gemini(pdf_path)
            
            if parsed_text:
                # LangChain Document 객체로 수동 변환
                doc = Document(
                    page_content=parsed_text,
                    metadata={"source": pdf_path}
                )
                documents.append(doc)
            else:
                # 실패 시 기존 PyPDFLoader로 백업 처리 가능 (선택 사항)
                print(f"⚠️ {pdf_path} Gemini 파싱 실패. 건너뜁니다.")

        if not documents:
            return "처리할 문서가 없습니다."

        # 3. 청크 분할 및 저장 (이후 과정 동일)
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=1500,
            chunk_overlap=200,
            separators=["\n## ", "\n\n", "\n", " ", ""]
        )
        chunks = text_splitter.split_documents(documents)

        if os.path.exists(DB_PATH):
            shutil.rmtree(DB_PATH)
        
        self.vector_db = Chroma.from_documents(
            documents=chunks,
            embedding=self.embedding_model,
            persist_directory=DB_PATH
        )
        return f"✅ 지식 베이스 구축 완료! (PDF 정밀 분석 포함, 총 {len(chunks)} 청크)"

    def retrieve_context(self, query, k=3):
        # ... (기존 동일) ...
        if not self.vector_db:
             return ""
        docs = self.vector_db.similarity_search(query, k=k)
        context_text = "\n\n".join([f"--- [참고 자료: {d.metadata['source']}] ---\n{d.page_content}" for d in docs])
        return context_text