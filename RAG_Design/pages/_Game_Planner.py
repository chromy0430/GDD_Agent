import streamlit as st
import google.generativeai as genai
from utils import log_usage, render_sidebar_settings

st.set_page_config(layout="wide", page_title="게임 전체 기획 플래너")

def build_prompt(mode, idea):

    if mode == "AAA Studio":

        system = """
You are a Lead Game Designer in a AAA game studio.

Create a FULL Game Design Document.

Focus on:
- large scale gameplay systems
- team based development
- long term content pipeline
- monetization
- live service possibilities

Output language: Korean
"""

    elif mode == "Indie Studio":

        system = """
You are a game designer in a small indie studio.

Design a game with:

- strong core mechanic
- unique gameplay hook
- achievable scope
- small team development

Output language: Korean
"""

    elif mode == "Solo Dev":

        system = """
You are a solo indie developer.

Design a game that can realistically be built by ONE developer.

Focus on:

- minimal scope
- simple systems
- asset reuse
- short development cycle

Output language: Korean
"""

    else:

        system = """
You are designing a game prototype.

Focus on testing a core mechanic.

Limit scope heavily.

Output language: Korean
"""

    return f"""
{system}

Game Idea:
{idea}

Create the following sections:

1. Game Overview
2. Target Audience
3. Core Gameplay Loop
4. Core Mechanics
5. Progression System
6. Content Structure
7. Monetization Strategy
8. Technical Scope
9. Development Scope
"""

def main():

    st.title("🎮 Game Planner Agent")

    api_key, cx_id, model_name = render_sidebar_settings()

    st.markdown(
        "아이디어를 입력하면 **전체 게임 기획서**를 생성합니다."
    )

    mode = st.selectbox(
        "Development Mode",
        ["AAA Studio", "Indie Studio", "Solo Dev", "Prototype"]
    )

    idea = st.text_area(
        "Game Idea",
        placeholder="예: 뱀파이어 서바이버 + 덱빌딩 로그라이크"
    )

    if st.button("Generate Game Plan", type="primary"):

        if not api_key:
            st.warning("API Key를 설정하세요.")
            return

        genai.configure(api_key=api_key)
        model = genai.GenerativeModel(model_name)

        prompt = build_prompt(mode, idea)

        with st.spinner("Generating..."):

            response = model.generate_content(prompt)

        result = response.text

        st.markdown(result)

if __name__ == "__main__":
    main()