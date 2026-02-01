--- 
Source: Unity 6 Manual (shader-built-in.md)
---

# Prebuilt shaders render pipeline compatibility reference
| ****Shaders**A program that runs on the GPU. [More info](Shaders.html) See in [Glossary](Glossary.html#shader)** | **Universal **Render Pipeline**A series of operations that take the contents of a Scene, and displays them on a screen. Unity lets you choose from pre-built render pipelines, or write your own. [More info](render-pipelines.html) See in [Glossary](Glossary.html#renderpipeline) (URP)** | **High Definition Render Pipeline (HDRP)** | **Custom SRP** | **Built-in Render Pipeline** |
| --- | --- | --- | --- | --- |
| [**URP shaders**](urp/shaders-in-universalrp.html) | Yes | No | No | No |
| [**HDRP shaders**](https://docs.unity3d.com/Packages/com.unity.render-pipelines.high-definition@17.0/manual/materials-and-surfaces.html) | No | Yes | No | No |
| [**Standard Shader**](shader-StandardShader-landing.html) | No  Can convert Standard Shader to equivalent on import | No  Can convert Standard Shader to equivalent on import | No | Yes |
| [**Standard Particle Shaders**](shader-StandardParticleShadersLanding.html) | No | No | No | Yes |
| [**Legacy shaders**](Built-inShaderGuide.html) | Yes  Simple unlit Legacy shaders will likely render fine, but they might not be SRP Batcher compatible. | Yes  Simple unlit Legacy shaders will likely render fine, but they might not be SRP Batcher compatible. They also do not support any HDRP features. For an unlit shader that supports HDRP features, use the HDRP/Unlit shader. | Yes  Simple unlit Legacy shaders will likely render fine, but they might not be SRP Batcher compatible. | Yes |