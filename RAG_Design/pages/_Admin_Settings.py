import streamlit as st
import shutil
import os
from rag_utils import UnityRAG
from utils import render_sidebar_settings

st.set_page_config(page_title="관리자 설정", layout="wide")

def main():
    st.title("⚙️ 시스템 관리 및 지식 베이스 구축")
    
    # API 키 설정 (사이드바)
    api_key, _, _ = render_sidebar_settings()
    
    st.divider()
    
    st.header("📚 RAG 지식 베이스 관리")
    st.info("새로운 문서(Markdown, PDF)를 추가했다면, 반드시 아래 버튼을 눌러 DB를 갱신해야 합니다.")

    c1, c2 = st.columns([1, 2])
    
    with c1:
        # DB 상태 확인
        db_exists = os.path.exists("./db/chroma_db") and len(os.listdir("./db/chroma_db")) > 0
        st.metric("벡터 DB 상태", "✅ 연결됨" if db_exists else "❌ 없음 (구축 필요)")
        
        # 지식 베이스 폴더 확인
        kb_files = []
        for root, dirs, files in os.walk("./knowledge_base"):
            for file in files:
                if file.endswith((".md", ".txt", ".pdf")):
                    kb_files.append(os.path.join(root, file))
        
        st.metric("학습할 문서 수", f"{len(kb_files)} 개")

    with c2:
        st.write("### 🚀 지식 주입 (Ingestion)")
        st.caption("주의: 문서 양에 따라 수 분이 소요될 수 있습니다.")
        
        if st.button("🧠 지식 베이스 새로 구축하기 (Rebuild DB)", type="primary"):
            if not api_key:
                st.error("API Key가 설정되지 않았습니다.")
                return
            
            rag = UnityRAG(api_key)
            
            progress_bar = st.progress(0)
            status_text = st.empty()
            
            try:
                status_text.text("📂 기존 DB 정리 중...")
                # (rag_utils.py 내부에서 처리하지만, 확실하게 하기 위해)
                if os.path.exists("./db/chroma_db"):
                    # rag_utils의 ingest_knowledge가 shutil.rmtree를 수행하므로 호출만 하면 됨
                    pass
                
                status_text.text("📖 문서 읽기 및 벡터 변환 중 (Gemini Embedding)...")
                progress_bar.progress(30)
                
                # [핵심] DB 구축 실행
                result_msg = rag.ingest_knowledge()
                
                progress_bar.progress(100)
                st.success(result_msg)
                st.balloons()
                
            except Exception as e:
                st.error(f"오류 발생: {e}")
            finally:
                status_text.empty()

    # (선택) 문서 목록 미리보기
    with st.expander("📂 학습 대상 파일 목록 보기"):
        st.write(kb_files)

if __name__ == "__main__":
    main()