--- 
Source: Unity 6 Manual (wizard-RagdollWizard.md)
---

# Create a ragdoll
You can create a skinned **mesh**The main graphics primitive of Unity. Meshes make up a large part of your 3D worlds. Unity supports triangulated or Quadrangulated polygon meshes. Nurbs, Nurms, Subdiv surfaces must be converted to polygons. [More info](mesh.html)
See in [Glossary](Glossary.html#Mesh) character and rig it up with bones in a 3D modeling application.
Unity can then generate all **colliders**An invisible shape that is used to handle physical collisions for an object. A collider doesn’t need to be exactly the same shape as the object’s mesh - a rough approximation is often more efficient and indistinguishable in gameplay. [More info](CollidersOverview.html)
See in [Glossary](Glossary.html#collider), **rigidbody**A component that allows a GameObject to be affected by simulated gravity and other forces. [More info](class-Rigidbody.html)
See in [Glossary](Glossary.html#Rigidbody) components, and joints that make up a ragdoll from your skinned mesh character.
1. Create and rig a skinned mesh character in your 3D modeling application.
2. Save the skinned mesh character in your project folder.
3. Launch Unity, and select the skinned mesh file. The **Import Settings** dialog appears in the **Inspector**A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](UsingTheInspector.html)
   See in [Glossary](Glossary.html#Inspector) window. If needed, disable **Generate Colliders** in the **Import Settings** dialog.
4. Create an instance of the character by dragging it from the **Project**In Unity, you use a project to design and develop a game. A project stores all of the files that are related to a game, such as the asset and Scene files. [More info](2Dor3D.html)
   See in [Glossary](Glossary.html#project) window
   to the **Hierarchy** window..
5. Select **GameObject > 3D Object > Ragdoll…** from the menu bar.
6. Drag the different limbs of your character instance from the **Hierarchy** window to the matching wizard area and create your ragdoll. The inspector displays the following components:
   * Skinned mesh renderer
   * Box collider
   * Rigidbody
   You can check how your ragdoll moves in play mode.
7. To save the ragdoll as a prefab, select **Assets -> Create -> Prefab** from the menu bar.
8. Drag the ragdoll character instance from the Hierarchy on top of the ragdoll **prefab**An asset type that allows you to store a GameObject complete with components and properties. The prefab acts as a template from which you can create new object instances in the scene. [More info](Prefabs.html)
   See in [Glossary](Glossary.html#prefab).
You can now reuse your ragdoll character prefab in your project.
For **character joints**An extended ball-socket joint which allows a joint to be limited on each axis. Mainly used for Ragdoll effects. [More info](class-CharacterJoint.html)
See in [Glossary](Glossary.html#CharacterJoint) made with the Ragdoll wizard, the following naming scheme applies:
| **Character joint axis** | **Description** |
| --- | --- |
| **Twist** | Twists the limb. |
| **Swing 1** | Limb’s largest **swing axis**A joint property that defines the axis around which the joint can swing. [More info](class-CharacterJoint.html) See in [Glossary](Glossary.html#SwingAxis). |
| **Swing 2** | Limb’s smaller swing axis. |
## Additional resources
* [Joints](joints-section.html)A physics component allowing a dynamic connection between Rigidbody components, usually allowing some degree of movement such as a hinge. [More info](Joints.html)
  See in [Glossary](Glossary.html#joint)
* [Character Joint component reference](class-CharacterJoint.html)