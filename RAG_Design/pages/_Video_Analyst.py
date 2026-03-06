import os
import re
import json
import time
import html
import tempfile
import streamlit as st

from google import genai
from graphviz import Digraph

from utils import render_sidebar_settings, retry_with_backoff, log_usage
from rag_utils import UnityRAG


# =========================================================
# 1. 페이지 설정
# =========================================================
st.set_page_config(layout="wide", page_title="영상 분석 에이전트 (Video Reverse Engineer)")


# =========================================================
# 2. JSON / 텍스트 유틸
# =========================================================
def extract_json_block(text: str):
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
        try:
            return json.loads(raw.group(1))
        except Exception:
            pass

    return None


def safe_list(value):
    return value if isinstance(value, list) else []


def safe_dict(value):
    return value if isinstance(value, dict) else {}


def sanitize_text(value) -> str:
    if value is None:
        return ""
    return str(value).strip()


def normalize_port_name(port_name: str) -> str:
    return (
        str(port_name)
        .strip()
        .lower()
        .replace(" ", "_")
        .replace("-", "_")
        .replace(".", "_")
        .replace("/", "_")
    )


def html_escape(value) -> str:
    return html.escape(sanitize_text(value))


# =========================================================
# 3. 영상 업로드 / 대기
# =========================================================
@retry_with_backoff(max_retries=3, initial_delay=4)
def upload_video_to_gemini(uploaded_file, api_key):
    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp4") as tmp:
        tmp.write(uploaded_file.getvalue())
        tmp_path = tmp.name

    client = genai.Client(api_key=api_key)

    try:
        with st.spinner("📡 영상을 Gemini 서버로 전송 중입니다..."):
            file_ref = client.files.upload(file=tmp_path)
        return file_ref, client
    except Exception as e:
        st.error(f"업로드 실패: {e}")
        return None, None
    finally:
        if os.path.exists(tmp_path):
            os.remove(tmp_path)


def wait_for_files_active(client, files):
    st.info("⏳ 영상 처리 대기 중... (서버 인덱싱)")
    progress_bar = st.progress(0)

    total = max(len(files), 1)
    done = 0

    for name in (file.name for file in files):
        file = client.files.get(name=name)

        while file.state.name == "PROCESSING":
            time.sleep(2)
            file = client.files.get(name=name)

        if file.state.name != "ACTIVE":
            st.error(f"영상 처리 실패: {file.name} (상태: {file.state.name})")
            return False

        done += 1
        progress_bar.progress(int((done / total) * 100))

    st.success("✅ 영상 처리 완료! 분석을 시작합니다.")
    return True


# =========================================================
# 4. 포트 기반 Shader Graph 렌더링
# =========================================================
def get_node_fillcolor(node_type: str) -> str:
    type_colors = {
        "Property": "#FFF4CC",
        "Color": "#FFF4CC",
        "Vector1": "#FFF4CC",
        "Vector2": "#FFF4CC",
        "Vector3": "#FFF4CC",
        "Vector4": "#FFF4CC",
        "Float": "#FFF4CC",

        "Texture2D": "#DDEEFF",
        "Sample Texture 2D": "#DDEEFF",
        "SampleTexture2D": "#DDEEFF",
        "Tiling And Offset": "#E8F1FF",
        "UV": "#E8F5E9",
        "Time": "#DFF3F7",

        "Simple Noise": "#E1F5FE",
        "Gradient Noise": "#E1F5FE",
        "Noise": "#E1F5FE",

        "Multiply": "#F3E5F5",
        "Add": "#F3E5F5",
        "Subtract": "#F3E5F5",
        "Divide": "#F3E5F5",
        "Lerp": "#F3E5F5",
        "One Minus": "#F3E5F5",
        "Smoothstep": "#F3E5F5",
        "Saturate": "#F3E5F5",
        "Power": "#F3E5F5",

        "Fresnel Effect": "#FFE0E0",
        "FresnelEffect": "#FFE0E0",
        "Normal Strength": "#FFE9D6",

        "FragmentOutput": "#D7FFD9",
        "Master Stack": "#D7FFD9",
        "MasterStack": "#D7FFD9",
    }
    return type_colors.get(node_type, "#F5F5F5")


