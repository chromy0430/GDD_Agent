--- 
Source: Unity 6 Manual (ts-emissive-mats-not-rendering.md)
---

## Troubleshooting emissive materials not rendering
Fix issues causing emissive materials to not render as brightly as intended.
![Three images of a rendered room showing a sphere, two boxes, and a light plane in the ceiling. Each image demonstrates how emissive materials are rendered under different techniques: only emissive materials, with a bloom postprocessing effect, and when marked as Global Illumination contributors.](../uploads/Main/ex-emiss-mat-lights.png)
Three images of a rendered room showing a sphere, two boxes, and a light plane in the ceiling. Each image demonstrates how emissive materials are rendered under different techniques: only emissive materials, with a bloom postprocessing effect, and when marked as Global Illumination contributors.
## Emissive materials not appearing to glow
When emissive materials don’t appear to glow.
### Symptoms
GameObjects with emissive materials don’t appear to glow as expected.
### Cause
When emissive materials don’t appear to glow, this indicates a **post-processing**A process that improves product visuals by applying filters and effects before the image appears on screen. You can use post-processing effects to simulate physical camera and film properties, for example Bloom and Depth of Field. [More info](PostProcessingOverview.html) post processing, postprocessing, postprocess
See in [Glossary](Glossary.html#post-processing) issue.
* Emissive materials not contributing to **global illumination**A group of techniques that model both direct and indirect lighting to provide realistic lighting results.
  See in [Glossary](Glossary.html#globalillumination). This indicates an issue with object or material setup.
### Resolution
To create the appearance of a glowing material, enable **Bloom** in the post processing stack. Refer to [Built-in RP](https://docs.unity3d.com/Packages/com.unity.postprocessing@latest?subfolder=/manual/Bloom.html), [URP](urp/post-processing-bloom.html), or [HDRP](https://docs.unity3d.com/Packages/com.unity.render-pipelines.high-definition@latest?subfolder=/manual/Post-Processing-Bloom.html) respectively for the steps required for each of the different pipelines.
## Emissive materials not contributing to global illumination
When emissive materials don’t contribute to global illumination.
### Symptoms
Emissive materials don’t contribute to global illumination and don’t light up the **scene**A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](CreatingScenes.html)
See in [Glossary](Glossary.html#Scene) as expected.
### Cause
This indicates an issue with object or material setup.
### Resolution
![Standard Shader Material Inspector window in the Built-in render pipeline. The Emission properties are highlighted by a blue box.](../uploads/Main/inspector-color-materials-property.png)
Standard Shader Material Inspector window in the Built-in render pipeline. The Emission properties are highlighted by a blue box.
To make sure the emissive objects are ready for lightmapping, follow these steps:
\* In the ****Shader**A program that runs on the GPU. [More info](Shaders.html)
See in [Glossary](Glossary.html#shader) Material **Inspector**A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](UsingTheInspector.html)
See in [Glossary](Glossary.html#Inspector)** window, go to **Emission** and set **Global Illumination** to **Baked**. Refer to [Built-in RP](StandardShaderMaterialParameters.html), [URP](urp/shaders-in-universalrp-reference.html), or [HDRP](https://docs.unity3d.com/Packages/com.unity.render-pipelines.high-definition@latest?subfolder=/manual/unlit-material-inspector-reference.html) respectively for the **Emission** property in the different pipelines.
\* Select the emissive **GameObject**The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](class-GameObject.html)
See in [Glossary](Glossary.html#GameObject) and go to the [Mesh Renderer](class-MeshRenderer.md#lighting)A mesh component that takes the geometry from the Mesh Filter and renders it at the position defined by the object’s Transform component. [More info](class-MeshRenderer.html)
See in [Glossary](Glossary.html#MeshRenderer) component property settings of the GameObject.
\* Enable **Contribute Global Illumination** to mark the object as a Global Illumination contributor.
## Resolution - Inspect lighting settings
If the previous resolutions don’t solve the issue, make sure that the baked contribution from baked emissive objects is not disabled. To do so, go to the [Lighting window](lighting-window.html) and make sure that **Indirect Intensity** is not set to zero. If it is set to zero, it disables all indirect lighting which includes baked contribution from baked emissive objects.