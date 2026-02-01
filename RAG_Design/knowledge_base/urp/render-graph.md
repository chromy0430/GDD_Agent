--- 
Source: Unity 6 URP Manual (render-graph.html)
---

# Render graph system in URP
The render graph system is a set of APIs you use to create a [Scriptable Render Pass](renderer-features/intro-to-scriptable-render-passes.html).
| Page | Description |
| --- | --- |
| [Introduction to the render graph system](render-graph-introduction.html) | What the render graph system is, and how it optimizes rendering. |
| [Write a render pass using the render graph system](render-graph-write-render-pass.html) | Write a Scriptable Render Pass using the render graph APIs. |
| [Blit using the render graph system](render-graph-blit.html) | **Blit**A shorthand term for “bit block transfer”. A blit operation is the process of transferring blocks of data from one place in memory to another. See in [Glossary](../Glossary.html#blit) from one texture to another in the render graph system with the `AddBlitPass` API. |
| [Textures in the render graph system](working-with-textures.html) | Access and use textures in your render passes. |
| [Frame data in the render graph system](render-graph-frame-data.html) | Get the textures URP creates for the current frame and use them in your render passes. |
| [Draw objects in the render graph system](render-graph-draw-objects-in-a-pass.html) | Draw objects in the render graph system using the `RendererList` API. |
| [Compute shaders in the render graph system](render-graph-compute-shader.html) | Create a render pass that runs a compute **shader**A program that runs on the GPU. [More info](../Shaders.html) See in [Glossary](../Glossary.html#shader). |
| [Analyze a render graph](render-graph-view.html) | Check a render graph using the Render Graph Viewer, Rendering Debugger, or Frame Debugger. |
| [Optimize a render graph](render-graph-optimize.html) | To optimize a render graph, merge or reduce the number of render passes. |
| [Use the CommandBuffer interface in a render graph](render-graph-unsafe-pass.html) | Use `CommandBuffer` interface APIs such as `SetRenderTarget` in render graph system render passes. |
| [Render Graph Viewer window reference](render-graph-viewer-reference.html) | Reference for the **Render Graph Viewer** window. |
## Additional resources
* [Inject a render pass using a Scriptable Renderer Feature](customize/inject-render-pass-via-script.html)
* [Frame Debugger](https://docs.unity3d.com/2023.3/Documentation/Manual/frame-debugger-window.html)