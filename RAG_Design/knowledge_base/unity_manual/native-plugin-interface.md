--- 
Source: Unity 6 Manual (native-plugin-interface.md)
---

# Native plug-in APIs
Access Unity Editor and Engine functionality such as low-level graphics device features, rendering, **shader**A program that runs on the GPU. [More info](Shaders.html)
See in [Glossary](Glossary.html#shader) compiler, memory management, profiling, and logging from your [native plug-in](plug-ins-native.html)A platform-specific native code library that is created outside of Unity for use in Unity. Allows you can access features like OS calls and third-party code libraries that would otherwise not be available to Unity. [More info](./plug-ins.html)
See in [Glossary](Glossary.html#nativeplug-in) code.
| **Topic** | **Description** |
| --- | --- |
| **[Introduction to the native plug-in APIs](native-plugin-interface-introduction.html)** | Locate the native **plug-in**A set of code created outside of Unity that creates functionality in Unity. There are two kinds of plug-ins you can use in Unity: Managed plug-ins (managed .NET assemblies created with tools like Visual Studio) and Native plug-ins (platform-specific native code libraries). [More info](./plug-ins.html) See in [Glossary](Glossary.html#plug-in) API files and import them into your native plug-in. |
| **[Native plug-in API for graphics and rendering](low-level-native-plugin-rendering-extensions.html)** | Access low-level graphics device and rendering features from native plug-ins. |
| **[Native plug-in API for shader compiler](low-level-native-plugin-shader-compiler-access.html)** | Control shader compiler variants from native plug-ins. |
| **[Native plug-in API for memory management](low-level-native-plugin-memory-manager-api.html)** | Access Unity’s memory manager and track memory usage from native plug-ins. |
| **[Memory manager API reference](low-level-native-plugin-memory-manager-api-reference.html)** | Use the memory manager API in native plug-ins. |
| **[Native plug-in API for profiling](LowLevelNativePluginProfiler.html)** | Extend the profiler and collect performance data from native plug-ins. |
| **[Native plug-in API for logging](low-level-native-plugin-logging.html)** | Write Unity log messages from native plug-ins. |
## Additional resources
* [Native plug-ins](plug-ins-native.html)
* [Import and configure plug-ins](plug-in-inspector.html)