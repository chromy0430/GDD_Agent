--- 
Source: Unity 6 Manual (writing-shader-change-properties.md)
---

# Adding material properties to shaders
Resources and techniques for adding properties to **shaders**A program that runs on the GPU. [More info](Shaders.html)
See in [Glossary](Glossary.html#shader) that artists can use to create, edit, and share materials with different configurations.
| **Page** | **Description** |
| --- | --- |
| [Introduction to material properties](writing-shader-material-properties.html) | Understand how to add material properties, how material property values are provided to shaders, and the difference between serialized and runtime material properties. |
| [Add material properties](SL-PropertiesInPrograms.html) | To assign material properties to a **Shader object**An instance of the Shader class, a Shader object is container for shader programs and GPU instructions, and information that tells Unity how to use them. Use them with materials to determine the appearance of your scene. [More info](shader-objects.html) See in [Glossary](Glossary.html#Shaderobject) in **ShaderLab**Unity’s language for defining the structure of Shader objects. [More info](SL-Shader.html) See in [Glossary](Glossary.html#ShaderLab), use a `Properties` block inside a `Shader` block. |
| [Texture properties](material-properties-texture-properties.html) | Understand the extra properties Unity adds for texture. |
| [Access material properties in a script](writing-shader-use-material-properties-code.html) | Use the `MaterialProperty` API to access material properties. |
| [Set shader variables to material property values](writing-shader-use-material-properties.html) | Use material properties to set variables in ShaderLab code or in HLSL code. |
| [Control material properties in the Inspector window](writing-shader-display-types.html) | Use the `MaterialPropertyDrawer` API or a custom editor to expose material properties in the **Inspector**A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](UsingTheInspector.html) See in [Glossary](Glossary.html#Inspector) window of a material. |
## Additional resources
* [Properties block reference in ShaderLab](SL-Properties.html)