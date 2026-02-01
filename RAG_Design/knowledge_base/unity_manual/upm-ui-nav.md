--- 
Source: Unity 6 Manual (upm-ui-nav.md)
---

# Navigation panel reference
Use the Package Manager’s navigation panel to select which subset of packages you want to view.
![The navigation panel (A), the list panel (B), and the details panel (C)](../uploads/Main/upm-ui-nav.png)
The navigation panel **(A)**, the list panel **(B)**, and the details panel **(C)**
Select a context from the navigation panel **(A)** to list those types of packages in the list panel **(B)**. When you select a package from the list panel, its details display in the details view **(C)**.
## Context list
Select the context you want from the navigation panel. You can select from these options:
| **Context** | **Description** |
| --- | --- |
| **In Project** | Displays all feature sets and packages installed in your project, including [local](upm-localpath.html), [git](upm-git.html), and [embedded](upm-embed.html) packages, and packages installed from any registry. The list also includes any packages from the Asset Store that you added from the **My Assets** context.  **In Project** has nested entries that appear when the proper conditions are met: - **Updates** lists all packages in your project that you can update, including Asset Store packages. - **Errors and Warnings** lists all packages in your project that require attention. |
| **Unity Registry** | Displays all **feature sets**A feature set is a collection of related packages that you can use to achieve specific results in the Unity Editor. You can manage feature sets directly in Unity’s Package Manager. [More info](FeatureSets.html) See in [Glossary](Glossary.html#featureset) and packages on the [Unity package registry](upm-concepts.html#Registry), regardless of whether they’re already installed in your project. This doesn’t include packages installed from any other location or from any [scoped registry](upm-scoped.html). |
| **My Assets** | Displays all [Asset Store packages](AssetStorePackages.html)A bundled collection of assets or tools available for purchase or download on the Unity Asset Store, compressed and stored as an asset package (`.unitypackage` extension) or a UPM package. You can manage your packages from the Asset Store either on the online store or through the Package Manager window. [More info](AssetStorePackages.html) See in [Glossary](Glossary.html#AssetStorepackage) that you have purchased using the Unity ID you’re currently logged in with. |
| **Built-in** | Displays only built-in Unity packages, which represent core Unity features. You can use these packages to [turn Unity modules on and off](upm-ui-disable.html).  **Tip**: You can find out more about what each built-in package (module) implements in the [Unity Scripting API](upm-api.html). Each module assembly page lists which APIs the built-in package implements. |
| **Services**A Unity facility that provides a growing range of complimentary services to help you make games and engage, retain and monetize audiences. [More info](UnityServices.html) See in [Glossary](Glossary.html#Services) | Displays integrated [services](UnityServices.html) to help you to engage, retain, and monetize audiences. |
| **My Registries** | Displays any packages available from any [scoped registry](upm-scoped.html) installed in this project.  This context appears only if you installed a scoped registry in this project.  If you installed a scoped registry but it’s not listed in the **My Registries** context or the **My Registries** context isn’t available at all, it might be because the package registry server you added doesn’t implement either of the `/-/v1/search` or `/-/all` endpoints, which means that it’s not compatible with Unity’s Package Manager. |
**Note**: If you entered text in the [search box](upm-ui-search.html) or set [filters](upm-ui-filter2.html), the list panel displays only feature sets and packages which match the context, search criteria, and active filters.
## Additional resources
* [List panel](upm-ui-list.html)
* [Details panel](upm-ui-details.html)