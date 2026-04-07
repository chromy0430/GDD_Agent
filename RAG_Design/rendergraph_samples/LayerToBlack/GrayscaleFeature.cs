using System.Collections.Generic;
using UnityEngine;
using UnityEngine.Rendering;
using UnityEngine.Rendering.RenderGraphModule;
using UnityEngine.Rendering.Universal;

public class BlackLayerRenderFeature : ScriptableRendererFeature
{
    [Tooltip("검은색으로 렌더링할 대상 레이어를 선택하십시오.")]
    public LayerMask targetLayer;

    [Tooltip("검은색을 출력하는 오버라이드 머티리얼 (BlackOverride.shader 사용 권장)")]
    public Material blackOverrideMaterial;

    private BlackLayerPass m_BlackLayerPass;

    public override void Create()
    {
        m_BlackLayerPass = new BlackLayerPass(targetLayer, blackOverrideMaterial);

        // 투명/불투명 객체 렌더링 이후에 덮어쓰기 위해 Opaque 직후로 설정합니다.
        m_BlackLayerPass.renderPassEvent = RenderPassEvent.AfterRenderingOpaques;
    }

    public override void AddRenderPasses(ScriptableRenderer renderer, ref RenderingData renderingData)
    {
        if (blackOverrideMaterial == null)
        {
            Debug.LogWarning("[BlackLayerRenderFeature] Black Override Material이 할당되지 않아 Pass를 건너뜁니다.");
            return;
        }

        renderer.EnqueuePass(m_BlackLayerPass);
    }

    protected override void Dispose(bool disposing)
    {
        m_BlackLayerPass = null;
    }

    private class BlackLayerPass : ScriptableRenderPass
    {
        private LayerMask m_LayerMask;
        private Material m_OverrideMaterial;

        // Zero-GC 원칙을 위한 정적 캐싱 배열 및 리스트 할당
        private static readonly ShaderTagId[] s_ForwardShaderTags = new ShaderTagId[]
        {
            new ShaderTagId("UniversalForwardOnly"),
            new ShaderTagId("UniversalForward"),
            new ShaderTagId("SRPDefaultUnlit"),
            new ShaderTagId("LightweightForward")
        };

        private List<ShaderTagId> m_ShaderTagIdList = new List<ShaderTagId>();

        public BlackLayerPass(LayerMask layerMask, Material overrideMaterial)
        {
            m_LayerMask = layerMask;
            m_OverrideMaterial = overrideMaterial;

            // List 인스턴스는 생성 시 단 1회만 할당하여 가비지 컬렉션을 방지합니다.
            foreach (ShaderTagId sid in s_ForwardShaderTags)
            {
                m_ShaderTagIdList.Add(sid);
            }
        }

        // RenderGraph 람다 내부에서 사용할 데이터를 담는 구조체
        private class PassData
        {
            public RendererListHandle rendererListHandle;
        }

        public override void RecordRenderGraph(RenderGraph renderGraph, ContextContainer frameData)
        {
            string passName = "Black Layer Override Pass";

            using (var builder = renderGraph.AddRasterRenderPass<PassData>(passName, out var passData, profilingSampler))
            {
                UniversalResourceData resourceData = frameData.Get<UniversalResourceData>();

                // RendererList 생성을 위한 데이터 주입
                SetupPassData(ref passData, frameData, renderGraph);

                if (!passData.rendererListHandle.IsValid())
                    return;

                // RenderGraph에게 해당 RendererList를 사용함을 알림
                builder.UseRendererList(passData.rendererListHandle);

                // 컬러 및 뎁스 어태치먼트 설정 (현재 화면의 버퍼를 타겟으로 지정)
                builder.SetRenderAttachment(resourceData.activeColorTexture, 0);
                builder.SetRenderAttachmentDepth(resourceData.activeDepthTexture, AccessFlags.Write);

                builder.SetRenderFunc(static (PassData data, RasterGraphContext context) => ExecutePass(data, context));
            }
        }

        // 구조체를 ref로 전달하여 메모리 복사를 방지하고 성능을 최적화합니다.
        private void SetupPassData(ref PassData passData, ContextContainer frameData, RenderGraph renderGraph)
        {
            UniversalRenderingData universalRenderingData = frameData.Get<UniversalRenderingData>();
            UniversalCameraData cameraData = frameData.Get<UniversalCameraData>();
            UniversalLightData lightData = frameData.Get<UniversalLightData>();

            var sortFlags = cameraData.defaultOpaqueSortFlags;

            // 모든 큐(Opaque, Transparent 등)를 대상으로 삼되 LayerMask로 필터링합니다.
            RenderQueueRange renderQueueRange = RenderQueueRange.all;
            FilteringSettings filterSettings = new FilteringSettings(renderQueueRange, m_LayerMask);

            // 기본 렌더링 세팅 생성
            DrawingSettings drawSettings = RenderingUtils.CreateDrawingSettings(
                m_ShaderTagIdList,
                universalRenderingData,
                cameraData,
                lightData,
                sortFlags
            );

            // 중요: 지정된 오브젝트들을 렌더링할 때 무조건 할당된 검은색 머티리얼을 사용하도록 덮어씁니다.
            drawSettings.overrideMaterial = m_OverrideMaterial;
            drawSettings.overrideMaterialPassIndex = 0;

            // RendererList 파라미터 조합 및 핸들 생성
            RendererListParams param = new RendererListParams(universalRenderingData.cullResults, drawSettings, filterSettings);
            passData.rendererListHandle = renderGraph.CreateRendererList(param);
        }

        static void ExecutePass(PassData data, RasterGraphContext context)
        {
            // 준비된 작업 지시서(RendererList)를 기반으로 그리기 명령을 실행합니다.
            context.cmd.DrawRendererList(data.rendererListHandle);
        }
    }
}