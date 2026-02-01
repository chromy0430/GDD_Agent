--- 
Source: Unity 6 Manual (physics-optimization-cpu-collision-layers.md)
---

# Use the layer collision matrix to reduce overlaps
Reduce **collision**A collision occurs when the physics engine detects that the colliders of two GameObjects make contact or overlap, when at least one has a Rigidbody component and is in motion. [More info](CollidersOverview.html)
See in [Glossary](Glossary.html#collision) calculation overhead by configuring interaction rules between **GameObjects**The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](class-GameObject.html)
See in [Glossary](Glossary.html#GameObject) with collision layers.
Use the **Layer Collision Matrix** to control how objects on different layers interact with each other in the physics simulation. You can assign objects to a layer in their **Inspector**A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](UsingTheInspector.html)
See in [Glossary](Glossary.html#Inspector), and then use the **Layer Collision Matrix** to define the interaction rules between them. Defining how objects interact on a layer basis can reduce the number of overlap checks and collision calculations performed each frame.
The benefits of layer-based filtering are:
* Reduced broad phase workload: The physics system skips entire groups of objects when calculating potential collisions.
* Improved narrow phase efficiency: By ignoring irrelevant interactions, the simulation can focus computational resources on meaningful collisions.
* Better scalability: Helps maintain performance as the number of objects and complexity in your **scene**A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](CreatingScenes.html)
  See in [Glossary](Glossary.html#Scene) increases.
To begin optimizing with collision layers, first define and assign layers to your GameObjects. Then, configure how these layers interact in the **Layer Collision Matrix**. This matrix directly tells the physics system which layers must ignore each other during collision checks, which effectively culls potential interactions early in the simulation.
The recommended best practices for layer-based **collision detection**An automatic process performed by Unity which determines whether a moving GameObject with a Rigidbody and collider component has come into contact with any other colliders. [More info](CollidersOverview.html)
See in [Glossary](Glossary.html#collisiondetection) are:
* Enable interactions only between layers that are absolutely necessary for gameplay.
* Revisit the collision matrix periodically as your project grows. Disable unused layer pairs to increase performance.
* Use clear and consistent naming conventions for your layers to simplify debugging and future maintenance.
* Use the [Profiler](Profiler.html)A window that helps you to optimize your game. It shows how much time is spent in the various areas of your game. For example, it can report the percentage of time spent rendering, animating, or in your game logic. [More info](Profiler.html)
  See in [Glossary](Glossary.html#Profiler) to monitor the effect of your changes. In the [Physics Profiler module](ProfilerPhysics.html), observe counters related to broad phase pairs, narrow phase checks, and active contacts. Reducing unnecessary layer interactions leads to a decrease in these values, especially the broad phase work.
To learn more, refer to [Layer-based collision detection](LayerBasedCollision.html).
To define and assign layers to your GameObjects and configure the Layer Collision Matrix:
1. Select **Edit > Project Settings** to open the Project Settings window.
2. Select the **Tags and Layers** tab.
3. In the **Layers** section, define custom layers under the **User Layers** section. For example, you can create a “Player” “Environment”, or “Projectiles” layer.
4. In the Editor, assign a GameObject to a layer in the **Inspector** window. To learn more, refer to [Layers](Layers.html)Layers in Unity can be used to selectively opt groups of GameObjects in or out of certain processes or calculations. This includes camera rendering, lighting, physics collisions, or custom calculations in your own code. [More info](Layers.html)
   See in [Glossary](Glossary.html#layer).
5. Select \*\*Edit > Project Settings.
6. Select the **Physics > Settings** tab.
7. Select the **Shared** tab.
8. In the **Layer Collision Matrix**, uncheck any layer pairs that you do not want to interact. For example, you might not want projectiles to collide with other projectiles.
## Additional resources
* [Unity Profiler](Profiler.html)
* [Managing time and frame rate](managing-time-and-frame-rate.html)
* [Memory Profiler](https://docs.unity3d.com/Packages/com.unity.memoryprofiler@latest)
* [Physics Project Settings](class-PhysicsManager.html)
* [Layer-based collision detection](LayerBasedCollision.html)
* [Layers](Layers.html)