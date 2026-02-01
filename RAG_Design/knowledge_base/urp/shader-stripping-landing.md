--- 
Source: Unity 6 URP Manual (shader-stripping-landing.html)
---

# Reducing shader variants in URP
The **shaders**A program that runs on the GPU. [More info](../Shaders.html)
See in [Glossary](../Glossary.html#shader) in the Universal **Render Pipeline**A series of operations that take the contents of a Scene, and displays them on a screen. Unity lets you choose from pre-built render pipelines, or write your own. [More info](../render-pipelines.html)
See in [Glossary](../Glossary.html#renderpipeline) (URP) use [shader keywords](../shader-keywords.html) to support many different features, which might mean Unity compiles a lot of [shader variants](../shader-variants.html)A verion of a shader program that Unity generates according to a specific combination of shader keywords and their status. A Shader object can contain multiple shader variants. [More info](../shader-variants.html)
See in [Glossary](../Glossary.html#shadervariant).
The following resources are about speeding up builds by reducing the number of shader variants URP compiles.
For more information, refer to [Reduce shader variants](../shader-variant-stripping.html), which applies to all render pipelines.
| **Page** | **Description** |
| --- | --- |
| [Check how many shader variants your build has](shader-stripping-check.html) | Log how many shader variants Unity compiles and strips. |
| [Strip feature shader variants](shader-stripping-features.html) | To remove shader variants for features you don’t use, enable **Strip Unused Variants** in URP Graphics settings. |
| [Enable dynamic branching in shaders](shader-stripping-fog.html) | Make Unity use dynamic branching in prebuilt or custom shaders, instead of keywords and shader variants. |
## Additional resources
* [Graphics performance and profiling in URP](../graphics-performance-and-profiling-in-urp.html)
* [Troubleshooting shaders](../shader-troubleshooting.html)