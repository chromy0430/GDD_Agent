--- 
Source: Unity 6 Manual (class-Flare.md)
---

# Flare asset reference
[Switch to Scripting](../ScriptReference/Flare.html "Go to Flare page in the Scripting Reference")
Explore the properties in the Flare asset to create and configure a Flare.
| **Property** | **Function** |
| --- | --- |
| **Elements** | The number of Flare images included in the Flare. |
| **Image Index** | Which Flare image to use from the **Flare Texture** for this Element. |
| **Position** | The Element’s offset along a line running from the containing **GameObject**The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](class-GameObject.html) See in [Glossary](Glossary.html#GameObject)’s position through the screen center. 0 = GameObject position, 1 = screen center. |
| **Size** | The size of the element. |
| **Color** | Color tint of the element. |
| **Use Light Color** | If the Flare is attached to a Light, enabling this will tint the Flare with the Light’s color. |
| **Rotate** | If enabled, bottom of the Element will always face the center of the screen, making the Element spin as the **Lens Flare**A component that simulates the effect of lights refracting inside a camera lens. Use a Lens Flare to represent very bright lights or add atmosphere to your scene. [More info](class-LensFlare.html) See in [Glossary](Glossary.html#LensFlare) moves around on the screen. |
| **Zoom**A camera control that lets you scale the view on your screen. To zoom a camera in the Unity Editor, press Alt + right click and drag. [More info](SceneViewNavigation.html) See in [Glossary](Glossary.html#zoom) | If enabled, the Element will scale up when it becomes visible and scale down again when it isn’t. |
| **Fade** | If enabled, the Element will fade in to full strength when it becomes visible and fade out when it isn’t. |
| **Flare Texture** | A texture containing images used by this Flare’s **Elements**. It must be arranged according to one of the **TextureLayout** options. |
| **Texture Layout** | How the individual Flare Element images are laid out inside the **Flare Texture** (see [Configuring Flare Elements: Understand texture layouts](configuring-flare-elements.html#texture-layouts) for further details). |
| **Use Fog** | If enabled, the Flare will fade away with distance fog. This is used commonly for small Flares. |