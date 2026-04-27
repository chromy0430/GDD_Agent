import os
import streamlit as st
import google.generativeai as genai
from utils import log_usage, render_sidebar_settings

# ==========================================
# 1. 설정 및 상수
# ==========================================
st.set_page_config(layout="wide", page_title="Render Graph 전문가")
SAMPLE_FOLDER = "rendergraph_samples"

# ==========================================
# 2. 유틸리티 함수 (샘플 파일 읽기)
# ==========================================
def read_rendergraph_samples(folder_path):
    combined_samples = ""
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
        return ""

    # os.walk를 사용하여 모든 하위 폴더를 재귀적으로 탐색
    for root, dirs, files in os.walk(folder_path):
        for filename in files:
            filepath = os.path.join(root, filename)
            try:
                # .compute 및 셰이더 관련 확장자 통합 필터링
                if filename.lower().endswith((".cs", ".txt", ".md", ".shader", ".hlsl", ".cginc", ".compute")):
                    # 기준 폴더로부터의 상대 경로를 계산하여 폴더명(역할)을 파악 가능하도록 포매팅
                    relative_path = os.path.relpath(filepath, folder_path)
                    relative_path = relative_path.replace("\\", "/") # OS 호환성 처리
                    
                    with open(filepath, "r", encoding="utf-8") as f:
                        # LLM이 폴더명을 통해 역할을 유추할 수 있도록 상대 경로를 헤더로 제공
                        combined_samples += f"\n--- [{relative_path}] ---\n{f.read()}\n"
            except Exception as e:
                # 읽기 실패 시 중단하지 않고 다음 파일로 진행
                pass
                
    return combined_samples

# ==========================================
# 3. 메인 로직
# ==========================================
def main():
    st.title("🖌️ Unity 6.3 URP: Render Graph 제너레이터")
    api_key, cx_id, model_name = render_sidebar_settings()
    
    st.markdown("""
    `rendergraph_samples` 폴더에 저장된 Unity 6.3 URP **Render Graph 샘플 코드**를 바탕으로,
    새로운 커스텀 렌더 패스(Render Pass)와 렌더러 피처(Renderer Feature) 코드를 작성합니다.
    """)

    # 사이드바 샘플 상태 표시
    with st.sidebar:
        st.divider()
        st.markdown("**📂 학습된 샘플 코드 (Ground Truth)**")
        sample_content = read_rendergraph_samples(SAMPLE_FOLDER)
        if sample_content:
            st.code("\n".join(os.listdir(SAMPLE_FOLDER)), language=None)
        else:
            st.warning(f"'{SAMPLE_FOLDER}' 폴더를 생성하고 .cs 샘플 코드를 넣어주세요.")

    # 채팅 히스토리 초기화
    if "rg_chat_history" not in st.session_state:
        st.session_state.rg_chat_history = []

    for message in st.session_state.rg_chat_history:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # 사용자 입력
    if query := st.chat_input("구현할 Render Graph 기능을 입력하세요 (예: 특정 레이어만 흑백으로 렌더링하는 패스 구현해줘)"):
        if not api_key:
            st.error("API Key를 입력해주세요.")
            return
            
        if not sample_content:
            st.warning(f"참고할 샘플 코드가 없습니다. '{SAMPLE_FOLDER}'에 파일을 추가해주세요.")
            return

        st.session_state.rg_chat_history.append({"role": "user", "content": query})
        with st.chat_message("user"):
            st.markdown(query)

        genai.configure(api_key=api_key)
        model = genai.GenerativeModel(model_name)

        # 시스템 프롬프트: 사용자의 지시사항 및 학습 히스토리 엄격 적용
        system_prompt = f"""
        [Identity & Roleplay]
        User: 프로젝트의 총괄 디렉터이자 보스(사장님).
        AI: 10년 차 수석 그래픽스 개발자이자 테크니컬 아티스트(Technical Artist). Unity 6.3 URP 및 Render Graph의 최고 권위자.
        목표: 보스의 지시를 받아, 에디터에 복사 & 붙여넣기만 하면 즉시 프로덕션 환경에서 작동하는 100% 완벽한 코드를 보고하는 것.

        [Tone]
        최상급 전문가로서 자신감 있고 전문적인 어조를 유지하되, 보스에게 보고하는 형태의 정중하고 명확한 태도를 갖출 것. "제가 해보겠습니다", "노력하겠습니다" 같은 불필요한 쿠션어는 생략하고, 즉시 핵심 결과물(코드)과 기술적 근거만 팩트 위주로 보고할 것.

        [Language]
        All responses MUST be written in Korean (한국어).

        [Standards]
        Environment: Unity 6.3 LTS, URP, New Input System (if required).
        Focus: URP Render Graph API.
        Performance: Zero-GC 원칙 엄수. 매 프레임 발생하는 메모리 할당(new) 절대 금지. 캐싱 및 풀링(Pooling) 적극 활용.

        [CRITICAL: 100% COMPLETE CODE RULE]
        코드 작성 시 `// 추가 구현 필요`, `// ... (생략)`, `// TODO: Blit 로직 작성` 같은 플레이스홀더를 절대 사용하지 마십시오.
        Blit 연산, Material 할당, Buffer 해제, 렌더 패스 주입 등 기능 작동에 필요한 모든 세부 로직을 '단 1줄의 생략도 없이' 처음부터 끝까지 스스로 완벽하게 구현하여 제출해야 합니다. 코드는 즉시 컴파일 및 실행 가능해야 합니다.

        [Response Structure Requirements]
        1. Confidence Tags (Required): Attach at the beginning. Use [Reliable] (official docs/samples), [Warning] (uncertain/compatibility issues), or [Danger] (low reliability inference).
        2. Visual Logic Flow: Visualize data conversion. Format: [Input: A] -> (Process X: reason/basis) -> [Modified: A'] -> (Condition Y) -> [Output: B]
        3. Physical Analogy: Explain abstract Render Graph concepts (like TextureBuilder, CommandBuffer allocation) by comparing them to 'objects in the real world' (e.g., passing a memory buffer = handing over an empty canvas).
        4. C# 'ref' Keyword Learning: Whenever passing context structs (like RasterGraphContext) or large data structs, explicitly utilize the `ref` keyword in code examples. Explain the memory Trade-off and how it aids in future learning and zero-GC principles.
        5. Analysis Format: No overall summary. List only core technical differences and Trade-offs between options.
        6. Step-by-Step Application Guide: 작성된 코드를 Unity Editor에서 어떻게 적용하는지 보스가 쉽게 확인할 수 있도록 단계별(Step 1, Step 2...)로 상세히 안내할 것. (예: URP Universal Renderer Data 에셋에 Feature 추가, 머티리얼 세팅, 스크립트 연결 등)

        [Ground Truth Data - RENDER GRAPH SAMPLES]
        The user has provided the following validated Render Graph sample codes. This is your absolute source of truth for syntax and architecture.
        {sample_content}
        """

        full_prompt = f"{system_prompt}\n\n[User Request]\n{query}"

        with st.chat_message("assistant"):
            message_placeholder = st.empty()
            full_response = ""
            
            try:
                response = model.generate_content(full_prompt, stream=True)
                for chunk in response:
                    full_response += chunk.text
                    message_placeholder.markdown(full_response + "▌")
                
                message_placeholder.markdown(full_response)
                st.session_state.rg_chat_history.append({"role": "assistant", "content": full_response})
                log_usage("Render Graph 전문가 봇")

            except Exception as e:
                st.error(f"오류 발생: {e}")

if __name__ == "__main__":
    main()