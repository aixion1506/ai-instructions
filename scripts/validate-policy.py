#!/usr/bin/env python3
"""Validate the proposed private v5.2 policy set; do not install it."""
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
ACTIVE = {
    "common": ROOT / "policy/ranikun-common-senior-policy-v5.2.md",
    "chatgpt": ROOT / "adapters/ranikun-chatgpt-custom-instructions-v5.2.txt",
    "codex": ROOT / "adapters/ranikun-codex-AGENTS-cloud-local-v5.2.md",
}
HISTORY = [
    ROOT / "policy/ranikun-common-senior-policy-v5.1.md",
    ROOT / "adapters/ranikun-chatgpt-custom-instructions-v5.1.txt",
    ROOT / "adapters/ranikun-codex-AGENTS-cloud-local-v5.1.md",
]
REQUIRED = {
    "common": ["RPL-114", "Jira-first", "Confluence", "ChatGPT Web", "Codex Cloud",
               "Codex Local", "Claude Code", "Independent Review", "Owner"],
    "chatgpt": ["[업무 시작 — Jira-first]", "[정본·컨텍스트 — 필요할 때만]",
                "[Personal AI / Runtime]", "[개발 검증·승인]", "Confluence",
                "Source Merge", "/async-batch", "/핵심정리", "NOT_RUN"],
    "codex": ["RPL-114", "Jira-first", "Codex Cloud", "Codex Local",
              "ChatGPT", "Claude", "Confluence", "Independent Review",
              "Source Merge", "NOT_RUN"],
}
HARD_CHATGPT_LIMIT = 5000
BUDGET_CHATGPT = 3500


def main() -> int:
    errors = []
    loaded = {}
    for name, path in ACTIVE.items():
        try:
            loaded[name] = path.read_text(encoding="utf-8")
        except (OSError, UnicodeDecodeError) as exc:
            errors.append(f"unreadable active file {path.relative_to(ROOT)}: {exc}")
    for path in HISTORY:
        if not path.is_file():
            errors.append(f"missing preserved v5.1 file: {path.relative_to(ROOT)}")
    for name, markers in REQUIRED.items():
        text = loaded.get(name)
        if text is None:
            continue
        for marker in markers:
            if marker not in text:
                errors.append(f"missing {name} contract marker: {marker}")
        if not text.endswith("\n"):
            errors.append(f"missing final newline: {name}")

    chatgpt = loaded.get("chatgpt")
    if chatgpt is not None:
        length = len(chatgpt)
        print(f"ChatGPT v5.2: {length}/{HARD_CHATGPT_LIMIT} Unicode code points")
        if length > HARD_CHATGPT_LIMIT:
            errors.append(f"ChatGPT limit exceeded: {length}")
        if length > BUDGET_CHATGPT:
            errors.append(f"ChatGPT lean budget exceeded: {length}")
    for name, text in loaded.items():
        print(f"{name} v5.2: {len(text)} Unicode code points")

    if errors:
        print("Private policy v5.2 validation: FAIL")
        for error in errors:
            print(f"- {error}")
        return 1
    print("Private policy v5.2 validation: PASS (static contract only)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
