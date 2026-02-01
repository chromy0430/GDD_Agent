--- 
Source: Unity 6 Manual (vulkan.md)
---

# Vulkan
[Vulkan](https://www.vulkan.org) is a modern graphics API that works across multiple platforms including mobile and desktop. Unity supports Vulkan allowing you to target Vulkan-capable devices and providing direct control over the GPU.
## Platform compatibility
Unity supports the Vulkan API for developing applications on the following platforms:
* Android
* Embedded Linux
* Linux
* Windows
For developing [XR](XR.html)An umbrella term encompassing Virtual Reality (VR), Augmented Reality (AR) and Mixed Reality (MR) applications. Devices supporting these forms of interactive applications can be referred to as XR devices. [More info](XR.html)
See in [Glossary](Glossary.html#XR) applications, Unity supports Vulkan on the Windows and Android platform.
## Vulkan on Android
When you create a new Android project, Vulkan is enabled as the default graphics API. For other platforms where Vulkan is not the default graphics API, you can enable it through Unity Editor’s **Player settings**Settings that let you set various player-specific options for the final game built by Unity. [More info](class-PlayerSettings.html)
See in [Glossary](Glossary.html#PlayerSettings). For more information, refer to [Override default graphics APIs](configure-graphicsAPIs.html#override-default-gfxapi).
When developing a Unity Android project with Vulkan, consider the following recommendations and features:
### Vulkan device filtering
You can manage Vulkan support on Android devices to fine-tune which devices use the Vulkan API with the [Vulkan Device Filtering Asset](introduction-vulkan-device-filtering-asset.html). This asset allows you to exclude specific Android devices on which Vulkan might lead to suboptimal performance.
### Swapchain pre-rotation
It is recommended to enable framebuffer orientation through the Android Player settings. For more information, refer to the documentation on [Framebuffer orientation](vulkan-swapchain-pre-rotation.html).
### Vulkan validation layers
You can enable validation layers for debugging native Vulkan API **plug-ins**A set of code created outside of Unity that creates functionality in Unity. There are two kinds of plug-ins you can use in Unity: Managed plug-ins (managed .NET assemblies created with tools like Visual Studio) and Native plug-ins (platform-specific native code libraries). [More info](./plug-ins.html)
See in [Glossary](Glossary.html#plug-in) through the `-force-vulkan-layers` command-line argument. For more information about the plug-in requirements when using validation layers, refer to [Plug-in using the Vulkan graphics API](low-level-native-plugin-rendering-extensions.html#vulkan-plugin).
## Advantages and limitations
Consider the following advantages and limitations of using Vulkan as the graphics API in your Unity project.
* Vulkan enables [High Definition Render Pipeline (HDRP)](high-definition-render-pipeline.html) support on Linux.
* On Linux and Android, Vulkan generally supports more capabilities, such as graphics jobs and direct control over the GPU, which aren’t available in [OpenGL Core](OpenGLCoreDetails.html) on Linux or OpenGL ES on Android.
* Unity doesn’t support Vulkan for Windows on Arm devices. If your application targets such devices, consider using alternative graphics APIs supported by Unity.
* On Windows, some features such as async compute and **ray tracing**The process of generating an image by tracing out rays from the Camera through each pixel and recording the color contribution at the hit point. This is an alternative to rasterization. raytracing
  See in [Glossary](Glossary.html#raytracing) are currently not implemented for Vulkan. For these features, [D3D12](UsingDX11GL3Features.html) is recommended in Unity.
## Key features and differences in Vulkan API
Vulkan supports several features and capabilities that differentiate it from other graphics APIs, such as OpenGL.
* [Graphics jobs](class-PlayerSettingsAndroid.html#GraphicsJobsMode): Vulkan supports graphics jobs, a feature that allows rendering tasks to run on multiple threads. This might help improve performance of your application. Graphics jobs feature isn’t supported with OpenGL.
* [Dynamic Resolution](DynamicResolution-introduction.html)A Camera setting that allows you to dynamically scale individual render targets to reduce workload on the GPU. [More info](DynamicResolution-landing.html)
  See in [Glossary](Glossary.html#dynamicresolution): Vulkan supports dynamic resolution scaling on devices allowing to adjust the resolution of the individual render targets in real time. This feature reduces workload on the GPU thereby improving performance of your application.
* [Memoryless Render Textures](../ScriptReference/RenderTexture-memorylessMode.html): On some Vulkan compatible platforms, memoryless **render textures**A special type of Texture that is created and updated at runtime. To use them, first create a new Render Texture and designate one of your Cameras to render into it. Then you can use the Render Texture in a Material just like a regular Texture. [More info](class-RenderTexture.html)
  See in [Glossary](Glossary.html#RenderTexture) temporarily store data in the on-tile memory during rendering. This can help improve performance and reduce memory usage of your application.
* [Direct control over GPU](PlayerCommandLineArguments.html): Unity uses Vulkan’s direct GPU control capability to support the `-force-device-index` option, allowing you to specify which GPU Unity’s Standalone Player should use. This capability of Vulkan allows you to optimize your application for better performance. This feature isn’t supported with OpenGL.
* [XR features](xr-untethered-device-optimization.html#vulkan): Vulkan is recommended for Android XR and Meta Quest devices because some newer graphics features are only supported with Vulkan. For example, [Multiview Render Regions](xr-multiview-render-regions.html) is a Vulkan-specific feature. Vulkan API is more stable and provides better performance compared to OpenGL in URP projects targeting XR platforms.
## Additional resources
* [Vulkan design guidelines](https://developer.android.com/ndk/guides/graphics/design-notes?authuser=3)
* [Vulkan validation layers on Android](https://developer.android.com/ndk/guides/graphics/validation-layer)