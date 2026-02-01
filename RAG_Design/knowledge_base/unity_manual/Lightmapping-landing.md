--- 
Source: Unity 6 Manual (Lightmapping-landing.md)
---

# Precalculating surface lighting with lightmaps
Resources for improving performance by setting up Unity to do complicated lighting calculations ahead of time, either by baking **lightmaps**A pre-rendered texture that contains the effects of light sources on static objects in the scene. Lightmaps are overlaid on top of scene geometry to create the effect of lighting. [More info](Lightmapping.html)
See in [Glossary](Glossary.html#Lightmap) into a build or creating lightmaps at runtime.
| **Page** | **Description** |
| --- | --- |
| [Global illumination](choose-a-lighting-setup.html)A group of techniques that model both direct and indirect lighting to provide realistic lighting results. See in [Glossary](Glossary.html#globalillumination) | Learn about baking lightmaps before runtime, or creating lightmaps at runtime using **Enlighten**A lighting system by Geomerics used in Unity for Enlighten Realtime Global Illumination. [More info](https://www.siliconstudio.co.jp/en/products-service/enlighten/) See in [Glossary](Glossary.html#Enlighten) Realtime Global Illumination. |
| [Baking lightmaps before runtime](Lightmapping-baking-before-runtime.html) | Resources for precalculating the lit colors of **GameObjects**The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](class-GameObject.html) See in [Glossary](Glossary.html#GameObject) and storing them in textures called lightmaps. |
| [Update lightmaps at runtime with Enlighten Realtime Global Illumination](realtime-gi-using-enlighten-landing.html) | Resources for using Enlighten to precalculate visibility information, which Unity uses to create and update lightmaps at runtime. |
| [Configuring lightmapping](configure-lightmapping-settings.html) | Resources for choosing between baked and real-time lightmapping, and changing how GameObjects contribute to lightmaps. |