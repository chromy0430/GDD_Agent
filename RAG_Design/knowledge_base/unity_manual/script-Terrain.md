--- 
Source: Unity 6 Manual (script-Terrain.md)
---

# Terrain
The Unity Editor includes a built-in set of **Terrain**The landscape in your scene. A Terrain GameObject adds a large flat plane to your scene and you can use the Terrain’s Inspector window to create a detailed landscape. [More info](terrain-UsingTerrains.html)
See in [Glossary](Glossary.html#Terrain) features that you can use to add landscapes to your game. In the Unity Editor, you can create multiple Terrain tiles, adjust the height or appearance of your landscape, and add trees or grass to it. At runtime, Unity optimizes built-in Terrain rendering for efficiency. The pages in this section explain the built-in options available for Terrain and how to use them.
| **Topic** | **Description** |
| --- | --- |
| [**Create and edit Terrains**](terrain-UsingTerrains.html) | Add and edit Terrain **GameObjects**The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](class-GameObject.html) See in [Glossary](Glossary.html#GameObject) |
| [**Create Neighbor Terrains**](terrain-CreateNeighborTerrains.html) | Create adjacent Terrain tiles |
| [**Height**](terrain-Height-Landing.html) | Sculpt the terrain’s height with the built-in Terrain system and the Terrain Tools package |
| [**Textures and layers**](terrain-Textures-Landing.html) | Paint textures on the terrain and combine them in layers |
| [**Brushes**](class-Brush.html) | Understand Brushes and Brush settings |
| [**Add trees to the terrain**](terrain-Trees-Landing.html) | Create and customize Trees |
| [**Animate trees with Wind Zones**](class-WindZone.html) | Simulate wind to animate trees on your Terrain. |
| [**Wind Zones**](class-WindZone.html) | Adjust **Wind Zone**A GameObject that adds the effect of wind to your terrain. For instance, Trees within a wind zone will bend in a realistic animated fashion and the wind itself will move in pulses to create natural patterns of movement among the tree. [More info](class-WindZone.html) See in [Glossary](Glossary.html#windzone) settings |
| [**Grass and other details**](terrain-Grass.html) | Add and remove paint details |
| [**Working with Heightmaps**](terrain-Heightmaps.html) | Import and export **heightmaps**A greyscale Texture that stores height data for an object. Each pixel stores the height difference perpendicular to the face that pixel represents. See in [Glossary](Glossary.html#heightmap) |
| [**Terrain Settings reference**](terrain-OtherSettings.html) | Adjust the Terrain settings |
| [**Render Terrain with Shader Graph**](terrain-shader-graph.html) | Use **Shader**A program that runs on the GPU. [More info](Shaders.html) See in [Glossary](Glossary.html#shader) Graph to create a new material for HDRP or URP terrains |
| [**Using Terrain at runtime**](terrain-Runtime.html) | Create Terrain dynamically at runtime |
## Additional resources
* [Terrain and the Terrain Tools package](TerrainTools.html)
* [Create trees with Tree Editor](class-Tree.html)
* [Terrain Texture Node](https://docs.unity3d.com/Packages/com.unity.shadergraph@latest/index.html?subfolder=/manual/Terrain-Texture-Node.html) in Shader Graph