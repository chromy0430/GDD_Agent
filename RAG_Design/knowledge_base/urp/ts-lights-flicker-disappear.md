--- 
Source: Unity 6 URP Manual (ts-lights-flicker-disappear.html)
---

# Troubleshooting lights flickering or disappearing
Fix issues causing lights to flicker or disappear, and causing objects to not cast shadows.
![Two images of the same scene of a room containing a 3 by 3 grid of spheres. The first image displays how there are no shadows or specular highlights when the pixel light count set to zero. The second image shows the same scene with the pixel light count set to nine, with the spheres casting shadows.](../../uploads/Main/ex-light-flicker.png)
Two images of the same scene of a room containing a 3 by 3 grid of spheres. The first image displays how there are no shadows or specular highlights when the pixel light count set to zero. The second image shows the same scene with the pixel light count set to nine, with the spheres casting shadows.
## Symptoms
Real-time lights and specular highlights are missing or flicker in the **scene**A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](../CreatingScenes.html)
See in [Glossary](../Glossary.html#Scene), and also cause objects to not cast shadows.
## Cause
When you use the [Forward rendering path](../RenderTech-ForwardRendering.html), Unity converts **pixel**The smallest unit in a computer image. Pixel size depends on your screen resolution. Pixel lighting is calculated at every screen pixel. [More info](../ShadowPerformance.html)
See in [Glossary](../Glossary.html#pixel) lights to more performant vertex lights when the number of pixel lights exceeds a certain value. This can result in flickering or disappearing lights in the scene.
**Note:** This limitation affects only the Built-in **Render Pipeline**A series of operations that take the contents of a Scene, and displays them on a screen. Unity lets you choose from pre-built render pipelines, or write your own. [More info](../render-pipelines.html)
See in [Glossary](../Glossary.html#renderpipeline) and the Universal Render Pipeline (URP). When you use the High Definition Render Pipeline (HDRP), Unity doesn’t convert pixel lights to vertex lights.
## Resolution - Adjust the Render Mode property
![Light component in URP.](../../uploads/Main/ex-ts-render-mode-property.png)
Light component in URP.
To control the probability of Unity converting a light into a vertex light, you can adjust their **Render Mode** priority in the **Light** component property settings.
For lights of high importance, set its **Render Mode** to **Important** to reduce the probability of Unity converting the selected lights to vertex lights. When **Render Mode** is set to **Auto**, Unity will check the light’s intensity and its relative distance from the **camera**A component which creates an image of a particular viewpoint in your scene. The output is either drawn to the screen or captured as a texture. [More info](../CamerasOverview.html)
See in [Glossary](../Glossary.html#Camera) before converting it.
Lights which have **Render Mode** set to **Not Important** will always be converted to vertex lights.
## Resolution - Switch to a different rendering path
If you need many [mixed](../LightModes-introduction.md#mixed) or [real-time](../LightModes-introduction.md#realtime) lights in the scene, switch to a different **rendering path**The technique that a render pipeline uses to render graphics. Choosing a different rendering path affects how lighting and shading are calculated. Some rendering paths are more suited to different platforms and hardware than others. [More info](../RenderingPaths.html)
See in [Glossary](../Glossary.html#renderingpath) that supports more lights.
If you’re using the Built-in Render Pipeline, follow these steps:
1. Go to **Project Settings** > **Graphics**.
2. Under [Tier Settings](../class-GraphicsSettings.md#Tier), disable the **Use Defaults** checkbox for your selected [graphics tier](../graphics-tiers.html).
3. Set the **Rendering Path** to [Deferred](rendering/deferred-rendering-path-landing.html).
If you’re using the Universal Rendering pipeline (URP):
1. Select the [Render Pipeline Asset](https://docs.unity3d.com/Packages/com.unity.render-pipelines.universal@latest?subfolder=/manual/universalrp-asset.html).
2. Under **Rendering**, set the **Rendering Path** to [Forward+](rendering/forward-rendering-paths.html) or [Deferred](rendering/deferred-rendering-path-landing.html) depending on the rendering path that [best fits](rendering-paths-comparison.html) your project needs.
## Resolution - Switch to baked lights
To mitigate pixel light limitations, use **baked lights**Light components whose Mode property is set to Baked. Unity pre-calculates the illumination from Baked Lights before runtime, and does not include them in any runtime lighting calculations. [More info](../LightModes-introduction.html#baked)
See in [Glossary](../Glossary.html#bakedlights). Go to the [Light](../class-Light.html) component and set its **Mode** to **Baked**.