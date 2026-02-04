import streamlit as st
from google import genai
from google.genai import types
import time
import json
import tempfile
import os
from rag_utils import UnityRAG
from foundry import guard
from utils import render_sidebar_settings, retry_with_backoff

# ==========================================
# 1. 설정 및 헬퍼 함수
# ==========================================
st.set_page_config(layout="wide", page_title="Agent Headquarters")

def process_uploaded_file(uploaded_file, client):
    """
    업로드된 파일을 유형별로 처리하여 Gemini가 이해할 수 있는 형태(Text 또는 File Object)로 변환합니다.
    """
    file_type = uploaded_file.type
    file_name = uploaded_file.name
    
    # 1. 텍스트 파일 (MD, TXT, Code)
    if file_type in ["text/plain", "text/markdown", "text/x-python"]:
        return {
            "type": "text",
            "content": uploaded_file.getvalue().decode("utf-8"),
            "desc": f"텍스트 문서 ({file_name})"
        }
    
    # 2. 멀티모달 파일 (PDF, Video) - Gemini 서버 업로드 필요
    else:
        # 임시 파일로 저장 (접미사 자동 감지)
        suffix = ".mp4" if "video" in file_type else ".pdf"
        with tempfile.NamedTemporaryFile(delete=False, suffix=suffix) as tmp:
            tmp.write(uploaded_file.getvalue())
            tmp_path = tmp.name

        try:
            with st.spinner(f"📡 '{file_name}' 파일을 AI 서버로 전송 및 인덱싱 중..."):
                # [수정] 신규 SDK 방식 (path 기반 업로드)
                file_ref = client.files.upload(file=tmp_path)
                
                # 처리 대기 (Active 상태가 될 때까지)
                while file_ref.state.name == "PROCESSING":
                    time.sleep(2)
                    file_ref = client.files.get(name=file_ref.name)
                
                if file_ref.state.name != "ACTIVE":
                    st.error(f"파일 처리 실패: {file_ref.state.name}")
                    return None
                
                return {
                    "type": "file_ref",
                    "content": file_ref,
                    "desc": f"멀티모달 파일 ({file_name}, Type: {file_type})"
                }
        finally:
            if os.path.exists(tmp_path):
                os.remove(tmp_path)

