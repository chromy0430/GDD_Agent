--- 
Source: Unity 6 Manual (configurable-joints-driving-forces.md)
---

# Driving forces with Configurable Joints
A **joint**A physics component allowing a dynamic connection between Rigidbody components, usually allowing some degree of movement such as a hinge. [More info](Joints.html)
See in [Glossary](Glossary.html#joint) can react to the movements of the object it is attached to, and apply [driving forces](#understand-driving-forces) to set the object in motion.
You can use the **Configurable Joint**An extremely customizable joint that other joint types are derived from. It can be used to create anything from adapted versions of existing joints to custom designed and highly specialized joints. [More info](class-ConfigurableJoint.html)
See in [Glossary](Glossary.html#ConfigurableJoint) to apply driving forces toward either a [position-based target](configure-driving-forces.html#apply-target-position) like a position or rotation, or a [velocity-based target](configure-driving-forces.html#apply-target-velocity) like a linear velocity or angular velocity.
## Understand driving forces
The Configurable Joint applies driving forces on each axis, via **axis drives**, to apply motion and rotation.
The axis drives for linear force are:
\* **X Drive**
\* **Y Drive**
\* **Z Drive**
The axis drives for angular or rotational force are:
\* **Angular X Drive**
\* **Angular YZ Drive**
Each axis drive has spring and damper options to simulate a motor that generates force. The physics system uses these values to calculate the driving force it should apply on that axis, via the following formula:
```
force = positionSpring * (targetPosition - position) + positionDamper * (targetVelocity - velocity)
```
The **Maximum Force** property prevents the force from exceeding a specific value, even if the force calculation result is higher.