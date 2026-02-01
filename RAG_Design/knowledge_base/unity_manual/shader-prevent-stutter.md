--- 
Source: Unity 6 Manual (shader-prevent-stutter.md)
---

# Prevent shader stutters
Learn how you can prevent **shader**A program that runs on the GPU. [More info](Shaders.html)
See in [Glossary](Glossary.html#shader) stutters in your project.
A stutter refers to a noticeable pause in rendering, which causes motion to stop or become uneven. Stutters can occur when Unity uses a shader variant for the first time in your build application. Stutters cause a negative impact on users of your application. For example, stutters reduce the responsiveness on your game, and cam lead to severe motion sickness on **XR**An umbrella term encompassing Virtual Reality (VR), Augmented Reality (AR) and Mixed Reality (MR) applications. Devices supporting these forms of interactive applications can be referred to as XR devices. [More info](XR.html)
See in [Glossary](Glossary.html#XR) platforms.
Refer to the following topics to understand the approaches you can use to prevent shaders stutters in your project:
| **Topic** | **Description** |
| --- | --- |
| [Tracing and warming up PSOs](shader-pso-trace-warming.html) | Trace and warm up graphics states with the experimental `GraphicsStateCollection` API to reduce shader compilation stutters. |
| [Other methods to warm up shaders](shader-prewarm-other.html) | Warm up shaders if your build targets the DirectX 11, OpenGL, OpenGLES, or **WebGL**A JavaScript API that renders 2D and 3D graphics in a web browser. The Unity Web build option allows Unity to publish content as JavaScript programs which use HTML5 technologies and the WebGL rendering API to run Unity content in a web browser. [More info](webgl.html) See in [Glossary](Glossary.html#WebGL) graphics APIs. |