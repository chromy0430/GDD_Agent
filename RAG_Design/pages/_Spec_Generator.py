import streamlit as st
import google.generativeai as genai
import os
import json
import tempfile
import io
from io import StringIO
from pypdf import PdfReader
from utils import log_usage, render_sidebar_settings
from rag_utils import UnityRAG

# ==========================================
# 1. 설정 및 상수
# ==========================================
st.set_page_config(layout="wide", page_title="개발 명세서 생성기")
# ==========================================
# 2. 유틸리티 함수 (app.py와 공유 가능하지만 독립성을 위해 포함)
# ==========================================

def read_text_file(uploaded_file):
    try:
        stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
        return stringio.read()
    except Exception as e:
        return f"읽기 오류: {e}"

def upload_to_gemini(uploaded_file):
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
        tmp.write(uploaded_file.getvalue())
        tmp_path = tmp.name
    try:
        return genai.upload_file(tmp_path, mime_type="application/pdf")
    except Exception as e:
        st.error(f"업로드 실패: {e}")
        return None

# HTML 명세서 생성 (개발용 TDD 스타일)
def create_tech_spec_html(data):
    classes_html = ""
    for cls in data.get('classes', []):
        fields = "".join([f"<li><code>{f}</code></li>" for f in cls.get('fields', [])])
        methods = "".join([f"<li><code>{m}</code></li>" for m in cls.get('methods', [])])
        classes_html += f"""
        <div class="class-card">
            <div class="class-header">
                <span class="type-badge">{cls.get('type', 'Class')}</span>
                <span class="class-name">{cls['name']}</span>
            </div>
            <p>{cls['description']}</p>
            <div class="code-section">
                <strong>Fields:</strong><ul>{fields}</ul>
                <strong>Methods:</strong><ul>{methods}</ul>
            </div>
        </div>
        """

    tasks_html = ""
    for task in data.get('tasks', []):
        tasks_html += f"""
        <div class="task-item">
            <span class="priority {task.get('priority', 'Normal')}">{task.get('priority', 'Normal')}</span>
            <span class="task-desc">{task['description']}</span>
        </div>
        """

    return f"""
    <html>
    <head>
        <style>
            body {{ font-family: 'Consolas', 'Malgun Gothic', monospace; background: #1e1e1e; color: #d4d4d4; padding: 20px; }}
            .container {{ max-width: 1000px; margin: 0 auto; }}
            h1, h2 {{ color: #569cd6; border-bottom: 1px solid #333; padding-bottom: 10px; }}
            .summary {{ background: #252526; padding: 15px; border-left: 5px solid #ce9178; margin-bottom: 30px; }}
            .class-grid {{ display: grid; grid-template-columns: repeat(auto-fill, minmax(300px, 1fr)); gap: 20px; }}
            .class-card {{ background: #2d2d2d; border: 1px solid #3e3e42; border-radius: 5px; padding: 15px; }}
            .class-header {{ display: flex; align-items: center; margin-bottom: 10px; }}
            .type-badge {{ background: #4ec9b0; color: #1e1e1e; padding: 2px 6px; border-radius: 3px; font-weight: bold; font-size: 12px; margin-right: 8px; }}
            .class-name {{ font-size: 18px; font-weight: bold; color: #dcdcaa; }}
            .code-section {{ background: #1e1e1e; padding: 10px; border-radius: 3px; font-size: 13px; margin-top: 10px; }}
            ul {{ padding-left: 20px; margin: 5px 0; }}
            li {{ margin-bottom: 3px; }}
            code {{ color: #9cdcfe; }}
            .task-item {{ background: #333; padding: 10px; margin-bottom: 8px; border-radius: 4px; display: flex; align-items: center; }}
            .priority {{ padding: 2px 8px; border-radius: 3px; font-size: 12px; font-weight: bold; margin-right: 10px; min-width: 60px; text-align: center; }}
            .priority.High {{ background: #f44336; color: white; }}
            .priority.Medium {{ background: #ff9800; color: black; }}
            .priority.Low {{ background: #4caf50; color: white; }}
        </style>
    </head>
    <body>
        <div class="container">
            <h1>🛠 Technical Design Document (TDD)</h1>
            <div class="summary">
                <h3>System Architecture</h3>
                <p>{data.get('architecture', '내용 없음')}</p>
            </div>

            <h2>📦 Class & Data Structure</h2>
            <div class="class-grid">
                {classes_html}
            </div>

            <h2>✅ Development Tasks</h2>
            {tasks_html}
        </div>
    </body>
    </html>
    """

