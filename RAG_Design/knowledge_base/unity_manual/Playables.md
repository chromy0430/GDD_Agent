--- 
Source: Unity 6 Manual (Playables.md)
---

# Playables API
Use the **Playables** API to dynamically blend animation, create gameplay mechanism, or other complex behaviors by organizing and evaluating data sources in a `PlayableGraph`.
The Playables API refers to a set of classes, structs, and methods that you use to create the PlayableGraph, its nodes, and outputs. Playables and the Playables API complement the Mecanim animation system.
The Scripting Reference on playables contains the list of classes, structs, and methods that you use to interact with animation, audio, and **scripts**A piece of code that allows you to create your own Components, trigger game events, modify Component properties over time and respond to user input in any way you like. [More info](creating-scripts.html)
See in [Glossary](Glossary.html#Scripts). You can also create custom playables and script playables.
Use the Playables API to do the following:
* Dynamically blend animation.
* Play an **animation clip**Animation data that can be used for animated characters or simple animations. It is a simple “unit” piece of motion, such as (one specific instance of) “Idle”, “Walk” or “Run”. [More info](class-AnimationClip.html)
  See in [Glossary](Glossary.html#AnimationClip) without having to create and manage an **Animator Controller**Controls animation through Animation Layers with Animation State Machines and Animation Blend Trees, controlled by Animation Parameters. The same Animator Controller can be referenced by multiple models with Animator components. [More info](class-AnimatorController.html)
  See in [Glossary](Glossary.html#AnimatorController) asset.
* Dynamically create blend graphs and control blend weights.
* Dynamically add or adjust playable nodes at runtime instead of creating a complex static graph that accounts for all possible outcomes. For example, if you have a **GameObject**The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](class-GameObject.html)
  See in [Glossary](Glossary.html#GameObject) with animation clips for interacting with a weapon, chest, and trap, you can use playables to dynamically transition and play the appropriate animation when the GameObject is near the weapon, chest, or trap.
The following topics provide details and examples on how to use the Playables API:
| **Topic** | **Description** |
| --- | --- |
| **[PlayableGraph, nodes, and output](Playables-Graph.html)** | Describes the PlayableGraph and its main parts including the graph itself, its playable nodes, and playable outputs. |
| **[ScriptPlayable and PlayableBehaviour](Playables-ScriptPlayable.html)** | Describes the `ScriptPlayable<>` object, the `PlayableBehaviour` custom behavior and how to use them together to create custom playables. |
| **[Playable Director component](class-PlayableDirector.html)** | Describes the Playable Director component which controls the playback and timing of a PlayableGraph. The Playable Director component is primarily used by the [Unity Timeline package](https://docs.unity3d.com/Packages/com.unity.timeline@latest). |
| **[Playables API examples](Playables-Examples.html)** | Provides example scripts that demonstrate how to use the Playables API. |
# Additional resources
* [Programming in Unity](scripting.html)
* [Playable struct](../ScriptReference/Playables.Playable.html)
* [Mecanim Animation system](AnimationOverview.html)