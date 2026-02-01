--- 
Source: Unity 6 URP Manual (post-processing\custom-post-processing-with-volume.html)
---

# Create a custom post-processing effect with Volume support in URP
This page describes how to create a custom **post-processing**A process that improves product visuals by applying filters and effects before the image appears on screen. You can use post-processing effects to simulate physical camera and film properties, for example Bloom and Depth of Field. [More info](../../PostProcessingOverview.html) post processing, postprocessing, postprocess
See in [Glossary](../../Glossary.html#post-processing) effect with Volume support.
URP provides a template for custom post-processing effects. The implementation in the template consists of a Renderer Feature, where you can inject the code for the custom effect, and the script that implements the code for interacting with the Volume component.
To create an effect using the template, select the following menu item:
* **Assets** > **Create** > **Scripting** > **URP Post-process Volume Scripts**.
Unity creates two new **scripts**A piece of code that allows you to create your own Components, trigger game events, modify Component properties over time and respond to user input in any way you like. [More info](../../creating-scripts.html)
See in [Glossary](../../Glossary.html#Scripts) in the `Assets` folder: the script containing the Renderer Feature template and the Volume component script.
The template contains the example effect implementation that inverts colors on the screen.
In the Renderer Feature, in the `Create` method you define the custom Material for the custom effect or the render pass that implements the effect logic.
The Renderer Feature script contains the `ScriptableRenderPass` implementation.
You set the **shader**A program that runs on the GPU. [More info](../../Shaders.html)
See in [Glossary](../../Glossary.html#shader) properties for the custom effect in the following region in the render pass code:
```
#region PASS_SHARED_RENDERING_CODE
```
To set the effect properties on the volume component, modify the following line in the `AddRenderPasses` method:
```
NewPostProcessEffectVolumeComponent myVolume = VolumeManager.instance.stack?.GetComponent<NewPostProcessEffectVolumeComponent>();
if (myVolume == null || !myVolume.IsActive())
    s_SharedPropertyBlock.SetFloat("_Intensity", myVolume.intensity.value);
```
## Additional resources
* [Render graph system](../render-graph.html)
* [Inject a render pass using a Scriptable Renderer Feature](../customize/inject-render-pass-via-script.html)