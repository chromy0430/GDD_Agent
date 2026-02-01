--- 
Source: Unity 6 URP Manual (renderer-features\scriptable-renderer-features\inject-a-pass-using-a-scriptable-renderer-feature.html)
---

# Inject a render pass with a Scriptable Renderer Feature in URP
Use the `ScriptableRenderFeature` API to insert a [Scriptable Render Pass](../../renderer-features/intro-to-scriptable-render-passes.html) into the Universal **Render Pipeline**A series of operations that take the contents of a Scene, and displays them on a screen. Unity lets you choose from pre-built render pipelines, or write your own. [More info](../../../render-pipelines.html)
See in [Glossary](../../../Glossary.html#renderpipeline) (URP) frame rendering loop.
Follow these steps:
1. Create a new C# script.
2. Replace the code with a class that inherits from the `ScriptableRendererFeature` class.
   ```
   using UnityEngine;
   using UnityEngine.Rendering.Universal;
   public class MyRendererFeature : ScriptableRendererFeature
   {
   }
   ```
3. In the class, override the `Create` method. For example:
   ```
   public override void Create()
   {
   }
   ```
   URP calls the `Create` methods on the following events:
   * When the Scriptable Renderer Feature loads the first time.
   * When you enable or disable the Scriptable Renderer Feature.
   * When you change a property in the ****Inspector**A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](../../../UsingTheInspector.html)
     See in [Glossary](../../../Glossary.html#Inspector)** window of the Renderer Feature.
4. In the `Create` method, create an instance of your Scriptable Render Pass, and inject it into the renderer.
   For example, if you have a Scriptable Render Pass called `RedTintRenderPass`:
   ```
   // Define an instance of the Scriptable Render Pass
   private RedTintRenderPass redTintRenderPass;
   public override void Create()
   {
       // Create an instance of the Scriptable Render Pass
       redTintRenderPass = new RedTintRenderPass();
       // Inject the render pass after rendering the skybox
       redTintRenderPass.renderPassEvent = RenderPassEvent.AfterRenderingSkybox;
   }
   ```
   You can also use the `Create` method to initialize any other resources the Scriptable Renderer Feature needs, such as materials.
5. Override the `AddRenderPasses` method.
   ```
   public override void AddRenderPasses(ScriptableRenderer renderer, ref RenderingData renderingData)
   {
   }
   ```
   URP calls the `AddRenderPasses` method every frame, once for each **camera**A component which creates an image of a particular viewpoint in your scene. The output is either drawn to the screen or captured as a texture. [More info](../../../CamerasOverview.html)
   See in [Glossary](../../../Glossary.html#Camera). Don’t create or instantiate any resources within this method.
6. Use the `EnqueuePass` API to inject the Scriptable Render Pass into the frame rendering loop.
   ```
   public override void AddRenderPasses(ScriptableRenderer renderer, ref RenderingData renderingData)
   {
       renderer.EnqueuePass(redTintRenderPass);
   }
   ```
   To add a render pass to a specific camera only, use an `if` statement to check the camera type. For example:
   ```
   if (renderingData.cameraData.cameraType == CameraType.Game)
   {
       renderer.EnqueuePass(redTintRenderPass);
   }
   ```
You can now add the Scriptable Renderer Feature to the active URP asset. Refer to [How to add a Renderer Feature to a Renderer](../../urp-renderer-feature.html) for more information.
To dispose of any resources, override the [`Dispose`](https://docs.unity3d.com/Packages/com.unity.render-pipelines.universal@latest/index.html?subfolder=/api/UnityEngine.Rendering.Universal.ScriptableRendererFeature.html#UnityEngine_Rendering_Universal_ScriptableRendererFeature_Dispose) method.
## Example
For a complete example of a Scriptable Renderer Feature with a custom render pass that uses a material to **blit**A shorthand term for “bit block transfer”. A blit operation is the process of transferring blocks of data from one place in memory to another.
See in [Glossary](../../../Glossary.html#blit), follow these steps:
1. Import the URP render graph samples. For more information, refer to [Importing a package sample in URP](../../package-sample-urp-package-samples.html).
2. In the **Project** window, go to **Samples** > **Universal Render Pipeline** > <your version> > **URP RenderGraph Samples** > **BlitWithMaterial**.
## Additional resources
* [`ScriptableRendererFeature`](https://docs.unity3d.com/Packages/com.unity.render-pipelines.universal@latest/index.html?subfolder=/api/UnityEngine.Rendering.Universal.ScriptableRendererFeature.html)
* [Add a Renderer Feature to a URP Renderer](../../urp-renderer-feature.html)
* [Restrict a render pass to a scene area](../../customize/restrict-render-pass-scene-area.html)
* [Create a custom post-processing effect with Volume support in URP](../../post-processing/custom-post-processing-with-volume.html)
* [Custom render pass workflow in URP](../custom-rendering-pass-workflow-in-urp.html)
* [Render graph system](../../render-graph.html)