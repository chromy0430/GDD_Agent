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
#MODEL_NAME = "gemini-2.5-flash-lite"
#CONFIG_FILE = "config.json" # 루트 경로의 설정 파일 공유

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
        당신은 Unity 6.3 기반의 테크니컬 디렉터입니다. 기획서를 바탕으로 **확장성 높고 데이터 주도적인(Data-Driven)** 시스템 아키텍처를 설계하세요.

        [RAG: 내부 개발 가이드라인 (반드시 준수)]
        아래 내용은 우리 팀의 핵심 기술 규칙입니다. 설계 시 최우선으로 반영하세요.
        {tech_knowledge}

        [설계 원칙]
        1. **데이터와 로직의 분리:**
        - 모든 기획 데이터(스탯, 설정값)는 `ScriptableObject`로 정의하여 에디터에서 관리하기 쉽게 설계하십시오.
        - 런타임 데이터는 `struct` 기반으로 설계하여 메모리 레이아웃 효율을 높이십시오.
        2. **느슨한 결합 (Loose Coupling):**
        - 클래스 간 직접 참조를 피하고, `Interface` 주입 방식이나 `Event Channel` 패턴(SO 기반 이벤트)을 활용하십시오.
        3. **Unity 6 기능 활용:**
        - UI 시스템은 **UIToolkit** 기준으로 설계하고, 뷰와 데이터 바인딩 구조를 고려하십시오.
        - 물리 연산이 많다면 Unity Physics(DOTS) 도입 가능성을 검토하십시오. 하지만 대부분은 기존 물리 엔진으로 충분합니다.
        - 멀티스레딩은 `Unity Jobs System`과 `Burst Compiler`를 활용하여 성능을 극대화하십시오.        
        4. 싱글톤 남발을 자제하고, 매니저 클래스와 데이터 컨테이너를 명확히 분리하세요.

        [출력 포맷 (JSON Only)]
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