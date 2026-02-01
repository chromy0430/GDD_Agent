--- 
Source: Unity 6 URP Manual (features\motion-vectors-landing.html)
---

# Motion vectors in URP
Resources for outputting and reading a texture with data about object motion in the **camera**A component which creates an image of a particular viewpoint in your scene. The output is either drawn to the screen or captured as a texture. [More info](../../CamerasOverview.html)
See in [Glossary](../../Glossary.html#Camera) view.
| **Page** | **Description** |
| --- | --- |
| [Introduction to motion vectors](../features/motion-vectors.html) | Learn about how URP calculates the frame-to-frame screen-space movement of surface fragments. |
| [Built-in shader support for motion vectors](../features/motion-vectors-shader-support.html) | Learn about which types of motion different **shader**A program that runs on the GPU. [More info](../../Shaders.html) See in [Glossary](../../Glossary.html#shader) types support for calculating motion vectors. |
| [Motion vectors render pass](../features/motion-vectors-render-pass.html) | Understand how the `MotionVectors` render pass renders the motion vector texture. |
| [Output a motion vector texture in a custom shader](../features/motion-vectors-custom-shader.html) | Render a motion vector texture in a custom shader. |
| [Sample motion vectors in a shader](../features/motion-vectors-sample.html) | Request the motion vector texture as an input in a custom shader. |
| [Troubleshooting motion vectors](../features/motion-vectors-troubleshooting.html) | Solve common issues with motion vectors, for example visual artefacts. |
| [Motion Vectors settings in the MeshRenderer component window reference](../features/motion-vectors-reference.html) | Explore the properties in the Motion Vectors settings to specify how a **GameObject**The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](../../class-GameObject.html) See in [Glossary](../../Glossary.html#GameObject) contributes to a motion vector texture. |
## Additional resources
* [Output a motion vector texture from a camera](../../SL-CameraDepthTexture-motionvectors.html)