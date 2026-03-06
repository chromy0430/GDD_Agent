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
    "gemini-3.1-flash-lite-preview"
    #"gemini-1.5-pro",          # 고성능
    #"gemini-2.0-flash-exp"     # 실험 버전
]

# ==========================================
# 2. 설정 관리 함수
# ==========================================
def load_config():
    if os.path.exists(CONFIG_FILE):
        try:
            with open(CONFIG_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except: return {}
    return {}

def save_config(api_key, cx_id, model_name):
    config = {"api_key": api_key, "cx_id": cx_id, "model_name": model_name}
    with open(CONFIG_FILE, "w", encoding="utf-8") as f:
        json.dump(config, f)

def log_usage(bot_name):
    """사용 로그 기록"""
    try:
        file_exists = os.path.isfile(LOG_FILE)
        with open(LOG_FILE, "a", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            if not file_exists: writer.writerow(["Timestamp", "Bot Name"])
            writer.writerow([datetime.now().strftime("%Y-%m-%d %H:%M:%S"), bot_name])
    except: pass

def search_google(query, api_key, cx_id, num_results=5):
    """Google Custom Search JSON API를 사용하여 웹 검색 결과를 반환합니다."""
    url = "https://www.googleapis.com/customsearch/v1"
    params = {
        'key': api_key,
        'cx': cx_id,
        'q': query,
        'num': num_results
    }
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()
        
        search_results = []
        if 'items' in data:
            for item in data['items']:
                title = item.get('title', 'No Title')
                snippet = item.get('snippet', 'No Snippet')
                link = item.get('link', '#')
                search_results.append(f"Title: {title}\nSnippet: {snippet}\nLink: {link}\n")
        
        return "\n---\n".join(search_results)
    except Exception as e:
        return f"구글 검색 오류: {e}"
    pass

def retry_with_backoff(max_retries=3, initial_delay=2, backoff_factor=2):
    def decorator(func):
        def wrapper(*args, **kwargs):
            retries = 0
            delay = initial_delay
            while retries < max_retries:
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    # 429(ResourceExhausted) 에러 체크
                    error_str = str(e)
                    if "429" in error_str or "ResourceExhausted" in error_str or "quota" in error_str.lower():
                        retries += 1
                        if retries >= max_retries:
                            raise e # 최대 재시도 초과 시 에러 발생
                        
                        # 지수 백오프 + Jitter(분산) 적용
                        sleep_time = delay + random.uniform(0, 1)
                        print(f"⚠️ Quota Exceeded. Retrying in {sleep_time:.1f}s... ({retries}/{max_retries})")
                        time.sleep(sleep_time)
                        delay *= backoff_factor
                    else:
                        raise e # 다른 에러는 즉시 발생
            return None
        return wrapper
    return decorator

# 2. 래퍼 함수 (다른 파일에서 가져다 쓰기 편하게 만듦)
@retry_with_backoff(max_retries=3)
def safe_generate_content(client, model_name, contents, config=None):
    """
    model.generate_content 대신 사용할 안전한 함수
    """
    return client.models.generate_content(
        model=model_name,
        contents=contents,
        config=config
    )


# ==========================================
# 3. 공통 사이드바 UI (모든 봇에서 호출)
# ==========================================
def render_sidebar_settings():
    """사이드바 설정을 그리고 (API Key, Model, CX ID) 반환"""
    config = load_config()
    saved_api = config.get("api_key", "")
    saved_cx = config.get("cx_id", "")
    saved_model = config.get("model_name", AVAILABLE_MODELS[0])

    with st.sidebar:
        st.header("⚙️ 통합 설정 (Settings)")
        
        # 모델 선택
        idx = 0
        if saved_model in AVAILABLE_MODELS: idx = AVAILABLE_MODELS.index(saved_model)
        selected_model = st.selectbox("🤖 AI 모델 선택", AVAILABLE_MODELS, index=idx)
        
        # 키 입력
        api_input = st.text_input("Google API Key", value=saved_api, type="password")
        cx_input = st.text_input("Search Engine ID (CX)", value=saved_cx, type="password", help="검색 봇용")

        if st.button("💾 설정 저장 (Save All)"):
            save_config(api_input, cx_input, selected_model)
            st.success("설정이 저장되었습니다!")
            st.rerun()
            
        st.divider()
        return api_input, cx_input, selected_model