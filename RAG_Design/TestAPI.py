import requests

# 여기에 사용자님의 키와 CX를 직접 넣어보세요
API_KEY = "AIzaSyCIXIm3x_aootnPBxFO7V6304pdIL5O6yY"
CX_ID = "1628e81ac0dfe42db" # 사용자님이 알려주신 CX

url = "https://www.googleapis.com/customsearch/v1"
params = {
    'key': API_KEY,
    'cx': CX_ID,
    'q': 'test'
}

print(f"📡 API 테스트 중... (CX: {CX_ID})")
response = requests.get(url, params=params)

if response.status_code == 200:
    print("✅ 성공! 검색 결과가 정상적으로 돌아왔습니다.")
    print(response.json()['items'][0]['snippet'])
else:
    print(f"❌ 실패! 상태 코드: {response.status_code}")
    print("▼ 구글이 보낸 에러 메시지 상세 내용 ▼")
    print(response.text) # 여기에 "Billing not enabled" 같은 진짜 이유가 나옵니다.