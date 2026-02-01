--- 
Source: Unity 6 Manual (class-LensFlare.md)
---

# Lens Flare component reference
[Switch to Scripting](../ScriptReference/LensFlare.html "Go to LensFlare page in the Scripting Reference")
Explore the properties in the **Lens Flare** component to create a lens flare with a [Flare asset](class-Flare.html).
| ***Property:*** | ***Function:*** |
| --- | --- |
| **Flare** | The [Flare asset](class-Flare.html) to render.  **Note**: The other properties in the Lens Flare Inspector are stored in this Flare asset. They are not stored in the Lens Flare component. |
| **Color** | The color to tint the Flare to. You can use this to make the lens flare better fit the **Scene**A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](CreatingScenes.html) See in [Glossary](Glossary.html#Scene)’s mood. |
| **Brightness** | The size and brightness the lens flare appears. If you use a very bright lens flare, make sure its direction fits with your Scene’s primary light source. Can only affect properties that Flare has enabled. |
| **Fade Speed** | The speed at which Unity fades the lens flare in and out. |
| **Ignore Layers** | A mask that determins which Layers can see the lens flare. |
| **Directional** | Indicates whether Unity orients the Flare along the positive z-axis of the **GameObject**The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](class-GameObject.html) See in [Glossary](Glossary.html#GameObject). It appears as if it was infinitely far away, and does not track the GameObject’s position, only the direction of its z-axis. |
LensFlare