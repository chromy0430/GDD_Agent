--- 
Source: Unity 6 Manual (lighting-mode-landing.md)
---

# Configuring Mixed lights with Lighting Modes
Resources for setting the **Lighting Mode** of a **scene**A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](CreatingScenes.html)
See in [Glossary](Glossary.html#Scene), which determines the behaviour of Light components with ****Light Mode**A Light property that defines the use of the Light. Can be set to Realtime, Baked and Mixed. [More info](LightModes.html)
See in [Glossary](Glossary.html#LightMode)** set to **Mixed**.
| **Page** | **Description** |
| --- | --- |
| [Lighting Modes](lighting-mode.html) | Compare **Lighting Mode** options. |
| [Set the Lighting Mode of a scene](LightMode-Scene.html) | Use a Lighting Settings Asset to set the Lighting Mode for a scene. |
| [Adjust Mixed Mode lights at runtime](lighting-mode-runtime.html) | Make subtle changes to lighting when you set **Lighting Mode** to **Baked Indirect**. |
| [Troubleshooting objects appearing unlit or darker than intended](ts-mixed-lights-render-as-baked.html) | Troubleshoot issues causing mixed lights to be rendered as **baked lights**Light components whose Mode property is set to Baked. Unity pre-calculates the illumination from Baked Lights before runtime, and does not include them in any runtime lighting calculations. [More info](LightModes-introduction.html#baked) See in [Glossary](Glossary.html#bakedlights) and causing objects and the scene to appear unlit or darker than intended. |