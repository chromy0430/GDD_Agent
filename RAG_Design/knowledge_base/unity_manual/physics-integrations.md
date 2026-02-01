--- 
Source: Unity 6 Manual (physics-integrations.md)
---

# Physics integrations in Unity
Unity helps you simulate physics in your Project to ensure that the objects correctly accelerate and respond to **collisions**A collision occurs when the physics engine detects that the colliders of two GameObjects make contact or overlap, when at least one has a Rigidbody component and is in motion. [More info](CollidersOverview.html)
See in [Glossary](Glossary.html#collision), gravity, and various other forces. Unity provides different physics system implementations which you can use according to your project needs: 3D, 2D, object-oriented, or data-oriented.
You can create some basic physics interactions with the user interface, but for more control over the simulation, you need some familiarity with C#. To develop your C# skills, refer to the Unity Learn [Junior Programmer](https://learn.unity.com/pathway/junior-programmer) course.
## Built-in physics systems for object-oriented projects
If your project is [object-oriented](object-oriented-development.html), use the Unity’s built-in physics system that corresponds to your needs:
* [Built-in 3D physics](PhysicsOverview.html): Uses an integration of the Nvidia PhysX engine by default.
* [Built-in 2D physics](2d-physics/2d-physics.html): Uses an integration of Box2D **physics engine**A system that simulates aspects of physical systems so that objects can accelerate correctly and be affected by collisions, gravity and other forces. [More info](PhysicsSection.html)
  See in [Glossary](Glossary.html#physicsengine) by default.
## Physics engine packages for data-oriented projects
If your project uses Unity’s Data-Oriented Technology Stack (DOTS), you need to install the [Unity Physics](http://docs.unity3d.com/Packages/com.unity.physics@latest/index.html) package. Unity Physics is the DOTS physics engine that simulates physics in a data-oriented project.
## Additional resources
* [Physics](PhysicsSection.html)
* [Physics project settings](class-PhysicsManager.html)
* [2D physics](2d-physics/2d-physics.html)
* [Built-in 3D physics](PhysicsOverview.html)
* [Unity Physics package](http://docs.unity3d.com/Packages/com.unity.physics@latest/index.html)
* [Havok Physics for Unity package](https://docs.unity3d.com/Packages/com.havok.physics@latest/index.html)