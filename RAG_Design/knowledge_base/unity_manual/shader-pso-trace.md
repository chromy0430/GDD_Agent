--- 
Source: Unity 6 Manual (shader-pso-trace.md)
---

# Trace and manage PSO data collections
Trace a new PSO data collection and manage existing collections.
**Important**: `GraphicsStateCollection` is an experimental API and might be changed or removed in the future.
PSO tracing means recording which pipeline state objects (PSO) your app uses, and the associated data to be able to prewarm PSOs. Modern graphics APIs compile shaders as part of PSO creation, so they require tracing additional graphics states and the **shader**A program that runs on the GPU. [More info](Shaders.html)
See in [Glossary](Glossary.html#shader) variant used.
The [GraphicsStateCollection](../ScriptReference/Experimental.Rendering.GraphicsStateCollection.html) API enables you to trace and prewarm PSOs in your project. **Tip**: Refer to the [GraphicsStateCollection](../ScriptReference/Experimental.Rendering.GraphicsStateCollection.html) API documentation for more information about the `GraphicsStateCollection` API and for code samples.
The following sections explain how to trace a PSO collection and manage PSO collections in your project.
## Requirements for tracing
Tracing with the `GraphicsStateCollection` API is only supported on **development builds**A development build includes debug symbols and enables the Profiler. [More info](building-introduction.html)
See in [Glossary](Glossary.html#developmentbuild), not release builds.
## Trace a new PSO data collection
Trace PSOs in your project and create a [GraphicsStateCollection](../ScriptReference/Experimental.Rendering.GraphicsStateCollection.ctor.html) asset (a PSO data collection), which stores information about the combinations of shader variants and graphics state your application uses.
To trace a new PSO data collection, follow these steps:
1. Create a new [GraphicsStateCollection](../ScriptReference/Experimental.Rendering.GraphicsStateCollection.ctor.html) in a C# script. This new collection will contain information about traced PSOs from your application or **scene**A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](CreatingScenes.html)
   See in [Glossary](Glossary.html#Scene).
2. To begin tracing PSOs into your PSO data collection, call the [GraphicsStateCollection.BeginTrace](../ScriptReference/Experimental.Rendering.GraphicsStateCollection.BeginTrace.html) method. You should begin tracing during scene or application startup to avoid missing any PSOs.
3. To end tracing, call the [GraphicsStateCollection.EndTrace](../ScriptReference/Experimental.Rendering.GraphicsStateCollection.EndTrace.html) method. End tracing during scene or application end.
**Tip**: The recommended best practice is to trace a separate collection per graphics API and build platform, because GPU states can vary per API.
## Save a collection
Once tracing is complete, save the PSO data collection to disk using [GraphicsStateCollection.SaveToFile](../ScriptReference/Experimental.Rendering.GraphicsStateCollection.SaveToFile.html).
When you save the PSO data collection, the collection saves as a `.graphicsstate` file at the path you provide.
## Retrieve a collection
If you deploy the Player on a different device, you need to manually retrieve the `.graphicsstate` file back to the Editor’s machine. This varies depending on your platform. On Android, use `adb pull`.
Alternatively, you can also use [GraphicsStateCollection.SendToEditor](../ScriptReference/Experimental.Rendering.GraphicsStateCollection.SendToEditor.html) to save and retrieve the PSO collection using `PlayerConnection`. To use `PlayerConnection`, enable **Development Build** and **Autoconnect Profiler** in your project’s ****Build Profile**A set of customizable configuration settings to use when creating a build for your target platform. [More info](build-profiles.html)
See in [Glossary](Glossary.html#buildprofile)** settings.
## Manage a collection
The `GraphicsStateCollection` API provides several methods that you can use to manage a collection and the shader variants within it. For more information, refer to the [GraphicsStateCollection](../ScriptReference/Experimental.Rendering.GraphicsStateCollection.html) API documentation.
### Append missing PSOs to a collection
If you modify the shaders used by your application or scene, the collection might not contain the new PSO data. To check whether a collection contains a specific shader variant, call [ContainsVariant](../ScriptReference/Experimental.Rendering.GraphicsStateCollection.ContainsVariant.html).
To trace missing PSOs, you can use the tracing workflow with the same collection to begin and end a trace around a subset of your scene that uses the missing shader variants. Unity appends any new shader variants encountered during tracing to the existing collection data when it’s saved.
You can also enable the [traceCacheMisses](../ScriptReference/Experimental.Rendering.GraphicsStateCollection.traceCacheMisses.html) option when calling a [prewarm method](shader-prewarm.html#warm-up-a-collection) to automatically trace any missing PSO data to a separate [cacheMissCollection](../ScriptReference/Experimental.Rendering.GraphicsStateCollection.cacheMissCollection.html).
To append new PSO data from other collections, call [Append](../ScriptReference/Experimental.Rendering.GraphicsStateCollection.Append.html) on the original collection.
## Additional resources
* [Warm up PSOs](shader-prewarm.html)
* [PSO tracing and warming example](shader-pso-example.html)