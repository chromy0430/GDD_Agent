--- 
Source: Unity 6 URP Manual (prebuilt-shader-graphs-urp-decal.html)
---

# Decal shader graph reference for URP
Explore the properties and settings you can use to customize the default Decal **shader**A program that runs on the GPU. [More info](../Shaders.html)
See in [Glossary](../Glossary.html#shader) graph in the Universal **Render Pipeline**A series of operations that take the contents of a Scene, and displays them on a screen. Unity lets you choose from pre-built render pipelines, or write your own. [More info](../render-pipelines.html)
See in [Glossary](../Glossary.html#renderpipeline) (URP).
You can assign a Material that uses a Decal Shader Graph to a **GameObject**The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](../class-GameObject.html)
See in [Glossary](../Glossary.html#GameObject) directly. For example, you can [use a Quad as the Decal GameObject](renderer-feature-decal-create.html#decal-gameobject).
## Contexts
The default **Fragment** Context contains the following Blocks. Which Blocks display might change depending on the [graph settings](https://docs.unity3d.com/Packages/com.unity.shadergraph@latest/index.html?subfolder=/manual/Graph-Settings-Tab.html).
### Fragment Context
| **Input** | **Type** | **Description** |
| --- | --- | --- |
| **Base Color** | Vector3 | Sets the base color of the material. The default is [`Color.grey`](../../ScriptReference/Color-grey.html). |
| **Alpha** | Float | Sets the alpha of the material. The range is 0 to 1. The default is 1. |
| **Normal (Tangent Space)** | Vector3 | Defines the normal of the material in tangent space. |
| **Normal Alpha** | Float | Defines the mask that controls where the decal’s normal displays. |
| **Metallic** | Float | Defines the metallic value of the material, where 0 is non-metallic and 1 is metallic. |
| ****Ambient Occlusion**A method to approximate how much ambient light (light not coming from a specific direction) can hit a point on a surface. See in [Glossary](../Glossary.html#ambientocclusion)** | Float | Defines the ambient occlusion of the material. Expected range 0 - 1. |
| **Smoothness** | Float | Defines the smoothness of the material. Expected range 0 - 1. |
| **MAOS Alpha** | Float | Defines the mask that controls where the decal’s metal, ambient occlusion, and smoothness display. |
## Graph Settings
Explore the shader graph settings you can use to customize the Fragment context.
For more details about graph settings that are common to all shader graph shaders, refer to [Graph Settings tab](https://docs.unity3d.com/Packages/com.unity.shadergraph@latest/index.html?subfolder=/manual/Graph-Settings-Tab.html).
| **Setting** | **Description** |
| --- | --- |
| **Affect BaseColor** | Affects the base color with the shader. Most decals make use of this option. An exception is a surface damage effect, where you might want to manipulate other properties, such as normals. |
| **Affect Normal** | Affects normals with the shader. Use the **Blend** property to blend the normals of the decal with the normals of the surface it’s projected to. If the **Blend** property is disabled, the decal overrides the normals all over the surface it’s projected to. Use case: add damage effects to materials, for example, bullet holes or cracks. |
| **Blend** | Blends the normals of the decal with the normals of the surface it’s projected to. |
| **Affect MAOS** | Affects normals with the shader. Use the **Blend** property to blend the normals of the decal with the normals of the surface it’s projected to. If the **Blend** property is disabled, the decal overrides the normals all over the surface it’s projected to. Use cases:  * Override smoothness to highlight puddles or wet paint. * Override metallic values with lower values to render rust. * Override AO to give the decal more depth. |
| **Affect Emission** | Affects the emission values to make surfaces seem like they are emitting light, or to make surfaces seem like they are being lit by light. |
| **Supports **LOD**The *Level Of Detail* (LOD) technique is an optimization that reduces the number of triangles that Unity has to render for a GameObject when its distance from the Camera increases. [More info](../LevelOfDetail.html) See in [Glossary](../Glossary.html#LOD) Cross Fade** | Allow objects with LODs to cross fade from one LOD to the next without causing issues with decals, ensuring that decals applied to objects cross fading between LODs continue to display correctly. |
| **Angle Fade** | Fades out the effects of the decal at the specified surface normal angle. This prevents decals projected in 2D along a particular axis or direction from stretching. Otherwise, the object’s surface deviates from the decal projection direction. |
| **Custom Editor GUI** | Renders a custom editor GUI in the ****Inspector**A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](../UsingTheInspector.html) See in [Glossary](../Glossary.html#Inspector)** window of the material. Enter the name of the GUI class in the field. For more information, refer to [Control material properties in the Inspector window](../writing-shader-display-types.html). |
## Additional resources
* [Create a decal via a Decal Projector in URP](decal-shader.html)
* [Shader Graph manual](https://docs.unity3d.com/Packages/com.unity.shadergraph@latest)