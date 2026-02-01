--- 
Source: Unity 6 Manual (xr-meta-quest-build-profile.md)
---

# Meta Quest build platform and build profile
Understand how to configure the Meta Quest build platform and build profile.
In Unity 6.1 and later, you can use the Meta Quest build platform and build profile in the [Build Profiles](build-profiles.html)A set of customizable configuration settings to use when creating a build for your target platform. [More info](build-profiles.html)
See in [Glossary](Glossary.html#buildprofile) window.
By default, the Meta Quest platform shares **Player settings**Settings that let you set various player-specific options for the final game built by Unity. [More info](class-PlayerSettings.html)
See in [Glossary](Glossary.html#PlayerSettings) with the [Android build platform](android-build-settings.html). You can use the Meta Quest build profile to override **project settings**A broad collection of settings which allow you to configure how Physics, Audio, Networking, Graphics, Input and many other areas of your project behave. [More info](comp-ManagerGroup.html)
See in [Glossary](Glossary.html#ProjectSettings) specifically for Meta Quest.
## Prerequisites
* [Android Build Support](android-install-dependencies.html) module for the version of the Editor you’re using.
## Select the Meta Quest build platform
You can use this build platform to configure settings for standalone Meta Quest headsets.
To select the Meta Quest build platform:
1. Go to **File** > **Build Profiles** to open the [Build Profiles](build-profiles-reference.html) window.
2. In the **Platforms** list, select **Meta Quest**.
3. Click the **Switch Platform** button.
**Note:** Unity automatically installs the [OpenXR Plugin](https://docs.unity3d.com/Packages/com.unity.xr.openxr@latest) when you select the Meta Quest build platform.
## Create the Meta Quest build profile
To create a Meta Quest build profile:
1. Open the **Build Profiles** window (**File** > **Build Profiles**), and select **Add Build Profile** to open the **Platform Browser** window.
2. Select **Meta Quest** from the list of supported platforms.
3. Optionally, [Choose packages from the platform browser](#choose-packages) to install in your project.
4. Select **Add Build Profile**.
Unity creates a Meta Quest build profile and installs any required or requested packages.
### Choose packages from the platform browser
When you add the Meta Quest build profile, you can select packages for Meta Quest development that Unity installs when you create the build profile.
**Note:** The [OpenXR](https://docs.unity3d.com/Packages/com.unity.xr.openxr@latest) **plug-in**A set of code created outside of Unity that creates functionality in Unity. There are two kinds of plug-ins you can use in Unity: Managed plug-ins (managed .NET assemblies created with tools like Visual Studio) and Native plug-ins (platform-specific native code libraries). [More info](./plug-ins.html)
See in [Glossary](Glossary.html#plug-in) is a required package for the Meta Quest build profile, and is automatically installed when you create the build profile.
Optionally, you can install Meta’s packages for Meta Quest development from the **Partner Packages** section of the [Platform Browser](platform-browser-reference.html) window. To learn which Meta packages you can install with the **Platform Browser**, refer to [Meta packages](xr-meta-quest-packages.html#meta-packages).
To install partner packages:
1. Select the packages you want to install from the **Partner Packages** section.
2. Select **Add Build Profile** to [Add the build profile](#add-build-profile) and install selected packages.
Unity installs the packages you have selected, and you can access them from the [Package Manager](upm-ui.html).
## Default settings reference
When you create a Meta Quest build profile, Unity pre-configures some specific [Player](class-PlayerSettingsAndroid.html) and [Quality](class-QualitySettings.html) settings.
To access Player settings, click the **Player Settings** button at the top of the **Meta Quest Build Profile** page. The following table outlines the default overridden **Player settings** for the Meta Quest build profile:
| **Setting** | **Default value** |
| --- | --- |
| [Graphics API](class-PlayerSettingsAndroid.html#Rendering) | **Vulkan** |
| [Minimal Android API Level](class-PlayerSettingsAndroid.html#Identification) | **Android 10.0 (API level 29)** |
| [Target API level](class-PlayerSettingsAndroid.html#Identification) | **Android 12L (API level 32)** |
| [Scripting Backend](class-PlayerSettingsAndroid.html#Configuration)A framework that powers scripting in Unity. Unity supports three different scripting backends depending on target platform: Mono, .NET and IL2CPP. Universal Windows Platform, however, supports only two: .NET and IL2CPP. [More info](scripting-backends.html) See in [Glossary](Glossary.html#ScriptingBackend) | **IL2CPP** |
| [Target Architecture](class-PlayerSettingsAndroid.html#Configuration) | **ARM64** |
| **Stereo **Rendering Path**The technique that a render pipeline uses to render graphics. Choosing a different rendering path affects how lighting and shading are calculated. Some rendering paths are more suited to different platforms and hardware than others. [More info](RenderingPaths.html) See in [Glossary](Glossary.html#renderingpath)** | **Instancing** |
To access quality settings, click the **Player Settings** button at the top of the **Meta Quest Build Profile** page and select **Quality** from the left-hand menu. The following table outlines the default overridden **Quality Settings** for the Meta Quest build profile:
| **Setting** | **Default value** |
| --- | --- |
| [Anisotropic Filtering](class-QualitySettings.html#anisotropic-textures-dropdown) | **Forced On** |
| [Quality Level](class-QualitySettings.html) | A new **Meta Quest (Build Profile)** option |
## Customize build profile settings
In the **Meta Quest Build Profile** tab, you can configure the following settings derived from the Meta Quest build target:
* **Platform Settings**: customizable build settings specific for the Meta Quest platform. These settings aren’t shared by the Android build target.
* **Player Settings**, **Graphics Settings**, and **Quality Settings**: shared with the Android build target by default. You can customize and override these settings for the Meta Quest platform. To override these settings, select the relevant override option from the **Player Settings Overrides** section to reveal the override options.
## Meta Quest platform settings
The Meta Quest platform is derived from the Android build platform and shares most of its settings with the Android platform. To learn about the settings available in the Android build platform, refer to [Android build settings reference](android-build-settings.html).
The following table describes settings that are specific to the Meta Quest platform:
| **Setting** | **Description** |
| --- | --- |
| **Link Time Optimization** | Use the precompiled and link time optimized (ThinLTO) Unity engine code (`libunity.so`) for non-development builds. Use this property for improved runtime performance and reduced memory usage. The options are:  * **None**: The project build uses the default Unity engine code. * **Thin**: The project build uses precompiled and thin link time optimized (ThinLTO) Unity engine code. For more information, refer to the [ThinLTO Documentation](https://clang.llvm.org/docs/ThinLTO.html).  **Note:** You can use link time optimized Unity engine code if your project uses IL2CPP scripting backend and [Strip Engine Code](class-PlayerSettingsAndroid.html#Optimization) is disabled. This doesn’t affect [IL2CPP](class-PlayerSettingsAndroid.html#Configuration)A Unity-developed scripting back-end which you can use as an alternative to Mono when building projects for some platforms. [More info](./scripting-backends-il2cpp.html) See in [Glossary](Glossary.html#IL2CPP) compilation. |
## Additional resources
* [Android build settings reference](android-build-settings.html)
* [Introduction to build profiles](build-profiles.html)