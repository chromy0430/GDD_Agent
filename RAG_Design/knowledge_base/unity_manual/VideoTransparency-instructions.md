--- 
Source: Unity 6 Manual (VideoTransparency-instructions.md)
---

# Set up transparent videos in Unity
Import and prepare per-pixel transparent videos for use with Unity and edit global transparency levels of your videos.
You can control the transparency of an entire video (global alpha), or, with certain video formats, you can use different transparency levels for each **pixel**The smallest unit in a computer image. Pixel size depends on your screen resolution. Pixel lighting is calculated at every screen pixel. [More info](ShadowPerformance.html)
See in [Glossary](Glossary.html#pixel) (per-pixel alpha). This information covers how to prepare and use these videos in Unity.
For more information about the per-pixel alpha and global alpha transparency types, refer to [Introduction to video transparency support](VideoTransparency-overview.html).
## Change your entire video’s transparency (global alpha)
To change the level of transparency for your entire video’s image in Unity:
* Create a **Video Player** (**Add** (**+**) > **Video** > **Video Player**).
* In the **Video Player** **Inspector**A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](UsingTheInspector.html)
  See in [Glossary](Glossary.html#Inspector) window, set **Render Mode** to ****Camera**A component which creates an image of a particular viewpoint in your scene. The output is either drawn to the screen or captured as a texture. [More info](CamerasOverview.html)
  See in [Glossary](Glossary.html#Camera) Near Plane** or **Camera Far Plane**.
* Change **Alpha** to your preferred value.
  + Set to 0 for full transparency (the video isn’t visible).
  + Set to 1 for full visibility of the video.
  + Set to any value between 0 and 1 for partial transparency.
As a result, your video appears with your preferred transparency level.
## Change the transparency of pixels in your video (per-pixel alpha)
You can’t control per-pixel transparency for imported video clips in the Unity Editor. Instead you need to edit the video’s transparency with an external tool then import it into Unity.
To use a video with per-pixel transparency in Unity:
1. Use an external video rendering or authoring application to create your transparent video or image sequence.
2. Export the video in a format that allows transparency and that Unity supports. For more information, refer to [Supported codecs for transparent videos (per-pixel alpha)](VideoTransparency-codecs.html).
3. Drag your video file into Unity. The video imports as a [Video Clip](class-VideoClip.html).
4. If your video has the Apple ProRes 4444 codec, [Change your Video Clip settings](#change-video-clip).
As a result, your transparent video is ready for use in Unity.
## Change your Video Clip settings
If your transparent video’s codec is Apple ProRes 4444:
1. Select your imported video clip. The [Video Clip Importer](class-VideoClip.html) Inspector window displays.
2. Enable **Transcode**.
3. Enable **Keep Alpha**.
As a result, your ProRes video is ready for use in Unity.
## References
* [Video Player](https://docs.unity3d.com/Manual/VideoPlayer.html)
* [Introduction to video transparency support in Unity](VideoTransparency-overview.html)
* [Supported codecs for transparent videos (per-pixel alpha)](VideoTransparency-codecs.html)