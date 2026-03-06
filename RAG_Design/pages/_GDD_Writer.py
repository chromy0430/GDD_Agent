import streamlit as st
import google.generativeai as genai
import pandas as pd
import os
import json
import tempfile
from io import StringIO
from pypdf import PdfReader
from utils import log_usage, render_sidebar_settings
from rag_utils import UnityRAG

# ==========================================
# 1. 설정 및 상수
# ==========================================
st.set_page_config(layout="wide", page_title="기획서 작성/업데이트 봇")
#MODEL_NAME = "gemini-2.5-flash" 
#CONFIG_FILE = "config.json"
SAMPLES_FOLDER = "samples"

# ==========================================
# 2. 유틸리티 함수
# ==========================================
def read_text_file(uploaded_file):
    """TXT, MD 파일 읽기"""
    try:
        stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
        return stringio.read()
    except Exception as e:
        return f"텍스트 읽기 오류: {e}"

def read_sample_files(folder_path):
    """샘플 폴더 자료 읽기 (구조 추출 최적화)"""
    combined_samples = ""
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
        return "샘플 폴더가 비어있습니다."

    files = os.listdir(folder_path)
    if not files: return "샘플 폴더가 비어있습니다."

    for filename in files:
        filepath = os.path.join(folder_path, filename)
        try:
            # 1. 텍스트 파일 (TXT, MD) 처리
            if filename.lower().endswith((".txt", ".md")):
                with open(filepath, "r", encoding="utf-8") as f:
                    content = f.read()
                    # 내용을 태그로 감싸서 명확히 구분
                    combined_samples += f"\n<Template_Style filename='{filename}'>\n"
                    combined_samples += "NOTE: 아래 내용은 오직 '문서 구조'와 '말투'만 참고하십시오. 실제 게임 데이터(아이템명, 수치 등)는 무시하십시오.\n"
                    combined_samples += content
                    combined_samples += f"\n</Template_Style>\n"

            # 2. CSV 파일 처리 (헤더와 데이터 타입만 추출)
            elif filename.lower().endswith(".csv"):
                df = pd.read_csv(filepath)
                combined_samples += f"\n<Template_Table filename='{filename}'>\n"
                # 값 대신 데이터 타입이나 공백을 넣어 구조만 보여줌
                empty_df = df.head(1).copy() 
                for col in empty_df.columns:
                    empty_df[col] = f"[{col}_Example_Value]" # 값을 추상화시킴
                
                combined_samples += empty_df.to_markdown(index=False)
                combined_samples += "\nNOTE: 위 테이블의 컬럼명(Header)만 사용하고, 값은 사용자 아이디어로 채우십시오.\n"
                combined_samples += f"</Template_Table>\n"

        except Exception as e:
            combined_samples += f"\n[파일 읽기 실패: {filename}] {e}\n"
    
    return combined_samples

def upload_to_gemini(uploaded_file):
    """이미지 PDF 인식을 위한 파일 업로드"""
    import os
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf", mode='wb') as tmp:
        tmp.write(uploaded_file.getvalue())
        tmp_path = tmp.name
    
    try:
        if not os.path.exists(tmp_path): return None
        return genai.upload_file(tmp_path, mime_type="application/pdf")
    except Exception as e:
        st.error(f"업로드 실패: {e}")
        return None
    finally:
        try:
            if os.path.exists(tmp_path): os.remove(tmp_path)
        except: pass

# ==========================================
# 3. 프롬프트 정의 (수정됨)
# ==========================================

