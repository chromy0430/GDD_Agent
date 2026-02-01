--- 
Source: Unity 6 Manual (physics-optimization-collision-callbacks.md)
---

# Optimize collision callbacks
Reduce garbage collector (GC) load and improve performance by optimizing physics **collision**A collision occurs when the physics engine detects that the colliders of two GameObjects make contact or overlap, when at least one has a Rigidbody component and is in motion. [More info](CollidersOverview.html)
See in [Glossary](Glossary.html#collision) callback allocations.
Unity provides physics collision callback messages like:
* [`OnCollisionEnter`](../ScriptReference/Collider.OnCollisionEnter.html)
* [`OnCollisionStay`](../ScriptReference/Collider.OnCollisionStay.html)
* [`OnCollisionExit`](../ScriptReference/Collider.OnCollisionExit.html)
By default, each time these callbacks are invoked, Unity allocates new `Collision` (or `Collider` for triggers) data objects in memory to hold information about the collision. These frequent small allocations can increase the load on the garbage collector.
To reduce the number of allocations from these callbacks, you can enable the **Reuse Collision Callbacks** setting, to make Unity reuse a smaller pool of `Collision` data instances. This reduces memory overhead and improves performance, especially in scenarios with many collision events per frame. Note that if you reuse collision callbacks, the `Collision` data passed to the callbacks is then only valid during that specific callback.
To learn more about garbage collection, refer to [Garbage collector overview](performance-garbage-collector.html).
By default, **Reuse Collision Callbacks** is enabled in the **Project Settings**A broad collection of settings which allow you to configure how Physics, Audio, Networking, Graphics, Input and many other areas of your project behave. [More info](comp-ManagerGroup.html)
See in [Glossary](Glossary.html#ProjectSettings). To make sure that you are reusing collision callbacks and reducing GC allocations from these callbacks in the Editor:
1. Go to **Edit > Project Settings** to open the Project Settings window.
2. Select the **Physics > Settings** tab.
3. Select the ****GameObject**The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](class-GameObject.html)
   See in [Glossary](Glossary.html#GameObject)** tab.
4. Make sure that **Reuse Collision Callbacks** is enabled.
To reduce GC allocations from these callbacks in script, set `Physics.reuseCollisionCallbacks = true`.
## Additional resources
* [Unity Profiler](Profiler.html)
* [Managing time and frame rate](managing-time-and-frame-rate.html)
* [Memory Profiler](https://docs.unity3d.com/Packages/com.unity.memoryprofiler@latest)
* [Physics Project Settings](class-PhysicsManager.html)
* [Garbage collector overview](performance-garbage-collector.html)