--- 
Source: Unity 6 URP Manual (renderer-features\how-to-custom-effect-render-objects.html)
---

# Example of creating a custom rendering effect using a Render Objects Renderer Feature in URP
The [Render Objects Renderer Feature](renderer-feature-render-objects.html) lets you draw objects at a specific point in the frame rendering loop. You can interpret and write rendering data such as depth and stencil in different ways, or draw a set of **GameObjects**The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](../../class-GameObject.html)
See in [Glossary](../../Glossary.html#GameObject) at a certain time.
The following example uses a Render Objects Renderer Feature to draw a GameObject in a different color if it’s behind other GameObjects.
![A character created from 3 simple capsules for the body and arms. The character is red, but as it moves behind a wall, the hidden parts are rendered blue.](../../../uploads/urp/how-to-render-objects/character-goes-behind-object.gif)
A character created from 3 simple capsules for the body and arms. The character is red, but as it moves behind a wall, the hidden parts are rendered blue.
First, create a GameObject and attach it to a new [layer](../../layers.html)Layers in Unity can be used to selectively opt groups of GameObjects in or out of certain processes or calculations. This includes camera rendering, lighting, physics collisions, or custom calculations in your own code. [More info](../../Layers.html)
See in [Glossary](../../Glossary.html#layer).
1. Create a GameObject in your **scene**A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](../../CreatingScenes.html)
   See in [Glossary](../../Glossary.html#Scene).
2. In the ****Inspector**A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](../../UsingTheInspector.html)
   See in [Glossary](../../Glossary.html#Inspector)** window, open the **Layer** dropdown and add a new layer. You can call the layer **DrawBehind**.
3. Set the GameObject to the new layer.
Next, create a Render Objects Renderer Feature that renders only the new layer, on top of the scene.
1. In the **Project** window, select the [URP Renderer asset](../universalrp-asset.html) your project uses, for example **Settings** > **PC\_Renderer**.
2. To create a Render Objects Renderer Feature, select **Add Renderer Feature** in the **Inspector** window, then select **Render Objects**.
3. To make the Renderer Feature draw only the layer with the GameObject, open the **Render Objects (Render Objects)** dropdown, then set ****Layer Mask**A value defining which layers to include or exclude from an operation, such as rendering, collision or your own code. [More info](../../Layers.html)
   See in [Glossary](../../Glossary.html#LayerMask)** to the layer.
4. Set **Event** to the **AfterRenderingOpaques** injection point. For more information about custom pass injection points, refer to [Custom Pass injection points](../customize/custom-pass-injection-points.html).
Next, adjust the Renderer Feature so it renders only the parts hidden behind other GameObjects, and in a different color.
1. Open the **Overrides** dropdown, then select **Depth** and set **Depth Test** to **Greater**.
   The Renderer Feature now only renders a **pixel**The smallest unit in a computer image. Pixel size depends on your screen resolution. Pixel lighting is calculated at every screen pixel. [More info](../../ShadowPerformance.html)
   See in [Glossary](../../Glossary.html#pixel) if its depth is greater than the current pixel in the **depth buffer**A memory store that holds the z-value depth of each pixel in an image, where the z-value is the depth for each rendered pixel from the projection plane. [More info](../../class-RenderTexture.html)
   See in [Glossary](../../Glossary.html#depthbuffer), which means the new pixel is behind another GameObject.
2. [Create a new material](../shaders-in-universalrp.html) that uses the **Universal **Render Pipeline**A series of operations that take the contents of a Scene, and displays them on a screen. Unity lets you choose from pre-built render pipelines, or write your own. [More info](../../render-pipelines.html)
   See in [Glossary](../../Glossary.html#renderpipeline)/Unlit** **shader**A program that runs on the GPU. [More info](../../Shaders.html)
   See in [Glossary](../../Glossary.html#shader).
3. Set the **Base Map** color to a color of your choice.
4. In the Renderer Feature, in the **Overrides** section, set **Material** to the material you created.
When you move the GameObject behind other GameObjects, Unity now renders the hidden parts in the color you selected.
![The red characters moves behind a wall. Unity renders the hidden parts using a blue material.](../../../uploads/urp/how-to-render-objects/character-depth-test-greater.gif)
The red characters moves behind a wall. Unity renders the hidden parts using a blue material.
## Fix overlapping areas of a GameObject
If you use a complex GameObject, the Renderer Feature might draw overlapping parts as though they’re hidden. This is because the depth of one part is greater than the overlapping part.
![A capsule with a smaller capsule attached. The Renderer Feature renders part of the larger capsule using the blue material, because its behind the smaller part.](../../../uploads/urp/how-to-render-objects/rendobj-depth-greater-see-through.png)
A capsule with a smaller capsule attached. The Renderer Feature renders part of the larger capsule using the blue material, because it’s behind the smaller part.
To fix this issue, disable rendering the whole GameObject, and create a new Renderer Feature that renders the non-hidden parts. Follow these steps:
1. In the URP Renderer asset, open the **Opaque Layer Mask** dropdown and disable the layer you added.
   Unity now doesn’t draw the layer in the opaque render pass. The Renderer Feature still draws the hidden parts, because it’s in a different render pass.
   ![Unity does not draw the character unless its behind an object](../../../uploads/urp/how-to-render-objects/rendobj-character-only-behind.png)
   Unity does not draw the character unless it’s behind an object
2. Add a new Render Objects Renderer Feature.
3. Set **Layer Mask** to the new layer, so this Renderer Feature draws the GameObject.
4. Set **Event** to the **AfterRenderingOpaques** injection point.
5. To avoid the first Renderer Feature affecting the depth calculations in the new Renderer Feature, disable **Write Depth** in the **Overrides** section of the first Renderer Feature.
The first Renderer Feature draws the hidden parts, and the second Renderer Feature draws the rest of the GameObject.
![A character created from 3 simple capsules for the body and arms. The character is red, but as it moves behind a wall, the hidden parts are rendered blue.](../../../uploads/urp/how-to-render-objects/character-goes-behind-object.gif)
A character created from 3 simple capsules for the body and arms. The character is red, but as it moves behind a wall, the hidden parts are rendered blue.
## Additional resources
* [Renderer Objects Renderer Feature reference](renderer-feature-render-objects.html)