import streamlit as st
import os
from rag_utils import UnityRAG
from utils import render_sidebar_settings

st.set_page_config(page_title="관리자 설정", layout="wide")

def main():
    st.title("⚙️ 시스템 관리")
    
    # API 키 설정
    api_key, _, _ = render_sidebar_settings()
    
    st.divider()
    st.header("📚 RAG 지식 베이스 관리")

    # DB 상태 확인
    db_exists = os.path.exists("./db/chroma_db") and len(os.listdir("./db/chroma_db")) > 0
    st.metric("벡터 DB 상태", "✅ 연결됨" if db_exists else "❌ 없음 (구축 필요)")

    st.write("### 🚀 지식 베이스 구축")
    st.info("버튼을 누르면 모든 문서를 읽고 DB를 새로 만듭니다. (문서 양에 따라 시간이 소요됩니다)")
    
    if st.button("🧠 지식 베이스 구축하기 (Rebuild)", type="primary"):
        if not api_key:
            st.error("API Key가 없습니다.")
            return

        rag = UnityRAG(api_key)
        
        with st.spinner("🚀 문서를 분석하고 DB를 구축하는 중입니다... (잠시만 기다려주세요)"):
            try:
                # 인자 없이 호출 (원래 방식)
                result_msg = rag.ingest_knowledge()
                st.success(result_msg)
                st.balloons()
            except Exception as e:
                st.error(f"오류 발생: {e}")

    # (선택) 문서 목록 미리보기
    with st.expander("📂 학습 대상 파일 목록 보기"):
        kb_files = []
        for root, dirs, files in os.walk("./knowledge_base"):
            for file in files:
                kb_files.append(file)
        st.write(kb_files)

if __name__ == "__main__":
    main()