# ==========================================
# 3. 메인 로직
# ==========================================
def main():
    st.title("📋 기획서 → 개발 명세서 변환기")
    api_key, _, model_name = render_sidebar_settings()
    st.markdown("기획서를 넣으면 **Unity C# 클래스 구조**와 **개발 할 일 목록(To-Do)**을 뽑아줍니다.")
   
    # 입력 UI
    uploaded_file = st.file_uploader("기획서 파일 (PDF/TXT/MD)", type=['pdf', 'txt', 'md'])
    text_input = st.text_area("또는 기획 내용 직접 입력", height=200)

    if st.button("🛠️ 개발 명세서 생성 (Generate Spec)", type="primary"):
        if not api_key:
            st.warning("API Key가 필요합니다.")
            return
        
        # 입력 확인
        content = []
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel(model_name)

        # [RAG 단계]
        rag = UnityRAG(api_key)
        with st.spinner("📚 내부 개발 가이드라인(Zero-GC, Architecture) 검색 중..."):
            tech_knowledge = rag.retrieve_context("Unity 6.3 Architecture ScriptableObject Zero-GC Pattern", k=3)

        system_prompt = """
        # 역할 (Role)
        당신은 Unity 6.3 환경의 **Technical Game Designer**입니다.
        추상적인 아이디어를 프로그래머가 작업 가능한 **Data-Driven Architecture 명세서**로 변환합니다.

        # 1. 기술 가이드라인 (Strict Rules)
        1. **Data Separation:** 모든 기획 데이터(Stat, Skill Info)는 반드시 `ScriptableObject` 구조로 설계하십시오.
        2. **Unity 6 Features:** UI는 `UIToolkit`, 비동기 처리는 `Awaitable`, 렌더링은 `RenderGraph`를 기준으로 작성하십시오.
        3. **Interface First:** 구체적인 클래스보다 `IDamageable`, `IInteractable` 등 인터페이스 기반 설계를 우선하십시오.

        # 2. 작성 가이드
        - **[Class]**: 모호한 설명 금지. 필드명과 타입을 명시하십시오. (예: `moveSpeed (float)`, `itemDatabase (List<ItemSO>)`)
        - **[Logic]**: '공격한다' 대신 'Input Action이 트리거되면 AttackState로 전환하고 Hitbox를 활성화한다'와 같이 상태 머신 관점에서 서술하십시오.

        # 3. 출력 포맷 (JSON Only)
        반드시 아래 JSON 구조로만 출력하세요. 마크다운 코드는 포함하지 마세요.
        {
            "architecture": "시스템 전체 구조에 대한 요약 설명 (Core Loop와 데이터 흐름 위주)",
            "classes": [
                {
                    "name": "클래스명 (예: PlayerController)",
                    "type": "MonoBehaviour 또는 ScriptableObject 또는 Pure C# Class",
                    "description": "이 클래스의 역할",
                    "fields": ["private float moveSpeed", "public int hp"],
                    "methods": ["public void Move()", "private void Die()"]
                }
            ],
            "tasks": [
                {
                    "priority": "High 또는 Medium 또는 Low",
                    "description": "구체적인 작업 내용 (예: PlayerController 이동 로직 구현)"
                }
            ]
        }
        """        

        with st.spinner("기획서를 분석하여 시스템 아키텍처를 설계 중입니다..."):
            try:
                # 파일 처리
                if uploaded_file:
                    ext = uploaded_file.name.split('.')[-1].lower()
                    if ext == 'pdf':
                        pdf_ref = upload_to_gemini(uploaded_file)
                        content = [system_prompt, pdf_ref]
                    else:
                        text = read_text_file(uploaded_file)
                        content = [system_prompt, f"[기획서 내용]\n{text}"]
                elif text_input:
                    content = [system_prompt, f"[기획서 내용]\n{text_input}"]
                else:
                    st.warning("기획서를 입력해주세요.")
                    return

                # API 호출
                log_usage("개발 명세서 봇")
                response = model.generate_content(content)
                result = json.loads(response.text.replace("```json", "").replace("```", "").strip())

                # 결과 화면 출력
                st.divider()
                
                # 탭으로 구분해서 보여주기
                tab1, tab2, tab3 = st.tabs(["🏗️ 시스템 구조", "📦 클래스 설계", "✅ 할 일 목록"])

                with tab1:
                    st.subheader("시스템 아키텍처")
                    st.info(result['architecture'])
                    
                with tab2:
                    st.subheader("필요한 클래스 & 데이터")
                    for cls in result['classes']:
                        with st.expander(f"🔹 {cls['name']} ({cls['type']})"):
                            st.write(f"**역할:** {cls['description']}")
                            c1, c2 = st.columns(2)
                            with c1:
                                st.markdown("**Variables (Fields)**")
                                for f in cls['fields']: st.code(f, language='csharp')
                            with c2:
                                st.markdown("**Functions (Methods)**")
                                for m in cls['methods']: st.code(m, language='csharp')

                with tab3:
                    st.subheader("개발 작업 리스트 (To-Do)")
                    for task in result['tasks']:
                        prio_color = "🔴" if task['priority'] == "High" else "🟡" if task['priority'] == "Medium" else "🟢"
                        st.markdown(f"{prio_color} **[{task['priority']}]** {task['description']}")

                # 다운로드 버튼
                st.divider()
                html_spec = create_tech_spec_html(result)
                st.download_button("💾 개발 명세서 다운로드 (TDD)", html_spec, "tech_spec.html", "text/html")

            except Exception as e:
                st.error(f"설계 중 오류 발생: {e}")

if __name__ == "__main__":
    main()