#!/usr/bin/env python3
"""Read-only structural checks for the private personal-policy repository."""

from pathlib import Path
import hashlib
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


# v5.2 candidate validation extends, not replaces, the v5.1 safety checks above.
V52_FILES = {
    "common": ROOT / "policy/ranikun-common-senior-policy-v5.2.md",
    "chatgpt": ROOT / "adapters/ranikun-chatgpt-custom-instructions-v5.2.txt",
    "codex": ROOT / "adapters/ranikun-codex-AGENTS-cloud-local-v5.2.md",
}
V52_MARKERS = {
    "common": ("RPL-114", "v5.1 필수 계약의 보존", "Jira-first", "Confluence", "Context-aware Lazy Loading",
               "Independent Review", "/핵심정리", "/한글화", "Luna Max", "CODEX_DIR"),
    "chatgpt": ("[판단·검토 계약]", "[Codex 위임·Git]", "[업무 시작 — Jira-first]", "[정본·컨텍스트 — 필요할 때만]",
                "[커밋·PR 문장]", "[모델·세션]", "Confluence", "/async-batch", "NOT_RUN"),
    "codex": ("v5.1 필수 계약 복원", "Luna Max + Fast ON", "Jira-first", "Codex Cloud", "Codex Local", "ChatGPT",
              "독립 Reviewer", "Confluence", "성과", "Source Merge", "NOT_RUN"),
}
LEAN_CHATGPT_BUDGET = 3500
MIN_CHATGPT_BUDGET = 3000
# Exact Git blob identities of the three approved v5.1 originals.
V51_GIT_BLOBS = {"common_policy":"ddecdc225d4f0588bd6975c71d179187efc924ec","chatgpt_adapter":"e8eb8f1db5f1e8b15757d743e018b1f0c2bc07b5","codex_adapter":"ac7f334cb4df9cbc55d4f87a01e5a9773b84c799"}



def validate_v52() -> int:
    errors = []
    for name, path in V52_FILES.items():
        try:
            source = path.read_text(encoding="utf-8")
        except (OSError, UnicodeDecodeError) as exc:
            errors.append(f"missing or unreadable v5.2 {name}: {exc}")
            continue
        for marker in V52_MARKERS[name]:
            if marker not in source:
                errors.append(f"missing v5.2 {name} marker: {marker}")
        if not source.endswith("\n"):
            errors.append(f"missing v5.2 {name} trailing newline")
        if name == "chatgpt":
            size = len(source)
            print(f"ChatGPT v5.2 adapter: {size}/{MAX_CHATGPT_CODEPOINTS} code points")
            if size < MIN_CHATGPT_BUDGET:
                errors.append(f"ChatGPT v5.2 below coverage budget: {size}")
            if size > LEAN_CHATGPT_BUDGET:
                errors.append(f"ChatGPT v5.2 exceeds lean budget: {size}")
            if size > MAX_CHATGPT_CODEPOINTS:
                errors.append(f"ChatGPT v5.2 exceeds platform limit: {size}")
    for name, expected in V51_GIT_BLOBS.items():
        path = FILES[name]
        if not path.is_file():
            continue  # The v5.1 main() check already reports missing files.
        raw = path.read_bytes()
        prefix = b"blob " + str(len(raw)).encode("ascii") + bytes([0])
        actual = hashlib.sha1(prefix + raw).hexdigest()
        if actual != expected:
            errors.append(f"v5.1 original modified: {path.relative_to(ROOT)}")
    if errors:
        print("v5.2 extension validation: FAIL")
        for error in errors:
            print(f"- {error}")
        return 1
    print("v5.2 extension validation: PASS")
    return 0


if __name__ == "__main__":
    legacy_result = main()
    v52_result = validate_v52()
    sys.exit(0 if legacy_result == 0 and v52_result == 0 else 1)
