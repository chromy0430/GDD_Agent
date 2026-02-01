--- 
Source: Unity 6 Manual (shader-pso-example.md)
---

# PSO tracing and warming example
Get started with PSO tracing and warm up using the Universal **Render Pipeline**A series of operations that take the contents of a Scene, and displays them on a screen. Unity lets you choose from pre-built render pipelines, or write your own. [More info](render-pipelines.html)
See in [Glossary](Glossary.html#renderpipeline) (URP) sample.
**Important**: `GraphicsStateCollection` is an experimental API and might be changed or removed in the future.
The Universal 3D sample uses the `GraphicsStateCollection` API. You can use this sample to help you get started with PSO tracing and warming methods. For more information about creating a project from the Universal 3D sample, refer to [Create a new project that uses URP](urp/creating-a-new-project-with-urp.html).
## Sample script reference
The following table outlines the key PSO tracing and warming **scripts**A piece of code that allows you to create your own Components, trigger game events, modify Component properties over time and respond to user input in any way you like. [More info](creating-scripts.html)
See in [Glossary](Glossary.html#Scripts) used in this sample and their function:
| **Script** | **Description** |
| --- | --- |
| `Assets/SharedAssets/Scripts/Runtime/GraphicsStateCollectionManager.cs` | Performs PSO tracing and warmup at runtime. Holds a list of recorded collections. |
| `Assets/SharedAssets/Scripts/Editor/GraphicsStateCollectionStripper.cs` | Ensures the build only includes the relevant collections for the target platform. The sample project targets multiple platforms and quality levels, so it contains multiple collections under the `Assets/SharedAssets/GraphicsStateCollections` folder. The filtering script removes unneeded collections for the target platform to reduce build size. |
| `Assets/SharedAssets/Scripts/Editor/GraphicsStateCollectionCombiner.cs` | Utility script that combines multiple selected collection files into one. Unity uses the first collection you select as the result collection. **Note**: This script combines collections that match the platform, graphics API, and quality level. |
### Trace and warm up with the URP sample project
To trace and warm up PSOs with the sample project:
1. Open the main terminal **scene**A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](CreatingScenes.html)
   See in [Glossary](Glossary.html#Scene) from `Assets/Scenes/Terminal/TerminalScene.unity`.
2. Add an empty **GameObject**The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](class-GameObject.html)
   See in [Glossary](Glossary.html#GameObject) to the scene.
3. Open your empty GameObject in the ****Inspector**A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](UsingTheInspector.html)
   See in [Glossary](Glossary.html#Inspector)**, select **Add Component** and add the **Graphics State Collection Manager** component.
4. Set the **Mode** property of the **Graphics State Collection Manager** to **Warm Up**.
5. Open the **More** (⋮) menu next to the **Graphics State Collection Manager**. Select **Update collection list** to populate the collection list with the collections from the `GraphicsStateCollections` folder.
6. Save the scene and project.
7. Build and run the Player, targeting either Windows and the DirectX 12 or Vulkan graphics API, or OSX and the Metal graphics API.
When you load the scene in the Player, Unity will now perform PSO warmup automatically.
## Additional resources
* [Introduction to PSO tracing and warming](shader-pso-introduction.html)