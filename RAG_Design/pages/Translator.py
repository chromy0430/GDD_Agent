import streamlit as st
import os
import asyncio
import wave
import io
from google import genai
from google.genai import types

# 불필요한 sys.path 조작 제거 후 직접 임포트
try:
    from utils import render_sidebar_settings
except ImportError:
    st.error("utils.py를 찾을 수 없습니다. 동일한 폴더에 파일이 있는지 확인하세요.")
    st.stop()

# ==========================================
# 1. 전역 설정 및 API Key 획득
# ==========================================
st.set_page_config(layout="wide", page_title="실시간 음성 번역기")

api_key_input, cx_id, model_name = render_sidebar_settings()

# ==========================================
# 2. 데이터 정의 (97개 언어 및 음성)
# ==========================================
SUPPORTED_LANGUAGES = [
    "아프리칸스어 (af)", "아칸어 (ak)", "알바니아어 (sq)", "암하라어 (am)", "아랍어 (ar)", 
    "아르메니아어 (hy)", "아삼어 (as)", "아제르바이잔어 (az)", "바스크어 (eu)", "벨라루스어 (be)", 
    "뱅골어 (bn)", "보스니아어 (bs)", "불가리아어 (bg)", "버마어 (my)", "카탈로니아어 (ca)", 
    "세부아노어 (ceb)", "중국어 (zh)", "크로아티아어 (hr)", "체코어 (cs)", "덴마크어 (da)", 
    "네덜란드어 (nl)", "영어 (en)", "에스토니아어 (et)", "페로어 (fo)", "필리핀어 (fil)", 
    "핀란드어 (fi)", "프랑스어 (fr)", "갈리시아어 (gl)", "조지아어 (ka)", "독일어 (de)", 
    "그리스어 (el)", "구자라트어 (gu)", "하우사어 (ha)", "히브리어 (iw)", "힌디어 (hi)", 
    "헝가리어 (hu)", "아이슬란드어 (is)", "인도네시아어 (id)", "아일랜드어 (ga)", "이탈리아어 (it)", 
    "일본어 (ja)", "칸나다어 (kn)", "카자흐어 (kk)", "크메르어 (km)", "키냐르완다어 (rw)", 
    "한국어 (ko)", "쿠르드어 (ku)", "키르기스어 (ky)", "라오어 (lo)", "라트비아어 (lv)", 
    "리투아니아어 (lt)", "마케도니아어 (mk)", "말레이어 (ms)", "말라얄람어 (ml)", "몰타어 (mt)", 
    "마오리어 (mi)", "마라타어 (mr)", "몽골어 (mn)", "네팔어 (ne)", "노르웨이어 (no)", 
    "오리야어 (or)", "오로모어 (om)", "파슈토어 (ps)", "페르시아어 (fa)", "폴란드어 (pl)", 
    "포르투갈어 (pt)", "펀자브어 (pa)", "케추아어 (qu)", "루마니아어 (ro)", "로만시어 (rm)", 
    "러시아어 (ru)", "세르비아어 (sr)", "신드어 (sd)", "싱할라어 (si)", "슬로바키아어 (sk)", 
    "슬로베니아어 (sl)", "소말리어 (so)", "소토어(남부) (st)", "스페인어 (es)", "스와힐리어 (sw)", 
    "스웨덴어 (sv)", "타지크어 (tg)", "타밀어 (ta)", "텔루구어 (te)", "태국어 (th)", 
    "츠와나어 (tn)", "튀르키예어 (tr)", "투르크멘어 (tk)", "우크라이나어 (uk)", "우르두어 (ur)", 
    "우즈베크어 (uz)", "베트남어 (vi)", "웨일즈어 (cy)", "서프리지아어 (fy)", "월로프어 (wo)", 
    "요루바어 (yo)", "줄루어 (zu)"
]

SUPPORTED_VOICES = ["Kore", "Aoide", "Puck", "Charon", "Fenrir"]

