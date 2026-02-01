--- 
Source: Unity 6 Manual (compressing-mesh-data-optimization.md)
---

# Compressing mesh data for optimization
Techniques and strategies for compressing **mesh**The main graphics primitive of Unity. Meshes make up a large part of your 3D worlds. Unity supports triangulated or Quadrangulated polygon meshes. Nurbs, Nurms, Subdiv surfaces must be converted to polygons. [More info](mesh.html)
See in [Glossary](Glossary.html#Mesh) data in Unity to reduce its size, which can improve performance.
| **Topic** | **Description** |
| --- | --- |
| [Types of mesh data compression](types-of-mesh-data-compression.html) | Understand the difference between mesh **compression**A method of storing data that reduces the amount of storage space it requires. See [Texture Compression](texture-choose-format-by-platform.html), [Animation Compression](class-AnimationClip.html#AssetProperties), [Audio Compression](class-AudioClip.html), [Build Compression](ReducingFilesize.html). See in [Glossary](Glossary.html#compression) and vertex compression, and their impact on your project. |
| [Configure vertex compression](configure-vertex-compression.html) | Configure the precision of data formats in all meshes, to impact reduces the size of mesh data in memory. |
| [Configure mesh compression](configure-mesh-compression.html) | Compress the data of individual meshes, to impact file size. |