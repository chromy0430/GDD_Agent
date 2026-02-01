--- 
Source: Unity 6 Manual (ts-missing-spec-response.md)
---

## Troubleshooting materials missing specular highlights
Fix issues causing specular highlights to be missing after baking **lightmaps**A pre-rendered texture that contains the effects of light sources on static objects in the scene. Lightmaps are overlaid on top of scene geometry to create the effect of lighting. [More info](Lightmapping.html)
See in [Glossary](Glossary.html#Lightmap).
![Two images of a rendered room with a sphere in the middle. The first image shows the sphere has several baked point lights that reflect on its surface. The second image shows the same scene after the lightmap is baked and the specular highlights in the first image are missing.](../uploads/Main/ex-missing-spec-response.png)
Two images of a rendered room with a sphere in the middle. The first image shows the sphere has several baked point lights that reflect on its surface. The second image shows the same scene after the lightmap is baked and the specular highlights in the first image are missing.
## Symptoms
Materials don’t appear glossy or have specular highlights when the lighting is baked.
## Cause
[Baked lights](LightModes-introduction.html#baked-light-behavior)Light components whose Mode property is set to Baked. Unity pre-calculates the illumination from Baked Lights before runtime, and does not include them in any runtime lighting calculations. [More info](LightModes-introduction.html#baked)
See in [Glossary](Glossary.html#bakedlights) don’t provide real-time specular response to materials. This means that glossy materials lack specular highlights after you generate lighting.
## Resolution - Use mixed lights
Use [mixed lights](LightModes-introduction.html#mixed)Light components whose Mode property is set to Mixed. Some calculations for Mixed Lights are performed in advance, and some calculations for Mixed Lights are performed at runtime. The behavior of all Mixed Lights in a Scene is determined by the Scene’s Lighting Mode. [More info](LightModes-landing.html)
See in [Glossary](Glossary.html#MixedLights) instead of baked lights, as mixed lights provide real-time direct specular response to materials. To use mixed lights, in the [Light](class-Light.html) component, set the ****Light Mode**A Light property that defines the use of the Light. Can be set to Realtime, Baked and Mixed. [More info](LightModes.html)
See in [Glossary](Glossary.html#LightMode)** property to **Mixed**.
## Resolution - Use emissive proxies
![Two images of a rendered room with a sphere in the middle. The first image shows the sphere with bake point lights, and emissive proxies captured by a reflection probe. The second image is a zoomed out perspective of the first, showing the emissive proxies are placed above the sphere.](../uploads/Main/ex-emissive-proxies.png)
Two images of a rendered room with a sphere in the middle. The first image shows the sphere with bake point lights, and emissive proxies captured by a reflection probe. The second image is a zoomed out perspective of the first, showing the emissive proxies are placed above the sphere.
Use emissive proxies to imitate the specular response from using emissive objects. To use emissive proxies, follow these steps:
1. Place a [reflection probe](class-ReflectionProbe.html)A rendering component that captures a spherical view of its surroundings in all directions, rather like a camera. The captured image is then stored as a Cubemap that can be used by objects with reflective materials. [More info](class-ReflectionProbe.html)
   See in [Glossary](Glossary.html#ReflectionProbe) in your **scene**A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](CreatingScenes.html)
   See in [Glossary](Glossary.html#Scene).
2. Right-click the **Hierarchy** panel and select **3D Object** > **Sphere**.
3. Select the newly created object and set its [Static Editor Flag](StaticObjects.html) to **Reflection Probe Static**.
4. Right-click the **Project** panel and select **Create** > **Material**.
5. Select the material and enable the **Emission** checkbox. Set the ****Global Illumination**A group of techniques that model both direct and indirect lighting to provide realistic lighting results.
   See in [Glossary](Glossary.html#globalillumination)** property to **None**.
6. Drag the material onto the sphere to assign it.
7. Place the sphere in the same position as your light.
8. Go to the **Baked Lightmaps** tab in the Lighting window (**Window** > **Rendering** > **Lighting**).
9. Select the **Generate Lighting** button to generate lighting based on these settings.
After Unity generates the lighting, the emissive objects are captured in the reflection probe **cubemap**A collection of six square textures that can represent the reflections in an environment or the skybox drawn behind your geometry. The six squares form the faces of an imaginary cube that surrounds an object; each face represents the view along the directions of the world axes (up, down, left, right, forward and back). [More info](class-Cubemap-landing.html)
See in [Glossary](Glossary.html#Cubemap). You can hide the emissive proxies after baking or use a ****Culling Mask**Allows you to include or omit objects to be rendered by a Camera, by Layer.
See in [Glossary](Glossary.html#CullingMask)** in the [Camera](class-Camera.html)A component which creates an image of a particular viewpoint in your scene. The output is either drawn to the screen or captured as a texture. [More info](CamerasOverview.html)
See in [Glossary](Glossary.html#Camera) component to hide the emissive objects.