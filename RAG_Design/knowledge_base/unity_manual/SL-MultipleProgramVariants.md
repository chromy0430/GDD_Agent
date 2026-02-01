--- 
Source: Unity 6 Manual (SL-MultipleProgramVariants.md)
---

# Changing how shaders work using keywords
Resources and techniques for adding **shader**A program that runs on the GPU. [More info](Shaders.html)
See in [Glossary](Glossary.html#shader) keywords, using them to create branches and shader variants, and toggling them in the Unity Editor or in a script.
| **Page** | **Description** |
| --- | --- |
| [Shader keywords workflow](shader-keywords.html) | Learn about defining shader keywords to create shaders that share some common code, but have different functionality when you enable or disable a keyword. |
| [How Unity compiles branching shaders](shader-conditionals-choose-a-type.html) | Choose dynamic branching or shader variants. |
| [Declare shader keywords](SL-MultipleProgramVariants-declare.html) | Use a `#pragma` directive in HLSL code to declare keywords. |
| [Make shader behavior conditional on keywords](SL-MultipleProgramVariants-make-conditionals.html) | Use an `if` statement in HLSL code to mark parts of your shader code conditional based on whether you enable or disable a shader keyword. |
| [Toggle shader keywords in the Editor](shader-keywords-material-inspector.html) | Add material properties for shader keywords. |
| [Toggle shader keywords in a script](shader-keywords-scripts.html) | Check if a keyword is enabled or disabled, and enable and disable it. |
| [Add built-in keyword sets](SL-MultipleProgramVariants-shortcuts.html) | Use Unity shader directive shortcuts to create sets of shader keywords and variants. |
## Additional resources
* [Limit shader variants when you declare shader keywords](shader-variant-stripping.html#limit-shader-variants-when-you-declare-shader-keywords)
* [Unity Shader Variants Optimization & Troubleshooting Tips](https://unity.com/blog/engine-platform/shader-variants-optimization-troubleshooting-tips)
* [HLSL `pragma` directives reference](SL-PragmaDirectives.html)