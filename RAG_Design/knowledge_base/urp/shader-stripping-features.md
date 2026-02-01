--- 
Source: Unity 6 URP Manual (shader-stripping-features.html)
---

# Strip feature shader variants in URP
By default, URP compiles variants where a feature is enabled, and variants where a feature is disabled.
To reduce the number of variants, you can enable **Strip Unused Variants** in [URP Graphics settings](urp-global-settings.html) and do the following:
* Disable a feature in all URP Assets in your build, so URP keeps only variants where the feature is disabled.
* Enable a feature in all URP Assets in your build, so URP keeps only variants where the feature is enabled.
If you disable the **Strip Unused Variants setting**, URP can’t strip variants where the feature is disabled. This might increase the number of variants.
## Disable a feature
To let Unity strip variants related to a feature, disable it in all the URP Assets in your build.
Unity includes the following URP Assets in your build:
* The URP Asset you set as the default **render pipeline**A series of operations that take the contents of a Scene, and displays them on a screen. Unity lets you choose from pre-built render pipelines, or write your own. [More info](../render-pipelines.html)
  See in [Glossary](../Glossary.html#renderpipeline) asset in [Graphics settings](https://docs.unity3d.com/Manual/class-GraphicsSettings.html).
* Any URP Asset you set as a **Render Pipeline Asset** in a [Quality settings level](https://docs.unity3d.com/Manual/class-QualitySettings.html) you enable for the current build target.
**Note:** Avoid including URP Assets in your build that use different [rendering paths](rendering-paths-introduction-urp.html)The technique that a render pipeline uses to render graphics. Choosing a different rendering path affects how lighting and shading are calculated. Some rendering paths are more suited to different platforms and hardware than others. [More info](../RenderingPaths.html)
See in [Glossary](../Glossary.html#renderingpath): this would cause Unity to create two sets of variants for each keyword.
You can also disable **shader**A program that runs on the GPU. [More info](../Shaders.html)
See in [Glossary](../Glossary.html#shader) keywords in Graphics settings. For more information, refer to [Reduce shader variants](../shader-variant-stripping.html).
| **Feature** | **How to disable the feature** | **Shader keywords this turns off** | **Rendering Path** |
| --- | --- | --- | --- |
| Accurate G-buffer normals | Disable **Accurate G-buffer normals** in the URP Asset. This has no effect on platforms that use the Vulkan graphics API. | `_GBUFFER_NORMALS_OCT` | Deferred |
| Additional lights | In the **URP Asset**, in the **Lighting section**, disable **Additional Lights**. | `_ADDITIONAL_LIGHTS`, `_ADDITIONAL_LIGHTS_VERTEX` | Forward |
| Ambient occlusion | Remove the [Ambient Occlusion](post-processing-ssao.html)A method to approximate how much ambient light (light not coming from a specific direction) can hit a point on a surface. See in [Glossary](../Glossary.html#ambientocclusion) Renderer Feature in all Renderers that URP Assets use. | `_SCREEN_SPACE_OCCLUSION` | Forward and Deferred |
| Decals | Remove the [Decals](renderer-feature-decal.html) Renderer Feature in all Renderers that URP Assets use. | `_DBUFFER_MRT1`, `_DBUFFER_MRT2`, `_DBUFFER_MRT3`, `_DECAL_NORMAL_BLEND_LOW`, `_DECAL_NORMAL_BLEND_MEDIUM`, `_DECAL_NORMAL_BLEND_HIGH`, `_DECAL_LAYERS` | Forward and Deferred |
| Fast sRGB to linear conversion | In the **URP Asset**, in the ****Post-processing**A process that improves product visuals by applying filters and effects before the image appears on screen. You can use post-processing effects to simulate physical camera and film properties, for example Bloom and Depth of Field. [More info](../PostProcessingOverview.html) post processing, postprocessing, postprocess See in [Glossary](../Glossary.html#post-processing)** section, disable **Fast sRGB/Linear conversions**. | `_USE_FAST_SRGB_LINEAR_CONVERSION` | Forward and Deferred |
| Holes in **terrain**The landscape in your scene. A Terrain GameObject adds a large flat plane to your scene and you can use the Terrain’s Inspector window to create a detailed landscape. [More info](../terrain-UsingTerrains.html) See in [Glossary](../Glossary.html#Terrain) | In the **URP Asset**, in the **Rendering** section, disable **Terrain Holes**. | `_ALPHATEST_ON` | Forward |
| Level of detail (LOD) transitions | In the **URP Asset**, disable **LOD Cross Fade**.  If you need cross-fading, set **LOD Cross Fade Dithering Type** to **2x2 Stencil** instead to reduce shader variants by around 50% but slightly increase processing time on the GPU. This setting might not work correctly if you enable [GPU instancing](../GPUInstancing-landing.html) or enable **Stencil** in the **Overrides** section of the [Universal Renderer asset](urp-universal-renderer.html). | `_LOD_FADE_CROSSFADE` | Forward and Deferred |
| Light cookies | Remove [Cookie textures](https://docs.unity3d.com/Manual/Cookies.html) from all the lights in your project. | `_LIGHT_COOKIES` | Forward and Deferred |
| Rendering Layers for lights | Disable [Rendering Layers for Lights](features/rendering-layers.html). | `_LIGHT_LAYERS` | Forward and Deferred |
| **Reflection Probe**A rendering component that captures a spherical view of its surroundings in all directions, rather like a camera. The captured image is then stored as a Cubemap that can be used by objects with reflective materials. [More info](../class-ReflectionProbe.html) See in [Glossary](../Glossary.html#ReflectionProbe) blending | Disable [Probe Blending](../class-ReflectionProbe.html). | `_REFLECTION_PROBE_BLENDING` | Forward and Deferred |
| Reflection Probe box projection | Disable [Box Projection](../class-ReflectionProbe.html). | `_REFLECTION_PROBE_BOX_PROJECTION` | Forward and Deferred |
| Render Pass | Disable **Native Render** in all Renderers that URP Assets use. | `_RENDER_PASS_ENABLED` | Forward and Deferred |
| Shadows from additional lights | In the URP Asset, in the **Additional Lights** section, disable **Cast Shadows**. | `_ADDITIONAL_LIGHT_SHADOWS` | Forward and Deferred |
| Shadows from the main light | In the URP Asset, in the **Main Light** section, disable **Cast Shadows**. The keywords Unity removes might depend on your settings. | `_MAIN_LIGHT_SHADOWS`, `_MAIN_LIGHT_SHADOWS_CASCADE`, `_MAIN_LIGHT_SHADOWS_SCREEN` | Forward and Deferred |
| Soft shadows | In the URP Asset, in the **Shadows** section, disable **Soft shadows**. | `_SHADOWS_SOFT` | Forward and Deferred |
## Strip post-processing shader variants
Enable **Strip Unused Post Processing Variants** in [URP Graphics settings](urp-global-settings.html) to strip shader variants for [Volume Overrides](VolumeOverrides.html) you don’t use.
For example, if your project uses only the Bloom effect, URP keeps Bloom variants but strips all other post-processing variants.
Unity checks for Volume Overrides in all scenes, so you can’t strip variants by removing a **scene**A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](../CreatingScenes.html)
See in [Glossary](../Glossary.html#Scene) from your build but keeping it in your project. You must remove the scene from the project.
| **Volume Override removed** | **Shader keywords this turns off** |
| --- | --- |
| Bloom | `_BLOOM_HQ`, `BLOOM_HQ_DIRT`, `_BLOOM_LQ`, `BLOOM_LQ_DIRT` |
| Chromatic Aberration | `_CHROMATIC_ABERRATION` |
| Film Grain | `_FILM_GRAIN` |
| **HDR**high dynamic range See in [Glossary](../Glossary.html#HDR) Grading | `_HDR_GRADING` |
| Lens Distortion | `_DISTORTION` |
| **Tonemapping**The process of remapping HDR values of an image into a range suitable to be displayed on screen. [More info](../PostProcessingOverview.html) See in [Glossary](../Glossary.html#tonemapping) | `_TONEMAP_ACES`, `_TONEMAP_NEUTRAL`, `_TONEMAP_GRADING` |
Unless you override screen coordinates to support post-processing on large numbers of multiple displays (‘cluster’ displays), enable **Strip Screen Coord Override Variants** in URP Graphics settings as well.
## Strip XR and VR shader variants
If you don’t use [XR](https://docs.unity3d.com/Manual/XR.html)An umbrella term encompassing Virtual Reality (VR), Augmented Reality (AR) and Mixed Reality (MR) applications. Devices supporting these forms of interactive applications can be referred to as XR devices. [More info](../XR.html)
See in [Glossary](../Glossary.html#XR) or [VR](https://docs.unity3d.com/Manual/VROverview.html)Virtual Reality [More info](../VROverview.html)
See in [Glossary](../Glossary.html#VR), you can [disable the XR and VR modules](https://docs.unity3d.com/Documentation/Manual/upm-ui.html). This allows URP to strip XR and VR-related shader variants from its standard shaders.
## Open the URP stripping code
If you want to examine the code that strips shaders in URP, check the `Editor/ShaderPreprocessor.cs` file. The file uses the [IPreprocessShaders](https://docs.unity3d.com/ScriptReference/Build.IPreprocessShaders.html) API.
## Additional resources
* [FilterAttribute API](../../ScriptReference/ShaderKeywordFilter.FilterAttribute.html)