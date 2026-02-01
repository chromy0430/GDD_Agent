--- 
Source: Unity 6 URP Manual (reduce-rendering-work-on-cpu.html)
---

# GPU Resident Drawer
To speed up rendering, enable the GPU Resident Drawer so Unity automatically uses the `BatchRendererGroup` API to reduce the number of draw calls.
| **Page** | **Description** |
| --- | --- |
| [Enable the GPU Resident Drawer](gpu-resident-drawer.html) | Automatically use the `BatchRendererGroup` API to use instancing and reduce the number of draw calls. |
| [Make a GameObject compatible with the GPU Resident Drawer](make-object-compatible-gpu-rendering.html) | Include or exclude a **GameObject**The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](../class-GameObject.html) See in [Glossary](../Glossary.html#GameObject) from the GPU Resident Drawer. |
## Additional resources
* [Choose a method for optimizing draw calls](../optimizing-draw-calls-choose-method.html)
* [GPU occlusion culling](gpu-culling.html)
* [Graphics performance fundamentals](https://docs.unity3d.com/Manual/OptimizingGraphicsPerformance.html)