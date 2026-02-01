--- 
Source: Unity 6 Manual (shader-keywords-default.md)
---

# Default shader keywords
Unity uses predefined sets of **shader**A program that runs on the GPU. [More info](Shaders.html)
See in [Glossary](Glossary.html#shader) keywords to generate shader variants that enable common functionality.
Unity adds the following sets of shader variant keywords at compile time:
* By default, Unity adds this set of keywords to all graphics shader programs: STEREO\_INSTANCING\_ON, STEREO\_MULTIVIEW\_ON, STEREO\_CUBEMAP\_RENDER\_ON, UNITY\_SINGLE\_PASS\_STEREO. You can strip these keywords using an Editor script. For more information, see [Shader variant stripping](shader-variant-stripping.html).
* By default, Unity adds this set of keywords to the Standard Shader: LIGHTMAP\_ON, DIRLIGHTMAP\_COMBINED, DYNAMICLIGHTMAP\_ON, LIGHTMAP\_SHADOW\_MIXING, SHADOWS\_SHADOWMASK. You can strip these keywords using the [Graphics settings](class-GraphicsSettings.html) window.
* In the Built-in **Render Pipeline**A series of operations that take the contents of a Scene, and displays them on a screen. Unity lets you choose from pre-built render pipelines, or write your own. [More info](render-pipelines.html)
  See in [Glossary](Glossary.html#renderpipeline), if your project uses [tier settings](graphics-tiers-customize.html) that differ from each other, Unity adds this set of keywords to all graphics shaders: UNITY\_HARDWARE\_TIER1, UNITY\_HARDWARE\_TIER2, UNITY\_HARDWARE\_TIER3. For more information, see [Graphics tiers: Graphics tiers and shader variants](graphics-tiers.html#shader-variants).