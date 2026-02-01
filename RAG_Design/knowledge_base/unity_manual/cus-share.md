--- 
Source: Unity 6 Manual (cus-share.md)
---

# Share your package
When you have finished developing your package, you can share it with others to use.
Choose from the following methods to share your package:
| **Type** | **Description** |
| --- | --- |
| **Compressed file** | You can share a zip file to other Unity users. That way, they can decompress the zip file to a local folder on their own computer and [install the package from disk](upm-ui-local.html). |
| **Tarball** | You can share a tarball to other Unity users. That way, they can [install the package from the local tarball](upm-ui-tarball.html) directly. For information about creating a tarball from a **UPM package**A **Package** managed by the **Unity Package Manager**. Refer to **Packages**. See in [Glossary](Glossary.html#UPMpackage) you created, refer to [Export and sign your UPM package](cus-export.html). |
| **Git URL** | You can share a link to your Git repository, using one of the [supported protocols](upm-git.html). Then users can [install your package using its Git URL](upm-git.html), because the Unity Package Manager can fetch packages from services that host Git repositories, such as GitHub and GitLab. |
| **Scoped Registry** | You can set up a package registry server to host your package and then publish it to that registry. For more information, refer to [Host a scoped registry](upm-scoped-host.html).  Your package’s consumers can then configure their project settings to [Use a scoped registry](upm-scoped-use.html) to fetch your custom packages from your package registry. |
## Additional resources
* [Package development workflow](CustomPackages.html)
* [Asset packages](AssetPackages.html)A collection of files and data from Unity projects, or elements of projects, which are compressed and stored in one file, similar to Zip files, with the `.unitypackage` extension. Asset packages are a handy way of sharing and re-using Unity projects and collections of assets. [More info](AssetPackages.html)
  See in [Glossary](Glossary.html#assetpackage)