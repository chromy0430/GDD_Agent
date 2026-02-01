--- 
Source: Unity 6 Manual (DrawCallBatching-landing.md)
---

# Combine meshes using batching
Resources and approaches for improving performance by combining static **GameObjects**The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](class-GameObject.html)
See in [Glossary](Glossary.html#GameObject) or moving GameObjects into fewer draw calls.
| **Page** | **Description** |
| --- | --- |
| [Introduction to batching](DrawCallBatching.html) | Understand how Unity creates batches of static and dynamic GameObjects to reduce draw calls. |
| [Set up GameObjects for batching](DrawCallBatching-SetUp.html) | Get the best results from batching, and make sure Unity batches GameObjects. |
| [Batch static meshes at build time](DrawCallBatching-Enable.html) | Use **static batching**A technique Unity uses to draw GameObjects on the screen that combines static (non-moving) GameObjects into big Meshes, and renders them in a faster way. [More info](DrawCallBatching.html) See in [Glossary](Glossary.html#StaticBatching) to combine static meshes at build time. |
| [Batch meshes at runtime](static-batching-enable.html) | Batch static objects with the `StaticBatchingUtility` API, or dynamic GameObjects with **dynamic batching**An automatic Unity process which attempts to render multiple meshes as if they were a single mesh for optimized graphics performance. The technique transforms all of the GameObject vertices on the CPU and groups many similar vertices together. [More info](DrawCallBatching.html) See in [Glossary](Glossary.html#dynamicbatching). |
| [Combine meshes manually](combining-meshes.html) | Merge multiple meshes into a single **mesh**The main graphics primitive of Unity. Meshes make up a large part of your 3D worlds. Unity supports triangulated or Quadrangulated polygon meshes. Nurbs, Nurms, Subdiv surfaces must be converted to polygons. [More info](mesh.html) See in [Glossary](Glossary.html#Mesh) that Unity can render in a single draw call. |
| [Access properties in combined meshes](DrawCallBatching-Properties.html) | Use MaterialPropertyBlocks to change properties of combined meshes without breaking batching. |
## Additional resources
* [Choose a method for optimizing draw calls](optimizing-draw-calls-choose-method.html)
* [Reduce rendering work on the CPU or GPU](OptimizingGraphicsPerformance.html)