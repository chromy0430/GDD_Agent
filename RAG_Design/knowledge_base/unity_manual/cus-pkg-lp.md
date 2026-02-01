--- 
Source: Unity 6 Manual (cus-pkg-lp.md)
---

# Package creation
Create packages that deliver Unity Editor or runtime tools to support game development workflows.
This information focuses on creating Unity Package Manager (UPM) packages. **UPM packages**A **Package** managed by the **Unity Package Manager**. Refer to **Packages**.
See in [Glossary](Glossary.html#UPMpackage) typically include functional content, such as custom Editor windows, runtime tools, or utilities designed for use during development, rather than content-only assets like models or textures. These tools are often designed to streamline workflows for game designers, developers, or technical artists within a Unity project.
UPM packages offer modularity, versioning, and reuse across projects. UPM packages support a wide range of content, including C# **scripts**A piece of code that allows you to create your own Components, trigger game events, modify Component properties over time and respond to user input in any way you like. [More info](creating-scripts.html)
See in [Glossary](Glossary.html#Scripts), managed assemblies, and built-in **plug-ins**A set of code created outside of Unity that creates functionality in Unity. There are two kinds of plug-ins you can use in Unity: Managed plug-ins (managed .NET assemblies created with tools like Visual Studio) and Native plug-ins (platform-specific native code libraries). [More info](./plug-ins.html)
See in [Glossary](Glossary.html#plug-in). While the primary purpose is tool delivery, packages can also include supporting assets like animations, textures, **audio clips**A container for audio data in Unity. Unity supports mono, stereo and multichannel audio assets (up to eight channels). Unity can import .aif, .wav, .mp3, and .ogg audio file format, and .xm, .mod, .it, and .s3m tracker module formats. [More info](class-AudioClip.html)
See in [Glossary](Glossary.html#AudioClip), or models when necessary.
For more information about the differences between UPM packages and **asset packages**A collection of files and data from Unity projects, or elements of projects, which are compressed and stored in one file, similar to Zip files, with the `.unitypackage` extension. Asset packages are a handy way of sharing and re-using Unity projects and collections of assets. [More info](AssetPackages.html)
See in [Glossary](Glossary.html#assetpackage) (`.unitypackage` format), refer to [package types](upm-package-types.html). If you want to create an asset package rather than a UPM package, refer to [create and export asset packages](AssetPackagesCreate.html).
| **Topic** | **Description** |
| --- | --- |
| [Get started with package creation](cus-pkg-intro.html) | Get a high-level overview of creating UPM packages. |
| [Comparison of package creation locations](cus-location.html) | Choose whether to create your package inside or outside of the project’s `Packages` folder. |
| [Package development workflow](CustomPackages.html) | Develop your package by supplying the required and recommended components. |
| [Export and sign your UPM package](cus-export.html) | Export and sign your package so you can share it with others. |
| [Share your package](cus-share.html) | Learn the different ways you can share your UPM package when it’s ready for consumption. |
## Additional resources
* [Package types](upm-package-types.html)
* [Create and export asset packages](AssetPackagesCreate.html)