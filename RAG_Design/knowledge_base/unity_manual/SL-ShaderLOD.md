--- 
Source: Unity 6 Manual (SL-ShaderLOD.md)
---

# LOD directive in ShaderLab reference
This page contains information on using a `LOD` block in your **ShaderLab**Unity’s language for defining the structure of Shader objects. [More info](SL-Shader.html)
See in [Glossary](Glossary.html#ShaderLab) code to assign a **LOD**The *Level Of Detail* (LOD) technique is an optimization that reduces the number of triangles that Unity has to render for a GameObject when its distance from the Camera increases. [More info](LevelOfDetail.html)
See in [Glossary](Glossary.html#LOD) (level of detail) value to a SubShader.
## Render pipeline compatibility
| **Feature name** | **Universal **Render Pipeline**A series of operations that take the contents of a Scene, and displays them on a screen. Unity lets you choose from pre-built render pipelines, or write your own. [More info](render-pipelines.html) See in [Glossary](Glossary.html#renderpipeline) (URP)** | **High Definition Render Pipeline (HDRP)** | **Custom SRP** | **Built-in Render Pipeline** |
| --- | --- | --- | --- | --- |
| **ShaderLab: SubShader LOD block** | Yes | Yes | Yes | Yes |
## Syntax
In ShaderLab, you assign a LOD value to a SubShader by placing a `LOD` block inside a `SubShader` block.
| **Signature** | **Function** |
| --- | --- |
| LOD [value] | Assigns the given LOD value to the SubShader. |
## LOD values for Unity’s built-in shaders
In the Built-in Render Pipeline, Unity’s built-in **shaders**A program that runs on the GPU. [More info](Shaders.html)
See in [Glossary](Glossary.html#shader) have the following LOD values:
| **LOD value** | **Shader name** |
| --- | --- |
| 100 | Unlit/Texture Unlit/Color Unlit/Transparent Unlit/Transparent Cutout |
| 300 | Standard Standard (Specular Setup) Autodesk Interactive |
## LOD values for legacy shaders
In the Built-in Render Pipeline, Unity’s built-in [legacy shaders](Built-inShaderGuide.html) have the following LOD values:
| **LOD value** | **Shader name** |
| --- | --- |
| 100 | VertexLit |
| 150 | Decal Reflective VertexLit |
| 200 | Diffuse |
| 250 | Diffuse Detail Reflective Bumped Unlit Reflective Bumped VertexLit |
| 300 | Bumped Specular |
| 400 | Bumped Specular |
| 500 | Parallax |
| 600 | Parallax Specular |
## Additional resources
* [Optimize shaders](SL-ShaderPerformance.html)