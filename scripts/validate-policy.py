#!/usr/bin/env python3
"""Read-only structural checks for the private personal-policy repository."""

from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
FILES = {
    "common_policy": ROOT / "policy/ranikun-common-senior-policy-v5.1.md",
    "chatgpt_adapter": ROOT / "adapters/ranikun-chatgpt-custom-instructions-v5.1.txt",
    "codex_adapter": ROOT / "adapters/ranikun-codex-AGENTS-cloud-local-v5.1.md",
}
MAX_CHATGPT_CODEPOINTS = 5000
REQUIRED_MARKERS = {
    "common_policy": (
        "Jira Governance",
        "PR Authoring",
        "모델 라우팅",
        "Spec-to-Implementation",
        "Session Lifecycle",
    ),
    "chatgpt_adapter": (
        "[Model Policy]",
        "Luna Max + Fast ON",
        "[Jira Governance / Write Gate]",
        "[PR Authoring]",
        "[Spec → Implementation]",
        "[Session Lifecycle]",
        "/async-batch",
        "[Private Policy / AGENTS Gate]",
        "개인/Private 지침·설정의 공개 저장소 추적 파일 복사·Commit·Push 금지",
        "AGENTS.md 적용 전 실제 경로·파일 종류·Symlink·해석 Target",
        "양쪽 소유자/관리자·생성/관리 상태 확인",
        "불명확·충돌 시 설치·덮어쓰기·링크 변경 중단",
        "oh-my-ai 관리 전역 파일·링크·Target 변경은 통합 설계·Owner 승인 필수",
        "런타임 CODEX_HOME·설치기 CODEX_DIR은 별개",
        "각각 경로·설정·버전 확인",
        "CODEX_HOME 미참조",
        "명시적 Owner 승인·파일/Target/링크 Metadata 백업·복구 경로 검증 후만 적용",
        "승인 전 전역 설치 금지·복구 시 후속 변경 보존",
    ),
    "codex_adapter": (
        "Jira Governance / CRUD WRITE Gate",
        "Luna Max + Fast ON",
        "PR Authoring",
        "모델 라우팅",
        "Spec-to-Implementation",
        "Session Lifecycle",
    ),
}


def main() -> int:
    errors = []
    loaded = {}
    for name, path in FILES.items():
        if not path.is_file():
            errors.append(f"missing file: {path.relative_to(ROOT)}")
            continue
        try:
            loaded[name] = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            errors.append(f"not valid UTF-8: {path.relative_to(ROOT)}")

    for name, markers in REQUIRED_MARKERS.items():
        text = loaded.get(name)
        if text is None:
            continue
        for marker in markers:
            if marker not in text:
                errors.append(f"missing marker in {name}: {marker}")

    chatgpt = loaded.get("chatgpt_adapter")
    if chatgpt is not None:
        count = len(chatgpt)
        if count > MAX_CHATGPT_CODEPOINTS:
            errors.append(
                f"ChatGPT adapter is {count} Unicode code points; limit is {MAX_CHATGPT_CODEPOINTS}"
            )
        print(f"ChatGPT adapter: {count}/{MAX_CHATGPT_CODEPOINTS} Unicode code points")

    if errors:
        print("Policy validation: FAIL")
        for error in errors:
            print(f"- {error}")
        return 1

    print("Policy validation: PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
