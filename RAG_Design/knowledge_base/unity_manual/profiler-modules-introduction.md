--- 
Source: Unity 6 Manual (profiler-modules-introduction.md)
---

# Profiler modules introduction
Collect specific performance data about your application with Profiler modules.
The top area of the [Profiler window](ProfilerWindow.html) contains Profiler modules that profile specific areas of your application. When you profile your application, Unity displays the data related to each module in corresponding charts.
![Profiler window with a frame in the CPU Usage Profiler module selected. The Timeline view is selected in the details pane.](../uploads/Main/profiler-cpu-module.png)
Profiler window with a frame in the CPU Usage Profiler module selected. The Timeline view is selected in the details pane.
## Module types
The [CPU Usage module](ProfilerCPU.html) provides an overview of how much time your application spends on each frame. The other modules collect data which you can use to inspect specific areas or to monitor the vitals of your application, such as memory consumption, rendering, or audio statistics.
Each module has its own chart. When you select a module, the details panel in the bottom section of the Profiler window displays detailed data that the module collects. You can then use this data to identify areas of improvement in your application.
For a full list of available Profiler modules refer to the [Profiler window reference](ProfilerWindow.html).
## Custom Profiler modules
You can add your own Profiler modules to the Profiler window to capture and visualize specific performance data in your application. You can either use the [Profiler Module Editor](profiler-module-editor.html) or use **scripts**A piece of code that allows you to create your own Components, trigger game events, modify Component properties over time and respond to user input in any way you like. [More info](creating-scripts.html)
See in [Glossary](Glossary.html#Scripts) to automatically create and populate modules.
The following image of a customized Profiler window contains:
* **A**: A [custom Profiler module](profiler-creating-custom-modules.html) named **Tank Effects**.
* **B**: A [custom module details panel](profiler-customizing-details-view.html) that visualizes the data in the Tank Effects profiler module.
* **C**: [Custom Profiler counters](profiler-adding-information-code-intro.html) which track **particle**A small, simple image or mesh that is emitted by a particle system. A particle system can display and move particles in great numbers to represent a fluid or amorphous entity. The effect of all the particles together creates the impression of the complete entity, such as smoke. [More info](class-ParticleSystem.html)
  See in [Glossary](Glossary.html#particle) data.
![A custom Profiler module with custom game data displayed](../uploads/Main/Profiler_Tank_details.png)
A custom Profiler module with custom game data displayed
For more information, refer to [Customizing Profiler modules](profiler-customizing.html).
## Additional resources
* [Using the Profiler window](ProfilerWindow.html)
* [Profiling your application](profiler-profiling-applications.html)
* [Profiler window reference](ProfilerWindow.html)
* [Customizing Profiler modules](profiler-customizing.html)