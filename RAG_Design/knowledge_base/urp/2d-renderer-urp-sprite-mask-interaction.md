--- 
Source: Unity 6 URP Manual (2d-renderer-urp-sprite-mask-interaction.html)
---

# Set 3D GameObjects to interact with Sprite masks
To allow a 3D **GameObject**The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](../class-GameObject.html)
See in [Glossary](../Glossary.html#GameObject) to interact with **Sprite**A 2D graphic objects. If you are used to working in 3D, Sprites are essentially just standard textures but there are special techniques for combining and managing sprite textures for efficiency and convenience during development. [More info](../sprite/sprite-landing.html)
See in [Glossary](../Glossary.html#Sprite) masks, set the **Mask Interaction** property of the **mesh**The main graphics primitive of Unity. Meshes make up a large part of your 3D worlds. Unity supports triangulated or Quadrangulated polygon meshes. Nurbs, Nurms, Subdiv surfaces must be converted to polygons. [More info](../mesh.html)
See in [Glossary](../Glossary.html#Mesh) renderer.
## Prerequisites
Your project must be a 2D URP Project for the **Mesh Renderer** component to show the additional **2D > Mask Interaction** property setting.
## Enable Sprite mask interaction
To enable Sprite mask interaction in a [Mesh Renderer](../class-MeshRenderer.html)A mesh component that takes the geometry from the Mesh Filter and renders it at the position defined by the object’s Transform component. [More info](../class-MeshRenderer.html)
See in [Glossary](../Glossary.html#MeshRenderer) or [Skinned Mesh Renderer](../class-SkinnedMeshRenderer.html) component of a 3D GameObject, follow these steps:
1. Select the 3D GameObject.
2. In the **Inspector** window, in the **Mesh Renderer** or **Skinned Mesh Renderer** component, go to the **2D > Mask Interaction** section.
3. Select either **Visible Inside Mask** or **Visible Outside Mask** to have the mesh renderer interact with a Sprite mask. Refer to the following table for the effect of each option.
### Mask Interaction dropdown
| Option | Description |
| --- | --- |
| **None** | Renders without interacting with Sprite masks. |
| **Visible Inside Mask** | Renders only the parts of the mesh that overlap the Sprite mask. |
| **Visible Outside Mask** | Renders only the parts of the mesh that don’t overlap the Sprite mask. |
## Examples
The following are examples of the visual effect that each option has when Unity renders the meshes with Sprite masks.
![This shows two 3D cubes - one red and the other blue - are rendered on top one another when you select None and there is no sprite mask interaction. The Sprite mask is displayed as an orange circle outline.](../../uploads/urp/2D/mesh-renderer-sprite-mask-none.png)
This shows two 3D cubes - one red and the other blue - are rendered on top one another when you select None and there is no sprite mask interaction. The Sprite mask is displayed as an orange circle outline.
![This shows the result of selecting Visible Inside Mask. Only the area of the blue cube that overlaps the Sprite mask is rendered and visible.](../../uploads/urp/2D/mesh-renderer-sprite-mask-visible-inside-mask.png)
This shows the result of selecting Visible Inside Mask. Only the area of the blue cube that overlaps the Sprite mask is rendered and visible.
![This shows the result of selecting Visible Outside Mask. Only the part of the blue cube that doesnt overlap the Sprite mask is rendered and visible. A bit of the red cube is visible through blue cube where it isnt rendered.](../../uploads/urp/2D/mesh-renderer-sprite-mask-visible-outside-mask.png)
This shows the result of selecting Visible Outside Mask. Only the part of the blue cube that doesn’t overlap the Sprite mask is rendered and visible. A bit of the red cube is visible through blue cube where it isn’t rendered.
## Additional resources
* [Sprite masks](../sprite/mask/mask-landing.html)A texture which defines which areas of an underlying image to reveal or hide. [More info](../sprite/mask/mask-landing.html)
  See in [Glossary](../Glossary.html#SpriteMask)
* [Sprite mask reference](../sprite/mask/sprite-mask-reference.html)