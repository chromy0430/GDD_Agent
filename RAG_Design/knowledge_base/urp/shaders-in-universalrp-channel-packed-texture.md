--- 
Source: Unity 6 URP Manual (shaders-in-universalrp-channel-packed-texture.html)
---

# Assign a channel-packed texture to a URP material
In the [Lit](lit-shader.html) and [Complex Lit](shader-complex-lit.html) **shaders**A program that runs on the GPU. [More info](../Shaders.html)
See in [Glossary](../Glossary.html#shader) in the Universal **Render Pipeline**A series of operations that take the contents of a Scene, and displays them on a screen. Unity lets you choose from pre-built render pipelines, or write your own. [More info](../render-pipelines.html)
See in [Glossary](../Glossary.html#renderpipeline) (URP), you can use a single RGBA texture for the metallic, smoothness, and occlusion properties. This technique is called channel packing or texture packing.
Follow these steps:
1. Create a texture with the following channels:
   | **Channel** | **Property** |
   | --- | --- |
   | Red | Metallic |
   | Green | Occlusion |
   | Blue | Not used |
   | Alpha | Smoothness |
2. [Import the texture](../ImportingTextures.html).
3. In the **Inspector**A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](../UsingTheInspector.html)
   See in [Glossary](../Glossary.html#Inspector) window for the texture, disable **sRGB (Color Texture)**.
4. Assign the texture to the **Metallic** and **Occlusion** properties of the material. Unity automatically uses the correct channels from the texture.
You can use [Shader Graph](../shader-graph.html) instead if you pack channels in textures differently.
## Additional resources
* [Materials](../Materials.html)An asset that defines how a surface should be rendered. [More info](../class-Material.html)
  See in [Glossary](../Glossary.html#Material)
* [Custom textures](../Textures-landing.html)