--- 
Source: Unity 6 Manual (GraphicsCommandBuffers-landing.md)
---

# Custom rendering in the Built-In Render Pipeline
Resources for using the `CommandBuffer` API to schedule and execute rendering commands at various points in the Built-in **Render Pipeline**A series of operations that take the contents of a Scene, and displays them on a screen. Unity lets you choose from pre-built render pipelines, or write your own. [More info](render-pipelines.html)
See in [Glossary](Glossary.html#renderpipeline). This allows you to customize and extend Unity’s rendering functionality
| **Page** | **Description** |
| --- | --- |
| [Command buffer fundamentals](GraphicsCommandBuffers.html) | Understand how a `CommandBuffer` object holds a list of rendering commands that you can schedule and execute at various points in the Built-in Render Pipeline. |
| [CameraEvent and LightEvent events order reference](GraphicsCommandBuffers-order.html) | Explore the **camera**A component which creates an image of a particular viewpoint in your scene. The output is either drawn to the screen or captured as a texture. [More info](CamerasOverview.html) See in [Glossary](Glossary.html#Camera) and light events you can use to schedule rendering commands at a specific time. |
## Additional resources
* [Introduction to render pipelines](render-pipelines-overview.html)
* [Execute rendering commands in a Scriptable Render Pipeline](https://docs.unity3d.com/Packages/com.unity.render-pipelines.core@17.0/manual/srp-using-scriptable-render-context.html)
* [Custom rendering and post-processing in URP](urp/customizing-urp.html)