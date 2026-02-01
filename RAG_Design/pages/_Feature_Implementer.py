import streamlit as st
import google.generativeai as genai
from utils import log_usage, render_sidebar_settings
from rag_utils import UnityRAG

# ==========================================
# 1. 설정
# ==========================================
st.set_page_config(layout="wide", page_title="기능 구현 코딩 봇")

def main():
    st.title("💻 유니티 기능 구현 어시스턴트 (Feature Implementer)")
    api_key, _, model_name = render_sidebar_settings()

    st.markdown("""
    **"이 기능 어떻게 구현하나요?"** 라고 물어보세요.
    구축된 **Unity 매뉴얼(RAG)** 을 검색하여, 공식 문서 기반의 **신뢰할 수 있는 C# 코드**를 작성해드립니다.
    """)

    # 채팅 기록 초기화
    if "implement_chat_history" not in st.session_state:
        st.session_state.implement_chat_history = []

    # 이전 대화 출력
    for message in st.session_state.implement_chat_history:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # 사용자 입력 처리
    if query := st.chat_input("질문 예: 캐릭터가 벽타기(Wall Run)를 하는 기능을 구현해줘."):
        if not api_key:
            st.error("설정에서 API Key를 먼저 입력해주세요.")
            return

        # 1. 사용자 메시지 표시
        st.session_state.implement_chat_history.append({"role": "user", "content": query})
        with st.chat_message("user"):
            st.markdown(query)

        # 2. RAG 검색 (지식 베이스 활용)
        rag = UnityRAG(api_key)
        with st.spinner("📚 Unity 매뉴얼에서 관련 API와 예제를 찾는 중..."):
            # 검색 정확도를 위해 키워드 보정
            search_context = rag.retrieve_context(f"Unity C# Implementation API Example: {query}", k=4)

        # 3. AI 응답 생성
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel(model_name)

        system_prompt = f"""
        당신은 Unity 6.3 LTS 전문 클라이언트 개발자입니다.
        사용자의 요구사항을 구현하기 위한 **실제 작동하는 C# 스크립트**를 작성하세요.

        [검색된 Unity 공식 문서 (RAG Context)]
        {search_context}

        [작성 원칙]
        1. **코드 중심:** 불필요한 서론을 줄이고, 바로 복사해서 쓸 수 있는 `MonoBehaviour` 코드를 제공하세요.
        2. **최신 문법:** 검색된 문서에 나온 최신 API(예: New Input System, Physics.RaycastNonAlloc 등)를 우선 사용하세요.
        3. **주석 설명:** 코드의 주요 로직마다 한글 주석으로 원리를 설명하세요.
        4. **사용법 가이드:** 코드를 작성한 후, 에디터에서 컴포넌트를 어떻게 세팅해야 하는지(예: Layer 설정, Rigidbody 추가 등) 짧게 덧붙이세요.
        """

        full_prompt = f"{system_prompt}\n\n[사용자 요청]: {query}"

        with st.chat_message("assistant"):
            message_placeholder = st.empty()
            full_response = ""
            
            try:
                # 스트리밍 출력
                response = model.generate_content(full_prompt, stream=True)
                for chunk in response:
                    full_response += chunk.text
                    message_placeholder.markdown(full_response + "▌")
                
                message_placeholder.markdown(full_response)
                
                # 기록 저장
                st.session_state.implement_chat_history.append({"role": "assistant", "content": full_response})
                log_usage("기능 구현 봇")

            except Exception as e:
                st.error(f"오류 발생: {e}")

if __name__ == "__main__":
    main()