# 1. 신규 기획서 작성용 프롬프트
PROMPT_CREATE = """
# 역할 (Role)
당신은 Unity 6.3 (LTS) 환경에 최적화된 **'테크니컬 게임 기획자'**이자 **'시스템 아키텍트'**입니다.
추상적인 아이디어를 구체적인 **'개발 명세서(Spec)'** 수준의 기획서로 변환하며, 프로그래머가 즉시 코드로 옮길 수 있는 구조를 설계합니다.

# 1. Unity 6.3 & URP 테크니컬 가이드라인 (Strict Rules)
기획서 작성 시 아래 기술 표준을 반드시 준수하여 내용을 서술하십시오.
1. **Component & Architecture:**
   - 막연한 설명 대신 Unity 컴포넌트 단위로 매핑하여 서술하십시오. (예: "체력 관리" → "`HealthComponent`와 `IDamageable` 인터페이스 활용")
   - 데이터는 하드코딩이 아닌 **`ScriptableObject`** 기반의 데이터 테이블 구조로 설계하십시오.
2. **Graphics & Rendering (URP):**
   - 시각 효과는 `Particle System` 대신 **`VFX Graph`**, 쉐이더는 **`Shader Graph`**, 렌더링 패스는 **`RenderGraph`**를 명시하십시오.
3. **Performance (Mobile/Optimization):**
   - GC(Garbage Collection)를 유발하는 문자열 연산이나 잦은 `Instantiate`를 지양하고, **Object Pooling** 및 **StringBuilder** 등의 최적화 기법을 기획 단계에 포함하십시오.

# 2. 입력 자료의 처리 가이드 (Critical Instruction)
- **[Template_Style / Template_Table] 태그 내용:**
    - 이것은 **'빈 서식(Form)'**입니다.
    - ⚠️ **경고:** 샘플 내의 고유 명사(예: 스킬명, 캐릭터 이름)나 수치를 결과물에 포함시키지 마십시오.
    - 예: 샘플에 '파이어볼'이 있어도, 사용자가 '해상 전투'를 원하면 '함포 사격'으로 바꿔서 채워야 합니다.
    - 오직 **목차 순서, 마크다운 표 구조, 어조(Tone)**만 복제하십시오.

# 3. 문서 작성 구조 (Output Structure)
아래 목차를 기반으로 작성하되, 개발자가 읽기 편한 Markdown 형식으로 출력하십시오.

## [1] 개요 (Overview)
- 장르 / 타겟 / 플랫폼 / USP (Unity 6 기능 활용 포인트 포함)

## [2] 핵심 루프 (Core Gameplay Loop)
- Input(유저 행동) → System Processing(로직 처리) → Output(피드백/보상)의 흐름 도식화

## [3] 시스템 설계 (Technical Design)
- **클래스/컴포넌트 설계:** 주요 기능을 담당할 스크립트 역할 정의
- **데이터 구조 (Data Structure):** ScriptableObject로 관리할 데이터 필드(CSV 예시 포함)
- **제어 흐름:** Input System(New) Action 정의

## [4] 아트 & 사운드 스펙 (URP Specs)
- 필요한 에셋 리스트 및 URP 렌더링 기술 적용 방안

# 4. 검증 및 제안
- SOLID 원칙이나 Unity 퍼포먼스(GC 등)에 위배되는 기획이 있다면 **[Technical Warning]** 태그와 함께 대안을 제시하십시오.
"""

# 2. 기획서 업데이트용 프롬프트
# [기존 PROMPT_UPDATE 수정]

