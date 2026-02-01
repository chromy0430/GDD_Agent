--- 
Source: Unity 6 URP Manual (Post-Processing-Lens-Distortion.html)
---

# Lens Distortion Volume Override reference for URP
![Scene with Lens Distortion effect turned off.](../../uploads/urp/post-proc/lens-distortion-off.png)
Scene with Lens Distortion effect turned off.
![Scene with Lens Distortion effect turned on.](../../uploads/urp/post-proc/lens-distortion.png)
Scene with Lens Distortion effect turned on.
The **Lens Distortion** effect distorts the final rendered picture to simulate the shape of a real-world **camera**A component which creates an image of a particular viewpoint in your scene. The output is either drawn to the screen or captured as a texture. [More info](../CamerasOverview.html)
See in [Glossary](../Glossary.html#Camera) lens.
## Properties
| **Property** | **Description** |
| --- | --- |
| **Intensity** | Use the slider to set the overall strength of the **distortion effect**An audio effect that modifies the sound by squashing and clipping the waveform to produce a rough, harsh result. [More info](../class-AudioDistortionFilter.html) See in [Glossary](../Glossary.html#distortioneffect). |
| **X Multiplier** | Use the slider to set the distortion intensity on the x-axis. This value acts as a multiplier so you can set this value to 0 to disable distortion on this axis, |
| **Y Multiplier** | Use the slider to set the distortion intensity on the y-axis. This value acts as a multiplier so you can set this value to 0 to disable distortion on this axis, |
| **Center** | Set the center point of the distortion effect on the screen. |
| **Scale** | Use the slider to set the value for global screen scaling. This zooms the render to hide the borders of the screen. When you use a high distortion, **pixels**The smallest unit in a computer image. Pixel size depends on your screen resolution. Pixel lighting is calculated at every screen pixel. [More info](../ShadowPerformance.html) See in [Glossary](../Glossary.html#pixel) on the borders of the screen can break because they rely on information from pixels outside the screen boundaries that don’t exist. This property is useful for hiding these broken pixels around the screen border. |