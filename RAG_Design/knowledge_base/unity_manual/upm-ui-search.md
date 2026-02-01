--- 
Source: Unity 6 Manual (upm-ui-search.md)
---

# Search box
You can use the search box at the top of the list panel in the Package Manager window to find any packages or **feature sets**A feature set is a collection of related packages that you can use to achieve specific results in the Unity Editor. You can manage feature sets directly in Unity’s Package Manager. [More info](FeatureSets.html)
See in [Glossary](Glossary.html#featureset) that match the text you enter.
The Package Manager window updates the list as you enter search text, displaying every matching package or feature set for the context you’ve selected in the [navigation panel](upm-ui-nav.html).
**Note**: You can search for either Unity packages and feature sets or **Asset Store**A growing library of free and commercial assets created by Unity and members of the community. Offers a wide variety of assets, from textures, models and animations to whole project examples, tutorials and Editor extensions. [More info](AssetStore.html)
See in [Glossary](Glossary.html#AssetStore) packages. The list context you choose defines where the Package Manager searches:
| **List context** | **Where the Package Manager searches** |
| --- | --- |
| **In Project** | The package cache and the `Packages` folder under your current project. |
| **Unity Registry** | The list of packages and feature sets on the Unity [registry](upm-concepts.html#Registry). |
| **My Assets** | The list of [Asset Store packages](AssetPackagesOrganize.html)A bundled collection of assets or tools available for purchase or download on the Unity Asset Store, compressed and stored as an asset package (`.unitypackage` extension) or a UPM package. You can manage your packages from the Asset Store either on the online store or through the Package Manager window. [More info](AssetStorePackages.html) See in [Glossary](Glossary.html#AssetStorepackage) available with your Unity account. |
| **Built-in** | The list of [built-in](upm-concepts.html#BuiltIn) packages on the Unity registry. |
| **Services**A Unity facility that provides a growing range of complimentary services to help you make games and engage, retain and monetize audiences. [More info](UnityServices.html) See in [Glossary](Glossary.html#Services) | The list of integrated [services](UnityServices.html) you can install. |
| **My Registries** | Any [scoped registry](upm-scoped.html) defined for your project. |
**Important**: The Package Manager window recalls your search terms on a per-context basis. For example, if you set a search term in **In Project**, the Package Manager window filters that list. If you then select any other context, the Package Manager window resets the search and lists all packages for that context. But if you then return to **In Project**, the Package Manager window restores your search term and filters the **In Project** list again.
To illustrate this per-context search scope further, if you enter the same search term in separate contexts, you’ll get different results. For example, if you choose the **Unity Registry** context then type `web` in the search box, the results will be different if you then choose the **Built-in** context and search for the same term:
![Searching for the same term in separate contexts yields different results](../uploads/Main/upm-ui-search.png)
Searching for the same term in separate contexts yields different results
You can search for a package or a feature set either by:
* Its [display name](upm-manifestPkg.html#displayName) (as it appears at the top of the [details panel](upm-ui-details.html)).
* Its [name (ID)](upm-manifestPkg.html#name) (Unity packages and feature sets only), which is the registered package name that begins with **com.unity**.
Your search text can match the beginning, middle, or end of the name. The Package Manager window updates the list dynamically.
## Additional resources
* [list panel](upm-ui-list.html)