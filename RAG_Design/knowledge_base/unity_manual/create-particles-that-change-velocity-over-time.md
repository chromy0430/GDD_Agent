--- 
Source: Unity 6 Manual (create-particles-that-change-velocity-over-time.md)
---

# Create particles that change velocity over time
To create **particles**A small, simple image or mesh that is emitted by a particle system. A particle system can display and move particles in great numbers to represent a fluid or amorphous entity. The effect of all the particles together creates the impression of the complete entity, such as smoke. [More info](class-ParticleSystem.html)
See in [Glossary](Glossary.html#particle) that drift in a particular direction, use the [Velocity over Lifetime](PartSysVelOverLifeModule.html) module’s Linear X, Y and Z curves.
To create effects with particles that spin around a center position, use the use the [Velocity over Lifetime](PartSysVelOverLifeModule.html) module’s **Orbital** velocity values. Additionally, you can propel particles towards or away from a center position using the **Radial** velocity values. You can define a custom center of rotation for each particle by using the **Offset** value.
You can also use the [Velocity over Lifetime](PartSysVelOverLifeModule.html) module to adjust the speed of the particles in the **Particle System**A component that simulates fluid entities such as liquids, clouds and flames by generating and animating large numbers of small 2D images in the scene. [More info](class-ParticleSystem.html)
See in [Glossary](Glossary.html#particlesystem) without affecting their direction, by leaving all the above values at zero and only modifying the **Speed Modifier** value.