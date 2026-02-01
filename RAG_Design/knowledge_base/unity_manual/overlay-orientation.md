--- 
Source: Unity 6 Manual (overlay-orientation.md)
---

# Orientation overlay
The Orientation overlay appears in the **Scene**A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](CreatingScenes.html)
See in [Glossary](Glossary.html#Scene) view. This displays the Scene **Camera**A component which creates an image of a particular viewpoint in your scene. The output is either drawn to the screen or captured as a texture. [More info](CamerasOverview.html)
See in [Glossary](Glossary.html#Camera)’s current orientation, and allows you to change the viewing angle and projection mode.
![The scene cameras current orientation](../uploads/Main/Editor-SceneGizmo.png)
The scene camera’s current orientation
The Orientation overlay has a conical arm on each side of the cube. The arms at the forefront are labelled **X**, **Y**, and **Z**. Click on any of the conical axis arms to snap the Scene Camera to the axis it represents (for example: top view, left view, and front view). You can also right-click the cube to see a menu with a list of viewing angles. To return to the default viewing angle, right-click the Orientation overlay and select **Free**.
You can also toggle **Perspective** on and off. This changes the projection mode of the **Scene view**An interactive view into the world you are creating. You use the Scene View to select and position scenery, characters, cameras, lights, and all other types of Game Object. [More info](UsingTheSceneView.html)
See in [Glossary](Glossary.html#SceneView) between **Perspective** and **Orthographic** (sometimes called “isometric”). To do this, click the cube in the center of the Orientation overlay, or the text below it. The Orthographic view has no perspective, and is useful in combination with clicking one of the conical axis arms to get a front, top or side elevation.
![A Scene shown in Perspective mode (left) and Orthographic mode (right) ](../uploads/Main/scene-view-perspect-and-ortho.png)
A Scene shown in Perspective mode (left) and Orthographic mode (right)
![The same Scene viewed in top and right view, in orthographic mode](../uploads/Main/SceneViewOrthoTopAndSide.png)
The same Scene viewed in top and right view, in orthographic mode
If your Scene view is in an awkward viewpoint (upside-down or just an angle you find confusing), **Shift**-click the cube at the center of the Orientation overlay to get back to a **Perspective** view with an angle that looks at the Scene from the side and slightly from above.
Select the padlock icon in the Orientation overlay to enable or disable rotation of the Scene. Once Scene rotation is disabled, right-click to pan the view instead of rotating it.
In **2D Mode**, the Orientation overlay doesn’t appear. The only view option in **2d Mode** is to look perpendicularly at the XY plane.
## Additional resources
* [Position overlays](position-overlay.html)
* [Create and manage overlay presets](manage-overlay-configurations.html)
* [Scene view navigation](SceneViewNavigation.html)