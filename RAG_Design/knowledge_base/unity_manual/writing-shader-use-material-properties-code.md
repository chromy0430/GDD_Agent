--- 
Source: Unity 6 Manual (writing-shader-use-material-properties-code.md)
---

# Access material properties in a script
Material properties are represented in C# code by the [MaterialProperty](../ScriptReference/MaterialProperty.html) class.
To access variables defined in your HLSL code, you can call [Material.GetFloat](../ScriptReference/Material.GetFloat.html), [Material.SetFloat](../ScriptReference/Material.SetFloat.html). There are other, similar methods; see the [Material API documentation](../ScriptReference/Material.html) for a full list. When you access HLSL variables using these APIs, it doesn’t matter whether the variable is a material property or not.