--- 
Source: Unity 6 Manual (UIE-USS-Selectors-descendant.md)
---

# Descendant selectors
USS descendant selectors match elements that are the descendant of another element in the [visual tree](UIE-VisualTree.html)An object graph, made of lightweight nodes, that holds all the elements in a window or panel. It defines every UI you build with the UI Toolkit.
See in [Glossary](Glossary.html#visualtree).
## Syntax
A descendant selector consists of multiple simple selectors separated by a space:
```
selector1 selector2 {...}
```
## Example
To demonstrate how simple selectors match elements, here is an example UI Document.
```
<UXML xmlns="UnityEngine.UIElements">
  <VisualElement name="container1">
    <VisualElement name="container2" class="yellow">
      <Button name="OK" class="yellow" text="OK" />
      <Button name="Cancel" text="Cancel" />
    </VisualElement>
  </VisualElement>
</UXML>
```
With no styles applied, the UI looks like the following:
![Example buttons with margins and thin blue borders.](../uploads/Main/uss-selectors-nostyle.png)
Example buttons with margins and thin blue borders.
The following descendant selector style rule matches both the inner element and the first button.
```
#container1 .yellow {
  background-color: yellow;
}
```
The UI looks like the following when you apply the style:
![The container2 and the OK button have a yellow background.](../uploads/Main/uss-selectors-descendant.png)
The container2 and the OK button have a yellow background.
**Note**: Heavy use of descendant selectors could negatively affect performance. For more performance guidelines, see [Best practices for USS](UIE-USS-WritingStyleSheets.html).
## Additional resources
* [Best practices for USS](UIE-USS-WritingStyleSheets.html)