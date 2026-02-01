--- 
Source: Unity 6 Manual (assembly-definition-files.md)
---

# Organizing scripts into assemblies
Assemblies are individual units of compiled code that group types and resources together. Organizing **scripts**A piece of code that allows you to create your own Components, trigger game events, modify Component properties over time and respond to user input in any way you like. [More info](creating-scripts.html)
See in [Glossary](Glossary.html#Scripts) into assemblies has important advantages, especially as your codebase grows.
Assemblies help you think clearly about the architecture of your code and about managing dependencies. By exercising fine-grained control over references, you can reduce unnecessary recompilation time and make your code easier to debug.
| **Topic** | **Description** |
| --- | --- |
| [Introduction to assemblies in Unity](assembly-definitions-intro.html) | Understand the fundamentals of how assemblies work in Unity and why using them to organize your scripts is beneficial. |
| [Creating assembly assets](assembly-definitions-creating.html) | Create various kinds of assembly assets to customize your assemblies. |
| [Referencing assemblies](assembly-definitions-referencing.html) | Set up references between assemblies, override the default references and understand the limitations Unity places on references. |
| [Conditionally including assemblies](assembly-definition-includes.html) | Use scripting symbols to conditionally include or exclude assemblies from compilation. |
| [Assembly metadata and compilation details](assembly-definition-metadata.html) | Define metadata for your assemblies. |
| [Assembly Definition Inspector window reference](class-AssemblyDefinitionImporter.html) | Inspector-editable properties of assembly defintion assets and their meaning. |
| [Assembly Definition Reference Inspector window reference](class-AssemblyDefinitionReferenceImporter.html) | Inspector-editable properties of assembly defintion reference assets and their meaning. |
| [Assembly Definition file format reference](assembly-definition-file-format.html) | Assembly definition file format reference. |
| [Predefined assemblies reference](script-compile-order-folders.html) | Unity’s predefined assemblies and the order in which Unity compiles them. |
## Additional resources
* [Special folders and script compilation order](script-compile-order-folders.html)
* [Scripting backends](scripting-backends.html)A framework that powers scripting in Unity. Unity supports three different scripting backends depending on target platform: Mono, .NET and IL2CPP. Universal Windows Platform, however, supports only two: .NET and IL2CPP. [More info](scripting-backends.html)
  See in [Glossary](Glossary.html#ScriptingBackend)