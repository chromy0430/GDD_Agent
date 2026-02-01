--- 
Source: Unity 6 Manual (physics-optimization-cpu-broad-phase.md)
---

# Select a broad phase pruning algorithm
Select the most efficient broad phase pruning algorithm.
In the Unity Editor, you can select these algorithms for broad phase **collision**A collision occurs when the physics engine detects that the colliders of two GameObjects make contact or overlap, when at least one has a Rigidbody component and is in motion. [More info](CollidersOverview.html)
See in [Glossary](Glossary.html#collision) detection:
* Sweep and Prune (SAP): Projects Axis-Aligned Bounding Boxes (AABBs) onto axes. While generally efficient, SAP can generate false positives in large, flat worlds with many **colliders**An invisible shape that is used to handle physical collisions for an object. A collider doesn’t need to be exactly the same shape as the object’s mesh - a rough approximation is often more efficient and indistinguishable in gameplay. [More info](CollidersOverview.html)
  See in [Glossary](Glossary.html#collider). In these scenarios, it can identify pairs of objects for narrow phase collision checking that aren’t actually close and projections can overlap even if the objects are distant.
* Multibox Pruning: This algorithm uses a grid, and each grid cell performs sweep-and-prune. This usually helps improve performance if, for example, there are many **GameObjects**The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](class-GameObject.html)
  See in [Glossary](Glossary.html#GameObject) in a flat world.
* Automatic Box Pruning: Divides the world into a grid and automatically configures the boundaries and cell sizes of the world based on your **scene**A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](CreatingScenes.html)
  See in [Glossary](Glossary.html#Scene)’s content. This can significantly reduce the number of pairs that need narrow phase checks in suitable environments. This algorithm is similar to Multibox Pruning, except that it can also automatically compute the world boundaries and number of subdivisions
SAP is the default broad phase algorithm for 3D physics. If you want to select the Automatic Box Pruning algorithm, there are several associated drawbacks you must consider:
* Overhead in highly dynamic scenes: If your scene contains many objects that are all constantly and rapidly moving across grid cell boundaries, the overhead of updating their positions within the grid might negate or even outweigh the pruning benefits. In highly dynamic scenarios, the Sweep and Prune broad phase might be more efficient.
* Automatic grid configuration: The automatically determined grid might not be optimal for every conceivable scene layout. While it aims for a good general-purpose configuration, specific or unusual world structures might not have as high performance benefits.
* Initial setup and reconfiguration: There’s an initial performance cost to build the grid. If your world’s physical bounds change drastically at runtime, the system might need to reconfigure the grid, potentially causing a temporary performance spike.
* Memory usage: The grid structure consumes some memory, though typically not a major concern.
Automatic Box Pruning generally performs well in large, open worlds, or scenes with many static or infrequently moving colliders. For smaller, dense scenes or scenes with extreme numbers of rapidly moving objects, **Sweep and Prune** might be a better choice. Always profile your specific scenes using the [**Unity Profiler**](Profiler.html), and focus on physics broad phase processing time, to determine which broad phase type yields the best performance for your game.
To change the broad phase type:
1. Select **Edit > Project Settings** to open the Project Settings window.
2. Select the **Physics > Settings** tab.
3. Select the **GameObject** tab.
4. In **Broad phase Type**, select a broad phase type algorithm.
## Additional resources
* [Unity Profiler](Profiler.html)
* [Managing time and frame rate](managing-time-and-frame-rate.html)
* [Memory Profiler](https://docs.unity3d.com/Packages/com.unity.memoryprofiler@latest)
* [Physics Project Settings](class-PhysicsManager.html)
* [Collision detection](collision-detection.html)An automatic process performed by Unity which determines whether a moving GameObject with a Rigidbody and collider component has come into contact with any other colliders. [More info](CollidersOverview.html)
  See in [Glossary](Glossary.html#collisiondetection)