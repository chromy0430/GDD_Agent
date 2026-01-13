# Game Design Evaluation Criteria (Internal Audit)

## 1. Technical Feasibility (Unity 6 / Mobile)
- **[Critical]** Does the design consider mobile hardware limitations?
  - *Fail:* "Real-time global illumination with 100 dynamic lights."
  - *Pass:* "Baked lighting with light probes, max 2 real-time pixel lights."
- **[Critical]** Is the scale defined?
  - *Fail:* "Infinite open world."
  - *Pass:* "Grid-based generated map (Chunk system)."

## 2. System Structure
- **Data Driven:** Does the design specify which values are adjustable? (e.g., "Attack speed curve should be editable in SO").
- **Core Loop:** Is the Input -> Process -> Reward loop clearly defined?

## 3. Content Scalability
- **Modularity:** Can we add a new character/item by just adding a data file, without coding?
  - If the design implies hard-coding logic for every new item -> **Reject**.

## 4. Monetization (If applicable)
- Are ad placements or IAP logic integrated into the game flow naturally, or tacked on?
- Does the design account for 'Free-to-Play' economy balance?

## Grading Scale
- **S (Perfect):** Ready for implementation. Unity components mapped, optimization clear.
- **A (Good):** Logic is sound, minor tech details missing.
- **B (Average):** Abstract concepts, needs tech refinement.
- **C (Poor):** Feasibility concerns, structure weak.
- **F (Fail):** Technically impossible or violates project pillars.

# Game Suitability Evaluation Criteria (Real-World Review Standard)

이 기준은 기획서가 실제 출시되었을 때 유저가 남길 **'리뷰 관점'**에서 평가합니다.

## 1. Price & Volume (가격 만족도) [10점]
- **Value for Money:** 책정된 가격(또는 BM) 대비 볼륨이 충분한가?
  - *Check:* "11,000원인데 컨텐츠가 2시간 분량이면 감점."
  - *Check:* 반복 플레이 요소(Roguelike, Multi-play)가 볼륨을 커버하는가?

## 2. Pros & Cons Analysis (게임성 장단점) [30점]
### 2.1 Pros (재미 요소)
- **Multiplayer:** "뱀서류인데 멀티가 된다" 같은 장르적 한계를 뚫는 요소가 있는가?
- **Exploration:** 맵 탐방이나 이동의 자유도가 보장되는가?
- **Growth Variety:** 속성 조합, 무기 진화 등 성장의 다양성이 확보되었는가?

### 2.2 Cons (불쾌한 경험 - Critical)
- **Forced Mechanics:** 유저가 싫어하는 미니게임(예: 조작감 나쁜 축구, 억지 퍼즐)이 강제되는가?
- **Environmental Stress:** '얼음맵', '미끄러짐', '시야 제한' 등 불합리한 억까 요소가 있는가?
- **Meta Stagnation:** 고난이도에서 특정 무기/트리만 강제되는가? (선택지 제한)
- **Accessibility:** 멀티플레이가 강제되는 도전과제가 있어 '솔플 유저'를 배척하지 않는가?

## 3. Freshness (신선도) [20점]
- **Innovation:** 기존 장르(예: 뱀서라이크)에 새로운 해석(멀티, 장르 융합)이 있는가?
- **Cliché:** 양산형 게임의 문법을 그대로 답습하지 않았는가?

## 4. Developer Dignity (개발사의 품위 & 소통) [20점]
- **Communication Plan:** 기획서에 유저 소통 채널(Discord, Mail) 운영 계획이 포함되었는가?
- **Bug/Issue Response:** 버그나 밸런스 붕괴 시 대응 매뉴얼(패치 주기 등)이 고려되었는가?
- **Noise Control:** 개발진 이슈나 운영 잡음이 발생할 소지가 있는 BM/시스템이 있는가?

## 5. Evaluator's Taste (취향 및 종합 경험) [20점]
- **Learning Curve:** "쉽게 배우고 입문할 수 있는가?" (Easy to learn)
- **Co-op Synergy:** 친구와 역할 분담(포지션, 업글 루트)을 의논하는 재미가 있는가?
- **Retention:** "시간 가는 줄 모르고 플레이"할 몰입 요소(Flow)가 설계되었는가?

---
## [Bonus] Internal Technical Audit (내부 기술 검토)
*위 점수와 별개로, 아래 기술적 결함 발견 시 '구현 불가(Fail)' 판정.*
1. **Mobile Optimization:** 모바일 타겟 시 발열/메모리 대책이 있는가?
2. **Unity Feature:** URP, Input System 등 최신 스택을 활용하는가?