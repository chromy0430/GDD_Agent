Shader "Hidden/BlackOverride"
{
    SubShader
    {
        Tags 
        { 
            "RenderType"="Opaque" 
            "RenderPipeline"="UniversalPipeline"
            "Queue"="Geometry"
        }

        // Z-Fighting 방지 및 화면 위에 확실히 덮어씌우기 위한 기본 설정
        ZWrite On
        ZTest LEqual
        Cull Back

        Pass
        {
            Name "BlackOverridePass"

            HLSLPROGRAM
            #pragma vertex vert
            #pragma fragment frag

            #include "Packages/com.unity.render-pipelines.universal/ShaderLibrary/Core.hlsl"

            struct Attributes
            {
                float4 positionOS : POSITION;
                UNITY_VERTEX_INPUT_INSTANCE_ID
            };

            struct Varyings
            {
                float4 positionCS : SV_POSITION;
                UNITY_VERTEX_OUTPUT_STEREO
            };

            Varyings vert(Attributes input)
            {
                Varyings output;
                UNITY_SETUP_INSTANCE_ID(input);
                UNITY_INITIALIZE_VERTEX_OUTPUT_STEREO(output);

                // 오브젝트 공간의 정점을 화면 클립 공간으로 변환합니다.
                output.positionCS = TransformObjectToHClip(input.positionOS.xyz);
                return output;
            }

            half4 frag(Varyings input) : SV_Target0
            {
                // 완전한 검은색(불투명)을 반환합니다. 빛 연산은 일체 생략됩니다.
                return half4(0.0, 0.0, 0.0, 1.0);
            }
            ENDHLSL
        }
    }
}