--- 
Source: Unity 6 Manual (UIE-runtime-binding.md)
---

# Runtime data binding
Runtime data binding binds the properties of any plain C# `object` to the properties of a UI control. You can use this type of data binding in both the runtime and Editor UI. However, for serialized data in the Editor UI, use the [SerializedObject data binding](UIE-editor-binding.html) because it provides better support for Unity’s [serialization system](script-serialization.html), including undo/redo functionality and multi-selection operations.
| **Topic** | **Description** |
| --- | --- |
| [Get started with runtime binding](UIE-get-started-runtime-binding.html) | Learn the basics of runtime binding from an example. |
| [Create a runtime data binding in C# scripts](UIE-runtime-binding-types.html) | Create a runtime data binding. |
| [Define a data source](UIE-runtime-binding-define-data-source.html) | Understand how to define a data source for runtime binding, which can be any C# types. |
| [Define binding modes and update triggers](UIE-runtime-binding-mode-update.html) | Define binding modes and update triggers to configure how changes are replicated between the data source and the UI. |
| [Convert data types](UIE-runtime-binding-data-type-conversion.html) | Add type converters to convert data types between the data source and the UI. |
| [Define logging levels](UIE-runtime-binding-logging-levels.html) | Define logging levels to debug runtime bindings. |
| [Create custom binding types](UIE-runtime-binding-custom-types.html) | Create custom binding types and attributes. |
| [Runtime binding example](UIE-runtime-binding-examples.html) | Learn how to create a runtime binding from examples. |
## Additional resources
* [SerializedObject data binding](UIE-editor-binding.html)