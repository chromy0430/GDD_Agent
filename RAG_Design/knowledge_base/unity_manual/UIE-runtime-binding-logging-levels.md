--- 
Source: Unity 6 Manual (UIE-runtime-binding-logging-levels.md)
---

# Define logging levels
During the update of the binding, errors might occur where binding objects try to access invalid properties, encounter `null` values along a property path, or encounter missing type converters. If you set the binding system to log all errors to the Console, it can impact performance.
To control the console output, you can define logging levels for the binding system. The following are the available logging levels:
* **All logs**: Errors are consistently logged to the console.
* **One log per result**: Errors are logged to the console only the first time they occur.
* **No logs**: Error logging is disabled.
## In Unity Editor windows
You can set logging levels from the More (⋮) menu in a Unity Editor window that supports data binding, such as UI Builder, **Scene**A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](CreatingScenes.html)
See in [Glossary](Glossary.html#Scene) view, Game view, and the PanelSettings’s **Inspector**A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](UsingTheInspector.html)
See in [Glossary](Glossary.html#Inspector) windows.
To set logging levels:
1. Open the More (⋮) menu in the Unity Editor window.
2. Select **Binding Console Logs**.
3. Choose one of the logging levels from the list.
**Note:**:
* The default logging level in UI Builder is set to **No logs**.
* Each panel maintains independent logging level settings. PanelSettings assets and views (Scene, Game) operate on separate panels with their own logging configurations.
## In C# scripts
You can set the global and per-panel configurations to customize logging behavior in C# **scripts**A piece of code that allows you to create your own Components, trigger game events, modify Component properties over time and respond to user input in any way you like. [More info](creating-scripts.html)
See in [Glossary](Glossary.html#Scripts).
The following example sets the global log level of all panels or windows.
```
Binding.SetGlobalLogLevel(BindingLogLevel.Once);
```
The following example sets the log level per panel:
```
Binding.SetPanelLogLevel(myElement.panel, BindingLogLevel.None);
```
**Note:** The per-panel or the per-window logging level settings override the global logging level settings.
## Troubleshooting
When debugging binding issues, verify that Unity’s property system can access your object’s properties. The binding system relies on `Unity.Properties` to detect and access bindable properties. If properties aren’t properly exposed or serialized, bindings might fail silently.
## Additional resources
* [Runtime data binding](UIE-runtime-binding.html)
* [Create runtime data binding](UIE-runtime-binding-types.html)
* [Define a data source](UIE-runtime-binding-define-data-source.html)
* [Define binding modes and update triggers](UIE-runtime-binding-mode-update.html)
* [Convert data types](UIE-runtime-binding-data-type-conversion.html)