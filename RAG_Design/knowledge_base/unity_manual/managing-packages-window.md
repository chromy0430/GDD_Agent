--- 
Source: Unity 6 Manual (managing-packages-window.md)
---

# Package management with the Package Manager window
Use the Package Manager window to manage packages in your project.
| **Topic** | **Description** |
| --- | --- |
| **[Add and remove UPM packages or feature sets](upm-ui-actions.html)** | Add and remove packages whose type is UPM. Add and remove **feature sets**A feature set is a collection of related packages that you can use to achieve specific results in the Unity Editor. You can manage feature sets directly in Unity’s Package Manager. [More info](FeatureSets.html) See in [Glossary](Glossary.html#featureset). |
| **[Add and remove asset packages](upm-ui-actions-ap.html)** | Add and remove packages whose type is `.unitypackage`. |
| **[Disable a built-in package](upm-ui-disable.html)** | Reduce your project’s build size by disabling unused **built-in packages***Built-in* packages allow users to toggle Unity features on or off through the Package Manager. Enabling or disabling a package reduces the run-time build size. For example, most projects don’t use the legacy Particle System. By removing the abstracted package of this feature, the related code and resources are not part of the final built product. Typically, these packages contain only the package manifest and are bundled with Unity (rather than available on the package registry). See in [Glossary](Glossary.html#built-inpackage). |
| **[Perform an action on multiple packages](upm-ui-multi.html)** | Learn how to use Unity’s Package Manager to select and perform actions on multiple packages or feature sets simultaneously. |
| **[Find package documentation](upm-docs.html)** | Find package-specific documentation for the individual packages that you add to your project. |
## Additional resources
* [Package types](upm-package-types.html)
* [Package management with the project manifest file](managing-packages-manifest.html)
* [Package management with the scripting API](managing-packages-api.html)