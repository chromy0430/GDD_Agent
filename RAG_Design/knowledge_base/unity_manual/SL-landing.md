--- 
Source: Unity 6 Manual (SL-landing.md)
---

# Writing a custom shader in ShaderLab and HLSL
Resources and techniques for writing **Shader**A program that runs on the GPU. [More info](Shaders.html)
See in [Glossary](Glossary.html#shader) objects, subshaders and shader passes in **ShaderLab**Unity’s language for defining the structure of Shader objects. [More info](SL-Shader.html)
See in [Glossary](Glossary.html#ShaderLab) and HLSL.
| **Page** | **Description** |
| --- | --- |
| [Create a shader file](class-Shader.html) | Create a customshader asset file either using the Unity Editor or manually. |
| [Add a subshader in a custom shader](writing-shader-create-subshader-object.html) | Use a `SubShader` block to add one or more sections that define different GPU settings and shader programs for different hardware, **render pipelines**A series of operations that take the contents of a Scene, and displays them on a screen. Unity lets you choose from pre-built render pipelines, or write your own. [More info](render-pipelines.html) See in [Glossary](Glossary.html#renderpipeline), and runtime settings. |
| [Add a shader pass in a custom shader](writing-shader-create-shader-pass.html) | Use a `Pass` block to write instructions for setting the state of the GPU, and the shader programs that run on the GPU. |
| [Include a shader pass with the UsePass command](writing-shader-usepass.html) | Insert a named Pass from another **Shader object**An instance of the Shader class, a Shader object is container for shader programs and GPU instructions, and information that tells Unity how to use them. Use them with materials to determine the appearance of your scene. [More info](shader-objects.html) See in [Glossary](Glossary.html#Shaderobject), to avoid reduce code duplication in shader source files. |
| [Writing HLSL shader programs](writing-shader-writing-shader-programs-hlsl.html) | Resources for writing HLSL shader programs inside a `Pass` block in a custom ShaderLab shader. |
| [GLSL in Unity](SL-GLSLShaderPrograms.html) | If a platform supports OpenGL Core and OpenGL ES, you can write OpenGL Shading Language (GLSL) shader programs in Unity. |
| [Setting the render state on the GPU](writing-shader-render-state-commands.html) | Resources for using commands in a subshader or shader pass that change the render state on the GPU. |
## Additional resources
* [Shader languages reference](shaders-reference.html)
* [Writing custom shaders in URP](urp/writing-custom-shaders-urp.html)
* [Writing custom shaders in the Built-In Render Pipeline](writing-shaders-birp.html)
* [HLSL shader examples in the Built-In Render Pipeline](built-in-shader-examples.html)