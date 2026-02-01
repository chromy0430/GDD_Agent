--- 
Source: Unity 6 Manual (PartSysEmissionModule.md)
---

# Emission module reference
The properties in this module affect the rate and timing of [Particle System](class-ParticleSystem.html)A component that simulates fluid entities such as liquids, clouds and flames by generating and animating large numbers of small 2D images in the scene. [More info](class-ParticleSystem.html)
See in [Glossary](Glossary.html#particlesystem) emissions.
## Properties
For some properties in this section, you can use different modes to set their value. For information on the modes you can use, refer to [Vary Particle System properties over time](varying-particle-system-properties-over-time.html).
| **Property** | **Function** |
| --- | --- |
| **Rate over Time** | The number of **particles**A small, simple image or mesh that is emitted by a particle system. A particle system can display and move particles in great numbers to represent a fluid or amorphous entity. The effect of all the particles together creates the impression of the complete entity, such as smoke. [More info](class-ParticleSystem.html) See in [Glossary](Glossary.html#particle) emitted per unit of time. |
| **Rate over Distance** | The number of particles emitted per unit of distance moved. |
| **Bursts** | A burst is an event which spawns particles. These settings allow particles to be emitted at specified times. |
| *Time* | Set the time (in seconds, after the Particle System begins playing) at which to emit the burst. |
| *Count* | Set a value for the number of particles that may be emitted. |
| *Cycles* | Set a value for how many times to play the burst. |
| *Interval* | Set a value for the time (in seconds) between when each cycle of the burst is triggered. |
| *Probability* | Controls how likely it is that each burst event spawns particles. A higher value makes the system produce more particles, and a value of 1 guarantees that the system produces particles. |
## Additional resources
* [Particle emissions and emitters](particle-emissions-emitters.html)