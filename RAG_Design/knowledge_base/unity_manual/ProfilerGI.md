--- 
Source: Unity 6 Manual (ProfilerGI.md)
---

# Global Illumination Profiler module reference
The **Global Illumination**A group of techniques that model both direct and indirect lighting to provide realistic lighting results.
See in [Glossary](Glossary.html#globalillumination) Profiler module displays statistics about how much CPU time the [Enlighten Realtime Global Illumination](realtime-gi-using-enlighten.html) subsystem uses across all worker threads. To control the number of **Enlighten**A lighting system by Geomerics used in Unity for Enlighten Realtime Global Illumination. [More info](https://www.siliconstudio.co.jp/en/products-service/enlighten/)
See in [Glossary](Glossary.html#Enlighten) worker threads included, you can pass the Unity Editor a [command line argument](EditorCommandLineArguments.html).
To open the Profiler window, go to menu: **Window** > **Analysis** > **Profiler**.
![Global Illumination Profiler module](../uploads/Main/gi-chart.png)
Global Illumination Profiler module
## Chart categories
The Global Illumination Profiler module’s chart tracks the time the global illumination subsystem spent on all worker threads. The timings are divided into the following categories:
| **Chart** | **Description** |
| --- | --- |
| **Light Probe** | The time spent updating [Light Probes](LightProbes.html)Light probes store information about how light passes through space in your scene. A collection of light probes arranged within a given space can improve lighting on moving objects and static LOD scenery within that space. [More info](LightProbes.html) See in [Glossary](Glossary.html#LightProbe). |
| **Setup** | The time spent in the setup stage. |
| **Environment** | The time spent processing environment lighting. |
| **Input Lighting** | The time spent processing input lighting. |
| **Systems** | The time spent updating systems. |
| **Solve Tasks** | The time spent running [radiosity solver tasks](class-MeshRenderer.html). |
| **Dynamic Objects** | Time spent updating dynamic **GameObjects**The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](class-GameObject.html) See in [Glossary](Glossary.html#GameObject). |
| **Other Commands** | Time spent updating other commands. |
| **Blocked Command Write** | Time spent in a blocked state, waiting for the command buffer. |
To change the order of the categories in the chart, you can drag and drop them in the chart’s legend. You can also click a category’s colored legend to toggle its display.
## Module details pane
When you select the Global Illumination module, the details pane displays a breakdown of where the application spent time in the selected frame. The data available is as follows:
| **Data** | **Description** |
| --- | --- |
| **Total CPU Time** | Total Enlighten Global Illumination CPU time across all threads in ms. |
| **Probe Update Time** | Time spent updating light probes in ms. |
| **Setup Time** | Time spent in the setup stage in ms. |
| **Environment Time** | Time spent processing environment lighting in ms. |
| **Input Lighting Time** | Time spent processing input lighting in ms. |
| **Systems Time** | Time spent updating systems in ms. |
| **Solve Tasks Time** | Time spent running radiosity solver tasks in ms. |
| **Dynamic Objects Time** | Time spent updating dynamic GameObjects in ms. |
| **Time Between Updates** | Time between Global Illumination updates in ms. |
| **Other Commands Time** | Time spent processing other commands in ms. |
| **Blocked Command Write Time** | Time spent in blocked state, waiting for command buffer in ms. |
| **Blocked Buffer Writes** | Number of writes to the command buffer that were blocking. |
| **Total Light Probes** | Total number of Light Probes in the **scene**A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](CreatingScenes.html) See in [Glossary](Glossary.html#Scene). |
| **Solved Light Probes** | Number of solved Light Probes since the last update. |
| **Probe Sets** | Number of Light Probe sets in the scene. |
| **Systems** | Number of Enlighten Global Illumination systems in the scene. |
| **Pending Material GPU Renders** | Number of Albedo/Emission renders queued for rendering on the GPU. |
| **Pending Material Updates** | Number of material updates waiting to get processed. |
## Additional resources
* [Profiler window introduction](ProfilerWindow.html)
* [Profiling your application](profiler-profiling-applications.html)