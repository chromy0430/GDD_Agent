--- 
Source: Unity 6 URP Manual (cameras-multiple.html)
---

# Multiple cameras in URP
![An example of the effect camera stacking can produce in URP](../../uploads/urp/camera-stacking-example.png)
An example of the effect camera stacking can produce in URP
Resources and approaches for using multiple cameras to work with multiple **camera**A component which creates an image of a particular viewpoint in your scene. The output is either drawn to the screen or captured as a texture. [More info](../CamerasOverview.html)
See in [Glossary](../Glossary.html#Camera) outputs and targets in the Universal **Render Pipeline**A series of operations that take the contents of a Scene, and displays them on a screen. Unity lets you choose from pre-built render pipelines, or write your own. [More info](../render-pipelines.html)
See in [Glossary](../Glossary.html#renderpipeline) (URP).
**Note:** If you use multiple cameras, it might make rendering slower. An active camera runs through the entire rendering loop even if it renders nothing.
| Page | Description |
| --- | --- |
| [Camera stacking](cameras/camera-stacking-concepts.html) | Learn about the fundamental concepts of camera stacking. |
| [Set up a camera stack](camera-stacking.html) | Stack cameras to layer the outputs of multiple cameras into a single combined output. |
| [Add and remove cameras in a camera stack](cameras/add-and-remove-cameras-in-a-stack.html) | Add, remove, and reorder cameras within a camera stack. |
| [Set up split-screen rendering](rendering-to-the-same-render-target.html) | Render multiple camera outputs to a single render target to create effects such as split screen rendering. |
| [Apply different post processing effects to separate cameras](cameras/apply-different-post-proc-to-cameras.html) | Apply different **post-processing**A process that improves product visuals by applying filters and effects before the image appears on screen. You can use post-processing effects to simulate physical camera and film properties, for example Bloom and Depth of Field. [More info](../PostProcessingOverview.html) post processing, postprocessing, postprocess See in [Glossary](../Glossary.html#post-processing) setups to individual cameas within a **scene**A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](../CreatingScenes.html) See in [Glossary](../Glossary.html#Scene). |
| [Render a camera’s output to a Render Texture](rendering-to-a-render-texture.html) | Render to a **Render Texture**A special type of Texture that is created and updated at runtime. To use them, first create a new Render Texture and designate one of your Cameras to render into it. Then you can use the Render Texture in a Material just like a regular Texture. [More info](../class-RenderTexture.html) See in [Glossary](../Glossary.html#RenderTexture) to create effects such as in-game CCTV monitors. |
| [Create a render request](User-Render-Requests.html) | Trigger a camera to render to a Render Texture outside of URP rendering loop. |
## Additional resources
* [Multiple cameras](../MultipleCameras-landing.html)
* [Camera render types in URP](camera-types-and-render-type.html)
* [Camera render order in URP](cameras-advanced.html)