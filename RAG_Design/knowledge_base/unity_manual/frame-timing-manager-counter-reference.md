--- 
Source: Unity 6 Manual (frame-timing-manager-counter-reference.md)
---

# Frame timing API counter reference
The following table describes the purpose of the counters that [the `FrameTiming` API](../ScriptReference/FrameTiming.html) provides.
| **FrameTiming API field** | ****Profiler counter**Placed in code with the ProfilerCounter API to track metrics, such as the number of enemies spawned in your game. [More info](https://docs.unity3d.com/Packages/com.unity.profiling.core@latest/index.html?subfolder=/manual/profilercounter-guide.html) See in [Glossary](Glossary.html#profilercounter)** | **Description** |
| --- | --- | --- |
| [`cpuFrameTime`](../ScriptReference/FrameTiming-cpuFrameTime.html) | **CPU Total Frame Time** | The total CPU frame time, in nanoseconds. Unity calculates this as the time between the ends of two frames, including any overheads or time spent waiting between frames. |
| [`cpuMainThreadFrameTime`](../ScriptReference/FrameTiming-cpuMainThreadFrameTime.html) | **CPU Main Thread Frame Time** | Active main thread work time in nanoseconds. This is the **PlayerLoop** time without the time the main thread was waiting for the VSync or render thread to finish its work, calculated as follows:   `cpuMainThreadFrameTime = PlayerLoop - GfxDevice.WaitForRenderThread - Gfx.WaitForPresentOnGfxThread - WaitForTargetFPS` |
| [`cpuMainThreadPresentWaitTime`](../ScriptReference/FrameTiming-cpuMainThreadPresentWaitTime.html) | N/A | The CPU time in nanoseconds spent waiting for the frame presentation or VSync during the frame, calculated as follows:   `cpuMainThreadPresentWaitTime = Gfx.WaitForPresentOnGfxThread + WaitForTargetFPS`. |
| [`cpuRenderThreadFrameTime`](../ScriptReference/FrameTiming-cpuRenderThreadFrameTime.html) | **CPU Render Thread Frame Time** | Active Render Thread work time in nanoseconds without Unity calling the `Present()` function, calculated as follows:   `cpuRenderThreadFrameTime = RenderLoop - Gfx.PresentFrame`. |
| [`gpuFrameTime`](../ScriptReference/FrameTiming-gpuFrameTime.html) | **GPU Frame Time** | The time difference in nanoseconds between the beginning and the end of the GPU rendering a single frame. |
The following diagram visualizes the relationships between **FrameTiming** and [the Profiler](Profiler.html) frame data.
![Diagram showing relation of FrameTiming API to Profiler data](../uploads/Main/frame-timing-manager-times.drawio.svg)
Diagram showing relation of FrameTiming API to Profiler data
## Additional resources
* [Get frame timing data](frame-timing-manager-get-timing-data.html)
* [Record frame timing data](frame-timing-manager-record-timing-data.html)