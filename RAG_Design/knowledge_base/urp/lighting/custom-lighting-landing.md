--- 
Source: Unity 6 URP Manual (lighting\custom-lighting-landing.html)
---

# Custom lighting in URP
Implement custom lighting models to have more control over the visual style and achieve better performance.
| Page | Description |
| --- | --- |
| [Introduction to custom lighting in URP](custom-lighting-introduction.html) | An overview of approaches to implementing custom lighting. |
| [Render additional lights in a shader in URP](../use-built-in-shader-methods-additional-lights-fplus.html) | Create a light loop and iterate over additional lights in the Forward+ and Forward **rendering paths**The technique that a render pipeline uses to render graphics. Choosing a different rendering path affects how lighting and shading are calculated. Some rendering paths are more suited to different platforms and hardware than others. [More info](../../RenderingPaths.html) See in [Glossary](../../Glossary.html#renderingpath). |
| [Change how lights fade using light falloff in URP](custom-lighting-change-light-falloff.html) | Create a unique visual style in your **scene**A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](../../CreatingScenes.html) See in [Glossary](../../Glossary.html#Scene) by changing the light falloff function for real-time and baked lighting. |
## Additional resources
* [Use lighting in a custom URP shader](../use-built-in-shader-methods-lighting.html)
* [Use indirect lighting in a custom URP shader](../use-built-in-shader-methods-indirect-lighting.html)
* [Writing custom shaders](../writing-custom-shaders-urp.html)
* [Modify URP source code](../customize/modify-urp-source-code.html)
* [Upgrade custom shaders for URP compatibility](../urp-shaders/birp-urp-custom-shader-upgrade-guide.html)