# ==========================================
# 2. 메인 로직
# ==========================================
def main():
    st.title("🧠 Agent 365: 통합 지휘 통제실 (Orchestrator)")
    st.markdown("텍스트, PDF, 영상을 업로드하면 **오케스트레이터**가 내용을 보고 적절한 전문가(Agent)를 호출합니다.")

    api_key, _, model_name = render_sidebar_settings()
    
    # 세션 초기화
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # ---------------------------------------------------------
    # [UI] 파일 업로더 & 채팅 인터페이스
    # ---------------------------------------------------------
    with st.expander("📂 파일 첨부 (PDF, 문서, 영상)", expanded=True):
        uploaded_file = st.file_uploader(
            "분석할 자료를 여기에 드래그하세요.", 
            type=['txt', 'md', 'pdf', 'mp4', 'mov', 'py']
        )

    # 채팅 기록 표시
    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            if "file_info" in msg:
                st.caption(f"📎 첨부: {msg['file_info']}")
            st.markdown(msg["content"])

    # 사용자 입력
    if prompt := st.chat_input("명령을 입력하세요 (예: 이 영상 분석해서 기획서로 만들어줘)"):
        if not api_key:
            st.warning("API Key가 필요합니다.")
            return

        # [수정] Client 인스턴스 생성 (신규 SDK)
        client = genai.Client(api_key=api_key)
        
        # 1. 파일 처리 (있다면)
        file_data = None
        if uploaded_file:
            file_data = process_uploaded_file(uploaded_file, client)
            # 에러 발생 시(None 반환) 중단
            if uploaded_file and not file_data: return 

        # 메시지 기록 저장
        user_msg_obj = {"role": "user", "content": prompt}
        if file_data:
            user_msg_obj["file_info"] = file_data["desc"]
        
        st.session_state.messages.append(user_msg_obj)
        with st.chat_message("user"):
            if file_data: st.caption(f"📎 {file_data['desc']}")
            st.markdown(prompt)

        # ---------------------------------------------------------
        # [Step 1] Fabric IQ: 지식 검색
        # ---------------------------------------------------------
        rag = UnityRAG(api_key)
        with st.spinner("💾 Fabric IQ: 관련 지식 검색 중..."):
            user_context = rag.retrieve_context(prompt, k=2)

        # ---------------------------------------------------------
        # [Step 2] Work IQ: 계획 수립 (Planning)
        # ---------------------------------------------------------
        # 파일 존재 여부 메시지 구성
        attachment_info = f"사용자가 파일({file_data['desc']})을 첨부했습니다. 내용을 분석해야 합니다." if file_data else "첨부된 파일이 없습니다."

        plan_prompt = f"""
        당신은 AI 에이전트 매니저입니다.
        사용자의 [요청]과 [첨부파일]을 보고, 어떤 에이전트에게 일을 시킬지 결정하세요.

        [Available Agents]
        1. **Video_Analyst**: 영상 파일(.mp4, .mov)이 첨부되었을 때 시각적 분석 담당.
        2. **Spec_Generator**: 기획서 작성, 문서(PDF/TXT) 분석, 텍스트 요약.
        3. **Code_Reviewer**: 코드 파일(.py) 분석, 프로그래밍 질문 해결.
        4. **Market_Analyst**: 시장 조사, 데이터 분석.

        [Input Info]
        - Request: {prompt}
        - Attachment: {attachment_info}

        [Output Format (JSON)]
        {{
            "thought": "사용자가 영상을 올렸으므로 Video_Analyst에게 먼저 분석을 시키고, 그 결과를 바탕으로 Spec_Generator에게 문서를 쓰게 해야 함.",
            "steps": [
                {{
                    "agent": "Video_Analyst",
                    "instruction": "이 영상의 게임플레이 메카닉과 UI 구조를 상세히 분석해줘."
                }},
                {{
                    "agent": "Spec_Generator",
                    "instruction": "위 영상 분석 내용을 바탕으로 개발 명세서를 작성해줘."
                }}
            ]
        }}
        """

        with st.chat_message("assistant"):
            status_box = st.status("🤖 오케스트레이터가 작업을 조율 중...", expanded=True)
            
            try:
                # [수정] client.models.generate_content 사용 (GenerativeModel 클래스 X)
                plan_res = client.models.generate_content(
                    model=model_name,
                    contents=plan_prompt
                )
                
                validated_plan = guard.validate_json_structure(plan_res.text)
                
                if not validated_plan["valid"]:
                    st.error("계획 수립 오류 발생: JSON 파싱 실패")
                    st.stop()
                
                plan = validated_plan["data"]
                status_box.write(f"📋 **전략:** {plan['thought']}")
                
                final_report = "## 📝 통합 실행 리포트\n"
                
                # 에이전트 실행 루프
                for i, step in enumerate(plan["steps"]):
                    agent_name = step["agent"]
                    instruction = step["instruction"]
                    status_box.write(f"🔄 **[Step {i+1}] {agent_name}** 가 작업 중...")
                    
                    # 에이전트에게 보낼 컨텐츠 구성 (시스템 프롬프트 + 맥락 + 지시사항 + 파일)
                    agent_contents = [
                        f"당신은 {agent_name}입니다. 아래 지시를 수행하세요.\n[지시]: {instruction}\n[참고 지식]: {user_context}"
                    ]
                    
                    # 파일 데이터가 있고, 첫 번째 스텝이거나 파일 분석이 필요한 경우 전달
                    # (여기서는 단순하게 모든 스텝에 파일을 보여주되, 텍스트/객체 구분)
                    if file_data:
                        if file_data["type"] == "text":
                            agent_contents[0] += f"\n\n[첨부 문서 내용]:\n{file_data['content']}"
                        elif file_data["type"] == "file_ref":
                            agent_contents.append(file_data["content"]) # 파일 객체 추가
                    
                    # [수정] 에이전트 실행도 client.models.generate_content 사용
                    agent_res = client.models.generate_content(
                        model=model_name,
                        contents=agent_contents
                    )
                    
                    # 결과 누적
                    output_text = agent_res.text
                    final_report += f"\n---\n### 👤 {agent_name} 결과\n{output_text}\n"
                    
                    # 이전 에이전트의 결과를 컨텍스트에 추가 (정보 전달)
                    user_context += f"\n\n[Previous Agent Output ({agent_name})]:\n{output_text}"
                    
                    time.sleep(1)

                status_box.update(label="✅ 모든 작업 완료!", state="complete", expanded=False)
                st.markdown(final_report)
                
                # 결과 기록
                st.session_state.messages.append({"role": "assistant", "content": final_report})

            except Exception as e:
                st.error(f"작업 실행 중 오류: {e}")

if __name__ == "__main__":
    main()