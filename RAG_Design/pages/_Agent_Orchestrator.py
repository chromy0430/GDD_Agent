import os
import time
import json
import tempfile
import re
from typing import Dict, Any, List, Optional

import streamlit as st
from google import genai

from rag_utils import UnityRAG
from foundry import guard
from utils import render_sidebar_settings, retry_with_backoff, log_usage


# =========================================================
# 1. 설정
# =========================================================
st.set_page_config(layout="wide", page_title="Agent Headquarters")


# =========================================================
# 2. Agent Registry
# =========================================================
AGENT_REGISTRY: Dict[str, Dict[str, Any]] = {
    "Market_Analyst": {
        "file_path": "_Market_Analyst.py",
        "description": "게임 시장 트렌드 분석, 타겟 유저층 설정, 경쟁작 분석 및 BM(수익화) 모델 초기 방향성을 제안합니다.",
        "expected_output": "Market_Research_Report",
        "supported_inputs": ["text"],
        "supported_outputs": ["text"]
    },
    "Video_Analyst": {
        "file_path": "_Video_Analyst.py",
        "description": "경쟁 게임이나 레퍼런스 영상의 프레임을 분석하여 애니메이션, 이펙트, UI 연출 등의 시각적 데이터를 추출합니다.",
        "expected_output": "Video_Analysis_Data",
        "supported_inputs": ["text", "video", "image"],
        "supported_outputs": ["text"]
    },
    "Reference_Finder": {
        "file_path": "_Reference_Finder.py",
        "description": "기획 의도에 맞는 게임 내외적인 텍스트, 이미지, 시스템 레퍼런스를 RAG 및 웹 검색을 통해 수집합니다.",
        "expected_output": "Reference_List",
        "supported_inputs": ["text", "image"],
        "supported_outputs": ["text"]
    },
    "Game_Designer": {
        "file_path": "_Game_Designer.py",
        "description": "레퍼런스와 시장 분석을 바탕으로 게임의 핵심 코어 루프, 메커니즘, 시스템을 기획합니다.",
        "expected_output": "System_Design_Draft",
        "supported_inputs": ["text"],
        "supported_outputs": ["text"]
    },
    "Game_Planner": {
        "file_path": "_Game_Planner.py",
        "description": "게임의 전반적인 방향성, 비전, 핵심 타겟층 및 기초 컨셉을 기획합니다. (Designer 이전 단계의 상위 기획)",
        "expected_output": "Game_Concept_Plan",
        "supported_inputs": ["text"],
        "supported_outputs": ["text"]
    },
    "GDD_Writer": {
        "file_path": "_GDD_Writer.py",
        "description": "기획된 내용을 바탕으로 개발자와 아티스트가 볼 수 있는 정형화된 게임 시스템기획서(GDD) 문서를 작성합니다.",
        "expected_output": "Game_Design_Document(Markdown)",
        "supported_inputs": ["text"],
        "supported_outputs": ["text"]
    },
    "Spec_Generator": {
        "file_path": "_Spec_Generator.py",
        "description": "GDD를 기반으로 실제 개발에 필요한 리소스 명세서, 데이터 테이블 구조, API 요구사항 등을 정의합니다.",
        "expected_output": "Technical_Specification",
        "supported_inputs": ["text"],
        "supported_outputs": ["text"]
    },
    "Balance_Calc": {
        "file_path": "_Balance_Calc.py",
        "description": "게임 내 전투 수치, 확률, 경제 밸런스를 계산하고 시뮬레이션하여 검증된 CSV/JSON 데이터를 생성합니다.",
        "expected_output": "Balance_Table_Data",
        "supported_inputs": ["text", "csv"],
        "supported_outputs": ["text", "csv"]
    },
    "Graphics_Expert": {
        "file_path": "_Graphics_Expert.py",
        "description": "Unity URP 환경에 맞는 셰이더, 라이팅, 포스트 프로세싱 세팅 및 아트 리소스 최적화 방향을 제안합니다.",
        "expected_output": "Graphics_Guideline",
        "supported_inputs": ["text", "image"],
        "supported_outputs": ["text"]
    },
    "RenderGraph_Expert": {
        "file_path": "_RenderGraph_Expert.py",
        "description": "Unity 6.3 URP Render Graph 기반 커스텀 렌더 패스 및 셰이더 코드를 작성하고 Zero-GC 원칙을 엄수하여 구현합니다.",
        "expected_output": "C#_and_Shader_Code",
        "supported_inputs": ["text", "code"],
        "supported_outputs": ["text", "code"]
    },
    "Feature_Implementer": {
        "file_path": "_Feature_Implementer.py",
        "description": "기획서와 명세서를 바탕으로 실제 Unity C# 기반의 코드를 작성하고 기능을 구현합니다.",
        "expected_output": "C#_Source_Code",
        "supported_inputs": ["text"],
        "supported_outputs": ["text", "code"]
    },
    "Code_Reviewer": {
        "file_path": "_Code_Reviewer.py",
        "description": "작성된 코드의 Unity 6 최적화 여부(Zero GC 등), SOLID 원칙 준수 여부를 리뷰하고 개선안을 제시합니다.",
        "expected_output": "Code_Review_Feedback",
        "supported_inputs": ["text", "code"],
        "supported_outputs": ["text"]
    }    
}


