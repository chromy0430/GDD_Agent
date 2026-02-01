--- 
Source: Unity 6 Manual (RenderingPaths.md)
---

# Introduction to rendering paths in the Built-In Render Pipeline
Unity’s Built-In **Render Pipeline**A series of operations that take the contents of a Scene, and displays them on a screen. Unity lets you choose from pre-built render pipelines, or write your own. [More info](render-pipelines.html)
See in [Glossary](Glossary.html#renderpipeline) supports different rendering paths. A **rendering path** is a series of operations related to lighting and shading. Different rendering paths have different capabilities and performance characteristics. Deciding on which rendering path is most suitable for your Project depends on the type of Project, and on the target hardware.
You can choose the rendering path that your Project uses in the [Graphics](class-GraphicsSettings.html) window, and you can override that path for each [Camera](class-Camera.html)A component which creates an image of a particular viewpoint in your scene. The output is either drawn to the screen or captured as a texture. [More info](CamerasOverview.html)
See in [Glossary](Glossary.html#Camera).
If the GPU on the device running your Project does not support the rendering path that you have selected, Unity automatically uses a lower fidelity rendering path. For example, on a GPU that does not handle **Deferred Shading**A rendering path in the Built-in Render Pipeline that places no limit on the number of Lights that can affect a GameObject. All Lights are evaluated per-pixel, which means that they all interact correctly with normal maps and so on. Additionally, all Lights can have cookies and shadows. [More info](RenderTech-DeferredShading.html)
See in [Glossary](Glossary.html#deferredshading), Unity uses **Forward Rendering**A rendering path that renders each object in one or more passes, depending on lights that affect the object. Lights themselves are also treated differently by Forward Rendering, depending on their settings and intensity. [More info](RenderTech-ForwardRendering.html)
See in [Glossary](Glossary.html#ForwardRendering).
* [Forward](RenderTech-ForwardRendering.html) is the default rendering path in the Built-in Render Pipeline. It is a general-purpose rendering path.
* [Deferred](RenderTech-DeferredShading.html) is the rendering path with the most lighting and shadow fidelity in the Built-in Render Pipeline.
* [Legacy Vertex Lit](RenderTech-VertexLit.html) is the rendering path with the lowest lighting fidelity and no support for real-time shadows. It is a subset of the Forward rendering path.
## Rendering Path comparison
|  | ***Deferred*** | ***Forward*** | ***Vertex Lit*** |
| --- | --- | --- | --- |
| **Features** |  |  |  |
| Per-pixel lighting (normal maps, light cookies) | Yes | Yes | - |
| Real-time shadows | Yes | With caveats | - |
| **Reflection Probes**A rendering component that captures a spherical view of its surroundings in all directions, rather like a camera. The captured image is then stored as a Cubemap that can be used by objects with reflective materials. [More info](class-ReflectionProbe.html) See in [Glossary](Glossary.html#ReflectionProbe) | Yes | Yes | - |
| Depth & Normal Buffers | Yes | Additional render passes | - |
| Soft **Particles**A small, simple image or mesh that is emitted by a particle system. A particle system can display and move particles in great numbers to represent a fluid or amorphous entity. The effect of all the particles together creates the impression of the complete entity, such as smoke. [More info](class-ParticleSystem.html) See in [Glossary](Glossary.html#particle) | Yes | - | - |
| Semi-transparent objects | - | Yes | Yes |
| Anti-Aliasing | - | Yes | Yes |
| Light **Culling Masks**Allows you to include or omit objects to be rendered by a Camera, by Layer. See in [Glossary](Glossary.html#CullingMask) | Limited | Yes | Yes |
| Lighting Fidelity | All per-pixel | Some per-pixel | All per-vertex |
| **Performance** |  |  |  |
| Cost of a per-pixel Light | Number of **pixels**The smallest unit in a computer image. Pixel size depends on your screen resolution. Pixel lighting is calculated at every screen pixel. [More info](ShadowPerformance.html) See in [Glossary](Glossary.html#pixel) it illuminates | Number of pixels \* Number of objects it illuminates | - |
| Number of times objects are normally rendered | 1 | Number of per-pixel lights | 1 |
| Overhead for simple **Scenes**A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](CreatingScenes.html) See in [Glossary](Glossary.html#Scene) | High | None | None |
| **Platform Support** |  |  |  |
| PC (Windows/Mac) | **Shader**A program that runs on the GPU. [More info](Shaders.html) See in [Glossary](Glossary.html#shader) Model 3.0+ & MRT | All | All |
| Mobile (iOS/Android) | OpenGL ES 3.0 & MRT, Metal | All | All |
| Consoles | XB1, PS4 | All | - |