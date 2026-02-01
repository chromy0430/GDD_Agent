--- 
Source: Unity 6 Manual (build-deterministic-assets.md)
---

# Asset import determinism
Before you build assets, confirm whether the imported assets are deterministic.
You can use the following tools to verify this:
* **Use the consistency check argument**: Open the Unity Editor with the following launch argument, which enables the ConsistencyChecker to record results in the Editor log:
  ```
  -consistencyCheck
  ```
* **Check the log and reimport assets**: If the log contains a message such as the following, the asset import process is nondeterministic.:
  ```
  Importer(<ImporterName>) generated inconsistent result for asset (guid:<GUID>)
  ```
## Keeping import history
Use the [Import Activity window](ImportActivityWindow.html) to inspect re-import reasons and timestamps.
You can disable automatic artifact cleanup when analyzing imports as follows:
```
EditorUserSettings.artifactGarbageCollection = false
```
This prevents Unity from deleting previous import artifacts. Deleting the `Library` folder clears all historical import data.
## Non-deterministic asset types
Some Unity Editor-generated assets are non-deterministic and can produce different binary outputs when regenerated, even with identical source data and settings.
To maintain deterministic builds, avoid regenerating these assets unless the source content changes, and keep previously baked or generated data under **version control**A system for managing file changes. You can use Unity in conjunction with most common version control tools, including Perforce, Git, Mercurial and PlasticSCM. [More info](VersionControl.html)
See in [Glossary](Glossary.html#versioncontrol). Only rebuild **lightmaps**A pre-rendered texture that contains the effects of light sources on static objects in the scene. Lightmaps are overlaid on top of scene geometry to create the effect of lighting. [More info](Lightmapping.html)
See in [Glossary](Glossary.html#Lightmap), or other baked assets when the source content changes, and not as part of every build routine.
| **Asset type** | **Behavior** |
| --- | --- |
| **Lightmaps** | Re-baking lightmaps for every build produces different binary data, even with the same lighting setup. This is because the baking system involves not only floating-point rounding but also sampling noise that can make lightmaps non-reproducible. |
| ****NavMesh**A mesh that Unity generates to approximate the walkable areas and obstacles in your environment for path finding and AI-controlled navigation. [More info](https://docs.unity3d.com/Packages/com.unity.ai.navigation@latest/index.html?subfolder=/manual/NavInnerWorkings.html%23walkable-areas) See in [Glossary](Glossary.html#NavMesh)** | Build NavMeshes under identical input and environmental conditions. However, NavMeshes are sensitive to floating-point operations because Unity calculates the NavMesh based on the **scene**A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](CreatingScenes.html) See in [Glossary](Glossary.html#Scene)’s meshes. Therefore, the NavMesh might bake differently on other architectures. |
| **Generated assets based on noise sampling** | Creating assets based on sampling noise textures or other randomness can generate assets differently each time. |
## Additional resources
* [Import Activity window](ImportActivityWindow.html)
* [Managing assets at runtime](assets-managing-runtime.html)
* [Command line arguments](CommandLineArguments.html)