import streamlit as st
import os
from google import genai
from google.genai import types

def run_voice_translator():
    st.title("🛡️ Phantom Linguist: 실시간 음성 번역기")
    
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    PROMPT_PATH = os.path.join(BASE_DIR, "Translator_Prompt.txt")

    # 1. 프롬프트 로드 (파일 읽기)
    try:
        with open(PROMPT_PATH, "r", encoding="utf-8") as f:
            system_instruction = f.read()
    except FileNotFoundError:
        st.error("프롬프트 파일이 없습니다.")
        return

    client = genai.Client(api_key="AIzaSyCf9qWfPQuwUtbnZNEsjNc1_F-lQp-Oacs")

    # 2. 사용자 음성 입력 (Streamlit 오디오 입력 컴포넌트)
    audio_input = st.audio_input("대화를 시작하세요 (한국어 -> 아제르바이잔어)")

    if audio_input:
        # 데이터 흐름 추적: [사용자 음성 바이너리] -> [Gemini 멀티모달 해석] -> [번역된 음성 생성]
        with st.spinner("번역 중..."):
            response = client.models.generate_content(
                model="gemini-3.1-flash-live-preview",
                contents=[
                    types.Part.from_bytes(
                        data=audio_input.read(),
                        mime_type="audio/wav"
                    ),
                    f"""
            Translate the spoken Korean audio into Azerbaijani.

            Requirements:
            - Output ONLY the translated result.
            - Do not explain, do not summarize.
            - Preserve tone, nuance, and speaking style exactly.
            - Maintain politeness level and emotional expression.

            Target_Lang: Azerbaijani
            """
                ],
                config=types.GenerateContentConfig(
                    response_modalities=["AUDIO"],
                    speech_config=types.SpeechConfig(
                        voice_config=types.VoiceConfig(
                            prebuilt_voice_config=types.PrebuiltVoiceConfig(
                                voice_name='Kore',
                            )
                        )
                    )
                )
            )
            '''response = client.models.generate_content(
                model="gemini-3.1-flash-live-preview", # 음성 입력을 받기 위해 gemini-3.1-flash-live-preview
                contents=[
                    types.Part.from_bytes(data=audio_input.read(), mime_type="audio/wav"),
                    ". " # 프롬프트 지침에 따른 Force-Translate 트리거
                ],
                config=types.GenerateContentConfig(
                    system_instruction=system_instruction,
                    response_modalities=["AUDIO"],
                    speech_config=types.SpeechConfig(
                        voice_config=types.VoiceConfig(
                            prebuilt_voice_config=types.PrebuiltVoiceConfig(
                                voice_name='Kore', # 혹은 'Puck', 'Aoide' 등 선택
                            )
                        )
                    )
                )
            )'''

            # 3. 결과 데이터 추출 및 재생
            audio_data = response.candidates[0].content.parts[0].inline_data.data
            st.audio(audio_data, format="audio/wav", autoplay=True)

if __name__ == "__main__":
    run_voice_translator()