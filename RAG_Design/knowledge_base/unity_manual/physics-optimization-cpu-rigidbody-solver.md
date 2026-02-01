--- 
Source: Unity 6 Manual (physics-optimization-cpu-rigidbody-solver.md)
---

# Adjust Rigidbody component solver iterations
Adjust solver iteration counts for individual ****Rigidbody**A component that allows a GameObject to be affected by simulated gravity and other forces. [More info](class-Rigidbody.html)
See in [Glossary](Glossary.html#Rigidbody)** components to improve simulation results.
If a specific **Rigidbody** component in your **scene**A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](CreatingScenes.html)
See in [Glossary](Glossary.html#Scene) requires higher simulation accuracy or stability, such as preventing jittering in stacks or ensure **joint**A physics component allowing a dynamic connection between Rigidbody components, usually allowing some degree of movement such as a hinge. [More info](Joints.html)
See in [Glossary](Glossary.html#joint) stability, adjust its solver iteration count individually. Increasing solver iterations uses more CPU time for that specific **Rigidbody** component. This targeted approach is more efficient than increasing the global solver iteration count, which would affect all **Rigidbody** components.
To adjust the solver iterations for a specific **Rigidbody** component, use [`Rigidbody.solverIterations`](../ScriptReference/Rigidbody-solverIterations.html) on that specific component. This setting overrides the global project setting for that **Rigidbody** component only.
To configure the global setting for all **Rigidbody** components in your project:
1. Select **Edit > Project Settings** to open the Project Settings window.
2. Select the **Physics > Settings** tab.
3. Select the ****GameObject**The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](class-GameObject.html)
   See in [Glossary](Glossary.html#GameObject)** tab.
4. Adjust the **Default Solver Iterations** value.
## Additional resources
* [Unity Profiler](Profiler.html)
* [Managing time and frame rate](managing-time-and-frame-rate.html)
* [Memory Profiler](https://docs.unity3d.com/Packages/com.unity.memoryprofiler@latest)
* [Physics Project Settings](class-PhysicsManager.html)
* [`Rigidbody.solverIterations`](../ScriptReference/Rigidbody-solverIterations.html)