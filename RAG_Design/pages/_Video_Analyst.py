import streamlit as st
from google import genai
from google.genai import types
import os
import time
import json
import tempfile
# utils.py의 설정을 그대로 가져옵니다.
from utils import render_sidebar_settings, retry_with_backoff

# ==========================================
# 1. 설정
# ==========================================
st.set_page_config(layout="wide", page_title="영상 분석 에이전트 (Video Reverse Engineer)")

# ==========================================
# 2. 유틸리티 함수 (영상 처리)
# ==========================================
@retry_with_backoff(max_retries=3, initial_delay=4)
def upload_video_to_gemini(uploaded_file, api_key):
    """
    Streamlit 메모리 파일을 로컬 임시 파일로 저장 후 Gemini에 업로드합니다.
    """
    # 1. 임시 파일 생성
    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp4") as tmp:
        tmp.write(uploaded_file.getvalue())
        tmp_path = tmp.name

    client = genai.Client(api_key=api_key)
    
    try:
        with st.spinner("📡 영상을 Gemini 서버로 전송 중입니다..."):
            # SDK v2 방식: file 매개변수 사용
            file_ref = client.files.upload(file=tmp_path)
        return file_ref, client
    except Exception as e:
        st.error(f"업로드 실패: {e}")
        return None, None
    finally:
        # 로컬 임시 파일 정리
        if os.path.exists(tmp_path):
            os.remove(tmp_path)

def wait_for_files_active(client, files):
    """
    영상 인덱싱(Processing)이 끝날 때까지 대기합니다.
    """
    st.info("⏳ 영상 처리 대기 중... (서버 인덱싱)")
    progress_bar = st.progress(0)
    
    for name in (file.name for file in files):
        file = client.files.get(name=name)
        while file.state.name == "PROCESSING":
            time.sleep(2) 
            file = client.files.get(name=name)
            
        if file.state.name != "ACTIVE":
            st.error(f"영상 처리 실패: {file.name} (상태: {file.state.name})")
            return False
            
    progress_bar.progress(100)
    st.success("✅ 영상 처리 완료! 분석을 시작합니다.")
    return True

# ==========================================
# 3. 메인 로직
# ==========================================
def main():
    st.title("🎥 게임 영상 리버스 엔지니어링 봇")
    st.markdown("`utils.py`에 정의된 최신 모델을 사용하여 영상을 분석하고 코드를 생성합니다.")

    # [핵심 변경] utils.py의 사이드바 설정을 그대로 호출합니다.
    # 사용자가 사이드바에서 'gemini-3-flash' 등을 선택하면 selected_model_name에 담깁니다.
    api_key_input, cx_id, selected_model_name = render_sidebar_settings()
    
    col1, col2 = st.columns([1, 1])

    with col1:
        st.subheader("1. 영상 업로드")
        uploaded_video = st.file_uploader("분석할 MP4/MOV 파일", type=['mp4', 'mov', 'avi', 'mkv'])
    
    with col2:
        st.subheader("2. 분석 요청 사항")
        user_query = st.text_area(
            "어떤 부분을 중점적으로 분석할까요?", 
            value="이 영상에 나오는 스킬 이펙트와 캐릭터 움직임이 어떻게 구현되었는지 Unity URP와 C# 스크립트 기준으로 설명해줘.",
            height=150
        )

    if st.button("🚀 영상 분석 시작 (Analyze Video)", type="primary"):
        if not api_key_input:
            st.warning("API Key가 필요합니다.")
            return

        if not uploaded_video:
            st.warning("영상 파일을 업로드해주세요.")
            return

        # 1. 파일 업로드
        file_ref, client = upload_video_to_gemini(uploaded_video, api_key_input)
        
        if file_ref:
            # 2. 상태 대기
            if wait_for_files_active(client, [file_ref]):
                
                # 3. 프롬프트 구성
                system_prompt = """
                당신은 **Unity Graphics Engineer**입니다.
                영상을 프레임 단위로 분석하여 게임의 구현 로직을 역설계하십시오.

                [분석 가이드]
                1. **VFX 분석:** 파티클이 GPU Instancing인지, CPU 기반인지, VFX Graph인지 추론하십시오.
                2. **Animation:** 캐릭터 움직임이 Root Motion인지, In-place 애니메이션에 코드로 이동하는 것인지 분석하십시오.
                3. **Camera:** 시점 변환이 Cinemachine을 사용한 것으로 보이는지, 쉐이크 효과나 Post-Processing(Bloom, Vignette)이 적용되었는지 확인하십시오.

                결과는 개발자가 바로 따라 할 수 있는 **기술 명세서(Technical Spec)** 형태로 작성하십시오.
                """
                
                # 레거시 프롬프트
                '''"""
                당신은 시니어 Unity 클라이언트 개발자이자 테크니컬 아티스트(TA)입니다.
                사용자가 제공한 게임플레이/튜토리얼 영상을 분석하여 구현 원리를 역설계(Reverse Engineering)해야 합니다.

                **필수 준수 사항:**
                1. **Unity 6.3 LTS / URP** 환경 기준.
                2. **시각적 요소 분석:** 쉐이더 그래프, 파티클 시스템, VFX Graph 사용 여부 식별.
                3. **로직 추론:** 입력 -> 처리 -> 출력(이펙트/애니메이션) 과정을 단계별로 설명.
                4. **코드 제공:** 핵심 로직을 **C# (Monobehaviour)** 코드로 작성 (SOLID 원칙 준수).
                5. **데이터 변화 시각화:** [입력: A] -> (로직) -> [출력: B] 형태의 텍스트 다이어그램 포함.

                **출력 형식:**
                1. **🔍 영상 분석 요약**
                2. **🛠 기술적 분석 (Visual & Logic)**
                3. **💾 데이터 흐름 (Data Flow)**
                4. **💻 핵심 C# 구현 코드**
                5. **🎨 쉐이더/VFX 설정 가이드**
                """'''

                request_content = [
                    system_prompt,
                    file_ref, 
                    f"\n\n[사용자 요청사항]: {user_query}"
                ]

                # 4. 분석 요청 (선택된 모델 사용)
                with st.spinner(f"🧠 {selected_model_name} 모델이 영상을 분석 중입니다..."):
                    try:
                        # [핵심] 사이드바에서 선택한 모델명을 그대로 사용합니다.
                        response = client.models.generate_content(
                            model=selected_model_name,
                            contents=request_content
                        )
                        
                        st.divider()
                        st.subheader("📊 분석 결과 Report")
                        st.markdown(response.text)
                        
                    except Exception as e:
                        st.error(f"분석 중 오류 발생: {e}")
                        st.warning(f"선택하신 모델({selected_model_name})이 영상을 지원하지 않거나, 트래픽이 많을 수 있습니다.")

if __name__ == "__main__":
    main()