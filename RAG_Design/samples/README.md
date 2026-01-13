# 데이터 시트 폴더 안내

## 📊 이 폴더의 목적

게임 개발에 **즉시 사용 가능한 데이터**가 CSV 형식으로 정리되어 있습니다.  
모든 데이터는 게임 밸런스와 시스템 설계 문서를 기반으로 작성되었습니다.

---

## 📁 파일 목록 (카테고리별)

### ⚔️ 전투 관련 (9개)

| 파일명 | 내용 | 행 수 |
|--------|------|-------|
| [element_chart.csv](element_chart.csv) | 속성 상성표 (25개 조합) | 25 |
| [element_stats.csv](element_stats.csv) | 속성별 스탯 보정 | 5 |
| [status_effects.csv](status_effects.csv) | 상태이상 10종 | 10 |
| [skill_database.csv](skill_database.csv) | 스킬 15종 | 15 |
| [skill_levels.csv](skill_levels.csv) | 스킬 레벨 1-10 | 10 |
| [skill_balance.csv](skill_balance.csv) | 스킬 밸런스 기준 | 5 |
| [monster_patterns.csv](monster_patterns.csv) | 몬스터 패턴 25개 | 25 |
| [monster_drops.csv](monster_drops.csv) | 드롭 테이블 | 20+ |
| [stage_difficulty.csv](stage_difficulty.csv) | 스테이지 난이도 18단계 | 18 |

### 👥 캐릭터 관련 (3개)

| 파일명 | 내용 | 행 수 |
|--------|------|-------|
| [character_stats.csv](character_stats.csv) | 캐릭터 13명 스탯 | 13 |
| [character_visual_design.csv](character_visual_design.csv) | 캐릭터 외형 설계 | 13 |
| [character_visual_details.csv](character_visual_details.csv) | 일러스트 제작 가이드 | 13 |

### 👹 몬스터 관련 (2개)

| 파일명 | 내용 | 행 수 |
|--------|------|-------|
| [monster_database.csv](monster_database.csv) | 몬스터 16종 | 16 |
| [monster_visual_design.csv](monster_visual_design.csv) | 몬스터 외형 설계 | 18 |

### 💰 경제 관련 (3개)

| 파일명 | 내용 | 행 수 |
|--------|------|-------|
| [gacha_rates.csv](gacha_rates.csv) | 가챠 확률 | 4 |
| [shop_items.csv](shop_items.csv) | 상점 상품 17종 | 17 |
| [reward_tables.csv](reward_tables.csv) | 보상 테이블 | 15 |

### 📈 성장 관련 (1개)

| 파일명 | 내용 | 행 수 |
|--------|------|-------|
| [level_experience.csv](level_experience.csv) | 레벨 1-100 경험치 | 19 |

### 🎨 UI/UX 관련 (4개)

| 파일명 | 내용 | 행 수 |
|--------|------|-------|
| [ui_layout.csv](ui_layout.csv) | UI 레이아웃 좌표 | 10 |
| [color_palette.csv](color_palette.csv) | 컬러 팔레트 17색 | 17 |
| [animation_timing.csv](animation_timing.csv) | 애니메이션 타이밍 | 15 |
| [ui_mockup.txt](ui_mockup.txt) | 전투 화면 ASCII | - |

### 📝 기타 (1개)

| 파일명 | 내용 |
|--------|------|
| [속성상성표.csv](속성상성표.csv) | element_chart.csv와 동일 (한글명) |

**총 파일 수**: 23개 (CSV 21개 + TXT 1개 + 중복 1개)

---

## 💡 사용 방법

### CSV 파일 열기
- **Excel**: 그대로 열기
- **Google Sheets**: 가져오기 사용
- **텍스트 에디터**: UTF-8 인코딩으로 열기
- **프로그래밍**: pandas, csv 라이브러리 사용

### 데이터 형식
```csv
항목1,항목2,항목3
값1,값2,값3
```
- 첫 줄: 컬럼명 (한글)
- 둘째 줄부터: 데이터
- 구분자: 쉼표(,)
- 인코딩: UTF-8

---

## 🔗 연관 문서

각 데이터 시트는 시스템 설계 문서와 연결되어 있습니다:

| 데이터 시트 | 설계 문서 |
|-------------|-----------|
| element_*.csv | [05_속성상성시스템.md](../02_시스템설계/05_속성상성시스템.md) |
| skill_*.csv | [06_스킬시스템.md](../02_시스템설계/06_스킬시스템.md) |
| character_*.csv | [02_캐릭터시스템.md](../02_시스템설계/02_캐릭터시스템.md) |
| monster_*.csv | [08_몬스터시스템.md](../02_시스템설계/08_몬스터시스템.md) |
| gacha_*.csv, shop_*.csv | [03_경제시스템.md](../02_시스템설계/03_경제시스템.md) |
| ui_*.csv | [07_UI_UX설계.md](../02_시스템설계/07_UI_UX설계.md) |

---

## 📖 주요 데이터 시트 가이드

### ⭐ 필수 데이터

#### element_chart.csv
```
용도: 속성 상성 계산
핵심: 화→목(1.5), 수→화(1.5), 목→수(1.5) 순환 구조
```

#### character_stats.csv
```
용도: 캐릭터 기본 스탯
핵심: HP, ATK, DEF, SPD, 스킬ID
```

#### skill_database.csv
```
용도: 스킬 정보
핵심: 데미지 배율, 쿨타임, 효과
```

#### monster_database.csv
```
용도: 적 정보
핵심: HP, ATK, 패턴, 드롭
```

### 🎨 비주얼 데이터

#### character_visual_design.csv
```
용도: 캐릭터 외형 설명
대상: 아티스트
내용: 헤어, 복장, 색상, 포즈 등
```

#### color_palette.csv
```
용도: 게임 컬러 시스템
대상: UI 디자이너
내용: HEX, RGB 값
```

---

## ⚙️ 개발 활용 예시

### Unity (C#)
```csharp
// CSV 로드 예시
TextAsset csvData = Resources.Load<TextAsset>("Data/character_stats");
string[] lines = csvData.text.Split('\n');
```

### Python
```python
import pandas as pd
df = pd.read_csv('character_stats.csv')
print(df.head())
```

### JavaScript
```javascript
const fs = require('fs');
const csv = require('csv-parser');

fs.createReadStream('character_stats.csv')
  .pipe(csv())
  .on('data', (row) => console.log(row));
```

---

## 🔧 수정 가이드

### 데이터 추가 시
1. 해당 CSV 파일 열기
2. 마지막 줄에 데이터 추가
3. ID는 순차적으로 증가
4. 관련 시스템 문서도 업데이트

### 밸런스 조정 시
1. skill_balance.csv 참조
2. DPS 기준에 맞춰 조정
3. stage_difficulty.csv도 함께 조정

### 신규 시스템 추가 시
1. 새 CSV 파일 생성
2. 이 README에 추가
3. 시스템 설계 문서 작성
4. 문서 하단에 데이터 시트 링크

---

## ⚠️ 주의사항

- **인코딩**: 반드시 UTF-8 사용 (한글 깨짐 방지)
- **일관성**: ID 체계 유지 (CH001, MON001 등)
- **검증**: 변경 후 관련 시스템 동작 확인
- **백업**: 수정 전 백업 권장

---

## 📊 데이터 통계

- **캐릭터**: 13명 (R 3명, SR 4명, SSR 3명, UR 3명)
- **몬스터**: 16종 + 레어 2종
- **스킬**: 15종
- **스테이지**: 18단계
- **상점 아이템**: 17종

---

**최종 수정**: 2024-10-30  
**관리자**: 데이터 팀
