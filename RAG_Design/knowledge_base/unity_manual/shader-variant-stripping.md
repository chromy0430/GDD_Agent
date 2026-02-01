--- 
Source: Unity 6 Manual (shader-variant-stripping.md)
---

# Reduce shader variants
You can prevent [shader variants](shader-variants.html)A verion of a shader program that Unity generates according to a specific combination of shader keywords and their status. A Shader object can contain multiple shader variants. [More info](shader-variants.html)
See in [Glossary](Glossary.html#shadervariant) from being compiled. This is called **stripping**. Stripping unneeded variants can greatly reduce build times, file size, **shader**A program that runs on the GPU. [More info](Shaders.html)
See in [Glossary](Glossary.html#shader) loading times, and runtime memory usage. In larger projects, or projects with complex shaders, this is a very important consideration.
**Note:** For information about shader keywords in Shader Graph, refer to [Introduction to keywords in Shader Graph](https://docs.unity3d.com/Packages/com.unity.shadergraph@latest?subfolder=/manual/Keywords-concepts.html).
## Limit or remove shader variants by keyword
To reduce the number of shader variants Unity compiles, use the Shader Build Settings in the Graphics settings window.
Follow these steps:
1. From the main menu, go to **Edit** > **Project Settings** > **Graphics**.
2. In the **Shader Build Settings** section, select the **Add** (**+**) button.
3. Add the keyword set you want to change.
4. Use spaces to separate keywords in the set, for example `FOG_LINEAR FOG_EXP FOG_EXP2`.
5. Enter all the keywords in the set, including `_` if it exists.
For which keywords Unity uses in prebuilt shaders in the Universal **Render Pipeline**A series of operations that take the contents of a Scene, and displays them on a screen. Unity lets you choose from pre-built render pipelines, or write your own. [More info](render-pipelines.html)
See in [Glossary](Glossary.html#renderpipeline), refer to [Strip feature shader variants](urp/shader-stripping-features.html).
You can then do one of the following:
* To limit the number of shader variants, set **Type Override** to either `shader_feature` or `dynamic_branch`. For more information about choosing a type, refer to [How Unity compiles branching shaders](shader-conditionals-choose-a-type.html#choose-type).
* To exclude shader code for the keywords in the build, select the foldout (triangle). Unity displays a checkbox for each keyword. To compile shader code for a keyword, enable its checkbox.
Select **Apply** to apply the changes. To remove a keyword set, select the **Remove** (**-**) button.
To customize shader variants for different platforms, use a **build profile**A set of customizable configuration settings to use when creating a build for your target platform. [More info](build-profiles.html)
See in [Glossary](Glossary.html#buildprofile). Each build profile you create has its own **Shader Build Settings** section that overrides the settings in the Graphics settings window. For more information, refer to [Override settings with build profiles](build-profiles-override-settings.html).
## Reduce shader variants using other settings
You can also do the following to reduce or remove shader variants:
* Strip certain shader variants in the **Shader Stripping** section.
* If you use the Universal Render Pipeline (URP), refer to [Reducing shader variants in URP](urp/shader-stripping-landing.html).
* If you use the High Definition Render Pipeline (HDRP), refer to [Reduce shader variants in HDRP](https://docs.unity3d.com/Packages/com.unity.render-pipelines.high-definition@17.3/manual/reduce-shader-variants.html).
* If you use the Built-In Render Pipeline, ensure your Tier settings are identical unless you need them to be different. For more information, refer to [Graphics tiers](graphics-tiers.html).
## Reduce shader variants using Editor scripts
For shader variants that you can’t strip in other ways, you can use the following APIs in an Editor script to perform build-time stripping:
* [IPreprocessShaders.OnProcessShader](../ScriptReference/Build.IPreprocessShaders.OnProcessShader.html): receive a callback before Unity compiles a graphics shader Pass into a build.
* [IPreprocessComputeShaders.OnProcessComputeShader](../ScriptReference/Build.IPreprocessComputeShaders.OnProcessComputeShader.html): receive a callback before Unity compiles a compute shader into a build.
For more information on this subject, refer to [Stripping scriptable shader variants](https://unity.com/blog/engine-platform/stripping-scriptable-shader-variants)
## Avoid removing shader variants your build uses
If you strip a shader variant that a Material needs at runtime, Unity tries to choose a similar shader variant that’s available. To avoid this, use the following approaches:
* [Check what shader variants you have](shader-how-many-variants.html) to help you see which shader variants and keyword combinations Materials need at runtime.
* Add shaders to the **Always Included Shaders** list in [Graphics settings](class-GraphicsSettings.html).
* If you use a `shader_feature` keyword, don’t use the keyword to change which code branch executes at runtime.
## Additional resources
* [Troubleshooting shader duplication from AssetBundles](avoid-shader-duplication.html)