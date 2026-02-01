--- 
Source: Unity 6 Manual (properties.md)
---

# Handle type data generically with Unity Properties
The Unity Properties API, in the `Unity.Properties` namespace, uses a [visitor design pattern](https://en.wikipedia.org/wiki/Visitor_pattern) to visit .NET objects at runtime. Visiting objects allows you to discover and modify their properties and add new operations to an existing object structure at runtime without modifying the structure itself. You can build various functionalities on top of the visitor pattern, such as serialization, data migration, deep data comparisons, and data binding.
| **Topic** | **Description** |
| --- | --- |
| **[Introduction to Unity Properties](properties-intro.html)** | Understand the fundamentals and uses of the Unity Properties API. |
| **[Property bags](property-bags.html)** | Understand the role of property bags and the performance considerations when using them. |
| **[Property visitors](property-visitors.html)** | Understand the role of property visitors and the performance considerations when using them. |
| **[Property paths](property-paths.html)** | Understand the role of property paths and the performance considerations when using them. |
| **[Create a property visitor with the PropertyVisitor class](property-visitors-propertyvisitor.html)** | Learn how to use the `PropertyVisitor` base class to create a property visitor from an example. |
| **[Create a property visitor with low-level APIs](property-visitors-low-level-api.html)** | Learn how to use the `IPropertyBagVisitor` and `IPropertyVisitor` interfaces to create a property visitor from an example. |
## Additional resources
* [Serialization](https://docs.unity3d.com/Packages/com.unity.serialization@latest)
* [Runtime data binding](UIE-runtime-binding.html)