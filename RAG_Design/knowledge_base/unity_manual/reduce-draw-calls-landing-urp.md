--- 
Source: Unity 6 Manual (reduce-draw-calls-landing-urp.md)
---

# Optimizing draw calls in URP
Techniques for speeding up rendering by reducing the number of drawing commands the CPU sends to the GPU, in the Universal **Render Pipeline**A series of operations that take the contents of a Scene, and displays them on a screen. Unity lets you choose from pre-built render pipelines, or write your own. [More info](render-pipelines.html)
See in [Glossary](Glossary.html#renderpipeline) (URP).
For more information about techniques for optimizing draw calls, refer to [choose a method for optimizing draw calls](optimizing-draw-calls-choose-method.html).
| **Page** | **Description** |
| --- | --- |
| [Scriptable Render Pipeline Batcher](SRPBatcher-landing.html) | Resources for using the Scriptable Render Pipeline (SRP) Batcher to reduce the number of render state changes between draw calls. |
| [GPU Resident Drawer](urp/reduce-rendering-work-on-cpu.html) | Automatically use the `BatchRendererGroup` API to use instancing and reduce the number of draw calls. |
| [BatchRendererGroup API](batch-renderer-group.html) | Resources for using the `BatchRendererGroup` API to reduce the number of batches in the SRP Batcher. |
## Additional resources
* [Reduce rendering work on the CPU](urp/reduce-rendering-work-on-cpu.html)
* [Optimize rendering lots of objects](reduce-draw-calls-landing.html)
* [Graphics rendering: Getting the best performance with Unity 6](https://www.youtube.com/watch?v=Oc6T4hh5gaI)
* [Performance tips and tricks from a Unity consultant](https://www.youtube.com/watch?v=CmD8MVGkDxQ)