# =========================================================
# 3. 파일 처리
# =========================================================
def classify_uploaded_file(uploaded_file) -> str:
    file_type = uploaded_file.type or ""
    file_name = uploaded_file.name.lower()

    if file_name.endswith(".py") or file_name.endswith(".cs"):
        return "code"
    if "video" in file_type or file_name.endswith(".mp4") or file_name.endswith(".mov"):
        return "video"
    if file_name.endswith(".pdf") or file_name.endswith(".md") or file_name.endswith(".txt"):
        return "document"
    return "text"


@retry_with_backoff(max_retries=3, initial_delay=3)
def process_uploaded_file(uploaded_file, client):
    file_type = uploaded_file.type or ""
    file_name = uploaded_file.name
    classified_type = classify_uploaded_file(uploaded_file)

    # 텍스트 / 코드 계열은 바로 읽기
    if classified_type in {"text", "document", "code"} and not file_name.lower().endswith(".pdf"):
        try:
            content = uploaded_file.getvalue().decode("utf-8")
        except Exception:
            content = uploaded_file.getvalue().decode("utf-8", errors="ignore")

        return {
            "type": "text",
            "classified_type": classified_type,
            "content": content,
            "desc": f"{classified_type} 파일 ({file_name})",
            "name": file_name,
            "mime_type": file_type,
        }

    # PDF / Video 는 파일 업로드
    suffix = ".mp4" if classified_type == "video" else ".pdf"

    with tempfile.NamedTemporaryFile(delete=False, suffix=suffix) as tmp:
        tmp.write(uploaded_file.getvalue())
        tmp_path = tmp.name

    try:
        with st.spinner(f"📡 '{file_name}' 파일을 AI 서버로 전송 및 인덱싱 중..."):
            file_ref = client.files.upload(file=tmp_path)

            while file_ref.state.name == "PROCESSING":
                time.sleep(2)
                file_ref = client.files.get(name=file_ref.name)

            if file_ref.state.name != "ACTIVE":
                st.error(f"파일 처리 실패: {file_ref.state.name}")
                return None

            return {
                "type": "file_ref",
                "classified_type": classified_type,
                "content": file_ref,
                "desc": f"멀티모달 파일 ({file_name}, Type: {file_type})",
                "name": file_name,
                "mime_type": file_type,
            }
    finally:
        if os.path.exists(tmp_path):
            os.remove(tmp_path)


# =========================================================
# 4. 프롬프트 / 라우팅
# =========================================================
def make_agent_list_text() -> str:
    lines = []
    for name, meta in AGENT_REGISTRY.items():
        # .get()을 사용하여 방어적 프로그래밍 적용 (KeyError 방지)
        inputs = meta.get('supported_inputs', ['text'])
        outputs = meta.get('supported_outputs', ['text'])
        lines.append(
            f"- {name}: {meta.get('description', '')} / "
            f"supported_inputs={sorted(list(inputs))} / "
            f"supported_outputs={sorted(list(outputs))}"
        )
    return "\n".join(lines)


