--- 
Source: Unity 6 Manual (scripting-optimization.md)
---

# Code optimization
Considering performance in all the code you write helps your project scale without bottlenecks. There are several ways you can improve performance, including avoiding bad practices, [profiling](Profiler.html) your code, implementing appropriate design patterns, and using techniques like asynchronous programming to split work across multiple threads of execution.
| **Topic** | **Description** |
| --- | --- |
| [Unity programming best practices](programming-best-practices.html) | Key issues to be aware of when writing code for Unity applications, along with best practices to help you avoid common pitfalls. |
| [Asynchronous programming](./async-await-support.html) | Asynchronous programming in Unity with the .NET `async` and `await` keywords and Unity’s own custom `Awaitable` class. |
| [Job system](./job-system.html) | Use Unity’s own `Job` system to get the most out of multi-core CPUs and parallelize your algorithms. |
| [Optimizing your code for managed memory](performance-optimizing-code-managed-memory.html) | Approaches for optimizing your code to work with managed memory. |
| [Using unmanaged API for transform operations](transformhandle-landing.html) | Use the [`TransformHandle`](../ScriptReference/TransformHandle.html) API as an alternative to the [`Transform`](../ScriptReference/Transform.html) API. |
## Additional resources
* [Optimization in Unity](analysis.html)