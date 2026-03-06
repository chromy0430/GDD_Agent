import json
import re
from io import StringIO

import streamlit as st
import google.generativeai as genai

from utils import log_usage, render_sidebar_settings
from rag_utils import UnityRAG


# ==========================================
# 1. 설정
# ==========================================
st.set_page_config(layout="wide", page_title="유니티 코드 리뷰어")


# ==========================================
# 2. 유틸
# ==========================================
def read_file_content(uploaded_file):
    try:
        stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
        return stringio.read()
    except Exception as e:
        return f"Error: {e}"


def extract_json_block(text: str):
    """
    모델 응답에서 JSON 객체만 최대한 안전하게 추출
    1) ```json ... ```
    2) 일반 텍스트 안의 { ... }
    """
    if not text:
        return None

    fenced = re.search(r"```json\s*(\{.*?\})\s*```", text, re.DOTALL)
    if fenced:
        try:
            return json.loads(fenced.group(1))
        except Exception:
            pass

    raw = re.search(r"(\{.*\})", text, re.DOTALL)
    if raw:
        candidate = raw.group(1)
        try:
            decoder = json.JSONDecoder()
            obj, _ = decoder.raw_decode(candidate)
            return obj
        except Exception:
            pass

    return None


def extract_csharp_block(text: str) -> str:
    """
    모델이 규칙을 어기고 별도 ```csharp 블록을 내놓은 경우 fallback
    """
    if not text:
        return ""

    code_match = re.search(r"```csharp\s*(.*?)\s*```", text, re.DOTALL | re.IGNORECASE)
    if code_match:
        return code_match.group(1).strip()

    generic_code_match = re.search(r"```(?:cs|c#)?\s*(.*?)\s*```", text, re.DOTALL | re.IGNORECASE)
    if generic_code_match:
        return generic_code_match.group(1).strip()

    return ""


def normalize_review_result(data: dict, raw_text: str) -> dict:
    """
    파싱된 JSON을 UI가 기대하는 형태로 보정
    """
    if not isinstance(data, dict):
        data = {}

    score = data.get("score", 0)
    summary = data.get("summary", "요약이 제공되지 않았습니다.")
    issues = data.get("issues", [])
    review_comment = data.get("review_comment", "리뷰 코멘트가 제공되지 않았습니다.")
    refactored_code = data.get("refactored_code", "")

    if not isinstance(score, int):
        try:
            score = int(score)
        except Exception:
            score = 0

    if not isinstance(issues, list):
        issues = []

    cleaned_issues = []
    for issue in issues:
        if not isinstance(issue, dict):
            continue
        cleaned_issues.append({
            "severity": str(issue.get("severity", "Info")),
            "line": str(issue.get("line", "?")),
            "description": str(issue.get("description", "설명이 없습니다."))
        })

    if not refactored_code:
        refactored_code = extract_csharp_block(raw_text)

    return {
        "score": max(0, min(100, score)),
        "summary": str(summary),
        "issues": cleaned_issues,
        "review_comment": str(review_comment),
        "refactored_code": str(refactored_code).strip(),
    }


def build_prompt(code_content: str, related_knowledge: str) -> str:
    return f"""
당신은 Unity 6.3 (LTS) 엔진 아키텍트이자 퍼포먼스 최적화 전문가입니다.
입력된 C# 코드를 **Unity 6 최신 스펙**과 **Zero-GC 원칙**에 따라 리뷰하고 리팩토링해야 합니다.

[참고 문서 (RAG Context)]
{related_knowledge}

[작업 절차]
1. 코드를 줄 단위로 분석하여 GC 발생 지점, 레거시 API, 구조적 결함을 찾으십시오.
2. 가능하면 다음 방향으로 개선하십시오.
   - Coroutine -> Awaitable (Unity 6 문맥에 맞을 때만)
   - LINQ/New in Update -> 할당 최소화, 캐싱, 풀링
   - GetComponent 반복 호출 -> Cached Reference
   - 문자열 보간 / 문자열 연결 -> GC 관점에서 검토
3. 문제점은 severity, line, description으로 구조화하십시오.
4. 전체 리팩토링 코드를 제공하십시오.
5. 불필요한 설명문, 마크다운 코드블록, JSON 외 텍스트는 출력하지 마십시오.

[출력 형식]
반드시 JSON 객체 하나만 출력하십시오.
절대 ```json, ```csharp, ### 같은 마크다운을 출력하지 마십시오.

{{
  "score": 0~100 사이 정수,
  "summary": "평가 요약 (한 줄)",
  "issues": [
    {{
      "severity": "Critical/Warning/Info",
      "line": "관련 라인 번호",
      "description": "구체적인 문제점"
    }}
  ],
  "review_comment": "기술적 조언 및 수정 이유",
  "refactored_code": "리팩토링된 전체 C# 코드 문자열"
}}

[입력 코드]
{code_content}
"""


