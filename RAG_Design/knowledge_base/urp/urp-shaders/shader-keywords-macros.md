--- 
Source: Unity 6 URP Manual (urp-shaders\shader-keywords-macros.html)
---

# Shader keywords and macros reference in URP
Shader keywords and macros that enable or provide access to URP features in **shaders**A program that runs on the GPU. [More info](../../Shaders.html)
See in [Glossary](../../Glossary.html#shader).
| **Element** | **Description** |
| --- | --- |
| `_CLUSTER_LIGHT_LOOP` | Use this `multi_compile` keyword to make the shader compatible with the Forward+ and Deferred+ **rendering paths**The technique that a render pipeline uses to render graphics. Choosing a different rendering path affects how lighting and shading are calculated. Some rendering paths are more suited to different platforms and hardware than others. [More info](../../RenderingPaths.html) See in [Glossary](../../Glossary.html#renderingpath). For an implementation example, refer to [Render additional lights in a shader](../use-built-in-shader-methods-additional-lights-fplus.html). |
| `_ADDITIONAL_LIGHTS` | Use this keyword to define areas in shader code that Unity should execute if per-pixel additional lights are enabled in a **scene**A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](../../CreatingScenes.html) See in [Glossary](../../Glossary.html#Scene) and URP Asset. If a renderer uses the Forward+ rendering path, Unity ignores this keyword and uses the `_CLUSTER_LIGHT_LOOP` keyword instead. For an implementation example, refer to [Render additional lights in a shader](../use-built-in-shader-methods-additional-lights-fplus.html). |
| `LIGHT_LOOP_BEGIN` | Use this macro to iterate over the additional lights. In the Forward+ rendering path, the `LIGHT_LOOP_BEGIN` macro requires the following struct to be in its scope, both the type and the variable name must match this signature: `InputData inputData`. For an implementation example, refer to [Render additional lights in a shader](../use-built-in-shader-methods-additional-lights-fplus.html). |
## Additional resources
* [Changing how shaders work via branching and keywords](../../SL-MultipleProgramVariants.html)
* [Shader methods in URP](../use-built-in-shader-methods.html)
* [Custom lighting in URP](../lighting/custom-lighting-landing.html)