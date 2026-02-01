--- 
Source: Unity 6 Manual (UpgradeGuideUnity62.md)
---

# Upgrade to Unity 6.2
This page lists changes in Unity 6.2 that can affect existing projects when you upgrade them from Unity 6.1 to Unity 6.2.
Review changes for Unity 6.2 in these areas:
* [Graphics](#graphics)
* [UI Toolkit](#ui-toolkit)
## Graphics
This section outlines recent updates to Unity’s graphics systems that can affect your upgrade experience.
### Select shader APIs are now deprecated
Unity 6.2 deprecates a set of **shader**A program that runs on the GPU. [More info](Shaders.html)
See in [Glossary](Glossary.html#shader) APIs that are superseded by more recent APIs. Refer to the [6.2 release notes](https://unity.com/releases/editor/whats-new/6000.2.0) for the full list of deprecated APIs and the APIs to replace them with. The deprecated APIs will be removed in a future release.
### Change to AfterRendering injection point timing in URP
The `AfterRendering` injection point now always executes after the final **blit**A shorthand term for “bit block transfer”. A blit operation is the process of transferring blocks of data from one place in memory to another.
See in [Glossary](Glossary.html#blit) to the back buffer. In previous Unity versions, `AfterRendering` sometimes executes before the final blit, if, for example, an effect like Fast Approximate Anti-Aliasing (FXAA) or an upscaler requires an additional final **post-processing**A process that improves product visuals by applying filters and effects before the image appears on screen. You can use post-processing effects to simulate physical camera and film properties, for example Bloom and Depth of Field. [More info](PostProcessingOverview.html) post processing, postprocessing, postprocess
See in [Glossary](Glossary.html#post-processing) render pass.
To preserve the old behavior and continue rendering into an intermediate texture rather than the back buffer, change the event in your custom render pass from `AfterRendering` to `AfterRenderingPostProcessing`. This avoids further changes such as handling y-flips. The change is backward-compatible, so you can apply it to Unity 6.0 and later to maintain compatibility across all Unity 6 versions.
### SetupRenderPasses is deprecated in URP
The `SetupRenderPasses` API is now deprecated in the Universal **Render Pipeline**A series of operations that take the contents of a Scene, and displays them on a screen. Unity lets you choose from pre-built render pipelines, or write your own. [More info](render-pipelines.html)
See in [Glossary](Glossary.html#renderpipeline) (URP). This API will be removed in a future release.
If your project contains Scriptable Renderer Features that use `SetupRenderPasses`, rewrite them using the render graph system and the `AddRenderPasses` API. For more information, refer to [Render graph system](urp/render-graph.html).
For compatibility purposes, Unity 6 includes the option to disable the render graph system and use the **rendering path**The technique that a render pipeline uses to render graphics. Choosing a different rendering path affects how lighting and shading are calculated. Some rendering paths are more suited to different platforms and hardware than others. [More info](RenderingPaths.html)
See in [Glossary](Glossary.html#renderingpath) from previous URP versions. Unity no longer develops or improves this rendering path. For more information, refer to [Compatibility Mode](urp/compatibility-mode).
## UI Toolkit
This section outlines recent updates to Unity’s UI Toolkit that can affect your upgrade experience.
### VisualElement.transform API deprecated
The [VisualElement.transform](../ScriptReference/UIElements.VisualElement-transform.html) API has been deprecated.
To set values, use:
* [VisualElement.style.translate](../ScriptReference/UIElements.IStyle-translate.html)
* [VisualElement.style.rotate](../ScriptReference/UIElements.IStyle-rotate.html)
* [VisualElement.style.scale](../ScriptReference/UIElements.IStyle-scale.html)
To read values, use:
* [VisualElement.resolvedStyle.translate](../ScriptReference/UIElements.IResolvedStyle-translate.html)
* [VisualElement.resolvedStyle.rotate](../ScriptReference/UIElements.IResolvedStyle-rotate.html)
* [VisualElement.resolvedStyle.scale](../ScriptReference/UIElements.IResolvedStyle-scale.html)