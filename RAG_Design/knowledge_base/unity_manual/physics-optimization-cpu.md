--- 
Source: Unity 6 Manual (physics-optimization-cpu.md)
---

# Optimize the physics system for CPU usage
You can optimize how the Unity physics system uses CPU resources in several ways. For example, you can adjust simulation frequency, carefully manage **collider**An invisible shape that is used to handle physical collisions for an object. A collider doesn’t need to be exactly the same shape as the object’s mesh - a rough approximation is often more efficient and indistinguishable in gameplay. [More info](CollidersOverview.html)
See in [Glossary](Glossary.html#collider) types, configure **Rigidbody**A component that allows a GameObject to be affected by simulated gravity and other forces. [More info](class-Rigidbody.html)
See in [Glossary](Glossary.html#Rigidbody) component behaviors, and more. Effective CPU optimization helps ensure your game maintains a high frame rate and responsive physics interactions.
Use the guidance in these pages to maintain your target frame rate and ensure smooth, responsive gameplay. The instructions in these pages address issues identified by Unity Editor diagnostic tools. Before you apply these optimizations described in the documentation in this section and throughout your development, you must be familiar with these diagnostic tools:
* [**The Unity Profiler**](Profiler.html)
* [**The Memory Profiler**](https://docs.unity3d.com/Packages/com.unity.memoryprofiler@latest)
* [**The Physics Debug window**](PhysicsDebugVisualization.html)
| **Topic** | **Description** |
| --- | --- |
| **[Set fixed timestep to optimize physics simulation frequency](physics-optimization-cpu-frequency.html)** | Configure the fixed time step and manage potential performance spirals to control physics update frequency. |
| **[Manually set physics simulation](physics-optimization-cpu-manual-simulation.html)** | Control over when physics calculations occur to align them with game performance. |
| **[Optimize physics for query-only or non-simulating games](physics-optimization-cpu-query-only.html)** | Prevent the default physics update loop from running to reduce unnecessary performance overhead. |
| **[Optimize transform value syncing](physics-optimization-cpu-transform-sync.html)** | Optimize the synchronization of Transform values with the physics system to improve performance and query accuracy. |
| **[Move static colliders](physics-optimization-cpu-static-colliders.html)** | Understand best practices for moving static colliders and when to use Kinematic **Rigidbody** components instead. |
| **[Use the layer collision matrix to reduce overlaps](physics-optimization-cpu-collision-layers.html)** | Reduce **collision**A collision occurs when the physics engine detects that the colliders of two GameObjects make contact or overlap, when at least one has a Rigidbody component and is in motion. [More info](CollidersOverview.html) See in [Glossary](Glossary.html#collision) calculation overhead by configuring interaction rules between **GameObjects**The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](class-GameObject.html) See in [Glossary](Glossary.html#GameObject) with collision layers. |
| **[Select a broad phase pruning algorithm](physics-optimization-cpu-broad-phase.html)** | Optimize physics performance in large **scenes**A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](CreatingScenes.html) See in [Glossary](Glossary.html#Scene) by selecting the most efficient broad phase pruning algorithm. |
| **[Collider types and performance](physics-optimization-cpu-collider-types.html)** | Select the most efficient collider types for different GameObjects. |
| **[Configure Mesh Collider component cooking options for optimization](physics-optimization-cpu-mesh-cooking-options.html)** | Optimize physics calculations by configuring cooking options for ****Mesh**The main graphics primitive of Unity. Meshes make up a large part of your 3D worlds. Unity supports triangulated or Quadrangulated polygon meshes. Nurbs, Nurms, Subdiv surfaces must be converted to polygons. [More info](mesh.html) See in [Glossary](Glossary.html#Mesh) Collider** components |
| **[Use Rigidbody sleeping to improve physics performance](physics-optimization-cpu-rigidbody-sleeping.html)** | Reduce CPU load and improve physics performance by enabling **Rigidbody** sleeping for stationary objects. |
| **[Adjust Rigidbody component solver iterations](physics-optimization-cpu-rigidbody-solver.html)** | Adjust solver iteration counts for a **Rigidbody** component to improve simulation accuracy. |
| **[Optimize Rigidbody component collision detection modes](physics-optimization-cpu-rigidbody-collision-modes.html)** | Balance collision accuracy and CPU performance by choosing appropriate detection modes for **Rigidbody** components. |
## Additional resources
* [Unity Profiler](Profiler.html)
* [Built-in 3D Physics](PhysicsOverview.html)
* [Memory Profiler](https://docs.unity3d.com/Packages/com.unity.memoryprofiler@latest)
* [Physics Project Settings](class-PhysicsManager.html)