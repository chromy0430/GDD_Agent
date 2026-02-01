--- 
Source: Unity 6 URP Manual (working-with-textures.html)
---

# Textures in the Render Graph system in URP
How to access and use textures in custom render passes in the Universal **Render Pipeline**A series of operations that take the contents of a Scene, and displays them on a screen. Unity lets you choose from pre-built render pipelines, or write your own. [More info](../render-pipelines.html)
See in [Glossary](../Glossary.html#renderpipeline) (URP).
| Page | Description |
| --- | --- |
| [Read or write to a texture in a render pass](render-graph-read-write-texture.html) | Set a texture as an input or output for a render pass. |
| [Create a temporary texture for a single frame](render-graph-create-a-texture.html) | Create a temporary texture in a render pass, also known as an internal resource. |
| [Use a texture in multiple render passes](render-graph-pass-textures-between-passes.html) | Point render graph to an external texture, set a texture as a global texture, or add a texture to the frame data. |
## Additional resources
* [Use frame data](accessing-frame-data.html)
* The **blit**A shorthand term for “bit block transfer”. A blit operation is the process of transferring blocks of data from one place in memory to another.
  See in [Glossary](../Glossary.html#blit) examples in the [URP RenderGraph Samples](package-sample-urp-package-samples.html)