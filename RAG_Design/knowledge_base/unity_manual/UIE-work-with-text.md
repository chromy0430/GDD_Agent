--- 
Source: Unity 6 Manual (UIE-work-with-text.md)
---

# Work with text
Text objects are defined by the following attributes of a UI control:
* The `text` attribute of some UI controls, such as [Label](UIE-uxml-element-Label.html) or [TextElement](UIE-uxml-element-TextElement.html), that sets the display text.
* The `value` attribute of the [TextField](UIE-uxml-element-TextField.html) that accepts the input text, and the `label` attribute that sets the display text for [TextField](UIE-uxml-element-TextField.html).
You can use [USS](UIE-USS.html) [text properties](UIE-USS-SupportedProperties.html#unity-text) to style text, such as set the font size and color, etc.
You can also add a new font to style text. Convert fonts to font assets before you use them in your project. In addition to USS styling, you can use rich text tags to style certain words in a text string.
| **Topic** | **Description** |
| --- | --- |
| [Get started with text](UIE-get-started-with-text.html) | Learn how to style text, create fonts, and style with rich text tags and style sheets by examples. |
| [Advanced Text Generator](UIE-advanced-text-generator.html) | Add comprehensive Unicode support and text shaping capabilities to your project. |
| [Style text with USS](UIB-styling-ui-text.html) | Style text with USS text properties inline in UXML, a USS file, or directly in UI Builder. |
| [Style text with rich text tags](UIE-rich-text-tags.html) | Style words between tags in a text string. |
| [Font assets](UIE-font-asset-landing.html) | Understand different font assets and all their properties. |
| [Text effects](UIE-text-effects.html) | Apply text effects to text elements to enhance the visual appearance of the text. |
| [Style sheet assets](UIE-style-sheet.html) | Create custom text styles to extend the rich text tags. |
| [Include sprites in text](UIE-sprite.html) | Create **sprite**A 2D graphic objects. If you are used to working in 3D, Sprites are essentially just standard textures but there are special techniques for combining and managing sprite textures for efficiency and convenience during development. [More info](sprite/sprite-landing.html) See in [Glossary](Glossary.html#Sprite) assets to interpret emoji characters and include them in text. |
| [Color gradients](UIE-color-gradient.html) | Create color gradients to apply up to four colors for each character in a text string. |
| [Color emojis](UIE-color-emojis.html) | Include color glyphs and emojis in text. |
| [Language direction](ui-systems/language-direction.html) | Set the text directionality of a text element to support right-to-left (RTL) languages. |
| [UITK Text Settings assets](UIE-text-setting-asset.html) | Referenced by a Panel Settings asset and controls the default values for all text objects used within that Panel. |
| [Fallback font](UIE-fallback-font.html) | Add fallback font for missing character in a font asset. |
| [Create custom text animation](ui-systems/create-custom-text-animation.html) | Use the `TextElement.PostProcessTextVertices` API to create custom text animation |
## Additional resources
* [MeshGenerationContext](../ScriptReference/UIElements.MeshGenerationContext.html)
* [UI Renderer](UIE-ui-renderer.html)
* 📖 **E-Book**: [UI Toolkit for advanced Unity developers - Graphic and font assets preparation](best-practice-guides/ui-toolkit-for-advanced-unity-developers/graphic-and-font-assets-preparation.html)
* 📖 **E-Book**: [UI Toolkit for advanced Unity developers - Text](best-practice-guides/ui-toolkit-for-advanced-unity-developers/text.html)