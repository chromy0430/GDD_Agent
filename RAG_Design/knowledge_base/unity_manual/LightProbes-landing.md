--- 
Source: Unity 6 Manual (LightProbes-landing.md)
---

# Precalculating indirect light with Light Probes
Resources and techniques for using **Light Probes**Light probes store information about how light passes through space in your scene. A collection of light probes arranged within a given space can improve lighting on moving objects and static LOD scenery within that space. [More info](LightProbes.html)
See in [Glossary](Glossary.html#LightProbe) to store the light at specific points in a **scene**A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](CreatingScenes.html)
See in [Glossary](Glossary.html#Scene), so that Unity can calculate indirect lighting for **GameObjects**The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](class-GameObject.html)
See in [Glossary](Glossary.html#GameObject) more quickly.
| **Page** | **Description** |
| --- | --- |
| [Introduction to Light Probes](LightProbes.html) | Learn about using Light Probes to store the light passing through specific points in a scene. |
| [Light Probes and moving GameObjects](LightProbes-MovingObjects.html) | Understand how dynamic GameObjects sample the light from Light Probes. |
| [Place Light Probes with the Editor](class-LightProbeGroup.html) | Choose where to place Light Probes, and choose the right amount of probes if you use **Enlighten**A lighting system by Geomerics used in Unity for Enlighten Realtime Global Illumination. [More info](https://www.siliconstudio.co.jp/en/products-service/enlighten/) See in [Glossary](Glossary.html#Enlighten) Realtime **Global Illumination**A group of techniques that model both direct and indirect lighting to provide realistic lighting results. See in [Glossary](Glossary.html#globalillumination). |
| [Place Light Probes with a script](LightProbes-Placing-Scripting.html) | An example of forming a ring of Light Probes with a script. |
| [Set a GameObject to use light from Light Probes](LightProbes-MeshRenderer.html) | Use a **Mesh**The main graphics primitive of Unity. Meshes make up a large part of your 3D worlds. Unity supports triangulated or Quadrangulated polygon meshes. Nurbs, Nurms, Subdiv surfaces must be converted to polygons. [More info](mesh.html) See in [Glossary](Glossary.html#Mesh) Renderer component to set a GameObject correctly to receive light from Light Probes. |
| [Load Light Probes in multiple scenes](light-probes-and-scene-loading.html) | Use a script to control when Unity updates Light Probes if you load multiple scenes. |
| [Move Light Probes at runtime](LightProbes-Moving.html) | Use the `LightProbes` API to move Light Probes, for example if you create a world by loading multiple scenes additively and moving each scene to a different position. |
| [Troubleshooting Light Probes](light-probes-troubleshooting.html) | Solve common issues with Light Probes, such as light bleeding and ringing. |
| [Troubleshooting objects appearing unlit by Light Probes](ts-objects-missing-lighting.html) | Troubleshoot issues causing objects to appear unlit by Light Probes. |
| [Light Probes reference](LightProbes-Reference.html) | Explore the properties and settings in the Light Probe component **Inspector**A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](UsingTheInspector.html) See in [Glossary](Glossary.html#Inspector) window reference and the Edit **Light Probe Group**A component that enables you to add Light Probes to GameObjects in your scene. [More info](class-LightProbeGroup.html) See in [Glossary](Glossary.html#LightProbeGroup) tool. |
# Additional resources
* [Adaptive Probe Volumes (APV) in URP](urp/probevolumes.html)
* [Configure an object to sample more light probes in the Built-In Render Pipeline](LightProbeProxyVolume-landing.html)