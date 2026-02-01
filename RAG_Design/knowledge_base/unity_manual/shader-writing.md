--- 
Source: Unity 6 Manual (shader-writing.md)
---

# Writing shaders in code
This section contains information on the following subjects:
| **Page** | **Description** |
| --- | --- |
| [Introduction to writing shaders in code](SL-ShadingLanguage.html) | Learn about **ShaderLab**Unity’s language for defining the structure of Shader objects. [More info](SL-Shader.html) See in [Glossary](Glossary.html#ShaderLab), **Surface Shaders**A streamlined way of writing shaders for the Built-in Render Pipeline. [More info](SL-SurfaceShaders.html) See in [Glossary](Glossary.html#SurfaceShader), and High Level **Shader**A program that runs on the GPU. [More info](Shaders.html) See in [Glossary](Glossary.html#shader) Language (HLSL), and which languages and approaches to use for each **render pipeline**A series of operations that take the contents of a Scene, and displays them on a screen. Unity lets you choose from pre-built render pipelines, or write your own. [More info](render-pipelines.html) See in [Glossary](Glossary.html#renderpipeline). |
| [Shader object fundamentals](shader-objects.html) | Understand the object that Unity uses as a wrapper for shader programs and other information. |
| [Writing a custom shader in ShaderLab and HLSL](SL-landing.html) | Resources and techniques for writing **Shader objects**An instance of the Shader class, a Shader object is container for shader programs and GPU instructions, and information that tells Unity how to use them. Use them with materials to determine the appearance of your scene. [More info](shader-objects.html) See in [Glossary](Glossary.html#Shaderobject), subshaders and shader passes in ShaderLab and HLSL. |
| [Adding material properties to shaders](writing-shader-change-properties.html) | Resources and techniques for adding properties that artists can use to create, edit, and share materials with different configurations. |
| [Change how shaders work via branching and keywords](SL-MultipleProgramVariants.html) | Resources and techniques for writing shader code so it uses conditionals to do different things under different circumstances. |
| [Configure if or when Unity uses a shader](writing-shader-tags.html) | Resources for using tags and blocks in a shader to configure how and when Unity uses the shader. |
## Additional resources
* [Writing custom shaders in URP](urp/writing-custom-shaders-urp.html)
* [Writing custom shaders in the Built-In Render Pipeline](writing-shaders-birp.html)
* [Shader code blocks in ShaderLab reference](shader-shaderlab-code-blocks.html)