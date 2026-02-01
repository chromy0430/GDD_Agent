--- 
Source: Unity 6 Manual (GPUInstancing-landing.md)
---

# GPU instancing
Render multiple copies of the same **mesh**The main graphics primitive of Unity. Meshes make up a large part of your 3D worlds. Unity supports triangulated or Quadrangulated polygon meshes. Nurbs, Nurms, Subdiv surfaces must be converted to polygons. [More info](mesh.html)
See in [Glossary](Glossary.html#Mesh) at the same time.
| **Page** | **Description** |
| --- | --- |
| [Introduction to GPU instancing](GPUInstancing.html) | Learn about the GPU drawing multiple copies of a mesh at the same time, for example to draw multiple trees or bushes. |
| [Enable GPU instancing](gpu-instancing-enable.html) | Make sure meshes and **shaders**A program that runs on the GPU. [More info](Shaders.html) See in [Glossary](Glossary.html#shader) are compatible with GPU instancing. |
| [Troubleshooting GPU instancing](gpu-instancing-troubleshoot.html) | Solve common issues with GPU instancing, such as slower rendering. |
## Additional resources
* [Choose a method for optimizing draw calls](optimizing-draw-calls-choose-method.html)
* [Make materials incompatible with the SRP Batcher in URP](SRPBatcher-Incompatible.html)
* [Creating shaders that support GPU instancing in the Built-In Render Pipeline](gpu-instancing-shader.html)