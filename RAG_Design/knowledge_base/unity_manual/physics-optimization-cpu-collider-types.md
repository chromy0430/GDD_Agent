--- 
Source: Unity 6 Manual (physics-optimization-cpu-collider-types.md)
---

# Collider types and performance
Optimize CPU performance by selecting the most appropriate **collider**An invisible shape that is used to handle physical collisions for an object. A collider doesn’t need to be exactly the same shape as the object’s mesh - a rough approximation is often more efficient and indistinguishable in gameplay. [More info](CollidersOverview.html)
See in [Glossary](Glossary.html#collider) type for your **scene**A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](CreatingScenes.html)
See in [Glossary](Glossary.html#Scene).
Choosing the right collider type directly affects CPU performance. Unity has several collider types, each with different computational costs.
To learn more about ****Mesh**The main graphics primitive of Unity. Meshes make up a large part of your 3D worlds. Unity supports triangulated or Quadrangulated polygon meshes. Nurbs, Nurms, Subdiv surfaces must be converted to polygons. [More info](mesh.html)
See in [Glossary](Glossary.html#Mesh) Collider** component properties, refer to [Mesh collider component reference](class-MeshCollider.html).
To learn more about collider interactions, refer to [Collider interactions](collider-interactions.html).
The following table summarizes the collider types and their performance characteristics in order from most to least performant:
| **Collider type** | **Performance characteristics** |
| --- | --- |
| ****Sphere Collider**A sphere-shaped collider component that handles collisions for GameObjects like balls or other things that can be roughly approximated as a sphere for the purposes of physics. [More info](class-SphereCollider.html) See in [Glossary](Glossary.html#SphereCollider)** | The simplest and most efficient collider. Use for round objects and general-purpose interactions. |
| ****Capsule Collider**A capsule-shaped collider component that handles collisions for GameObjects like barrels and character limbs. [More info](class-CapsuleCollider.html) See in [Glossary](Glossary.html#CapsuleCollider)** | Slightly more complex than a Sphere Collider, but still efficient. Use for characters, poles, or other elongated shapes. |
| ****Box Collider**A cube-shaped collider component that handles collisions for GameObjects like dice and ice cubes. [More info](class-BoxCollider.html) See in [Glossary](Glossary.html#BoxCollider)** | Efficient and flexible, especially for rectangular or block-shaped objects. Slightly more resource-intensive than Sphere Collider or Capsule Collider. |
| **Convex Mesh Collider** | More resource-intensive than primitive colliders. Use only when primitive shapes or compound colliders cannot approximate the geometry. The mesh must be convex. You can attach this to **GameObjects**The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](class-GameObject.html) See in [Glossary](Glossary.html#GameObject) with non-kinematic **Rigidbody**A component that allows a GameObject to be affected by simulated gravity and other forces. [More info](class-Rigidbody.html) See in [Glossary](Glossary.html#Rigidbody) components attached. |
| **Non-convex Mesh Collider** | A Mesh Collider with **Convex** unchecked. The most resource-intensive collider type. Use only for static, non-moving geometry that requires precise **collision**A collision occurs when the physics engine detects that the colliders of two GameObjects make contact or overlap, when at least one has a Rigidbody component and is in motion. [More info](CollidersOverview.html) See in [Glossary](Glossary.html#collision) surfaces. Cannot be attached to non-kinematic Rigidbodies. |
## Compound colliders
[Compound colliders](compound-colliders.html) are formed by parenting multiple primitive colliders, such as Sphere, Box, and Capsule colliders, to a single GameObject with a Rigidbody component. You can use compound colliders, which are comprised of simple components, to approximate complex shapes. Compound colliders are generally more efficient than using a single, complex Mesh Collider for a dynamic object, but they’re more resource-intensive than a single primitive collider.
Use as few primitive colliders as possible within a compound setup to have effective **collision detection**An automatic process performed by Unity which determines whether a moving GameObject with a Rigidbody and collider component has come into contact with any other colliders. [More info](CollidersOverview.html)
See in [Glossary](Glossary.html#collisiondetection).
To learn more about compound colliders, refer to [Compound colliders](compound-colliders.html).
Use Compound colliders when:
* You have an object whose shape cannot be accurately represented by a single primitive collider.
* You have dynamic objects that require a complex collision shape but must remain performant (as an alternative to a costly convex Mesh Collider).
* You need dynamic concave collision shapes, which a single Mesh Collider on a dynamic `Rigidbody` cannot do because a single Mesh Collider must be convex.
* You need fine-tuned collision zones for gameplay. For example you have distinct head, torso, or limb hitboxes on a character.
## Prepare meshes for mesh colliders
[Mesh Collider components](mesh-colliders.html) require a preprocessing step called “mesh cooking” to convert their geometry into an optimized format for efficient physics calculations. If this cooking occurs at runtime, it can cause significant CPU performance spikes.
To learn more about Mesh Collider components, refer to [Mesh colliders](mesh-colliders.html)A free-form collider component which accepts a mesh reference to define its collision surface shape. [More info](class-MeshCollider.html)
See in [Glossary](Glossary.html#MeshCollider).
You can avoid mesh cooking at runtime by doing the following:
* Use Editor-Time cooking (Implicit): The primary way to pre-cook meshes is in the Editor. When you assign a Mesh asset to a Mesh Collider component in the **Inspector**A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](UsingTheInspector.html)
  See in [Glossary](Glossary.html#Inspector) window and save your scene or **prefab**An asset type that allows you to store a GameObject complete with components and properties. The prefab acts as a template from which you can create new object instances in the scene. [More info](Prefabs.html)
  See in [Glossary](Glossary.html#prefab), the Editor automatically cooks the mesh for that specific collider instance. The cooked data is then saved with your asset.
* Enable Prebake Collision Meshes in the Player section of the **Project Settings**A broad collection of settings which allow you to configure how Physics, Audio, Networking, Graphics, Input and many other areas of your project behave. [More info](comp-ManagerGroup.html)
  See in [Glossary](Glossary.html#ProjectSettings): Enable **Prebake Collision Meshes** to make the Editor proactively find and cook all meshes used by Mesh Collider components in your project during builds, asset imports, and Editor loads. This setting is enabled by default. **Prebake Collision Meshes** can increase build times and Editor load times as the meshes process. The cooked data is stored, which slightly affects build size if many unique meshes are involved, but the main trade-off is increased build and load duration versus runtime stability. Use **Prebake Collision Meshes** to prevent unexpected runtime cooking spikes by ensuring most meshes are ready. The recommended best practice is to keep **Prebake Collision Meshes** enabled as a safety net. Consider disabling **Prebake Collision Meshes** only if you manually and meticulously manage all mesh cooking. For example, you rely solely on Editor-time instance cooking and `Physics.BakeMesh` for all dynamic cases and you want to potentially reduce build and Editor processing times.
* Use [`Physics.BakeMesh`](../ScriptReference/Physics.BakeMesh.html): For meshes assigned or procedurally generated at runtime, use `Physics.BakeMesh(meshInstanceId, convex, cookingOptions)` to explicitly control when cooking occurs. Preferably use `Physics.BakeMesh` during loading screens or in background threads if you use the [job system](job-system-overview.html).
# Additional resources
* [Unity Profiler](Profiler.html)
* [Managing time and frame rate](managing-time-and-frame-rate.html)
* [Memory Profiler](https://docs.unity3d.com/Packages/com.unity.memoryprofiler@latest)
* [Physics Project Settings](class-PhysicsManager.html)
* [Mesh collider component reference](class-MeshCollider.html)
* [Collider interactions](collider-interactions.html)
* [Compound colliders](compound-colliders.html)
* [Mesh colliders](mesh-colliders.html)