--- 
Source: Unity 6 Manual (UsingDX11GL3Features.md)
---

# DirectX
Unity supports the DirectX graphics API including both DirectX 11 and DirectX 12. However, not all features are available in DirectX 11. For more information, refer to [Feature comparison of DirectX 11 and DirectX 12 in Unity](#comparison-of-directx11-and-directx12-in-unity).
## Set your default graphics API to DirectX
You can choose to set DirectX 11 (DX11) or DirectX 12 (DX12) as your default Graphics API in the Editor or Standalone Player:
1. Open the [Player settings](class-PlayerSettings.html)Settings that let you set various player-specific options for the final game built by Unity. [More info](class-PlayerSettings.html)
   See in [Glossary](Glossary.html#PlayerSettings) (menu: **Edit** > **Project Settings** > **Player**).
2. In the **Other Settings** > **Rendering** section, disable the **Auto Graphics API for a platform (Windows/Mac/Linux)** option.
3. Select the **Add** (**+**) button, then select **Direct3D11** or **Direct3D12** from the list of the supported Graphics APIs.
## Feature comparison of DirectX 11 and DirectX 12 in Unity
The following lists include the features introduced with the DirectX 12 graphics API, which are unavailable in DirectX 11.
| **APIs** | **DirectX 11** | **DirectX 12** |
| --- | --- | --- |
| [Dynamic resolution](DynamicResolution-introduction.html)A Camera setting that allows you to dynamically scale individual render targets to reduce workload on the GPU. [More info](DynamicResolution-landing.html) See in [Glossary](Glossary.html#dynamicresolution) | Unsupported | Supported |
| [Asynchronous compute](../ScriptReference/Graphics.ExecuteCommandBufferAsync.html) | Unsupported | Supported |
| [Native render pass](../ScriptReference/Rendering.ScriptableRenderContext.BeginRenderPass.html) | Unsupported | Supported |
| [Ray tracing acceleration](../ScriptReference/Rendering.RayTracingAccelerationStructure.html) | Unsupported | Supported |
| [Graphics state collection](../ScriptReference/Experimental.Rendering.GraphicsStateCollection.html) | Unsupported | Supported |
| [XR foveated rendering](xr-foveated-rendering.html) | Unsupported | Supported |
| **Render Threading Mode** | **DirectX 11** | **DirectX 12** |
| --- | --- | --- |
| [Direct](../ScriptReference/Rendering.RenderingThreadingMode.Direct.html) | Supported | Supported |
| [Single threaded](../ScriptReference/Rendering.RenderingThreadingMode.SingleThreaded.html) | Supported | Supported |
| [Main + render thread](../ScriptReference/Rendering.RenderingThreadingMode.MultiThreaded.html) | Supported | Supported |
| [Legacy jobified](../ScriptReference/Rendering.RenderingThreadingMode.LegacyJobified.html) | Supported | Supported |
| [Native graphics jobs](../ScriptReference/Rendering.RenderingThreadingMode.NativeGraphicsJobs.html) | Unsupported | Supported |
| [Split graphics jobs](../ScriptReference/Rendering.RenderingThreadingMode.NativeGraphicsJobsSplitThreading.html) | Unsupported | Supported |
| ****Shader**A program that runs on the GPU. [More info](Shaders.html) See in [Glossary](Glossary.html#shader) features** | **DirectX 11** | **DirectX 12** |
| --- | --- | --- |
| [Ray tracing shader](../ScriptReference/Rendering.RayTracingShader.html) | Unsupported | Supported |
| [Inline ray tracing](../ScriptReference/ComputeShader.SetRayTracingAccelerationStructure.html) (`#pragma multi_compile _ UNITY_DEVICE_SUPPORTS_INLINE_RAY_TRACING`) | Unsupported | Supported |
| [Native 16-bit](SL-ShaderCompileTargets.html) (`#pragma multi_compile _ UNITY_DEVICE_SUPPORTS_NATIVE_16BIT`) | Unsupported | Supported |
| [Wave function](SL-ShaderCompileTargets.html) (`#pragma multi_compile _ UNITY_DEVICE_SUPPORTS_WAVE_ANY`) | Unsupported | Supported |
| **Universal **Render Pipeline**A series of operations that take the contents of a Scene, and displays them on a screen. Unity lets you choose from pre-built render pipelines, or write your own. [More info](render-pipelines.html) See in [Glossary](Glossary.html#renderpipeline)** | **DirectX 11** | **DirectX 12** |
| --- | --- | --- |
| [Raster pass merging](urp/render-graph-introduction.html) | Unsupported | Supported (Windows on ARM) |
| [Native RenderPass](urp/urp-universal-renderer.html#native-renderpass) | Unsupported | Supported (Windows on ARM) |
| [Framebuffer fetch](urp/render-graph-framebuffer-fetch.html) | Unsupported | Supported (Windows on ARM) |
| **High Definition Render Pipeline** | **DirectX 11** | **DirectX 12** |
| --- | --- | --- |
| [Hardware dynamic resolution](https://docs.unity3d.com/Packages/com.unity.render-pipelines.high-definition@latest/index.html?subfolder=/manual/Dynamic-Resolution.html) | Unsupported | Supported |
| [Asynchronous Compute Shaders](https://docs.unity3d.com/Packages/com.unity.render-pipelines.high-definition@latest/index.html?subfolder=/manual/frame-settings-reference.html#asynchronous-compute-shaders) | Unsupported | Supported |
| [Ray traced ambient occlusion](https://docs.unity3d.com/Packages/com.unity.render-pipelines.high-definition@latest/index.html?subfolder=/manual/Ray-Traced-Ambient-Occlusion.html) | Unsupported | Supported |
| [Ray traced contact shadows](https://docs.unity3d.com/Packages/com.unity.render-pipelines.high-definition@latest/index.html?subfolder=/manual/Ray-Traced-Contact-Shadows.html) | Unsupported | Supported |
| [Ray traced global illumination](https://docs.unity3d.com/Packages/com.unity.render-pipelines.high-definition@latest/index.html?subfolder=/manual/Ray-Traced-Global-Illumination.html) | Unsupported | Supported |
| [Ray traced reflections](https://docs.unity3d.com/Packages/com.unity.render-pipelines.high-definition@latest/index.html?subfolder=/manual/Ray-Traced-Reflections.html) | Unsupported | Supported |
| [Ray traced shadows](https://docs.unity3d.com/Packages/com.unity.render-pipelines.high-definition@latest/index.html?subfolder=/manual/Ray-Traced-Shadows.html) | Unsupported | Supported |
| [Ray traced recursion](https://docs.unity3d.com/Packages/com.unity.render-pipelines.high-definition@latest/index.html?subfolder=/manual/Ray-Tracing-Recursive-Rendering.html) | Unsupported | Supported |
| [Ray traced subsurface scattering](https://docs.unity3d.com/Packages/com.unity.render-pipelines.high-definition@latest/index.html?subfolder=/manual/Ray-Traced-Subsurface-Scattering.html) | Unsupported | Supported |
## Additional resources
* [Configure graphics APIs](configure-graphicsAPIs.html)
* [Surface Shaders with DX11 / OpenGL Core Tessellation](SL-SurfaceShaderTessellation.html)
* [Surface shaders and DirectX 11 HLSL syntax](SL-SurfaceShaders.html#surface-shaders-directX)