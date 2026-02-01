--- 
Source: Unity 6 Manual (writing-shader-writing-shader-programs-hlsl.md)
---

# Writing HLSL shader programs
Write High-Level **Shader**A program that runs on the GPU. [More info](Shaders.html)
See in [Glossary](Glossary.html#shader) Language (HLSL) vertex and fragment shader programs inside a `Pass` block in a custom **ShaderLab**Unity’s language for defining the structure of Shader objects. [More info](SL-Shader.html)
See in [Glossary](Glossary.html#ShaderLab) shader.
| **Page** | **Description** |
| --- | --- |
| [Introduction to HLSL shader programs](writing-shader-programs-introduction.html) | Learn about writing shader programs in HLSL in Unity, and vertex and fragment shaders. |
| [Add an HLSL shader program](writing-shader-add-shader-program.html) | Use the `HLSLPROGRAM` directive to add a shader program to a shader pass. |
| [Reuse HLSL code](writing-shader-include-shader-program.html) | Include or duplicate HLSL in different places, or share `#pragma` directives across different shaders. |
| [Input data into HLSL](SL-VertexProgramInputs.html) | Create a `struct` that declares shader variables and connects them to the vertex data of the **mesh**The main graphics primitive of Unity. Meshes make up a large part of your 3D worlds. Unity supports triangulated or Quadrangulated polygon meshes. Nurbs, Nurms, Subdiv surfaces must be converted to polygons. [More info](mesh.html) See in [Glossary](Glossary.html#Mesh). |
| [Sample a texture in HLSL](SL-SamplerStates.html) | Declare and sample a texture in HLSL using a sampler. |
| [Writing HLSL for different graphics APIs](SL-PlatformDifferences.html) | Write HLSL to take into account how graphics rendering differs between different graphics APIs. |
| [Use 16-bit precision in shaders](SL-Use16BitPrecisionInShaders.html) | Use 16-bit precision in GPU calculations, so shaders use less memory, bandwidth, and power, and calculations are faster. |
| [Pass information to the shader compiler](writing-shader-programs-pragma-directives.html) | Use the `#define`, `#pragma`, and `#define_for_platform_compiler` directives to pass information to the shader compiler. |
## Additional resources
* [Shader languages reference](shaders-reference.html)
* [HLSL pragma directives reference](SL-PragmaDirectives.html)
* [HLSL shader examples in the Built-In Render Pipeline](built-in-shader-examples.html)
* [Writing custom shaders in the Universal Render Pipeline (URP)](urp/writing-custom-shaders-urp.html)