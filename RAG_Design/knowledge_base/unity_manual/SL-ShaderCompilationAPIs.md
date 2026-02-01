--- 
Source: Unity 6 Manual (SL-ShaderCompilationAPIs.md)
---

# Set the graphics API or platform for a shader
By default, Unity compiles all **shader**A program that runs on the GPU. [More info](Shaders.html)
See in [Glossary](Glossary.html#shader) programs for each graphics API in the list for the current build target. To compile certain shader programs only for certain graphics APIs or platforms, for example if you use features that aren’t supported on all platforms, use a `#pragma` statement.
Use one of the following in the `HLSLPROGRAM` block of a shader:
* `#pragma only_renderers` to compile shaders only for a specific graphics API, for example `#pragma only_renderers metal`.
* `#pragma exclude_renderers` to exclude shaders from compilation for a specific graphics API, for example `#pragma exclude_renderers metal`.
You can pass multiple values by adding a space between each argument, for example `#pragma only_renderers metal vulkan`.
The supported values are:
| **Value** | **Description** |
| --- | --- |
| `d3d11` | DirectX 11 feature level 10 and above, DirectX 12 |
| `glcore` | OpenGL 3.x, OpenGL 4.x |
| `gles3` | OpenGL ES 3.x, **WebGL**A JavaScript API that renders 2D and 3D graphics in a web browser. The Unity Web build option allows Unity to publish content as JavaScript programs which use HTML5 technologies and the WebGL rendering API to run Unity content in a web browser. [More info](webgl.html) See in [Glossary](Glossary.html#WebGL) 2.0 |
| `metal` | Metal on iOS or macOS |
| `ps4` | PlayStation®4 |
| `ps5` | PlayStation®5 |
| `playstation` | PlayStation®4 or PlayStation®5 |
| `switch` | Nintendo Switch™ |
| `vulkan` | Vulkan |
| `webgpu` | WebGPU |
| `xboxseries` | Xbox Series S|X |
## Additional resources
* [HLSL pragma directives reference](SL-PragmaDirectives.html)
* [HLSL pragma target command reference](SL-Pragma-target.html)
* [HLSL pragma require command reference](SL-Pragma-require.html)
* [SubShader tags in ShaderLab reference](SL-SubShaderTags.html)
* [Pass tags in ShaderLab reference](SL-PassTags.html)