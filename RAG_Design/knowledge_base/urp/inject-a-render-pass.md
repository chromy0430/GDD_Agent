--- 
Source: Unity 6 URP Manual (inject-a-render-pass.html)
---

# Adding a Scriptable Render Pass to the frame rendering loop in URP
Add a custom render pass to the Universal **Render Pipeline**A series of operations that take the contents of a Scene, and displays them on a screen. Unity lets you choose from pre-built render pipelines, or write your own. [More info](../render-pipelines.html)
See in [Glossary](../Glossary.html#renderpipeline) (URP) frame rendering loop by creating a Scriptable Renderer Feature, or using the `RenderPipelineManager` API.
| Page | Description |
| --- | --- |
| [Inject a render pass using a Scriptable Renderer Feature](renderer-features/scriptable-renderer-features/inject-a-pass-using-a-scriptable-renderer-feature.html) | Write a class that inherits `ScriptableRendererFeature`, and use it to creates an instance of the custom render pass you created, and insert the custom render pass into the rendering pipeline. |
| [Inject a render pass using the RenderPipelineManager API](customize/inject-render-pass-via-script.html) | Use the `RenderPipelineManager` API to insert a custom render pass into the rendering pipeline. |
| [Restrict a render pass to a scene area](customize/restrict-render-pass-scene-area.html) | Enable a custom rendering effect only if the **camera**A component which creates an image of a particular viewpoint in your scene. The output is either drawn to the screen or captured as a texture. [More info](../CamerasOverview.html) See in [Glossary](../Glossary.html#Camera) is inside a volume in a **scene**A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](../CreatingScenes.html) See in [Glossary](../Glossary.html#Scene). |
| [Injection points reference](customize/custom-pass-injection-points.html) | URP contains multiple injection points that let you inject render passes at different points in the frame rendering loop. |
## Additional resources
* [Custom post-processing](post-processing/custom-post-processing.html)