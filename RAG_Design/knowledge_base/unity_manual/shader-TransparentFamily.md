--- 
Source: Unity 6 Manual (shader-TransparentFamily.md)
---

# Transparent Shader Family
**Note.** Unity 5 introduced the [Standard Shader](shader-StandardShader.html) which replaces these **shaders**A program that runs on the GPU. [More info](Shaders.html)
See in [Glossary](Glossary.html#shader).
The Transparent shaders are used for fully- or semi-transparent objects. Using the alpha channel of the **Base** texture, you can determine areas of the object which can be more or less transparent than others. This can create a great effect for glass, HUD interfaces, or sci-fi effects.
## [Transparent Vertex-Lit](shader-TransVertexLit.html)
![shader-TransVertexLit](../uploads/Shaders/Thumb-TransVertex.jpg)
shader-TransVertexLit
**Assets needed:**
* One **Base** texture with alpha channel for Transparency Map
[» More details](shader-TransVertexLit.html)
## [Transparent Diffuse](shader-TransDiffuse.html)
![shader-TransDiffuse](../uploads/Shaders/Thumb-TransDiffuse.jpg)
shader-TransDiffuse
**Assets needed:**
* One **Base** texture with alpha channel for Transparency Map
[» More details](shader-TransDiffuse.html)
## [Transparent Specular](shader-TransSpecular.html)
![shader-TransSpecular](../uploads/Shaders/Thumb-TransSpec.jpg)
shader-TransSpecular
**Assets needed:**
* One **Base** texture with alpha channel for combined Transparency Map/Specular Map
**Note:**
One limitation of this shader is that the **Base** texture’s alpha channel doubles as a Specular Map for the Specular shaders in this family.
[» More details](shader-TransSpecular.html)
## [Transparent Normal mapped](shader-TransBumpedDiffuse.html)
![shader-TransBumpedDiffuse](../uploads/Shaders/Thumb-TransBump.jpg)
shader-TransBumpedDiffuse
**Assets needed:**
* One **Base** texture with alpha channel for Transparency Map
* One **Normal map**A type of Bump Map texture that allows you to add surface detail such as bumps, grooves, and scratches to a model which catch the light as if they are represented by real geometry.
  See in [Glossary](Glossary.html#normalmap) normal map, no alpha channel required
[» More details](shader-TransBumpedDiffuse.html)
## [Transparent Normal mapped Specular](shader-TransBumpedSpecular.html)
![shader-TransBumpedSpecular](../uploads/Shaders/Thumb-TransBumpSpec.jpg)
shader-TransBumpedSpecular
**Assets needed:**
* One **Base** texture with alpha channel for combined Transparency Map/Specular Map
* One **Normal map** normal map, no alpha channel required
**Note:**
One limitation of this shader is that the **Base** texture’s alpha channel doubles as a Specular Map for the Specular shaders in this family.
[» More details](shader-TransBumpedSpecular.html)
## [Transparent Parallax](shader-TransParallaxDiffuse.html)
![shader-TransParallaxDiffuse](../uploads/Shaders/Thumb-TransParallaxBump.jpg)
shader-TransParallaxDiffuse
**Assets needed:**
* One **Base** texture with alpha channel for Transparency Map
* One **Normal map** normal map with alpha channel for Parallax Depth
[» More details](shader-TransParallaxDiffuse.html)
## [Transparent Parallax Specular](shader-TransParallaxSpecular.html)
![shader-TransParallaxSpecular](../uploads/Shaders/Thumb-TransParallaxBumpSpec.jpg)
shader-TransParallaxSpecular
**Assets needed:**
* One **Base** texture with alpha channel for combined Transparency Map/Specular Map
* One **Normal map** normal map with alpha channel for Parallax Depth
**Note:**
One limitation of this shader is that the **Base** texture’s alpha channel doubles as a Specular Map for the Specular shaders in this family.
[» More details](shader-TransParallaxSpecular.html)
TransparentFamily