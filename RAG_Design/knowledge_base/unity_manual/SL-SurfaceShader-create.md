--- 
Source: Unity 6 Manual (SL-SurfaceShader-create.md)
---

# Create a surface shader in the Built-In Render Pipeline
Follow these steps:
1. Add a `CGPROGRAM` block to the `SubShader` block in your **shader**A program that runs on the GPU. [More info](Shaders.html)
   See in [Glossary](Glossary.html#shader) code, not the `Pass` block. Unity automatically creates multiple passes when it compiles the **surface shader**A streamlined way of writing shaders for the Built-in Render Pipeline. [More info](SL-SurfaceShaders.html)
   See in [Glossary](Glossary.html#SurfaceShader).
2. Add a `#pragma surface [surfaceFunction] [lightModel]` directive.
Surface shaders aren’t compatible with `HLSLPROGRAM` blocks, but you can use HLSL inside a `CGPROGRAM` block. For more information, refer to [Shader code blocks in ShaderLab reference](shader-shaderlab-code-blocks.html).
## Example
```
Shader "Example/Diffuse Simple" {
  SubShader {
    Tags { "RenderType" = "Opaque" }
    CGPROGRAM
    #pragma surface surf Lambert
    struct Input {
        float4 color : COLOR;
    };
    void surf (Input IN, inout SurfaceOutput o) {
        o.Albedo = 1;
    }
    ENDCG
  }
  Fallback "Diffuse"
}
```
Here’s how it looks like on a model with two [Lights](class-Light.html) set up:
![Basic surface shader example.](../uploads/Main/SurfaceShaderSimple.jpg)
Basic surface shader example.