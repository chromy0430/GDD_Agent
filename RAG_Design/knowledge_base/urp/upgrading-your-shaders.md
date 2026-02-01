--- 
Source: Unity 6 URP Manual (upgrading-your-shaders.html)
---

# Convert shaders to URP with the Render Pipeline Converter
Use the [Render Pipeline Converter](features/rp-converter.html) to convert any of Unity’s built-in Built-In **Render Pipeline**A series of operations that take the contents of a Scene, and displays them on a screen. Unity lets you choose from pre-built render pipelines, or write your own. [More info](../render-pipelines.html)
See in [Glossary](../Glossary.html#renderpipeline) materials and shaders to a URP material and **shader**A program that runs on the GPU. [More info](../Shaders.html)
See in [Glossary](../Glossary.html#shader). Refer to [Shader mappings](upgrade-shaders-landing.html) for more information.
> **Note**: The Render Pipeline Converter makes irreversible changes to the project. Back up your project before the conversion.
If the preview thumbnails in the Project view are not shown correctly after the conversion, try right-clicking anywhere in the Project view and selecting **Reimport All**.
For [SpeedTree](https://docs.unity3d.com/Manual/SpeedTree.html) Shaders, Unity does not re-generate Materials when you re-import them, unless you click the **Generate Materials** or **Apply & Generate Materials** button.
## Shader mappings
The following table shows which URP shaders the Built-in Render Pipeline shaders convert to when you use the Render Pipeline Converter.
| Unity built-in shader | Universal Render Pipeline shader |
| --- | --- |
| Standard | Universal Render Pipeline/Lit |
| Standard (Specular Setup) | Universal Render Pipeline/Lit |
| Standard **Terrain**The landscape in your scene. A Terrain GameObject adds a large flat plane to your scene and you can use the Terrain’s Inspector window to create a detailed landscape. [More info](../terrain-UsingTerrains.html) See in [Glossary](../Glossary.html#Terrain) | Universal Render Pipeline/Terrain/Lit |
| **Particles**A small, simple image or mesh that is emitted by a particle system. A particle system can display and move particles in great numbers to represent a fluid or amorphous entity. The effect of all the particles together creates the impression of the complete entity, such as smoke. [More info](../class-ParticleSystem.html) See in [Glossary](../Glossary.html#particle)/Standard Surface | Universal Render Pipeline/Particles/Lit |
| Particles/Standard Unlit | Universal Render Pipeline/Particles/Unlit |
| Mobile/Diffuse | Universal Render Pipeline/Simple Lit |
| Mobile/Bumped Specular | Universal Render Pipeline/Simple Lit |
| Mobile/Bumped Specular(1 Directional Light) | Universal Render Pipeline/Simple Lit |
| Mobile/Unlit (Supports Lightmap) | Universal Render Pipeline/Simple Lit |
| Mobile/VertexLit | Universal Render Pipeline/Simple Lit |
| Legacy Shaders/Diffuse | Universal Render Pipeline/Simple Lit |
| Legacy Shaders/Specular | Universal Render Pipeline/Simple Lit |
| Legacy Shaders/Bumped Diffuse | Universal Render Pipeline/Simple Lit |
| Legacy Shaders/Bumped Specular | Universal Render Pipeline/Simple Lit |
| Legacy Shaders/Self-Illumin/Diffuse | Universal Render Pipeline/Simple Lit |
| Legacy Shaders/Self-Illumin/Bumped Diffuse | Universal Render Pipeline/Simple Lit |
| Legacy Shaders/Self-Illumin/Specular | Universal Render Pipeline/Simple Lit |
| Legacy Shaders/Self-Illumin/Bumped Specular | Universal Render Pipeline/Simple Lit |
| Legacy Shaders/Transparent/Diffuse | Universal Render Pipeline/Simple Lit |
| Legacy Shaders/Transparent/Specular | Universal Render Pipeline/Simple Lit |
| Legacy Shaders/Transparent/Bumped Diffuse | Universal Render Pipeline/Simple Lit |
| Legacy Shaders/Transparent/Bumped Specular | Universal Render Pipeline/Simple Lit |
| Legacy Shaders/Transparent/Cutout/Diffuse | Universal Render Pipeline/Simple Lit |
| Legacy Shaders/Transparent/Cutout/Specular | Universal Render Pipeline/Simple Lit |
| Legacy Shaders/Transparent/Cutout/Bumped Diffuse | Universal Render Pipeline/Simple Lit |
| Legacy Shaders/Transparent/Cutout/Bumped Specular | Universal Render Pipeline/Simple Lit |