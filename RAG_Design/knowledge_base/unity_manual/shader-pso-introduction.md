--- 
Source: Unity 6 Manual (shader-pso-introduction.md)
---

# Introduction to PSO tracing and warming
Understand what PSO tracing and warming is, and the project requirements to use the `GraphicsStateCollection` API.
**Important**: `GraphicsStateCollection` is an experimental API and might be changed or removed in the future.
When Unity uses a **shader**A program that runs on the GPU. [More info](Shaders.html)
See in [Glossary](Glossary.html#shader) variant for the first time in your built application, the **scene**A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](CreatingScenes.html)
See in [Glossary](Glossary.html#Scene) might stutter. This is because Unity and the graphics driver need to compile the shader variant, and create a pipeline state object (PSO) with the compiled shader code and its related GPU state.
To reduce stuttering, compile shaders and create PSOs before they’re first needed, so that the graphics driver caches them to disk. This is called warming up, prewarming, or precooking graphics states.
## Project requirements
The [GraphicsStateCollection](../ScriptReference/Experimental.Rendering.GraphicsStateCollection.html) API is supported on Unity 6.0 or newer.
## Supported graphics APIs
You can use the `GraphicsStateCollection` API on the following graphics APIs:
* DirectX 12
* Vulkan
* Metal
* DirectX 11
* OpenGL
* OpenGLES
* WebGL
**Note**: On DirectX 11, OpenGL, OpenGLES, or **WebGL**A JavaScript API that renders 2D and 3D graphics in a web browser. The Unity Web build option allows Unity to publish content as JavaScript programs which use HTML5 technologies and the WebGL rendering API to run Unity content in a web browser. [More info](webgl.html)
See in [Glossary](Glossary.html#WebGL), the `GraphicsStateCollection` API automatically falls back to shader warm up as outlined in [Other methods to warm up shaders](shader-prewarm-other.html).
## Shader compatibility
The following shader types aren’t compatible with PSO tracing:
* Compute shaders
* **Ray tracing**The process of generating an image by tracing out rays from the Camera through each pixel and recording the color contribution at the hit point. This is an alternative to rasterization. raytracing
  See in [Glossary](Glossary.html#raytracing) shaders
## Additional resources
* [Graphics API support](GraphicsAPIs.html)
* [GraphicsStateCollection](../ScriptReference/Experimental.Rendering.GraphicsStateCollection.html) API documentation
* [Trace and manage PSO data collections](shader-pso-trace.html)
* [PSO tracing and warming example](shader-pso-example.html)