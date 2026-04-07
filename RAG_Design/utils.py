import requests
import streamlit as st
import json
import os
import csv
from datetime import datetime
import random
import time

# ==========================================
# 1. 공통 상수 (모델 목록 관리)
# ==========================================
CONFIG_FILE = "config.json"
LOG_FILE = "usage_log.csv"

# [핵심] 여기에 모델을 추가하면 모든 봇에 자동 적용됩니다.
AVAILABLE_MODELS = [
    "gemini-2.5-flash",        # 최신 표준
    "gemini-2.5-flash-lite",   # 가성비/속도
    "gemini-3-flash-preview",
    "gemini-3.1-flash-lite-preview",
    "gemini-3.1-flash-image-preview", # 이미지 입력 지원 (실험적)
    "gemini-3.1-pro-preview",          # 고성능
    #"gemini-2.0-flash-exp"     # 실험 버전
]

# ==========================================
# 2. 설정 관리 함수
# ==========================================
def load_config():
    if os.path.exists(CONFIG_FILE):
        try:
            with open(CONFIG_FILE, "r", encoding="utf-8") as f:
                config = json.load(f)
                
                # [하위 호환성] 예전 방식의 api_key만 저장되어 있던 경우 변환
                if "api_key" in config and "api_presets" not in config:
                    config["api_presets"] = {"기본 API": config["api_key"]}
                    config["active_preset"] = "기본 API"
                    
                return config
        except: return {}
    return {}

def save_config(api_presets, active_preset, cx_id, model_name):
    config = {
        "api_presets": api_presets,
        "active_preset": active_preset,
        "cx_id": cx_id,
        "model_name": model_name
    }
    with open(CONFIG_FILE, "w", encoding="utf-8") as f:
        json.dump(config, f, ensure_ascii=False, indent=2)

def log_usage(bot_name):
    """사용 로그 기록"""
    try:
        file_exists = os.path.isfile(LOG_FILE)
        with open(LOG_FILE, "a", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            if not file_exists:
                writer.writerow(["Timestamp", "Bot Name"])
            writer.writerow([datetime.now().strftime("%Y-%m-%d %H:%M:%S"), bot_name])
    except Exception:
        pass

def search_google(query, api_key, cx_id, num_results=5):
    url = "https://www.googleapis.com/customsearch/v1"
    params = {
        "key": api_key,
        "cx": cx_id,
        "q": query,
        "num": num_results
    }

    try:
        response = requests.get(url, params=params, timeout=20)
        response.raise_for_status()
        data = response.json()

        search_results = []
        if "items" in data:
            for item in data["items"]:
                title = item.get("title", "No Title")
                snippet = item.get("snippet", "No Snippet")
                link = item.get("link", "#")
                search_results.append(
                    f"Title: {title}\nSnippet: {snippet}\nLink: {link}\n"
                )

        return "\n---\n".join(search_results)

    except Exception as e:
        return f"구글 검색 오류: {e}"

def retry_with_backoff(max_retries=3, initial_delay=2, backoff_factor=2):
    def decorator(func):
        def wrapper(*args, **kwargs):
            retries = 0
            delay = initial_delay

            while retries < max_retries:
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    error_str = str(e).lower()

                    if (
                        "429" in error_str
                        or "503" in error_str
                        or "high demand" in error_str
                        or "resourceexhausted" in error_str
                        or "quota" in error_str
                        or "rate limit" in error_str
                    ):
                        retries += 1
                        if retries >= max_retries:
                            raise e

                        sleep_time = delay + random.uniform(0, 1)
                        print(f"⚠️ Quota Exceeded. Retrying in {sleep_time:.1f}s... ({retries}/{max_retries})")
                        time.sleep(sleep_time)
                        delay *= backoff_factor
                    else:
                        raise e
            return None
        return wrapper
    return decorator


@retry_with_backoff(max_retries=3)
def safe_generate_content(client, model_name, contents, config=None):
    return client.models.generate_content(
        model=model_name,
        contents=contents,
        config=config
    )


# ==========================================
# 3. 공통 사이드바 UI (모든 봇에서 호출)
# ==========================================
def render_sidebar_settings():
    config = load_config()
    
    # 설정값 로드
    api_presets = config.get("api_presets", {"1번 (기본 API)": ""})
    active_preset = config.get("active_preset", list(api_presets.keys())[0] if api_presets else "1번 (기본 API)")
    saved_cx = config.get("cx_id", "")
    saved_model = config.get("model_name", AVAILABLE_MODELS[0])

    with st.sidebar:
        st.header("⚙️ 통합 설정 (Settings)")

        # 1. 모델 선택
        idx = 0
        if saved_model in AVAILABLE_MODELS:
            idx = AVAILABLE_MODELS.index(saved_model)
        selected_model = st.selectbox("🤖 AI 모델 선택", AVAILABLE_MODELS, index=idx)

        st.divider()
        
        # 2. API Key 프리셋 관리
        st.subheader("🔑 API Key 프리셋")
        
        preset_options = list(api_presets.keys())
        preset_options.append("➕ 새 프리셋 추가")
        
        # 현재 활성화된 프리셋 인덱스 찾기
        try:
            default_idx = preset_options.index(active_preset)
        except ValueError:
            default_idx = 0
            
        selected_preset = st.selectbox("활성 API 선택", preset_options, index=default_idx)
        
        # 새 프리셋 추가 모드인지 기존 수정 모드인지 판단
        if selected_preset == "➕ 새 프리셋 추가":
            preset_name_input = st.text_input("새 프리셋 이름", "2번 (유료 API)")
            actual_preset_name = preset_name_input
            current_key_val = ""
        else:
            actual_preset_name = selected_preset
            current_key_val = api_presets.get(selected_preset, "")
            
        # API 키 입력란
        api_input = st.text_input(f"'{actual_preset_name}' Key 입력", value=current_key_val, type="password")

        # 삭제 버튼 (기본 API가 아니고, 새로 추가하는 모드가 아닐 때만 표시)
        if selected_preset != "➕ 새 프리셋 추가" and len(api_presets) > 1:
            if st.button(f"🗑️ '{selected_preset}' 삭제"):
                del api_presets[selected_preset]
                # 삭제 후 첫 번째 프리셋으로 자동 변경
                save_config(api_presets, list(api_presets.keys())[0], saved_cx, selected_model)
                st.rerun()

        st.divider()
        cx_input = st.text_input("Search Engine ID (CX)", value=saved_cx, type="password", help="검색 봇용")

        # 3. 설정 저장
        if st.button("💾 설정 저장 (Save All)", type="primary"):
            if actual_preset_name: # 이름이 비어있지 않은 경우
                api_presets[actual_preset_name] = api_input
                active_preset = actual_preset_name
            
            save_config(api_presets, active_preset, cx_input, selected_model)
            st.success(f"'{active_preset}' 설정이 저장되었습니다!")
            st.rerun()

        st.divider()
        
        # 각 봇으로 전달할 최종 API Key 반환
        return api_input, cx_input, selected_model