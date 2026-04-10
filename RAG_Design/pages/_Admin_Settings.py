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
    valid_extensions = {".md", ".txt", ".pdf", ".png", ".jpg", ".jpeg", ".mp4", ".mpeg", ".mp3", ".wav"}
    
    if os.path.exists("./knowledge_base"):
        for root, _, files in os.walk("./knowledge_base"):
            for file in files:
                ext = os.path.splitext(file)[1].lower()
                if ext in valid_extensions:
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
    
    # 멀티모달 임베딩 제약 사항 안내 (보스 지시사항 반영)
    with st.expander("ℹ️ 지원되는 파일 유형 및 임베딩 제약 사항", expanded=False):
        st.markdown("""
        `knowledge_base` 폴더에 넣을 수 있는 미디어 파일의 제약 사항입니다. 
        Gemini 2 Preview 모델의 제한을 따릅니다.

        * **이미지 (`image/png`, `image/jpeg`)**
            * 프롬프트당 최대 이미지 수: 6개
            * 최대 파일 크기: 제한 없음
        * **문서 (`application/pdf`, `.md`, `.txt`)**
            * 프롬프트당 최대 파일 수: 1개
            * 파일당 최대 페이지 수: 6페이지 (PDF)
        * **동영상 (`video/mpeg`, `video/mp4`)**
            * 최대 동영상 길이 (오디오 포함): 80초
            * 최대 동영상 길이 (오디오 제외): 120초
            * 프롬프트당 최대 동영상 수: 1개
        * **오디오 (`audio/mp3`, `audio/wav`)**
            * 프롬프트당 최대 오디오 길이: 80초
            * 프롬프트당 최대 오디오 파일 수: 1개
        
        > **💡 시스템 참고:** 오디오/비디오/이미지 파일은 Chroma DB에 적재되기 전, Gemini 모델을 통해 내용이 고도로 분석(전사 및 OCR)되어 텍스트 형태로 벡터화됩니다. 이를 통해 기존 텍스트 파일과 완벽히 동일한 검색 성능을 제공합니다.
        """)

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

        with st.spinner("변경된 파일만 분석하여 벡터 DB를 업데이트하는 중입니다... (미디어 파일은 다소 시간이 걸릴 수 있습니다)"):
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