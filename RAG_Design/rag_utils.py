import os
import shutil
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_community.document_loaders import DirectoryLoader, TextLoader, PyPDFLoader
# langchain_text_splitters 패키지를 명시적으로 사용
from langchain_text_splitters import RecursiveCharacterTextSplitter
# 설정
DB_PATH = "./db/chroma_db"
KNOWLEDGE_PATH = "./knowledge_base"

class UnityRAG:
    def __init__(self, api_key):
        self.embedding_model = GoogleGenerativeAIEmbeddings(
            model="models/embedding-001", 
            google_api_key=api_key
        )
        self.vector_db = None
        self._load_db()

    def _load_db(self):
        """기존 DB가 있으면 로드, 없으면 새로 생성"""
        if os.path.exists(DB_PATH) and os.listdir(DB_PATH):
            self.vector_db = Chroma(persist_directory=DB_PATH, embedding_function=self.embedding_model)
        else:
            self.vector_db = None # 데이터 주입 필요

    def ingest_knowledge(self):
        """knowledge_base 폴더의 문서를 읽어 벡터 DB화 (업데이트 시 실행)"""
        if not os.path.exists(KNOWLEDGE_PATH):
            os.makedirs(KNOWLEDGE_PATH)
            return "지식 베이스 폴더가 비어있습니다."

        # 1. 문서 로드 (Markdown, PDF, TXT 지원)
        loaders = {
            ".md": DirectoryLoader(KNOWLEDGE_PATH, glob="**/*.md", loader_cls=TextLoader),
            ".txt": DirectoryLoader(KNOWLEDGE_PATH, glob="**/*.txt", loader_cls=TextLoader),
            ".pdf": DirectoryLoader(KNOWLEDGE_PATH, glob="**/*.pdf", loader_cls=PyPDFLoader),
        }

        documents = []
        for ext, loader in loaders.items():
            try:
                documents.extend(loader.load())
            except Exception as e:
                print(f"{ext} 로드 중 오류: {e}")

        if not documents:
            return "로딩된 문서가 없습니다."

        # 2. 청크 분할 (코드/기술 문서는 맥락 유지가 중요하므로 넉넉하게)
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=1500,
            chunk_overlap=200,
            separators=["\n## ", "\n\n", "\n", " ", ""]
        )
        chunks = text_splitter.split_documents(documents)

        # 3. 벡터 DB 저장 (기존 DB 삭제 후 재생성 - 데이터 무결성 위해)
        if os.path.exists(DB_PATH):
            shutil.rmtree(DB_PATH)
        
        self.vector_db = Chroma.from_documents(
            documents=chunks,
            embedding=self.embedding_model,
            persist_directory=DB_PATH
        )
        return f"✅ 지식 베이스 구축 완료! (문서 {len(documents)}개, 청크 {len(chunks)}개)"

    def retrieve_context(self, query, k=3):
        """질문과 관련된 가장 유사한 문서 내용을 반환"""
        if not self.vector_db:
            return "" # DB가 없으면 빈 문자열 반환

        # 유사도 검색
        docs = self.vector_db.similarity_search(query, k=k)
        
        # 검색된 내용을 하나의 문자열로 합침
        context_text = "\n\n".join([f"--- [참고 자료: {d.metadata['source']}] ---\n{d.page_content}" for d in docs])
        return context_text