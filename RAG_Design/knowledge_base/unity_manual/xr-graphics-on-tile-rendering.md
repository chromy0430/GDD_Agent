--- 
Source: Unity 6 Manual (xr-graphics-on-tile-rendering.md)
---

# Tile-based rendering in XR
Understand on-tile rendering in **XR**An umbrella term encompassing Virtual Reality (VR), Augmented Reality (AR) and Mixed Reality (MR) applications. Devices supporting these forms of interactive applications can be referred to as XR devices. [More info](XR.html)
See in [Glossary](Glossary.html#XR).
Tile-based GPUs are common in mobile and untethered XR devices. Performance on devices with a tile-based GPU is improved when your project uses features that are optimized for tile-based architecture.
Rendering off-tile results in additional render passes and requires intermediate data to be written to and read from external memory. Graphical loads are inefficient and increase memory bandwidth usage and power consumption, leading to reduced performance and shorter battery life. To maximize performance on untethered XR devices, minimize off-tile operations and use features optimized for tile-based rendering.
Refer to the following sections to learn more about tile-based rendering in XR, and methods to ensure rendering remains on-tile.
## About tile-based GPUs
Tile-based GPUs divide the screen into small regions (tiles), which are rendered on-chip in the tile buffer. When a tile is rendered, its data is written to the framebuffer in the main memory. Tile-based GPUs enable faster memory and improved power-efficiency on mobile and untethered XR devices.
## Tips to ensure tile-based rendering
If your project targets an untethered XR device and enables [On-tile post-processing](xr-graphics-on-tile-post-processing.html), you must ensure your project only renders on-tile.
Any feature that creates intermediate textures results in an additional final **blit**A shorthand term for “bit block transfer”. A blit operation is the process of transferring blocks of data from one place in memory to another.
See in [Glossary](Glossary.html#blit) pass and breaks tile-based rendering, resulting in app and device performance issues.
Only [memoryless intermediate textures](../ScriptReference/RenderTexture-memorylessMode.html) are supported on-tile. To use memoryless intermediate textures, your project must use the Vulkan or Metal API. To understand how to configure your API, refer to [Configure graphics APIs](configure-graphicsAPIs.html#override-default-gfxapi).
Features that create non-memoryless intermediate textures result in an additional final blit pass and are unable to stay on-tile, which breaks the render pass. Non-memoryless intermediate textures introduce performance issues from moving data from on-tile to off-tile memory.
You should avoid the following features on untethered XR devices as they introduce off-tile rendering:
* [Intermediate textures](urp/urp-universal-renderer.html)
* [Depth](urp/universalrp-asset.html) and [Opaque](urp/universalrp-asset.html) textures.
* [Upscaling filter](urp/universalrp-asset.html)
* URP built-in Post processing
* [Renderer feature](urp/urp-renderer-feature.html) that require intermediate texture:
  + [Decal](urp/renderer-feature-decal-landing.html)
  + [FullScreenPass](urp/renderer-features/renderer-feature-full-screen-pass.html) if **FetchColorBuffer** is `true`
  + [SSAO](urp/post-processing-ssao-landing.html)
### Use Render Graph Viewer to check render passes
To ensure your project remains on-tile, configure your [URP asset](urp/universalrp-asset.html) and [URP renderer](urp/urp-renderer-feature.html) to render directly to the eye texture, which means that your project uses a single merged render pass. You can use the [Render Graph Viewer](urp/render-graph-viewer-reference.html) to [Analyze a render graph in URP](urp/render-graph-view.html) and [Merge render passes](urp/render-graph-optimize.html#merge-render-passes.html).
#### Render Graph Viewer example
The following image demonstrates the optimal pipeline configuration with on-tile **post-processing**A process that improves product visuals by applying filters and effects before the image appears on screen. You can use post-processing effects to simulate physical camera and film properties, for example Bloom and Depth of Field. [More info](PostProcessingOverview.html) post processing, postprocessing, postprocess
See in [Glossary](Glossary.html#post-processing) and how to interpret the Render Graph Viewer:
![Render Graph Viewer example of merged render passes that will render on-tile.](../uploads/Main/xr-graphics-on-tile-render-graph.png)
Render Graph Viewer example of merged render passes that will render on-tile.
The blue line (A) represents merged render passes.
**cameraTargetAttachment** (B) and **cameraDepthAttachment (C)** are memoryless on-tile resources. The on-tile post-processing features uses frame buffer fetch (denoted by an **F** symbol) (D) to fetch the **cameraTargetAttachment** and write to the **Backbuffer color** (E).
## Additional resources
* [On-tile post processing](xr-graphics-on-tile-post-processing.html)
* [Optimize for untethered XR devices in URP](xr-untethered-device-optimization.html)
* [Mobile GPUs and tiled rendering]([https://developers.meta.com/horizon/documentation/unity/gpu-tiled](https://developers.meta.com/horizon/documentation/unity/gpu-tiled/?locale=en_GB)) (Meta developer documentation)