PROMPT_UPDATE = """
# 역할 (Role)
당신은 프로젝트의 **'리드 테크니컬 기획자'**입니다.
이미 작성된 기획서(Legacy)의 아키텍처를 완벽히 이해하고 있으며, 새로운 요구사항(New Feature)을 기존 시스템에 **'충돌 없이 통합(Integration)'**하는 것이 임무입니다.

# 1. 통합 및 리팩토링 원칙 (Integration Rules)
단순히 텍스트를 이어 붙이지 말고, 기존 문서의 **구조(Structure)** 속에 자연스럽게 녹여내십시오.
1. **Tech Spec 일관성 유지:** - 추가되는 기능도 앞선 기획서와 동일하게 **Unity 6.3 컴포넌트/ScriptableObject 구조**로 변환하여 기술하십시오.
2. **기술 부채 방지:**
   - 새로운 기능이 기존의 최적화(Object Pooling 등) 구조를 해치는지 검토하십시오.

# 2. 입력 자료의 처리 가이드 (Critical Instruction)
- **[기존 기획서]:** 프로젝트의 **Master Data**입니다. 이 문서의 내용을 절대적으로 유지하며, 여기에 살을 붙여야 합니다.
- **[추가 아이디어]:** 새로 탑재할 기능입니다. 이를 기술 용어로 번역하여 문서에 삽입하십시오.
- **[Template_Style / Template_Table] 태그 내용 (중요):**
    - ⚠️ **경고:** 이것은 오직 **'서식(Format)'** 참고용입니다.
    - 이 태그 안의 **내용(텍스트, 수치, 고유명사)**을 절대 결과물에 가져오지 마십시오.
    - 예: 샘플에 '퍼즐 전투'가 있고 사용자가 'FPS'를 원하면, 샘플의 내용은 버리고 'FPS' 내용으로 채우십시오.

# 3. 작업 지시사항 (Workflow)
1. **문맥 파악:** 기존 기획서의 [시스템 설계] 파트를 분석하여 데이터 흐름을 파악하십시오.
2. **내용 삽입:** 새로운 아이디어를 [개요], [핵심 루프], [시스템 설계] 등 **적절한 섹션에 나누어 배치**하십시오.
3. **변경 표기:** 수정/추가된 라인 끝에 **`(New)`** 또는 **`(Update)`** 태그 부착.

# 4. 결과물 형식
- 기존 기획서의 Markdown 포맷을 유지하면서, 내용이 세련되게 통합된 완성형 문서를 출력하십시오.
"""

