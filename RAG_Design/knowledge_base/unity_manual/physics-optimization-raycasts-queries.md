--- 
Source: Unity 6 Manual (physics-optimization-raycasts-queries.md)
---

# Optimize raycasts and other physics queries
Optimize physics query performance and reduce garbage collection overhead by using efficient query versions and batch processing.
## Use non-allocating query versions
Standard physics queries, such as [`Physics.Raycast`](../ScriptReference/Physics.Raycast.html), [`Physics.SphereCast`](../ScriptReference/Physics.SphereCast.html), or [`Physics.OverlapSphere`](../ScriptReference/Physics.OverlapSphere.html), allocate memory on the heap for their results. This allocation can contribute to garbage collection pauses, especially if they are called frequently.
Instead, use the non-allocating counterparts of these queries that write their results into a pre-allocated array that you provide. Non-allocating counterparts can include:
* [`Physics.RaycastNonAlloc`](../ScriptReference/Physics.RayCastNonAlloc.html)
* [`Physics.SphereCastNonAlloc`](../ScriptReference/Physics.SphereCastNonAlloc.html)
* [`Physics.OverlapSphereNonAlloc`](../ScriptReference/Physics.OverlapSphereNonAlloc.html)
For example:
```
int hitCount = Physics.RaycastNonAlloc(ray, preAllocatedHitsArray, distance, layerMask);
```
When you use non-allocating queries, you must provide a pre-allocated array. For example, `RaycastHit[] preAllocatedHitsArray = new RaycastHit[10];`.
Size this array appropriately: make it large enough to capture the maximum expected hits in typical scenarios, but not so large as to waste memory. If the number of actual **colliders**An invisible shape that is used to handle physical collisions for an object. A collider doesn’t need to be exactly the same shape as the object’s mesh - a rough approximation is often more efficient and indistinguishable in gameplay. [More info](CollidersOverview.html)
See in [Glossary](Glossary.html#collider) found exceeds the size of your buffer array, only the results up to the array’s capacity are returned, and the rest are ignored.
**Tip:** Choose a buffer size that balances typical needs with memory considerations. Profile your game to understand common hit counts.
## Use batch queries for multiple operations
Running many individual physics queries (for example, many raycasts per frame) can reduce performance because of the overhead of each call. If you need to perform many queries simultaneously, batch them using APIs like [`RaycastCommand`](../ScriptReference/RaycastCommand.html), [`SpherecastCommand`](../ScriptReference/SpherecastCommand.html), or [`BoxcastCommand`](../ScriptReference/BoxcastCommand.html) in conjunction with the [job system](job-system.html).
This approach leverages multi-threading to process queries in parallel, significantly improving performance for bulk query operations. This is particularly powerful when you have many independent raycasts (or other queries) that can be processed in parallel.
To use batch queries, follow these steps:
1. Create and populate a `NativeArray<RaycastCommand>` with the parameters for all your raycasts.
2. Allocate a `NativeArray<RaycastHit>` to store the results.
3. Schedule the batch processing using `RaycastCommand.ScheduleBatch`, which returns a `JobHandle`.
4. You can then perform other work, and later ensure the job is complete using `jobHandle.Complete` before you access the results. For example, ensure the job is complete at the start of the next frame or when needed.
## Additional resources
* [Unity Profiler](Profiler.html)
* [Managing time and frame rate](managing-time-and-frame-rate.html)
* [Memory Profiler](https://docs.unity3d.com/Packages/com.unity.memoryprofiler@latest)
* [Physics Project Settings](class-PhysicsManager.html)
* [RaycastCommand](../ScriptReference/RaycastCommand.html)
* [Write multithreaded code with the job system](job-system.html)
* [Collections package](https://docs.unity3d.com/Packages/com.unity.collections@latest?subfolder=/manual/index.html)