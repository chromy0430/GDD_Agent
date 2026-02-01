--- 
Source: Unity 6 Manual (physics-optimization-memory.md)
---

# Optimize the physics system for memory usage
You can optimize how the Unity physics system uses memory resources by managing **collision**A collision occurs when the physics engine detects that the colliders of two GameObjects make contact or overlap, when at least one has a Rigidbody component and is in motion. [More info](CollidersOverview.html)
See in [Glossary](Glossary.html#collision) callback allocations and optimizing various physics queries. Efficient memory usage helps reduce garbage collection overhead and ensures smoother gameplay.
Use the guidance in these pages to maintain your target frame rate and ensure smooth, responsive gameplay. The instructions in these pages address issues identified by Unity Editor diagnostic tools. Before you apply these optimizations described in the documentation in this section and throughout your development, you must be familiar with these diagnostic tools:
* [**The Unity Profiler**](Profiler.html)
* [**The Memory Profiler**](https://docs.unity3d.com/Packages/com.unity.memoryprofiler@latest)
* [**The Physics Debug window**](PhysicsDebugVisualization.html)
| **Topic** | **Description** |
| --- | --- |
| **[Optimize collision callbacks](physics-optimization-collision-callbacks.html)** | Reduce memory allocations caused by frequent collision events. |
| **[Optimize raycasts and other physics queries](physics-optimization-raycasts-queries.html)** | Optimize physics query performance and reduce garbage collection overhead by using efficient query versions and batch processing. |
## Additional resources
* [Unity Profiler](Profiler.html)
* [Built-in 3D Physics](PhysicsOverview.html)
* [Memory Profiler](https://docs.unity3d.com/Packages/com.unity.memoryprofiler@latest)
* [Physics Project Settings](class-PhysicsManager.html)