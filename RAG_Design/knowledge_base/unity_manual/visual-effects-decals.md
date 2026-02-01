--- 
Source: Unity 6 Manual (visual-effects-decals.md)
---

# Decals
Resources and techniques for projecting materials to act as decals that decorate the surface of other materials.
| **Topic** | **Description** |
| --- | --- |
| [Introduction to decals and projection](introduction-decals-projection.html) | Understand what decals are, how Unity uses projection to create them, and what you could use projection for. |
| [Decals in the Universal Render Pipeline](urp/renderer-feature-decal-landing.html) | Techniques for using a Decal Renderer Feature or a Decal Projector in the Universal **Render Pipeline**A series of operations that take the contents of a Scene, and displays them on a screen. Unity lets you choose from pre-built render pipelines, or write your own. [More info](render-pipelines.html) See in [Glossary](Glossary.html#renderpipeline) (URP). |
| [Decals in the Built-In Render Pipeline](decals-birp.html) | Techniques for using a Projector component in the Built-In Render Pipeline. |
## Render pipeline information
How you work with decals and projectors depends on the render pipeline you use.
| **Feature name** | **Built-in Render Pipeline** | **Universal Render Pipeline (URP)** | **High Definition Render Pipeline (HDRP)** |
| --- | --- | --- | --- |
| **Decal and projectors** | Yes  Use the [Projector component](class-Projector.html). | Yes  Use the [Decal Renderer Feature](urp/renderer-feature-decal.html). | Yes  Use the [Decal Projector](https://docs.unity3d.com/Packages/com.unity.render-pipelines.high-definition@17.0/manual/decals.html). |