def build_plan_prompt(prompt: str, attachment_info: str, attachment_type: Optional[str], user_context: str) -> str:
    return f"""
당신은 멀티 에이전트 오케스트레이터의 플래너입니다.
사용자 요청과 첨부 정보를 보고, 가장 합리적인 실행 계획을 JSON 하나로만 출력하세요.
설명문, 마크다운, 코드블록 없이 JSON 객체만 반환하세요.

[CRITICAL RULE : STRICT AGENT SELECTION]
1. 반드시 아래 [Available Agents] 목록에 있는 에이전트의 '정확한 이름(Exact Key)'만 사용해야 합니다.
2. 'Unity_Expert', 'Product_Manager' 등 목록에 없는 임의의 에이전트 이름을 절대 창조하지 마십시오.
3. 대소문자와 언더바(_)를 정확히 일치시키십시오.

[Available Agents]
{make_agent_list_text()}

[User Request]
<user_input>
{prompt}
</user_input>

[Attachment Info]
{attachment_info}

[Attachment Type]
{attachment_type or "none"}

[RAG Context]
{user_context}

[계획 원칙]
- 영상 첨부가 있으면 보통 Video_Analyst를 먼저 고려
- 게임의 방향성, 비전, 기초 컨셉 기획 요청이면 Game_Planner 우선 고려
- URP 렌더그래프(Render Graph), 커스텀 패스, 셰이더 코드 구현 요청이면 반드시 RenderGraph_Expert 사용
- 일반적인 기능 구현 및 C# 로직 작성은 Feature_Implementer 사용
- 코드의 성능 최적화, Zero-GC 점검 요청이면 Code_Reviewer 우선 고려
- 문서/PDF 요약 또는 기획서 작성이면 Spec_Generator 활용
- 그래픽/아트 최적화 방향성이면 Graphics_Expert 고려
- 필요 없는 step은 만들지 말 것
- step 수는 1~4개 권장
- 이전 결과가 다음 step에 필요한 경우 depends_on에 step id를 적을 것
- 첨부가 꼭 필요한 step만 use_attachment=true
- 최종 보고서 형식을 final_output에 적을 것

[출력 스키마]
{{
  "intent": "사용자 의도 요약",
  "task_type": "analysis/spec/code/graphics/market/mixed",
  "thought": "왜 이런 순서인지 짧게 설명",
  "steps": [
    {{
      "id": "step1",
      "agent": "RenderGraph_Expert",
      "instruction": "사용자가 요청한 흑백 처리 포스트 프로세싱 렌더그래프 코드를 작성해줘.",
      "depends_on": [],
      "input_mode": "text",
      "use_attachment": false,
      "expected_output": "code"
    }}
  ],
  "final_output": {{
    "format": "report",
    "sections": ["executive_summary", "step_results", "final_recommendation"]
  }}
}}
"""


def build_agent_prompt(
    agent_name: str,
    instruction: str,
    global_context: str,
    dependency_outputs: List[Dict[str, Any]],
    attachment_summary: str,
) -> str:
    return f"""
당신은 {agent_name}입니다.
아래 지시를 수행하고 반드시 JSON 객체 하나만 출력하세요.
마크다운, 코드블록, 장황한 머리말은 쓰지 마세요.

[Agent Role]
{AGENT_REGISTRY[agent_name]["description"]}

[Instruction]
{instruction}

[Global Context]
{global_context}

[Dependency Outputs]
{json.dumps(dependency_outputs, ensure_ascii=False, indent=2)}

[Attachment Summary]
{attachment_summary}

[출력 스키마]
{{
  "summary": "이번 step 결과 요약",
  "key_findings": ["핵심 발견 1", "핵심 발견 2"],
  "deliverable": "실제 산출물 본문",
  "next_step_hint": "다음 step이 활용해야 할 핵심 한 줄",
  "artifacts": {{
    "format": "text",
    "tags": ["analysis", "spec", "code", "graphics"]
  }}
}}
"""


