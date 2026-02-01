--- 
Source: Unity 6 Manual (optimizing-draw-calls-choose-method.md)
---

# Choose a method for optimizing draw calls
Use draw call optimization if the CPU sends too many draw calls to the GPU, which is also known as being CPU-bound. For more information about draw calls, refer to [Introduction to optimizing draw calls](optimizing-draw-calls.html).
## Check the number of draw calls
To check if your **scene**A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](CreatingScenes.html)
See in [Glossary](Glossary.html#Scene) sends too many draw calls, do any of the following:
* Open the [Rendering Statistics window](RenderingStatistics.html) and check the **SetPass calls** value.
* Open the [Profiler](Profiler.html)A window that helps you to optimize your game. It shows how much time is spent in the various areas of your game. For example, it can report the percentage of time spent rendering, animating, or in your game logic. [More info](Profiler.html)
  See in [Glossary](Glossary.html#Profiler) and select the **Rendering** section to display the number of draw calls.
* Check the number of draw calls in the [Frame Debugger](FrameDebugger-landing.html).
## Choose optimization methods
The supported and recommended methods for optimizing draw calls depend on whether you use the Universal **Render Pipeline**A series of operations that take the contents of a Scene, and displays them on a screen. Unity lets you choose from pre-built render pipelines, or write your own. [More info](render-pipelines.html)
See in [Glossary](Glossary.html#renderpipeline) (URP), the High Definition Render Pipeline (HDRP), or the Built-In Render Pipeline (BIRP).
| **Feature** | **Type** | **Multithreaded** | **Recommendation in URP** | **Recommendation in HDRP** | **Recommendation in the Built-In Render Pipeline** |
| --- | --- | --- | --- | --- | --- |
| **Scriptable Render Pipeline (SRP) Batcher** | Reduces render state updates | No. | Enable. Refer to [SRP Batcher in URP](SRPBatcher.html) | Enable. Refer to [SRP Batcher in HDRP](https://docs.unity3d.com/Packages/com.unity.render-pipelines.high-definition@17.3/manual/SRPBatcher-landing.html) | Not supported. |
| **GPU Resident Drawer** | Uses GPU instancing. | Yes. | Enable. Refer to [GPU Resident Drawer in URP](urp/gpu-resident-drawer.html) | Enable. Refer to [GPU Resident Drawer in HDRP](https://docs.unity3d.com/Packages/com.unity.render-pipelines.high-definition@17.3/manual/gpu-resident-drawer.html) | Not supported. |
| [**`BatchRendererGroup` (BRG) API**](batch-renderer-group.html) | Uses GPU instancing. | Yes. | Use the GPU Resident Drawer instead, except for advanced use cases. | Use the GPU Resident Drawer instead, except for advanced use cases. | Not supported. |
| **GPU Instancing** | Uses GPU instancing. | No. | Disable, to avoid extra **shader**A program that runs on the GPU. [More info](Shaders.html) See in [Glossary](Glossary.html#shader) variants. | Disable, to avoid extra shader variants. | Enable if you have many instances or lights. Refer to [GPU Instancing](GPUInstancing-landing.html). |
| **Batching** | Combines meshes | No. | Disable. **Static batching**A technique Unity uses to draw GameObjects on the screen that combines static (non-moving) GameObjects into big Meshes, and renders them in a faster way. [More info](DrawCallBatching.html) See in [Glossary](Glossary.html#StaticBatching) isn’t compatible with the BRG API or GPU Resident Drawer. | Disable. Static batching isn’t compatible with the BRG API or GPU Resident Drawer. | Enable static batching. **Dynamic batching**An automatic Unity process which attempts to render multiple meshes as if they were a single mesh for optimized graphics performance. The technique transforms all of the GameObject vertices on the CPU and groups many similar vertices together. [More info](DrawCallBatching.html) See in [Glossary](Glossary.html#dynamicbatching) is no longer recommended. Refer to [Batching](DrawCallBatching-landing.html). |
If you have many instances or lights, you can also use [optimize mesh rendering using level of detail (LOD)](lod-landing.html).
To get the best results from any draw call optimization method, do the following:
* Use the same materials for different **GameObjects**The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](class-GameObject.html)
  See in [Glossary](Glossary.html#GameObject) as much as possible.
* If you want to render the same **mesh**The main graphics primitive of Unity. Meshes make up a large part of your 3D worlds. Unity supports triangulated or Quadrangulated polygon meshes. Nurbs, Nurms, Subdiv surfaces must be converted to polygons. [More info](mesh.html)
  See in [Glossary](Glossary.html#Mesh) with different properties, for example different colors, use [Material Variants](materialvariant-landingpage.html) instead of multiple materials.
* Avoid using the `MaterialPropertyBlock` API in URP and HDRP.
## Use multiple optimization methods
You can use multiple draw call optimization methods in the same scene, but each GameObject uses only one of the following methods, in this priority order:
1. SRP Batcher, and static batching if you enable it.
2. GPU instancing, including the GPU Resident Drawer or the `BatchRendererGroup` API.
3. Dynamic batching.
## Additional resources
* [Shader variants](shader-variants.html)A verion of a shader program that Unity generates according to a specific combination of shader keywords and their status. A Shader object can contain multiple shader variants. [More info](shader-variants.html)
  See in [Glossary](Glossary.html#shadervariant)
* [Fantasy Kingdom in Unity 6](https://unity.com/demos/fantasy-kingdom), which uses the GPU Resident Drawer.
* [SRP Batcher: Speed up your rendering](https://unity.com/blog/engine-platform/srp-batcher-speed-up-your-rendering)
* [BatchRendererGroup sample: Achieve high frame rate even on budget devices](https://unity.com/blog/engine-platform/batchrenderergroup-sample-high-frame-rate-on-budget-devices)
* [Megacity Metro](https://unity.com/demos/megacity-competitive-action-sample), which uses the BatchRendererGroup API to render a large number of objects.