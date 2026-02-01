--- 
Source: Unity 6 Manual (shader-NormalFamily.md)
---

# Normal Shader Family
**Note.** Unity 5 introduced the [Standard Shader](shader-StandardShader.html) which replaces these **shaders**A program that runs on the GPU. [More info](Shaders.html)
See in [Glossary](Glossary.html#shader).
These shaders are the basic shaders in Unity. They are not specialized in any way and should be suitable for most opaque objects. They are not suitable if you want your object to be transparent, emitting light etc.
## [Vertex Lit](shader-NormalVertexLit.html)
![shader-NormalVertexLit](../uploads/Shaders/Thumb-NormalVertex.jpg)
shader-NormalVertexLit
**Assets needed:**
* One **Base** texture, no alpha channel required
## [Diffuse](shader-NormalDiffuse.html)
![shader-NormalDiffuse](../uploads/Shaders/Thumb-NormalDiffuse.jpg)
shader-NormalDiffuse
**Assets needed:**
* One **Base** texture, no alpha channel required
## [Specular](shader-NormalSpecular.html)
![shader-NormalSpecular](../uploads/Shaders/Thumb-NormalSpec.jpg)
shader-NormalSpecular
**Assets needed:**
* One **Base** texture with alpha channel for Specular Map
## [Normal mapped](shader-NormalBumpedDiffuse.html)
![shader-NormalBumpedDiffuse](../uploads/Shaders/Thumb-NormalBump.jpg)
shader-NormalBumpedDiffuse
**Assets needed:**
* One **Base** texture, no alpha channel required
* One **Normal map**A type of Bump Map texture that allows you to add surface detail such as bumps, grooves, and scratches to a model which catch the light as if they are represented by real geometry.
  See in [Glossary](Glossary.html#normalmap)
## [Normal mapped Specular](shader-NormalBumpedSpecular.html)
![shader-NormalBumpedSpecular](../uploads/Shaders/Thumb-NormalBumpSpec.jpg)
shader-NormalBumpedSpecular
**Assets needed:**
* One **Base** texture with alpha channel for Specular Map
* One **Normal map**
## [Parallax](shader-NormalParallaxDiffuse.html)
![shader-NormalParallaxDiffuse](../uploads/Shaders/Thumb-NormalParallaxBump.jpg)
shader-NormalParallaxDiffuse
**Assets needed:**
* One **Base** texture, no alpha channel required
* One **Normal map**
* One **Height** texture with Parallax Depth in the alpha channel
## [Parallax Specular](shader-NormalParallaxSpecular.html)
![shader-NormalParallaxSpecular](../uploads/Shaders/Thumb-NormalParallaxBumpSpec.jpg)
shader-NormalParallaxSpecular
**Assets needed:**
* One **Base** texture with alpha channel for Specular Map
* One **Normal map**
* One **Height** texture with Parallax Depth in the alpha channel
## [Decal](shader-NormalDecal.html)
![shader-NormalDecal](../uploads/Shaders/Thumb-NormalDecal.jpg)
shader-NormalDecal
**Assets needed:**
* One **Base** texture, no alpha channel required
* One **Decal** texture with alpha channel for Decal transparency
## [Diffuse Detail](shader-NormalDiffuseDetail.html)
![shader-NormalDiffuseDetail](../uploads/Shaders/Thumb-NormalDiffuseDetail.jpg)
shader-NormalDiffuseDetail
**Assets needed:**
* One **Base** texture, no alpha channel required
* One **Detail** grayscale texture; with 50% gray being neutral color
NormalFamily