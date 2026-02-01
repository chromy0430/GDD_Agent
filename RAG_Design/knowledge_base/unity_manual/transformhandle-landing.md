--- 
Source: Unity 6 Manual (transformhandle-landing.md)
---

# Using unmanaged API for transform operations
The [`TransformHandle`](../ScriptReference/TransformHandle.html) API is an alternative to the [`Transform`](../ScriptReference/Transform.html) API. Unlike the `Transform` component (a managed class), `TransformHandle` is an unmanaged `struct`, which makes it fully compatible with the [Burst](http://docs.unity3d.com/Packages/com.unity.burst@latest) compiler.
| **Page** | **Description** |
| --- | --- |
| [Introduction to TransformHandle API](class-TransformHandle.html) | Introduction to the [`TransformHandle`](../ScriptReference/TransformHandle.html) API and the key differences from the [`Transform`](../ScriptReference/Transform.html) API. |
| [TransformHandle API code examples](transformhandle-examples.html) | Code examples that demonstrate the difference between `Transform` and `TransformHandle` API. |
## Additional resources
* [Transforms](class-Transform.html)