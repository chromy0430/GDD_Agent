--- 
Source: Unity 6 URP Manual (probe-volumes-change-lighting-at-runtime.html)
---

# Changing lighting at runtime
You can change how objects use the baked data in Adaptive Probe Volumes, to create lighting that changes at runtime. For example, you can turn the lights on and off in a **scene**A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](../CreatingScenes.html)
See in [Glossary](../Glossary.html#Scene), or change the time of day.
| Page | Description |
| --- | --- |
| [Choose how to change lighting at runtime](probevolumes-understand-changing-lighting-at-runtime.html) | Choose whether to use Lighting Scenarios or sky occlusion. |
| [Bake different lighting setups with Lighting Scenarios](probevolumes-bakedifferentlightingsetups.html) | Use multiple Lighting Scenarios to store baking results for different scene setups, and switch or blend between them at runtime. |
| [Update light from the sky at runtime with sky occlusion](probevolumes-skyocclusion.html) | Sky occlusion means that when a **GameObject**The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](../class-GameObject.html) See in [Glossary](../Glossary.html#GameObject) samples a color from the sky, Unity dims the color if the light can’t reach the GameObject. |