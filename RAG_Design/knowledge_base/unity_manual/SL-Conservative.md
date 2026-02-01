--- 
Source: Unity 6 Manual (SL-Conservative.md)
---

# Conservative command in ShaderLab reference
Enables or disables conservative **rasterization**The process of generating an image by calculating pixels for each polygon or triangle in the geometry. This is an alternative to ray tracing.
See in [Glossary](Glossary.html#rasterization).
## Render pipeline compatibility
| **Feature name** | **Universal **Render Pipeline**A series of operations that take the contents of a Scene, and displays them on a screen. Unity lets you choose from pre-built render pipelines, or write your own. [More info](render-pipelines.html) See in [Glossary](Glossary.html#renderpipeline) (URP)** | **High Definition Render Pipeline (HDRP)** | **Custom SRP** | **Built-in Render Pipeline** |
| --- | --- | --- | --- | --- |
| **Conservative** | Yes | Yes | Yes | Yes |
## Syntax
This command makes a change to the render state. Use it in a `Pass` block to set the render state for that Pass, or use it in a `SubShader` block to set the render state for all Passes in that SubShader.
| **Signature** | **Example syntax** | **Function** |
| --- | --- | --- |
| `Conservative <enabled>` | `Conservative True` | Enables or disables conservative rasterization.  Requires DX 11.3+, or GL\_NV\_conservative\_raster. |
## Parameters
| **Parameter** | **Value** | **Function** |
| --- | --- | --- |
| **enabled** | `True` | Enables conservative rasterization. |
|  | `False` | Disables conservative rasterization. |
## Additional resources
* [Enable conservative rasterization in a shader](writing-shader-conservative-rasterization.html)