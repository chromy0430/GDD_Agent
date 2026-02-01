--- 
Source: Unity 6 Manual (LightingOverview.md)
---

# Lighting
![A scene with photo-realistic lighting.](../uploads/Main/ProgressiveLightmapper-0.jpg)
A scene with photo-realistic lighting.
With Unity, you can achieve realistic lighting that is suitable for a range of art styles.
| **Page** | **Description** |
| --- | --- |
| [Introduction to lighting](LightingInUnity.html) | Resources for learning about lighting and choosing a lighting setup. |
| [Lighting configuration workflow](lighting-configuration-workflow.html) | Resources for selecting a **render pipeline**A series of operations that take the contents of a Scene, and displays them on a screen. Unity lets you choose from pre-built render pipelines, or write your own. [More info](render-pipelines.html) See in [Glossary](Glossary.html#renderpipeline), configuring global lighting settings, and adding lighting elements. |
| [Light sources](lighting-light-sources.html) | Resources for adding light to a **scene**A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](CreatingScenes.html) See in [Glossary](Glossary.html#Scene), with Light components, **ambient light**Light that doesn’t come from any specific direction, and contributes equal light in all directions to the Scene. [More info](lighting-window.html) See in [Glossary](Glossary.html#ambientlight), emissive materials, and cookies. |
| [Direct and indirect lighting](direct-and-indirect-lighting.html) | Resources on choosing whether Unity calculates **global illumination**A group of techniques that model both direct and indirect lighting to provide realistic lighting results. See in [Glossary](Glossary.html#globalillumination) in real time, or stores baked lighting in a build. |
| [Shadows](Shadows.html)A UI component that adds a simple outline effect to graphic components such as Text or Image. It must be on the same GameObject as the graphic component. [More info](https://docs.unity3d.com/Packages/com.unity.ugui@latest/index.html?subfolder=/manual/script-Shadow.html) See in [Glossary](Glossary.html#Shadow) | Techniques and resources for Lights casting shadows from a **GameObject**The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](class-GameObject.html) See in [Glossary](Glossary.html#GameObject) onto other parts of itself, or onto nearby GameObjects. |
| [Reflections](reflections-landing.html) | Techniques and resources for using **Reflection Probes**A rendering component that captures a spherical view of its surroundings in all directions, rather like a camera. The captured image is then stored as a Cubemap that can be used by objects with reflective materials. [More info](class-ReflectionProbe.html) See in [Glossary](Glossary.html#ReflectionProbe) to capture and display reflections on GameObjects. |
| [Lighting in URP](urp/lighting-landing.html) | Resources and approaches for lighting in the Universal Render Pipeline (URP). |
| [Lighting in the Built-In Render Pipeline](lighting-birp.html) | Resources and approaches for lighting in the Built-In Render Pipeline. |
| [Lighting reference](lighting-reference.html) | Explore lighting properties and settings, for example in the Lighting window, the Lighting Settings Asset, and Debug Draw Modes. |
## Additional resources and examples
* 👥 **Community**: [Join the conversation on Unity Discussions for Graphics](https://discussions.unity.com/lists/graphics)
* 📖 **E-Book**: [Introduction to the Universal Render Pipeline for advanced creators (Unity 6 edition)](https://unity.com/resources/introduction-to-urp-advanced-creators-unity-6?isGated=false)
* 📺 **Video**: [The URP 3D Sample - a short introduction](https://youtu.be/lg1W3Deoprg)
* 📺 **Video**: [Understanding URP settings and essentials](https://youtu.be/HCXCmHgV7Sk)
* 📚 **Documentation**: [Visual effects](visual-effects.html)