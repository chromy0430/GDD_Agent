--- 
Source: Unity 6 URP Manual (customize\blit-overview.html)
---

# Blit in URP
To **blit**A shorthand term for “bit block transfer”. A blit operation is the process of transferring blocks of data from one place in memory to another.
See in [Glossary](../../Glossary.html#blit) from one texture to another in a custom render pass in the Universal **Render Pipeline**A series of operations that take the contents of a Scene, and displays them on a screen. Unity lets you choose from pre-built render pipelines, or write your own. [More info](../../render-pipelines.html)
See in [Glossary](../../Glossary.html#renderpipeline) (URP), use the following:
* The `AddBlitPass` API in the render graph system. For more information, refer to [Blit using the render graph system](../render-graph-blit.html).
* The [Blitter API](https://docs.unity3d.com/Packages/com.unity.render-pipelines.core@latest?subfolder=/api/UnityEngine.Rendering.Blitter.html) from the Core Scriptable Render Pipeline (SRP).
The **shader**A program that runs on the GPU. [More info](../../Shaders.html)
See in [Glossary](../../Glossary.html#shader) you use with the `Blitter` API must be a hand-coded shader. [Shader Graph](../../shader-graph.html) shaders aren’t compatible with the `Blitter` API.
**Note:** Don’t use the `CommandBuffer.Blit` or `Graphics.Blit` APIs, or APIs that use them internally such as `RenderingUtils.Blit`. These APIs might break **XR**An umbrella term encompassing Virtual Reality (VR), Augmented Reality (AR) and Mixed Reality (MR) applications. Devices supporting these forms of interactive applications can be referred to as XR devices. [More info](../../XR.html)
See in [Glossary](../../Glossary.html#XR) rendering, and aren’t compatible with native render passes.
For example in the `Execute` function in a render pass, add the following:
```
{
    Blitter.BlitCameraTexture(commandBuffer, sourceTexture, destinationTexture, materialToUse, passNumber);
}
```
You can also use the [`AddBlitPass`](https://docs.unity3d.com/Packages/com.unity.render-pipelines.core@17.3/api/UnityEngine.Rendering.RenderGraphModule.Util.RenderGraphUtils.html#UnityEngine_Rendering_RenderGraphModule_Util_RenderGraphUtils_AddBlitPass_UnityEngine_Rendering_RenderGraphModule_RenderGraph_UnityEngine_Rendering_RenderGraphModule_TextureHandle_UnityEngine_Rendering_RenderGraphModule_TextureHandle_UnityEngine_Vector2_UnityEngine_Vector2_System_Int32_System_Int32_System_Int32_System_Int32_System_Int32_System_Int32_UnityEngine_Rendering_RenderGraphModule_Util_RenderGraphUtils_BlitFilterMode_System_String_System_Boolean_) or [`AddCopyPass`](https://docs.unity3d.com/Packages/com.unity.render-pipelines.core@17.3/api/UnityEngine.Rendering.RenderGraphModule.Util.RenderGraphUtils.html#UnityEngine_Rendering_RenderGraphModule_Util_RenderGraphUtils_AddCopyPass_UnityEngine_Rendering_RenderGraphModule_RenderGraph_UnityEngine_Rendering_RenderGraphModule_TextureHandle_UnityEngine_Rendering_RenderGraphModule_TextureHandle_System_Int32_System_Int32_System_Int32_System_Int32_System_String_) APIs in your `RecordRenderGraph` method to blit or copy textures. For example:
```
using UnityEngine.Rendering.RenderGraphModule.Util;
...
    public override void RecordRenderGraph(RenderGraph renderGraph, ContextContainer frameData) {
        // Set up the source texture, destination texture, material, and shader pass number for the blit
        RenderGraphUtils.BlitMaterialParameters parameters = new(sourceTexture, destinationTexture, materialToUse, passNumber);
        // Add the blit pass
        renderGraph.AddBlitPass(parameters, passName: "My Blit Pass");
    }
```
## Examples
For full examples of using the `Blitter`, `AddBlitPass`, and `AddCopyPass` APIs, follow these steps:
1. Import the URP render graph samples. For more information, refer to [Importing a package sample in URP](../package-sample-urp-package-samples.html).
2. In the **Project** window, go to **Samples** > **Universal Render Pipeline** > **17.3.0** > **URP RenderGraph Samples**.
3. Open **Blit**, **BlitWithFrameData**, or **BlitWithMaterial**.
## Additional resources
* [Custom render pass workflow](../renderer-features/custom-rendering-pass-workflow-in-urp.html)
* [Textures in the Render Graph system](../working-with-textures.html)