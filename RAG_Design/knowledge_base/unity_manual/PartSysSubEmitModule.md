--- 
Source: Unity 6 Manual (PartSysSubEmitModule.md)
---

# Sub Emitters module reference
View and edit the settings for the Sub Emitters module.
Sub emitters are **particle**A small, simple image or mesh that is emitted by a particle system. A particle system can display and move particles in great numbers to represent a fluid or amorphous entity. The effect of all the particles together creates the impression of the complete entity, such as smoke. [More info](class-ParticleSystem.html)
See in [Glossary](Glossary.html#particle) emitters that Unity uses to spawn additional particles at the location of an existing particle.
## Properties
For some properties in this section, you can use different modes to set their value. For information on the modes you can use, refer to [Vary Particle System properties over time](varying-particle-system-properties-over-time.html).
The Sub Emitters module contains the following settings.
| **Property** | **Function** |
| --- | --- |
| **Spawn condition** | Determines when a parent particle emits additional particles. For more information, refer to [Spawn condition dropdown](#spawn-condition). To assign a sub emitter for the spawn condition, use the picker (**⊙**) to select an existing **Particle System**A component that simulates fluid entities such as liquids, clouds and flames by generating and animating large numbers of small 2D images in the scene. [More info](class-ParticleSystem.html) See in [Glossary](Glossary.html#particlesystem) or use the **Add** (**+**) button to create a new one. |
| **Inherit** | Selects which properties to inherit from the parent system. |
| **Emit Probability** | Sets the probability that a parent particle emits new particles. A value of 0 means particles never spawn new particles. A value of 1 means particles always spawn new particles. |
### Spawn condition dropdown
The Spawn condition dropdown contains the following settings.
| **Spawn condition** | **Function** |
| --- | --- |
| **Birth** | Emits particles from the start to the end of a parent particle’s lifetime. |
| ****Collision**A collision occurs when the physics engine detects that the colliders of two GameObjects make contact or overlap, when at least one has a Rigidbody component and is in motion. [More info](CollidersOverview.html) See in [Glossary](Glossary.html#collision)** | Emits particles when a parent particle [collides](particle-collisions.html) with another **GameObject**The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](class-GameObject.html) See in [Glossary](Glossary.html#GameObject). For more information on how to control particle collisions, refer to the [Collision module reference](PartSysCollisionModule.html). |
| **Death** | Emits particles when Unity destroys a parent particle at the end of its lifetime. |
| **Trigger** | Emits particles when a parent particle [interacts with a trigger volume](configure-particle-trigger.html). For more information, refer to [Triggers module reference](PartSysTriggersModule.html). |
| **Manual** | Emits particles only when explicitly triggered by [`ParticleSystem.TriggerSubEmitter`](../ScriptReference/ParticleSystem.TriggerSubEmitter.html). You can trigger this for all particles or just a subset. |
**Note:** In the sub emitter [Emission module](PartSysEmissionModule.html), the **Birth** condition supports all the settings and multiple bursts in the **Bursts** list. The **Collision**, **Death**, **Trigger**, and **Manual** conditions support only a single burst in the **Bursts** list.
## Additional resources
* [Particle emissions and emitters](particle-emissions-emitters.html)