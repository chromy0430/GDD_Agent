--- 
Source: Unity 6 Manual (webgl-gettingstarted.md)
---

# Web development and publishing process
Build and deploy a Web application in mobile and desktop environments.
Before you get started, check the [browser compatibility](webgl-browsercompatibility.html) and [technical limitations](webgl-technical-overview.html) for Web. Make sure you’re aware of any limitations for developing a project for this platform.
For a guided tutorial of the Web platform, refer to [Getting started with Unity Web](https://learn.unity.com/tutorial/getting-started-with-unity-web).
To build and deploy a Web application, complete the following tasks:
* [Add the Web module.](#add-module)
* [Set up a testing environment.](#test)
* [Profile and optimize.](#profile-optimize)
* [Host your build.](#host)
## Add the Web module
To get started with Web, [add the Web module](https://docs.unity3d.com/hub/manual/AddModules.html) to your project. Once you add the module, you can access the Web **Player** and **Build** settings.
## Set up a testing environment
To test your project, do either of the following:
* Use the **Build and Run** option in the Unity Editor’s [Build Profiles](build-profiles-reference.html)A set of customizable configuration settings to use when creating a build for your target platform. [More info](build-profiles.html)
  See in [Glossary](Glossary.html#buildprofile) window.
* Run your own web server.
If you run your own web server, Unity doesn’t need to rebuild the project for every test. Refer to [Server configuration code samples](webgl-server-configuration-code-samples.html) and [Deploy a web application](webgl-deploying.html) for information about running your own server.
## Profile and optimize
Before you publish, gather performance metrics and reduce the build size to make a project that runs smoothly with the best quality possible.
[Profile your Web build](web-profile.html) to get performance data and refer to [Optimize your Web build](web-optimization.html) and [Optimize Web platform for mobile](web-optimization-mobile.html).
## Host your build
You need to host projects online to make them accessible to users. Use web hosting services such as [Unity Play](https://play.unity.com/en) depending on your needs.
## Additional resources
* [Unity Learn tutorial: Getting started with Unity Web](https://learn.unity.com/tutorial/getting-started-with-unity-web)
* [Web Player settings](class-PlayerSettingsWebGL.html)
* [Web build settings](web-build-settings.html)
* [Memory in Web](webgl-memory.html)
* [Web graphics](webgl-graphics.html)