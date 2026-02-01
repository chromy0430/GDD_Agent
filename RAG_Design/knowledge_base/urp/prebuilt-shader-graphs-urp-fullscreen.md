--- 
Source: Unity 6 URP Manual (prebuilt-shader-graphs-urp-fullscreen.html)
---

# Fullscreen shader graph reference for URP
Explore the properties and settings you can use to customize the default Fullscreen **shader**A program that runs on the GPU. [More info](../Shaders.html)
See in [Glossary](../Glossary.html#shader) graph in the Universal **Render Pipeline**A series of operations that take the contents of a Scene, and displays them on a screen. Unity lets you choose from pre-built render pipelines, or write your own. [More info](../render-pipelines.html)
See in [Glossary](../Glossary.html#renderpipeline) (URP).
Create a Fullscreen shader graph to apply a material to the entire screen at the end of the rendering process, to implement custom post-process and custom pass effects.
## Contexts
The default **Fragment** Context contains the following Blocks. Which Blocks display might change depending on the [graph settings](https://docs.unity3d.com/Packages/com.unity.shadergraph@latest/index.html?subfolder=/manual/Graph-Settings-Tab.html).
### Fragment Context
| **Input** | **Type** | **Description** |
| --- | --- | --- |
| **Base Color** | Vector3 | Sets the base color of the material. The default is [`Color.grey`](../../ScriptReference/Color-grey.html). |
| **Alpha** | Float | Sets the alpha of the material. The range is 0 to 1. The default is 1. |
| **Eye Depth** | Float | Scales a value to world space to represent the depth from the near plane. This value represents a point in world space, determined by the platform you use. The default is 0. For more information, refer to [The Depth (Z) direction in shaders](../SL-PlatformDifferences.html). This property is available only if you enable **Depth Test** or **Depth Write**, and set **Depth Write Mode** to **Eye** in the graph settings. |
| **Linear01 Depth** | Float | Uses a linear depth value between 0 and 1. The default is 0. This property is available only if you enable **Depth Test** or **Depth Write**, and set **Depth Write Mode** to **Linear 01** in the graph settings. |
| **Raw Depth** | Float | Samples the depth value from the **depth buffer**A memory store that holds the z-value depth of each pixel in an image, where the z-value is the depth for each rendered pixel from the projection plane. [More info](../class-RenderTexture.html) See in [Glossary](../Glossary.html#depthbuffer). You can also use this setting with a nonlinear depth value. The default is 0. This property is available only if you enable **Depth Test** or **Depth Write**, and set **Depth Write Mode** to **Raw** in the graph settings. |
## Graph Settings
Explore the shader graph settings you can use to customize the Vertex and Fragment Contexts.
For more details about graph settings that are common to all shader graph shaders, refer to the [Graph Settings tab](https://docs.unity3d.com/Packages/com.unity.shadergraph@latest/index.html?subfolder=/manual/Graph-Settings-Tab.html).
| **Setting** | **Description** |
| --- | --- |
| **Allow Material Override** | Enables material instances to override properties exposed in the shader graph. When disabled, materials using this shader will always use the values defined in the shader asset. |
| **Blend Mode** | Specifies the blend mode Unity uses when it renders the full-screen shader. Each option has an equivalent `BlendMode` operation. The options are:  * **Disabled**: Doesn’t use a blend mode. When you write to a Blit shader, use this option to avoid undesired effects. * **Alpha**: Calculates transparency using the alpha value of the material. * **Premultiply**: Calculates transparency using the alpha value of the material, but multiplies the RGB values by the alpha value first. * **Additive**: Adds the color of the material to the background color. * **Multiply**: Multiplies the color of the material with the background color. * **Custom**: Sets every parameter of the blending equation manually. For more information on the options for Custom Blend Mode, refer to [Custom Blend Mode settings](#custom-blend-mode). |
| **Depth Test** | Specifies the comparison function used to determine whether a pixel passes the depth test. The options are:  * **Disabled**: Doesn’t perform a depth test. * **Never**: The pixel never passes the depth test. * **Less**: Passes if the incoming depth value is less than the stored depth. * **Equal**: Passes if the incoming depth value equals the stored depth. * **L Equal**: Passes if the incoming depth value is less than or equal to the stored depth. * **Greater**: Passes if the incoming depth value is greater than the stored depth. * **Not Equal**: Passes if the incoming depth value isn’t equal to the stored depth. * **G Equal**: Passes if the incoming depth value is greater than or equal to the stored depth. * **Always**: The pixel always passes the depth test. |
| **Depth Write** | Determines whether the shader writes depth information to the depth buffer. |
| **Depth Write Mode** | Determines the depth value’s input format before Unity passes it to the depth buffer. This property determines which Depth block you can use in the Fragment context. The options are:  * **Linear Eye**: Scales a value to world space to represent the depth from the near plane. * **Linear 01**: Uses a linear depth value between 0 and 1. * **Raw**: Samples the depth value from the depth buffer.  This property is available only when you enable **Depth Test** or **Depth Write** in the graph settings. |
| **Enable Stencil** | Controls how the shader graph uses the **stencil buffer**A memory store that holds an 8-bit per-pixel value. In Unity, you can use a stencil buffer to flag pixels, and then only render to pixels that pass the stencil operation. [More info](../class-RenderTexture.html) See in [Glossary](../Glossary.html#stencilbuffer). For more information on these options, refer to [Enable Stencil settings](#enable-stencil). |
| **Custom Editor GUI** | Renders a custom editor GUI in the ****Inspector**A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](../UsingTheInspector.html) See in [Glossary](../Glossary.html#Inspector)** window of the material. Enter the name of the GUI class in the field. For more information, refer to [Control material properties in the Inspector window](../writing-shader-display-types.html). |
### Custom Blend Mode settings
The Custom blend mode properties specify the blending operation to use for this fullscreen shader graph’s alpha and color channels.
In the blend mode properties, **Src** (source) refers to the full-screen shader itself. **Dst** (destination) refers to the **Scene**A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](../CreatingScenes.html)
See in [Glossary](../Glossary.html#Scene) **camera**A component which creates an image of a particular viewpoint in your scene. The output is either drawn to the screen or captured as a texture. [More info](../CamerasOverview.html)
See in [Glossary](../Glossary.html#Camera)’s raw output, which this shader doesn’t affect. The blending operation applies the source contents to the destination contents to produce a rendering result.
For more information on the blending equation, refer to [ShaderLab command: Blend](../SL-Blend.html).
#### Color Blend Mode
Determines the blending equation Unity uses for the red, green, and blue channels (RGB). Each setting defines one part of the equation.
| **Property** | **Description** |
| --- | --- |
| **Src Color** | Sets the blend mode of the source color. |
| **Dst Color** | Sets the blend mode of the destination color. |
| **Color Operation** | Determines how to combine the source and destination color during the blending process. For information on these options, refer to [ShaderLab command: BlendOp](../SL-BlendOp.html). |
#### Alpha Blend Mode
Determines the blending equation Unity uses for the alpha channel. Each setting defines one part of the equation.
| **Property** | **Description** |
| --- | --- |
| **Src** | Sets the blend mode of the source alpha. For information on these options, refer to [Valid parameter values](../SL-Blend.html#valid-parameter-values). |
| **Dst** | Sets the blend mode of the destination alpha. For information on these options, refer to [Valid parameter values](../SL-Blend.html). |
| **Blend Operation Alpha** | Determines how to combine the source and destination alpha during the blending process. For more information on these options, refer to [ShaderLab command: BlendOp](../SL-BlendOp.html). |
### Enable Stencil settings
The Enable Stencil properties affect how this fullscreen shader graph uses the stencil buffer. For more information on the stencil buffer, refer to [SL-Stencil](../SL-Stencil.html).
| **Property** | **Description** |
| --- | --- |
| **Reference** | Determines the stencil reference value this shader uses for all stencil operations. |
| **Read Mask** | Determines which bits this shader can read during the stencil test. |
| **Write Mask** | Determines which bits this shader can write to during the stencil test. |
| **Comparison** | Determines the comparison function this shader uses during the stencil test. The options are:  * **Disabled**: Doesn’t perform a stencil test. * **Never**: The stencil test never passes. * **Less**: The stencil test passes if the pixel’s depth value is less than the value stored in the depth buffer. * **Equal**: The stencil test passes if the pixel’s depth value is equal to the value stored in the depth buffer. * **Less Equal**: The stencil test passes if the pixel’s depth value is less than or equal to the depth buffer value. This renders the tested pixel in front of other pixels. * **Greater**: The stencil test passes if the pixel’s depth value is greater than the value stored in the depth buffer. * **Not Equal**: The stencil test passes if the pixel’s depth value isn’t equal to the value stored in the depth buffer. * **Greater Equal**: The stencil test passes if the pixel’s depth value is greater than or equal to the value stored in the depth buffer. * **Always**: The stencil test always passes, and Unity doesn’t compare the pixel’s depth value to the value it has stored in the depth buffer. |
| **Pass** | Determines the operation this shader executes if the stencil test succeeds. For more information on this property’s options, refer to [Stencil pass and fail options](#stencil-pass-fail). |
| **Fail** | Determines the operation this shader executes if the stencil test fails. For more information on this property’s options, refer to [Stencil pass and fail options](#stencil-pass-fail). |
| **Depth Fail** | Determines the operation this shader executes if the depth test fails. This option has no effect if the depth test **Comparison** value is **Never** or **Disabled.** For more information on this property’s options, refer to [Stencil pass and fail options](#stencil-pass-fail). |
#### Stencil pass and fail options
| **Option** | **Description** |
| --- | --- |
| **Keep** | Doesn’t change the current contents of the stencil buffer. |
| **Zero** | Writes a value of 0 into the stencil buffer. |
| **Replace** | Writes the **Reference** value into the buffer. |
| **IncrementSaturate** | Adds a value of 1 to the current value in the buffer. A value of 255 remains 255. |
| **DecrementSaturate** | Subtracts a value of 1 from the current value in the buffer. A value of 0 remains 0. |
| **Invert** | Performs a bitwise NOT operation. This means it negates all the bits of the current value in the buffer. For example, a decimal value of 59 is 0011 1011 in binary. The NOT operation reverses each bit to 1100 0100, which is a decimal value of 196. |
| **IncrementWrap** | Adds a value of 1 to the current value in the buffer. A value of 255 becomes 0. |
| **DecrementWrap** | Subtracts a value of 1 from the current value in the buffer. A value of 0 becomes 255. |
## Additional resources
* [Create a Fullscreen Shader Graph](post-processing/post-processing-custom-effect-low-code.html#create-fullscreen-shader)
* [Shader Graph manual](https://docs.unity3d.com/Packages/com.unity.shadergraph@latest)
* [GPU render state commands in ShaderLab reference](../SL-Commands.html)