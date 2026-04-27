import streamlit as st
import google.generativeai as genai
import pandas as pd
import os
import json
import io
from utils import log_usage, render_sidebar_settings
from rag_utils import UnityRAG

# ==========================================
# 1. 설정 및 상수
# ==========================================
st.set_page_config(layout="wide", page_title="게임 밸런스 시뮬레이터")

# ==========================================
# 2. 유틸리티 함수
# ==========================================
def parse_data_files(uploaded_files):
    """업로드된 CSV/Excel 파일을 마크다운 표 문자열로 변환"""
    context_str = ""
    for file in uploaded_files:
        try:
            if file.name.endswith('.csv'):
                df = pd.read_csv(file)
            else:
                df = pd.read_excel(file)
            
            # 데이터가 너무 많을 경우를 대비해 요약 정보를 먼저 넣음 (선택사항)
            # context_str += f"\n--- [Table: {file.name}] ---\n"
            # context_str += df.to_markdown(index=False)
            
            # 전체 데이터를 문자열로 변환 (Gemini 1.5 Flash는 컨텍스트가 커서 통째로 넣어도 됨)
            csv_string = df.to_csv(index=False)
            context_str += f"\n--- [Data Table: {file.name}] ---\n{csv_string}\n"
            
        except Exception as e:
            st.error(f"{file.name} 읽기 실패: {e}")
    return context_str

