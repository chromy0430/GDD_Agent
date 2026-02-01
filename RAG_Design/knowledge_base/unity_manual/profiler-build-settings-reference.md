--- 
Source: Unity 6 Manual (profiler-build-settings-reference.md)
---

# Build Profiles Profiler settings
Configure the way the Profiler collects data when you build your application.
The [Build Profiles window](build-profiles.html) has settings which you can enable to change how the Profiler measures data.
## Prerequisites
To enable the Profiler specific settings, you must enable the ****Development Build**A development build includes debug symbols and enables the Profiler. [More info](building-introduction.html)
See in [Glossary](Glossary.html#developmentbuild)** setting:
1. Open the **Build Profiles** window (menu: **File > Build Profiles**)
2. Select your application’s target platform
3. Enable the **Development Build** setting
![Build Profiles with Development Build enabled](../uploads/Main/profiler-build-profiles.png)
Build Profiles with Development Build enabled
## Profiler Build Profiles settings
There are two settings related to how the Profiler collects data.
| **Setting** | **Description** |
| --- | --- |
| **Autoconnect Profiler** | Enable this setting to automatically connect to the Profiler when your application starts. The Unity Editor bakes its IP address into the built player during the build process. When you start the player, it attempts to connect to the Profiler in the Editor located at the baked IP address. |
| **Deep Profiling Support** | Unity performs [Deep Profiling](profiler-deep-profiling.html) when the built Player starts, which means that the Profiler profiles every part of your code, and not just code timings explicitly wrapped in [Profiler markers](profiler-markers.html)Placed in code to describe a CPU or GPU event that is then displayed in the Unity Profiler window. Added to Unity code by default, or you can use [ProfilerMarker API](https://docs.unity3d.com/Packages/com.unity.profiling.core@latest/index.html?subfolder=/manual/profilermarker-guide.html) to add your own custom markers. [More info](profiler-markers.html) See in [Glossary](Glossary.html#profilermarker). This is useful to get profiling information on your application’s start up times, however, this adds a small amount of overhead to your build. |
## Additional resources
* [Connecting the Profiler to a data source](profiler-profiling-applications.html)
* [Build Profiles](BuildSettings.html)A set of customizable configuration settings to use when creating a build for your target platform. [More info](build-profiles.html)
  See in [Glossary](Glossary.html#buildprofile)
* [Instrument all function calls](profiler-deep-profiling.html)
* [Profiler markers introduction](profiler-markers.html)