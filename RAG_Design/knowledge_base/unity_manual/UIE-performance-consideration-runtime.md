--- 
Source: Unity 6 Manual (UIE-performance-consideration-runtime.md)
---

# Performance consideration for runtime UI
This section describes how you can improve the performance for runtime UI.
| **Topic** | **Description** |
| --- | --- |
| [Use usage hints to reduce draw calls and geometry regeneration](UIE-use-usage-hints-to-reduce-draw-calls-and-geometry-regeneration.html) | Use usage hints to set how an element is used at runtime. Usage hints can reduce draw calls and avoid geometry regeneration. |
| [Control textures of the dynamic atlas](UIE-control-textures-of-the-dynamic-atlas.html) | Use an atlas to reduce the number of batches broken by texture changes and achieve good performance. |
| [Platform and mesh consideration](UIE-platform-and-mesh.html) | Consider device capabilities and avoid **mesh**The main graphics primitive of Unity. Meshes make up a large part of your 3D worlds. Unity supports triangulated or Quadrangulated polygon meshes. Nurbs, Nurms, Subdiv surfaces must be converted to polygons. [More info](mesh.html) See in [Glossary](Glossary.html#Mesh) tessellation. |
## Additional resources
* [Panel Settings asset](UIE-Runtime-Panel-Settings.html)
* [`usageHints`](../ScriptReference/UIElements.VisualElement-usageHints.html)