def build_html_port_cell(port_name: str, side: str) -> str:
    escaped_name = html_escape(port_name)
    port_id = f"{side}_{normalize_port_name(port_name)}"

    if side == "in":
        return (
            f'<TR>'
            f'<TD PORT="{port_id}" ALIGN="LEFT" BALIGN="LEFT" CELLPADDING="6">'
            f'◀ {escaped_name}'
            f'</TD>'
            f'</TR>'
        )

    return (
        f'<TR>'
        f'<TD PORT="{port_id}" ALIGN="RIGHT" BALIGN="RIGHT" CELLPADDING="6">'
        f'{escaped_name} ▶'
        f'</TD>'
        f'</TR>'
    )


def build_port_table_label(title: str, node_type: str, inputs: list, outputs: list, fillcolor: str) -> str:
    safe_title = html_escape(title)
    safe_type = html_escape(node_type)

    input_rows = "".join(build_html_port_cell(p, "in") for p in inputs) if inputs else (
        '<TR><TD CELLPADDING="6"> </TD></TR>'
    )
    output_rows = "".join(build_html_port_cell(p, "out") for p in outputs) if outputs else (
        '<TR><TD CELLPADDING="6"> </TD></TR>'
    )

    return (
        f'<'
        f'<TABLE BORDER="1" CELLBORDER="1" CELLSPACING="0" CELLPADDING="0" COLOR="#222222">'
        f'<TR>'
        f'<TD>'
        f'<TABLE BORDER="0" CELLBORDER="1" CELLSPACING="0" CELLPADDING="0">'
        f'{input_rows}'
        f'</TABLE>'
        f'</TD>'
        f'<TD BGCOLOR="{fillcolor}" CELLPADDING="10">'
        f'<TABLE BORDER="0" CELLBORDER="0" CELLSPACING="0" CELLPADDING="0">'
        f'<TR><TD ALIGN="CENTER"><B>{safe_title}</B></TD></TR>'
        f'<TR><TD ALIGN="CENTER">[{safe_type}]</TD></TR>'
        f'</TABLE>'
        f'</TD>'
        f'<TD>'
        f'<TABLE BORDER="0" CELLBORDER="1" CELLSPACING="0" CELLPADDING="0">'
        f'{output_rows}'
        f'</TABLE>'
        f'</TD>'
        f'</TR>'
        f'</TABLE>'
        f'>'
    )


def build_shader_graphviz(graph_data: dict) -> Digraph:
    dot = Digraph(comment="Shader Graph")
    dot.attr(rankdir="LR", splines="spline", nodesep="0.5", ranksep="1.0", bgcolor="white")
    dot.attr("graph", pad="0.25")
    dot.attr("node", shape="plaintext", fontname="Malgun Gothic", fontsize="11")
    dot.attr("edge", fontname="Malgun Gothic", fontsize="9", color="#222222")

    nodes = safe_list(graph_data.get("nodes"))
    edges = safe_list(graph_data.get("edges"))

    declared_node_ids = set()

    for node in nodes:
        node_id = sanitize_text(node.get("id"))
        if not node_id:
            continue

        node_type = sanitize_text(node.get("type", "Node"))
        title = sanitize_text(node.get("title", node_type))
        inputs = [sanitize_text(x) for x in safe_list(node.get("inputs")) if sanitize_text(x)]
        outputs = [sanitize_text(x) for x in safe_list(node.get("outputs")) if sanitize_text(x)]

        fillcolor = get_node_fillcolor(node_type)
        label = build_port_table_label(title, node_type, inputs, outputs, fillcolor)

        dot.node(node_id, label=label)
        declared_node_ids.add(node_id)

    for edge in edges:
        from_id = sanitize_text(edge.get("from"))
        to_id = sanitize_text(edge.get("to"))
        from_port = sanitize_text(edge.get("from_port"))
        to_port = sanitize_text(edge.get("to_port"))

        if not from_id or not to_id:
            continue
        if from_id not in declared_node_ids or to_id not in declared_node_ids:
            continue
        if not from_port or not to_port:
            continue

        from_port_id = f"out_{normalize_port_name(from_port)}"
        to_port_id = f"in_{normalize_port_name(to_port)}"

        dot.edge(
            f"{from_id}:{from_port_id}",
            f"{to_id}:{to_port_id}",
            arrowsize="0.8",
        )

    return dot


