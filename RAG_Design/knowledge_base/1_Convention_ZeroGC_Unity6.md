# Unity 6.3 Zero-GC & Performance Guidelines

## 1. Memory Management (Zero-GC Rule)
**Core Principle:** Hot Path(`Update`, `FixedUpdate`, `LateUpdate`) 내부에서의 힙 할당은 절대 금지한다.

### 1.1 Collections
- **Forbidden:** `List<T>`, `Dictionary<K,V>` inside loops.
- **Recommended:** - Use `NativeArray<T>`, `NativeList<T>` (Collections package) for heavy data processing.
  - Use pre-allocated `List<T>` with `Capacity` set.
  - Use `Span<T>` for array slicing without allocation.

### 1.2 Strings
- **Forbidden:** String concatenation (`+` operator), `.ToString()` inside Update.
- **Recommended:** - Use `ZString` (Zero allocation string library) or `StringBuilder` (reused instance).
  - Use `FixedString32Bytes`, `FixedString64Bytes` for ECS/Jobs compatibility.

### 1.3 Boxing
- Avoid passing value types (`struct`, `int`, `enum`) to parameters expecting `object` or interfaces.
- Be careful with `Debug.Log($"Val: {x}");` -> Use strict formatters or conditional compilation.

## 2. Asynchronous Logic (Unity 6.3)
**Core Principle:** Legacy `Coroutine` is deprecated for logic. Use `Awaitable`.

- **Do NOT Use:** `StartCoroutine()`, `IEnumerator` (except for legacy asset/UI fades).
- **USE:** `Awaitable`, `async/await`.
  - `await Awaitable.NextFrameAsync();`
  - `await Awaitable.WaitForSecondsAsync(1.0f);`
- **Why?** `Awaitable` in Unity 6 reduces overhead and provides better exception handling compared to Coroutines.

## 3. Input System
- **Forbidden:** `Input.GetKey`, `Input.GetMouseButton`.
- **Mandatory:** Use **Input System Package (New)**.
  - Use `InputAction.CallbackContext` for event-driven input.
  - Separate `InputReader` (ScriptableObject) to broadcast input events via C# Actions.