# ==========================================
# 3. 메인 로직
# ==========================================
def main():
    st.title("⚖️ 게임 밸런스 시뮬레이터")
    api_key, _, model_name = render_sidebar_settings()
    st.markdown("""
    몬스터, 아이템, 캐릭터 스탯 등의 **데이터 테이블(CSV/Excel)**을 업로드하고, 
    **"Lv 10 전사가 오크랑 싸우면 누가 이겨?"** 같은 질문을 던지세요.
    """)

    
    # 사이드바
    with st.sidebar:
        st.markdown("---")
        st.markdown("### 💡 사용 팁")
        st.caption("1. 몬스터 테이블, 캐릭터 테이블 등을 업로드하세요.")
        st.caption("2. 구체적인 시나리오를 입력하세요.")

    # 메인 UI
    col1, col2 = st.columns([1, 1.5])

    with col1:
        st.subheader("1. 데이터 업로드")
        uploaded_files = st.file_uploader(
            "밸런스 데이터 (CSV, Excel)", 
            type=['csv', 'xlsx'], 
            accept_multiple_files=True
        )
        
        # 업로드된 데이터 미리보기
        if uploaded_files:
            st.success(f"{len(uploaded_files)}개의 파일이 로드되었습니다.")
            with st.expander("데이터 미리보기"):
                for f in uploaded_files:
                    f.seek(0) # 포인터 초기화
                    if f.name.endswith('.csv'):
                        st.dataframe(pd.read_csv(f).head(3))
                    else:
                        st.dataframe(pd.read_excel(f).head(3))

    with col2:
        st.subheader("2. 시뮬레이션 요청")
        scenario = st.text_area(
            "시나리오 입력 (예: 5레벨 기사가 기본 검을 들고 3스테이지 보스와 싸울 때 TTK는?)",
            height=150,
            placeholder="예시: 현재 데이터 기준으로 1레벨 플레이어가 고블린을 잡을 때 몇 대를 때려야 죽나요? 물약 소모량은 얼마나 될까요?"
        )
        
        run_btn = st.button("⚔️ 시뮬레이션 시작", type="primary")

    # 결과 처리
    if run_btn:
        if not api_key:
            st.warning("API Key가 필요합니다.")
            return
        if not uploaded_files:
            st.warning("분석할 데이터 테이블을 먼저 업로드해주세요.")
            return
        if not scenario:
            st.warning("시나리오를 입력해주세요.")
            return

        # 데이터 파싱
        for f in uploaded_files: f.seek(0) # 포인터 초기화
        data_context = parse_data_files(uploaded_files)

        rag = UnityRAG(api_key)
        with st.spinner("⚖️ 밸런스 표준(Standard Table) 조회 중..."):
            # "TTK", "Monster Stats" 등 밸런싱 기준 문서를 검색
            balance_rules = rag.retrieve_context("Combat Balance Guidelines TTK Standard", k=2)

        # 프롬프트 구성
        system_prompt = f"""
        당신은 전문 게임 밸런스 디자이너이자 수학자입니다.
        데이터 테이블과 시나리오를 시뮬레이션하고, [밸런스 가이드라인]에 부합하는지 평가하세요.

        [RAG: 밸런스 가이드라인 (기준점)]
        {balance_rules}
        
        [데이터 테이블]
        {data_context}

        [지시사항]
        1. 뇌피셜이 아닌, 제공된 데이터의 수치(공격력, 방어력, 체력 등)를 사용하여 계산 과정을 보여주세요.
        2. TTK(Time To Kill), DPS(초당 데미지), 예상 피격 횟수 등을 구체적으로 명시하세요.
        3. 결과가 밸런스상 적절한지(너무 어렵거나 쉬운지) 판단하고, 수정이 필요하다면 어떤 수치를 조절해야 할지 제안하세요.
        4. 결과는 아래 JSON 포맷으로 출력하세요.

        {{
            "winner": "승리 대상 (예: 플레이어)",
            "duration": "전투 예상 시간 (초)",
            "player_hp_left": "플레이어 남은 체력 %",
            "log": [
                "1. 플레이어 공격: 10 데미지 (고블린 HP 90/100)",
                "2. 고블린 반격: 5 데미지 (방어력 2 적용)"
            ],
            "analysis": {{
                "ttk": "15초",
                "dps": "플레이어 12.5",
                "verdict": "적절함 / 너무 어려움 / 너무 쉬움",
                "suggestion": "몬스터 체력을 10% 하향하는 것을 추천합니다."
            }}
        }}
        """

        full_prompt = [system_prompt, f"[시나리오]\n{scenario}"]

        genai.configure(api_key=api_key)
        model = genai.GenerativeModel(model_name)

        with st.spinner("데이터를 분석하고 전투를 시뮬레이션 중입니다..."):
            try:
                log_usage("밸런스 계산 봇")
                response = model.generate_content(full_prompt)
                result_text = response.text.replace("```json", "").replace("```", "").strip()
                result = json.loads(result_text)

                st.divider()
                st.subheader("📊 시뮬레이션 결과")

                # 상단 요약 메트릭
                m1, m2, m3 = st.columns(3)
                m1.metric("승리자", result['winner'])
                m2.metric("전투 시간 (TTK)", result['analysis']['ttk'])
                m3.metric("남은 체력", result['player_hp_left'])

                # 밸런스 판정
                verdict = result['analysis']['verdict']
                color = "green" if "적절" in verdict else "red"
                st.markdown(f"**⚖️ 밸런스 판정:** :{color}[{verdict}]")
                st.info(f"**💡 제안:** {result['analysis']['suggestion']}")

                # 상세 분석 (로그 & 수치)
                tab1, tab2 = st.tabs(["📝 전투 로그 (Logic)", "🧮 상세 분석"])
                
                with tab1:
                    for log in result['log']:
                        st.text(log)
                
                with tab2:
                    st.write(f"**DPS Analysis:** {result['analysis']['dps']}")
                    st.markdown("**사용된 데이터 근거:**")
                    st.json(result) # 전체 데이터 디버깅용

            except Exception as e:
                st.error(f"시뮬레이션 오류: {e}")
                st.error("데이터 형식이 복잡하거나 시나리오가 불분명할 수 있습니다. AI의 답변 원문:")
                st.write(response.text if 'response' in locals() else "응답 없음")

if __name__ == "__main__":
    main()