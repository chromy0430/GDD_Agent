import os
import json
import streamlit as st

from rag_utils import UnityRAG, MANIFEST_PATH, FAILED_PATH, DB_PATH
from utils import render_sidebar_settings

st.set_page_config(page_title="관리자 설정", layout="wide")


def load_json(path, default):
    if not os.path.exists(path):
        return default
    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return default


def get_lightweight_status():
    manifest = load_json(MANIFEST_PATH, {})
    failed_data = load_json(FAILED_PATH, {"failed_files": []})
    failed_files = failed_data.get("failed_files", [])

    total_chunks = sum(int(v.get("chunk_count", 0)) for v in manifest.values())
    db_exists = os.path.exists(os.path.join(DB_PATH, "chroma.sqlite3"))

    knowledge_files = 0
    if os.path.exists("./knowledge_base"):
        for root, _, files in os.walk("./knowledge_base"):
            for file in files:
                ext = os.path.splitext(file)[1].lower()
                if ext in [".md", ".txt", ".pdf"]:
                    knowledge_files += 1

    return {
        "db_exists": db_exists,
        "indexed_files": len(manifest),
        "failed_files": len(failed_files),
        "total_chunks": total_chunks,
        "knowledge_files": knowledge_files,
    }


def main():
    st.title("⚙️ 시스템 관리")

    api_key, _, _ = render_sidebar_settings()

    st.divider()
    st.header("📚 RAG 지식 베이스 관리")

    status = get_lightweight_status()

    col1, col2, col3, col4, col5 = st.columns(5)
    col1.metric("DB 존재", "✅ 있음" if status["db_exists"] else "❌ 없음")
    col2.metric("knowledge_base 파일 수", status["knowledge_files"])
    col3.metric("색인 완료 파일 수", status["indexed_files"])
    col4.metric("실패 파일 수", status["failed_files"])
    col5.metric("총 청크 수", status["total_chunks"])

    st.write("### 🚀 작업 실행")

    col_a, col_b, col_c = st.columns(3)

    if col_a.button("➕ 증분 업데이트", type="primary", use_container_width=True):
        if not api_key:
            st.error("API Key가 없습니다.")
            return

        with st.spinner("변경된 파일만 분석하여 벡터 DB를 업데이트하는 중입니다..."):
            try:
                rag = UnityRAG(api_key_input=api_key)
                result_msg = rag.ingest_knowledge(full_rebuild=False, only_failed=False)
                st.success(result_msg)
            except Exception as e:
                st.error(f"오류 발생: {e}")

    if col_b.button("🔁 실패 파일만 재시도", use_container_width=True):
        if not api_key:
            st.error("API Key가 없습니다.")
            return

        with st.spinner("이전에 실패했던 파일만 다시 시도하는 중입니다..."):
            try:
                rag = UnityRAG(api_key_input=api_key)
                result_msg = rag.ingest_knowledge(full_rebuild=False, only_failed=True)
                st.success(result_msg)
            except Exception as e:
                st.error(f"오류 발생: {e}")

    if col_c.button("🧨 전체 재구축", use_container_width=True):
        if not api_key:
            st.error("API Key가 없습니다.")
            return

        with st.spinner("모든 문서를 다시 분석하여 DB를 새로 구축하는 중입니다..."):
            try:
                rag = UnityRAG(api_key_input=api_key)
                result_msg = rag.ingest_knowledge(full_rebuild=True, only_failed=False)
                st.success(result_msg)
            except Exception as e:
                st.error(f"오류 발생: {e}")


if __name__ == "__main__":
    main()