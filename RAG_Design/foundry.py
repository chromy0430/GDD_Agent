import re
import json
from typing import Any, Dict, List, Optional


class FoundryGuard:
    """
    Governance / Validation Layer
    - JSON 추출 및 복구
    - 코드 안전성 검사
    - Plan schema / semantics 검사
    - Agent output schema 검사
    """

    def __init__(self):
        self.banned_imports = ["os", "sys", "subprocess", "shutil", "eval", "exec"]
        self.allowed_agents = {
            "Market_Analyst",
            "Video_Analyst",
            "Reference_Finder",
            "Game_Designer",
            "GDD_Writer",
            "Spec_Generator",
            "Balance_Calc",
            "Graphics_Expert",
            "Code_Reviewer",
            "RenderGraph_Expert",  # 추가됨
            "Game_Planner",        # 추가됨
            "Feature_Implementer"  # 추가됨 (기존 orchestrator에는 있었으나 여기서 누락되어 있었음)
        }

    # =========================================================
    # 1. 기본 JSON 추출
    # =========================================================
    def extract_json_object(self, text: str) -> Dict[str, Any]:
        """
        응답에서 JSON 객체 하나를 최대한 안전하게 추출
        """
        if not text or not isinstance(text, str):
            return {"valid": False, "error": "Empty text", "raw": text}

        # fenced json
        fenced = re.search(r"```json\s*(\{.*?\})\s*```", text, re.DOTALL)
        if fenced:
            try:
                data = json.loads(fenced.group(1))
                return {"valid": True, "data": data}
            except Exception as e:
                return {"valid": False, "error": str(e), "raw": text}

        # raw JSON object
        try:
            decoder = json.JSONDecoder()
            stripped = text.strip()
            obj, _ = decoder.raw_decode(stripped)
            return {"valid": True, "data": obj}
        except Exception:
            pass

        # fallback: first { ... }
        raw = re.search(r"(\{.*\})", text, re.DOTALL)
        if raw:
            try:
                decoder = json.JSONDecoder()
                obj, _ = decoder.raw_decode(raw.group(1))
                return {"valid": True, "data": obj}
            except Exception as e:
                return {"valid": False, "error": str(e), "raw": text}

        return {"valid": False, "error": "No JSON object found", "raw": text}

    def validate_json_structure(self, text: str) -> Dict[str, Any]:
        """
        하위 호환용
        """
        return self.extract_json_object(text)

    # =========================================================
    # 2. 코드 안전성 검사
    # =========================================================
    def validate_code_safety(self, code_text: str) -> dict:
        validation_result = {"is_safe": True, "warnings": []}

        if not code_text:
            return validation_result

        for lib in self.banned_imports:
            pattern = re.compile(fr"^\s*(import|from)\s+{lib}\b", re.MULTILINE)
            if pattern.search(code_text):
                validation_result["is_safe"] = False
                validation_result["warnings"].append(
                    f"Security Violation: '{lib}' module usage is restricted."
                )

        dangerous_keywords = ["remove", "rmtree", "system(", "popen"]
        for kw in dangerous_keywords:
            if kw in code_text:
                validation_result["warnings"].append(
                    f"Potential Risk: '{kw}' keyword detected. Review required."
                )

        return validation_result

    # =========================================================
    # 3. Plan 검증
    # =========================================================
    def validate_plan_schema(
        self,
        plan: Dict[str, Any],
        attachment_type: Optional[str] = None,
    ) -> Dict[str, Any]:
        """
        planner가 만든 JSON의 구조/의미 검증
        """
        errors: List[str] = []
        warnings: List[str] = []

        if not isinstance(plan, dict):
            return {"valid": False, "errors": ["Plan is not a dict"], "warnings": warnings}

        required_top = ["intent", "thought", "steps", "final_output"]
        for key in required_top:
            if key not in plan:
                errors.append(f"Missing top-level key: {key}")

        steps = plan.get("steps", [])
        if not isinstance(steps, list) or len(steps) == 0:
            errors.append("Plan must contain at least one step")
            return {"valid": False, "errors": errors, "warnings": warnings}

        if len(steps) > 5:
            warnings.append("Too many steps; truncation may be needed")

        step_ids = set()

        for idx, step in enumerate(steps):
            if not isinstance(step, dict):
                errors.append(f"Step {idx+1} is not an object")
                continue

            for key in ["id", "agent", "instruction", "input_mode", "expected_output", "use_attachment"]:
                if key not in step:
                    errors.append(f"Step {idx+1} missing key: {key}")

            step_id = str(step.get("id", "")).strip()
            agent = str(step.get("agent", "")).strip()
            instruction = str(step.get("instruction", "")).strip()
            input_mode = str(step.get("input_mode", "")).strip()
            expected_output = str(step.get("expected_output", "")).strip()

            if not step_id:
                errors.append(f"Step {idx+1} has empty id")
            elif step_id in step_ids:
                errors.append(f"Duplicate step id: {step_id}")
            else:
                step_ids.add(step_id)

            if agent not in self.allowed_agents:
                errors.append(f"Step {idx+1} uses unknown agent: {agent}")

            if not instruction:
                errors.append(f"Step {idx+1} has empty instruction")

            if input_mode not in {"text", "document", "video", "code", "mixed"}:
                errors.append(f"Step {idx+1} has invalid input_mode: {input_mode}")

            if not expected_output:
                errors.append(f"Step {idx+1} has empty expected_output")

            depends_on = step.get("depends_on", [])
            if depends_on is None:
                depends_on = []
            if not isinstance(depends_on, list):
                errors.append(f"Step {idx+1} depends_on must be a list")

            # 첨부 적합성 간단 검사
            if attachment_type == "video" and agent == "Video_Analyst" and input_mode not in {"video", "mixed"}:
                warnings.append(f"Step {idx+1}: Video_Analyst usually expects video/mixed input")

            if attachment_type == "code" and agent == "Code_Reviewer" and input_mode not in {"code", "mixed"}:
                warnings.append(f"Step {idx+1}: Code_Reviewer usually expects code/mixed input")

        # depends_on 대상 존재 확인
        valid_ids = {str(step.get("id", "")).strip() for step in steps if isinstance(step, dict)}
        for idx, step in enumerate(steps):
            if not isinstance(step, dict):
                continue
            for dep in step.get("depends_on", []) or []:
                if dep not in valid_ids:
                    errors.append(f"Step {idx+1} depends on unknown step id: {dep}")

        return {"valid": len(errors) == 0, "errors": errors, "warnings": warnings}

    # =========================================================
    # 4. Agent 결과 검증
    # =========================================================
    def validate_agent_output(self, data: Dict[str, Any]) -> Dict[str, Any]:
        errors: List[str] = []

        if not isinstance(data, dict):
            return {"valid": False, "errors": ["Agent output is not a dict"]}

        required = ["summary", "key_findings", "deliverable", "next_step_hint"]
        for key in required:
            if key not in data:
                errors.append(f"Missing agent output key: {key}")

        if "key_findings" in data and not isinstance(data.get("key_findings"), list):
            errors.append("key_findings must be a list")

        return {"valid": len(errors) == 0, "errors": errors}


guard = FoundryGuard()