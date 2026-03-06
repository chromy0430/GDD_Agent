import json
import re
import html
import streamlit as st
import google.generativeai as genai
from graphviz import Digraph

from utils import log_usage, render_sidebar_settings
from rag_utils import UnityRAG


st.set_page_config(layout="wide", page_title="URP 그래픽스 전문가")


# =========================================================
# 공통 유틸
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


def sanitize_text(value) -> str:
    if value is None:
        return ""
    return str(value).strip()


def html_escape(value) -> str:
    return html.escape(sanitize_text(value))


# =========================================================
# Graphviz 포트 기반 Shader Graph 렌더링
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
    """
    side:
      - in  : 입력 포트
      - out : 출력 포트
    """
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
    """
    Graphviz HTML-like label
    왼쪽 입력 포트 / 가운데 제목 / 오른쪽 출력 포트
    """
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
        label = build_port_table_label(
            title=title,
            node_type=node_type,
            inputs=inputs,
            outputs=outputs,
            fillcolor=fillcolor,
        )

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


# =========================================================
# UI 렌더링
# =========================================================
def render_properties(properties: list):
    if not properties:
        st.write("프로퍼티 정보가 없습니다.")
        return

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


def render_steps(steps: list):
    if not steps:
        st.write("구현 단계 정보가 없습니다.")
        return

    for idx, step in enumerate(steps, start=1):
        st.markdown(f"**{idx}.** {step}")


def render_outputs(outputs: dict):
    if not outputs:
        st.write("출력 슬롯 정보가 없습니다.")
        return

    for key, value in outputs.items():
        st.markdown(f"**{key}**: {value}")


def render_notes(notes: list):
    if not notes:
        st.write("구현 메모가 없습니다.")
        return

    for note in notes:
        st.markdown(f"- {note}")


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
        render_steps(steps)

        st.markdown("### 출력 슬롯")
        render_outputs(outputs)

    b1, b2 = st.columns(2)

    with b1:
        st.markdown("### 프로퍼티 / 노출 변수")
        render_properties(properties)

    with b2:
        st.markdown("### 구현 메모")
        render_notes(notes)


# =========================================================
# 프롬프트
# =========================================================
def make_visualization_prompt(context: str, user_prompt: str) -> str:
    return f"""
당신은 Unity URP Shader Graph 설계 전문가입니다.
아래 참고 문서와 사용자 요청을 바탕으로, 반드시 JSON 객체 하나만 출력하세요.
설명문, 머리말, 코드블록 마크다운은 절대 쓰지 마세요.

[참고 문서 / RAG Context]
{context}

[사용자 요청]
{user_prompt}

[목표]
- 사용자가 Shader Graph를 실제 노드 연결 구조처럼 이해할 수 있도록 설계한다.
- Unity URP Shader Graph 기준으로 작성한다.
- Multiply, Add, Lerp, Sample Texture 2D 같은 노드는 반드시 포트 단위로 설명한다.
- 특히 다중 입력 노드는 inputs를 생략하지 말고 A, B, T 등의 포트를 분리한다.
- 출력은 BaseColor, Emission, Alpha, Normal 등 최종 연결을 명확히 적는다.

[매우 중요]
- nodes의 inputs / outputs는 실제 포트 이름이다.
- edges는 반드시 포트 단위로 연결한다.
- 잘못된 예:
  "Multiply가 Time과 ScrollSpeed를 받는다"
- 올바른 예:
  {{"from":"time_1","from_port":"Time","to":"multiply_1","to_port":"A"}}
  {{"from":"scroll_speed","from_port":"Out","to":"multiply_1","to_port":"B"}}

[출력 JSON 스키마]
{{
  "graph_title": "그래프 제목",
  "target": "Unity Shader Graph / URP",
  "difficulty": "쉬움 또는 중간 또는 고급",
  "summary": "이 그래프가 어떤 효과를 만드는지 한두 문장",
  "properties": [
    {{
      "name": "_ScrollSpeed",
      "type": "Vector2 또는 Float 또는 Color",
      "default": "1 또는 0.2,0.6,1,1",
      "usage": "어디에 쓰는 값인지"
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
    "URP 설정 팁"
  ]
}}

[노드명 가이드]
가능하면 아래처럼 실무에서 익숙한 이름을 우선 사용:
- Time
- UV
- Tiling And Offset
- Sample Texture 2D
- Simple Noise
- Gradient Noise
- Fresnel Effect
- Multiply
- Add
- Lerp
- One Minus
- Smoothstep
- Saturate
- Normal Strength
- Split
- Combine
- Color
- Vector1
- Vector2
- Texture2D
- Fragment Stack

[규칙]
- JSON 객체 하나만 출력.
- nodes는 최소 5개 이상.
- edges는 실제 연결 흐름이 보일 정도로 충분히 작성.
- 다중 입력 노드의 포트는 반드시 분리.
- 확실하지 않은 구현은 implementation_notes에 "추정"이라고 적을 것.
"""


