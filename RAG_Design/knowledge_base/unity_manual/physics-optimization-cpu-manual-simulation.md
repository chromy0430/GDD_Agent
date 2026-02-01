--- 
Source: Unity 6 Manual (physics-optimization-cpu-manual-simulation.md)
---

# Manually set physics simulation
Control the physics simulation manually to decide when physics calculations occur to align physics updates with your application’s actual performance and avoid redundant updates. This can help optimize performance during busy frames and is beneficial for scenarios that require tight synchronization with game logic or custom physics update loops.
Manually control the physics simulation to:
* Ensure stability and consistency: Physics systems are designed for small, consistent time steps. Variable time step values, such as [`Time.deltaTime`](../ScriptReference/Time-deltaTime.html), can cause unstable simulations, and lead to issues such as objects passing through each other, a phenomenon known as tunneling, at low frame rates or jittery behavior when frame rates fluctuate.
* Create reproducible behavior: Using a fixed step is crucial for more reproducible physics behavior (though true determinism with PhysX has other challenges).
* Avoid large, inaccurate steps: If frame rates drop, [`Time.deltaTime`](../ScriptReference/Time-deltaTime.html) increases. Simulating a physics step with a large, variable delta can be computationally resource intensive and less accurate, potentially worsening performance issues.
Use `Physics.Simulate(float stepTime)` (or `yourPhysicsScene.Simulate(float stepTime)`) to manually control the physics simulation and in specific, local `PhysicsScene` instances. Refer to the [Multi-Scene Physics learn tutorial](https://learn.unity.com/tutorial/multi-scene-physics) to learn more about multi-scene physics.
When you call [`Physics.Simulate`](../ScriptReference/Physics.Simulate.html), the recommended best practice is to use a fixed time step, rather than directly passing `Time.deltaTime`. For example, use the same value that you might use in the ****Project Settings**A broad collection of settings which allow you to configure how Physics, Audio, Networking, Graphics, Input and many other areas of your project behave. [More info](comp-ManagerGroup.html)
See in [Glossary](Glossary.html#ProjectSettings)**’ ****Fixed Timestep**A customizable frame-rate-independent interval that dictates when physics calculations and FixedUpdate() events are performed. [More info](class-TimeManager.html)
See in [Glossary](Glossary.html#fixedtimestep)** value, such as **0.02** for 50Hz.
If you manually simulate physics in a **scene**A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](CreatingScenes.html)
See in [Glossary](Glossary.html#Scene) using `Physics.Simulate()`, ensure that automatic simulation is disabled. You can do this by setting the **Simulation Mode** to **Script**. Once in **Script** mode (either through **Project Settings** or script), you must call `Physics.Simulate` for the scene at a selected frequency with an appropriate, preferably fixed, time step.
To disable automatic simulation, in the Editor:
1. Select **Edit > Project Settings** to open the Project Settings window.
2. Select the **Physics > Settings** tab.
3. Select the ****GameObject**The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](class-GameObject.html)
   See in [Glossary](Glossary.html#GameObject)** tab.
4. Set **Simulation Mode** to **Script**.
To disable automatic simulation, in script, set `Physics.simulationMode = SimulationMode.Script;`. Typically, you do this at the start of your game, before any physics simulation occurs.
## Additional resources
* [Unity Profiler](Profiler.html)
* [Managing time and frame rate](managing-time-and-frame-rate.html)
* [Memory Profiler](https://docs.unity3d.com/Packages/com.unity.memoryprofiler@latest)
* [Physics Project Settings](class-PhysicsManager.html)
* [Time](class-TimeManager.html)
* [Optimize physics for query-only or non-simulating games](physics-optimization-cpu-query-only.html)
* [Physics.Simulate](../ScriptReference/Physics.Simulate.html)
* [Multi-Scene Physics learn tutorial](https://learn.unity.com/tutorial/multi-scene-physics)