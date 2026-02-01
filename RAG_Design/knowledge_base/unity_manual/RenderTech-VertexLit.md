--- 
Source: Unity 6 Manual (RenderTech-VertexLit.md)
---

# Legacy Vertex Lit rendering path in the Built-In Render Pipeline
This page describes details of the Vertex Lit [rendering path](RenderingPaths.html)The technique that a render pipeline uses to render graphics. Choosing a different rendering path affects how lighting and shading are calculated. Some rendering paths are more suited to different platforms and hardware than others. [More info](RenderingPaths.html)
See in [Glossary](Glossary.html#renderingpath) in Unity’s Built-in **Render Pipeline**A series of operations that take the contents of a Scene, and displays them on a screen. Unity lets you choose from pre-built render pipelines, or write your own. [More info](render-pipelines.html)
See in [Glossary](Glossary.html#renderpipeline).
The Vertex Lit path generally renders each object in one pass, with lighting from all lights calculated for each vertex.
It’s the fastest rendering path and has the widest hardware support.
Since all lighting is calculated at the vertex level, this rendering path does not support most per-pixel effects: shadows, normal mapping, light cookies, and highly detailed specular highlights are not supported.