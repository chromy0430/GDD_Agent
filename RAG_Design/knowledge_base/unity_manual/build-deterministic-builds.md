--- 
Source: Unity 6 Manual (build-deterministic-builds.md)
---

# Deterministic builds
Deterministic builds produce identical output when given the same source code, assets, and build settings. This consistency is essential for reliable deployment pipelines, debugging, and collaborative development.
In Unity, many factors can introduce non-deterministic behavior, which causes builds to vary.
| **Topic** | **Description** |
| --- | --- |
| **[Introduction to deterministic builds](build-deterministic-builds-introduction.html)** | Understand deterministic builds and common factors that can cause build variations. |
| **[Asset import determinism](build-deterministic-assets.html)** | Create consistent asset import results across different machines and build environments. |
| **[Editor scripts determinism](build-deterministic-editor-scripts.html)** | Create reliable build **scripts**A piece of code that allows you to create your own Components, trigger game events, modify Component properties over time and respond to user input in any way you like. [More info](creating-scripts.html) See in [Glossary](Glossary.html#Scripts) that produce consistent results. |
| **[AssetBundle and Addressables determinism](build-deterministic-assetbundles-addressables.html)** | Configure AssetBundle and Addressables builds for deterministic output. |
## Additional resources
* [Customize the build pipeline](build-customize-build-pipeline.html)
* [Introduction to Unity Accelerator](UnityAccelerator.html)
* [Use AssetBundles to load assets at runtime](assetbundles-section.html)
* [Managing assets at runtime](assets-managing-runtime.html)
* [Import Activity window](ImportActivityWindow.html)