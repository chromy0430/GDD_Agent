import os
import time
import streamlit as st
from google import genai
from utils import log_usage, render_sidebar_settings
from rag_utils import UnityRAG

st.set_page_config(layout="wide", page_title="Music Composer (Lyria 3)")

def main():
    st.title("🎵 Music Composer (Lyria 3)")
    st.markdown("""
    RAG DB에서 상황 묘사나 기존 오디오 분석 데이터를 검색한 후, 
    Gemini-3.1-Flash-Lite가 프롬프트를 정제하고 Lyria 3 Pro 모델이 실제 오디오를 렌더링합니다.
    """)

    api_key, _, _ = render_sidebar_settings()

    query = st.text_area(
        "검색할 오디오 파일명이나 작곡할 상황을 묘사해주십시오.", 
        height=100, 
        placeholder="예: 로랜시아 bgm 파일의 테마와 비슷한 음악"
    )

    if st.button("음악 생성 (약 1~2분 소요)", type="primary"):
        if not api_key:
            st.error("API Key가 필요합니다.")
            return
        if not query:
            st.warning("검색어나 상황 묘사를 입력하십시오.")
            return

        client = genai.Client(api_key=api_key)

        with st.status("🎵 음악 생성 파이프라인 가동 중...", expanded=True) as status:
            
            # 1. RAG DB 검색 단계
            st.write("1. 🔍 RAG DB: 관련 오디오/기획 문서 검색 중...")
            try:
                rag = UnityRAG(api_key_input=api_key)
                retrieved_context = rag.retrieve_context(query, k=3)
                
                if retrieved_context.strip():
                    with st.expander("🔎 AI가 작곡에 참조한 RAG 원문 데이터 (Cross-Check)", expanded=True):
                        st.text(retrieved_context)
                else:
                    st.warning("⚠️ 지식 베이스에서 관련 내용을 찾지 못했습니다. 입력한 텍스트만으로 생성을 시도합니다.")
                    retrieved_context = "관련 데이터 없음."
            except Exception as e:
                st.error(f"DB 검색 오류: {e}")
                retrieved_context = "검색 실패"

            # 2. Flash 모델 프롬프트 생성 단계 (지시하신 gemini-3.1-flash-lite-preview 적용)
            st.write("2. 🧠 Gemini 3.1 모델: 분석 및 프롬프트 엔지니어링 진행 중...")
            prompt_maker = f"""
            당신은 수석 음악 감독입니다. 아래 [RAG Context]에 제공된 기존 오디오 분석 데이터나 기획서를 바탕으로,
            Lyria 3 음악 생성 모델이 이해할 수 있는 완벽한 영문 프롬프트로 변환하십시오.
            
            - 장르, 핵심 악기(Lead Instrument), 리듬(BPM), 분위기(Mood), 믹싱 스타일(예: lo-fi, orchestral, chiptune)을 구체적인 음악 용어로 반드시 포함할 것.
            - 보컬이 필요 없다면 "Instrumental only, no vocals"를 명시할 것.

            [User Query]: {query}
            
            [RAG Context (참고 데이터)]:
            {retrieved_context}

            반드시 영문 프롬프트 내용만 텍스트로 출력하십시오.
            """
            
            try:
                # [CRITICAL FIX] 지정된 모델로 강제 고정
                lyria_prompt_res = client.models.generate_content(
                    model="gemini-3.1-flash-lite-preview", 
                    contents=prompt_maker
                )
                lyria_prompt = lyria_prompt_res.text.strip()
                st.info(f"✨ 최적화된 영문 프롬프트:\n{lyria_prompt}")
            except Exception as e:
                status.update(label="❌ 프롬프트 생성 실패", state="error")
                st.error(f"프롬프트 정제 중 오류: {e}")
                return

            # 3. Lyria 3 Pro 오디오 렌더링 단계 (OTHER 에러 방어 및 재시도 로직 포함)
            st.write("3. 🎹 Lyria 3 Pro: 오디오 렌더링 중 (최대 2분 소요)...")
            
            max_retries = 2
            audio_saved = False
            audio_path = f"./output_audio/theme_{int(time.time())}.mp3"
            os.makedirs("./output_audio", exist_ok=True)

            for attempt in range(1, max_retries + 1):
                try:
                    lyria_res = client.models.generate_content(
                        model="lyria-3-pro-preview",
                        contents=lyria_prompt
                    )
                    
                    parts = lyria_res.parts if hasattr(lyria_res, 'parts') else None
                    
                    if parts is not None:
                        for part in parts:
                            if hasattr(part, 'inline_data') and part.inline_data:
                                with open(audio_path, "wb") as f:
                                    f.write(part.inline_data.data)
                                audio_saved = True
                    
                    if audio_saved:
                        break # 성공 시 반복문 탈출
                    else:
                        # parts는 있으나 inline_data가 없는 경우, 또는 OTHER 에러인 경우
                        finish_reason = ""
                        try:
                            finish_reason = lyria_res.candidates[0].finish_reason if hasattr(lyria_res, 'candidates') else "UNKNOWN"
                        except: pass
                        
                        if finish_reason == "OTHER" and attempt < max_retries:
                            st.warning(f"⚠️ 구글 서버 내부 오류(OTHER) 발생. ({attempt}/{max_retries}) 재시도 중...")
                            time.sleep(3) # 서버 안정을 위해 3초 대기 후 재시도
                            continue
                        
                        status.update(label="⚠️ 오디오 데이터 반환 실패", state="error")
                        st.error(f"API 서버가 오디오 데이터를 반환하지 않았습니다. (사유: {finish_reason})")
                        raw_data = lyria_res.model_dump() if hasattr(lyria_res, 'model_dump') else str(lyria_res)
                        with st.expander("🔎 API 원문 응답 보기 (디버깅용)"):
                            st.json(raw_data)
                        return

                except Exception as e:
                    if attempt < max_retries:
                        st.warning(f"⚠️ 네트워크/서버 오류 발생. ({attempt}/{max_retries}) 재시도 중...")
                        time.sleep(3)
                    else:
                        status.update(label="❌ 오디오 렌더링 실패", state="error")
                        st.error(f"Lyria 3 호출 중 서버 오류 발생: {e}")
                        return

            if audio_saved:
                status.update(label="✅ 음악 작곡 완료!", state="complete", expanded=False)
                st.success(f"오디오 렌더링 완료: `{audio_path}`")
                st.audio(audio_path, format="audio/mp3")
                log_usage("Music Composer")

if __name__ == "__main__":
    main()