# ==========================================
# 4. 메인 로직
# ==========================================
def main():
    st.title("📝 기획서 작성 및 관리 봇 (The Architect)")
    api_key, _, model_name = render_sidebar_settings()
    st.markdown("""
    **입력된 기획서(PDF/텍스트)**를 기준으로 내용을 작성합니다.  
    `samples` 폴더의 자료는 오직 **양식과 스타일**만 참고합니다.
    """)

    
    with st.sidebar:
        st.divider()
        st.markdown("**📂 스타일/양식 가이드 (Format Only)**")
        if os.path.exists(SAMPLES_FOLDER) and os.listdir(SAMPLES_FOLDER):
            st.code("\n".join(os.listdir(SAMPLES_FOLDER)), language=None)
            st.caption("⚠️ 이 파일들의 내용은 베끼지 않고, '양식'만 따라합니다.")
        else:
            st.warning(f"'{SAMPLES_FOLDER}' 폴더가 비어있습니다.")

    tab1, tab2 = st.tabs(["✨ 기획서 신규 작성", "🔄 기획서 업데이트"])

    # ----------------------------------------------------
    # TAB 1: 신규 작성
    # ----------------------------------------------------
    with tab1:
        st.subheader("💡 아이디어 → 표준 양식 기획서")
        raw_ideas = st.text_area("아이디어 입력", height=300, placeholder="- 해상 전투 배틀쉽 게임...")
        
        if st.button("✨ 기획서 초안 생성", type="primary", key="create_btn"):
            if not api_key or not raw_ideas: 
                st.warning("API Key와 아이디어를 입력하세요.")
                return

            sample_context = read_sample_files(SAMPLES_FOLDER)
            genai.configure(api_key=api_key)
            model = genai.GenerativeModel(model_name)
            
            rag = UnityRAG(api_key)
            with st.spinner("🌍 세계관 및 기술 제약 사항 확인 중..."):
                # 사용자의 아이디어와 관련된 설정을 검색 (예: "해상 전투" -> 해상 관련 세계관/제약 검색)
                design_knowledge = rag.retrieve_context(f"Game Design Rules Lore Constraints: {raw_ideas}", k=4)

            # 프롬프트 순서 배치: 지시사항 -> 샘플(양식) -> 사용자입력(내용)
            full_prompt = f"""
            {PROMPT_CREATE}

            # ==================================================
            # PART 1. 스타일 레퍼런스 (DO NOT COPY CONTENT)
            # 아래 자료는 오직 '양식'을 파악하는 용도로만 사용하십시오.
            # ==================================================
            {sample_context}


            # ==================================================
            # PART 2. 프로젝트 컨텍스트 (RAG Data)
            # ==================================================
            {design_knowledge}


            # ==================================================
            # PART 3. 실제 작성해야 할 내용 (CORE CONTENT)
            # 위 양식을 사용하여, 아래 아이디어를 기획서로 변환하십시오.
            # ==================================================
            User Idea:
            {raw_ideas}
            """
            
            with st.spinner("게임 아이디어를 샘플 양식에 맞추는 중..."):
                try:
                    response = model.generate_content(full_prompt)
                    st.success("완료!")
                    st.markdown(response.text)
                    st.download_button("📥 다운로드 (.md)", response.text, "GDD.md")
                except Exception as e:
                    st.error(f"실패: {e}")

    # ----------------------------------------------------
    # TAB 2: 업데이트 (PDF 지원)
    # ----------------------------------------------------
    with tab2:
        st.subheader("🔄 기획서 업데이트")
        st.markdown("**기존 기획서(PDF 등)**를 기반으로 내용을 추가합니다.")
        
        c1, c2 = st.columns(2)
        with c1:
            uploaded_gdd = st.file_uploader("기존 기획서 (PDF/TXT/MD)", type=['pdf', 'txt', 'md'])
        with c2:
            new_ideas = st.text_area("추가할 아이디어", height=200, placeholder="예: 3스테이지 보스 패턴 추가...")

        if st.button("🔄 기획서 업데이트", type="primary", key="update_btn"):
            if not api_key: 
                st.warning("API Key가 필요합니다.")
                return
            if not uploaded_gdd:
                st.warning("기존 기획서 파일을 업로드해주세요.")
                return

            genai.configure(api_key=api_key)
            model = genai.GenerativeModel(model_name)
            sample_context = read_sample_files(SAMPLES_FOLDER)
            
            request_content = []
            
            with st.spinner("파일 분석 중..."):
                ext = uploaded_gdd.name.split('.')[-1].lower()
                
                # 프롬프트 구성: 역할 -> 샘플 -> 추가아이디어 -> [파일] 순서
                prompt_header = f"""
                {PROMPT_UPDATE}

                # ==================================================
                # [참고 자료 1] 스타일/양식 레퍼런스 (DO NOT COPY CONTENT)
                # 아래 내용은 무시하고, 오직 '작성 톤'과 '표 형식'만 참고하십시오.
                # ==================================================
                {sample_context}
                
                # ==================================================
                # [참고 자료 2] 추가 아이디어 (New Requirements)
                # 이 내용을 기존 기획서에 통합해야 합니다.
                # ==================================================
                {new_ideas if new_ideas else "추가 아이디어 없음 (기존 내용 정리 및 보완)"}

                # ==================================================
                # [작업 대상] 기존 기획서 (Master Data)
                # 아래 문서를 기반으로 작업을 수행하십시오.
                # ==================================================
                """
                
                if ext == 'pdf':
                    pdf_file = upload_to_gemini(uploaded_gdd)
                    if not pdf_file: return
                    request_content = [prompt_header, pdf_file]
                else:
                    text_content = read_text_file(uploaded_gdd)
                    request_content = [prompt_header + "\n" + text_content]

            with st.spinner("기획서를 업데이트 중입니다..."):
                try:
                    response = model.generate_content(request_content)
                    st.success("업데이트 완료!")
                    st.markdown(response.text)
                    st.download_button("📥 다운로드 (.md)", response.text, "Updated_GDD.md")
                except Exception as e:
                    st.error(f"실패: {e}")

if __name__ == "__main__":
    main()