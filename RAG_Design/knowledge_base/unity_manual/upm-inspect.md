--- 
Source: Unity 6 Manual (upm-inspect.md)
---

# Inspect packages
The **Project window**A window that shows the contents of your `Assets` folder (Project tab) [More info](ProjectView.html)
See in [Glossary](Glossary.html#Projectwindow) displays the list of packages currently installed in your project from all sources. This list includes **immutable**You cannot change the contents of an immutable (read-only) package. This is the opposite of **mutable**. Most packages are immutable, including packages downloaded from the package registry or by Git URL.
See in [Glossary](Glossary.html#immutable) packages that you installed from a package registry and **mutable**You can change the contents of a mutable package. This is the opposite of **immutable**. Only **Local package****s** and **Embedded package****s** are mutable.
See in [Glossary](Glossary.html#mutable) packages (such as embedded and local packages).
![Registry package (immutable) on the left and an embedded package (mutable) on the right](../uploads/Main/upm-inspect.png)
Registry package (immutable) on the left and an embedded package (mutable) on the right
You can inspect the contents of any package that appears in the **Project** window. You can also inspect the **package manifest**Each package has a *manifest*, which provides information about the package to the Package Manager. The manifest contains information such as the name of the package, its version, a description for users, dependencies on other packages (if any), and other details. [More info](upm-manifestPkg.html)
See in [Glossary](Glossary.html#packagemanifest) through a dedicated **Inspector**A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](UsingTheInspector.html)
See in [Glossary](Glossary.html#Inspector).
To inspect a package manifest, open the package’s `package.json` file from the **Project** window.
![Inspecting a package manifest](../uploads/Main/upm-project-view.png)
Inspecting a package manifest
For packages with a [custom or local label](cus-location.html), you can change the package contents and [edit the package manifest](class-PackageManifestImporter.html).
## Additional resources
* [Package manifest reference](upm-manifestPkg.html)