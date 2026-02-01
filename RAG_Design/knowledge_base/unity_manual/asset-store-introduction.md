--- 
Source: Unity 6 Manual (asset-store-introduction.md)
---

# Introduction to the Asset Store
The **Asset Store**A growing library of free and commercial assets created by Unity and members of the community. Offers a wide variety of assets, from textures, models and animations to whole project examples, tutorials and Editor extensions. [More info](AssetStore.html)
See in [Glossary](Glossary.html#AssetStore) contains a library of free and commercial assets that Unity Technologies and members of the community create. A wide variety of assets are available, including textures, models, animations, entire project examples, tutorials, and extensions for the Unity Editor.
![Unitys Asset Store, with a selection of assets by Unity displayed.](../uploads/Main/AssetStore-main.png)
Unity’s Asset Store, with a selection of assets by Unity displayed.
## Access the Asset Store
You can access the Asset Store website at <https://assetstore.unity.com/>.
In Unity 6.0 and later, you can open the Asset Store website in the Unity Editor from the **Asset Store** dropdown in the [toolbar](Toolbar.html)A row of buttons and basic controls at the top of the Unity Editor that allows you to interact with the Editor in various ways (e.g. scaling, translation). [More info](Toolbar.html)
See in [Glossary](Glossary.html#toolbar). You can also use this dropdown to open your downloaded assets in the [Package Manager Window](upm-ui.html).
In all supported versions of Unity, you can [search](upm-ui-find.html) for your purchased and downloaded [Asset Store packages](AssetStorePackages.html)A bundled collection of assets or tools available for purchase or download on the Unity Asset Store, compressed and stored as an asset package (`.unitypackage` extension) or a UPM package. You can manage your packages from the Asset Store either on the online store or through the Package Manager window. [More info](AssetStorePackages.html)
See in [Glossary](Glossary.html#AssetStorepackage) in the Package Manager window.
## Asset Store package types
Asset Store packages are collections of files and data from Unity projects, or elements of projects. An Asset Store package type is either a **UPM package**A **Package** managed by the **Unity Package Manager**. Refer to **Packages**.
See in [Glossary](Glossary.html#UPMpackage) or an **asset package**A collection of files and data from Unity projects, or elements of projects, which are compressed and stored in one file, similar to Zip files, with the `.unitypackage` extension. Asset packages are a handy way of sharing and re-using Unity projects and collections of assets. [More info](AssetPackages.html)
See in [Glossary](Glossary.html#assetpackage) (`.unitypackage` format). When you add an Asset Store package to your project, the Unity Package Manager unpacks the package and maintains its directory structure and metadata about assets. This metadata includes information such as import settings and links to other assets.
Both package types have their advantages, as follows:
* **Asset packages**: Best for one-off imports or sharing assets without setting up a package registry and requires fast one-off iterations. It is suited for content assets such as 3D models and UI elements that end players will interact with. For more information about asset packages, refer to [Distribute assets as packages](AssetPackages.html).
* **Unity Package Manager (UPM) packages (currently in beta testing)**: Can be versioned, and excluded from source control. Use UPM when you need **version control**A system for managing file changes. You can use Unity in conjunction with most common version control tools, including Perforce, Git, Mercurial and PlasticSCM. [More info](VersionControl.html)
  See in [Glossary](Glossary.html#versioncontrol), dependency management, or plan to maintain the package across multiple projects. For more information about UPM packages, refer to [Introduction to packages](upm-concepts.html).
For more information, refer to [Package types](upm-package-types.html), and [Introduction to publishing Asset Store packages](asset-store-publishing-introduction.html).
## Additional resources
* [Downloading and managing Asset Store packages](asset-store-downloads.html)
* [Publishing Asset Store packages](asset-store-publishing.html)