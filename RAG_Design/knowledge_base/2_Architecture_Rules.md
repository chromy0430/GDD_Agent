# Project Architecture & Design Patterns (Based on Samples)

이 문서는 프로젝트의 시스템 기획서 작성 및 데이터 구조 설계의 표준을 정의합니다.
모든 기획 내용은 **'데이터 주도(Data-Driven)'** 구조를 따르며, Unity 6.3 환경에서의 구현 가능성을 전제로 합니다.

## 1. System Design Hierarchy (기획서 작성 표준)
기획서는 아래 4단계 계층 구조를 반드시 준수해야 합니다. (참고: `00_시스템설계_통합본.txt`)

1.  **Overview (개요):** 시스템의 목적, 핵심 메커니즘, 타겟 유저 경험.
2.  **Logic & Flow (로직):**
    * State Machine (상태 전이): `08_몬스터시스템.txt`의 AI 패턴 참조.
    * Core Loop: Input → Process (규칙) → Feedback (연출) → Result (데이터 변경).
3.  **Data Structure (데이터 명세):**
    * 변수명, 데이터 타입, 참조 테이블 명시. (CSV 파일 기반 필드 정의)
4.  **UI/UX & Visual (표현):**
    * 화면 레이아웃, 연출 타이밍, VFX 연결. (참고: `07_UI_UX설계.txt`, `animation_timing.txt`)

---

## 2. Data-Driven Architecture (ScriptableObject Map)
모든 고정 데이터(Static Data)는 `ScriptableObject`로 정의하며, 런타임 데이터(Dynamic Data)와 분리합니다.

### 2.1 Character System (참고: `02_캐릭터시스템.txt`)
* **Data Class (`CharacterDataSO`):**
    * **Base Stats:** `HP`, `ATK`, `DEF`, `Speed` (참고: `character_stats.txt`)
    * **Growth:** `LevelCurve` (AnimationCurve or Table), `ExpTable` (참고: `level_experience.txt`)
    * **Visuals:** `ModelPrefab`, `Portrait`, `ThemeColor` (참고: `character_visual_details.txt`)
* **Implementation Note:**
    * 캐릭터의 상태 이상(Status Effect)은 별도의 `StatusEffectSO` 리스트로 관리하여 확장성 확보.

### 2.2 Monster & AI System (참고: `08_몬스터시스템.txt`)
* **Data Class (`MonsterDataSO`):**
    * **Stats:** `MaxHP`, `AttackRange`, `MovementSpeed` (참고: `monster_database.txt`)
    * **Drop Table:** `LootTableSO` 참조 (참고: `monster_drops.txt`)
    * **Visual Design:** `Scale`, `ShaderParams`, `SpawnVFX` (참고: `monster_visual_design.txt`)
* **AI Pattern (FSM):**
    * 패턴 정의: `Idle` → `Detect` → `Chase` → `Attack` → `Dead` (참고: `monster_patterns.txt`)
    * 공격 패턴은 `ActionSO` 형태로 모듈화하여 재사용 권장.

### 2.3 Combat & Skill System (참고: `01_퍼즐전투`, `06_스킬`)
* **Data Class (`SkillDataSO`):**
    * **Logic:** `Cooldown`, `DamageMultiplier`, `TargetType` (Single/Area), `Element` (참고: `skill_database.txt`)
    * **Balance:** `LevelMultiplier`, `Cost` (참고: `skill_balance.txt`)
* **Elemental System (속성):**
    * **Interaction:** `ElementChartSO` (Matrix 구조)로 상성 계수 관리 (참고: `05_속성상성시스템.txt`, `element_chart.txt`)
    * 하드코딩된 `switch` 문 대신, `Dictionary<Element, float>` 구조 사용 권장.

### 2.4 Economy & Reward (참고: `03_경제시스템.txt`)
* **Data Class (`RewardTableSO`):**
    * **Gacha:** `RateTable` (Weighted Random) (참고: `gacha_rates.txt`)
    * **Shop:** `ProductList`, `Price`, `CurrencyType` (참고: `shop_items.txt`)
* **Validation:**
    * 재화의 소수점 처리는 `Floor`(내림)를 기본으로 하며, DB 저장 시 `BigInteger` 혹은 `SecureInt` 사용 고려.

---

## 3. Unity 6.3 Implementation Guidelines
위 기획 내용을 실제 코드로 옮길 때의 제약 사항입니다.

### 3.1 Zero-GC Data Handling
* **CSV Parsing:** 런타임에 텍스트 파싱 금지. 에디터 타임에 `ScriptableObject`로 변환하여 빌드에 포함.
* **Combat Calculations:**
    * 전투 공식(Damage Formula) 계산 시 `List<Modifier>` 할당 주의.
    * `NativeArray`를 활용한 버퍼링 권장 (특히 퍼즐 보드 연산 시).

### 3.2 Visual & Feedback (URP)
* **VFX:** 스킬 이펙트는 `VisualEffectGraph` 에셋을 `SkillDataSO`에 연결하여 인스턴싱.
* **UI:** `ui_layout.txt`에 정의된 레이아웃은 **UI Toolkit (UXML/USS)** 기반으로 설계.
* **Animation:** `animation_timing.txt`의 프레임 데이터는 `Animancer` 또는 `Animator Override Controller`로 제어.

---

## 4. Documentation formatting (샘플 기반 양식)
기획서 작성 시 아래 테이블 포맷을 유지하십시오.

**[Table Format Example: Skill]**
| ID | Name | Type | Element | Cooldown | Effect_Ref | Description |
|:--:|:----:|:----:|:-------:|:--------:|:----------:|:-----------:|
| 1001 | FireBall | Active | Fire | 5.0s | VFX_Fire_01 | 전방에 화염 구체 발사 |

**[Table Format Example: Monster Stat]**
| ID | Name | HP | ATK | DEF | Range | AI_Pattern |
|:--:|:----:|:--:|:---:|:---:|:-----:|:----------:|
| 2001 | Goblin | 150 | 25 | 5 | 1.5m | Melee_Aggressive |