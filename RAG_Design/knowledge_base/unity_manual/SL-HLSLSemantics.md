--- 
Source: Unity 6 Manual (SL-HLSLSemantics.md)
---

# HLSL semantics reference
Explore the semantics you can use to input **mesh**The main graphics primitive of Unity. Meshes make up a large part of your 3D worlds. Unity supports triangulated or Quadrangulated polygon meshes. Nurbs, Nurms, Subdiv surfaces must be converted to polygons. [More info](mesh.html)
See in [Glossary](Glossary.html#Mesh) data into custom shaders in High-Level **Shader**A program that runs on the GPU. [More info](Shaders.html)
See in [Glossary](Glossary.html#shader) Language (HLSL) in Unity.
| **Semantic** | **Description** | **Type** |
| --- | --- | --- |
| `POSITION` | The vertex position. | `float3` or `float4` |
| `NORMAL` | The vertex normal. | `float3` |
| `TEXCOORD0` | The first UV coordinates. | `float2`, `float3`, or `float4` |
| `TEXCOORD1` | The second UV coordinates. | `float2`, `float3`, or `float4` |
| `TEXCOORD2` | The third UV coordinates. | `float2`, `float3`, or `float4` |
| `TEXCOORD3` | The fourth UV coordinates. | `float2`, `float3`, or `float4` |
| `TANGENT` | The tangent vector used for normal mapping. | `float4` |
| `COLOR` | The per-vertex color. | `float4` |
| `VPOS` | The **pixel**The smallest unit in a computer image. Pixel size depends on your screen resolution. Pixel lighting is calculated at every screen pixel. [More info](ShadowPerformance.html) See in [Glossary](Glossary.html#pixel) position in screen space. You can use `VPOS` only in the fragment shader. | Use `UNITY_VPOS_TYPE` for cross-platform compatibility, which is `float4` on most platforms. |
| `VFACE` | Indicates whether the pixel surface is facing the **camera**A component which creates an image of a particular viewpoint in your scene. The output is either drawn to the screen or captured as a texture. [More info](CamerasOverview.html) See in [Glossary](Glossary.html#Camera). | `float` |
| `SV_VertexID` | The index of the vertex. You can’t use `SV_VertexID` in **Surface Shaders**A streamlined way of writing shaders for the Built-in Render Pipeline. [More info](SL-SurfaceShaders.html) See in [Glossary](Glossary.html#SurfaceShader). | `uint` |
## Additional resources
* [HLSL pragma directives reference](SL-PragmaDirectives.html)
* [Semantics](https://learn.microsoft.com/en-us/windows/win32/direct3dhlsl/dx-graphics-hlsl-semantics) in the Microsoft HLSL documentation