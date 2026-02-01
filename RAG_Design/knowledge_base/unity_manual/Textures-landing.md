--- 
Source: Unity 6 Manual (Textures-landing.md)
---

# Custom textures
Resources for importing, converting, and loading textures so that you can use them in **shaders**A program that runs on the GPU. [More info](Shaders.html)
See in [Glossary](Glossary.html#shader) and materials.
| **Page** | **Description** |
| --- | --- |
| [Get started with textures](textures-getting-started.html) | Learn about texture types, GPU **texture formats**A file format for handling textures during real-time rendering by 3D graphics hardware, such as a graphics card or mobile device. [More info](texture-choose-format-by-platform.html) See in [Glossary](Glossary.html#textureformat), and mipmaps. |
| [Import a texture](ImportingTextures.html) | Import an image or movie file as a Texture asset. |
| [Texture arrays](class-Texture2DArray.html) | Resources for creating and using an array of textures with the same size, format and flags. |
| [Cubemaps](class-Cubemap-landing.html)A collection of six square textures that can represent the reflections in an environment or the skybox drawn behind your geometry. The six squares form the faces of an imaginary cube that surrounds an object; each face represents the view along the directions of the world axes (up, down, left, right, forward and back). [More info](class-Cubemap-landing.html) See in [Glossary](Glossary.html#Cubemap) | Resources for creating and using a collection of six square textures that represent the reflections in an environment, and form an imaginary cube around a **GameObject**The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](class-GameObject.html) See in [Glossary](Glossary.html#GameObject). |
| [3D textures](class-Texture3D.html) | Resources for creating and using a bitmap image that contains information in three dimensions, for example to create volumetric effects, 3D meshes, or animated textures. |
| [Rendering to a texture](render-texture-landing.html) | Techniques for rendering a **camera**A component which creates an image of a particular viewpoint in your scene. The output is either drawn to the screen or captured as a texture. [More info](CamerasOverview.html) See in [Glossary](Glossary.html#Camera) view to a **render texture**A special type of Texture that is created and updated at runtime. To use them, first create a new Render Texture and designate one of your Cameras to render into it. Then you can use the Render Texture in a Material just like a regular Texture. [More info](class-RenderTexture.html) See in [Glossary](Glossary.html#RenderTexture), or using a shader to draw to a texture. |
| [Playing video in Movie Textures](MovieTexture-landing.html) | Resources for importing a video file into Unity as an animated texture, and playing it back. |
| [Texture optimization](TextureLoading.html) | Techniques for speeding up texture loading, and reducing how much memory textures use. |
| [Textures reference](textures-reference.html) | Explore the properties in Texture Import Settings windows to configure how Unity imports and converts textures. |
## Additional resources
* [Import a texture into the render graph system in URP](urp/render-graph-import-a-texture.html)
* [Draw a texture in a shader in URP](urp/writing-shaders-urp-unlit-texture.html)
* [Rendering to a render texture in URP](urp/rendering-to-a-render-texture.html)