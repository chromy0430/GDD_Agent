--- 
Source: Unity 6 Manual (writing-shader-programs-introduction.md)
---

# Introduction to HLSL shader programs
In Unity, you usually write **shader**A program that runs on the GPU. [More info](Shaders.html)
See in [Glossary](Glossary.html#shader) programs in High-Level Shader Language (HLSL). To add HLSL code to your [shader asset](SL-Shader.html), add the code in a [shader code block](shader-shaderlab-code-blocks.html).
**Note:** Unity also supports writing shader programs in other languages like [OpenGL Shading Language (GLSL)](SL-GLSLShaderPrograms.html), but this isn’t generally needed or recommended.
There are two main types of shader programs you write in HLSL:
* **Vertex shader**A program that runs on each vertex of a 3D model when the model is being rendered. [More info](writing-shader-writing-shader-programs-hlsl.html)
  See in [Glossary](Glossary.html#vertexshader) programs, also known as vertex shaders. These programs usually transform the position of the **mesh**The main graphics primitive of Unity. Meshes make up a large part of your 3D worlds. Unity supports triangulated or Quadrangulated polygon meshes. Nurbs, Nurms, Subdiv surfaces must be converted to polygons. [More info](mesh.html)
  See in [Glossary](Glossary.html#Mesh) from object space to clip space, and pass data such as UV coordinates to the fragment shader program.
* Fragment shader programs, also known as fragment shaders or **pixel**The smallest unit in a computer image. Pixel size depends on your screen resolution. Pixel lighting is calculated at every screen pixel. [More info](ShadowPerformance.html)
  See in [Glossary](Glossary.html#pixel) shaders. These programs usually calculate and output the color of each pixel on-screen.
To make it easier to write shaders across different HLSL versions, graphics APIs, and platforms, Unity provides shader libraries with preprocessor macros. For more information, refer to [Shader methods in the Universal Render Pipeline (URP)](urp/use-built-in-shader-methods.html) or [Shader methods in the Built-In Render Pipeline](use-built-in-shader-methods-birp.html).
For general information on writing HLSL, refer to the [HLSL documentation](https://docs.microsoft.com/en-us/windows/win32/direct3dhlsl/dx-graphics-hlsl) on the Microsoft website.
## Additional resources
* [Optimize shaders](SL-ShaderPerformance.html)
* [Writing shaders for different graphics APIs](SL-PlatformDifferences.html)
* [Use 16-bit precision in shaders](SL-Use16BitPrecisionInShaders.html)
* [Custom Function Node](https://docs.unity3d.com/Packages/com.unity.shadergraph@latest/index.html?subfolder=/manual/Custom-Function-Node.html) in Shader Graph