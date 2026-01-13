# URP & Rendering Guidelines (Unity 6.3)

## 1. Render Graph API
**Status:** Unity 6 URP uses **Render Graph** by default. Legacy `ScriptableRenderPass` is discouraged.

- **Custom Passes:** Must inherit from `ScriptableRenderPass` but implement `RecordRenderGraph`.
- **Resource Management:** Do not manually allocate RTHandles if possible. Let Render Graph handle lifetime/aliasing.
- **Performance:** Render Graph allows Unity to cull unused passes and optimize memory layout automatically.

## 2. Material & Shader
- **Material Property Blocks (MPB):**
  - Always use MPB for modifying material properties on individual objects to maintain **SRP Batcher** compatibility.
  - **Never** use `renderer.material` (creates a copy instance -> breaks batching). Use `renderer.GetPropertyBlock` / `SetPropertyBlock`.
- **Shader Graph:** Preferred over hand-written HLSL for maintenance.

## 3. VFX & Particles
- **VFX Graph:** Mandatory for complex effects (GPU computed).
- **Particle System:** Use only for simple, low-count CPU effects (UI effects, simple dust).