--- 
Source: Unity 6 Manual (loading-texture-mesh-data-asynchronously.md)
---

# Loading texture and mesh data asynchronously
Strategies and resources for uploading texture and **mesh**The main graphics primitive of Unity. Meshes make up a large part of your 3D worlds. Unity supports triangulated or Quadrangulated polygon meshes. Nurbs, Nurms, Subdiv surfaces must be converted to polygons. [More info](mesh.html)
See in [Glossary](Glossary.html#Mesh) data to the GPU asynchronously, to improve performance.
| **Topic** | **Description** |
| --- | --- |
| [Uploading texture and mesh data to the GPU](LoadingTextureandMeshData.html) | Understand the difference between the synchronous and asynchronous upload pipelines, and what makes a mesh eligible for asynchronous upload. |
| [Check whether a mesh uses the asynchronous upload pipeline](identify-mesh-upload-pipeline.html) | Identify whether Unity is using the synchronous or asynchronous upload pipeline for a specific mesh. |
| [Configure the asynchronous upload pipeline](configure-asynchronous-upload-pipeline.html) | Configure the streaming buffer and upload time Unity allocates for asynchronously uploading mesh data to the GPU. |