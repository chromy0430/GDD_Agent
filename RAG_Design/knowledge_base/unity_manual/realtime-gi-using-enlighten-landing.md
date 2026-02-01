--- 
Source: Unity 6 Manual (realtime-gi-using-enlighten-landing.md)
---

# Update lightmaps at runtime with Enlighten Realtime Global Illumination
Resources for using **Enlighten**A lighting system by Geomerics used in Unity for Enlighten Realtime Global Illumination. [More info](https://www.siliconstudio.co.jp/en/products-service/enlighten/)
See in [Glossary](Glossary.html#Enlighten) to precalculate visibility information, then update **lightmaps**A pre-rendered texture that contains the effects of light sources on static objects in the scene. Lightmaps are overlaid on top of scene geometry to create the effect of lighting. [More info](Lightmapping.html)
See in [Glossary](Glossary.html#Lightmap) at runtime.
| **Page** | **Description** |
| --- | --- |
| [Realtime Global Illumination using Enlighten](realtime-gi-using-enlighten.html) | Learn about when to use Enlighten Realtime **Global Illumination**A group of techniques that model both direct and indirect lighting to provide realistic lighting results. See in [Glossary](Glossary.html#globalillumination), and how it generates lightmaps. |
| [Enable Enlighten Realtime Global Illumination](realtime-gi-using-enlighten-use.html) | Enable realtime lightmaps in a **scene**A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](CreatingScenes.html) See in [Glossary](Glossary.html#Scene), and set whether specific light components contribute to indirect lighting. |
| [Optimize Enlighten Realtime Global Illumination](realtime-gi-using-enlighten-optimize.html) | Configure Enlighten Realtime Global Illumination to use less memory or CPU time. |
| [Level of detail (LOD) and Enlighten Realtime Global Illumination](LODRealtimeGI.html) | Learn about how Unity updates lightmaps for high and low detail models in the **level of detail**The *Level Of Detail* (LOD) technique is an optimization that reduces the number of triangles that Unity has to render for a GameObject when its distance from the Camera increases. [More info](LevelOfDetail.html) See in [Glossary](Glossary.html#levelofdetail) (LOD) system. |
| [Global Illumination Profiler module](ProfilerGI.html) | Reference for the Global Illumination Profiler module, which displays statistics about how much CPU time the Enlighten Realtime Global Illumination subsystem uses. |
## Additional resources
* [Configure lightmapping with a Lighting Settings Asset](global-illumination-configure.html)
* [Lighting Settings Asset Inspector window reference](class-LightingSettings.html)