def render_shader_graph_ui(graph_data: dict):
    graph_title = graph_data.get("graph_title", "Shader Graph")
    target = graph_data.get("target", "Unity Shader Graph / URP")
    difficulty = graph_data.get("difficulty", "중간")
    summary = graph_data.get("summary", "")

    properties = safe_list(graph_data.get("properties"))
    steps = safe_list(graph_data.get("steps"))
    outputs = safe_dict(graph_data.get("output_slots"))
    notes = safe_list(graph_data.get("implementation_notes"))
    nodes = safe_list(graph_data.get("nodes"))
    edges = safe_list(graph_data.get("edges"))

    st.subheader(f"🎛️ {graph_title}")

    c1, c2, c3 = st.columns(3)
    c1.metric("대상", target)
    c2.metric("난이도", difficulty)
    c3.metric("노드 / 연결", f"{len(nodes)} / {len(edges)}")

    if summary:
        st.info(summary)

    left, right = st.columns([1.7, 1.0])

    with left:
        st.markdown("### 포트 기반 노드 연결도")
        st.graphviz_chart(build_shader_graphviz(graph_data), use_container_width=True)

    with right:
        st.markdown("### 구현 순서")
        if steps:
            for idx, step in enumerate(steps, start=1):
                st.markdown(f"**{idx}.** {step}")
        else:
            st.write("구현 단계 정보가 없습니다.")

        st.markdown("### 출력 슬롯")
        if outputs:
            for key, value in outputs.items():
                st.markdown(f"**{key}**: {value}")
        else:
            st.write("출력 슬롯 정보가 없습니다.")

    b1, b2 = st.columns(2)

    with b1:
        st.markdown("### 프로퍼티 / 노출 변수")
        if properties:
            for prop in properties:
                name = prop.get("name", "Unnamed")
                prop_type = prop.get("type", "Unknown")
                default = prop.get("default", "")
                usage = prop.get("usage", "")

                st.markdown(f"- **{name}** ({prop_type})")
                if default != "":
                    st.caption(f"기본값: {default}")
                if usage:
                    st.caption(f"용도: {usage}")
        else:
            st.write("프로퍼티 정보가 없습니다.")

    with b2:
        st.markdown("### 구현 메모")
        if notes:
            for note in notes:
                st.markdown(f"- {note}")
        else:
            st.write("구현 메모가 없습니다.")


# =========================================================
# 5. 프롬프트
# =========================================================
def make_video_analysis_prompt(user_query: str, rag_context: str) -> str:
    return f"""
당신은 Unity Graphics Engineer이자 Technical Artist입니다.
업로드된 게임 영상을 분석해서 구현 방식을 역설계하세요.

[추가 RAG 참고 문서]
{rag_context}

[사용자 요청]
{user_query}

[분석 목표]
- 영상에 보이는 이펙트, 캐릭터 움직임, 카메라, 후처리, 머티리얼 표현을 기술적으로 추론한다.
- Unity URP 기준으로 가장 가능성 높은 구현 방식을 설명한다.
- 추정인 부분은 추정이라고 명시한다.

[출력 형식]
반드시 아래 구조를 따르는 기술 리포트 형식으로 작성:
1. 효과 개요
2. 화면에서 보이는 핵심 요소
3. 구현 추정
   - Shader Graph / HLSL / 머티리얼
   - 파티클 / VFX
   - 애니메이션 / 이동
   - 카메라 / 포스트 프로세싱
4. Unity 구현 순서
5. 성능 주의점
6. Shader Graph로 옮길 수 있는 핵심 구성 요약

[가이드]
- Shader Graph 노드 후보를 구체적으로 적을 것
- Base Color, Emission, Alpha, Distortion, Fresnel, Noise, Dissolve 등 관련 요소가 보이면 언급
- 모바일 비용이나 오버드로우 문제가 보이면 반드시 적을 것
"""