def make_normal_answer_prompt(context: str, user_prompt: str) -> str:
    return f"""
당신은 Unity URP(Universal Render Pipeline) 수석 테크니컬 아티스트입니다.
사용자의 질문에 대해 제공된 URP 매뉴얼(Context)을 근거로 답변하세요.

[참고 문서 / RAG Context]
{context}

[답변 가이드라인]
1. URP 전용 용어를 사용하세요.
2. Shader Graph 노드 구성이나 HLSL 코드가 필요하면 구체적 예시를 포함하세요.
3. 성능 이슈가 있으면 Draw Call, Overdraw, Texture Sample 수, 모바일 비용을 함께 언급하세요.
4. 답변은 개발자가 바로 적용할 수 있도록 단계형으로 설명하세요.
5. 가능하면 마지막에 "Shader Graph로 옮기면 어떤 노드 조합인지"를 짧게 요약하세요.

[사용자 질문]
{user_prompt}
"""


# =========================================================
# 메인
# =========================================================
def main():
    st.title("🎨 URP 테크니컬 아티스트 (Graphics Expert)")
    api_key, _, model_name = render_sidebar_settings()

    st.markdown(
        """
**Unity URP 매뉴얼(RAG)** 기반으로 쉐이더, 포스트 프로세싱, 렌더링 최적화 질문에 답합니다.  
시각화 모드에서는 **포트가 실제로 나뉜 Shader Graph 스타일 연결도**로 보여줍니다.
"""
    )

    with st.expander("🧭 사용 예시"):
        st.markdown(
            """
- `물결치는 에너지 쉴드를 Shader Graph로 시각화해줘`
- `발광 룬 문양 이펙트를 포트 기반 노드 연결도로 보여줘`
- `검기 이펙트 구현법 설명 + Shader Graph 시각화`
- `모바일용 홀로그램 쉐이더를 포트가 보이게 구성해줘`
"""
        )

    col1, col2 = st.columns([1, 1])
    with col1:
        visualize_toggle = st.toggle("Shader Graph 시각화 모드", value=True)
    with col2:
        rag_k = st.slider("RAG 검색 개수", min_value=2, max_value=6, value=4, step=1)

    if "graphics_chat_history" not in st.session_state:
        st.session_state.graphics_chat_history = []

    for message in st.session_state.graphics_chat_history:
        with st.chat_message(message["role"]):
            if message.get("mode") == "visual" and message.get("graph_data"):
                render_shader_graph_ui(message["graph_data"])
                if message.get("raw_text"):
                    with st.expander("원문 응답 보기"):
                        st.code(message["raw_text"], language="json")
            else:
                st.markdown(message["content"])

    if prompt := st.chat_input("그래픽스/렌더링 관련 질문을 입력하세요..."):
        if not api_key:
            st.error("API Key가 필요합니다.")
            return

        st.session_state.graphics_chat_history.append(
            {"role": "user", "content": prompt}
        )

        with st.chat_message("user"):
            st.markdown(prompt)

        rag = UnityRAG(api_key)

        with st.spinner("📚 URP 매뉴얼과 렌더링 문서를 검색 중..."):
            search_query = f"Unity URP Rendering Shader Graphics ShaderGraph: {prompt}"
            context = rag.retrieve_context(search_query, k=rag_k)

        genai.configure(api_key=api_key)
        model = genai.GenerativeModel(model_name)

        full_prompt = (
            make_visualization_prompt(context, prompt)
            if visualize_toggle
            else make_normal_answer_prompt(context, prompt)
        )

        with st.chat_message("assistant"):
            try:
                if visualize_toggle:
                    with st.spinner("🧠 포트 기반 Shader Graph를 설계하는 중..."):
                        response = model.generate_content(full_prompt)
                        raw_text = response.text if hasattr(response, "text") else ""
                        graph_data = extract_json_block(raw_text)

                        if not graph_data:
                            st.warning("JSON 파싱에 실패했습니다. 원문 답변을 표시합니다.")
                            st.markdown(raw_text)

                            st.session_state.graphics_chat_history.append(
                                {
                                    "role": "assistant",
                                    "content": raw_text,
                                    "mode": "text"
                                }
                            )
                        else:
                            render_shader_graph_ui(graph_data)

                            with st.expander("원문 JSON 보기"):
                                st.code(
                                    json.dumps(graph_data, ensure_ascii=False, indent=2),
                                    language="json"
                                )

                            st.session_state.graphics_chat_history.append(
                                {
                                    "role": "assistant",
                                    "content": "",
                                    "mode": "visual",
                                    "graph_data": graph_data,
                                    "raw_text": raw_text
                                }
                            )

                else:
                    message_placeholder = st.empty()
                    full_response = ""

                    response = model.generate_content(full_prompt, stream=True)
                    for chunk in response:
                        chunk_text = getattr(chunk, "text", "")
                        full_response += chunk_text
                        message_placeholder.markdown(full_response + "▌")

                    message_placeholder.markdown(full_response)

                    st.session_state.graphics_chat_history.append(
                        {
                            "role": "assistant",
                            "content": full_response,
                            "mode": "text"
                        }
                    )

                log_usage("URP 그래픽스 봇")

            except Exception as e:
                st.error(f"답변 생성 실패: {e}")


if __name__ == "__main__":
    main()