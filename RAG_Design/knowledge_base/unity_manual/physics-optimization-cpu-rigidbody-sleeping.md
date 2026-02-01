--- 
Source: Unity 6 Manual (physics-optimization-cpu-rigidbody-sleeping.md)
---

# Use Rigidbody sleeping to improve physics performance
Reduce CPU load and improve physics performance by enabling **Rigidbody**A component that allows a GameObject to be affected by simulated gravity and other forces. [More info](class-Rigidbody.html)
See in [Glossary](Glossary.html#Rigidbody) sleeping for stationary objects.
Rigidbody sleeping can drastically reduce CPU load, especially in **scenes**A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](CreatingScenes.html)
See in [Glossary](Glossary.html#Scene) with many physical objects that are often stationary or frequently come to rest. When a **Rigidbody** component moves at a slower speed than the **[Sleep Threshold](class-PhysicsManager.html)**, the physics system sets the **Rigidbody** component to a sleeping state. When a **Rigidbody** component is asleep, the physics system doesn’t include it in physics calculations. When a sleeping **Rigidbody** component receives a **collision**A collision occurs when the physics engine detects that the colliders of two GameObjects make contact or overlap, when at least one has a Rigidbody component and is in motion. [More info](CollidersOverview.html)
See in [Glossary](Glossary.html#collision) or force, the physics system wakes up the Rigidbody component and includes it in physics calculations.
In script, control Rigidbody sleeping with [`Rigidbody.Sleep`](../ScriptReference/Rigidbody.Sleep.html) and [`Rigidbody.WakeUp`](../ScriptReference/Rigidbody.WakeUp.html)
Rigidbody sleeping is highly effective in environments with many interactive props, destructible elements that settle, or physics-based puzzles that stabilize. While scenes with constant high-velocity motion benefit less, enabling sleeping is generally a good default behavior.
To enable Rigidbody sleeping, the recommended best practices are:
* Ensure that the **Rigidbody** component’s sleep threshold is set appropriately. Set the **Sleep Threshold** in the [Physics Project Settings](class-PhysicsManager.html) and in script with [`Rigidbody.sleepThreshold`](../ScriptReference/Rigidbody-sleepThreshold.html).
* Avoid calling `Rigidbody.WakeUp` unnecessarily on objects unless they need to be active in the simulation. Continuously waking objects negates the benefit of sleeping.
* Check if a **Rigidbody** component is sleeping with [`Rigidbody.IsSleeping`](../ScriptReference/Rigidbody.IsSleeping.html).
* Use the Physics Debugger (**Window > Analysis > Physics Debugger**) to visually inspect the sleep state of **Rigidbody** components in your scene. The Physics Debugger can help identify objects that are unexpectedly active and not sleeping, potentially due to persistent small contacts or incorrect sleep settings.
## Additional resources
* [Unity Profiler](Profiler.html)
* [Managing time and frame rate](managing-time-and-frame-rate.html)
* [Memory Profiler](https://docs.unity3d.com/Packages/com.unity.memoryprofiler@latest)
* [Physics Project Settings](class-PhysicsManager.html)
* [`Rigidbody.Sleep`](../ScriptReference/Rigidbody.Sleep.html)