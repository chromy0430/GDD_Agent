--- 
Source: Unity 6 Manual (PartSysInheritVelocity.md)
---

# Inherit Velocity module reference
Use this module on subemitters. Each **particle**A small, simple image or mesh that is emitted by a particle system. A particle system can display and move particles in great numbers to represent a fluid or amorphous entity. The effect of all the particles together creates the impression of the complete entity, such as smoke. [More info](class-ParticleSystem.html)
See in [Glossary](Glossary.html#particle) in the parent system can spawn particles in the subemitter. This module reads the velocity from the parent particle and controls how the speed of the subemitter particles reacts to that velocity over time.
## Properties
For some properties in this section, you can use different modes to set their value. For information on the modes you can use, refer to [Vary Particle System properties over time](varying-particle-system-properties-over-time.html).
| **Property** | **Function** |
| --- | --- |
| **Mode** | Specifies how the emitter velocity is applied to particles |
| Current | The emitter’s current velocity will be applied to all particles on every frame. For example, if the emitter slows down, all particles will also slow down. |
| Initial | The emitter’s velocity will be applied once, when each particle is born. Any changes to the emitter’s velocity made after a particle is born will not affect that particle. |
| **Multiplier** | The proportion of the emitter’s velocity that the particle should inherit. |
## Additional resources
* [Particle velocity](particle-velocity.html)
* [Create particles that change velocity over time](create-particles-that-change-velocity-over-time.html)