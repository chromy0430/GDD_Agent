--- 
Source: Unity 6 Manual (reduce-draw-calls-landing.md)
---

# Optimize rendering lots of objects
Speed up rendering lots of similar objects by optimizing draw calls, which reduces how often the CPU sends information to the GPU.
| **Page** | **Description** |
| --- | --- |
| [Introduction to optimizing draw calls](optimizing-draw-calls.html) | Understand why reducing draw calls improves rendering time. |
| [Choose a method for optimizing draw calls](optimizing-draw-calls-choose-method.html) | Compare the different methods for optimizing draw calls. |
| [GPU instancing](GPUInstancing-landing.html) | Resources and techniques for rendering multiple copies of the same **mesh**The main graphics primitive of Unity. Meshes make up a large part of your 3D worlds. Unity supports triangulated or Quadrangulated polygon meshes. Nurbs, Nurms, Subdiv surfaces must be converted to polygons. [More info](mesh.html) See in [Glossary](Glossary.html#Mesh) at the same time. |
| [Batching meshes](DrawCallBatching-landing.html) | Combine meshes to reduce draw calls, for either static or moving **GameObjects**The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](class-GameObject.html) See in [Glossary](Glossary.html#GameObject). |
## Additional resources
* [Optimizing draw calls in URP](reduce-draw-calls-landing-urp.html)
* [Introduction to Mesh LOD](lod/mesh-lod-introduction.html)