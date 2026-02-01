--- 
Source: Unity 6 Manual (LightModes-landing.md)
---

# Setting a light as realtime or baked
Resources for setting the **Light Mode** of a Light component, which determines whether Unity calculates light in real time, or stores precalculated light in the build.
| **Page** | **Description** |
| --- | --- |
| [Light Modes](LightModes-introduction.html)A Light property that defines the use of the Light. Can be set to Realtime, Baked and Mixed. [More info](LightModes.html) See in [Glossary](Glossary.html#LightMode) | Compare the differences between **realtime lights**Light components whose Mode property is set to Realtime. Unity calculates and updates the lighting of Realtime Lights every frame at runtime. No Realtime Lights are precomputed. [More info](LightModes-introduction.html#realtime) See in [Glossary](Glossary.html#RealtimeLights), **baked lights**Light components whose Mode property is set to Baked. Unity pre-calculates the illumination from Baked Lights before runtime, and does not include them in any runtime lighting calculations. [More info](LightModes-introduction.html#baked) See in [Glossary](Glossary.html#bakedlights), and mixed lights. |
| [Choose a Light Mode](LightModes-choose.html) | Choose between realtime, baked, and mixed light modes for a Light component. |
| [Set the Mode of a Light component](LightModes.html) | Set the Mode property of a Light component to **Realtime**, **Baked** or **Mixed**. |