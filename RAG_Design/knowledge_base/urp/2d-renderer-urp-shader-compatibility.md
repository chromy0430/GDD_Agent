--- 
Source: Unity 6 URP Manual (2d-renderer-urp-shader-compatibility.html)
---

# Render 3D GameObjects in 2D scenes
To render a 3D **GameObject**The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](../class-GameObject.html)
See in [Glossary](../Glossary.html#GameObject) in a 2D Universal **Render Pipeline**A series of operations that take the contents of a Scene, and displays them on a screen. Unity lets you choose from pre-built render pipelines, or write your own. [More info](../render-pipelines.html)
See in [Glossary](../Glossary.html#renderpipeline) (URP) **scene**A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](../CreatingScenes.html)
See in [Glossary](../Glossary.html#Scene), set its **Mesh**The main graphics primitive of Unity. Meshes make up a large part of your 3D worlds. Unity supports triangulated or Quadrangulated polygon meshes. Nurbs, Nurms, Subdiv surfaces must be converted to polygons. [More info](../mesh.html)
See in [Glossary](../Glossary.html#Mesh) Renderer component to be compatible with 2D scenes. This makes the 3D GameObject use 2D features like [2D lighting in URP](2d-index.html).
Use either of the following approaches:
* Create a 3D GameObject in a 2D URP project.
* Create a custom **shader**A program that runs on the GPU. [More info](../Shaders.html)
  See in [Glossary](../Glossary.html#shader) in Shader Graph.
## Create a 3D GameObject in a 2D URP project
When you create a 3D GameObject in a 2D URP project, Unity automatically assigns the **Mesh2D-Lit-Default** material. This material makes the GameObject compatible with 2D Lights.
## Add the default material to a 3D GameObject
To add the default **Mesh2D-Lit-Default** material to an existing 3D GameObject, follow these steps:
1. Select the 3D GameObject.
2. In the ****Inspector**A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](../UsingTheInspector.html)
   See in [Glossary](../Glossary.html#Inspector)** window, go to the ****Mesh Renderer**A mesh component that takes the geometry from the Mesh Filter and renders it at the position defined by the object’s Transform component. [More info](../class-MeshRenderer.html)
   See in [Glossary](../Glossary.html#MeshRenderer)** or **Skinned Mesh Renderer** component.
3. Open the **Materials** dropdown, then select the Material picker (**⊙**).
4. Select **Mesh2D-Lit-Default**.
## Create a compatible custom shader in Shader Graph
To create a compatible shader in Shader Graph for a Mesh Renderer or Skinned Mesh Renderer, follow these steps:
1. From the main menu, select **Assets** > **Create** > **Shader Graph** > **URP**, then either **Sprite Lit Shader Graph**, **Sprite Unlit Shader Graph**, or **Sprite Custom Lit Shader Graph**.
2. Open the [Graph Inspector](https://docs.unity3d.com/Packages/com.unity.shadergraph@laetst?subfolder=/manual/Internal-Inspector.html), then in the **Graph Settings** enable **Sort 3D As 2D Compatible**.
3. Complete and save your shader. Refer to the [Shader Graph package documentation](https://docs.unity3d.com/Packages/com.unity.shadergraph@latest?) for more information.
4. In the **Inspector** window of a 3D GameObject, apply the new custom material to the Mesh Renderer component or Skinned Mesh Renderer component.
## Additional resources
* [Shader Graph package documentation](https://docs.unity3d.com/Packages/com.unity.shadergraph@latest)
* [2D lighting in URP](2d-index.html)
* [2D Renderer asset component reference for URP](2DRendererData-overview.html)