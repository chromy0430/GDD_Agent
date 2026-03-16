import streamlit as st
from google import genai
from utils import log_usage, render_sidebar_settings, safe_generate_content

# ==========================================
# 페이지 설정
# ==========================================

st.set_page_config(layout="wide", page_title="Game Design Document Generator")

api_key_input, cx_id, model_name = render_sidebar_settings()

# ==========================================
# AAA MODE PROMPT
# ==========================================

PROMPT_AAA = """
# Role
You are a Lead Game Designer working in a AAA game studio.

Create a professional High-Level Game Design Document.

# Design Philosophy

AAA games must include:

- scalable systems
- long progression
- large content volume
- replayability
- possible live service expansion

# Required Structure

## 1. Game Overview
Title, Genre, Platform, Target Market

## 2. Core Vision
High level design philosophy

## 3. Target Audience

## 4. Core Gameplay Loop

## 5. Core Systems
Combat, progression, exploration, crafting, etc.

## 6. Progression Design
Levels, gear tiers, skill trees

## 7. Content Structure
Regions, bosses, quests, activities

## 8. Economy System
Currencies, rewards, sinks

## 9. Multiplayer / Social Systems

## 10. Endgame Design

Write in a professional AAA design document style.
"""

# ==========================================
# INDIE MODE PROMPT
# ==========================================

PROMPT_INDIE = """
# Role
You are the Creative Director of an Indie Game Studio.

Focus on creativity and a strong core mechanic.

# Design Philosophy

Indie games prioritize:

- originality
- a strong central gameplay idea
- small but polished scope
- unique atmosphere

# Required Structure

## 1. Game Concept

## 2. Unique Hook
What makes the game special?

## 3. Core Gameplay Loop

## 4. Player Experience

## 5. Core Mechanics

## 6. Art Style Direction

## 7. Content Scope
Designed for a small team.

## 8. Development Scope
Estimated complexity and scope.

Keep the document concise and idea-focused.
"""

# ==========================================
# MOBILE F2P MODE PROMPT
# ==========================================

PROMPT_MOBILE = """
# Role
You are a Senior Game Designer at a Mobile Free-to-Play studio.

Design a game optimized for retention and monetization.

# Design Philosophy

Mobile F2P games require:

- strong retention loops
- clear progression
- live service design
- monetization systems
- daily engagement

# Required Structure

## 1. Game Overview

## 2. Target Audience

## 3. Core Gameplay Loop

## 4. Retention Systems
Daily quests, login rewards, events

## 5. Progression Systems
Levels, upgrades, collections

## 6. Monetization Design
Gacha, battle pass, cosmetics, energy systems

## 7. Economy System
Soft currency, premium currency

## 8. Live Operations
Seasonal events, content updates

## 9. Long-Term Engagement

Focus on sustainable live service game design.
"""

# ==========================================
# EXPERIMENTAL MODE PROMPT
# ==========================================

PROMPT_EXPERIMENTAL = """
# Role
You are an experimental game designer exploring innovative game experiences.

Focus on artistic and unconventional design.

# Design Philosophy

Experimental games emphasize:

- new interaction models
- unusual mechanics
- emotional or philosophical experiences
- unique storytelling structures

# Required Structure

## 1. Concept

## 2. Experimental Hook

## 3. Player Experience

## 4. Core Interaction Model

## 5. Narrative Approach

## 6. Artistic Direction

## 7. Gameplay Structure

## 8. Intended Emotional Impact

Think creatively and break traditional design rules.
"""

# ==========================================
# UI
# ==========================================

st.title("🎮 Game Design Document Generator")

st.write("게임 아이디어를 입력하면 **게임 기획서(GDD)** 를 생성합니다.")

design_mode = st.radio(
    "Design Mode",
    [
        "AAA Studio",
        "Indie Studio",
        "Mobile F2P Studio",
        "Experimental Game Lab"
    ],
    horizontal=True
)

user_input = st.text_area(
    "Game Idea",
    height=200,
    placeholder="예: 작은 섬에서 낚시를 하며 전설 물고기를 잡는 Cozy 낚시 게임"
)

generate_button = st.button("게임 기획서 생성")

# ==========================================
# PROMPT SELECT
# ==========================================

if design_mode == "AAA Studio":
    system_prompt = PROMPT_AAA

elif design_mode == "Indie Studio":
    system_prompt = PROMPT_INDIE

elif design_mode == "Mobile F2P Studio":
    system_prompt = PROMPT_MOBILE

else:
    system_prompt = PROMPT_EXPERIMENTAL

# ==========================================
# GENERATE
# ==========================================

if generate_button:

    if not api_key_input:
        st.error("API Key를 입력해주세요.")
        st.stop()

    client = genai.Client(api_key=api_key_input)

    full_prompt = f"""
{system_prompt}

# User Game Idea
{user_input}

# Output Language Rule
반드시 한국어로 작성하십시오.

Create the complete Game Design Document.
"""

    with st.spinner("기획서 생성 중..."):

        response = safe_generate_content(
            client,
            model_name,
            contents=full_prompt
        )

        result = response.text

    log_usage("Game_Designer")

    st.markdown("## 게임 기획서 결과")

    st.markdown(result)