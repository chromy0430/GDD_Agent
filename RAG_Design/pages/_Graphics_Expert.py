import streamlit as st
import google.generativeai as genai
import json
from utils import log_usage, render_sidebar_settings
from rag_utils import UnityRAG

# ==========================================
# 1. 설정 및 상수
# ==========================================
st.set_page_config(layout="wide", page_title="URP 그래픽스 전문가")

# ==========================================
# 2. 메인 로직
# ==========================================
def main():
    st.title("🎨 URP 테크니컬 아티스트 (Graphics Expert)")
    api_key, _, model_name = render_sidebar_settings()
    
    st.markdown("""
    **Unity URP 매뉴얼(RAG)**을 기반으로 쉐이더, 포스트 프로세싱, 렌더링 최적화 질문에 답해드립니다.
    예) *"모바일용 물 쉐이더 최적화 방법은?"*, *"Render Feature로 아웃라인 구현하려면?"*
    """)

    # 채팅 기록 초기화
    if "graphics_chat_history" not in st.session_state:
        st.session_state.graphics_chat_history = []

    # 채팅 UI 표시
    for message in st.session_state.graphics_chat_history:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # 사용자 입력
    if prompt := st.chat_input("그래픽스/렌더링 관련 질문을 입력하세요..."):
        if not api_key:
            st.error("API Key가 필요합니다.")
            return

        # 1. 사용자 메시지 표시
        st.session_state.graphics_chat_history.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        # 2. RAG 검색 (URP 특화)
        rag = UnityRAG(api_key)
        with st.spinner("📚 URP 매뉴얼과 렌더링 문서를 검색 중..."):
            # 검색 쿼리에 'URP', 'Rendering', 'Shader' 등의 키워드를 내부적으로 강조
            search_query = f"Unity URP Rendering Shader Graphics: {prompt}"
            context = rag.retrieve_context(search_query, k=4)

        # 3. Gemini 답변 생성
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel(model_name)
        
        system_prompt = f"""
        당신은 Unity URP(Universal Render Pipeline) 수석 테크니컬 아티스트(TA)입니다.
        사용자의 질문에 대해 **제공된 URP 매뉴얼(Context)**을 근거로 전문적인 답변을 제공하세요.

        [참고 문서 (RAG Context)]
        {context}

        [답변 가이드라인]
        1. **URP 전용 용어 사용:** Built-in 파이프라인 용어(예: Standard Shader) 대신 URP 용어(예: Lit Shader, Render Objects)를 사용하세요.
        2. **쉐이더/VFX:** Shader Graph 노드 구성이나 HLSL 코드가 필요하다면 구체적인 예시를 포함하세요.
        3. **최적화:** 성능(Draw Call, Batches)에 민감하게 답변하고, 모바일/콘솔 등 타겟 플랫폼에 맞는 설정을 제안하세요.
        4. **출처 명시:** 답변이 매뉴얼의 어떤 부분(예: Lighting.md)을 참고했는지 가능하다면 언급하세요.
        """

        full_prompt = f"{system_prompt}\n\n[사용자 질문]: {prompt}"

        with st.chat_message("assistant"):
            message_placeholder = st.empty()
            full_response = ""
            
            try:
                # 스트리밍 답변
                response = model.generate_content(full_prompt, stream=True)
                for chunk in response:
                    full_response += chunk.text
                    message_placeholder.markdown(full_response + "▌")
                
                message_placeholder.markdown(full_response)
                
                # 기록 저장
                st.session_state.graphics_chat_history.append({"role": "assistant", "content": full_response})
                log_usage("URP 그래픽스 봇")

            except Exception as e:
                st.error(f"답변 생성 실패: {e}")

if __name__ == "__main__":
    main()