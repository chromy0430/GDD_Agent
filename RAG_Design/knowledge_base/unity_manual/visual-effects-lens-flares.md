--- 
Source: Unity 6 Manual (visual-effects-lens-flares.md)
---

# Lens flares
Resources and techniques for creating lens flares lighting effects, which can add atmosphere to your **scene**A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](CreatingScenes.html)
See in [Glossary](Glossary.html#Scene).
![Lens flare](../uploads/Main/srp-lens-flare.png)
Lens flare
| **Topic** | **Description** |
| --- | --- |
| [Introduction to lens flare effects](lens-flare-introduction.html) | Understand how Unity manages lens flares, which simulate the effect of lights refracting inside a **camera**A component which creates an image of a particular viewpoint in your scene. The output is either drawn to the screen or captured as a texture. [More info](CamerasOverview.html) See in [Glossary](Glossary.html#Camera) lens. |
| [Lens flares in URP](urp/shared/lens-flare/lens-flare.html) | Resources and techniques for creating and configuring lens flares in the Universal **Render Pipeline**A series of operations that take the contents of a Scene, and displays them on a screen. Unity lets you choose from pre-built render pipelines, or write your own. [More info](render-pipelines.html) See in [Glossary](Glossary.html#renderpipeline) (URP). |
| [Lens flares in the Built-In Render Pipeline](lens-flare-birp.html) | Resources and techniques for creating lens flares lighting effects in the Built-In Render Pipeline. |
## Render pipeline information
How you work with lens flare depends on the render pipeline you use.
| **Feature name** | **Universal Render Pipeline (URP)** | **High Definition Render Pipeline (HDRP)** | **Built-in Render Pipeline** |
| --- | --- | --- | --- |
| **Lens flares** | Yes  Use a [Lens Flare (SRP) Data Asset](urp/shared/lens-flare/lens-flare-asset.html) and a [Lens Flare (SRP) component](urp/shared/lens-flare/lens-flare-component.html), or a [Screen Space Lens Flare override](urp/shared/lens-flare/post-processing-screen-space-lens-flare.html). | Yes  Use a [Lens Flare (SRP) Data Asset](https://docs.unity3d.com/Packages/com.unity.render-pipelines.high-definition@17.0/manual/shared/lens-flare/lens-flare-asset.html) and a [Lens Flare (SRP) component](https://docs.unity3d.com/Packages/com.unity.render-pipelines.high-definition@17.0/manual/shared/lens-flare/lens-flare-component.html), or a [Screen Space Lens Flare override](https://docs.unity3d.com/Packages/com.unity.render-pipelines.high-definition@17.0/manual/shared/lens-flare/Override-Screen-Space-Lens-Flare). | Yes  Use a [Flare asset](class-Flare.html) and, optionally, a [Lens Flare component](class-LensFlare.html). |