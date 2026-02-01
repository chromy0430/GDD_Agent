--- 
Source: Unity 6 Manual (xr-graphics.md)
---

# XR graphics
Graphics and rendering in an **XR**An umbrella term encompassing Virtual Reality (VR), Augmented Reality (AR) and Mixed Reality (MR) applications. Devices supporting these forms of interactive applications can be referred to as XR devices. [More info](XR.html)
See in [Glossary](Glossary.html#XR) app follow the same principles as they do in any Unity application, with some differences arising from the need for stereo rendering and increased efficiency.
XR apps generally require very high and consistent frame rates for user comfort. At the same time, rendering in stereo means that every visible object must be drawn twice from different perspectives. Techniques like single-pass rendering can improve rendering efficiency by reducing the duplication of effort, but also require changes to **shader**A program that runs on the GPU. [More info](Shaders.html)
See in [Glossary](Glossary.html#shader) code.
| Topic | Description |
| --- | --- |
| [Universal Render Pipeline compatibility in XR](xr-render-pipeline-compatibility.html) | Understand which Universal **Render Pipeline**A series of operations that take the contents of a Scene, and displays them on a screen. Unity lets you choose from pre-built render pipelines, or write your own. [More info](render-pipelines.html) See in [Glossary](Glossary.html#renderpipeline) features are compatible with XR platforms. |
| [Stereo rendering](SinglePassStereoRendering.html) | Understand stereo rendering for XR platforms. |
| [Foveated rendering](xr-foveated-rendering.html) | Learn about foveated rendering for XR. |
| [Multiview Render Regions](xr-multiview-render-regions.html) | Understand the Multiview Render Regions feature for XR devices. |
| [VR frame timing](VRFrameTiming.html) | Learn about **VR**Virtual Reality [More info](VROverview.html) See in [Glossary](Glossary.html#VR) frame timing. |
| [URP Application Spacewarp](xr-graphics-spacewarp.html) | How to use the URP Application Spacewarp feature on OpenXR platforms to optimize graphics performance. |
| [Optimize for untethered XR devices in URP](xr-untethered-device-optimization.html) | Understand the ways you can optimize your URP project for XR devices. |
| [Resolution control in XR projects](xr-graphics-resolution-scaling.html) | Understand how to control the resolution in your untethered XR project. |
| [Tile-based rendering in XR](xr-graphics-on-tile-rendering.html) | Understand on-tile rendering in XR. |
| [On-tile post-processing (URP)](xr-graphics-on-tile-post-processing.html) | Learn about on-tile **post-processing**A process that improves product visuals by applying filters and effects before the image appears on screen. You can use post-processing effects to simulate physical camera and film properties, for example Bloom and Depth of Field. [More info](PostProcessingOverview.html) post processing, postprocessing, postprocess See in [Glossary](Glossary.html#post-processing) for untethered XR devices. |