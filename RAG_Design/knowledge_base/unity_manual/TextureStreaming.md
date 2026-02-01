--- 
Source: Unity 6 Manual (TextureStreaming.md)
---

# Optimizing GPU texture memory with mipmap streaming
Use mipmap streaming to limit the size of textures in GPU memory.
| Page | Description |
| --- | --- |
| [Introduction to mipmap streaming](TextureStreaming-introduction.html) | How mipmap streaming works, and its limitations. |
| [Use mipmap streaming](TextureStreaming-use.html) | Enable mipmap streaming, make a texture work with mipmap streaming, and change the mipmap level of a texture. |
| [Configure mipmap streaming](TextureStreaming-configure.html) | Enable or disable mipmap streaming on cameras, set which mipmap levels a **camera**A component which creates an image of a particular viewpoint in your scene. The output is either drawn to the screen or captured as a texture. [More info](CamerasOverview.html) See in [Glossary](Glossary.html#Camera) uses, and set a memory budget for textures. |
| [Override the mipmap level of a texture](TextureStreaming-override-mipmap-level.html) | Request that Unity overrides the mipmap level of a texture. |
| [Preload mipmap levels](TextureStreaming-preload.html) | Use the API to preload mipmap levels to avoid textures pop-in when you enable a camera. |
| [Analyze mipmap streaming](TextureStreaming-analyze.html) | Understand and debug mipmap streaming in your **scene**A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](CreatingScenes.html) See in [Glossary](Glossary.html#Scene). |