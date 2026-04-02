import streamlit as st
import os
import asyncio
from google import genai
from google.genai import types

async def get_live_translation(audio_bytes, system_instruction, text_prompt):
    import wave
    import io
    from google import genai
    from google.genai import types
    
    client = genai.Client(http_options={'api_version': 'v1alpha'})
    
    config = types.LiveConnectConfig(
        system_instruction=types.Content(parts=[types.Part.from_text(text=system_instruction)]),
        response_modalities=["AUDIO"],
        speech_config=types.SpeechConfig(
            voice_config=types.VoiceConfig(
                prebuilt_voice_config=types.PrebuiltVoiceConfig(
                    voice_name='Kore'
                )
            )
        )
    )
    
    output_audio = bytearray()
    
    async with client.aio.live.connect(model="gemini-3.1-flash-live-preview", config=config) as session:
        # 1. 번역 지시 프롬프트 전송
        await session.send_realtime_input(text=text_prompt)
        
        # 2. WAV 파일에서 헤더를 제거하고 원시 PCM 추출
        with wave.open(io.BytesIO(audio_bytes), 'rb') as wf:
            framerate = wf.getframerate()
            pcm_data = wf.readframes(wf.getnframes())
            
        # 3. 추출된 PCM 데이터를 문서 규격에 맞춰 전송
        await session.send_realtime_input(
            audio=types.Blob(
                data=pcm_data,
                mime_type=f"audio/pcm;rate={framerate}"
            )
        )
        
        # 4. [수정됨] 오디오 스트림 종료 신호 전송 (응답 강제 트리거)
        await session.send_realtime_input(audio_stream_end=True)
        
        # 5. 서버 응답 (오디오 청크) 수신 및 병합
        async for response in session.receive():
            if response.server_content is not None:
                if response.server_content.model_turn is not None:
                    for part in response.server_content.model_turn.parts:
                        if part.inline_data and part.inline_data.data:
                            output_audio.extend(part.inline_data.data)
                
                if response.server_content.turn_complete:
                    break
                    
    # 응답받은 데이터가 없는 경우 안전하게 None 반환
    if not output_audio:
        return None

    # 6. [수정됨] 수신된 24kHz 원시 PCM을 온전한 WAV 파일로 패키징
    wav_io = io.BytesIO()
    with wave.open(wav_io, 'wb') as wav_file:
        wav_file.setnchannels(1)      # 모노 채널
        wav_file.setsampwidth(2)      # 16-bit (2 bytes)
        wav_file.setframerate(24000)  # Live API 출력 규격 
        wav_file.writeframes(output_audio)

    return wav_io.getvalue()

def run_voice_translator():
    st.title("🛡️ Phantom Linguist: 실시간 음성 번역기")
    
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    PROMPT_PATH = os.path.join(BASE_DIR, "Translator_Prompt.txt")

    try:
        with open(PROMPT_PATH, "r", encoding="utf-8") as f:
            system_instruction = f.read()
    except FileNotFoundError:
        st.error("프롬프트 파일이 없습니다.")
        return

    # [Danger] 하드코딩 유지. 단, OS 환경 변수에 직접 주입하여 내부 aio 클라이언트가 누락 없이 인식하도록 강제함.
    os.environ["GEMINI_API_KEY"] = "AIzaSyCf9qWfPQuwUtbnZNEsjNc1_F-lQp-Oacs"

    audio_input = st.audio_input("대화를 시작하세요 (한국어 -> 번역)")

    if audio_input:
        with st.spinner("번역 중..."):
            audio_bytes = audio_input.read()
            text_prompt = """
            Translate the spoken Korean audio into Italiano.

            Requirements:
            - Output ONLY the translated result.
            - Do not explain, do not summarize.
            - Preserve tone, nuance, and speaking style exactly.
            - Maintain politeness level and emotional expression.

            Target_Lang: Italiano
            """
            
            try:
                # api_key 파라미터 전달 제거
                result_audio = asyncio.run(
                    get_live_translation(audio_bytes, system_instruction, text_prompt)
                )
                
                if result_audio:
                    st.audio(result_audio, format="audio/wav", autoplay=True)
                else:
                    st.error("모델로부터 오디오 응답을 받지 못했습니다.")
            except Exception as e:
                st.error(f"Live API 통신 오류 발생: {e}")

if __name__ == "__main__":
    run_voice_translator()