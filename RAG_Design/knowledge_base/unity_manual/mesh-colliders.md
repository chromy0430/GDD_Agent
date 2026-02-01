--- 
Source: Unity 6 Manual (mesh-colliders.md)
---

# Mesh colliders
The **Mesh**The main graphics primitive of Unity. Meshes make up a large part of your 3D worlds. Unity supports triangulated or Quadrangulated polygon meshes. Nurbs, Nurms, Subdiv surfaces must be converted to polygons. [More info](mesh.html)
See in [Glossary](Glossary.html#Mesh) **collider**An invisible shape that is used to handle physical collisions for an object. A collider doesn’t need to be exactly the same shape as the object’s mesh - a rough approximation is often more efficient and indistinguishable in gameplay. [More info](CollidersOverview.html)
See in [Glossary](Glossary.html#collider) takes a [Mesh Asset](class-Mesh.html) and builds a collider that matches the geometry of that Mesh. It is more accurate for **collision**A collision occurs when the physics engine detects that the colliders of two GameObjects make contact or overlap, when at least one has a Rigidbody component and is in motion. [More info](CollidersOverview.html)
See in [Glossary](Glossary.html#collision) detection than primitive colliders, and is a better option for complicated Meshes.
| **Topic** | **Description** |
| --- | --- |
| [Introduction to Mesh colliders](mesh-colliders-introduction.html) | Overview of the fundamental concepts around **Mesh colliders**A free-form collider component which accepts a mesh reference to define its collision surface shape. [More info](class-MeshCollider.html) See in [Glossary](Glossary.html#MeshCollider) in Unity. |
| [Prepare a Mesh for Mesh colliders](prepare-mesh-for-mesh-collider.html) | Configure a Mesh so that a Mesh collider can use it to generate collision geometry. |
| [Mesh collider component reference](class-MeshCollider.html) | Reference page for the Mesh collider component. |