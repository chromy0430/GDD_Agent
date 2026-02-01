--- 
Source: Unity 6 URP Manual (render-graph-view.html)
---

# Analyze a render graph in URP
To analyze a render graph, use the **Render Graph Viewer** window.
The Render Graph Viewer window displays a render graph, which is the optimized sequence of render passes the Universal **Render Pipeline**A series of operations that take the contents of a Scene, and displays them on a screen. Unity lets you choose from pre-built render pipelines, or write your own. [More info](../render-pipelines.html)
See in [Glossary](../Glossary.html#renderpipeline) (URP) steps through each frame. The Render Graph Viewer displays both built-in render passes and any [custom render passes](renderer-features/intro-to-scriptable-render-passes.html) you create.
For more information about the **Render Graph Viewer** window, refer to [Render Graph Viewer window reference](render-graph-viewer-reference.html).
You can also use the following windows to analyze a render graph:
* [Rendering Debugger](features/rendering-debugger-reference.html#render-graph)
* [Frame Debugger](../FrameDebugger-debug.html#render-graph)
## Open the Render Graph Viewer window
Go to **Window** > **Analysis** > **Render Graph Viewer**.
The **Render Graph Viewer** window displays the render graph for the active **camera**A component which creates an image of a particular viewpoint in your scene. The output is either drawn to the screen or captured as a texture. [More info](../CamerasOverview.html)
See in [Glossary](../Glossary.html#Camera) by default. To select another camera, use the dropdown in the **toolbar**A row of buttons and basic controls at the top of the Unity Editor that allows you to interact with the Editor in various ways (e.g. scaling, translation). [More info](../Toolbar.html)
See in [Glossary](../Glossary.html#toolbar).
## View the render graph for a build
To connect the Render Graph Viewer window to a build, enable ****Development Build**A development build includes debug symbols and enables the Profiler. [More info](../building-introduction.html)
See in [Glossary](../Glossary.html#developmentbuild)** in the ****Build Profiles**A set of customizable configuration settings to use when creating a build for your target platform. [More info](../build-profiles.html)
See in [Glossary](../Glossary.html#buildprofile)** window when you build the project. If you build for **WebGL**A JavaScript API that renders 2D and 3D graphics in a web browser. The Unity Web build option allows Unity to publish content as JavaScript programs which use HTML5 technologies and the WebGL rendering API to run Unity content in a web browser. [More info](../webgl.html)
See in [Glossary](../Glossary.html#WebGL) or Universal Windows Platform (UWP), enable both **Development Build** and **Autoconnect Profiler**.
After you build your project, follow these steps:
1. Run your built project.
2. In the **Render Graph Viewer** window, select the **Target Selection** dropdown. The dropdown is set to **Editor** by default.
3. In the **Local** section, select your build.
Your build appears in the **Local** section only if the build is running.
## Example: Check how URP uses a resource
You can use the resource access blocks next to a resource name to check how the render passes use the resource.
![Render Graph Viewer example](../../uploads/urp/render-graph-viewer.png)
Render Graph Viewer example
In this example, the `_MainLightShadowmapTexture_` texture goes through the following stages:
1. During the first five render passes between **InitFrame** and **SetupCameraProperties**, the texture doesn’t exist. The resource access blocks are dotted lines.
2. The **Main Light Shadowmap** render pass creates the texture as a global texture, and has write-only access to it. The resource access block is red. For more information about global textures, refer to [Transfer textures between passes](render-graph-pass-textures-between-passes.html).
   The blue merge bar below **Main Light Shadowmap** means URP merged **Main Light Shadowmap**, **Additional Lights Shadowmap** and **SetupCameraProperties** into a single render pass.
3. The next five render passes don’t have access to the texture. The resource access blocks are gray.
4. The first **Draw Objects** render pass has read-only access to the texture. The resource access block is green.
5. The next two render passes don’t have access to the texture. The resource access blocks are gray.
6. The second **Draw Objects** render pass has read-only access to the texture. The resource access block is green.
7. Unity destroys the texture, because it’s no longer needed. The resource access blocks are blank.
## Check how URP optimized a render pass
To check the details of a render pass, for example to find out why it’s not a native render pass or a merged pass, do either of the following:
* Select the render pass name to display the details in the Pass List.
* Below the render pass name, hover your cursor over the gray, blue, or flashing blue resource access overview block.
For more information about displaying details of a render pass, refer to [Render Graph Viewer window reference](render-graph-viewer-reference.html).
## Additional resources
* [Render Graph settings in the Rendering Debugger window reference](features/rendering-debugger-reference.html#render-graph)
* [Debug a Render Graph frame in the Frame Debugger](../FrameDebugger-debug.html#render-graph).
* [Optimize a render graph](render-graph-optimize.html)
* [Understand performance](understand-performance.html)
* [Rendering in the Universal Render Pipeline](rendering-in-universalrp.html)