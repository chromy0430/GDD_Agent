--- 
Source: Unity 6 Manual (particle-system-optimization.md)
---

# Particle System optimization in the Built-In Render Pipeline
Resources for using GPU instancing to improve the performance of your **particle**A small, simple image or mesh that is emitted by a particle system. A particle system can display and move particles in great numbers to represent a fluid or amorphous entity. The effect of all the particles together creates the impression of the complete entity, such as smoke. [More info](class-ParticleSystem.html)
See in [Glossary](Glossary.html#particle) systems.
| **Property** | **Function** |
| --- | --- |
| [Apply GPU instancing for a Particle System](PartSysInstancing.html) | Activate and apply GPU instancing, which renders **Mesh**The main graphics primitive of Unity. Meshes make up a large part of your 3D worlds. Unity supports triangulated or Quadrangulated polygon meshes. Nurbs, Nurms, Subdiv surfaces must be converted to polygons. [More info](mesh.html) See in [Glossary](Glossary.html#Mesh) particles instead of **billboard**A textured 2D object that rotates so that it always faces the Camera. [More info](class-BillboardRenderer.html) See in [Glossary](Glossary.html#billboard) particles to improve performance. |
| [Example of Particle System GPU Instancing in a Surface Shader](example-particle-system-gpu-instancing-surface-shader.html) | View an example script for applying GPU instancing to a Surface **Shader**A program that runs on the GPU. [More info](Shaders.html) See in [Glossary](Glossary.html#shader). |
| [Example of Particle System GPU Instancing in a Custom Shader](example-particle-system-gpu-instancing-custom-shader.html) | View an example script for applying GPU instancing to a Custom Shader. |
| [Example of Particle system GPU Instancing with custom vertex streams](example-particle-system-gpu-instancing-custom-vertex-streams.html) | View an example script for applying GPU instancing with custom vertex streams. |