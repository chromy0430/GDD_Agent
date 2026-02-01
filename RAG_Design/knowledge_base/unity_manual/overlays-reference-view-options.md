--- 
Source: Unity 6 Manual (overlays-reference-view-options.md)
---

# View Options overlay reference
Change what the ****Scene**A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](CreatingScenes.html)
See in [Glossary](Glossary.html#Scene)** view displays.
These controls only affect the **Scene** view during development and have no effect on the built game.
![The View Options overlay with all effects, hidden objects, and gizmos selected](../uploads/Main/ViewOptionsOverlay.png)
The View Options overlay with all effects, hidden objects, and gizmos selected
| **View option** | **Description** |
| --- | --- |
| **2D** | View the scene in 2D or 3D. In 2D mode, the **camera**A component which creates an image of a particular viewpoint in your scene. The output is either drawn to the screen or captured as a texture. [More info](CamerasOverview.html) See in [Glossary](Glossary.html#Camera) looks towards positive z, with the x-axis pointing right and the y-axis pointing up. |
| **Audio** | Enable or disable audio. |
| **Effects** | Enable or disable rendering effects. Use the dropdown to select the following effects: Enable or disable rendering effects. Use the dropdown to select from the following effects:  * **Skybox**: Show a skybox texture as the scene’s background. * **Clouds**: Shows cloud layers and volumetric clouds. Only available when using an SRP that supports clouds. * **Fog**: Gradually fade the view to a flat color with distance from the camera. * **Flares**: Lens flares on lights. * **Always Refresh**: Display the animation of animated materials, such as grass waving on a Terrain. * **Post Processing**: Show [Post-processing](PostProcessingOverview.html)A process that improves product visuals by applying filters and effects before the image appears on screen. You can use post-processing effects to simulate physical camera and film properties, for example Bloom and Depth of Field. [More info](PostProcessingOverview.html) post processing, postprocessing, postprocess See in [Glossary](Glossary.html#post-processing) effects. * **Particle Systems**: Show [Particle System](ParticleSystems.html)A component that simulates fluid entities such as liquids, clouds and flames by generating and animating large numbers of small 2D images in the scene. [More info](class-ParticleSystem.html) See in [Glossary](Glossary.html#particlesystem) effects. |
| **Scene Visibility** | Show or hide all hidden **GameObjects**The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](class-GameObject.html) See in [Glossary](Glossary.html#GameObject) (GameObjects marked as not visible in the **Hierarchy** window). For more information, refer to [Scene Visibility](SceneVisibility.html). |
| **Layers** | Select which layers to display. For more information, refer to [Layers](Layers.html)Layers in Unity can be used to selectively opt groups of GameObjects in or out of certain processes or calculations. This includes camera rendering, lighting, physics collisions, or custom calculations in your own code. [More info](Layers.html) See in [Glossary](Glossary.html#layer). |
| **Camera Settings** | Configure the **Scene view**An interactive view into the world you are creating. You use the Scene View to select and position scenery, characters, cameras, lights, and all other types of Game Object. [More info](UsingTheSceneView.html) See in [Glossary](Glossary.html#SceneView) Camera. For more information, refer to [Scene view Camera](SceneViewCamera.html). |
| ****Gizmos**A graphic overlay associated with a GameObject in a Scene, and displayed in the Scene View. Built-in scene tools such as the move tool are Gizmos, and you can create custom Gizmos using textures or scripting. Some Gizmos are only drawn when the GameObject is selected, while other Gizmos are drawn by the Editor regardless of which GameObjects are selected. [More info](GizmosMenu.html#GizmosIcons) See in [Glossary](Glossary.html#Gizmo)** | Enable or disable gizmos. Use the dropdown to select individual gizmos, or the **Gizmos** button for all gizmos. For more information, refer to [Gizmos Menu](GizmosMenu.html). |
## Additional resources
* [Overlays](overlays.html)
* [Display or hide an overlay](display-and-hide-overlay.html)
* [Display or hide an overlay](display-and-hide-overlay.html)
* [Create and manage overlay presets](manage-overlay-configurations.html)
* [Layers](Layers.html)