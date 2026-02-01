--- 
Source: Unity 6 Manual (UIE-USS-Selectors.md)
---

# USS selectors
Selectors decide which elements that USS rules affect.
USS supports a set of simple selectors that are analogous, but not identical, to simple selectors in CSS. A simple selector matches elements by element type, USS class, element name, and wildcard.
You can combine simple selectors into complex selectors, or append [pseudo-classes](UIE-USS-Selectors-Pseudo-Classes.html) to them to target elements in specific states. USS supports descendant, child, and multiple complex selectors.
| **Topic** | **Description** |
| --- | --- |
| [Type selectors](UIE-USS-Selectors-type.html) | Match elements based on their element types. |
| [Name selectors](UIE-USS-Selectors-name.html) | Match elements based on the name of an element. |
| [Class selectors](UIE-USS-Selectors-class.html) | Match elements that have specific USS classes assigned. |
| [Universal selectors](UIE-USS-Selectors-universal.html) | Match any element. |
| [Descendant selectors](UIE-USS-Selectors-descendant.html) | Match elements that are descendants of another element in the **visual tree**An object graph, made of lightweight nodes, that holds all the elements in a window or panel. It defines every UI you build with the UI Toolkit. See in [Glossary](Glossary.html#visualtree). |
| [Child selectors](UIE-USS-Selectors-child.html) | Match elements that are children of another element in the visual tree. |
| [Multiple selectors](UIE-USS-Selectors-multiple.html) | Select elements that match all the simple selectors. |
| [Selectors list](UIE-USS-Selectors-list.html) | Create a comma-separated list of selectors that share the same style rule. |
| [Pseudo-classes](UIE-USS-Selectors-Pseudo-Classes.html) | Use pseudo-classes with selectors to target elements that are in a specific state. |
| [Selector precedence](UIE-uss-selector-precedence.html) | Understand USS precedence when multiple USS rules target the same elements. |
## Additional resources
* [Best practices for USS](UIE-USS-WritingStyleSheets.html)