--- 
Source: Unity 6 Manual (runtime-performance-scaling-introduction.md)
---

# Introduction to runtime performance scaling
Runtime performance scaling is the process of adjusting an application’s quality settings while it’s running. The goal is to maintain a stable frame rate and manage device resources like power and temperature by dynamically trading visual quality for performance.
## Systems for runtime performance scaling
In Unity, you can control quality settings at runtime with the following tools and APIs:
* [Dynamic Resolution](DynamicResolution-landing.html)A Camera setting that allows you to dynamically scale individual render targets to reduce workload on the GPU. [More info](DynamicResolution-landing.html)
  See in [Glossary](Glossary.html#dynamicresolution): Adjusts rendering resolution automatically to maintain a target frame rate in URP and HDRP.
* [QualitySettings](../ScriptReference/QualitySettings.html) API: Defines and changes between performance tiers with different settings for shadows, textures, and more.
* [Level of Detail (LOD)](LevelOfDetail.html): Modifies the complexity of rendered models by changing the **LOD**The *Level Of Detail* (LOD) technique is an optimization that reduces the number of triangles that Unity has to render for a GameObject when its distance from the Camera increases. [More info](LevelOfDetail.html)
  See in [Glossary](Glossary.html#LOD) bias, using simpler or more detailed meshes based on performance needs.
* [Frame Timing Manager](frame-timing-manager.html): Provides low-level CPU and GPU timing data, enabling **scripts**A piece of code that allows you to create your own Components, trigger game events, modify Component properties over time and respond to user input in any way you like. [More info](creating-scripts.html)
  See in [Glossary](Glossary.html#Scripts) to detect performance bottlenecks and respond as needed.
You can also use the [Adaptive Performance](adaptive-performance/adaptive-performance.html) system, which monitors device performance and automatically manages these foundational features and APIs to meet your performance targets. This system is especially useful on mobile devices, where hardware constraints can change rapidly.
## Additional resources
* [Memory in Unity](performance-memory.html)
* [Unity Profiler](Profiler.html)
* [Profiling tools](performance-profiling-tools.html)
* [Graphics performance and profiling](graphics-performance-profiling.html)