--- 
Source: Unity 6 Manual (renderer-shader-user-value.md)
---

# Renderer Shader User Value (RSUV)
In certain scenarios, games need to manage a large number of objects (e.g., MeshRenderers) while applying unique visual customization to each instance. Prior to the introduction of the Scriptable **Render Pipeline**A series of operations that take the contents of a Scene, and displays them on a screen. Unity lets you choose from pre-built render pipelines, or write your own. [More info](render-pipelines.html)
See in [Glossary](Glossary.html#renderpipeline) (SRP), the most efficient method for achieving this was through the use of Material Property Blocks (MPBs).
With the advent of the SRP Batcher, a more performant approach has been to generate a dedicated Material for each customized renderer. This method has demonstrated significantly better runtime performance compared to MPBs.
Nevertheless, in many cases the required customization per object is limited to only a small set of parameters. While duplicating the entire Material for each object is a nice and simple solution, you can now use a more focused and efficient alternative: the Renderer User **Shader**A program that runs on the GPU. [More info](Shaders.html)
See in [Glossary](Glossary.html#shader) Value (RSUV).
**Note**: RSUV is only available with Scriptable Render Pipelines (SRP). It is not supported in Unity’s Built-in Renderer Pipeline (BiRP).
## Principle
RSUV is accessible via the MeshRenderer and SkinnedMeshRenderer APIs:
* [`MeshRenderer.SetShaderUserValue(uint value)`](../ScriptReference/MeshRenderer.SetShaderUserValue.html)
* [`SkinnedMeshRenderer.SetShaderUserValue(uint value)`](../ScriptReference/SkinnedMeshRenderer.SetShaderUserValue.html)
This API enables the assignment of a custom 32-bit unsigned integer value to each renderer. The value is accessible within shader HLSL code through the `unity_RendererUserValue` property. Importantly, this functionality introduces **no additional CPU overhead and does not interfere with batching.**
The primary advantage of this approach is that all customized renderers continue to share a single Material. As a result, in most scenarios it yields a notable performance improvement (see the Performance section below).
**Note**: From the shader side, you can easily access the RSUV within Shader Graph through a [**Custom Function** node](https://docs.unity3d.com/Packages/com.unity.shadergraph@latest/index.html?subfolder=/manual/Custom-Function-Node.html).
## Use cases
The RSUV can be applied flexibly in a variety of scenarios. For example:
| **Visual customization requirement** | **Recommended method with RSUV** |
| --- | --- |
| Different diffuse colors per object | Encode an RGBA32 color directly into the RSUV and decode it in shader code. |
| Different shirt logo textures per character | For example, with 16 available logos, allocate 4 bits of RSUV to encode the UV index across a single texture atlas containing all logos. You can use the remaining 28 bits to encode additional variations, such as color adjustments. |
| Large amounts of custom data per renderer | Use the RSUV as an index into a larger data structure stored in a global GraphicsBuffer. |
**Note**: RSUV usage and encoding are shader-specific. For instance, one shader might interpret the RSUV as a color, while another may treat it as an index into auxiliary data.
## Performance
The RSUV feature introduces no additional CPU overhead. Using RSUV to customize values per renderer is always slightly faster than duplicating a material and way faster than using Material Property Block (MPB).
The performance gain is maximum when using GPU Resident Drawer (GRD) as you no longer need to duplicate materials and break GRD instancing draw calls.
## Set and use the RSUV
### Set the value
The following example sets a random color to all MeshRenderer of the **scene**A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](CreatingScenes.html)
See in [Glossary](Glossary.html#Scene), encoded as 24bits integer:
```
        MeshRenderer[] allMeshRenderers = FindObjectsByType<MeshRenderer>(FindObjectsSortMode.InstanceID);
        foreach (MeshRenderer meshRenderer in allMeshRenderers)
        {
            // compute a random color
            Color32 c = Color.HSVToRGB(UnityEngine.Random.Range(0f, 1f), UnityEngine.Random.Range(0.6f, 1.0f), UnityEngine.Random.Range(0.6f, 1.0f));
            // set it as a LDR color in the RSUV value of the renderer
            uint cc = ((uint)c.b << 16) | ((uint)c.g << 8) | ((uint)c.r << 0);
            meshRenderer.SetShaderUserValue(cc);
        }
```
### Use the value in the shader
In the shader code, you can decode the 24bits value as a float4 color. For example:
```
uint c = unity_RendererUserValue;
float4 mycolor = float4((float)((c >> 0) & 255) * (1.f / 255.f),
                        (float)((c >> 8) & 255) * (1.f / 255.f),
                        (float)((c >> 16) & 255) * (1.f / 255.f),
                        (float)1.f);
```
To retrieve the RSUV in [Shader Graph](https://docs.unity3d.com/Packages/com.unity.shadergraph@latest), you have to use a [**Custom Function** node](https://docs.unity3d.com/Packages/com.unity.shadergraph@latest/index.html?subfolder=/manual/Custom-Function-Node.html). For example:
1. In the Graph **Inspector**A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](UsingTheInspector.html)
   See in [Glossary](Glossary.html#Inspector), in the Custom Function node properties:
2. Add an **Output** of type **Vector 4** and call it **mycolor**.
3. Set the **Type** to **String**.
4. Set the **Name** to **getMyColor**.
5. In the **Body** field, paste the code previously provided in this section.
6. In the Shader Graph’s workspace, connect the Custom Function node’s **mycolor** output to the Fragment’s **Base Color** input.
### Use RSUV with Entities Graphics
You can also use the RSUV feature along with Unity’s [Entities Graphics package](https://docs.unity3d.com/Packages/com.unity.entities.graphics@latest).
The following code example assigns a distinct RSUV value to all entities that include a MaterialMeshInfo component.
```
using Unity.Entities;
using UnityEngine;
using Unity.Rendering;
using Unity.Burst;
[MaterialProperty("unity_RendererUserValuesPropertyEntry")]
public struct RendererUserValue_BaseValue : IComponentData
{
    public uint Value;
}
[BurstCompile]
public partial struct MaterialMeshInfoDebugSystem : ISystem
{
    private bool m_done;
    public void OnCreate(ref SystemState state)
    {
        m_done = false;
    }
    public void OnUpdate(ref SystemState state)
    {
        if ( !m_done )
        {
            var entityManager = state.EntityManager;
            var mQuery = entityManager.CreateEntityQuery(ComponentType.ReadOnly<MaterialMeshInfo>());
            // subscene may not be fully loaded, so wait for some entities to be here
            if (!mQuery.IsEmpty)
            {
                using (var entities = mQuery.ToEntityArray(Unity.Collections.Allocator.Temp))
                {
                    foreach (var entity in entities)
                    {
                        Color32 c = Color.HSVToRGB(UnityEngine.Random.Range(0f, 1f), UnityEngine.Random.Range(0.6f, 1.0f), UnityEngine.Random.Range(0.6f, 1.0f));
                        uint cc = ((uint)255<<24) | ((uint)c.b << 16) | ((uint)c.g << 8) | ((uint)c.r << 0);
                        entityManager.AddComponentData(entity, new RendererUserValue_BaseValue { Value = cc });
                    }
                }
                m_done = true;
            }
        }
    }
}
```