import streamlit as st
import google.generativeai as genai
import os
import json
from io import StringIO
from utils import log_usage, render_sidebar_settings
from rag_utils import UnityRAG

# ==========================================
# 1. 설정 및 상수
# ==========================================
st.set_page_config(layout="wide", page_title="유니티 코드 리뷰어")
#MODEL_NAME = "gemini-2.5-flash-lite"
#CONFIG_FILE = "config.json"

# ==========================================
# 2. 유틸리티 함수
# ==========================================

def read_file_content(uploaded_file):
    try:
        stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
        return stringio.read()
    except Exception as e:
        return f"Error: {e}"

# ==========================================
# 3. 메인 로직
# ==========================================
def main():
    st.title("💻 유니티 C# 코드 리뷰 & 최적화 봇")
    st.markdown("""
    작성한 C# 스크립트를 붙여넣으세요. 
    **메모리 최적화(GC), 성능 이슈, SOLID 원칙** 관점에서 분석하고 코드를 수정해 드립니다.
    """)

    api_key, cx_id, model_name = render_sidebar_settings()

    with st.sidebar:        
        st.caption("🔍 **주요 점검 항목**")
        st.caption("- Update 내 GC 발생 (new, string)")
        st.caption("- 고비용 API (GetComponent, Find)")
        st.caption("- 스파게티 코드 & 강한 결합")
        st.caption("- 네이밍 컨벤션 & 가독성")
    

    # 입력 UI (파일 업로드 or 텍스트 입력)
    input_method = st.radio("입력 방식", ["직접 붙여넣기", "C# 파일 업로드 (.cs)"], horizontal=True)
    
    code_content = ""
    
    if input_method == "직접 붙여넣기":
        code_content = st.text_area("C# 코드 입력", height=300, placeholder="using UnityEngine;\n\npublic class Player : MonoBehaviour {\n    void Update() {\n        Debug.Log(\"HP: \" + 100);\n    }\n}")
    else:
        uploaded_file = st.file_uploader("C# 스크립트 파일", type=['cs'])
        if uploaded_file:
            code_content = read_file_content(uploaded_file)
            with st.expander("파일 내용 확인"):
                st.code(code_content, language='csharp')

    # 분석 버튼
    if st.button("🚀 코드 리뷰 및 리팩토링 시작", type="primary"):
        if not api_key:
            st.warning("API Key가 필요합니다.")
            return
        if not code_content or len(code_content.strip()) < 10:
            st.warning("분석할 코드를 입력해주세요.")
            return

        # Gemini 설정
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel(model_name)

        # [RAG 단계]
        rag = UnityRAG(api_key)
        
        # 사용자의 코드를 쿼리로 사용하여 관련 Unity 6 지식을 검색
        # (예: 코드가 Coroutine을 쓰면 Awaitable 문서를 찾아옴)
        related_knowledge = rag.retrieve_context(code_content, k=3)

        # 프롬프트 구성
        system_prompt = """당신은 Unity 6.3 (LTS) 엔진 아키텍트이자 퍼포먼스 최적화 전문가입니다.
        입력된 C# 코드를 **Unity 6 최신 스펙**과 **Zero-GC 원칙**에 따라 리뷰하고 리팩토링해야 합니다.

        [참고 문서 (RAG Context)]
        {related_knowledge}

        [작업 절차]
        1. **Deep Analysis:** 코드를 줄 단위로 분석하여 GC 발생 지점, 레거시 API, 구조적 결함을 찾으십시오.
        2. **Refactoring Strategy:** - `Coroutine` -> `Awaitable` (Unity 6)
           - `LINQ/New` in Update -> `NativeArray`, `Object Pooling`
           - `GetComponent` -> `Cached Reference`
        3. **Output Generation:** 아래 [출력 형식]을 엄격히 준수하십시오.

        [출력 형식]
        반드시 **JSON 블록**을 먼저 출력하고, 그 뒤에 **리팩토링된 전체 코드**를 마크다운으로 출력하세요.

        ```json
        {
            "score": 0~100 사이 정수,
            "summary": "평가 요약 (한 줄)",
            "issues": [
                {
                    "severity": "Critical/Warning/Info",
                    "line": "관련 라인 번호",
                    "description": "구체적인 문제점"
                }
            ],
            "review_comment": "기술적 조언 및 수정 이유"
        }
        ```

        ### Refactored Code
        ```csharp
        // 여기에 리팩토링된 전체 코드를 작성하세요.
        // 주석으로 변경 사유를 달아주세요.
        ```
        """

        # 레거시 프롬프트
        '''system_prompt = """
        당신은 15년 경력의 유니티(Unity) 수석 최적화 엔지니어이자 당신은 Unity 6.3 (LTS) 엔진 아키텍트이자 퍼포먼스 최적화 전문가이며, 코드 리뷰어입니다.
        입력된 C# 코드를 분석하여 성능, 메모리, 구조적 문제를 진단하고 개선된 코드를 제시하세요.        
        입력된 코드를 **Unity 6.3 최신 스펙**과 **Zero-GC(Garbage Collection) 원칙**에 따라 리뷰하고 리팩토링하세요.

        아래 [Reference Docs]를 참고하여, 입력된 코드를 최신 스펙(Unity 6) 및 GC-Free 원칙에 맞춰 리팩토링하세요.
        
        [Reference Docs (RAG 검색 결과)]
        {related_knowledge}
        
        [필수 점검 및 리팩토링 기준]
        1. **비동기 처리 (Unity 6.3):**
        - 레거시 `Coroutine`은 **`Awaitable`** 및 `async/await` 패턴으로 전면 교체하십시오.
        - `UniTask`가 있다면 UniTask를 사용한 비동기 방식을 사용해주세요.
        2. **렌더링 및 URP:**
        - 커스텀 렌더링 로직이 있다면 `ScriptableRenderPass` 대신 **`RenderGraph` API**를 사용하는 구조로 제안하십시오.
        - Material 제어 시 `MaterialPropertyBlock`을 사용하여 인스턴싱 드로우콜이 깨지지 않게 하십시오.
        3. **메모리 & GC 최적화 (Hot Path):**
        - `Update`, `FixedUpdate` 내부의 힙 할당(new, LINQ, Boxing)을 **엄격히 금지**합니다.
        - 컬렉션은 `List<T>` 대신 가능하다면 `NativeArray`나 `Span<T>` 활용을 고려하고, 재사용 가능한 버퍼 패턴을 적용하십시오.
        4. **Input System:**
        - `Input.Get...` 레거시 코드는 반드시 **`Input System Package`의 Action 기반 콜백**으로 변경하십시오.
        5. **SOLID 및 구조:** 객체지향 원칙 준수 여부와 유지보수성을 확인하세요.


        반드시 아래 JSON 포맷으로만 출력하세요. (마크다운 코드블록 없이)
        [출력 포맷 (JSON)]        
        {
            "score": 0~100 사이 정수,
            "summary": "Unity 6.3 호환성 및 GC 관점에서의 요약, 전체적인 평가 요약 (한 줄)",
            "issues": [
                {
                    "severity": "Critical(치명적) 또는 Warning(경고) 또는 Info(참고)",
                    "line": "관련 라인 번호 (추정)",
                    "description": "구체적인 문제점 설명"
                }
            ],
            "refactored_code": "Unity 6.3 API가 적용된, GC가 발생하지 않는 개선된 전체 C# 코드 (주석으로 변경 사항 설명 포함)",
            "review_comment": "리팩토링에 대한 상세한 설명과 조언, Awaitable 도입 이유, 구조 변경 사유 등 기술적 설명"
        }
        """'''
        
        full_prompt = [system_prompt, f"[Input Code]\n{code_content}"]

        with st.spinner("코드를 한 줄 한 줄 뜯어보는 중입니다..."):
            try:
                log_usage("코드 리뷰 봇")
                response = model.generate_content(full_prompt)
                result_text = response.text.replace("```json", "").replace("```", "").strip()
                #result = json.loads(result_text)
                result = json.loads(result_text, strict=False)

                # 결과 출력
                st.divider()
                
                # 1. 점수 및 요약
                c1, c2 = st.columns([1, 3])
                with c1:
                    score = result['score']
                    score_color = "red" if score < 50 else "orange" if score < 80 else "green"
                    st.markdown(f"<h1 style='color:{score_color}; text-align: center;'>{score}점</h1>", unsafe_allow_html=True)
                with c2:
                    st.info(f"**총평:** {result['summary']}")

                # 2. 상세 탭
                tab1, tab2, tab3 = st.tabs(["🚨 발견된 문제", "✨ 리팩토링 코드", "📝 상세 리뷰"])

                with tab1:
                    if not result['issues']:
                        st.success("발견된 주요 문제가 없습니다! 훌륭합니다.")
                    for issue in result['issues']:
                        severity_icon = "🔴" if issue['severity'] == "Critical" else "🟡" if issue['severity'] == "Warning" else "🔵"
                        with st.expander(f"{severity_icon} [{issue['severity']}] {issue['description']}"):
                            st.write(f"**예상 위치:** Line {issue.get('line', '?')}")
                            st.write(f"**내용:** {issue['description']}")

                with tab2:
                    st.markdown("### ✅ 개선된 코드")
                    st.code(result['refactored_code'], language='csharp')
                    st.caption("우측 상단의 복사 버튼을 눌러 바로 유니티에 붙여넣으세요.")

                with tab3:
                    st.markdown("### 👨‍💻 엔지니어 코멘트")
                    st.write(result['review_comment'])

            except Exception as e:
                st.error(f"분석 중 오류 발생: {e}")
                st.write("응답 원문:", response.text if 'response' in locals() else "없음")

if __name__ == "__main__":
    main()