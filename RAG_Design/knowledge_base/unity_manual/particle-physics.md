--- 
Source: Unity 6 Manual (particle-physics.md)
---

# Particle physics
Resources for configuring simulated physics and **collisions**A collision occurs when the physics engine detects that the colliders of two GameObjects make contact or overlap, when at least one has a Rigidbody component and is in motion. [More info](CollidersOverview.html)
See in [Glossary](Glossary.html#collision) on **particles**A small, simple image or mesh that is emitted by a particle system. A particle system can display and move particles in great numbers to represent a fluid or amorphous entity. The effect of all the particles together creates the impression of the complete entity, such as smoke. [More info](class-ParticleSystem.html)
See in [Glossary](Glossary.html#particle).
| **Topic** | **Description** |
| --- | --- |
| [Particle physics forces](particle-physics-forces.html) | Understand how the **Particle System**A component that simulates fluid entities such as liquids, clouds and flames by generating and animating large numbers of small 2D images in the scene. [More info](class-ParticleSystem.html) See in [Glossary](Glossary.html#particlesystem) can simulate physics forces that act on a particle. |
| [Apply forces to particles](apply-forces-particles.html) | Use the Particle System Force Field to set up forces on the particles in a Particle System. |
| [Particle collisions](particle-collisions.html) | Understand how the Particle System can create and calculate collisions between particles and **GameObjects**The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](class-GameObject.html) See in [Glossary](Glossary.html#GameObject) |
| [Particle triggers](particle-triggers.html) | Understand how the Particle System can use particle **colliders**An invisible shape that is used to handle physical collisions for an object. A collider doesn’t need to be exactly the same shape as the object’s mesh - a rough approximation is often more efficient and indistinguishable in gameplay. [More info](CollidersOverview.html) See in [Glossary](Glossary.html#collider) to act as triggers. |
| [Configure a particle trigger](configure-particle-trigger.html) | Create and configure a trigger on the particles of a Particle System. |
| [Particle System Force Field component reference](class-ParticleSystemForceField.html) | Explore the properties on the Particle System Force Field component, to apply forces to particles. |
## Additional resources
* [Force Over Lifetime Module reference](PartSysForceOverLifeModule.html)
* [External Forces Module reference](PartSysExtForceModule.html)
* [Collision Module reference](PartSysCollisionModule.html)
* [Triggers Module reference](PartSysTriggersModule.html)