def route_attachment_to_step(file_data: Optional[Dict[str, Any]], step: Dict[str, Any]) -> Dict[str, Any]:
    """
    step에 전달할 첨부 정보를 고른다. (텍스트 호환성 로직 강화)
    """
    if not file_data or not step.get("use_attachment", False):
        return {"summary": "첨부 없음", "contents": []}

    classified_type = file_data.get("classified_type", "unknown")
    input_mode = step.get("input_mode", "text")

    # 1. 텍스트 호환 타입 그룹핑 (문서, 코드, 텍스트, CSV는 모두 텍스트로 취급하여 상호 호환)
    text_compatible_types = {"text", "document", "code", "csv"}
    
    # 혼합 모드이거나, 타입이 정확히 일치하거나, 둘 다 텍스트 기반 포맷일 경우 통과
    is_compatible = (
        (input_mode == "mixed") or 
        (classified_type == input_mode) or 
        (classified_type in text_compatible_types and input_mode in text_compatible_types)
    )

    # 2. 타입이 호환되지 않으면 첨부 제외
    if not is_compatible:
        return {
            "summary": f"⚠️ 첨부 파일({classified_type})이 있으나 이 step의 input_mode({input_mode})와 호환되지 않아 전달 제외됨",
            "contents": []
        }

    # 3. 텍스트 기반 데이터의 경우 프롬프트 하단에 문자열로 결합하여 전달
    if file_data["type"] == "text":
        return {
            "summary": f"✅ 텍스트 호환 첨부 전달됨: {file_data['desc']}",
            "contents": [f"\n\n[첨부 파일 원문 데이터]\n{file_data['content']}\n\n"]
        }

    # 4. 멀티모달 (PDF, Video 등 Google GenAI File API 객체) 처리
    return {
        "summary": f"✅ 멀티모달 첨부(File API) 전달됨: {file_data['desc']}",
        "contents": [file_data["content"]]
    }


# =========================================================
# 5. 실행기
# =========================================================
def collect_dependency_outputs(execution_state: Dict[str, Any], depends_on: List[str]) -> List[Dict[str, Any]]:
    results = []
    for dep_id in depends_on:
        if dep_id in execution_state["step_outputs"]:
            results.append(execution_state["step_outputs"][dep_id])
    return results


@retry_with_backoff(max_retries=2, initial_delay=2)
def safe_generate(client, model_name: str, contents):
    return client.models.generate_content(model=model_name, contents=contents)

    # _Agent_Orchestrator.py 내부

def build_agent_prompt(
    agent_name: str,
    instruction: str,
    global_context: str,
    dependency_outputs: List[Dict[str, Any]],
    attachment_summary: str,
) -> str:
    return f"""
        당신은 {agent_name}입니다.
        아래 지시를 수행하고 반드시 JSON 객체 하나만 출력하세요.
        마크다운, 코드블록, 장황한 머리말은 쓰지 마세요.

        [Agent Role]
        {AGENT_REGISTRY[agent_name]["description"]}

        [Instruction]
        {instruction}

        [Global Context]
        {global_context}

        [Dependency Outputs]
        {json.dumps(dependency_outputs, ensure_ascii=False, indent=2)}

        [Attachment Summary]
        {attachment_summary}

        [출력 스키마]
        {{
        "summary": "이번 step 결과 요약",
        "key_findings": ["핵심 발견 1", "핵심 발견 2"],
        "deliverable": [
            "실제 산출물의 첫 번째 단락 또는 1번 항목",
            "실제 산출물의 두 번째 단락 또는 2번 항목",
            "상세 내용..."
        ],
        "next_step_hint": "다음 step이 활용해야 할 핵심 한 줄",
        "artifacts": {{
            "format": "text",
            "tags": ["analysis", "spec", "code", "graphics"]
        }}
        }}
    """

