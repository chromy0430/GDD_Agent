--- 
Source: Unity 6 Manual (Playables-Examples.md)
---

# Playables API examples
The **Playables**An API that provides a way to create tools, effects or other gameplay mechanisms by organizing and evaluating data sources in a tree-like structure known as the PlayableGraph. [More info](Playables.html)
See in [Glossary](Glossary.html#Playables) API examples include sample **scripts**A piece of code that allows you to create your own Components, trigger game events, modify Component properties over time and respond to user input in any way you like. [More info](creating-scripts.html)
See in [Glossary](Glossary.html#Scripts) that demonstrate how to perform basic animation tasks such as playing, mixing, and controlling **animation clips**Animation data that can be used for animated characters or simple animations. It is a simple “unit” piece of motion, such as (one specific instance of) “Idle”, “Walk” or “Run”. [More info](class-AnimationClip.html)
See in [Glossary](Glossary.html#AnimationClip) or other playables. The Playables API examples include the following topics:
| **Topic** | **Description** |
| --- | --- |
| **[PlayableGraph Visualizer](playables-visualizer.html)** | The Playable API examples use the PlayableGraph Visualizer package to visualize the result of most scripts. This topic demonstrates how to download and install the PlayableGraph Visualizer package. **Note:** The PlayableGraph Visualizer is a discontinued experimental package that might not work with your version of Unity. |
| **[Play an animation clip](playables-ex-play-clip.html)** | Learn how to create a `PlayableGraph` that plays a single animation clip. |
| **[Blend two animation clips](playables-ex-blend-clips.html)** | Learn how to use a `AnimationMixerPlayable` to blend two animation clips. |
| **[Blend an animation clip with a controller](playables-ex-blend-clip-controller.html)** | Learn how to use a `AnimatorMixerPlayable` to blend an animation clip with an **Animator Controller**Controls animation through Animation Layers with Animation State Machines and Animation Blend Trees, controlled by Animation Parameters. The same Animator Controller can be referenced by multiple models with Animator components. [More info](class-AnimatorController.html) See in [Glossary](Glossary.html#AnimatorController). |
| **[Control the play state](playables-ex-play-state.html)** | Learn about the `Pause()` and `Play()` methods and how to control the play state of a `PlayableGraph`. |
| **[Control the timing of a playable clip](playables-ex-control-timing.html)** | Learn about the `SetTime()` method and how to manually set the start of a paused playable. |
| **[Create a PlayableGraph with different outputs](playables-ex-different-outputs.html)** | Learn how to create a `PlayableGraph` with two different playable output types. |
| **[Create a custom playable](playables-ex-custom-playable.html)** | Learn about the `PlayableBehaviour` public class to create a custom Playable. This example also demonstrate how to override the `PrepareFrame()` virtual method. |
## Additional resources
* [The PlayableGraph, nodes, and output](Playables-Graph.html)
* [Playable struct](../ScriptReference/Playables.Playable.html)
* [Get started with packages](Packages.html)