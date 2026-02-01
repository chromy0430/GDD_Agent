--- 
Source: Unity 6 Manual (cus-location.md)
---

# Comparison of package creation locations
Compare the different locations where you can place the package you create.
By default, Unity places packages you create in the `Packages` folder of your project. However, you can move a package outside the project folder during development and optionally link it back to the project.
Packages in either location are identical in structure, but each supports different workflows, especially involving modularity, reuse, and collaboration. Understanding these differences can help you avoid refactoring later.
Use the following table to understand the key differences between packages you create inside and outside of your project:
| **Feature or characteristic** | **Packages in your project folder** | **Packages outside your project folder** |
| --- | --- | --- |
| Package location | Inside the `Packages` subfolder of your Unity project | Outside the `Packages` subfolder of your Unity project |
| Typical use | Develop a package within a single project (the current project) | Develop and reuse the package across multiple projects |
| Creation method | Package Manager window | Package Manager window with some manual steps |
| **Project manifest**Each Unity project has a *project manifest*, which acts as an entry point for the Package Manager. This file must be available in the `<project>/Packages` directory. The Package Manager uses it to configure many things, including a list of dependencies for that project, as well as any package repository to query for packages. [More info](upm-manifestPrj.html) See in [Glossary](Glossary.html#projectmanifest) file reference | Implicit (Unity automatically detects packages in the `Packages` subfolder) | Explicit reference required |
| **Version control**A system for managing file changes. You can use Unity in conjunction with most common version control tools, including Perforce, Git, Mercurial and PlasticSCM. [More info](VersionControl.html) See in [Glossary](Glossary.html#versioncontrol) | Same repository as the project | Different repository than the project |
| Portability during development | Highly portable if the project uses version control | Limited due to environment-specific paths and system configuration |
| Identifying label that appears in Package Manager window | **Custom** | **Local** |
After you decide on a location for the package you will create, begin the package creation process by referring to [package development workflow](CustomPackages.html).
## Additional resources
* [Package creation](cus-pkg-lp.html)
* [Package development workflow](CustomPackages.html)
* [Project manifest file](upm-manifestPrj.html)
* [Local folder or tarball paths](upm-localpath.html)