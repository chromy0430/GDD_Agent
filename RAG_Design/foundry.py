import re
import json
import logging

# [Foundry IQ] Governance & Safety Layer
# 역할: AI 출력물의 유해성 검사, 코드 보안 검사, 포맷 검증

class FoundryGuard:
    def __init__(self):
        self.banned_imports = ["os", "sys", "subprocess", "shutil", "eval", "exec"]
        
    def validate_code_safety(self, code_text: str) -> dict:
        """
        생성된 코드에 위험한 시스템 접근 권한이 있는지 검사합니다.
        """
        validation_result = {"is_safe": True, "warnings": []}
        
        # 1. 금지된 라이브러리 import 검사
        for lib in self.banned_imports:
            # "import os" 또는 "from os" 패턴 검색
            pattern = re.compile(fr"^\s*(import|from)\s+{lib}\b", re.MULTILINE)
            if pattern.search(code_text):
                validation_result["is_safe"] = False
                validation_result["warnings"].append(f"Security Violation: '{lib}' module usage is restricted.")

        # 2. 파일 시스템 조작 의심 키워드 검사
        dangerous_keywords = ["remove", "rmtree", "system(", "popen"]
        for kw in dangerous_keywords:
            if kw in code_text:
                validation_result["warnings"].append(f"Potential Risk: '{kw}' keyword detected. Review required.")
        
        return validation_result

    def validate_json_structure(self, text: str) -> dict:
        """
        AI 응답이 올바른 JSON 포맷인지 검증하고 복구합니다.
        """
        try:
            # Markdown Code Block 제거
            cleaned_text = text.replace("```json", "").replace("```", "").strip()
            data = json.loads(cleaned_text)
            return {"valid": True, "data": data}
        except json.JSONDecodeError as e:
            return {"valid": False, "error": str(e), "raw": text}

# 인스턴스 생성 (싱글톤처럼 사용)
guard = FoundryGuard()