def make_shader_graph_from_report_prompt(analysis_report: str, user_query: str) -> str:
    return f"""
당신은 Unity URP Shader Graph 설계 전문가입니다.
아래 영상 분석 리포트를 바탕으로, 해당 효과를 포트 기반 Shader Graph 구조로 바꾸세요.
반드시 JSON 객체 하나만 출력하세요.
설명문, 머리말, 마크다운 코드블록은 절대 쓰지 마세요.

[사용자 요청]
{user_query}

[영상 분석 리포트]
{analysis_report}

[목표]
- 실제 Shader Graph처럼 포트 단위로 노드를 분리해서 설계한다.
- Multiply, Add, Lerp 같은 다중 입력 노드는 입력 포트를 반드시 분리한다.
- 출력은 BaseColor, Emission, Alpha, Normal 등으로 명확히 연결한다.
- 영상 분석 결과를 기반으로 가장 가능성 높은 그래프를 만든다.
- 불확실한 부분은 implementation_notes에 "추정"이라고 적는다.

[중요]
- nodes의 inputs / outputs는 실제 포트 이름이다.
- edges는 반드시 포트 단위로 연결한다.
- 잘못된 예:
  "Multiply가 Noise와 Fresnel을 받는다"
- 올바른 예:
  {{"from":"noise_mul","from_port":"Out","to":"final_mul","to_port":"A"}}
  {{"from":"fresnel_1","from_port":"Out","to":"final_mul","to_port":"B"}}

[출력 JSON 스키마]
{{
  "graph_title": "그래프 제목",
  "target": "Unity Shader Graph / URP",
  "difficulty": "쉬움 또는 중간 또는 고급",
  "summary": "이 그래프가 어떤 효과를 만드는지 한두 문장",
  "properties": [
    {{
      "name": "_BaseColor",
      "type": "Color",
      "default": "0.2,0.6,1,1",
      "usage": "기본 색상"
    }}
  ],
  "nodes": [
    {{
      "id": "time_1",
      "type": "Time",
      "title": "Time",
      "inputs": [],
      "outputs": ["Time"]
    }},
    {{
      "id": "scroll_speed",
      "type": "Property",
      "title": "ScrollSpeed",
      "inputs": [],
      "outputs": ["Out"]
    }},
    {{
      "id": "multiply_1",
      "type": "Multiply",
      "title": "Multiply",
      "inputs": ["A", "B"],
      "outputs": ["Out"]
    }},
    {{
      "id": "master_1",
      "type": "FragmentOutput",
      "title": "Fragment Stack",
      "inputs": ["BaseColor", "Emission", "Alpha", "AlphaClipThreshold"],
      "outputs": []
    }}
  ],
  "edges": [
    {{
      "from": "time_1",
      "from_port": "Time",
      "to": "multiply_1",
      "to_port": "A"
    }},
    {{
      "from": "scroll_speed",
      "from_port": "Out",
      "to": "multiply_1",
      "to_port": "B"
    }}
  ],
  "steps": [
    "구현 순서 1",
    "구현 순서 2"
  ],
  "output_slots": {{
    "BaseColor": "무엇이 연결되는지",
    "Emission": "무엇이 연결되는지",
    "Alpha": "무엇이 연결되는지",
    "Normal": "필요 시만"
  }},
  "implementation_notes": [
    "최적화 메모",
    "모바일 주의점",
    "추정 항목"
  ]
}}

[규칙]
- JSON 객체 하나만 출력
- nodes는 최소 5개 이상
- edges는 실제 연결 흐름이 보일 정도로 충분히 작성
- 포트 이름은 실제 Shader Graph에서 읽기 쉬운 이름으로 작성
- 다중 입력 노드의 포트는 반드시 분리
"""


