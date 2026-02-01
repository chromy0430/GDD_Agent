--- 
Source: Unity 6 Manual (profiler-adding-information-code.md)
---

# Adding profiling information to your code
You can add **profiler markers**Placed in code to describe a CPU or GPU event that is then displayed in the Unity Profiler window. Added to Unity code by default, or you can use [ProfilerMarker API](https://docs.unity3d.com/Packages/com.unity.profiling.core@latest/index.html?subfolder=/manual/profilermarker-guide.html) to add your own custom markers. [More info](profiler-markers.html)
See in [Glossary](Glossary.html#profilermarker) and counters to your code to further understand specific performance data related to your application, and visualize that data in custom Profiler modules.
| **Topic** | **Description** |
| --- | --- |
| **[Adding profiling information to your code introduction](profiler-adding-information-code-intro.html)** | Use profiler markers and counters to collect specific data about your application. |
| **[Adding profiler markers to your code](profiler-add-markers-code.html)** | Add profiler markers to mark up areas of your code. |
| **[Adding profiler counters to your code](profiler-add-counters-code.html)** | Collect specific statistics with **profiler counters**Placed in code with the ProfilerCounter API to track metrics, such as the number of enemies spawned in your game. [More info](https://docs.unity3d.com/Packages/com.unity.profiling.core@latest/index.html?subfolder=/manual/profilercounter-guide.html) See in [Glossary](Glossary.html#profilercounter). |
| **[Visualizing profiler counters](profiler-creating-custom-counters.html)** | Add profiler counters to custom Profiler modules. |
## Additional resources
* [Using the Profiler window](ProfilerWindow.html)
* [Profiler modules introduction](profiler-modules-introduction.html)
* [Customizing Profiler modules](profiler-customizing.html)
* [Profiling low-level native plug-ins](LowLevelNativePluginProfiler.html)
* [Memory profiling low-level native plug-ins](low-level-native-plugin-memory-manager-api.html)