import streamlit as st
from google import genai
from google.genai import types
import pandas as pd
import os
import json
import io 
import datetime
from datetime import datetime
from io import StringIO
from pypdf import PdfReader
import tempfile
from utils import log_usage, render_sidebar_settings, safe_generate_content
from rag_utils import UnityRAG

# ==========================================
# 1. 설정 및 상수 정의
# ==========================================
st.set_page_config(layout="wide", page_title="AI 기획서 평가 봇")
CRITERIA_FOLDER = "criteria"
CONFIG_FILE = "config.json"

api_key_input, cx_id, model_name = render_sidebar_settings()
# ==========================================
# 2. 유틸리티 함수 (파일 처리)
# ==========================================
def load_api_key():
    """로컬 설정 파일에서 API 키를 불러옵니다."""
    if os.path.exists(CONFIG_FILE):
        try:
            with open(CONFIG_FILE, "r", encoding="utf-8") as f:
                config = json.load(f)
                return config.get("api_key", "")
        except:
            return ""
    return ""

def save_api_key(key):
    """API 키를 로컬 설정 파일에 저장합니다."""
    with open(CONFIG_FILE, "w", encoding="utf-8") as f:
        json.dump({"api_key": key}, f)

def read_criteria_files(folder_path):
    combined_criteria = ""
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
        return "평가 기준 폴더가 비어있습니다."

    for filename in os.listdir(folder_path):
        filepath = os.path.join(folder_path, filename)
        try:
            # MD 파일도 텍스트처럼 처리
            if filename.lower().endswith((".txt", ".md")):
                with open(filepath, "r", encoding="utf-8") as f:
                    combined_criteria += f"\n--- [{filename}] ---\n{f.read()}"
            elif filename.lower().endswith(".pdf"):
                reader = PdfReader(filepath)
                text = ""
                for page in reader.pages:
                    text += page.extract_text() + "\n"
                combined_criteria += f"\n--- [{filename}] ---\n{text}"
        except Exception as e:
            st.error(f"{filename} 읽기 실패: {e}")
            
    return combined_criteria

def extract_text_from_files(uploaded_file):
    if uploaded_file is None:
        return ""
    
    # 파일 포인터를 맨 앞으로 초기화 (이게 없으면 읽지 못하는 경우가 많음)
    uploaded_file.seek(0)
    file_ext = uploaded_file.name.split('.')[-1].lower()

    if file_ext == "pdf":
        try:
            # Streamlit의 uploaded_file은 그 자체로 file-like 객체이므로 
            # 굳이 io.BytesIO로 한 번 더 감쌀 필요가 없습니다.
            reader = PdfReader(uploaded_file)
            text = ""
            for i, page in enumerate(reader.pages):
                extracted = page.extract_text()
                if extracted:
                    text += extracted + "\n"
            
            # 텍스트 추출 결과가 비어있을 경우 (이미지 스캔본 등)
            if not text.strip():
                st.error("PDF에서 텍스트를 추출할 수 없습니다. (이미지 스캔본이거나 텍스트 레이어가 손상된 파일일 수 있습니다.)")
            
            return text

        except Exception as e:
            # 에러 발생 시 원인을 화면에 출력
            st.error(f"PDF 읽기 오류 발생: {e}")
            return ""
    else: 
        # txt, md 등
        try:
            stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
            return stringio.read()
        except Exception as e:
            st.error(f"텍스트 파일 읽기 오류: {e}")
            return ""

def parse_data_files(data_files):
    """CSV/Excel 데이터를 텍스트로 변환"""
    data_summary = ""
    for file in data_files:
        try:
            if file.name.endswith('.csv'):
                df = pd.read_csv(file)
            else:
                df = pd.read_excel(file)
            
            data_summary += f"\n--- 데이터 첨부: {file.name} (상위 5행) ---\n"
            data_summary += df.head(5).to_markdown(index=False)
            data_summary += "\n...\n"
        except Exception as e:
            data_summary += f"\n[데이터 파일 읽기 오류: {file.name}]\n"
    return data_summary

