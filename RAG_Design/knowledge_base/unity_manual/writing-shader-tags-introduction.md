--- 
Source: Unity 6 Manual (writing-shader-tags-introduction.md)
---

# Set the render pipeline and render order for a shader
To set the **render pipeline**A series of operations that take the contents of a Scene, and displays them on a screen. Unity lets you choose from pre-built render pipelines, or write your own. [More info](render-pipelines.html)
See in [Glossary](Glossary.html#renderpipeline) and render order for a subshader or a **shader**A program that runs on the GPU. [More info](Shaders.html)
See in [Glossary](Glossary.html#shader) pass, add a `Tag` block.
## Add a tag
Add a `Tag` block to a `SubShader` block or a `Pass` block. For example:
```
Shader "TagsExample"
{
    SubShader
    {
        // Add a subshader tag
        Tags { "TagName" = "Value" }
        Pass
        {
            // Add a pass tag
            Tags { "TagName" = "Value" }
            ...
        }
    }
}
```
For more information about tag names and values, refer to [`SubShader` tags in ShaderLab reference](SL-SubShaderTags.html) and [`Pass` tags in ShaderLab reference](SL-PassTags.html). Not all `Tag` blocks are compatible with both subshaders and passes.
You can also add your own custom tags and read them from a C# script.
## Set the render pipeline
To make a subshader compatible with the Universal Render Pipeline (URP) or the High Definition Render Pipeline (HDRP), add a `RenderPipeline` tag to the `SubShader` block:
* For URP, use `"RenderPipeline" = "UniversalPipeline"`
* For HDRP, use `"RenderPipeline" = "HDRenderPipeline"`
## Set the render order
Unity uses two tags to determine when to execute a shader:
* `LightMode` tag: Sets which stage of the render pipeline a shader pass runs during. For example, drawing opaque geometry, or drawing **post-processing**A process that improves product visuals by applying filters and effects before the image appears on screen. You can use post-processing effects to simulate physical camera and film properties, for example Bloom and Depth of Field. [More info](PostProcessingOverview.html) post processing, postprocessing, postprocess
  See in [Glossary](Glossary.html#post-processing) effects.
* `Queue` tag: Sets which group of objects a subshader belongs to. Unity draws each render queue in a specific order.
Each `LightMode` stage usually renders a specific `Queue` range. Unity warns you if you use a `Queue` tag that the `LightMode` stage doesn’t render.
**Note:** The `LightMode` tag isn’t related to the [light mode](LightModes-introduction.html)A Light property that defines the use of the Light. Can be set to Realtime, Baked and Mixed. [More info](LightModes.html)
See in [Glossary](Glossary.html#LightMode) parameter in the **Inspector**A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](UsingTheInspector.html)
See in [Glossary](Glossary.html#Inspector) window of a Light component.
### Set the `LightMode` tag
Add a `LightMode` tag to the `Pass` block. For example, to execute the shader during the **forward rendering**A rendering path that renders each object in one or more passes, depending on lights that affect the object. Lights themselves are also treated differently by Forward Rendering, depending on their settings and intensity. [More info](RenderTech-ForwardRendering.html)
See in [Glossary](Glossary.html#ForwardRendering) pass in the Universal Render Pipeline (URP) that renders the `Geometry` queue, use `Tags { "LightMode" = "UniversalForward" }`.
For a list of `LightMode` values, refer to [`LightMode` tag valid values](SL-PassTags.html#lightmode-tag) and [ShaderLab `Pass` tags in URP reference](urp/urp-shaders/urp-shaderlab-pass-tags.html).
To enable or disable a shader pass by its `LightMode` tag, use the [`Material.SetShaderPassEnabled`](../ScriptReference/Material.SetShaderPassEnabled.html) API.
### Set the Queue tag
Add a `Queue` tag to the `SubShader` block. Use one of the following approaches:
* To add the subshader to a queue, use `"Queue" = "RenderQueueName"`. For example `"Queue" = "Transparent"`.
* To add the subshader before or after a queue, use `"Queue" = "RenderQueueName-Offset"` or `"Queue" = "RenderQueueName+Offset"`. For example, `"Queue" = "Geometry+1"`.
You can also use queue values instead of names. For example, `"Queue" = "3000"` instead of `"Queue" = "Transparent"`, or `"Queue" = "2001"` instead of `"Queue" = "Geometry+1"`.
You can also set the queue in the [**Inspector** window of the material](class-Material.html) using the **Render Queue** property, or in a C# script using the [`Material.renderQueue`](../ScriptReference/Material-renderQueue.html) API.
For more information, refer to [Render queues and sorting behaviours](built-in-rendering-order.html).
## Check tags
To read tags from a C# script, use the following:
* To read a subshader tag, use the [`Material.GetTag`](../ScriptReference/Material.GetTag.html) API.
* To read a pass tag, use the [`Shader.FindPassTagValue`](../ScriptReference/Shader.FindPassTagValue.html) API.
* To read a `Queue` tag, use the [`Shader.renderQueue`](../ScriptReference/Shader-renderQueue.html) API.
## Additional resources
* [SubShader tags in ShaderLab reference](SL-SubShaderTags.html)
* [Pass tags in ShaderLab reference](SL-PassTags.html)