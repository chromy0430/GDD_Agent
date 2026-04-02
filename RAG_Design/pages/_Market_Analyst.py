import streamlit as st
import google.generativeai as genai
import requests 
import os
import json
from utils import log_usage, render_sidebar_settings, search_google

# ==========================================
# 1. 설정 및 상수
# ==========================================
st.set_page_config(layout="wide", page_title="시장 분석 전략가")
#MODEL_NAME = "gemini-2.5-flash" # 2.5는 아직 불안정할 수 있어 1.5 Flash 권장 (원하시면 변경 가능)
#CONFIG_FILE = "config.json"

# ==========================================
# 3. 메인 로직
# ==========================================
def main():
    st.title("📈 게임 시장 및 경쟁작 분석 봇 (Smart Cache)")
    api_key, cx_id, model_name = render_sidebar_settings()
    st.markdown("""
    내 게임 아이디어가 **시장에서 먹힐지** 분석합니다.  
    ✨ **Google Custom Search API를 사용하여 최신 정보를 검색하며, RPD를 절약합니다.**
    """)

    # 입력 UI
    col1, col2 = st.columns(2)
    with col1:
        genre = st.text_input("장르 (Genre)", placeholder="예: 뱀파이어 서바이버 라이크")
        target = st.text_input("타겟 유저 (Target)", placeholder="예: 30대 직장인")
    with col2:
        competitors = st.text_input("참고/경쟁 게임", placeholder="비워두면 AI가 검색합니다")
        concept = st.text_area("게임 핵심 컨셉", height=100, placeholder="예: 덱빌딩 로그라이크 + 오토배틀러")

    # [핵심] 세션 스테이트 초기화 (이름 통일됨)
    if "market_analysis_result" not in st.session_state:
        st.session_state["market_analysis_result"] = None

    # 버튼 클릭 시 (API 호출 로직)
    if st.button("🔍 실시간 시장 분석 시작", type="primary"):
        if not api_key or not cx_id: # [수정] 변수명 맞춤
            st.warning("설정에서 API Key와 CX ID를 입력해주세요.")
            return

        # 1. 구글 검색 수행
        status_box = st.status("🕵️ 시장 데이터를 수집하고 있습니다...", expanded=True)
        
        # 수정 후
        search_query_market = f"{genre} game market 2025"
        search_query_competitors = f"{genre} game top games steam mobile"

        status_box.write(f"🔍 구글 검색 중: '{search_query_market}' / '{search_query_competitors}'...")

        search_context = search_google(search_query_market, api_key, cx_id)
        search_context += "\n---\n"
        search_context += search_google(search_query_competitors, api_key, cx_id)

        # 경쟁작 직접 입력했을 때 추가 검색
        if competitors:
            search_context += "\n---\n"
            search_context += search_google(f"{competitors} game review analysis", api_key, cx_id)
        
        if "오류" in search_context:
            status_box.error(search_context)
            status_box.update(label="검색 실패", state="error")
            return
        else:
            status_box.write("✅ 검색 완료! 데이터를 분석합니다.")

        # 2. Gemini 호출
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel(model_name)

        prompt = f"""
            당신은 데이터 기반의 **Game Business Analyst**입니다.
            반드시 제공된 [구글 검색 결과]에 기반하여 사실만을 분석해야 합니다.
            검색 결과에 없는 부분은 게임 산업 일반 지식으로 보완하되 '[추정]' 태그를 붙이십시오.

            [분석 대상 게임]
            - 장르: {genre}
            - 핵심 컨셉: {concept}
            - 타겟 유저: {target}
            - 참고 경쟁작: {competitors if competitors else "AI가 판단"}

            [구글 검색 결과]
            {search_context}

            [분석 프레임워크]
            1. **Fact Check:** 언급하는 모든 경쟁작은 실제 검색 결과에 존재하는 게임이어야 합니다.
            2. **BM & Retention:** 경쟁작들이 어떻게 수익을 내고(Ads, IAP), 유저를 붙잡아두는지(Daily Quest, Season Pass) 분석하세요.
            3. **Gap Analysis:** 시장의 포화된 부분(Red Ocean)과 기회 요소(Blue Ocean)를 명확히 구분하세요.

            [출력 포맷 (JSON)]
            {{
                "search_trend": "검색 결과 기반 시장 동향 요약",
                "top_competitors": ["게임A (Steam)", "게임B (Mobile)"],
                "usp": "경쟁작 대비 확실한 차별점 (Core Mechanic 위주)",
                "swot": {{
                    "strengths": [], "weaknesses": [], "opportunities": [], "threats": []
                }},
                "verdict": "S/A/B/C 등급 및 냉철한 평가"
            }}
        """        
       
        try:
            log_usage("시장 분석 봇") # 로그 기록
            response = model.generate_content(prompt)
            res = json.loads(response.text.replace("```json", "").replace("```", "").strip())

            # [핵심 수정] 결과 저장 구조를 맞춤 (data + search_context)
            st.session_state["market_analysis_result"] = {
                "data": res,
                "search_context": search_context
            }
            status_box.update(label="✅ 분석 완료!", state="complete", expanded=False)
            
        except Exception as e:
            st.error(f"분석 중 오류 발생: {e}")
            status_box.update(label="분석 실패", state="error")


    # [핵심] 결과 출력 로직 (버튼 바깥에 위치해야 함)
    if st.session_state["market_analysis_result"] is not None:
        # 저장된 데이터 불러오기
        res = st.session_state["market_analysis_result"]["data"]
        search_ctx = st.session_state["market_analysis_result"]["search_context"]

        # 화면 그리기
        st.divider()
        st.subheader(f"🏆 판정: {res['verdict']}")
        
        st.markdown(f"### 🌐 최신 시장 동향 (Search Based)")
        st.info(res['search_trend'])
        st.write(f"**🔥 주요 경쟁작:** {', '.join(res['top_competitors'])}")

        st.divider()
        st.markdown(f"**💎 USP:** {res['usp']}")

        c1, c2 = st.columns(2)
        with c1:
            st.markdown("### ⚔️ SWOT 분석")
            st.success(f"**S:** {', '.join(res['swot']['strengths'])}")
            st.warning(f"**W:** {', '.join(res['swot']['weaknesses'])}")
        with c2:
            st.write("")
            st.write("")
            st.info(f"**O:** {', '.join(res['swot']['opportunities'])}")
            st.error(f"**T:** {', '.join(res['swot']['threats'])}")

        # 검색 결과 원본 보여주기
        with st.expander("🔎 검색된 원본 데이터 보기"):
            st.text(search_ctx)

        # 초기화 버튼
        if st.button("🔄 결과 초기화 (다시 하기)"):
            st.session_state["market_analysis_result"] = None
            st.rerun()

if __name__ == "__main__":
    main()