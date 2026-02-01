--- 
Source: Unity 6 Manual (writing-shader-tags.md)
---

# Configure when Unity uses a shader
Resources for using `#pragma` and `Tag` blocks in **ShaderLab**Unity’s language for defining the structure of Shader objects. [More info](SL-Shader.html)
See in [Glossary](Glossary.html#ShaderLab) to configure when Unity compiles and runs a **shader**A program that runs on the GPU. [More info](Shaders.html)
See in [Glossary](Glossary.html#shader).
| **Page** | **Description** |
| --- | --- |
| [Set the rendering pipeline and render pass for a shader](writing-shader-tags-introduction.html) | Use a `Tag` statement to set the **render pipeline**A series of operations that take the contents of a Scene, and displays them on a screen. Unity lets you choose from pre-built render pipelines, or write your own. [More info](render-pipelines.html) See in [Glossary](Glossary.html#renderpipeline) and render order for a shader. |
| [Set a shader to require a package](writing-shader-tags-require-package.html) | Use a `PackageRequirements` block to add package requirements to a subshader or a pass. |
| [Set a shader to require a shader model or GPU feature](SL-ShaderCompileTargets.html) | Use a `#pragma target` or `#pragma require` statement to set the minimum shader model or GPU feature for a shader. |
| [Set the graphics API or platform for a shader](SL-ShaderCompilationAPIs.html) | Use a `#pragma only_renderers` or `#pragma exclude_renderers` statement to set the graphics API or platform for a shader. |
## Additional resources
* [Replace shaders at runtime in the Built-In Render Pipeline](SL-ShaderReplacement.html)