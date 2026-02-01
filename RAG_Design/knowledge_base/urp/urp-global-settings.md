--- 
Source: Unity 6 URP Manual (urp-global-settings.html)
---

# Graphics settings window reference for URP
If a project has the Universal Render Pipeline (URP) package installed, Unity shows URP-specific graphics settings in **Project Settings** > **Graphics** > **Pipeline Specific Settings** > **URP**.
The section contains the following settings that let you define project-wide settings for URP.
You can also add your own settings. Refer to [Add custom settings](https://docs.unity3d.com/Packages/com.unity.render-pipelines.core@17.0/manual/add-custom-graphics-settings) in the Scriptable **Render Pipeline**A series of operations that take the contents of a Scene, and displays them on a screen. Unity lets you choose from pre-built render pipelines, or write your own. [More info](../render-pipelines.html)
See in [Glossary](../Glossary.html#renderpipeline) (SRP) Core manual for more information.
## Default Volume Profile
Use this section to assign and edit a [Volume Profile](Volume-Profile.html) for the default volume that all **scenes**A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](../CreatingScenes.html)
See in [Glossary](../Glossary.html#Scene) use. Refer to [Understand Volumes](Volumes.html) for more information.
| **Property** | **Description** |
| --- | --- |
| **Volume Profile** | Set the [Volume Profile](Volume-Profile.html) the global default volume uses. You can’t set **Volume Profile** to **None**. |
URP displays all the properties for all the possible [Volume Overrides](VolumeOverrides.html). To edit or override the properties, use [the global volume for a quality level](set-up-a-volume.html#configure-the-global-volume-for-a-quality-level) or [create a volume](set-up-a-volume.html#add-a-volume).
## Adaptive Probe Volumes
| **Property** | **Description** |
| --- | --- |
| **Probe Volume Disable Streaming Assets** | When enabled, URP uses [streaming assets](https://docs.unity3d.com/6000.0/Documentation/Manual/StreamingAssets.html) to optimize [Adaptive Probe Volumes](probevolumes.html). Disable this setting if you use Asset Bundles and Addressables, which aren’t compatible with streaming assets. |
## Lightmap Sampling Settings
| **Property** | **Description** |
| --- | --- |
| **Use Bicubic **Lightmap**A pre-rendered texture that contains the effects of light sources on static objects in the scene. Lightmaps are overlaid on top of scene geometry to create the effect of lighting. [More info](../Lightmapping.html) See in [Glossary](../Glossary.html#Lightmap) Sampling** | Improves the visual fidelity of lightmaps by smoothening sharp or jagged edges, especially at the edges of shadows. Enabling this property might reduce performance on lower-end platforms. |
## Additional Shader Stripping Settings
The check boxes in this section define which **shader**A program that runs on the GPU. [More info](../Shaders.html)
See in [Glossary](../Glossary.html#shader) variants Unity strips when you build the Player.
| **Property** | **Description** |
| --- | --- |
| **Export Shader Variants** | Output two log files with shader compilation information when you build your project. For more information, refer to [Reducing shader variants in URP](shader-stripping-landing.html). |
| **Shader Variant Log Level** | Select what information about Shader variants Unity saves in logs when you build your Unity Project. Options: • Disabled: Unity doesn’t save any shader variant information. • Only SRP Shaders: Unity saves only shader variant information for URP shaders. • All Shaders: Unity saves shader variant information for every shader type. |
| **Strip Debug Variants** | When enabled, Unity strips all debug view shader variants when you build the Player. This decreases build time, but prevents the use of Rendering Debugger in Player builds. |
| **Strip Unused Post Processing Variants** | When enabled, Unity assumes that the Player does not create new [Volume Profiles](Volume-Profile.html) at runtime. With this assumption, Unity only keeps the shader variants that the existing [Volume Profiles](Volume-Profile.html) use, and strips all the other variants. Unity keeps shader variants used in Volume Profiles even if the scenes in the project do not use the Profiles. |
| **Strip Unused Variants** | When enabled, Unity performs shader stripping in a more efficient way. This option reduces the amount of shader variants in the Player by a factor of 2 if the project uses the following URP features:  * Rendering Layers * Native Render Pass * Reflection Probe Blending * Reflection Probe Box Projection * SSAO Renderer Feature * Decal Renderer Feature * Certain post-processing effects  Disable this option only if you notice issues in the Player. |
| **Strip Screen Coord Override Variants** | When enabled, Unity strips Screen Coordinates Override shader variants in Player builds. |
## Render Graph
Use this section to enable, disable or configure the render graph system. Refer to [Render graph system](render-graph.html) for more information.
| **Property** | **Description** |
| --- | --- |
| **Enable Compilation Caching** | When enabled, URP uses the compiled render graph from the previous frame when it can, instead of compiling the render graph again. This speeds up rendering. |
| **Enable Validity Checks** | When enabled, URP validates aspects of a render graph in the Editor and in a **development build**A development build includes debug symbols and enables the Profiler. [More info](../building-introduction.html) See in [Glossary](../Glossary.html#developmentbuild). **Enable Validity Checks** is disabled automatically in final builds. |
## VRS - Runtime Resources
Use this section to configure Variable Rate Shading (VRS).
| **Property** | **Description** |
| --- | --- |
| **Texture Compute Shader** | Sets the compute shader that the [`ColorMaskTextureToShadingRateImage`](https://docs.unity3d.com/Packages/com.unity.render-pipelines.core@17.4/api/UnityEngine.Rendering.Vrs.html#UnityEngine_Rendering_Vrs_ColorMaskTextureToShadingRateImage_UnityEngine_Rendering_RenderGraphModule_RenderGraph_UnityEngine_Rendering_RTHandle_UnityEngine_Rendering_RTHandle_System_Boolean_) API uses to convert colors to shading rate values during Variable Rate Shading. The default is the built-in `VrsTexture` compute shader. |
| **Visualization Shader** | Sets the shader that the [`ShadingRateImageToColorMaskTexture`](https://docs.unity3d.com/Packages/com.unity.render-pipelines.core@17.4/api/UnityEngine.Rendering.Vrs.html#UnityEngine_Rendering_Vrs_ShadingRateImageToColorMaskTexture_UnityEngine_Rendering_RenderGraphModule_RenderGraph_UnityEngine_Rendering_RenderGraphModule_TextureHandle__UnityEngine_Rendering_RenderGraphModule_TextureHandle__) API uses to convert shading rate values to colors in visualizations, such as in the Rendering Debugger window. The default is the built-in `VrsVisualization` shader. |
| **Visualization Lookup Table** | Sets the color mapping the **Visualization Shader** uses to convert shading rate values into colors for display. |
| **Conversion Lookup Table** | Sets the lookup table the **Texture Compute Shader** uses to map input colors to their corresponding shading rate values. |