--- 
Source: Unity 6 Manual (MaterialsAccessingViaScript.md)
---

# Access material properties in a script
All the parameters of a material asset that you see in the **Inspector**A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](UsingTheInspector.html)
See in [Glossary](Glossary.html#Inspector) window are accessible via script, giving you the power to change or animate how a material works at runtime.
This allows you to modify numeric values on the material, change colours, and swap textures dynamically during gameplay. Some of the most commonly used methods to do this are:
| Method Name | Use |
| --- | --- |
| [SetColor](../ScriptReference/Material.SetColor.html) | Change the color of a material (Eg. the albedo tint color) |
| [SetFloat](../ScriptReference/Material.SetFloat.html) | Set a floating point value (Eg. the normal map multiplier) |
| [SetInteger](../ScriptReference/Material.SetInteger.html) | Set an integer value in the material |
| [SetTexture](../ScriptReference/Material.SetTexture.html) | Assign a new texture to the material |
The full set of methods available for manipulating materials via script can be found on the [Material class scripting reference](../ScriptReference/Material.html).
One important note is that these methods **only set properties that are available for the current **Shader**A program that runs on the GPU. [More info](Shaders.html)
See in [Glossary](Glossary.html#shader) object** on the material. This means that if you have a shader that doesn’t use any textures, or if you have no shader bound at all, calling [SetTexture](../ScriptReference/Material.SetTexture.html) will have no effect. This is true even if you later set a shader that needs the texture. For this reason it is recommended to set the shader you want before setting any properties. However, after you have set the shader you can switch from one shader to another that use the same textures or properties and values will be preserved.