--- 
Source: Unity 6 Manual (shader-prewarm.md)
---

# Warm up PSOs
Warm up PSO collections on the GPU at runtime.
**Important**: `GraphicsStateCollection` is an experimental API and might be changed or removed in the future.
To reduce stuttering, compile **shaders**A program that runs on the GPU. [More info](Shaders.html)
See in [Glossary](Glossary.html#shader) and create PSOs before they’re first needed, so that the graphics driver caches them to disk. This is called warming up, prewarming, or precooking graphics states. You usually warm up during a loading screen, either when your application starts or while loading a **scene**A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](CreatingScenes.html)
See in [Glossary](Glossary.html#Scene).
## Warm up a collection
Once you’ve [traced a PSO data collection](shader-pso-trace.html), you can warm up the cached PSOs to disk.
**Note**: The recommended best practice is to prewarm your collection during application or scene loading sequences.
To warm up a PSO data collection, you can use two API methods:
* [GraphicsStateCollection.WarmUp](../ScriptReference/Experimental.Rendering.GraphicsStateCollection.WarmUp.html) schedules the creation of all PSOs in the collection.
* [GraphicsStateCollection.WarmUpProgressively](../ScriptReference/Experimental.Rendering.GraphicsStateCollection.WarmUpProgressively.html) schedules the creation of a set number of PSOs in the collection. Progressive warm up can result in a smoother experience and prevent blocking the application.
The `GraphicsStateCollection.WarmUp` and `GraphicsStateCollection.WarmUpProgressively` prewarm methods return a job handle, which you can use to set whether Unity performs the warming synchronously or asynchronously.
**Tip**: To trace any PSOs used by your application that weren’t created during the collection warmup, enable the [traceCacheMisses](../ScriptReference/Experimental.Rendering.GraphicsStateCollection.traceCacheMisses.html) option when you call `GraphicsStateCollection.WarmUp` or `GraphicsStateCollection.WarmUpProgressively`. This creates a separate [cacheMissCollection](../ScriptReference/Experimental.Rendering.GraphicsStateCollection.cacheMissCollection.html) to store the new PSOs, which you can manage as its own collection, or [Append to an existing collection](shader-pso-trace.html#append).
Once PSOs are created, they are cached to disk. The next time the GPU needs a PSO, they can be loaded directly from the cache.
## Check if shaders are warmed up
To check when Unity and the graphics driver compile shaders and create PSOs, search for the following **profiler markers**Placed in code to describe a CPU or GPU event that is then displayed in the Unity Profiler window. Added to Unity code by default, or you can use [ProfilerMarker API](https://docs.unity3d.com/Packages/com.unity.profiling.core@latest/index.html?subfolder=/manual/profilermarker-guide.html) to add your own custom markers. [More info](profiler-markers.html)
See in [Glossary](Glossary.html#profilermarker) in the [Profiler](Profiler.html)A window that helps you to optimize your game. It shows how much time is spent in the various areas of your game. For example, it can report the percentage of time spent rendering, animating, or in your game logic. [More info](Profiler.html)
See in [Glossary](Glossary.html#Profiler):
* `Shader.CreateGPUProgram` for Unity creating a GPU-specific version of a shader variant.
* `CreateGraphicsGraphicsPipelineImpl` for Unity creating a PSO.
## Additional resources
* [PSO tracing and warming example](shader-pso-example.html)
* [Trace and manage PSO data collections](shader-pso-trace.html)
* [How Unity loads and uses shaders](shader-loading.html)
* [Optimizing shader runtime performance](SL-ShaderPerformance.html)
* [GraphicsStateCollection Tracing and Warmup in Unity 6](https://forum.unity.com/threads/graphicsstatecollection-tracing-and-warmup-in-unity-6.1606386/) (Unity Discussions)