def read_text_file(uploaded_file):
    try:
        stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
        return stringio.read()
    except Exception as e:
        return f"텍스트 읽기 오류: {e}" 

def upload_to_gemini(uploaded_file, api_key):
    """Streamlit 메모리 파일을 로컬 임시 파일로 저장 후 업로드"""
    # 1. 임시 파일 생성
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
        tmp.write(uploaded_file.getvalue())
        tmp_path = tmp.name
    
    # 2. 업로드
    try:
        client = genai.Client(api_key=api_key)
        # mime_type 지정 방식이 변경됨 (upload 메서드 내 config 사용 불필요, 자동 감지 혹은 별도 설정)
        # 새 SDK에서는 path만 주면 알아서 처리합니다.
        uploaded_file_ref = client.files.upload(
            file=tmp_path,
            config={'mime_type': 'application/pdf'} # 명시적으로 PDF임을 지정 (선택사항)
        )
        return uploaded_file_ref
    except Exception as e:
        st.error(f"Gemini 파일 업로드 실패: {e}")
        return None
    finally:
        # 3. 임시 파일 삭제 (리소스 정리)
        # 업로드가 성공하든 실패하든 임시 파일은 지워주는 것이 좋습니다.
        if os.path.exists(tmp_path):
            os.remove(tmp_path)

def summarize_large_text_if_needed(text, api_key, chunk_size=30000):
    """
    텍스트가 너무 길면(기본 3만자 이상), 쪼개서 요약한 뒤 핵심만 반환합니다.
    Gemini 1.5 Flash는 100만 토큰까지 가능하지만, 전송 속도와 비용 절약을 위해 사용합니다.
    """
    if len(text) <= chunk_size:
        return text

    # 1. 텍스트 쪼개기 (Chunking)
    chunks = [text[i:i+chunk_size] for i in range(0, len(text), chunk_size)]
    summaries = []

    client = genai.Client(api_key=api_key)
        
    st.info(f"📜 문서가 너무 길어서 {len(chunks)}개로 나누어 핵심 내용을 요약 중입니다...")
    
    # 2. 각 파트 요약 (Map)
    progress_bar = st.progress(0)
    for idx, chunk in enumerate(chunks):
        try:
            #레거시 프롬프트
            #prompt = f"아래 텍스트는 게임 기획서의 일부입니다... (중략) ...:\n\n{chunk}"
            prompt = f"""
            [지시사항]
            당신은 게임 기획서 데이터를 압축하는 역할을 맡았습니다.
            아래 텍스트에서 **시스템 규칙, 수치 데이터, 클래스 구조, 고유 명사**는 절대 생략하지 말고 보존하십시오.
            서술형 문장은 간결한 개조식(Bullet point)으로 변환하여 토큰을 절약하십시오.
            
            [원본 텍스트]
            {chunk}
            """


            # [변경] generate_content 호출 방식 변경
            response = safe_generate_content(client, model_name, prompt)
            '''response = client.models.generate_content(
                model=model_name,
                contents=prompt
            )'''
            summaries.append(response.text)
            progress_bar.progress((idx + 1) / len(chunks))
        except Exception as e:
            summaries.append(f"[요약 실패: {e}]")
            
    return "\n".join(summaries)

