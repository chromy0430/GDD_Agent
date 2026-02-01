--- 
Source: Unity 6 Manual (PartSysLimitVelOverLifeModule.md)
---

# Limit Velocity over Lifetime module reference
This module controls how the speed of **particles**A small, simple image or mesh that is emitted by a particle system. A particle system can display and move particles in great numbers to represent a fluid or amorphous entity. The effect of all the particles together creates the impression of the complete entity, such as smoke. [More info](class-ParticleSystem.html)
See in [Glossary](Glossary.html#particle) is reduced over their lifetime.
## Properties
For some properties in this section, you can use different modes to set their value. For information on the modes you can use, refer to [Vary Particle System properties over time](varying-particle-system-properties-over-time.html).
| **Property** | **Function** |
| --- | --- |
| **Separate Axes** | Splits the axes up into separate X, Y and Z components. |
| **Speed** | Sets the speed limit of the particles. |
| **Space** | Selects whether the speed limitation refers to local or world space. This option is only available when **Separate Axes** is enabled. |
| **Dampen** | The fraction by which a particle’s speed is reduced when it exceeds the speed limit. |
| **Drag** | Applies linear drag to the particle velocities. |
| **Multiply by Size** | When enabled, larger particles are affected more by the drag coefficient. |
| **Multiply by Velocity** | When enabled, faster particles are affected more by the drag coefficient. |
## Additional resources
* [Particle velocity](particle-velocity.html)
* [Create particles that change velocity over time](create-particles-that-change-velocity-over-time.html)