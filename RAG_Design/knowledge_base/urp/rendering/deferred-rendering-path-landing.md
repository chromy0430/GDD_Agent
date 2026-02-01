--- 
Source: Unity 6 URP Manual (rendering\deferred-rendering-path-landing.html)
---

# Deferred and Deferred+ rendering paths in URP
![Scene rendered with the Deferred Rendering Path](../../../uploads/urp/rendering-deferred/deferred-intro-image.png)
Scene rendered with the Deferred Rendering Path
Resources for using the Deferred and Deferred+ rendering paths. The Deferred **rendering path**The technique that a render pipeline uses to render graphics. Choosing a different rendering path affects how lighting and shading are calculated. Some rendering paths are more suited to different platforms and hardware than others. [More info](../../RenderingPaths.html)
See in [Glossary](../../Glossary.html#renderingpath) has no limit on the number of lights that can affect an opaque **GameObject**The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](../../class-GameObject.html)
See in [Glossary](../../Glossary.html#GameObject), however the Deferred+ rendering path uses [Forward+](forward-rendering-paths.html) instead of Forward for the transparent pass and for the forward only opaque pass, and has the same light limit as Forward+.
| **Page** | **Description** |
| --- | --- |
| [Introduction to the Deferred rendering path](../rendering/deferred-rendering-path-introduction.html) | Learn about how the Deferred rendering path works, and its limitations. |
| [Render passes in the Deferred and Deferred+ rendering path](../rendering/render-passes-deferred.html) | Learn about the sequence of render pass events in the Deferred rendering path. |
| [G-buffer layout in the Deferred and Deferred+ rendering path](../rendering/g-buffer-layout.html) | Understand how Unity stores material attributes in the geometry buffer (G-buffer) in the Deferred rendering path. |
| [Enable accurate G-buffer normals in the Deferred and Deferred+ rendering path in URP](../rendering/accurate-g-buffer-normals.html) | Configure how Unity encodes normals when it stores them in the G-buffer. |
| [Make a shader compatible with the Deferred or Deferred+ rendering paths in URP](../rendering/make-shader-compatible-with-deferred.html) | Use the `LightMode` tag in a **shader**A program that runs on the GPU. [More info](../../Shaders.html) See in [Glossary](../../Glossary.html#shader) to make the shader compatible with the Deferred rendering path. |