# ==========================================
# 3. 메인
# ==========================================
def main():
    st.title("💻 유니티 C# 코드 리뷰 & 최적화 봇")
    st.markdown(
        """
작성한 C# 스크립트를 붙여넣거나 업로드하세요.  
**메모리 최적화(GC), 성능 이슈, 구조 개선, 가독성** 관점에서 분석하고 리팩토링합니다.
"""
    )

    api_key, _, model_name = render_sidebar_settings()

    with st.sidebar:
        st.caption("🔍 주요 점검 항목")
        st.caption("- Update / FixedUpdate 내 GC 발생")
        st.caption("- 고비용 API 반복 호출")
        st.caption("- 이벤트 / 델리게이트 사용 비용")
        st.caption("- 강한 결합, 책임 분리 부족")
        st.caption("- 네이밍, 가독성, 유지보수성")

    input_method = st.radio("입력 방식", ["직접 붙여넣기", "C# 파일 업로드 (.cs)"], horizontal=True)

    code_content = ""

    if input_method == "직접 붙여넣기":
        code_content = st.text_area(
            "C# 코드 입력",
            height=320,
            placeholder="""using UnityEngine;

public class Player : MonoBehaviour
{
    void Update()
    {
        Debug.Log("HP: " + 100);
    }
}"""
        )
    else:
        uploaded_file = st.file_uploader("C# 스크립트 파일", type=["cs"])
        if uploaded_file:
            code_content = read_file_content(uploaded_file)
            with st.expander("파일 내용 확인"):
                st.code(code_content, language="csharp")

    if st.button("🚀 코드 리뷰 및 리팩토링 시작", type="primary"):
        if not api_key:
            st.warning("API Key가 필요합니다.")
            return

        if not code_content or len(code_content.strip()) < 10:
            st.warning("분석할 코드를 입력해주세요.")
            return

        genai.configure(api_key=api_key)
        model = genai.GenerativeModel(model_name)

        rag = UnityRAG(api_key)
        with st.spinner("📚 관련 Unity 문서를 검색 중입니다..."):
            related_knowledge = rag.retrieve_context(code_content, k=3)

        prompt = build_prompt(code_content, related_knowledge)

        with st.spinner("코드를 분석하고 리팩토링하는 중입니다..."):
            try:
                log_usage("코드 리뷰 봇")
                response = model.generate_content(prompt)
                raw_text = response.text if hasattr(response, "text") else ""

                parsed = extract_json_block(raw_text)
                if not parsed:
                    st.error("응답에서 JSON을 추출하지 못했습니다.")
                    with st.expander("응답 원문 보기"):
                        st.code(raw_text)
                    return

                result = normalize_review_result(parsed, raw_text)

                st.divider()

                # 1. 점수 및 요약
                c1, c2 = st.columns([1, 3])
                with c1:
                    score = result["score"]
                    score_color = "red" if score < 50 else "orange" if score < 80 else "green"
                    st.markdown(
                        f"<h1 style='color:{score_color}; text-align:center;'>{score}점</h1>",
                        unsafe_allow_html=True
                    )
                with c2:
                    st.info(f"**총평:** {result['summary']}")

                # 2. 상세 탭
                tab1, tab2, tab3, tab4 = st.tabs(
                    ["🚨 발견된 문제", "✨ 리팩토링 코드", "📝 상세 리뷰", "🔎 원문 응답"]
                )

                with tab1:
                    if not result["issues"]:
                        st.success("발견된 주요 문제가 없습니다.")
                    else:
                        for issue in result["issues"]:
                            severity = issue.get("severity", "Info")
                            severity_icon = (
                                "🔴" if severity == "Critical"
                                else "🟡" if severity == "Warning"
                                else "🔵"
                            )
                            with st.expander(f"{severity_icon} [{severity}] {issue.get('description', '')}"):
                                st.write(f"**예상 위치:** Line {issue.get('line', '?')}")
                                st.write(f"**내용:** {issue.get('description', '')}")

                with tab2:
                    st.markdown("### ✅ 개선된 코드")
                    if result["refactored_code"]:
                        st.code(result["refactored_code"], language="csharp")
                        st.caption("우측 상단의 복사 버튼을 눌러 바로 유니티에 붙여넣으세요.")
                    else:
                        st.warning("리팩토링 코드가 응답에 포함되지 않았습니다.")

                with tab3:
                    st.markdown("### 👨‍💻 엔지니어 코멘트")
                    st.write(result["review_comment"])

                with tab4:
                    st.code(raw_text)

            except Exception as e:
                st.error(f"분석 중 오류 발생: {e}")


if __name__ == "__main__":
    main()