# ==========================================
# 3. HTML 리포트 생성 (다운로드용)
# ==========================================
def create_html_report(result_json):
    """결과 JSON을 기반으로 스크린샷과 유사한 스타일의 HTML 생성"""
    
    details_html = ""
    for item in result_json.get("details", []):
        details_html += f"""
        <div class="card">
            <div class="card-header">
                <span class="criteria-title">{item['criteria']}</span>
                <span class="criteria-score">{item['score']}/10</span>
            </div>
            <div class="progress-bar">
                <div class="fill" style="width: {item['score'] * 10}%;"></div>
            </div>
            <div class="comment">{item['comment']}</div>
        </div>
        """

    improvements = "".join([f"<li>{txt}</li>" for txt in result_json['feedback']['improvements']])
    expectations = "".join([f"<li>{txt}</li>" for txt in result_json['feedback']['expectations']])
    advice_text = result_json['feedback'].get('detailed_advice', '상세 조언이 없습니다.').replace("\n", "<br>")

    html_content = f"""
    <html>
    <head>
        <style>
            body {{ font-family: 'Malgun Gothic', sans-serif; background-color: #f4f4f4; padding: 20px; }}
            .container {{ max-width: 900px; margin: 0 auto; background: white; padding: 40px; border-radius: 10px; box-shadow: 0 4px 15px rgba(0,0,0,0.1); }}
            .header {{ text-align: center; margin-bottom: 40px; border-bottom: 2px solid #eee; padding-bottom: 20px; }}
            .total-score {{ font-size: 60px; font-weight: bold; color: #333; }}
            .grade {{ font-size: 60px; font-weight: bold; color: #4CAF50; margin-left: 10px; }}
            .summary {{ background: #f9f9f9; padding: 15px; border-radius: 8px; margin-bottom: 30px; font-style: italic; color: #555; }}
            .grid {{ display: grid; grid-template-columns: repeat(2, 1fr); gap: 20px; }}
            .card {{ border: 1px solid #eee; padding: 15px; border-radius: 8px; background: #fff; }}
            .card-header {{ display: flex; justify-content: space-between; align-items: center; margin-bottom: 10px; }}
            .criteria-title {{ font-weight: bold; font-size: 18px; }}
            .criteria-score {{ font-weight: bold; color: #666; }}
            .progress-bar {{ width: 100%; height: 6px; background: #eee; border-radius: 3px; margin-bottom: 10px; }}
            .fill {{ height: 100%; background: #6c5ce7; border-radius: 3px; }}
            .comment {{ font-size: 14px; color: #666; line-height: 1.5; }}
            .feedback-section {{ margin-top: 40px; padding: 20px; background: #f8f9fa; border-radius: 8px; }}
            h3 {{ border-left: 4px solid #6c5ce7; padding-left: 10px; }}
            ul {{ color: #444; }}
            .advice-box {{ margin-top: 30px; padding: 20px; background-color: #e8f0fe; border-left: 5px solid #4285f4; border-radius: 5px; }}
            .advice-title {{ font-weight: bold; color: #1967d2; font-size: 18px; margin-bottom: 10px; display: block; }}
        </style>
    </head>
    <body>
        <div class="container">
            <div class="header">
                <h2>게임 기획서 평가 리포트</h2>
                <div>
                    <span class="total-score">{result_json['totalScore']}</span>
                    <span style="font-size: 24px; color:#aaa;">/ 10</span>
                    <span class="grade">{result_json['grade']}</span>
                </div>
            </div>
            
            <div class="summary">
                <strong>총평:</strong> {result_json['summary']}
            </div>

            <div class="grid">
                {details_html}
            </div>

            <div class="feedback-section">
                <h3>🛠 개선이 필요한 점 5가지</h3> <ul>{improvements}</ul>
                <br>
                <h3>✨ 기대되는 점</h3>
                <ul>{expectations}</ul>
                
                <div class="advice-box">
                    <span class="advice-title">💡 구체적 개선 가이드 및 예시</span>
                    {advice_text}
                </div>
            </div>
        </div>
    </body>
    </html>
    """
    return html_content

