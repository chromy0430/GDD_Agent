--- 
Source: Unity 6 Manual (package-manager-caches.md)
---

# Package Manager caches
The Unity Package Manager uses a global cache to store the package contents and metadata for packages in the Unity Package Manager (UPM) format.
The Package Manager maintains a separate cache for **asset packages**A collection of files and data from Unity projects, or elements of projects, which are compressed and stored in one file, similar to Zip files, with the `.unitypackage` extension. Asset packages are a handy way of sharing and re-using Unity projects and collections of assets. [More info](AssetPackages.html)
See in [Glossary](Glossary.html#assetpackage) in the `.unitypackage` format.
These caches make reusing and sharing packages more efficient, and allows you to install and update stored packages even when offline.
| **Topic** | **Description** |
| --- | --- |
| **[Global cache](upm-cache.html)** | Learn about the cache for **UPM packages**A **Package** managed by the **Unity Package Manager**. Refer to **Packages**. See in [Glossary](Glossary.html#UPMpackage), its location, and structure. |
| **[Customize the global cache](upm-config-cache.html)** | Customize the location and size of the global cache. |
| **[Customize the asset package cache location](upm-config-cache-as.html)** | Customize the location of the asset package cache. |
## Additional resources
* [Package types](upm-package-types.html)