def execute_agent_step(
    client,
    model_name: str,
    step: Dict[str, Any],
    file_data: Optional[Dict[str, Any]],
    global_context: str,
    execution_state: Dict[str, Any],
) -> Dict[str, Any]:
    agent_name = step["agent"]
    instruction = step["instruction"]
    depends_on = step.get("depends_on", []) or []

    dependency_outputs = collect_dependency_outputs(execution_state, depends_on)
    routed_attachment = route_attachment_to_step(file_data, step)

    special_context = ""
    if agent_name == "RenderGraph_Expert":
        folder_path = "rendergraph_samples"
        combined_samples = ""
        if os.path.exists(folder_path):
            for root, dirs, files in os.walk(folder_path):
                for filename in files:
                    if filename.lower().endswith((".cs", ".txt", ".md", ".shader", ".hlsl", ".cginc", ".compute")):
                        filepath = os.path.join(root, filename)
                        try:
                            rel_path = os.path.relpath(filepath, folder_path).replace("\\", "/")
                            with open(filepath, "r", encoding="utf-8") as f:
                                combined_samples += f"\n--- [{rel_path}] ---\n{f.read()}\n"
                        except Exception: pass
            
            if combined_samples:
                special_context = f"\n\n[CRITICAL: Ground Truth Data - RENDER GRAPH SAMPLES]\n반드시 아래 제공된 유니티 6.3 렌더그래프 샘플의 구조와 문법을 기준으로 코드를 작성할 것.\n{combined_samples}"
    
    # 병합된 컨텍스트 생성
    injected_global_context = global_context + special_context

    # [주의] 위에서 정의한 함수를 '호출'하여 prompt 변수에 저장합니다. 여기서 return 하지 않습니다.
    prompt = build_agent_prompt(
        agent_name=agent_name,
        instruction=instruction,
        global_context=global_context,
        dependency_outputs=dependency_outputs,
        attachment_summary=routed_attachment["summary"],
    )

    # 이제 아래 코드가 정상적으로 음영 없이 활성화됩니다.
    contents = [prompt]
    contents.extend(routed_attachment["contents"])

    res = safe_generate(client, model_name, contents)
    raw_text = res.text if hasattr(res, "text") else ""

    parsed = guard.extract_json_object(raw_text)
    if not parsed["valid"]:
        raise ValueError(f"{agent_name} JSON 파싱 실패: {parsed.get('error')}")

    validated = guard.validate_agent_output(parsed["data"])
    if not validated["valid"]:
        raise ValueError(f"{agent_name} output schema 오류: {validated['errors']}")

    # 모든 작업이 끝난 후 최종 결과를 return 합니다.
    return {
        "agent": agent_name,
        "step_id": step["id"],
        "instruction": instruction,
        "data": parsed["data"],
        "raw_text": raw_text,
    }

def try_repair_plan_once(client, model_name: str, raw_plan_text: str, validation_errors: List[str]) -> Dict[str, Any]:
    repair_prompt = f"""
    이전 planner 응답은 invalid입니다.
    오류:
    {json.dumps(validation_errors, ensure_ascii=False, indent=2)}

    이전 응답:
    {raw_plan_text}

    오류를 수정해서 JSON 객체 하나만 다시 출력하세요.
    [CRITICAL] 목록에 없는 에이전트 이름을 사용했다면, 반드시 아래 [Available Agents] 목록 내에 존재하는 올바른 이름으로만 교체하십시오.

    [Available Agents]
    {make_agent_list_text()}
    """
    res = safe_generate(client, model_name, repair_prompt)
    repaired = guard.extract_json_object(res.text if hasattr(res, "text") else "")
    return repaired


