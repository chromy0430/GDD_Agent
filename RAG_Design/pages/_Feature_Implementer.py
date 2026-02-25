import streamlit as st
import google.generativeai as genai
from io import StringIO
from utils import log_usage, render_sidebar_settings
from rag_utils import UnityRAG

# ==========================================
# 1. 설정
# ==========================================
st.set_page_config(layout="wide", page_title="기능 구현 및 리팩토링")

def read_code_file(uploaded_file):
    """업로드된 파일을 문자열로 변환"""
    try:
        stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
        return stringio.read()
    except Exception as e:
        return f"Error reading file: {e}"

def main():
    st.title("💻 유니티 기능 구현 & 리팩토링 (Feature Implementer)")
    api_key, _, model_name = render_sidebar_settings()

    # 탭 분리: 신규 구현 vs 리팩토링
    tab1, tab2 = st.tabs(["✨ 신규 기능 구현 (Chat)", "🛠 코드 리팩토링 (Multi-File)"])

    # ==========================================
    # TAB 1: 신규 기능 구현 (기존 로직 유지)
    # ==========================================
    with tab1:
        st.markdown("""
        **"이 기능 어떻게 구현하나요?"** 라고 물어보세요.
        Unity 매뉴얼(RAG) 기반의 **신뢰할 수 있는 C# 코드**를 작성해드립니다.
        """)

        if "implement_chat_history" not in st.session_state:
            st.session_state.implement_chat_history = []

        for message in st.session_state.implement_chat_history:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])

        if query := st.chat_input("질문 예: 캐릭터가 벽타기(Wall Run)를 하는 기능을 구현해줘."):
            if not api_key:
                st.error("설정에서 API Key를 먼저 입력해주세요.")
                return

            st.session_state.implement_chat_history.append({"role": "user", "content": query})
            with st.chat_message("user"):
                st.markdown(query)

            rag = UnityRAG(api_key)
            with st.spinner("📚 Unity 매뉴얼에서 관련 API와 예제를 찾는 중..."):
                search_context = rag.retrieve_context(f"Unity C# Implementation API Example: {query}", k=4)

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
            4. **사용법 가이드:** 코드를 작성한 후, 에디터 세팅법을 짧게 덧붙이세요.
            """

            full_prompt = f"{system_prompt}\n\n[사용자 요청]: {query}"

            with st.chat_message("assistant"):
                message_placeholder = st.empty()
                full_response = ""
                
                try:
                    response = model.generate_content(full_prompt, stream=True)
                    for chunk in response:
                        full_response += chunk.text
                        message_placeholder.markdown(full_response + "▌")
                    
                    message_placeholder.markdown(full_response)
                    st.session_state.implement_chat_history.append({"role": "assistant", "content": full_response})
                    log_usage("기능 구현 봇 (New)")

                except Exception as e:
                    st.error(f"오류 발생: {e}")

    # ==========================================
    # TAB 2: 레거시 코드 리팩토링 (다중 파일 지원)
    # ==========================================
    with tab2:
        st.header("🛠 Legacy to Unity 6.3 Migration")
        st.markdown("""
        구버전 Unity 코드(.cs)들을 업로드하세요. (복수 선택 가능)
        **RAG(지식 베이스)**를 참조하여 **Unity 6.3 LTS 최신 문법**으로 변환합니다.
        """)

        # [수정] accept_multiple_files=True 활성화
        uploaded_files = st.file_uploader(
            "코드 파일 업로드 (.cs, .txt, .md)", 
            type=["cs", "txt", "md"], 
            accept_multiple_files=True
        )
        
        if uploaded_files and st.button("🚀 리팩토링 시작 (Refactor)", type="primary"):
            if not api_key:
                st.warning("API Key가 필요합니다.")
                return

            # 1. 여러 파일을 하나의 컨텍스트로 병합
            combined_code_content = ""
            file_names = []
            
            for file in uploaded_files:
                content = read_code_file(file)
                combined_code_content += f"\n\n--- [File: {file.name}] ---\n{content}"
                file_names.append(file.name)

            # 토큰 제한 체크 (대략적인 문자 수 제한)
            if len(combined_code_content) > 50000:
                st.warning(f"전체 코드 양이 너무 많습니다. (현재 약 {len(combined_code_content)}자). 파일을 나누어 올려주세요.")
                return

            st.info(f"📂 총 {len(uploaded_files)}개의 파일({', '.join(file_names)})을 분석합니다.")

            # 2. RAG 검색 (마이그레이션 가이드 검색)
            rag = UnityRAG(api_key)
            with st.spinner("🔍 Unity 6 마이그레이션 가이드 및 대체 API 검색 중..."):
                # 코드 전체에서 키워드를 추출하는 대신, "Migration Guide" 자체를 검색하되
                # 코드에 포함된 주요 레거시 키워드(WWW, FindObjectOfType 등)가 있다면 힌트로 사용
                query_hint = combined_code_content[:1000].replace("\n", " ")
                search_context = rag.retrieve_context(f"Unity 6 migration legacy api upgrade guide rules: {query_hint}", k=4)

            # 3. 프롬프트 구성
            genai.configure(api_key=api_key)
            model = genai.GenerativeModel(model_name)

            refactor_prompt = f"""
            당신은 **Unity 6.3 LTS Migration Specialist**입니다.
            입력된 여러 개의 'Legacy Code' 파일들을 분석하여 상호 의존성을 고려해 **완전한 리팩토링**을 수행하십시오.

            [RAG Knowledge: Unity 6 변경점]
            {search_context}

            [리팩토링 필수 규칙 (Strict Rules)]
            1. **API 교체:** - `WWW` -> `UnityWebRequest`
               - `Object.FindObjectOfType` -> `Object.FindFirstObjectByType` (성능 최적화)
               - `Input.Get...` -> `UnityEngine.InputSystem` (New Input System)
            2. **비동기 처리:**
               - `Coroutine` -> `Awaitable` (Unity 6 표준) 또는 `UniTask`
            3. **메모리 최적화:**
               - `Update` 문 내부의 `new` 할당 금지.
               - 문자열 연결 시 `StringBuilder` 사용 또는 캐싱.
            4. **다중 파일 처리:**
               - 제공된 각 파일별로 리팩토링된 코드를 `--- [Refactored: 파일명] ---` 구분자를 써서 명확히 분리하여 출력할 것.

            [Legacy Code Files]
            {combined_code_content}
            """

            with st.spinner("코드를 최신 Unity 6.3 아키텍처로 변환 중..."):
                try:
                    response = model.generate_content(refactor_prompt)
                    
                    st.subheader("✅ 변환 결과")
                    st.markdown(response.text) # 마크다운 형식으로 출력
                    
                    log_usage("기능 구현 봇 (Refactor Multi)")
                except Exception as e:
                    st.error(f"리팩토링 실패: {e}")

if __name__ == "__main__":
    main()