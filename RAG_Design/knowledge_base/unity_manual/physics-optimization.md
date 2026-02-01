--- 
Source: Unity 6 Manual (physics-optimization.md)
---

# Optimize physics performance
Optimize physics system performance in the Unity Editor.
Use the guidance in these pages to optimize the physics system so you can maintain your target frame rate and ensure smooth, responsive gameplay. The instructions in these pages address issues identified by Unity Editor diagnostic tools. Before you apply the optimizations described in the documentation in this section and throughout your development, you must be familiar with these diagnostic tools:
* [**The Unity Profiler**](Profiler.html): The Profiler is the primary tool to measure CPU performance. The Profiler helps identify bottlenecks in your project, particularly in areas such as `Physics.FixedUpdate` and `Physics.Simulate`, and in its detailed breakdowns of physics phases such as broad phase and narrow phase processing. To open the Profiler window, go to **Window > Analysis > Profiler**.
* [**The Memory Profiler**](https://docs.unity3d.com/Packages/com.unity.memoryprofiler@latest): Use the Memory Profiler to identify and optimize memory allocations caused by physics operations, such as excessive `RaycastHit` arrays or frequent **collision**A collision occurs when the physics engine detects that the colliders of two GameObjects make contact or overlap, when at least one has a Rigidbody component and is in motion. [More info](CollidersOverview.html)
  See in [Glossary](Glossary.html#collision) data creation. You can use this information to reduce your garbage collection overhead.
* [**The Physics Debug**](PhysicsDebugVisualization.html) window: Use this tool to visually diagnose physics-related performance issues. It displays collision shapes, contacts, broad phase bounding boxes, and Rigidbody component sleep states. This helps you identify areas like overly complex colliders, unnecessary interactions, or objects failing to sleep, all of which contribute to performance bottlenecks. To open the Physics Debug window, select **Window > Analysis > Physics Debug**.
| **Topic** | **Description** |
| --- | --- |
| **[Optimize the physics system for CPU usage](physics-optimization-cpu.html)** | Optimize Unity’s physics system’s CPU usage by adjusting simulation frequency, managing **colliders**An invisible shape that is used to handle physical collisions for an object. A collider doesn’t need to be exactly the same shape as the object’s mesh - a rough approximation is often more efficient and indistinguishable in gameplay. [More info](CollidersOverview.html) See in [Glossary](Glossary.html#collider), and configuring **Rigidbody**A component that allows a GameObject to be affected by simulated gravity and other forces. [More info](class-Rigidbody.html) See in [Glossary](Glossary.html#Rigidbody) components. |
| **[Optimize the physics system for memory usage](physics-optimization-memory.html)** | Optimize Unity’s physics system’s memory usage by controlling collision callbacks and optimizing physics queries. |
| **[Understand physics performance issues](physics-performance-issues.html)** | Understand performance issues related to physics in your application. |
## Additional resources
* [Unity Profiler](Profiler.html)
* [Built-in 3D Physics](PhysicsOverview.html)
* [Memory Profiler](https://docs.unity3d.com/Packages/com.unity.memoryprofiler@latest)
* [Physics Project Settings](class-PhysicsManager.html)