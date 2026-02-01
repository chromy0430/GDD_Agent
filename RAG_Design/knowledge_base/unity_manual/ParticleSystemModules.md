--- 
Source: Unity 6 Manual (ParticleSystemModules.md)
---

# Particle System module component reference
The [Particle System](class-ParticleSystem.html)A component that simulates fluid entities such as liquids, clouds and flames by generating and animating large numbers of small 2D images in the scene. [More info](class-ParticleSystem.html)
See in [Glossary](Glossary.html#particlesystem) component has a powerful set of properties that are organized into modules for ease of use. This section of the manual covers each of the modules in detail.
| **Topic** | **Description** |
| --- | --- |
| [Activate and access component modules](activate-access-particle-system-modules.html) | Activate component modules on a **Particle**A small, simple image or mesh that is emitted by a particle system. A particle system can display and move particles in great numbers to represent a fluid or amorphous entity. The effect of all the particles together creates the impression of the complete entity, such as smoke. [More info](class-ParticleSystem.html) See in [Glossary](Glossary.html#particle) System to access and change the properties of particles and emitters. |
| [Main module reference](PartSysMainModule.html) | Explore properties on the Main module, to configure the initial state of new particles. |
| [Emission module reference](PartSysEmissionModule.html) | Explore properties on the Emission module, to configure the rate and timing of particle emissions. |
| [Shape module reference](PartSysShapeModule.html) | Explore properties on the Shape module, to configure the volume or surface that the Particle System uses to emit particles, and the direction of the start velocity. |
| [Velocity over Lifetime module reference](PartSysVelOverLifeModule.html) | Explore properties on the Velocity over Lifetime module, to configure particles that change velocity over time. |
| [Noise module reference](PartSysNoiseModule.html) | Explore properties on the Noise module, to configure the turbulence of particles as they move. |
| [Limit Velocity over Lifetime module reference](PartSysLimitVelOverLifeModule.html) | Explore properties on the Limit Velocity over Lifetime module, to configure particles that reduce in velocity over time. |
| [Inherit Velocity module reference](PartSysInheritVelocity.html) | Explore properties on the Inherit Velocity module, to configure the velocity of particles from sub-emitters to match the velocity of the parent particle. |
| [Lifetime by Emitter Speed module reference](PartSysLifetimeByEmitterSpeedModule.html) | Explore properties on the Lifetime by Emitter Speed module, to configure the initial lifetime of each particle based on the speed of the emitter when the particle spawns. |
| [Force over Lifetime module reference](PartSysForceOverLifeModule.html) | Explore properties on the Force over Lifetime module, to configure simulated physics forces that affect the movement of particles over time. |
| [Color over Lifetime module reference](PartSysColorOverLifeModule.html) | Explore properties on the Color over Lifetime module, to configure particles that change color over time. |
| [Color by Speed module reference](PartSysColorBySpeedModule.html) | Explore properties on the Color by Speed module, to configure particles that change color based on their speed. |
| [Size over Lifetime module reference](PartSysSizeOverLifeModule.html) | Explore properties on the Size over Lifetime module, to configure particles that change size over time. |
| [Size by Speed module reference](PartSysSizeBySpeedModule.html) | Explore properties on the Size by Speed module, to configure particles that change size based on their speed. |
| [Rotation over Lifetime module reference](PartSysRotOverLifeModule.html) | Explore properties on the Rotation over Lifetime module, to configure particles that change rotation over time. |
| [Rotation by Speed module reference](PartSysRotBySpeedModule.html) | Explore properties on the Rotation by Speed module, to configure particles that change rotation based on their speed. |
| [External Forces module reference](PartSysExtForceModule.html) | Explore properties on the External Forces module, to configure the effect of external physics forces such as **wind zones**A GameObject that adds the effect of wind to your terrain. For instance, Trees within a wind zone will bend in a realistic animated fashion and the wind itself will move in pulses to create natural patterns of movement among the tree. [More info](class-WindZone.html) See in [Glossary](Glossary.html#windzone) and force fields on particles emitted by the system. |
| [Collision module reference](PartSysCollisionModule.html) | Explore properties on the **Collision**A collision occurs when the physics engine detects that the colliders of two GameObjects make contact or overlap, when at least one has a Rigidbody component and is in motion. [More info](CollidersOverview.html) See in [Glossary](Glossary.html#collision) module, to configure particle collisions. |
| [Triggers module reference](PartSysTriggersModule.html) | Explore properties on the Triggers module, to configure particles that act as triggers. |
| [Sub Emitters module reference](PartSysSubEmitModule.html) | Explore properties on the Sub Emitters module, to configure particles that emit other particles. |
| [Texture Sheet Animation module reference](PartSysTexSheetAnimModule.html) | Explore properties on the Texture Sheet Animation module, to configure particles that use a texture grid to create animation frames. |
| [Lights module reference](PartSysLightsModule.html) | Explore properties on the Lights module, to configure real-time lights on particles. |
| [Trails module reference](PartSysTrailsModule.html) | Explore properties on the Trails module, to configure trails on particles. |
| [Custom Data module reference](PartSysCustomDataModule.html) | Explore properties in the Custom Data module, to configure custom data formats in the Editor to attach to particles. |
| [Renderer module reference](PartSysRendererModule.html) | Explore properties on the Renderer module, to configure how a particle’s image or **mesh**The main graphics primitive of Unity. Meshes make up a large part of your 3D worlds. Unity supports triangulated or Quadrangulated polygon meshes. Nurbs, Nurms, Subdiv surfaces must be converted to polygons. [More info](mesh.html) See in [Glossary](Glossary.html#Mesh) is transformed, shaded and overdrawn by other particles. |