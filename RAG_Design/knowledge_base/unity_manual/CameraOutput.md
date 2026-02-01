--- 
Source: Unity 6 Manual (CameraOutput.md)
---

# Camera output
Techniques for outputting depth, depth-normal and motion vector information from a **camera**A component which creates an image of a particular viewpoint in your scene. The output is either drawn to the screen or captured as a texture. [More info](CamerasOverview.html)
See in [Glossary](Glossary.html#Camera).
| **Page** | **Description** |
| --- | --- |
| [Introduction to camera output](CameraOutput-introduction.html) | Learn about using the `DepthTextureMode` API to output a depth or motion texture from a camera. |
| [Output a depth texture from a camera](SL-CameraDepthTexture.html) | Output a texture with data about the object depth or surface normals in the camera view. |
| [Output a motion vector texture from a camera](SL-CameraDepthTexture-motionvectors.html) | Output a texture with data about object motion in the camera view. |
| [Sample output textures in a shader](CameraOutput-shader.html) | Read the data from a depth texture or a motion vector texture in custom **shader**A program that runs on the GPU. [More info](Shaders.html) See in [Glossary](Glossary.html#shader) code. |
| [Troubleshooting camera output](CameraOutput-troubleshoot.html) | Solve common issues with camera output, such as visual artefacts. |
## Additional resources
* [Motion vectors in URP](urp/features/motion-vectors.html)
* [Camera render order in URP](urp/cameras-advanced.html)
* [Access camera data with the Universal Additional Camera Data component in URP](urp/universal-additional-camera-data.html)