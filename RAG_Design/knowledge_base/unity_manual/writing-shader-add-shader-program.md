--- 
Source: Unity 6 Manual (writing-shader-add-shader-program.md)
---

# Add an HLSL shader program
To add a High-Level **Shader**A program that runs on the GPU. [More info](Shaders.html)
See in [Glossary](Glossary.html#shader) Language (HLSL) program to a [shader file](class-Shader.html), add the code to the `Pass` block. Wrap the code in `HLSLPROGRAM` and `ENDHLSL` macros. For example:
```
Shader "Examples/ExampleShader"
{
    SubShader
    {
        Pass
        {
              Name "ExamplePassName"
              HLSLPROGRAM
                // Add HLSL shader program code here
              ENDHLSL
        }
    }
}
```
## Additional resources
* [ShaderLab: adding shader programs](shader-shaderlab-code-blocks.html)