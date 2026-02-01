--- 
Source: Unity 6 URP Manual (2d-renderer-urp-features-landing.html)
---

# 3D GameObjects in 2D URP scenes
Render and sort 3D **GameObjects**The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](../class-GameObject.html)
See in [Glossary](../Glossary.html#GameObject) as if they were 2D **sprites**A 2D graphic objects. If you are used to working in 3D, Sprites are essentially just standard textures but there are special techniques for combining and managing sprite textures for efficiency and convenience during development. [More info](../sprite/sprite-landing.html)
See in [Glossary](../Glossary.html#Sprite) in your 2D URP project.
When Unity renders 3D GameObjects in a 2D **scene**A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](../CreatingScenes.html)
See in [Glossary](../Glossary.html#Scene), it usually renders them clipping into each other on the same z-position. By using the following properties and features, Unity renders the 3D GameObjects as if they were 2D sprites, so that they would overlap each other rather than intersect.
You can use features that usually only work with 2D sprites with these 3D GameObjects, such as allowing these 3D GameObjects to receive lighting from [2D Lights](2d-index.html) by using a compatible **shader**A program that runs on the GPU. [More info](../Shaders.html)
See in [Glossary](../Glossary.html#shader), or interact with [Sprite Masks](../sprite/mask/mask-landing.html)A texture which defines which areas of an underlying image to reveal or hide. [More info](../sprite/mask/mask-landing.html)
See in [Glossary](../Glossary.html#SpriteMask). These 3D GameObjects can also be sorted with sprites in the [2D renderer sorting queue](../2d-renderer-sorting.html) when **Sort 3D As 2D** is enabled in a [Sorting Group](../sprite/sorting-group/sorting-group-landing.html).
| Topic | Description |
| --- | --- |
| [Render 3D GameObjects in 2D scenes](2d-renderer-urp-shader-compatibility.html) | Create custom shaders and materials to render 3D GameObjects in 2D scenes. |
| [Set 3D GameObjects to interact with Sprite masks](2d-renderer-urp-sprite-mask-interaction.html) | Use Sprite masks with 3D GameObjects. |
| [Sort 3D GameObjects with 2D sprites](2d-renderer-urp-sorting-workflows.html) | Sort 3D GameObjects with 2D GameObjects in the same scene and control the order they’re rendered. |