# ==========================================
# 4. 메인 UI 로직
# ==========================================
def main():
    st.title("📄 AI 게임 기획서 평가 봇")
    st.markdown("로컬 기준 파일과 첨부 데이터를 기반으로 기획서를 분석합니다.")

    
    # saved_key = load_api_key()

    # 사이드바: 설정
    with st.sidebar:
        st.markdown("**평가 기준 폴더 상태:**")
        if os.path.exists(CRITERIA_FOLDER) and os.listdir(CRITERIA_FOLDER):
            files = os.listdir(CRITERIA_FOLDER)
            st.success(f"{len(files)}개의 기준 파일 로드됨")
            st.code("\n".join(files), language=None)
        else:
            st.error(f"'{CRITERIA_FOLDER}' 폴더에 기준 파일을 넣어주세요.")

    # 메인 입력 영역
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.subheader("1. 기획서 입력")
        input_type = st.radio("입력 방식", ["파일 업로드 (PDF/TXT/MD)", "직접 입력"])
        uploaded_gdd = None
        gdd_text_input = ""
        if input_type == "파일 업로드 (PDF/TXT/MD)":
            uploaded_gdd = st.file_uploader("기획서 파일", type=['pdf', 'txt', 'md'], accept_multiple_files=True)
        else:
            gdd_text_input = st.text_area("기획서 내용 붙여넣기", height=300)

        with col2:
            st.subheader("2. 데이터 첨부 (선택)")
            uploaded_data = st.file_uploader("밸런스 테이블 (CSV/Excel)", type=['csv', 'xlsx'], accept_multiple_files=True)  

    # 분석 버튼
    if st.button("🚀 분석 시작 (Analyze)", type="primary"):
        # 입력된 키가 없으면 저장된 키를 다시 시도, 그래도 없으면 경고
        if not api_key_input:
            st.warning("API Key를 입력해주세요.")
            return
        
        # 1. Gemini 설정 (파일 업로드를 위해 먼저 설정 필요)
        #genai.configure(api_key=api_key_input)      
        client = genai.Client(api_key=api_key_input)
        #model = genai.GenerativeModel(model_name)

        rag = UnityRAG(api_key_input)

        with st.spinner("🕵️ 내부 심사 가이드라인(Evaluation Criteria) 조회 중..."):
            # 'Evaluation Criteria', 'Project Goals', 'Restrictions' 등의 키워드로 검색
            # 예: "모바일 최적화 기준", "필수 포함 요소" 등이 담긴 문서를 찾아옴
            internal_guidelines = rag.retrieve_context("Game Design Evaluation Criteria Priority Guidelines", k=3)

        # 1. 기준 로드
        criteria_text = read_criteria_files(CRITERIA_FOLDER)
        
        # 2. 데이터 파싱
        data_context = parse_data_files(uploaded_data) if uploaded_data else "첨부 데이터 없음"
        
        # 3. 프롬프트 조립
        system_prompt = f"""
        당신은 냉철한 게임 기획 팀장입니다. 제공된 [기획서]를 [평가 기준]과 [데이터]에 맞춰 평가하세요.
        이미지나 도표가 포함된 경우 시각적 정보를 분석하여 평가에 반영하세요.
        Unity 기반 URP 프로젝트, 시스템 설계, 데이터 구조, C#/OOP/SOLID 원칙을 기준으로 기획서를 평가할 수 있습니다.        

        # 평가 기준
        - 기획서의 구조적 완성도
        - 핵심 콘셉트의 명확성 및 독창성
        - Core Gameplay Loop의 논리성 및 현실적 구현 가능성
        - Unity URP에서의 구현 난이도 및 실현 가능성
        - 시스템 구성의 OOP/SOLID 적합성
        - 데이터 흐름(ScriptableObject/테이블/레벨 구조)의 일관성
        - 밸런스 및 콘텐츠 확장성 고려 여부
        - 문서의 가독성과 개발 지향성

        [RAG: 내부 심사 가이드라인 (최우선 반영)]
        우리 팀의 핵심 평가 기준입니다. 이 기준에 미달하면 감점 사유를 구체적으로 명시하세요.
        {internal_guidelines}

        [평가 기준 문서 내용]
        {criteria_text}

        [첨부 데이터 테이블]
        {data_context}

        [지시사항]        
        0. [RAG 내부 가이드라인]과 [업로드된 평가 기준]을 모두 반영하여 평가하세요.
        1. [평가 기준 문서]의 구조 및 기준을 우선적으로 반영하여 10점 만점 점수를 산정하라.
        2. 평가 결과는 반드시 JSON 포맷으로 출력하라.
        3. ‘improvements’ 항목에는 즉시 고쳐야 하는 5개의 단점을 간결하게 기술하라.
        4. ‘detailed_advice’ 항목에는 위 5개 단점을 각 항목별로 어떻게 개선해야 하는지, Unity·URP·OOP 모범 구조 및 실제 개발 사례 기반으로 매우 상세하게 설명하라.
        5. 감정적 의견, 추상적 칭찬, 공감 문구는 금지한다.
        6. 불확실한 정보는 추측하지 말고 문제점으로 지적하라.
        7. PDF 경우 이미지·도표·UI 레이아웃 구성도 평가 항목에 반영하라.
                
        {{
            "totalScore": float (10.0 만점),
            "grade": string (S/A/B/C/F),
            "summary": string (3문장 요약),
            "details": [
                {{ "criteria": "주제 선정", "score": int, "comment": "평가..." }},
                {{ "criteria": "첫인상", "score": int, "comment": "평가..." }},
                {{ "criteria": "가독성", "score": int, "comment": "평가..." }},
                {{ "criteria": "문장력과 맞춤법", "score": int, "comment": "평가..." }},
                {{ "criteria": "논리적 전개", "score": int, "comment": "평가..." }},
                {{ "criteria": "분석력", "score": int, "comment": "평가..." }},
                {{ "criteria": "통찰력", "score": int, "comment": "평가..." }},
                {{ "criteria": "창의력", "score": int, "comment": "평가..." }},
                {{ "criteria": "실무력", "score": int, "comment": "평가..." }},
                {{ "criteria": "분량", "score": int, "comment": "평가..." }}
            ],
            "feedback": {{
                "improvements": ["개선점1", "개선점2", "개선점3", "개선점4", "개선점5"],
                "expectations": ["기대점1", "기대점2", ...],
                "detailed_advice": "각 단점을 어떻게 개선해야 하는지 Unity/URP/OOP 기준으로 매우 구체적으로 작성."
            }}
        }}
        """

        request_content = []

        #full_prompt = f"{system_prompt}\n\n[기획서 내용]\n{gdd_text}"

        with st.spinner("파일 처리 및 업로드 중..."):
            request_content = [system_prompt]
            
            if input_type == "파일 업로드 (PDF/TXT/MD)" and uploaded_gdd:

                combined_text_content = ""
                pdf_files_refs = []

                for file in uploaded_gdd:
                    file_ext = file.name.split('.')[-1].lower()
                
                    if file_ext == "pdf":
                        # [핵심 변경점] PDF는 텍스트 추출 없이 '파일 객체'로 보냄
                        pdf_ref = upload_to_gemini(file, api_key_input)
                        if pdf_ref:
                            pdf_files_refs.append(pdf_ref)
                        else:
                            st.error(f"{file.name} 업로드 실패")
                    else:
                        # TXT/MD는 텍스트로 읽어서 보냄
                        text = read_text_file(file)
                        combined_text_content += f"\n\n--- [파일: {file.name}] ---\n{text}"

                if combined_text_content:
                    processed_text = summarize_large_text_if_needed(combined_text_content, api_key_input)
                    request_content.append(f"\n\n[기획서 텍스트 모음]\n{processed_text}")
                
                # 2. PDF 레퍼런스들이 있다면 프롬프트 리스트에 추가 (Gemini는 텍스트와 파일 객체를 리스트로 받음)
                if pdf_files_refs:
                    request_content.extend(pdf_files_refs)
            
            elif input_type == "직접 입력" and gdd_text_input:
                gdd_text_input = summarize_large_text_if_needed(gdd_text_input, api_key_input)
                full_prompt = f"{system_prompt}\n\n[기획서 텍스트]\n{gdd_text_input}"
                request_content = [full_prompt]
            else:
                st.warning("기획서 파일을 업로드하거나 내용을 입력해주세요.")
                return

        # 입력 방식에 따른 처리
        #if input_type == "파일 업로드 (PDF/TXT/MD)" and uploaded_gdd:
        #    file_ext = uploaded_gdd.name.split('.')[-1].lower()
            
        #    if file_ext == "pdf":
        #        # [핵심] PDF는 텍스트 추출 안 하고 통째로 Gemini에게 보냄
        #        with st.spinner("PDF를 Gemini가 읽을 수 있도록 변환 및 업로드 중..."):
        #            pdf_file = upload_to_gemini(uploaded_gdd, mime_type="application/pdf")
        #            gemini_input_content = [system_prompt, pdf_file] # 프롬프트 + PDF파일객체
        #    else:
        #        # TXT, MD는 기존처럼 텍스트로 읽음
        #        text_content = extract_text_from_files(uploaded_gdd)
        #        gemini_input_content = [system_prompt, text_content]
        #        
        #else:
        #    # 직접 입력
        #    if not gdd_text:
        #        st.warning("기획서 내용을 입력하세요.")
        #        return
        #    gemini_input_content = [system_prompt, gdd_text]

        # 4. API 호출
        with st.spinner("Gemini가 기획서를 분석 중입니다..."):
            try:
                response = client.models.generate_content(
                    model=model_name,
                    contents=request_content
                )
                
                result_text = response.text.replace("```json", "").replace("```", "").strip()
                #result_json = json.loads(result_text)
                result_json = json.loads(result_text, strict=False)
                                                
                # 5. 결과 시각화
                st.divider()
                st.subheader("📊 평가 결과")
                
                score_col, grade_col, summ_col = st.columns([1, 1, 3])
                score_col.metric("총점", f"{result_json['totalScore']} / 10")
                grade_col.metric("등급", result_json['grade'])
                summ_col.info(result_json['summary'])

                st.markdown("#### 세부 항목 평가")
                details = result_json['details']
                rows = [details[i:i+3] for i in range(0, len(details), 3)]
                
                for row in rows:
                    cols = st.columns(3)
                    for idx, item in enumerate(row):
                        with cols[idx]:
                            st.markdown(f"**{item['criteria']}** ({item['score']}/10)")
                            st.progress(item['score'] / 10)
                            st.caption(item['comment'])
                
                st.markdown("#### 💡 피드백")
                f_col1, f_col2 = st.columns(2)
                with f_col1:
                    st.error("개선해야 할 점")
                    for imp in result_json['feedback']['improvements']:
                        st.markdown(f"- {imp}")
                with f_col2:
                    st.success("기대되는 점")
                    for exp in result_json['feedback']['expectations']:
                        st.markdown(f"- {exp}")

                st.markdown("---") # 구분선
                st.subheader("💡 구체적 개선 가이드 및 예시")
                
                # JSON에서 조언 내용 가져오기 (없을 경우 대비)
                advice_text = result_json['feedback'].get('detailed_advice', '상세 조언 내용이 없습니다.')
                
                # Streamlit의 파란색 알림 박스(info)로 출력
                st.info(advice_text)

                # 6. 리포트 다운로드
                st.divider()
                html_report = create_html_report(result_json)
                st.download_button("📥 리포트 다운로드", html_report, f"report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.html", "text/html")

            except Exception as e:
                st.error(f"오류가 발생했습니다: {e}")
                st.error("JSON 파싱 오류일 수 있습니다. 다시 시도해주세요.")

if __name__ == "__main__":
    main()