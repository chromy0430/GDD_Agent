--- 
Source: Unity 6 URP Manual (Post-Processing-Film-Grain.html)
---

# Film Grain Volume Override reference for URP
![Scene with Film Grain effect turned off.](../../uploads/urp/post-proc/film-grain-off.png)
Scene with Film Grain effect turned off.
![Scene with Film Grain effect turned on.](../../uploads/urp/post-proc/film-grain.png)
Scene with Film Grain effect turned on.
The Film Grain effect simulates the random optical texture of photographic film, usually caused by small **particles**A small, simple image or mesh that is emitted by a particle system. A particle system can display and move particles in great numbers to represent a fluid or amorphous entity. The effect of all the particles together creates the impression of the complete entity, such as smoke. [More info](../class-ParticleSystem.html)
See in [Glossary](../Glossary.html#particle) being present on the physical film.
## Properties
| **Property** | **Description** |
| --- | --- |
| **Type** | Use the drop-down to select the type of grain to use. You can select from a list of presets that URP includes, or select **Custom** to provide your own grain Texture. |
| **Texture** | Assign a Texture that this effect uses as a custom grain Texture.This property is only available when **Type** is set to **Custom**. |
| **Intensity** | Use the slider to set the strength of the Film Grain effect. |
| **Response** | Use the slider to set the noisiness response curve. The higher you set this value, the less noise there is in brighter areas. |