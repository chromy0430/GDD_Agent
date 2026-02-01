--- 
Source: Unity 6 URP Manual (render-graph-introduction.html)
---

# Introduction to the render graph system in URP
The render graph system is a set of APIs from the [Core Scriptable Render Pipeline (SRP) package](https://docs.unity3d.com/Packages/com.unity.render-pipelines.core@latest). You use the APIs to write a [Scriptable Render Pass](renderer-features/intro-to-scriptable-render-passes.html) in the Universal **Render Pipeline**A series of operations that take the contents of a Scene, and displays them on a screen. Unity lets you choose from pre-built render pipelines, or write your own. [More info](../render-pipelines.html)
See in [Glossary](../Glossary.html#renderpipeline) (URP).
When you use the render graph API to create a Scriptable Render Pass, you tell URP the following:
1. The textures or **render textures**A special type of Texture that is created and updated at runtime. To use them, first create a new Render Texture and designate one of your Cameras to render into it. Then you can use the Render Texture in a Material just like a regular Texture. [More info](../class-RenderTexture.html)
   See in [Glossary](../Glossary.html#RenderTexture) to use. This stage is the recording stage.
2. The graphics commands to execute, using the textures or render textures from the recording stage. This stage is the execution stage.
You can then [inject your Scriptable Render Pass into the URP renderer](renderer-features/custom-rendering-pass-workflow-in-urp.html). Your Scriptable Render Pass becomes part of URP’s internal render graph, which is the sequence of render passes URP steps through each frame.
The render graph system automatically optimizes the graph to minimize the number of render passes, and the memory and bandwidth the render passes use.
## How the render graph system optimizes rendering
The render graph system does the following to optimize rendering:
* Avoids allocating resources the frame doesn’t use.
* Removes render passes if the final frame doesn’t use their output.
* Optimizes GPU memory, for example by reusing allocated memory if a texture has the same properties as an earlier texture.
* Automatically synchronizes the compute and graphics GPU command queues, if compute **shaders**A program that runs on the GPU. [More info](../Shaders.html)
  See in [Glossary](../Glossary.html#shader) are used.
On mobile platforms that use tile-based deferred rendering (TBDR), the render graph system can also merge multiple render passes into a single native render pass. A native render pass keeps textures in tile memory, rather than copying textures from the GPU to the CPU. As a result, URP uses less memory bandwidth and rendering time.
To check how the render graph system optimizes rendering in your custom render passes, refer to [Analyze a render graph](render-graph-view.html).
## Resources in the render graph system
To declare a resource and use it in a render pass, for example a texture or a list of objects to render, call render graph system APIs that return a handle to the resource. You can’t directly allocate or dispose of resources yourself.
The render graph system only allocates the memory for a resource just before the first render pass that writes to it, and releases the memory after the last render pass that reads it. This lets render graph manage memory in the most efficient way possible, and avoid allocating memory for resources that aren’t used in a frame.
You can create resources in two ways:
* Create a resource inside a render pass. These are called internal resources. The render graph system handles the lifetime of these resources. You can’t access them outside of the render graph instance, or pass them between frames or **cameras**A component which creates an image of a particular viewpoint in your scene. The output is either drawn to the screen or captured as a texture. [More info](../CamerasOverview.html)
  See in [Glossary](../Glossary.html#Camera). For more information, refer to [Create a temporary texture for a single frame](render-graph-create-a-texture.html).
* Import an existing resource from outside a render pass, for example the camera back buffer, or textures you want a render graph to use across multiple frames. These are called imported or external resources. Render graph doesn’t handle the lifetime of these resources, so you pass them between frames and cameras. For more information, refer to [Use a texture in multiple render passes](render-graph-pass-textures-between-passes.html).
## Additional resources
* [Use frame data](accessing-frame-data.html)
* [Inject a render pass via scripting](customize/inject-render-pass-via-script.html)
* [Inject a render pass using a Scriptable Renderer Feature](renderer-features/scriptable-renderer-features/inject-a-pass-using-a-scriptable-renderer-feature.html)
* [RenderGraph API documentation](../api/UnityEngine.Rendering.RenderGraphModule.RenderGraph.html)
* [Package samples reference](package-sample-urp-package-samples.html)