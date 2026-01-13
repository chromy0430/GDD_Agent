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
        
        search_query = f"{genre} game market trend 2024 2025 top selling games"
        if competitors:
            search_query += f" {competitors} analysis"
        
        status_box.write(f"🔍 구글 검색 중: '{search_query}'...")
        
        search_context = search_google(search_query, api_key, cx_id)
        
        if "오류" in search_context:
            status_box.error(search_context)
            status_box.update(label="검색 실패", state="error")
            return
        else:
            status_box.write("✅ 검색 완료! 데이터를 분석합니다.")

        # 2. Gemini 호출
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel(model_name) # [핵심] model_name

        prompt = f"""
        당신은 실시간 시장 데이터를 분석하는 게임 사업 PM입니다.
        아래 [구글 검색 결과]를 바탕으로 시장 트렌드와 경쟁작 현황을 분석하세요.

        [구글 검색 결과]
        {search_context}

        [입력 정보]
        - 장르: {genre}
        - 타겟: {target}
        - 사용자 입력 경쟁작: {competitors}
        - 컨셉: {concept}

        [지시사항]
        1. 검색 결과에 언급된 최신 게임이나 트렌드를 반영하여 분석하세요.
        2. 경쟁작들의 성공/실패 요인을 분석하여 '핵심 차별점(USP)'을 제안하세요.
        3. SWOT 분석을 수행하세요.
        
        [출력 포맷 (JSON)]
        반드시 아래 JSON 포맷으로 출력하세요.
        {{
            "search_trend": "검색 결과 기반 시장 동향 요약",
            "top_competitors": ["경쟁작1", "경쟁작2"],
            "usp": "차별화된 세일즈 포인트",
            "swot": {{
                "strengths": [], "weaknesses": [], "opportunities": [], "threats": []
            }},
            "verdict": "시장성 평가 (S/A/B/C) 및 총평"
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