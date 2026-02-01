--- 
Source: Unity 6 Manual (shader-pso-trace-warming.md)
---

# Tracing and warming up PSOs
Trace and warm up graphics states with the experimental `GraphicsStateCollection` API to reduce **shader**A program that runs on the GPU. [More info](Shaders.html)
See in [Glossary](Glossary.html#shader) compilation stutters.
**Important**: `GraphicsStateCollection` is an experimental API and might be changed or removed in the future.
The following sections outline how to trace and warm up PSOs in your project:
| **Topic** | **Description** |
| --- | --- |
| [Introduction to PSO tracing and warming](shader-pso-introduction.html) | Understand what PSO tracing and warming is, and the project requirements to use the `GraphicsStateCollection` API. |
| [Trace and manage PSO data collections](shader-pso-trace.html) | Trace a new PSO data collection and manage existing collections. |
| [Warm up PSOs](shader-prewarm.html) | Warm up PSO collections on the GPU at runtime. |
| [PSO tracing and warming example](shader-pso-example.html) | Get started with PSO tracing and warm up using the Universal **Render Pipeline**A series of operations that take the contents of a Scene, and displays them on a screen. Unity lets you choose from pre-built render pipelines, or write your own. [More info](render-pipelines.html) See in [Glossary](Glossary.html#renderpipeline) (URP) sample. |
## Additional resources
* [Prevent shader compilation stutters with PSO Tracing in Unity 6](https://discussions.unity.com/t/prevent-shader-compilation-stutters-with-pso-tracing-in-unity-6/951031) (Unity Discussions)