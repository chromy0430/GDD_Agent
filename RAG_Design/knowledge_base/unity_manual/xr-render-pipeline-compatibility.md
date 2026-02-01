--- 
Source: Unity 6 Manual (xr-render-pipeline-compatibility.md)
---

# Universal Render Pipeline compatibility in XR
Support for **XR**An umbrella term encompassing Virtual Reality (VR), Augmented Reality (AR) and Mixed Reality (MR) applications. Devices supporting these forms of interactive applications can be referred to as XR devices. [More info](XR.html)
See in [Glossary](Glossary.html#XR) features in the Universal **Render Pipeline**A series of operations that take the contents of a Scene, and displays them on a screen. Unity lets you choose from pre-built render pipelines, or write your own. [More info](render-pipelines.html)
See in [Glossary](Glossary.html#renderpipeline) (URP) varies by URP package version. This page details compatibility between XR features in Unity 6 and the latest compatible URP version.
To determine which version of URP is compatible with your current Unity version, refer to the [Requirements and compatibility](urp/requirements.html) page in the Universal Render Pipeline documentation.
Unity 6 supports the following **AR**Augmented Reality [More info](AROverview.html)
See in [Glossary](Glossary.html#AR) and **VR**Virtual Reality [More info](VROverview.html)
See in [Glossary](Glossary.html#VR) features in the Universal Render Pipeline:
| **Feature** | **Supported in XR** |
| --- | --- |
| **Post-processing**A process that improves product visuals by applying filters and effects before the image appears on screen. You can use post-processing effects to simulate physical camera and film properties, for example Bloom and Depth of Field. [More info](PostProcessingOverview.html) post processing, postprocessing, postprocess See in [Glossary](Glossary.html#post-processing) effects: Bloom | Yes |
| Post-processing effects: MotionBlur | Yes |
| Post-processing effects: Lens Distortion | No |
| Post-processing effects: **Depth of Field**A post-processing effect that simulates the focus properties of a camera lens. [More info](PostProcessingOverview.html) See in [Glossary](Glossary.html#depthoffield) | Yes |
| Post-processing effects: **ToneMapping**The process of remapping HDR values of an image into a range suitable to be displayed on screen. [More info](PostProcessingOverview.html) See in [Glossary](Glossary.html#tonemapping) | Yes |
| Spatial Temporal Post-Processing | No |
| Other post-processing effects (color adjustment, etc.) | Yes |
| GI (Global Illumination) | Yes |
| **HDR**high dynamic range See in [Glossary](Glossary.html#HDR) | Yes |
| MSAA | Yes |
| Physical **Camera**A component which creates an image of a particular viewpoint in your scene. The output is either drawn to the screen or captured as a texture. [More info](CamerasOverview.html) See in [Glossary](Glossary.html#Camera) | No |
| CopyColor / ColorDepth | Yes |
| Multi Display | No |
| Camera Stacking | Yes |
| Cascaded Shadow | Yes |
| sRGB | Yes |
| **Skybox**A special type of Material used to represent skies. Usually six-sided. [More info](sky-landing.html) See in [Glossary](Glossary.html#Skybox) | Yes |
| Fog | Yes |
| **Billboard**A textured 2D object that rotates so that it always faces the Camera. [More info](class-BillboardRenderer.html) See in [Glossary](Glossary.html#billboard) | Yes |
| **Shader**A program that runs on the GPU. [More info](Shaders.html) See in [Glossary](Glossary.html#shader) Graph | Yes (1) |
| **Particles**A small, simple image or mesh that is emitted by a particle system. A particle system can display and move particles in great numbers to represent a fluid or amorphous entity. The effect of all the particles together creates the impression of the complete entity, such as smoke. [More info](class-ParticleSystem.html) See in [Glossary](Glossary.html#particle) | Yes |
| **Terrain**The landscape in your scene. A Terrain GameObject adds a large flat plane to your scene and you can use the Terrain’s Inspector window to create a detailed landscape. [More info](terrain-UsingTerrains.html) See in [Glossary](Glossary.html#Terrain) | Yes |
| 2D UI (Canvas Renderer, Text Mesh Pro) | Yes |
| URP Debug (Scene View Mode, Frame Debug) | Yes (2) |
* (1) Although Shader Graph shaders can run in XR, Shader Graph doesn’t currently support the XR utility feature to create SPI-compatible shader input textures. Unity will expand support for Shader Graph functionality in future releases.
* (2) Unity supports frame debugging for mock HMDs. Currently, there is no support for Meta/Oculus.
In Unity 6.3 and newer, you can use on-tile post-processing to enable certain URP post-processing effects on XR devices. Refer to [On-tile post-processing (URP)](xr-graphics-on-tile-post-processing.html) to learn more about on-tile post-processing and how to enable it in your XR project.
To learn more about post-processing effects, refer to the [Effect list](post-processing-effect-availability-reference.html) page in the Universal Render Pipeline documentation.