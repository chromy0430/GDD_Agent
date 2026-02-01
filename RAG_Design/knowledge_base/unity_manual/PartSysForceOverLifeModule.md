--- 
Source: Unity 6 Manual (PartSysForceOverLifeModule.md)
---

# Force over Lifetime module reference
Particles can be accelerated by forces (such as wind or attraction) that are specified in this module.
## Properties
For some properties in this section, you can use different modes to set their value. For information on the modes you can use, refer to [Vary Particle System properties over time](varying-particle-system-properties-over-time.html).
| ***Property*** | ***Function*** |
| --- | --- |
| **X, Y, Z** | Force applied to each **particle**A small, simple image or mesh that is emitted by a particle system. A particle system can display and move particles in great numbers to represent a fluid or amorphous entity. The effect of all the particles together creates the impression of the complete entity, such as smoke. [More info](class-ParticleSystem.html) See in [Glossary](Glossary.html#particle) in the X, Y and Z axes. |
| **Space** | Selects whether the force is applied in local or world space. |
| **Randomize** | When using the Two Constants or Two Curves modes, this causes a new force direction to be chosen on each frame within the defined ranges. This causes more turbulent, erratic movement. |
## Additional resources
* [Particle physics forces](particle-physics-forces.html)