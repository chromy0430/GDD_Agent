--- 
Source: Unity 6 Manual (dependencies-lp.md)
---

# Dependencies
The concept of dependencies is fundamental to Unity’s Package Manager behavior.
A dependency is a package that your project or another package needs to work.
| **Topic** | **Description** |
| --- | --- |
| **[Package dependency and resolution](upm-dependencies.html)** | Learn about the different types of dependencies and how Package Manager resolves them. |
| **[Package version conflict and resolution](upm-conflicts.html)** | Learn how Package Manager resolves package version conflicts when computing a compatible set of packages. |
| **[Embedded dependencies](upm-embed.html)** | Embed a package in your project to make it **mutable**You can change the contents of a mutable package. This is the opposite of **immutable**. Only **Local package****s** and **Embedded package****s** are mutable. See in [Glossary](Glossary.html#mutable). |
| **[Lock files](upm-conflicts-auto.html)** | Learn about lock files, which Package Manager uses to store the results of dependency resolution for a project. |
| **[Local folder or tarball paths](upm-localpath.html)** | Specify a dependency as a local folder or tarball that contains a package. |
## Additional resources
* [Packages and package management](PackagesList.html)