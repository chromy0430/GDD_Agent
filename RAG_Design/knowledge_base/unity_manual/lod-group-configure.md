--- 
Source: Unity 6 Manual (lod-group-configure.md)
---

# Import or create LOD levels for a LOD Group
To import or create **LOD**The *Level Of Detail* (LOD) technique is an optimization that reduces the number of triangles that Unity has to render for a GameObject when its distance from the Camera increases. [More info](LevelOfDetail.html)
See in [Glossary](Glossary.html#LOD) levels for a **LOD Group**A component to manage level of detail (LOD) for GameObjects. [More info](class-LODGroup.html)
See in [Glossary](Glossary.html#LODGroup) component in a **GameObject**The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](class-GameObject.html)
See in [Glossary](Glossary.html#GameObject), use one of the following methods:
* Add a LOD Group component, then manually add a renderer to each LOD level.
* Import a model with LOD levels you created in an external 3D modeling application. Unity adds a LOD Group component to the GameObject and configures it automatically.
## Import LOD levels
Follow these steps:
1. In your external 3D application, follow the application’s process to create as many LOD meshes as you need.
2. Add the suffix `_LODX` to the name of each **mesh**The main graphics primitive of Unity. Meshes make up a large part of your 3D worlds. Unity supports triangulated or Quadrangulated polygon meshes. Nurbs, Nurms, Subdiv surfaces must be converted to polygons. [More info](mesh.html)
   See in [Glossary](Glossary.html#Mesh), where `X` represents the LOD index. For example, use `ExampleMeshName_LOD0` for the most detailed LOD.
   The LOD Group component accepts a maximum of eight LOD levels. Unity uses LOD 0 closest to the **camera**A component which creates an image of a particular viewpoint in your scene. The output is either drawn to the screen or captured as a texture. [More info](CamerasOverview.html)
   See in [Glossary](Glossary.html#Camera), so it should be the most detailed LOD level.
3. Export your model as a .fbx file.
4. Import the .fbx file into Unity.
Unity automatically creates a [LOD Group component](class-LODGroup.html) with the appropriate settings.
## Manually add a LOD Group component and LOD levels
To manually add a LOD Group component and LOD levels to a GameObject, follow these steps:
1. In the **Hierarchy** window, create an empty GameObject.
2. Add child GameObjects for the LOD levels you want, each containing the Renderer components for that LOD level.
3. Select the empty GameObject, then in the **Inspector** window select **Add Component**, then **Rendering** > **LOD Group**.
4. In the **LOD Group** component, select a LOD level box to open the LOD level settings.
5. In the **Renderers** panel, select the **Add** (**+**) button, then select the Renderer picker (**⊙**) or drag and drop to add the child GameObject that contains the Renderers for this LOD level.
6. Repeat steps 4 and 5 for each LOD level.
To add or delete a LOD levels, right-click on the LOD level boxes.
## Configure project-wide LOD settings
To configure LOD settings for all the LOD Groups in your project, use the following settings in the [Quality settings](class-QualitySettings.html) window:
* **Maximum LOD Level**: Exclude meshes above a specified LOD level from your build.
* **LOD Bias**: Determine whether to favor higher or lower LOD levels at threshold distances.
## Additional resources
* [LOD Group component reference](class-LODGroup.html)
* [Make LOD transitions smooth in LOD Group](lod/lod-transitions-lod-group.html)
* [Importing models](https://docs.unity3d.com/Manual/ImportingModelFiles.html).
* [Creating LODs in Maya](https://learn.unity.com/tutorial/creating-lods-in-maya-for-unity)