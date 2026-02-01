--- 
Source: Unity 6 Manual (PartSysSizeBySpeedModule.md)
---

# Size by Speed module reference
This module allows you to create **particles**A small, simple image or mesh that is emitted by a particle system. A particle system can display and move particles in great numbers to represent a fluid or amorphous entity. The effect of all the particles together creates the impression of the complete entity, such as smoke. [More info](class-ParticleSystem.html)
See in [Glossary](Glossary.html#particle) that change size according to their speed in distance units per second.
## Properties
For some properties in this section, you can use different modes to set their value. For information on the modes you can use, refer to [Vary Particle System properties over time](varying-particle-system-properties-over-time.html).
| ***Property*** | ***Function*** |
| --- | --- |
| **Separate Axes** | Control the particle size independently on each axis. |
| **Size** | A curve defining the particle’s size over a speed range. |
| **Speed Range** | The low and high ends of the speed range to which the size curve is mapped (speeds outside the range will map to the end points of the curve). |
## Additional resources
* [Particle size](particle-size.html)