# =========================================================
# 6. 결과 조합
# =========================================================
def build_final_report(plan: Dict[str, Any], execution_state: Dict[str, Any]) -> str:
    lines = []
    lines.append("## 🧭 실행 개요")
    lines.append(f"- 의도: {plan.get('intent', '-')}")
    lines.append(f"- 작업 유형: {plan.get('task_type', '-')}")
    lines.append(f"- 전략: {plan.get('thought', '-')}")

    lines.append("\n## ✅ Step 결과")
    for item in execution_state["ordered_results"]:
        data = item["data"]
        lines.append(f"\n### {item['step_id']} · {item['agent']}")
        lines.append(f"- 요약: {data.get('summary', '-')}")

        findings = data.get("key_findings", [])
        if findings:
            for finding in findings:
                lines.append(f"  - {finding}")

        deliverable = data.get("deliverable", [])
        if deliverable:
            if isinstance(deliverable, list):
                # 배열일 경우 마크다운 문단 분리(\n\n)를 적용하여 결합
                joined_text = "\n\n".join(deliverable)
                lines.append(f"\n{joined_text}")
            elif isinstance(deliverable, str):
                # 기존처럼 단일 String으로 올 경우를 대비한 방어적 코드
                # LLM이 1. 2. 3. 패턴을 썼을 때 강제로 줄바꿈 처리
                formatted_text = deliverable.replace(" 1. ", "\n\n1. ").replace(" 2. ", "\n\n2. ").replace(" 3. ", "\n\n3. ").replace(" 4. ", "\n\n4. ")
                lines.append(f"\n{formatted_text}")

    lines.append("\n## 🧩 최종 권장")
    if execution_state["ordered_results"]:
        last = execution_state["ordered_results"][-1]["data"]
        lines.append(last.get("next_step_hint", "추가 권장사항 없음"))
    else:
        lines.append("실행 결과 없음")

    return "\n".join(lines)


