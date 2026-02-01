--- 
Source: Unity 6 Manual (built-in-render-pipeline.md)
---

# Using the Built-In Render Pipeline
![A scene from Adam, a short film created with the Built-In Render Pipeline. A robot studies its hand and arm.](../uploads/Main/Adam.jpg)
A scene from [Adam](https://unity.com/demos/adam), a short film created with the Built-In Render Pipeline. A robot studies its hand and arm.
Unity’s Built-in Render Pipeline is Unity’s older render pipeline. It’s not based on the Scriptable Render Pipeline, but you can configure it by choosing between different [rendering paths](RenderingPaths.html)The technique that a render pipeline uses to render graphics. Choosing a different rendering path affects how lighting and shading are calculated. Some rendering paths are more suited to different platforms and hardware than others. [More info](RenderingPaths.html)
See in [Glossary](Glossary.html#renderingpath), and extend its functionality with [command buffers](GraphicsCommandBuffers.html) and [callbacks](./execution-order.html).
| **Page** | **Description** |
| --- | --- |
| [Hardware requirements](RenderTech-HardwareRequirements.html) | Learn about general hardware requirements for the Built-In Render Pipeline, and requirements for realtime shadows, **post-processing**A process that improves product visuals by applying filters and effects before the image appears on screen. You can use post-processing effects to simulate physical camera and film properties, for example Bloom and Depth of Field. [More info](PostProcessingOverview.html) post processing, postprocessing, postprocess See in [Glossary](Glossary.html#post-processing) effects, and higher **shader**A program that runs on the GPU. [More info](Shaders.html) See in [Glossary](Glossary.html#shader) models. |
| [Graphics quality settings](built-in-graphics-quality-settings.html) | Resources for understanding and configuring graphics tiers in the Built-In Render Pipeline. |
| [Rendering paths](built-in-rendering-paths.html) | Resources for choosing between the Forward, Deferred and Legacy Vertex Lit rendering paths in the Built-In Render Pipeline. |
| [Custom rendering](GraphicsCommandBuffers-landing.html) | Resources for using the `CommandBuffer` API to schedule and execute rendering commands at various points in the Built-In Render Pipeline. |
## Additional resources
* [Render pipelines](render-pipelines.html)A series of operations that take the contents of a Scene, and displays them on a screen. Unity lets you choose from pre-built render pipelines, or write your own. [More info](render-pipelines.html)
  See in [Glossary](Glossary.html#renderpipeline)
* [Choosing a render pipeline](choose-a-render-pipeline-landing.html)
* [Upgrade to URP from the Built-In Render Pipeline](urp/upgrading-from-birp.html)
* [Graphics quality settings in URP](urp/urp-quality-settings-landing.html)