--- 
Source: Unity 6 Manual (writing-shader-usepass.md)
---

# Include a shader pass with the UsePass command
The UsePass command inserts a named Pass from another **Shader**A program that runs on the GPU. [More info](Shaders.html)
See in [Glossary](Glossary.html#shader) object. You can use this command to reduce code duplication in shader source files.
## Example
This example code creates a **Shader object**An instance of the Shader class, a Shader object is container for shader programs and GPU instructions, and information that tells Unity how to use them. Use them with materials to determine the appearance of your scene. [More info](shader-objects.html)
See in [Glossary](Glossary.html#Shaderobject) called ContainsNamedPass, which contains a Pass called ExampleNamedPass.
```
Shader "Examples/ContainsNamedPass"
{
    SubShader
    {
        Pass
        {
              Name "ExampleNamedPass"
              // The rest of the Pass contents go here.
        }
    }
}
```
This example code creates a Shader object called UseNamedPass, which uses the named Pass from the example code above.
```
Shader "Examples/UsesNamedPass"
{
    SubShader
    {
        UsePass "Examples/ContainsNamedPass/EXAMPLENAMEDPASS"
    }
}
```
## Additional resources
* [UsePass directive in ShaderLab reference](SL-UsePass.html)