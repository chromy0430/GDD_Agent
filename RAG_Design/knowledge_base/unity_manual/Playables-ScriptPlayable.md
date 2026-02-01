--- 
Source: Unity 6 Manual (Playables-ScriptPlayable.md)
---

# ScriptPlayable and PlayableBehaviour
Use the `ScriptPlayable<>` object and the `PlayableBehaviour` custom behavior to create custom playables.
To create your own custom playable, inherit from the `PlayableBehaviour` base class:
```
public class MyCustomPlayableBehaviour : PlayableBehaviour
{
    // Implementation of the custom playable behaviour
    // Override PlayableBehaviour methods as needed
}
```
To use a `PlayableBehaviour` as a custom playable, you must wrap it within a `ScriptPlayable<>` object. If you don’t have an instance of your custom playable, use the following code to create a `ScriptPlayable`:
```
ScriptPlayable<MyCustomPlayableBehaviour>.Create(playableGraph);
```
If you have an instance of your custom playable, use the following code to wrap the instance in a `ScriptPlayable<>` object:
```
MyCustomPlayableBehaviour myPlayable = new MyCustomPlayableBehaviour();
ScriptPlayable<MyCustomPlayableBehaviour>.Create(playableGraph, myPlayable);
```
This clones the instance and assigns the clone to the `ScriptPlayable` object. In this example, use the `myPlayable` public property in the **Inspector**A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](UsingTheInspector.html)
See in [Glossary](Glossary.html#Inspector) window to configure a different behaviour for each instance of your script.
To retrieve the PlayableBehaviour object from the ScriptPlayable object, use the `ScriptPlayable<T> .GetBehaviour()` method.
## Additional resources
* [Create a custom playable](playables-ex-custom-playable.html)
* [PlayableBehaviour base class](../ScriptReference/Playables.PlayableBehaviour.html)
* [ScriptPlayable struct](../ScriptReference/Playables.ScriptPlayable_1.html)