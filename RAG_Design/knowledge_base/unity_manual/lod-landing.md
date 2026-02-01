--- 
Source: Unity 6 Manual (lod-landing.md)
---

# Optimize mesh rendering using level of detail (LOD)
Strategies and resources for applying **level of detail**The *Level Of Detail* (LOD) technique is an optimization that reduces the number of triangles that Unity has to render for a GameObject when its distance from the Camera increases. [More info](LevelOfDetail.html)
See in [Glossary](Glossary.html#levelofdetail) (LOD) techniques to meshes to reduce rendering workload.
This section contains information on LOD techniques for meshes. For information on LOD techniques for **shaders**A program that runs on the GPU. [More info](Shaders.html)
See in [Glossary](Glossary.html#shader), refer to [SubShader LOD value](SL-ShaderLOD.html).
| **Topic** | **Description** |
| --- | --- |
| [Introduction to level of detail](LevelOfDetail.html) | Understand level of detail (LOD) and LOD indices, and learn about the LOD features available in Unity. |
| [Mesh LOD](lod/mesh-lod-landing.html) | **Mesh**The main graphics primitive of Unity. Meshes make up a large part of your 3D worlds. Unity supports triangulated or Quadrangulated polygon meshes. Nurbs, Nurms, Subdiv surfaces must be converted to polygons. [More info](mesh.html) See in [Glossary](Glossary.html#Mesh) LOD is a Unity feature that reduces the number of polygons to draw with minimum memory footprint and computational overhead. |
| [LOD Group](lod/lod-group-landing.html)A component to manage level of detail (LOD) for GameObjects. [More info](class-LODGroup.html) See in [Glossary](Glossary.html#LODGroup) | LOD Group is a flexible Unity LOD solution. It provides more optimization options than the [Mesh LOD](lod/mesh-lod-landing.html) feature, but has a larger memory footprint and computational overhead. |
| [2D images for low level of detail (LOD)](2d-images-lod.html) | Techniques and resources for using 2D **billboards**A textured 2D object that rotates so that it always faces the Camera. [More info](class-BillboardRenderer.html) See in [Glossary](Glossary.html#billboard) to simplify 3D meshes that are far away. |
## Additional resources
* [Importing models into Unity](models-importing.html)
* [Mesh components reference](mesh-components-reference.html)