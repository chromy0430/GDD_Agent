--- 
Source: Unity 6 Manual (FrameDebugger-attach.md)
---

# Attach the Frame Debugger to a built project
You can change the Frame Debugger’s target process to attach the Frame Debugger to a built Unity Player. To be compatible with the Frame Debugger, the Unity Player must:
* Use the ****Development Build**A development build includes debug symbols and enables the Profiler. [More info](building-introduction.html)
  See in [Glossary](Glossary.html#developmentbuild)** [Build Setting](BuildSettings.html).
* Support multithreaded rendering. Every Unity platform except Web supports this.
* For desktop platforms, use the **Run In Background** [Player Setting](class-PlayerSettings.html). Otherwise, when you focus the Frame Debugger window in the Unity Editor, the Unity Player loses focus and doesn’t reflect any rendering changes.
If the Unity Player fulfills the above requirements, when you next [debug a frame](FrameDebugger-debug.html), you can attach the Frame Debugger to the Unity Player.