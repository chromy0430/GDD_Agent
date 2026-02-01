--- 
Source: Unity 6 Manual (ts-objects-missing-lighting.md)
---

## Troubleshooting objects appearing unlit by Light Probes
Fix the issues causing objects to appear unlit.
![Three images of the same Cornell Box scene of a rendered room containing two boxes, a sphere, and a statue. In the first image, the sphere and statue are completely black. In the second image, light probes light up the statue and it is visible, while the sphere is still black. In the third image, both the statue and sphere are visible as light probes and reflection probes are in the scene. ](../uploads/Main/ts-ex-obj-missing-lighting.png)
Three images of the same Cornell Box scene of a rendered room containing two boxes, a sphere, and a statue. In the first image, the sphere and statue are completely black. In the second image, light probes light up the statue and it is visible, while the sphere is still black. In the third image, both the statue and sphere are visible as light probes and reflection probes are in the scene.
## Symptoms
The **GameObjects**The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](class-GameObject.html)
See in [Glossary](Glossary.html#GameObject) appear black and are unlit and unaffected by lighting in the **scene**A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](CreatingScenes.html)
See in [Glossary](Glossary.html#Scene).
## Cause
Certain objects appearing as unlit or out of place may indicate a problem with the scene setup. It often reproduces when dynamic objects have no light probes to sample the lighting from. Glossy metallic materials can appear as black when no local reflection probes are present.
Dynamic objects, or GI contributors receiving GI from light probes, need light probes to sample indirect lighting data. If none are present, objects will fall back to sampling the **Ambient Probe**, which is the light and reflection probe that is always present in the scene.
## Resolution - Place light probes
Set up a [Light Probe](class-LightProbeGroup.html)Light probes store information about how light passes through space in your scene. A collection of light probes arranged within a given space can improve lighting on moving objects and static LOD scenery within that space. [More info](LightProbes.html)
See in [Glossary](Glossary.html#LightProbe) network in the scene, adding more probes in areas of high importance. Make sure that there are enough light probes to encompass all affected objects. Generate lighting again to see the effect.
## Resolution - Place reflection probes
Reflective metallic objects might still render as black, even after placing a dense network of light probes. To shade these objects, place a [Reflection Probe](class-ReflectionProbe.html)A rendering component that captures a spherical view of its surroundings in all directions, rather like a camera. The captured image is then stored as a Cubemap that can be used by objects with reflective materials. [More info](class-ReflectionProbe.html)
See in [Glossary](Glossary.html#ReflectionProbe) that encompasses the affected object. Generate the lighting again or re-bake the probe in the Reflection Probe Component by clicking the **Bake** button.
If you observe black areas in the reflections, go to **Lighting** > **Environment** > **Environment Lighting** and increase the **Bounces** value. This will increase the number of light bounces and increase the number of reflections.
## Resolution - Ensure both Light Probes and Reflection Probes are active
Select the unlit GameObject and inspect its ****Mesh**The main graphics primitive of Unity. Meshes make up a large part of your 3D worlds. Unity supports triangulated or Quadrangulated polygon meshes. Nurbs, Nurms, Subdiv surfaces must be converted to polygons. [More info](mesh.html)
See in [Glossary](Glossary.html#Mesh) Renderer** component. Go to **Probes**, and ensure that the **Light Probes** and **Reflection Probes** properties are both set to **Blend Probes** and not set to **Off**.
## Resolution - Adjust material color values
Pure black materials in Unity absorb all direct and indirect light. This is physically correct behavior as no naturally occurring material is completely black.
Adjust your material color values to follow the **physically based shading**An advanced lighting model that simulates the interactions between materials and light in a way that mimics reality. [More info](shader-StandardShader.html)
See in [Glossary](Glossary.html#physicallybasedshading) standards. To determine whether albedo values are compliant with the Physically Based Rendering (PBR) standard:
* In URP, use the [Rendering Debugger](https://docs.unity3d.com/Packages/com.unity.render-pipelines.universal@latest?subfolder=/manual/features/rendering-debugger.html).
* In HDRP, use the [Rendering Debugger](https://docs.unity3d.com/Packages/com.unity.render-pipelines.high-definition@latest?subfolder=/manual/Render-Pipeline-Debug-Window.html).
* In the Built-in **Render Pipeline**A series of operations that take the contents of a Scene, and displays them on a screen. Unity lets you choose from pre-built render pipelines, or write your own. [More info](render-pipelines.html)
  See in [Glossary](Glossary.html#renderpipeline), use the Validate Albedo [scene view draw mode](GIVis.html).
## Resolution - Check the scene setup
If you have [multiple scenes](MultiSceneEditing.html), make sure that the scene containing lighting is set as the [active scene](../ScriptReference/SceneManagement.SceneManager.SetActiveScene.html). By default, Unity sets the first loaded scene as the active scene, which can affect the standalone player builds.