--- 
Source: Unity 6 Manual (shader-ReflectiveFamily.md)
---

# Reflective Shader Family
**Note.** Unity 5 introduced the [Standard Shader](shader-StandardShader.html) which replaces these **shaders**A program that runs on the GPU. [More info](Shaders.html)
See in [Glossary](Glossary.html#shader).
**Reflective** shaders will allow you to use a **Cubemap**A collection of six square textures that can represent the reflections in an environment or the skybox drawn behind your geometry. The six squares form the faces of an imaginary cube that surrounds an object; each face represents the view along the directions of the world axes (up, down, left, right, forward and back). [More info](class-Cubemap-landing.html)
See in [Glossary](Glossary.html#Cubemap) which will be reflected on your **mesh**The main graphics primitive of Unity. Meshes make up a large part of your 3D worlds. Unity supports triangulated or Quadrangulated polygon meshes. Nurbs, Nurms, Subdiv surfaces must be converted to polygons. [More info](mesh.html)
See in [Glossary](Glossary.html#Mesh). You can also define areas of more or less reflectivity on your object through the alpha channel of the **Base** texture. High reflectivity is a great effect for glosses, oils, chrome, etc. Low reflectivity can add effect for metals, liquid surfaces, or video monitors.
## [Reflective Vertex-Lit](shader-ReflectiveVertexLit.html)
![shader-ReflectiveVertexLit](../uploads/Shaders/Thumb-ReflVertex.jpg)
shader-ReflectiveVertexLit
**Assets needed:**
* One **Base** texture with alpha channel for defining reflective areas
* One **Reflection** Cubemap for Reflection Map
[» More details](shader-ReflectiveVertexLit.html)
## [Reflective Diffuse](shader-ReflectiveDiffuse.html)
![shader-ReflectiveDiffuse](../uploads/Shaders/Thumb-ReflDiffuse.jpg)
shader-ReflectiveDiffuse
**Assets needed:**
* One **Base** texture with alpha channel for defining reflective areas
* One **Reflection** Cubemap for Reflection Map
[» More details](shader-ReflectiveDiffuse.html)
## [Reflective Specular](shader-ReflectiveSpecular.html)
![shader-ReflectiveSpecular](../uploads/Shaders/Thumb-ReflSpec.jpg)
shader-ReflectiveSpecular
**Assets needed:**
* One **Base** texture with alpha channel for defining reflective areas & Specular Map combined
* One **Reflection** Cubemap for Reflection Map
**Note:**
One consideration for this shader is that the **Base** texture’s alpha channel will double as both the reflective areas and the Specular Map.
[» More details](shader-ReflectiveSpecular.html)
## [Reflective Normal mapped](shader-ReflectiveBumpedDiffuse.html)
![shader-ReflectiveBumpedDiffuse](../uploads/Shaders/Thumb-ReflBump.jpg)
shader-ReflectiveBumpedDiffuse
**Assets needed:**
* One **Base** texture with alpha channel for defining reflective areas
* One **Reflection** Cubemap for Reflection Map
* One **Normal map**A type of Bump Map texture that allows you to add surface detail such as bumps, grooves, and scratches to a model which catch the light as if they are represented by real geometry.
  See in [Glossary](Glossary.html#normalmap), no alpha channel required
[» More details](shader-ReflectiveBumpedDiffuse.html)
## [Reflective Normal Mapped Specular](shader-ReflectiveBumpedSpecular.html)
![shader-ReflectiveBumpedSpecular](../uploads/Shaders/Thumb-ReflBumpSpec.jpg)
shader-ReflectiveBumpedSpecular
**Assets needed:**
* One **Base** texture with alpha channel for defining reflective areas & Specular Map combined
* One **Reflection** Cubemap for Reflection Map
* One **Normal map**, no alpha channel required
**Note:**
One consideration for this shader is that the **Base** texture’s alpha channel will double as both the reflective areas and the Specular Map.
[» More details](shader-ReflectiveBumpedSpecular.html)
## [Reflective Parallax](shader-ReflectiveParallaxDiffuse.html)
![shader-ReflectiveParallaxDiffuse](../uploads/Shaders/Thumb-ReflParallaxBump.jpg)
shader-ReflectiveParallaxDiffuse
**Assets needed:**
* One **Base** texture with alpha channel for defining reflective areas
* One **Reflection** Cubemap for Reflection Map
* One **Normal map**, with alpha channel for Parallax Depth
[» More details](shader-ReflectiveParallaxDiffuse.html)
## [Reflective Parallax Specular](shader-ReflectiveParallaxSpecular.html)
![shader-ReflectiveParallaxSpecular](../uploads/Shaders/Thumb-ReflParallaxBumpSpec.jpg)
shader-ReflectiveParallaxSpecular
**Assets needed:**
* One **Base** texture with alpha channel for defining reflective areas & Specular Map
* One **Reflection** Cubemap for Reflection Map
* One **Normal map**, with alpha channel for Parallax Depth
**Note:**
One consideration for this shader is that the **Base** texture’s alpha channel will double as both the reflective areas and the Specular Map.
[» More details](shader-ReflectiveParallaxSpecular.html)
## [Reflective Normal mapped Unlit](shader-ReflectiveBumpedUnlit.html)
![shader-ReflectiveBumpedUnlit](../uploads/Shaders/Thumb-ReflBumpUnlit.jpg)
shader-ReflectiveBumpedUnlit
**Assets needed:**
* One **Base** texture with alpha channel for defining reflective areas
* One **Reflection** Cubemap for Reflection Map
* One **Normal map**, no alpha channel required
[» More details](shader-ReflectiveBumpedUnlit.html)
## [Reflective Normal mapped Vertex-Lit](shader-ReflectiveBumpedVertexLit.html)
![shader-ReflectiveBumpedVertexLit](../uploads/Shaders/Thumb-ReflBumpVertex.jpg)
shader-ReflectiveBumpedVertexLit
**Assets needed:**
* One **Base** texture with alpha channel for defining reflective areas
* One **Reflection** Cubemap for Reflection Map
* One **Normal map**, no alpha channel required
[» More details](shader-ReflectiveBumpedVertexLit.html)
ReflectiveFamily