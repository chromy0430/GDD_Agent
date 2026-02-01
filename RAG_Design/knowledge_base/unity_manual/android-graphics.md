--- 
Source: Unity 6 Manual (android-graphics.md)
---

# Graphics for Android
This section of the User Manual contains Android-specific graphics information.
Android device hardware capabilities vary between models, and there are many different Android models on the market. This is important to consider when you develop graphics features and write **shaders**A program that runs on the GPU. [More info](Shaders.html)
See in [Glossary](Glossary.html#shader).
| **Topic** | **Description** |
| --- | --- |
| [Screen configuration](android-screen-configuration.html) | Contains information on screen-related features such as application orientation and multi-window mode. |
| [Single-pass stereo instancing](Android-SinglePassStereoRendering.html) | Explains how to use single-pass stereo rendering in your Android application. |
| [Framebuffer orientation](vulkan-swapchain-pre-rotation.html) | Explains how to manually match the application’s frame buffer to the Android device’s native orientation. |
| [Vulkan API and graphics jobs mode configuration](vulkanapi-graphics-jobs-configuration.html) | Explains how to create and use the Vulkan Device Filtering Asset to allow or restrict Android devices from using the Vulkan API and set preferred graphics jobs modes. |