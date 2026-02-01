--- 
Source: Unity 6 Manual (PhysicsOverview.md)
---

# Built-in 3D physics
Unity’s default built-in 3D physics system is an integration of the Nvidia PhysX engine. You can use this system in object-oriented 3D projects.
This section includes the following topics.
| **Topic** | **Description** |
| --- | --- |
| **[Character control](character-control-section.html)** | Configure physics-based character control for first-person and third-person characters. |
| **[Rigidbody physics](rigidbody-physics-section.html)** | Apply physics-based behavior to **GameObjects**The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](class-GameObject.html) See in [Glossary](Glossary.html#GameObject). |
| **[Collision](collision-section.html)A collision occurs when the physics engine detects that the colliders of two GameObjects make contact or overlap, when at least one has a Rigidbody component and is in motion. [More info](CollidersOverview.html) See in [Glossary](Glossary.html#collision)** | Use **colliders**An invisible shape that is used to handle physical collisions for an object. A collider doesn’t need to be exactly the same shape as the object’s mesh - a rough approximation is often more efficient and indistinguishable in gameplay. [More info](CollidersOverview.html) See in [Glossary](Glossary.html#collider) to configure collisions between GameObjects. |
| **[Joints](joints-section.html)A physics component allowing a dynamic connection between Rigidbody components, usually allowing some degree of movement such as a hinge. [More info](Joints.html) See in [Glossary](Glossary.html#joint)** | Apply and configure joints that connect GameObjects and simulate physical forces for pivoting, movement, and restriction. |
| **[Articulations](articulations-section.html)** | Configure complex systems of rigid bodies and joints. |
| **[Ragdoll physics](ragdoll-physics-section.html)** | Configure ragdoll physics for characters. |
| **[Optimize physics performance](physics-optimization.html)** | Optimize physics system performance in the Unity Editor. |
| **[Cloth](class-Cloth.html)A component that works with the Skinned Mesh Renderer to provide a physics-based solution for simulating fabrics. [More info](class-Cloth.html) See in [Glossary](Glossary.html#Cloth)** | Simulate fabric movement for character clothing and other in-application textiles. |
| **[Multi-scene physics](physics-multi-scene.html)** | Manage different physics contexts in one project with multiple dedicated physics **scenes**A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](CreatingScenes.html) See in [Glossary](Glossary.html#Scene). |
| **[Physics Debug window reference](PhysicsDebugVisualization.html)** | Use the Physics Debug window to configure and generate visual representations of 3D physics activity in a scene. |
| **[Physics Profiler module](ProfilerPhysics.html)** | Analyze the performance of physics in your application. |
## Additional resources
* [World building](CreatingEnvironments.html)
* [2D Physics](2d-physics/2d-physics.html)
* [Managing time and frame rate](managing-time-and-frame-rate.html)