--- 
Source: Unity 6 URP Manual (2d-renderer-urp-sorting-workflows.html)
---

# Sort 3D GameObjects with 2D sprites
Sort 3D **GameObjects**The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](../class-GameObject.html)
See in [Glossary](../Glossary.html#GameObject) with 2D **sprites**A 2D graphic objects. If you are used to working in 3D, Sprites are essentially just standard textures but there are special techniques for combining and managing sprite textures for efficiency and convenience during development. [More info](../sprite/sprite-landing.html)
See in [Glossary](../Glossary.html#Sprite) in the same **scene**A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](../CreatingScenes.html)
See in [Glossary](../Glossary.html#Scene).
When you enable the **Sort as 2D** property, if 3D meshes have the same depth, Unity renders them like overlapping 2D sprites instead of intersecting meshes.
Follow these steps:
1. Add a [Sorting Group](../sprite/sorting-group/sorting-group-landing.html) component to the 3D GameObject.
2. Enable **Sort as 2D** in the **Sorting Group** property settings.
3. Assign [Sorting Layers and Order in Layer](../2d-renderer-sorting.html#sortlayer) values to determine the 3D renderer’s position in the render queue.
**Important:** Enabling the **Sort as 2D** setting clears the object’s depth information which means you cannot use it with depth-based **post-processing**A process that improves product visuals by applying filters and effects before the image appears on screen. You can use post-processing effects to simulate physical camera and film properties, for example Bloom and Depth of Field. [More info](../PostProcessingOverview.html) post processing, postprocessing, postprocess
See in [Glossary](../Glossary.html#post-processing) effects. If you want to use these kind of effects, use Unity’s default behavior that renders sprites and meshes based on their [world-space depth](../2d-renderer-sorting.html#cameradistance).
## Additional resources
* [2D Renderer sorting](../2d-renderer-sorting.html)
* [Sorting groups](../sprite/sorting-group/sorting-group-landing.html)