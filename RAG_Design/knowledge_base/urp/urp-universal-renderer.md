--- 
Source: Unity 6 URP Manual (urp-universal-renderer.html)
---

# Universal Renderer asset reference for URP
This page describes the URP Universal Renderer settings.
For more information on rendering in URP, also check [Rendering in the Universal Render Pipeline](rendering-in-universalrp.html).
## How to find the Universal Renderer asset
To find the Universal Renderer asset that a URP asset is using:
1. Select a URP asset.
2. In the Renderer List section, click a renderer item or the vertical ellipsis icon (⋮) next to a renderer.
   ![How to find the Universal Renderer asset](../../uploads/urp/urp-assets/find-renderer.png)
   How to find the Universal Renderer asset
## Properties
### Filtering
This section contains properties that define which layers the renderer draws.
| Property | Description |
| --- | --- |
| **Prepass **Layer Mask**A value defining which layers to include or exclude from an operation, such as rendering, collision or your own code. [More info](../Layers.html) See in [Glossary](../Glossary.html#LayerMask)** | The layers that **GameObjects**The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](../class-GameObject.html) See in [Glossary](../Glossary.html#GameObject) must be assigned to in order to affect any prepass. |
| **Opaque Layer Mask** | The layers that opaque GameObjects must be assigned to in order to be rendered. |
| **Transparent Layer Mask** | The layers that transparent GameObjects must be assigned to in order to be rendered. |
### Rendering
This section contains properties related to rendering.
| Property | Description |
| --- | --- |
| **Rendering Path** | Select the Rendering Path. Options:  * **Forward**: The Forward Rendering Path. * **Forward+**: The [Forward+ Rendering Path](rendering/forward-rendering-paths.html). * **Deferred**: The [Deferred Rendering Path](rendering/deferred-rendering-path-landing.html). * **Deferred+**: The [Deferred+ Rendering Path](rendering/deferred-rendering-path-landing.html) |
| **Depth Priming Mode** | Skips drawing overlapping pixels, to speed up rendering. Unity uses the depth texture to check which pixels overlap. The rendering improvement depends on the number of overlapping pixels and the complexity of the pixel shaders.  **Note**: If you use custom shaders, Unity renders opaque objects as invisible unless you add passes with `DepthOnly` and `DepthNormals` tags. For more information, refer to [Write depth only in a shader](writing-shaders-urp-depth-only.html).  The options are:  * **Disabled**: Doesn’t perform depth priming. * **Auto**: Performs depth priming only if a depth prepass already exists in the render pipeline. This setting isn’t supported on Android, iOS and Apple TV platforms. * **Forced**: Adds a depth prepass to the render pipeline if it doesn’t already exist, and performs depth priming. Adding the depth prepass has an impact on memory and performance.  **Note**: Depth priming isn’t supported if you use a [deferred rendering path](rendering/deferred-rendering-path-landing.html) or [Multisample Anti-aliasing](anti-aliasing.html#multisample-anti-aliasing-msaa), or at runtime on mobile devices that use tile-based deferred rendering (TBDR). |
| **Accurate G-buffer normals** | Indicates whether to use a more resource-intensive normal encoding/decoding method to improve visual quality.  This property is available only if **Rendering Path** is set to **Deferred**. |
| **Depth Texture Mode** | Specifies the stage in the render pipeline at which to copy the scene depth to a depth texture. The options are:  * **After Opaques**: URP copies the scene depth after the opaques render pass. * **After Transparents**: URP copies the scene depth after the transparents render pass. * **Force Prepass**: URP does a depth prepass to generate the scene depth texture.  **Note**: On mobile devices, the **After Transparents** option can lead to a significant improvement in memory bandwidth. This is because the Copy Depth pass causes a switch in render target between the Opaque pass and the Transparents pass. When this occurs, Unity stores the contents of the Color Buffer in the main memory, and then loads it again once the Copy Depth pass is complete. The impact increases significantly when MSAA is enabled as Unity must also store and load the MSAA data alongside the Color Buffer. |
### Native RenderPass
This section contains properties related to URP’s Native RenderPass API.
| Property | Description |
| --- | --- |
| **Native RenderPass** | Indicates whether to use URP’s Native RenderPass API. When enabled, URP uses this API to structure render passes. As a result, you can use [programmable blending](https://docs.unity3d.com/Manual/SL-PlatformDifferences.html#using-shader-framebuffer-fetch) in custom URP shaders. For more information about the RenderPass API, refer to [ScriptableRenderContext.BeginRenderPass](https://docs.unity3d.com/ScriptReference/Rendering.ScriptableRenderContext.BeginRenderPass.html).  **Note**: Enabling this property has no effect on OpenGL ES. |
### Shadows
This section contains properties related to rendering shadows.
| Property | Description |
| --- | --- |
| **Transparent Receive Shadows** | When this option is on, Unity draws shadows on transparent objects. |
### Post-processing
| **Property** | **Description** |
| --- | --- |
| **Enabled** | Enables **post-processing**A process that improves product visuals by applying filters and effects before the image appears on screen. You can use post-processing effects to simulate physical camera and film properties, for example Bloom and Depth of Field. [More info](../PostProcessingOverview.html) post processing, postprocessing, postprocess See in [Glossary](../Glossary.html#post-processing) effects in your **scene**A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](../CreatingScenes.html) See in [Glossary](../Glossary.html#Scene). If disabled, Unity excludes post-processing renderer passes, **shaders**A program that runs on the GPU. [More info](../Shaders.html) See in [Glossary](../Glossary.html#shader), and textures from the build. |
| **Data** | Selects the asset that the renderer uses for post-processing. This property is available only when **Enabled** is enabled. |
### Overrides
This section contains **Render Pipeline**A series of operations that take the contents of a Scene, and displays them on a screen. Unity lets you choose from pre-built render pipelines, or write your own. [More info](../render-pipelines.html)
See in [Glossary](../Glossary.html#renderpipeline) properties that this Renderer overrides.
#### Stencil
With this check box selected, the Renderer processes the **Stencil buffer**A memory store that holds an 8-bit per-pixel value. In Unity, you can use a stencil buffer to flag pixels, and then only render to pixels that pass the stencil operation. [More info](../class-RenderTexture.html)
See in [Glossary](../Glossary.html#stencilbuffer) values.
![URP Universal Renderer Stencil override](../../uploads/urp/urp-assets/urp-universal-renderer-stencil-on.png)
URP Universal Renderer Stencil override
For more information on how Unity works with the Stencil buffer, refer to [ShaderLab: Stencil](https://docs.unity3d.com/Manual/SL-Stencil.html).
In URP, you can use bits 0 to 3 of the stencil buffer for custom rendering effects. This means you can use stencil indices 0 to 15.
### Compatibility
This section contains settings related to backwards compatibility.
| Property | Description |
| --- | --- |
| **Intermediate Texture** | This property lets you force URP to renders via an intermediate texture. Options:  * **Auto**: URP uses the information provided by the `ScriptableRenderPass.ConfigureInput` method to determine automatically whether rendering via an intermediate texture is necessary. * **Always**: forces rendering via an intermediate texture. Use this option only for compatibility with Renderer Features that do not declare their inputs with `ScriptableRenderPass.ConfigureInput`. Using this option might have a significant performance impact on some platforms. |
### Renderer Features
This section contains the list of Renderer Features assigned to the selected Renderer.
For information on how to add a Renderer Feature, check [How to add a Renderer Feature to a Renderer](urp-renderer-feature.html).
URP contains the pre-built Renderer Feature called [Render Objects](renderer-features/renderer-feature-render-objects.html).