--- 
Source: Unity 6 Manual (performance-managed-memory.md)
---

# Managed memory
Unity’s managed memory system is a C# scripting environment based on the Mono or **IL2CPP**A Unity-developed scripting back-end which you can use as an alternative to Mono when building projects for some platforms. [More info](./scripting-backends-il2cpp.html)
See in [Glossary](Glossary.html#IL2CPP) Virtual Machines (VMs). The benefit of the managed memory system is that it manages the release of memory, so you don’t need to manually request the release of memory through your code. It makes use of a garbage collector to automatically free memory allocations.
| **Topic** | **Description** |
| --- | --- |
| **[Managed memory introduction](performance-managed-memory-introduction.html)** | Automatically manage the release and allocation of memory in your application. |
| **[Garbage collector introduction](performance-garbage-collector.html)** | Reclaim unused memory in your application. |
| **[Garbage collection modes](performance-incremental-garbage-collection.html)** | Overview of the different ways that the garbage collector runs. |
| **[Configuring garbage collection](performance-disabling-garbage-collection.html)** | Set up the garbage collector in your project. |
| **[Tracking garbage collection allocations](performance-track-garbage-collection.html)** | Monitor when your application performed garbage collection. |
| **[Avoid C# reflection overhead](performance-gc-avoid-reflection.html)** | Reduce garbage collector overhead by avoiding use of C# reflection at runtime. |
## Additional resources
* [Memory in Unity introduction](performance-memory-overview.html)
* [Memory Profiler module](profiler-memory.html)