# =========================================================
# 6. 세션 상태
# =========================================================
def init_state():
    defaults = {
        "video_analysis_report": "",
        "video_graph_data": None,
        "video_graph_raw_text": "",
        "video_uploaded_name": "",
        "video_last_query": "",
    }
    for key, value in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = value


# =========================================================
# 7. 메인
# =========================================================
def main():
    init_state()

    st.title("🎥 게임 영상 리버스 엔지니어링 봇")
    st.markdown(
        """
영상 파일을 분석해서 **구현 리포트**를 만들고,  
원하면 그 결과를 바탕으로 **포트 기반 Shader Graph 시각화**까지 이어서 보여줍니다.
"""
    )

    api_key_input, _, selected_model_name = render_sidebar_settings()

    top1, top2 = st.columns([1, 1])

    with top1:
        st.subheader("1. 영상 업로드")
        uploaded_video = st.file_uploader(
            "분석할 MP4/MOV/AVI/MKV 파일",
            type=["mp4", "mov", "avi", "mkv"]
        )

    with top2:
        st.subheader("2. 분석 요청 사항")
        user_query = st.text_area(
            "어떤 부분을 중점적으로 분석할까요?",
            value="이 영상에 나오는 스킬 이펙트와 캐릭터 움직임이 어떻게 구현되었는지 Unity URP와 C# 스크립트 기준으로 설명해줘. 그리고 가능하면 Shader Graph 구조도까지 보여줘.",
            height=160
        )

    opts1, opts2, opts3 = st.columns(3)
    with opts1:
        include_graph = st.toggle("분석 후 Shader Graph 시각화", value=True)
    with opts2:
        rag_k = st.slider("RAG 검색 개수", min_value=2, max_value=6, value=4, step=1)
    with opts3:
        show_raw_json = st.toggle("원문 JSON 표시", value=False)

    if st.button("🚀 영상 분석 시작 (Analyze Video)", type="primary"):
        if not api_key_input:
            st.warning("API Key가 필요합니다.")
            return

        if not uploaded_video:
            st.warning("영상 파일을 업로드해주세요.")
            return

        rag = UnityRAG(api_key_input)

        with st.spinner("📚 URP 관련 문서를 검색 중..."):
            rag_query = f"Unity URP VFX Shader Graph video effect analysis: {user_query}"
            rag_context = rag.retrieve_context(rag_query, k=rag_k)

        file_ref, client = upload_video_to_gemini(uploaded_video, api_key_input)
        if not file_ref or not client:
            return

        if not wait_for_files_active(client, [file_ref]):
            return

        analysis_prompt = make_video_analysis_prompt(user_query, rag_context)
        request_content = [
            analysis_prompt,
            file_ref,
            f"\n\n[사용자 요청사항]: {user_query}"
        ]

        with st.spinner(f"🧠 {selected_model_name} 모델이 영상을 분석 중입니다..."):
            try:
                response = client.models.generate_content(
                    model=selected_model_name,
                    contents=request_content
                )
                analysis_report = response.text if hasattr(response, "text") else ""

                st.session_state.video_analysis_report = analysis_report
                st.session_state.video_uploaded_name = uploaded_video.name
                st.session_state.video_last_query = user_query
                st.session_state.video_graph_data = None
                st.session_state.video_graph_raw_text = ""

            except Exception as e:
                st.error(f"영상 분석 중 오류 발생: {e}")
                st.warning(f"선택한 모델({selected_model_name})이 영상 입력을 지원하지 않거나, 현재 트래픽이 많을 수 있습니다.")
                return

        st.divider()
        st.subheader("📊 분석 결과 Report")
        st.markdown(st.session_state.video_analysis_report)

        if include_graph and st.session_state.video_analysis_report:
            with st.spinner("🎛️ 분석 결과를 Shader Graph로 변환 중..."):
                try:
                    graph_prompt = make_shader_graph_from_report_prompt(
                        st.session_state.video_analysis_report,
                        user_query
                    )

                    graph_response = client.models.generate_content(
                        model=selected_model_name,
                        contents=graph_prompt
                    )

                    raw_text = graph_response.text if hasattr(graph_response, "text") else ""
                    graph_data = extract_json_block(raw_text)

                    st.session_state.video_graph_raw_text = raw_text

                    if not graph_data:
                        st.warning("Shader Graph JSON 파싱에 실패했습니다. 원문을 확인하세요.")
                    else:
                        st.session_state.video_graph_data = graph_data

                except Exception as e:
                    st.error(f"Shader Graph 생성 중 오류 발생: {e}")

        log_usage("영상 분석 봇")

    # -----------------------------------------
    # 분석 결과 재표시
    # -----------------------------------------
    if st.session_state.video_analysis_report:
        st.divider()
        st.subheader("📌 최근 분석 결과")
        info1, info2 = st.columns(2)
        with info1:
            st.caption(f"영상 파일: {st.session_state.video_uploaded_name or '없음'}")
        with info2:
            st.caption(f"요청: {st.session_state.video_last_query or '없음'}")

        with st.expander("분석 리포트 다시 보기", expanded=False):
            st.markdown(st.session_state.video_analysis_report)

    # -----------------------------------------
    # 수동 Shader Graph 변환 버튼
    # -----------------------------------------
    if st.session_state.video_analysis_report:
        st.divider()
        st.subheader("🛠️ Shader Graph 후처리")

        col_a, col_b = st.columns([1, 2])

        with col_a:
            regenerate_graph = st.button("🎛️ 분석 결과로 Shader Graph 다시 생성", use_container_width=True)

        with col_b:
            st.caption("영상 분석 리포트는 유지한 채, 그래프만 다시 생성합니다.")

        if regenerate_graph:
            if not api_key_input:
                st.warning("API Key가 필요합니다.")
                return

            client = genai.Client(api_key=api_key_input)

            with st.spinner("포트 기반 Shader Graph를 다시 생성하는 중..."):
                try:
                    graph_prompt = make_shader_graph_from_report_prompt(
                        st.session_state.video_analysis_report,
                        st.session_state.video_last_query
                    )
                    graph_response = client.models.generate_content(
                        model=selected_model_name,
                        contents=graph_prompt
                    )

                    raw_text = graph_response.text if hasattr(graph_response, "text") else ""
                    graph_data = extract_json_block(raw_text)

                    st.session_state.video_graph_raw_text = raw_text

                    if not graph_data:
                        st.warning("JSON 파싱에 실패했습니다. 원문 응답을 확인하세요.")
                    else:
                        st.session_state.video_graph_data = graph_data
                        st.success("Shader Graph를 다시 생성했습니다.")

                except Exception as e:
                    st.error(f"Shader Graph 재생성 실패: {e}")

    # -----------------------------------------
    # 그래프 표시
    # -----------------------------------------
    if st.session_state.video_graph_data:
        st.divider()
        st.subheader("🎛️ Shader Graph 시각화")
        render_shader_graph_ui(st.session_state.video_graph_data)

        if show_raw_json:
            with st.expander("원문 JSON 보기"):
                st.code(
                    json.dumps(st.session_state.video_graph_data, ensure_ascii=False, indent=2),
                    language="json"
                )

    elif st.session_state.video_graph_raw_text and show_raw_json:
        st.divider()
        st.subheader("⚠️ 파싱 실패한 원문 응답")
        st.code(st.session_state.video_graph_raw_text, language="json")


if __name__ == "__main__":
    main()