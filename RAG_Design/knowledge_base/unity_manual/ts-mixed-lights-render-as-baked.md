--- 
Source: Unity 6 Manual (ts-mixed-lights-render-as-baked.md)
---

# Troubleshooting objects appearing unlit or darker than intended
Fix issues causing some objects to appear unlit or darker than intended.
![ Three images depicting the same scene of a room filled by a 3 by 3 grid of spheres, baked in Shadowmask Lighting Mode. The first image shows that some of the spheres are unlit and appear dark compared to others. The second image shows the same scene in the Light Overlap debug view to highlight overlapping lights in red. The third image shows the same scene in the Shadowmask debug view.](../uploads/Main/ex-mixed-lights-render-as-baked.png)
Three images depicting the same scene of a room filled by a 3 by 3 grid of spheres, baked in Shadowmask Lighting Mode. The first image shows that some of the spheres are unlit and appear dark compared to others. The second image shows the same scene in the Light Overlap debug view to highlight overlapping lights in red. The third image shows the same scene in the Shadowmask debug view.
## Symptoms
Mixed lights in the **scene**A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](CreatingScenes.html)
See in [Glossary](Glossary.html#Scene) are rendered as **baked lights**Light components whose Mode property is set to Baked. Unity pre-calculates the illumination from Baked Lights before runtime, and does not include them in any runtime lighting calculations. [More info](LightModes-introduction.html#baked)
See in [Glossary](Glossary.html#bakedlights) and some objects and areas in the scene appear unlit or darker than intended.
## Cause
This issue can occur when Unity converts mixed lights to baked lights during the lighting setup. Baked lights don’t provide real-time lighting, so they don’t illuminate dynamically in the scene. Instead, their contribution is baked into **lightmaps**A pre-rendered texture that contains the effects of light sources on static objects in the scene. Lightmaps are overlaid on top of scene geometry to create the effect of lighting. [More info](Lightmapping.html)
See in [Glossary](Glossary.html#Lightmap), **light probes**Light probes store information about how light passes through space in your scene. A collection of light probes arranged within a given space can improve lighting on moving objects and static LOD scenery within that space. [More info](LightProbes.html)
See in [Glossary](Glossary.html#LightProbe), or **reflection probes**A rendering component that captures a spherical view of its surroundings in all directions, rather like a camera. The captured image is then stored as a Cubemap that can be used by objects with reflective materials. [More info](class-ReflectionProbe.html)
See in [Glossary](Glossary.html#ReflectionProbe). If you don’t properly configure the baked lighting setup, objects may remain dark due to missing or incomplete lighting data during the bake process.
In [Shadowmask](lighting-mode.md#shadowmask)A shadowmask texture uses the same UV layout and resolution as its corresponding lightmap texture. [More info](lighting-mode.html#shadowmask)
See in [Glossary](Glossary.html#Shadowmask) Lighting Mode, only four mixed lights can overlap. Unity converts lights that exceed this limit into baked lights.
In [Subtractive](lighting-mode.md#subtractive) Lighting Mode, no lights (except for directional lights) cast real-time shadows. This is a limitation of this lighting mode.
When you use baked lighting, real-time adjustments (such as changing the light’s color, intensity, or position during runtime) are no longer possible, which may limit dynamic or interactive lighting effects in the scene and cause the objects to appear darker or lit in unintended ways.
## Resolution - Change the light placement and radius
To verify that light overlap exceeding the limit is the main issue, switch to the [Light Overlap](GIVis.md#light-overlap-baked-global-illumination-only) **Scene** view draw mode after generating lighting. This draw mode highlights overlapping lights in red so you can identify the number of overlapping lights.
Move the affected lights so that they no longer overlap. You can also adjust the **Range** or **Spot Angle** properties in the [Light](class-Light.html) component. Generate lighting again after making the changes to check if this fixes the issue.
## Resolution - Switch to a different Lighting Mode
Each [Lighting Mode](lighting-mode.html) has different advantages and limitations. If your project will be lit using a single directional light, then consider the **Subtractive** Lighting Mode instead of **Shadowmask**. Refer to [Lighting Modes](lighting-mode.html) to view the different limits and ways Unity calculates lighting for each mode.