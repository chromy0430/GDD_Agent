--- 
Source: Unity 6 Manual (SL-ShaderPerformance.md)
---

# Optimize shaders
This page contains information on optimizing your **shaders**A program that runs on the GPU. [More info](Shaders.html)
See in [Glossary](Glossary.html#shader) for runtime performance, especially on mobile platforms that have limited GPU performance.
## Avoid complex calculations
To avoid complex calculations, do the following for example:
* Use lookup textures instead of resource-intensive functions such as `pow`, `log` and `sin`.
* Use Unity HLSL functions, such as `normalize` and `dot`, instead of writing your own. This ensures that the driver can generate better code.
## Avoid repeated calculations
To avoid shaders repeating calculations, do the following for example:
* Move calculations from the fragment shader to the **vertex shader**A program that runs on each vertex of a 3D model when the model is being rendered. [More info](writing-shader-writing-shader-programs-hlsl.html)
  See in [Glossary](Glossary.html#vertexshader), so they run only for every vertex, not every fragment.
* Do calculations in a C# script instead, then use the calculated value in the shader.
* Avoid unnecessary calculations. For example, remove code that supports multiple colors per material if you always use the same color.
## Use lower precision data types
Use `half` instead of `float` for all variables except world space coordinates and texture coordinates. For more information, refer to [Use 16-bit precision in shaders](SL-Use16BitPrecisionInShaders.html).
## Use casts instead of suffixes
Unity doesn’t support suffixes, so a value like `2.0h` becomes a full `float`. This means when the GPU does calculations, it might have to convert other values to `float` and back. This can slow down the shader.
To prevent this, use casts instead of suffixes. For example, use `half(2.0)` instead of `2.0h`.
## Avoid discarding pixels or channels
To avoid shaders slowing down, avoid the following resource-intensive methods:
* The `discard` method in the fragment shader.
* [ColorMask](SL-Pass.html) on mobile platforms.
## Avoid writing to the depth buffer
To ensure mobile GPUs can use early depth testing to speed up rendering, don’t write to the **depth buffer**A memory store that holds the z-value depth of each pixel in an image, where the z-value is the depth for each rendered pixel from the projection plane. [More info](class-RenderTexture.html)
See in [Glossary](Glossary.html#depthbuffer) in the fragment shader.
For more information about depth testing, refer to [ShaderLab command: ZTest](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-ZTest.html).
## Prioritize lower quality shaders with the LOD command
To set Unity to prioritise lower quality shaders on lower-end hardware, use the `LOD` command in your **ShaderLab**Unity’s language for defining the structure of Shader objects. [More info](SL-Shader.html)
See in [Glossary](Glossary.html#ShaderLab) code.
**Note:** Although this technique is named after the **LOD**The *Level Of Detail* (LOD) technique is an optimization that reduces the number of triangles that Unity has to render for a GameObject when its distance from the Camera increases. [More info](LevelOfDetail.html)
See in [Glossary](Glossary.html#LOD) feature for rendering meshes, there are important differences: shader LOD does not relate to distance from the **Camera**A component which creates an image of a particular viewpoint in your scene. The output is either drawn to the screen or captured as a texture. [More info](CamerasOverview.html)
See in [Glossary](Glossary.html#Camera), and Unity does not calculate shader LOD automatically. You must set the maximum shader LOD manually.
Follow these steps:
1. Assign LOD values to subshaders. The lower the value, the less computationally demanding the subshader is. For example:
   ```
   Shader "Examples/ExampleLOD"
   {
       SubShader
       {
           LOD 200
           ...
       }
       SubShader
       {
           LOD 100
           ...
       }
   }
   ```
   If you have multiple subshaders in a single **Shader object**An instance of the Shader class, a Shader object is container for shader programs and GPU instructions, and information that tells Unity how to use them. Use them with materials to determine the appearance of your scene. [More info](shader-objects.html)
   See in [Glossary](Glossary.html#Shaderobject), make sure subshaders are in descending LOD order with the highest LOD value first. This is because Unity selects the first valid SubShader it finds, so if it finds one with a lower LOD first it will always use that.
2. At runtime, set the **shader LOD** value for a single Shader object, or for all Shader objects. Use [Shader.maximumLOD](../ScriptReference/Shader-maximumLOD.html). To set the shader LOD for all Shader objects, you can use [Shader.globalMaximumLOD](../ScriptReference/Shader-globalMaximumLOD.html). By default, there is no maximum LOD.
Unity now prioritises SubShaders that have a lower LOD value. For information on how Unity chooses when to use SubShaders, see [How Unity selects a subshader](shader-loading.html#selecting-subshaders).
## Additional resources
* [LOD directive in ShaderLab reference](SL-ShaderLOD.html)
## Additional resources
* [Writing shaders for different graphics APIs](SL-PlatformDifferences.html)
* [Metal requirements and compatibility](metal-requirements-and-compatibility.html)
* [Optimize surface shaders](SL-SurfaceShaderOptimize.html)