--- 
Source: Unity 6 Manual (ParticleSystems.md)
---

# Particle effects
A **particle**A small, simple image or mesh that is emitted by a particle system. A particle system can display and move particles in great numbers to represent a fluid or amorphous entity. The effect of all the particles together creates the impression of the complete entity, such as smoke. [More info](class-ParticleSystem.html)
See in [Glossary](Glossary.html#particle) system simulates and renders many small images or Meshes, called particles, to produce a visual effect. Each particle in a system represents an individual graphical element in the effect. The system simulates every particle collectively to create the impression of the complete effect.
![The holo table in Unitys Spaceship demo. Made with the Visual Effect Graph.](../uploads/Main/ParticleSystems-HoloTable.png)
The holo table in Unity’s Spaceship demo. Made with the Visual Effect Graph.
Particle systems are useful when you want to create dynamic objects like fire, smoke, or liquids because it is difficult to depict this kind of object with a **Mesh**The main graphics primitive of Unity. Meshes make up a large part of your 3D worlds. Unity supports triangulated or Quadrangulated polygon meshes. Nurbs, Nurms, Subdiv surfaces must be converted to polygons. [More info](mesh.html)
See in [Glossary](Glossary.html#Mesh) (3D) or **Sprite**A 2D graphic objects. If you are used to working in 3D, Sprites are essentially just standard textures but there are special techniques for combining and managing sprite textures for efficiency and convenience during development. [More info](sprite/sprite-landing.html)
See in [Glossary](Glossary.html#Sprite) (2D). Meshes and Sprites are better at depicting solid objects such as a house or a car.
This section contains information on:
* [Which particle system solution to use for your Project](ChoosingYourParticleSystem.html).
* [The Built-in Particle System](PartSysUsage.html).
* [The Visual Effect Graph](VFXGraph.html).