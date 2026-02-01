--- 
Source: Unity 6 Manual (built-in-rendering-paths.md)
---

# Rendering paths in the Built-In Render Pipeline
Resources for choosing between the Forward, Deferred and Legacy Vertex Lit **rendering paths**The technique that a render pipeline uses to render graphics. Choosing a different rendering path affects how lighting and shading are calculated. Some rendering paths are more suited to different platforms and hardware than others. [More info](RenderingPaths.html)
See in [Glossary](Glossary.html#renderingpath) in the Built-In **Render Pipeline**A series of operations that take the contents of a Scene, and displays them on a screen. Unity lets you choose from pre-built render pipelines, or write your own. [More info](render-pipelines.html)
See in [Glossary](Glossary.html#renderpipeline).
| **Page** | **Description** |
| --- | --- |
| [Introduction to rendering paths](RenderingPaths.html) | Learn about how rendering paths have different capabilities and performance characteristics, and understand the difference between Forward, Deferred and Legacy Vertex Lit. |
| [Forward rendering path](RenderTech-ForwardRendering.html) | Understand the **Forward rendering**A rendering path that renders each object in one or more passes, depending on lights that affect the object. Lights themselves are also treated differently by Forward Rendering, depending on their settings and intensity. [More info](RenderTech-ForwardRendering.html) See in [Glossary](Glossary.html#ForwardRendering) path, which renders each **GameObject**The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](class-GameObject.html) See in [Glossary](Glossary.html#GameObject) in one or more passes, depending on the lights that affect the GameObject. |
| [Deferred rendering path](RenderTech-DeferredShading.html) | Understand the Deferred rendering path, which has no limit on the number of lights that can affect a GameObject. |
| [Legacy Vertex Lit rendering path](RenderTech-VertexLit.html) | Understand the Vertex Lit rendering path, which has the lowest lighting fidelity and no support for real-time shadows. |
## Additional resources
* [Introduction to render pipelines](render-pipelines-overview.html)
* [Rendering paths in the Universal Render Pipeline](urp/rendering-paths-landing.html)