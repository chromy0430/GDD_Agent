--- 
Source: Unity 6 Manual (visual-effects-haloes.md)
---

# Light halos
Strategies for creating glowing halos around light sources, to give the impression of small dust **particles**A small, simple image or mesh that is emitted by a particle system. A particle system can display and move particles in great numbers to represent a fluid or amorphous entity. The effect of all the particles together creates the impression of the complete entity, such as smoke. [More info](class-ParticleSystem.html)
See in [Glossary](Glossary.html#particle) in the air, and add atmosphere to your **scene**A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](CreatingScenes.html)
See in [Glossary](Glossary.html#Scene).
![A Light with a separate Halo Component](../uploads/Main/HaloWindow.jpg)
A Light with a separate Halo **Component**
| **Topic** | **Description** |
| --- | --- |
| [Create and configure a halo light effect](create-configure-halo.html) | Create and customize a halo around a light source. |
| [Halo component reference](class-Halo.html) | Explore the properties for the Halo component to customize the appearance of a halo. |
## Render pipeline information
How you work with light halos depends on the **render pipeline**A series of operations that take the contents of a Scene, and displays them on a screen. Unity lets you choose from pre-built render pipelines, or write your own. [More info](render-pipelines.html)
See in [Glossary](Glossary.html#renderpipeline) you use.
| **Feature name** | **Universal Render Pipeline (URP)** | **High Definition Render Pipeline (HDRP)** | **Built-in Render Pipeline** |
| --- | --- | --- | --- |
| **Halos** | Yes  Use a [Lens Flare (SRP) Data Asset](urp/shared/lens-flare/lens-flare-asset.html) and a [Lens Flare (SRP) component](urp/shared/lens-flare/lens-flare-component.html). | Yes  Use a [Lens Flare (SRP) Data Asset](https://docs.unity3d.com/Packages/com.unity.render-pipelines.high-definition@17.0/manual/shared/lens-flare/lens-flare-asset.html) and a [Lens Flare (SRP) component](https://docs.unity3d.com/Packages/com.unity.render-pipelines.high-definition@17.0/manual/shared/lens-flare/lens-flare-component.html), or a [Screen Space Lens Flare override](https://docs.unity3d.com/Packages/com.unity.render-pipelines.high-definition@17.0/manual/shared/lens-flare/Override-Screen-Space-Lens-Flare.html). | Yes  Use a [Halo component](class-Halo.html). |