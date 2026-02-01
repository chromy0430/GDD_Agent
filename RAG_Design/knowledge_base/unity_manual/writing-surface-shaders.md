--- 
Source: Unity 6 Manual (writing-surface-shaders.md)
---

# Writing Surface Shaders
Resources and techniques for writing Surface **Shaders**A program that runs on the GPU. [More info](Shaders.html)
See in [Glossary](Glossary.html#shader) in the Built-In **Render Pipeline**A series of operations that take the contents of a Scene, and displays them on a screen. Unity lets you choose from pre-built render pipelines, or write your own. [More info](render-pipelines.html)
See in [Glossary](Glossary.html#renderpipeline), which are streamlined shaders that interact with lighting.
| **Page** | **Description** |
| --- | --- |
| [Introduction to Surface Shaders](SL-SurfaceShaders.html) | Learn about how **Surface Shaders**A streamlined way of writing shaders for the Built-in Render Pipeline. [More info](SL-SurfaceShaders.html) See in [Glossary](Glossary.html#SurfaceShader) let you write shaders in a streamlined way. |
| [Surface Shader output structures](SL-SurfaceShaders-output.html) | Understand the structures Surface Shaders uses for input data, for example albedo color and surface normals. |
| [Surface Shaders and rendering paths](SL-RenderPipeline.html) | Understand how the **rendering path**The technique that a render pipeline uses to render graphics. Choosing a different rendering path affects how lighting and shading are calculated. Some rendering paths are more suited to different platforms and hardware than others. [More info](RenderingPaths.html) See in [Glossary](Glossary.html#renderingpath) affects how Unity applies lighting, and which passes Unity uses. |
| [Create a Surface Shader](SL-SurfaceShader-create.html) | Create a Surface Shader using the `#pragma surface` directive. |
| [Set the lighting model in a Surface Shader](SL-SurfaceShaderLighting.html) | Set the lighting to a built-in model, or define a custom lighting model. |
| [Optimize Surface Shaders](SL-SurfaceShaderOptimize.html) | Make Surface Shaders run faster or reduce their file size. |
| [Surface Shader examples](SL-SurfaceShaderExamples.html) | Examples of Surface Shaders in the Built-In Render Pipeline. |
| [Surface Shader language reference](surface-shaders-language-reference.html) | Find the directives and input structures you need to write a Surface Shader in the Built-In Render Pipeline. |
## Additional resources
* [Writing custom shaders in URP](urp/writing-custom-shaders-urp.html)