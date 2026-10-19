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
