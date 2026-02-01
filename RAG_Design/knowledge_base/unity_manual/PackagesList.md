--- 
Source: Unity 6 Manual (PackagesList.md)
---

# Packages and package management
A package contains features to fit the various needs of your project. This can include any core Unity features included during the Unity Editor installation, or other packages that you can install as needed.
Unity’s Package Manager has several interfaces you can use to get packages and manage them.
| **Topic** | **Description** |
| --- | --- |
| **[Get started with packages](Packages.html)** | Learn about packages and get an introduction to Unity’s Package Manager and its core concepts. |
| **[Dependencies](dependencies-lp.html)** | Learn about the different types of dependencies and how Unity’s Package Manager resolves conflicts. |
| **[The Package Manager window](upm-ui.html)** | Get a tour of the Package Manager window. |
| **[Package management with the Package Manager window](managing-packages-window.html)** | Learn how to manage packages by using the Package Manager window. |
| **[Package management with the scripting API](managing-packages-api.html)** | Learn how to manage packages by using C# **scripts**A piece of code that allows you to create your own Components, trigger game events, modify Component properties over time and respond to user input in any way you like. [More info](creating-scripts.html) See in [Glossary](Glossary.html#Scripts). |
| **[Package management with the project manifest file](managing-packages-manifest.html)** | Learn how to manage packages by editing a JSON file. |
| **[Package inspection](package-inspection.html)** | Learn how to get details about a package. |
| **[Packages](Packages-all.html)** | View the lists of packages you can install. |
| **[Feature sets](FeatureSets.html)A feature set is a collection of related packages that you can use to achieve specific results in the Unity Editor. You can manage feature sets directly in Unity’s Package Manager. [More info](FeatureSets.html) See in [Glossary](Glossary.html#featureset)** | Learn about bundles of related packages that you can use for a specific task, such as building environments or optimizing specific platforms, or to find all the development tools you need in one place. Also view a list of feature sets that are available in this version of the Editor. |
| **[Git dependencies](upm-git.html)The Package Manager retrieves Git dependencies from a Git repository directly rather than from a package registry. Git dependencies use a Git URL reference instead of a version, and there’s no guarantee about the package quality, stability, validity, or even whether the version stated in its `package.json` file respects Semantic Versioning rules with regards to officially published releases of this package. [More info](upm-concepts.html#Git) See in [Glossary](Glossary.html#Gitdependency)** | Learn about dependencies that arise from fetching a package from a Git repository. Discover the protocols and extended syntax you can use to fetch packages from a Git repository. |
| **[Package Manager caches](package-manager-caches.html)** | Learn about the different caches stored locally, and how to customize them. |
| **[Scoped registries](upm-scoped.html)** | Learn how to user or host a custom package registry server. |
| **[Package Manager configuration](upm-config.html)** | Configure your network, set cache locations, or configure authentication for private repositories. |
| **[Create custom packages](CustomPackages.html)** | Build and share your own packages, by learning about custom package requirements, working with **package manifest**Each package has a *manifest*, which provides information about the package to the Package Manager. The manifest contains information such as the name of the package, its version, a description for users, dependencies on other packages (if any), and other details. [More info](upm-manifestPkg.html) See in [Glossary](Glossary.html#packagemanifest) files, and more. |
| **[Package Manager troubleshooting](upm-errors.html)** | Get information for troubleshooting Package Manager issues. |
## Additional resources
* [Overview of Unity’s Asset Store](AssetStore.html)