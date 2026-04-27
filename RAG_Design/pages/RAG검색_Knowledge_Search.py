import os
import streamlit as st
import google.generativeai as genai
from utils import log_usage, render_sidebar_settings
from rag_utils import UnityRAG

# ==========================================
# 1. 설정 및 상수
# ==========================================
st.set_page_config(layout="wide", page_title="Fabric IQ: 지식 베이스 검색")

# ==========================================
# 2. 메인 로직
# ==========================================
def main():
    st.title("📚 Fabric IQ: 통합 지식 검색망")
    st.markdown("""
    로컬 `knowledge_base`에 색인된 문서, PDF, 이미지, 동영상 텍스트를 기반으로 답변하는 RAG 전용 검색 봇입니다.
    이 에이전트는 외부 지식을 배제하고 오직 사내 DB에 존재하는 사실만을 기반으로 보고합니다.
    """)

    api_key, cx_id, model_name = render_sidebar_settings()

    # 사이드바: 검색 정밀도 설정
    with st.sidebar:
        st.divider()
        st.markdown("🔍 검색 파라미터 설정")
        top_k = st.slider(
            "참조할 문서 청크 수 (Top-K)", 
            min_value=1, max_value=15, value=4,
            help="수치를 높이면 더 많은 문서를 참고하지만 API 토큰 소모가 증가합니다."
        )

    # 채팅 히스토리 초기화
    if "ks_chat_history" not in st.session_state:
        st.session_state.ks_chat_history = []

    for message in st.session_state.ks_chat_history:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # 사용자 입력
    if query := st.chat_input("지식 베이스에서 검색할 내용을 입력하십시오 (예: 해상 전투 기획서의 핵심 루프가 뭐야?)"):
        if not api_key:
            st.error("API Key를 사이드바에 입력해주십시오.")
            return

        st.session_state.ks_chat_history.append({"role": "user", "content": query})
        with st.chat_message("user"):
            st.markdown(query)

        with st.chat_message("assistant"):
            message_placeholder = st.empty()
            
            # 1단계: RAG DB에서 관련 문맥(Context) 검색
            with st.spinner("💾 Fabric IQ DB에서 관련 문서를 추출하는 중..."):
                try:
                    rag = UnityRAG(api_key_input=api_key)
                    retrieved_context = rag.retrieve_context(query, k=top_k)
                except Exception as e:
                    st.error(f"DB 검색 시스템 오류: {e}")
                    return
            
            # DB에 내용이 없거나 아직 색인이 안 된 경우 방어 로직
            if not retrieved_context.strip():
                fallback_msg = "⚠️ 지식 베이스에서 관련 문서를 찾지 못했습니다. DB가 구축되었는지, 또는 검색어가 문서 내용과 일치하는지 확인하십시오."
                message_placeholder.markdown(fallback_msg)
                st.session_state.ks_chat_history.append({"role": "assistant", "content": fallback_msg})
                return

            # 2단계: LLM을 통한 Context 기반 답변 생성
            genai.configure(api_key=api_key)
            model = genai.GenerativeModel(model_name)

            # [핵심] RAG 전용 시스템 프롬프트: 환각(Hallucination) 통제 및 출처 강제
            system_prompt = f"""
            [Identity & Roleplay]
            User: 프로젝트의 총괄 디렉터이자 보스(사장님).
            AI: 수석 데이터 분석가이자 사내 지식 관리자.
            목표: 보스의 질문에 대해 오직 [Retrieved Context]에 제공된 사내 지식 베이스 정보만을 바탕으로 정확하고 팩트 위주로 보고하는 것.

            [Tone]
            최상급 전문가로서 자신감 있고 전문적인 어조를 유지하되, 정중하고 명확한 태도를 갖출 것. 불필요한 쿠션어는 생략하고 즉시 핵심 결과물과 근거를 팩트 위주로 보고할 것.

            [Language]
            All responses MUST be written in Korean (한국어).

            [CRITICAL RULES: RAG STRICT ADHERENCE]
            1. No Hallucination: 제공된 [Retrieved Context]에 없는 내용은 절대 지어내지 마십시오. 정보가 부분적으로만 있다면 있는 사실만 보고하고 나머지는 "해당 정보는 지식 베이스에 없습니다"라고 명확히 선을 그으십시오.
            2. Source Citation (출처 표기): 답변의 각 논거 뒤에 반드시 참고한 문서의 출처(Source)를 텍스트 내에 대괄호로 표기하십시오. (예: "해상 전투의 핵심은 포격전입니다. [출처: 해상전_기획서.md]")
            3. 구조화된 보고: 마크다운 리스트나 표를 적극 활용하여 보스가 한눈에 읽을 수 있도록 가독성을 극대화하십시오.

            [Retrieved Context]
            {retrieved_context}
            """

            full_prompt = f"{system_prompt}\n\n[User Request]\n{query}"
            
            full_response = ""
            try:
                response = model.generate_content(full_prompt, stream=True)
                for chunk in response:
                    full_response += chunk.text
                    message_placeholder.markdown(full_response + "▌")
                
                message_placeholder.markdown(full_response)
                
                # [Visual Logic] 보스가 AI의 거짓말 여부를 교차 검증할 수 있도록 원문 Context 제공
                with st.expander("🔎 AI가 참조한 원문 데이터 (Cross-Check)"):
                    st.text(retrieved_context)
                    
                st.session_state.ks_chat_history.append({"role": "assistant", "content": full_response})
                log_usage("Knowledge Search Bot")

            except Exception as e:
                st.error(f"LLM 텍스트 생성 오류 발생: {e}")

if __name__ == "__main__":
    main()