# ==========================================
# 3. 비동기 Live API 호출 함수
# ==========================================
async def get_live_translation(api_key, audio_bytes, system_instruction, text_prompt, voice_name):
    client = genai.Client(api_key=api_key, http_options={'api_version': 'v1alpha'})
    
    config = types.LiveConnectConfig(
        system_instruction=types.Content(parts=[types.Part.from_text(text=system_instruction)]),
        response_modalities=["AUDIO"],
        speech_config=types.SpeechConfig(
            voice_config=types.VoiceConfig(
                prebuilt_voice_config=types.PrebuiltVoiceConfig(
                    voice_name=voice_name
                )
            )
        )
    )
    
    output_audio = bytearray()
    
    async with client.aio.live.connect(model="gemini-3.1-flash-live-preview", config=config) as session:
        await session.send_realtime_input(text=text_prompt)
        
        with wave.open(io.BytesIO(audio_bytes), 'rb') as wf:
            framerate = wf.getframerate()
            pcm_data = wf.readframes(wf.getnframes())
            
        await session.send_realtime_input(
            audio=types.Blob(data=pcm_data, mime_type=f"audio/pcm;rate={framerate}")
        )
        
        await session.send_realtime_input(audio_stream_end=True)
        
        async for response in session.receive():
            if response.server_content is not None:
                if response.server_content.model_turn is not None:
                    for part in response.server_content.model_turn.parts:
                        if part.inline_data and part.inline_data.data:
                            output_audio.extend(part.inline_data.data)
                
                if response.server_content.turn_complete:
                    break
                    
    if not output_audio:
        return None

    wav_io = io.BytesIO()
    with wave.open(wav_io, 'wb') as wav_file:
        wav_file.setnchannels(1)      
        wav_file.setsampwidth(2)      
        wav_file.setframerate(24000)  
        wav_file.writeframes(output_audio)

    return wav_io.getvalue()

# ==========================================
# 4. 메인 UI 로직
# ==========================================
def main():
    st.title("🌐 Translator: 실시간 음성 번역기")

    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    PROMPT_PATH = os.path.join(BASE_DIR, "Translator_Prompt.txt")
    
    try:
        with open(PROMPT_PATH, "r", encoding="utf-8") as f:
            system_instruction = f.read()
    except FileNotFoundError:
        st.error("프롬프트 파일이 없습니다. (Translator_Prompt.txt)")
        return

    col1, col2 = st.columns(2)
    with col1:
        target_lang = st.selectbox("🌐 타겟 언어 선택", SUPPORTED_LANGUAGES, index=7)
    with col2:
        selected_voice = st.selectbox("🗣️ 출력 음성 선택", SUPPORTED_VOICES, index=0)

    audio_input = st.audio_input(f"대화를 시작하세요 (한국어 -> {target_lang.split('(')[0].strip()})")

    if audio_input:
        if not api_key_input:
            st.warning("사이드바에서 API Key를 입력해주세요.")
            return

        with st.spinner(f"번역 중... ({target_lang})"):
            audio_bytes = audio_input.read()
            
            text_prompt = f"""
            Translate the spoken Korean audio into {target_lang}.

            Requirements:
            - Output ONLY the translated result.
            - Do not explain, do not summarize.
            - Preserve tone, nuance, and speaking style exactly.
            - Maintain politeness level and emotional expression.

            Target_Lang: {target_lang}
            """
            
            try:
                result_audio = asyncio.run(
                    get_live_translation(api_key_input, audio_bytes, system_instruction, text_prompt, selected_voice)
                )
                
                if result_audio:
                    st.success("번역 완료!")
                    st.audio(result_audio, format="audio/wav", autoplay=True)
                else:
                    st.error("모델로부터 오디오 응답을 받지 못했습니다.")
            except Exception as e:
                st.error(f"Live API 통신 오류 발생: {e}")

if __name__ == "__main__":
    main()