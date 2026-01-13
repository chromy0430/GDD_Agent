1. 인터페이스 기반 추상화 (Interface-Based Abstraction)
핵심 원칙: 클래스 간의 직접 참조를 차단하고 인터페이스를 통해 상호작용하여 결합도를 낮춘다.

IDamageable 표준화: Enemy나 Player 클래스를 직접 참조하는 대신 IDamageable을 사용하여 어떤 객체든 데미지를 입을 수 있는 구조로 설계한다.

IWeapon 확장성: 플레이어가 특정 무기 클래스에 종속되지 않도록 IWeapon 인터페이스를 호출하여 무기 교체 및 신규 추가를 용이하게 한다.

유연성 확보: 인터페이스를 사용하면 코드 수정 없이도 새로운 기능을 가진 객체를 시스템에 즉시 통합할 수 있다.

2. 논리와 MonoBehaviour의 분리 (Logic-MonoBehaviour Separation)
핵심 원칙: 게임의 핵심 연산은 Unity 엔진 라이프사이클과 무관한 순수 C# 클래스(POCO)에서 처리한다.

POCO(Plain Old C# Object) 활용: 계산 로직을 MonoBehaviour 외부로 추출하여 엔진 의존성을 제거한다.

유닛 테스트 최적화: 유니티 에디터를 실행(Play Mode)하지 않고도 핵심 로직이 정확한지 0.001초 만에 검증할 수 있는 환경을 구축한다.

성능 이점: 불필요한 Update 호출을 줄이고 객체 지향적인 순수 로직에 집중할 수 있다.

3. 데이터 주도 설정 (Data-Driven Configuration)
핵심 원칙: 하드코딩된 수치와 에셋 참조를 ScriptableObject로 관리하여 데이터와 로직을 완전히 분리한다.

ScriptableObject 맵핑: 공격력, 사거리, 이동 속도 등 모든 밸런스 데이터를 에셋화한다.

기획 편의성: 코드를 수정하거나 컴파일할 필요 없이 인스펙터에서 즉시 수치를 조정하고 테스트할 수 있다.

재사용성: 하나의 클래스에 서로 다른 ScriptableObject 데이터 에셋을 할당하여 다양한 변종 객체를 생성한다.

4. 이벤트 기반 제어 흐름 (Event-Driven Control Flow)
핵심 원칙: 매 프레임 상태를 확인(Polling)하는 대신, 사건 발생 시 신호를 보내는(Push) 방식을 사용한다.

입력 시스템 격리: Update 내의 Input.GetKey 대신 C# Action 또는 UnityEvent를 활용하여 입력을 처리한다.

입력 소스 독립성: 키보드, 게임패드, 모바일 터치 등 입력 수단이 바뀌어도 실제 동작(Fire, Jump) 코드는 변경되지 않는다.

가독성 향상: 클래스 간의 복잡한 호출 관계가 이벤트 구독 모델로 단순화되어 스파게티 코드를 방지한다.

5. 정적 레지스트리 패턴 (Static Registry Pattern)
핵심 원칙: 성능에 악영향을 주는 Find 계열 함수를 금지하고, 객체가 스스로를 등록/해제하는 중앙 집중식 관리 시스템을 도입한다.

자동 등록 시스템: 객체가 생성(Awake)될 때 정적 리스트에 자신을 등록하고, 파괴(OnDestroy)될 때 해제한다.

조회 성능 최적화: HashSet<T> 기반의 레지스트리를 사용하여 $O(1)$의 속도로 현재 활성화된 객체들을 조회한다.

가장 가까운 타겟 찾기: 씬 전체를 검색하는 대신 레지스트리에 등록된 리스트만 순회하여 CPU 오버헤드를 최소화한다.

6. Implementation Notes (실무 구현 가이드)
영상 내용의 완벽한 구현과 안전성을 위해 봇이 코드 생성 시 반드시 준수해야 할 실무 디테일입니다.

6.1 POCO 생성자 주입 (Constructor Injection)
규칙: 로직 클래스(POCO)는 Resources.Load나 GameObject.Find를 내부에서 사용하지 않고, 필요한 데이터를 생성자를 통해 외부에서 주입받아야 합니다.

코드 예시:

C#

// Bad: 내부에서 의존성 해결 (테스트 불가)
public class WeaponLogic {
    public WeaponLogic() { 
        this.damage = 10; // 하드코딩 혹은 내부 로드 금지 
    }
}

// Good: 생성자를 통한 데이터 주입 [Video 09:47]
public class WeaponLogic {
    private readonly WeaponDataSO _config;
    public WeaponLogic(WeaponDataSO config) {
        _config = config;
    }
}
6.2 이벤트 구독 생명주기 (Memory Leak 방지)
필수 규칙: 이벤트를 구독(+=)한 객체는 비활성화되거나 파괴될 때 반드시 구독을 해제(-=)해야 합니다. 이를 누락하면 메모리 누수 및 치명적인 "MissingReferenceException" 오류가 발생합니다.

구현 패턴:

C#

void OnEnable() { input.OnFire += Fire; }
void OnDisable() { input.OnFire -= Fire; } // 필수!
6.3 유니티 객체 참조 주의 (Fake Null)
주의사항: 순수 C# 클래스(POCO)에서 MonoBehaviour 객체(예: IDamageable 타겟)를 참조할 때, 유니티 엔진이 객체를 Destroy하더라도 C# 래퍼 객체는 null이 아닐 수 있습니다.

해결책: POCO 내부에서 유니티 객체의 생존 여부를 확인할 때는 단순히 != null을 쓰기보다, 유니티의 생명주기 체크 로직을 신뢰하거나 호출 전 유효성 검사를 강화해야 합니다.