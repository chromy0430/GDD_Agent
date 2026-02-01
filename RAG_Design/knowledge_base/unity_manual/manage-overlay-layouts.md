--- 
Source: Unity 6 Manual (manage-overlay-layouts.md)
---

# Change the layout of an overlay
You can change the layout of each overlay to make it take up more or less space in the **Scene**A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](CreatingScenes.html)
See in [Glossary](Glossary.html#Scene) view.
## Dock an overlay
You can also dock overlays to the side of the **Scene view**An interactive view into the world you are creating. You use the Scene View to select and position scenery, characters, cameras, lights, and all other types of Game Object. [More info](UsingTheSceneView.html)
See in [Glossary](Glossary.html#SceneView) in the following ways.
You can set an overlay to display in one of the following layouts:
* **Panel**: Displays all the overlay’s content and its label. This mode only works with overlays that aren’t docked to the horizontal or vertical Scene view **toolbar**A row of buttons and basic controls at the top of the Unity Editor that allows you to interact with the Editor in various ways (e.g. scaling, translation). [More info](Toolbar.html)
  See in [Glossary](Glossary.html#toolbar).
* **Horizontal**: Displays the overlay’s content in a horizontal container. An overlay set to the Horizontal layout doesn’t display its label.
* **Vertical**: Displays the overlay’s content in a vertical container. An overlay set to the Vertical layout doesn’t display its label.
In each layout, you can collapse or expand the overlay. A collapsed overlay displays only its icon and a downward facing arrow. Select the arrow to display the content of the overlay. If the overlay has no icon, the icon of the collapsed container is the first two letters of the overlay’s label. To change an overlay to collapsed or expanded, follow the same steps as for changing the layout.
Overlays that aren’t toolbars, such as the [Orientation overlay](overlay-orientation.html), can’t use the Horizontal or Vertical layouts.
To save an overlay configuration, refer to [Create and manage overlay presets](manage-overlay-configurations.html).
To change the layout of an overlay:
1. Right-click the handle (**=**) of an overlay.
2. Select a layout:
   * You can select any layout for overlays that aren’t docked in the horizontal or vertical Scene view toolbar.
   * If the overlay is docked in the horizontal or vertical Scene view toolbar, you can only expand or collapse the overlay.
## Expand an overlay
To expand a collapsed overlay, right-click the handle (**=**) of a collapsed overlay and select **Expand**.
## Additional resources
* [Overlays](overlays.html)
* [Position overlays](position-overlay.html)
* [Create and manage overlay presets](manage-overlay-configurations.html).