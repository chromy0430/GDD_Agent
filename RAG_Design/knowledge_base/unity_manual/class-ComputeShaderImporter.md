--- 
Source: Unity 6 Manual (class-ComputeShaderImporter.md)
---

# Compute shader Import Settings window reference
[Switch to Scripting](../ScriptReference/ComputeShaderImporter.html "Go to ComputeShaderImporter page in the Scripting Reference")
View the properties and compiled code of a [compute shader](class-ComputeShader.html).
## Imported object
| **Property** | **Description** |
| --- | --- |
| **Kernels** | Displays the names of the kernels the **shader**A program that runs on the GPU. [More info](Shaders.html) See in [Glossary](Glossary.html#shader) code defines, and which graphics APIs Unity compiles the kernels for. |
| **Preprocess only** | Sets **Show compiled code** to generate only the preprocessed code instead of the final code. For more information, refer to [Shader compilation](shader-compilation.html). |
| **Strip #line directives** | Removes `#line` statements that display how the preprocessed code maps to the original HLSL code. This property is available only if you enable **Preprocess only**. |
| **Show compiled code** | Opens your text editor with the shader code Unity compiles. |
## Additional resources
* [Create a compute shader](class-ComputeShader-create.html)
* [Shader Import Settings window reference](class-ShaderImporter.html)