--- 
Source: Unity 6 Manual (properties-intro.md)
---

# Introduction to Unity Properties
Unity Properties is a system that allows you to explore and modify the properties of C# types at runtime. It uses a visitor-style API that traverses the properties of an object graph in a predictable, controllable way.
You can use Unity Properties to read from or write to C# types generically, with minimal type-specific handling. This allows you to work with custom, user-defined C# types and, for example, to validate them, or convert them between different representations.
Unity Properties makes it possible to avoid or minimize [reflection](https://learn.microsoft.com/en-us/dotnet/fundamentals/reflection/reflection), which is relatively slow, allocates memory (which increases garbage collector overhead), and has limited support, especially on platforms that require ahead-of-time (AOT) compilation with [IL2CPP](scripting-backends-il2cpp.html)A Unity-developed scripting back-end which you can use as an alternative to Mono when building projects for some platforms. [More info](./scripting-backends-il2cpp.html)
See in [Glossary](Glossary.html#IL2CPP).
Unity Properties can be useful for the following common scenarios:
* Data validation and processing:
  + Traverse an object graph to validate ranges, nulls, references, or enforce constraints.
  + Compute diffs, hashes, or change detection across properties.
* Copying, cloning, and patching:
  + Deep copy containers or apply patches by visiting and copying specific properties.
* Authoring-to-runtime data conversion:
  + For example, converting ScriptableObject configuration data into runtime structs) via property traversal.
## Fundamental features
The Unity Properties framework has the following fundamental features that you can use to handle C# type data generically:
* [Property bags](property-bags.html): An [`IPropertyBag<T>`](../ScriptReference/Unity.Properties.IPropertyBag_1.html) describes the fields and properties of type `T`. Unity generates property bags so the system can enumerate properties of your type.
* [Visitors](property-visitors.html): You implement a visitor with callbacks like [`Visit<TContainer, TValue>`](../ScriptReference/Unity.Properties.IPropertyVisitor.Visit.html). The framework traverses the container’s properties and invokes your logic per property.
* Adapters: Hooks that customize how specific types are visited or converted (for example, special handling for `Vector3`, enums, collections).
* [Property paths and traversal](property-paths.html): Support for nested containers, arrays, dictionaries, and addressing values via paths with controlled depth and options.
For more detailed examples that use these features together, refer to [Use `PropertyVisitor` to create a property visitor](property-visitors-PropertyVisitor.html) and [Use low level APIs to create a property visitor](property-visitors-low-level-api.html).
## Additional resources
* [Property bags](property-bags.html)
* [Property visitors](property-visitors.html)
* [Property paths](property-paths.html)
* [Use `PropertyVisitor` to create a property visitor](property-visitors-PropertyVisitor.html)
* [Use low level APIs to create a property visitor](property-visitors-low-level-api.html)