--- 
Source: Unity 6 URP Manual (prebuilt-shader-graphs-urp-sprite-unlit.html)
---

# Sprite Unlit shader graph reference for URP
Explore the properties and settings you can use to customize the default **Sprite**A 2D graphic objects. If you are used to working in 3D, Sprites are essentially just standard textures but there are special techniques for combining and managing sprite textures for efficiency and convenience during development. [More info](../sprite/sprite-landing.html)
See in [Glossary](../Glossary.html#Sprite) Unlit **shader**A program that runs on the GPU. [More info](../Shaders.html)
See in [Glossary](../Glossary.html#shader) graph in the Universal **Render Pipeline**A series of operations that take the contents of a Scene, and displays them on a screen. Unity lets you choose from pre-built render pipelines, or write your own. [More info](../render-pipelines.html)
See in [Glossary](../Glossary.html#renderpipeline) (URP).
For more information about 2D shaders in URP, refer to [2D Lighting in URP](2d-index.html).
## Contexts
The default **Vertex** and **Fragment** Contexts contain the following Blocks. Which Blocks display might change depending on the [graph settings](https://docs.unity3d.com/Packages/com.unity.shadergraph@latest/index.html?subfolder=/manual/Graph-Settings-Tab.html).
### Vertex Context
The default values are the values from the **mesh**The main graphics primitive of Unity. Meshes make up a large part of your 3D worlds. Unity supports triangulated or Quadrangulated polygon meshes. Nurbs, Nurms, Subdiv surfaces must be converted to polygons. [More info](../mesh.html)
See in [Glossary](../Glossary.html#Mesh).
| **Input** | **Type** | **Description** |
| --- | --- | --- |
| **Position** | Vector3 | Sets the vertex position in object space. |
| **Normal** | Vector3 | Sets the normal of the vertex in object space. |
| **Tangent** | Vector3 | Sets the tangent of the vertex in object space. |
### Fragment Context
| **Input** | **Type** | **Description** |
| --- | --- | --- |
| **Base Color** | Vector3 | Sets the base color of the material. The default is [`Color.grey`](../../ScriptReference/Color-grey.html). |
| **Alpha** | Float | Sets the alpha of the material. The range is 0 to 1. The default is 1. |
| **Alpha Clip Threshold** | Float | Sets the minimum alpha value for a **pixel**The smallest unit in a computer image. Pixel size depends on your screen resolution. Pixel lighting is calculated at every screen pixel. [More info](../ShadowPerformance.html) See in [Glossary](../Glossary.html#pixel) to be visible. The range is 0 to 1. The default is 0.5. This property is only available if you enable **Alpha Clipping** in the graph settings. |
## Graph Settings
Explore the shader graph settings you can use to customize the Fragment and Vertex contexts.
For more details about graph settings that are common to all shader graph shaders, refer to [Graph Settings tab](https://docs.unity3d.com/Packages/com.unity.shadergraph@latest/index.html?subfolder=/manual/Graph-Settings-Tab.html).
| **Setting** | **Description** |
| --- | --- |
| **Blending Mode** | Sets how the shader blends the color of a transparent material with the background. The options are:  * **Alpha**: Calculates transparency using the alpha value of the material. * **Premultiply**: Calculates transparency using the alpha value of the material, but multiplies the RGB values by the alpha value first. * **Additive**: Adds the color of the material to the background color. * **Multiply**: Multiplies the color of the material with the background color.  For more information about blending modes, refer to [Blend modes](2d-light-blend-modes.html). |
| **Depth Write** | Determines whether the shader writes depth information to the depth buffer. The options are:  * **Auto**: Sets opaque objects to write to the depth buffer, and transparent objects to not write to the depth buffer. * **Force Enabled**: Enables all objects from writing to the depth buffer. * **Force Disabled**: Disables all objects from writing to the depth buffer. |
| **Alpha Clipping** | Discards pixels if their alpha value is lower than a threshold value. Enabling this setting adds the **Alpha Clip Threshold** Block to the Fragment context. |
| **Disable Color Tint** | Prevents Shader Graph tinting the sprite with the **Color** property of the sprite. If you enable this setting, use a [Vertex Color Node](https://docs.unity3d.com/Packages/com.unity.shadergraph@latest/index.html?subfolder=/manual/Vertex-Color-Node.html) to access the **Color** property of the sprite. |
| **Sort 3D as 2D Compatible** | Uses 2D sorting rules to draw **3D objects**A 3D GameObject such as a cube, terrain or ragdoll. [More info](../GameObjects.html) See in [Glossary](../Glossary.html#3DObject), to avoid **2D objects**A 2D GameObject such as a tilemap or sprite. [More info](../Unity2D.html) See in [Glossary](../Glossary.html#2DObject) appearing at the wrong depth. |
| **Custom Editor GUI** | Renders a custom editor GUI in the ****Inspector**A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](../UsingTheInspector.html) See in [Glossary](../Glossary.html#Inspector)** window of the material. Enter the name of the GUI class in the field. For more information, refer to [Control material properties in the Inspector window](../writing-shader-display-types.html). |
## Additional resources
* [2D lighting in URP](2d-index.html)
* [20 advanced 2D shader effects - part 1](https://www.youtube.com/watch?v=wav3YUcqUCA)