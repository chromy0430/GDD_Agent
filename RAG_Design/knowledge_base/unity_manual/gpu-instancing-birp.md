--- 
Source: Unity 6 Manual (gpu-instancing-birp.md)
---

# GPU Instancing in the Built-In Render Pipeline
This section contains information on how to add GPU instancing support to a custom Unity **shader**A program that runs on the GPU. [More info](Shaders.html)
See in [Glossary](Glossary.html#shader). It first explains the shader keywords, variables, and functions custom Unity shaders require to support GPU instancing. Then it includes examples of how to add per-instance data to both **surface shaders**A streamlined way of writing shaders for the Built-in Render Pipeline. [More info](SL-SurfaceShaders.html)
See in [Glossary](Glossary.html#SurfaceShader) and vertex/fragment shaders.
## Render pipeline compatibility
| **Feature** | **Universal **Render Pipeline**A series of operations that take the contents of a Scene, and displays them on a screen. Unity lets you choose from pre-built render pipelines, or write your own. [More info](render-pipelines.html) See in [Glossary](Glossary.html#renderpipeline) (URP)** | **High Definition Render Pipeline (HDRP)** | **Custom Scriptable Render Pipeline (SRP)** | **Built-in Render Pipeline** |
| --- | --- | --- | --- | --- |
| **Custom GPU instanced shaders** | No | No | No | Yes |
## Additional resources
* [GPU instancing](GPUInstancing-landing.html)
* [Graphics performance and profiling](graphics-performance-profiling.html)