# =========================================================
# 7. 메인
# =========================================================
def main():
    st.title("🧠 Agent 365: 통합 지휘 통제실 (Orchestrator)")
    st.markdown(
        "텍스트, PDF, 영상, 코드 파일을 업로드하면 오케스트레이터가 의도를 파악하고 "
        "적절한 전문가 Agent를 순서대로 호출합니다."
    )

    api_key, _, model_name = render_sidebar_settings()

    if "messages" not in st.session_state:
        st.session_state.messages = []
    if "last_plan" not in st.session_state:
        st.session_state.last_plan = None
    if "last_execution" not in st.session_state:
        st.session_state.last_execution = None

    with st.expander("📂 파일 첨부 (문서 / 영상 / 코드)", expanded=True):
        uploaded_file = st.file_uploader(
            "분석할 자료를 드래그하세요.",
            type=["txt", "md", "pdf", "mp4", "mov", "py", "cs"]
        )

    preview_only = st.toggle("실행 전 계획 먼저 보기", value=True)

    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            if "file_info" in msg:
                st.caption(f"📎 첨부: {msg['file_info']}")
            st.markdown(msg["content"])

    if prompt := st.chat_input("명령을 입력하세요 (예: 이 영상 분석해서 기획서로 만들어줘)"):
        if not api_key:
            st.warning("API Key가 필요합니다.")
            return

        client = genai.Client(api_key=api_key)

        file_data = None
        if uploaded_file:
            file_data = process_uploaded_file(uploaded_file, client)
            if uploaded_file and not file_data:
                return

        user_msg_obj = {"role": "user", "content": prompt}
        if file_data:
            user_msg_obj["file_info"] = file_data["desc"]

        st.session_state.messages.append(user_msg_obj)

        with st.chat_message("user"):
            if file_data:
                st.caption(f"📎 {file_data['desc']}")
            st.markdown(prompt)

        rag = UnityRAG(api_key)
        with st.spinner("💾 Fabric IQ: 관련 지식 검색 중..."):
            user_context = rag.retrieve_context(prompt, k=3)

        attachment_info = (
            f"사용자가 파일({file_data['desc']})을 첨부했습니다."
            if file_data else
            "첨부된 파일이 없습니다."
        )
        attachment_type = file_data.get("classified_type") if file_data else None

        plan_prompt = build_plan_prompt(
            prompt=prompt,
            attachment_info=attachment_info,
            attachment_type=attachment_type,
            user_context=user_context,
        )

        with st.chat_message("assistant"):
            status_box = st.status("🤖 오케스트레이터가 계획을 수립 중...", expanded=True)

            try:
                plan_res = safe_generate(client, model_name, plan_prompt)
                raw_plan_text = plan_res.text if hasattr(plan_res, "text") else ""

                parsed_plan = guard.extract_json_object(raw_plan_text)
                if not parsed_plan["valid"]:
                    st.error(f"계획 수립 오류: {parsed_plan.get('error')}")
                    with st.expander("Planner 원문"):
                        st.code(raw_plan_text)
                    return

                plan = parsed_plan["data"]
                plan_check = guard.validate_plan_schema(plan, attachment_type=attachment_type)

                if not plan_check["valid"]:
                    status_box.write("⚠️ 계획이 invalid하여 자동 수정 시도 중...")
                    repaired = try_repair_plan_once(client, model_name, raw_plan_text, plan_check["errors"])
                    if not repaired["valid"]:
                        st.error("Planner 자동 수정 실패")
                        with st.expander("Planner 원문"):
                            st.code(raw_plan_text)
                        return

                    plan = repaired["data"]
                    plan_check = guard.validate_plan_schema(plan, attachment_type=attachment_type)

                if not plan_check["valid"]:
                    st.error("계획 검증 실패")
                    st.json({"errors": plan_check["errors"], "warnings": plan_check["warnings"]})
                    with st.expander("Planner 원문"):
                        st.code(raw_plan_text)
                    return

                st.session_state.last_plan = plan

                status_box.write(f"📋 전략: {plan.get('thought', '-')}")
                if plan_check["warnings"]:
                    status_box.write(f"⚠️ 경고: {', '.join(plan_check['warnings'])}")

                st.subheader("🗺️ 실행 계획")
                st.json(plan)

                execution_bundle = {
                    "ready_to_run": True,
                    "prompt": prompt,
                    "file_data": file_data,
                    "user_context": user_context,
                }

                st.session_state.last_execution = execution_bundle

                if preview_only:
                    status_box.update(label="📝 계획 수립 완료 (실행 대기)", state="complete", expanded=False)
                    st.info("계획 먼저 보기 모드입니다. 아래 버튼으로 실행하세요.")

            except Exception as e:
                st.error(f"계획 수립 중 오류: {e}")
                return

    # ---------------------------------------------------------
    # 계획 실행
    # ---------------------------------------------------------
    if st.session_state.last_plan and st.session_state.last_execution:
        if st.button("🚀 현재 계획 실행", type="primary", use_container_width=True):
            if not api_key:
                st.warning("API Key가 필요합니다.")
                return

            client = genai.Client(api_key=api_key)
            plan = st.session_state.last_plan
            execution_bundle = st.session_state.last_execution

            with st.chat_message("assistant"):
                status_box = st.status("🔄 계획 실행 중...", expanded=True)

                execution_state = {
                    "step_outputs": {},
                    "ordered_results": [],
                }

                try:
                    for idx, step in enumerate(plan["steps"], start=1):
                        status_box.write(f"🔄 [Step {idx}] {step['agent']} 실행 중...")
                        step_result = execute_agent_step(
                            client=client,
                            model_name=model_name,
                            step=step,
                            file_data=execution_bundle["file_data"],
                            global_context=execution_bundle["user_context"],
                            execution_state=execution_state,
                        )

                        execution_state["step_outputs"][step["id"]] = step_result["data"]
                        execution_state["ordered_results"].append(step_result)

                        status_box.write(f"✅ [Step {idx}] {step['agent']} 완료: {step_result['data'].get('summary', '')}")

                        # 다음 step용 컨텍스트에 최소 요약만 누적
                        execution_bundle["user_context"] += (
                            f"\n\n[Step Output Summary: {step['id']} / {step['agent']}]\n"
                            f"{step_result['data'].get('summary', '')}\n"
                            f"Key Findings: {json.dumps(step_result['data'].get('key_findings', []), ensure_ascii=False)}"
                        )

                    final_report = build_final_report(plan, execution_state)

                    status_box.update(label="✅ 모든 작업 완료!", state="complete", expanded=False)

                    st.markdown(final_report)

                    with st.expander("🔎 Step 원문 JSON 보기"):
                        raw_dump = {
                            item["step_id"]: item["data"]
                            for item in execution_state["ordered_results"]
                        }
                        st.code(json.dumps(raw_dump, ensure_ascii=False, indent=2), language="json")

                    st.session_state.messages.append(
                        {"role": "assistant", "content": final_report}
                    )

                    log_usage("Agent Orchestrator")

                except Exception as e:
                    st.error(f"작업 실행 중 오류: {e}")


if __name__ == "__main__":
    main()