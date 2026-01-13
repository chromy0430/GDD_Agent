import streamlit as st
import google.generativeai as genai
import requests
import os
import json
from utils import log_usage, render_sidebar_settings, search_google
from rag_utils import UnityRAG

# ==========================================
# 1. 설정 및 상수
# ==========================================
st.set_page_config(layout="wide", page_title="레퍼런스 탐색기")
#MODEL_NAME = "gemini-2.5-flash-lite"
#CONFIG_FILE = "config.json"

# ==========================================
# 3. 메인 로직
# ==========================================
# ==========================================
# 3. 메인 로직 (한국어 출력 및 정확도 개선판)
# ==========================================
def main():
    st.title("🎨 레퍼런스 & 메카닉 탐색 봇 (Ver 2.0)")
    api_key, cx_id, model_name = render_sidebar_settings()
    
    if "optimized_keywords" not in st.session_state:
        st.session_state.optimized_keywords = None

    st.markdown("""
    특정 기능, UI, 아트 스타일을 기획할 때 **참고할 만한 게임**과 **자료 링크**를 찾아줍니다.  
    ✨ **한국어로 결과를 출력하며, 검색 정확도를 높였습니다.**
    """)   

    # 입력 UI
    query = st.text_input("찾고 싶은 레퍼런스", 
                          placeholder="예: 배를 타고 적을 막는 뱀서류 게임, 타격감이 훌륭한 2D 횡스크롤")
    
    col1, col2 = st.columns(2)
    with col1:
        category = st.selectbox("카테고리", ["시스템/메카닉", "UI/UX 디자인", "아트/비주얼", "연출/이펙트", "사운드/BGM"])
    with col2:
        platform = st.selectbox("타겟 플랫폼", ["PC (Steam)", "Mobile", "Console", "All"])

    if st.button("📚 레퍼런스 & 링크 찾기", type="primary"):
        if not api_key or not cx_id:
            st.warning("설정 메뉴에서 API Key를 입력해주세요.")
            return
        if not query:
            st.warning("내용을 입력해주세요.")
            return

        status_box = st.status("🕵️ 레퍼런스 분석을 시작합니다...", expanded=True)
        
        try:
            genai.configure(api_key=api_key)
            model = genai.GenerativeModel(model_name)

            # ---------------------------------------------------------
            # [단계 1] 검색어 최적화 (더 구체적인 게임명을 찾도록 유도)
            # ---------------------------------------------------------
            status_box.write("🧠 검색어 최적화 중...")
            
            # 검색어 생성 프롬프트 개선: 구체적인 게임 타이틀을 찾도록 유도
            keyword_prompt = f"""
            You are a professional game researcher.
            The user is looking for games with specific mechanics.
            Convert the User Request into **3 Google Search Queries** (English).
            
            [User Request]: {query} (Category: {category}, Platform: {platform})
            
            Rules:
            1. Try to guess specific game titles that fit this niche.
            2. Use keywords like 'Best games like', 'Reddit', 'Steam' to find discussions.
            3. If the request involves a specific object (e.g., 'Boat', 'Gun'), emphasize it.
            
            Example output: "Sea of Survivors gameplay mechanics, Best naval roguelite survivor games steam, Ship-based bullet heaven games reddit"
            Output format: Just the 3 queries separated by commas.
            """
            
            kw_response = model.generate_content(keyword_prompt)
            search_keywords = kw_response.text.strip()
            
            # 첫 번째 쿼리 사용 + "Steam" 키워드 강제 결합 (PC 게임일 경우)
            primary_query = search_keywords.split(',')[0].strip()
            final_search_query = f"{primary_query} site:steampowered.com OR site:reddit.com"
            
            status_box.write(f"🔍 최적화된 검색어: '{primary_query}'")

            # ---------------------------------------------------------
            # [단계 2] 구글 검색 수행
            # ---------------------------------------------------------
            search_context = search_google(final_search_query, api_key, cx_id, num_results=8)
            
            if "오류" in search_context:
                status_box.error(search_context)
                status_box.update(label="검색 실패", state="error")
                return
            
            status_box.write("✅ 검색 완료! 한국어로 분석 리포트를 작성합니다...")

            # ---------------------------------------------------------
            # [단계 3] 결과 분석 및 JSON 생성 (한국어 강제)
            # ---------------------------------------------------------
            generation_config = {
                "response_mime_type": "application/json"
            }

            rag = UnityRAG(api_key)
            status_box.write("📂 내 로컬 노트(Reference) 검색 중...")
            local_refs = rag.retrieve_context(f"Game Reference Ideas: {query}", k=2)

            # 프롬프트 대폭 수정: 한국어 출력 강제 및 매칭 로직 강화
            analysis_prompt = f"""
            You are a Game Design Consultant. Analyze the [Google Search Results] AND [User's Local Notes] to recommend games.

            [User's Local Notes (Priority)]
            사용자가 과거에 메모해둔 관련 아이디어입니다. 구글 결과와 연관 지어 언급하세요.
            {local_refs}

            [User Request]: {query}
            [Google Search Results]
            {search_context}

            

            **CRITICAL INSTRUCTIONS**:
            1. **LANGUAGE**: All values in the JSON output (reason, feature_detail, dev_tip) MUST BE IN **KOREAN**.
            2. **ACCURACY**: Only recommend games that **ACTUALLY MATCH** the specific mechanic requested (e.g., if user asks for 'Boat', the game MUST have a boat). Do not recommend generic 'Vampire Survivors' clones if they don't have the requested feature.
            3. **REALITY CHECK**: Do not invent games. Only use games found in the search results. If a game is unreleased or Early Access, mention it in the 'release_year' (e.g., "2024 (Early Access)").

            Output JSON Schema:
            {{
                "recommendations": [
                    {{
                        "game_title": "Game Name (English)",
                        "release_year": "Release Year (e.g., 2023)",
                        "reason": "이 게임을 추천하는 이유 (한글로 작성)",
                        "feature_detail": "사용자가 요청한 기능이 어떻게 구현되어 있는지 구체적 분석 (한글로 작성)",
                        "useful_links": ["Link URL 1"]
                    }}
                ],
                "dev_tip": "1인 개발자를 위한 구현 팁 또는 에셋 추천 (한글로 작성)",
                "keywords": ["추가 검색어1", "추가 검색어2"]
            }}
            """

            final_response = model.generate_content(
                analysis_prompt, 
                generation_config=generation_config
            )
            
            res = json.loads(final_response.text)
            status_box.update(label="✅ 분석 완료!", state="complete", expanded=False)

            # ---------------------------------------------------------
            # [단계 4] 결과 렌더링
            # ---------------------------------------------------------
            st.divider()
            st.subheader(f"📚 '{query}' 분석 결과")
            
            if not res['recommendations']:
                st.warning("조건에 딱 맞는 게임을 찾기 어렵습니다. 검색어를 조금 더 넓게 잡아보세요.")
            
            for item in res['recommendations']:
                # 제목은 영어로 유지하되, 내용은 한글
                with st.expander(f"🎮 {item['game_title']} ({item.get('release_year', '미정')})", expanded=True):
                    st.info(f"**선정 이유:** {item['reason']}")
                    st.write(f"**🔍 메카닉 분석:** {item['feature_detail']}")
                    if item.get('useful_links'):
                        st.markdown("**🔗 관련 자료:**")
                        for link in item['useful_links']:
                            st.markdown(f"- {link}")

            st.divider()
            c1, c2 = st.columns([2, 1])
            with c1:
                st.markdown("### 💡 개발 팁")
                st.success(res.get('dev_tip', "팁이 없습니다."))
            with c2:
                st.markdown("### 🔍 사용된 검색어")
                st.code(primary_query, language="text")

            with st.expander("🔎 원본 데이터 확인"):
                st.text(search_context)

        except json.JSONDecodeError:
            st.error("AI 응답을 분석하는 도중 오류가 발생했습니다.")
            st.text_area("응답 원문", final_response.text if 'final_response' in locals() else "응답 없음")
            
        except Exception as e:
            st.error(f"오류 발생: {str(e)}")

if __name__ == "__main__":
    main()