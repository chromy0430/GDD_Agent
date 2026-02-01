--- 
Source: Unity 6 Manual (physics-optimization-cpu-static-colliders.md)
---

# Move static colliders to prevent performance issues
Properly manage static **colliders**An invisible shape that is used to handle physical collisions for an object. A collider doesn’t need to be exactly the same shape as the object’s mesh - a rough approximation is often more efficient and indistinguishable in gameplay. [More info](CollidersOverview.html)
See in [Glossary](Glossary.html#collider) when they move to avoid performance issues.
A [Static collider](collider-types-introduction.html#static-colliders) is a **GameObject**The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](class-GameObject.html)
See in [Glossary](Glossary.html#GameObject) with a Collider component but no **Rigidbody**A component that allows a GameObject to be affected by simulated gravity and other forces. [More info](class-Rigidbody.html)
See in [Glossary](Glossary.html#Rigidbody) or ArticulationBody component attached. You can use static colliders for objects that don’t move during gameplay, such as **terrain**The landscape in your scene. A Terrain GameObject adds a large flat plane to your scene and you can use the Terrain’s Inspector window to create a detailed landscape. [More info](terrain-UsingTerrains.html)
See in [Glossary](Glossary.html#Terrain), buildings, or other environmental features.
When you move a static collider by changing its transform values, the physics system detects the change and updates its internal spatial structures during the next physics step or when [`Physics.SyncTransforms`](../ScriptReference/Physics.SyncTransforms.html) is called. If you want to make frequent changes to the transform values of a static collider between physics simulations steps when you execute gameplay code, use a Kinematic Rigidbody component instead.
If you want to move a static collider, the recommended best practice is that you don’t add a Rigidbody component to a static object solely to move that GameObject. If it doesn’t need a physics simulation, you’re adding an unnecessary performance burden.
## Additional resources
* [Unity Profiler](Profiler.html)
* [Managing time and frame rate](managing-time-and-frame-rate.html)
* [Memory Profiler](https://docs.unity3d.com/Packages/com.unity.memoryprofiler@latest)
* [Physics Project Settings](class-PhysicsManager.html)
* [Introduction to collider types](collider-types-introduction.html)