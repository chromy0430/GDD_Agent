--- 
Source: Unity 6 Manual (SL-Reference.md)
---

# ShaderLab language reference
Find the blocks, directives, and commands you need to write a shader in **ShaderLab**Unity’s language for defining the structure of Shader objects. [More info](SL-Shader.html)
See in [Glossary](Glossary.html#ShaderLab).
| **Page** | **Description** |
| --- | --- |
| [Shader](SL-Shader-object.html)A program that runs on the GPU. [More info](Shaders.html) See in [Glossary](Glossary.html#shader) | Explore the `Shader` block in ShaderLab to create a shader, and add material properties, custom editors and a fallback shader. |
| [SubShader](SL-SubShader-object.html) | Explore the `SubShader` block in ShaderLab to create a subshader, and add **LOD**The *Level Of Detail* (LOD) technique is an optimization that reduces the number of triangles that Unity has to render for a GameObject when its distance from the Camera increases. [More info](LevelOfDetail.html) See in [Glossary](Glossary.html#LOD) values, tags, or a `UsePass` or `GrabPass` directive. |
| [Pass](SL-SubShader-pass.html) | Explore the `Pass` block in ShaderLab to create a shader pass, and add a name, tags, and shader code blocks. |
| [GPU render state commands](SL-Commands.html) | Find the commands in ShaderLab you need to change the render state on the GPU, such as `Blend`, `Cull` and `ZWrite`. |
| [PackageRequirements block](SL-PackageRequirements.html) | Explore the `PackageRequirements` block in ShaderLab to specify required packages for a subshader or shader pass. |
| [ShaderLab legacy functionality reference](shader-shaderlab-legacy.html) | Explore the ShaderLab commands that allow you to write shaders without using any HLSL code. |