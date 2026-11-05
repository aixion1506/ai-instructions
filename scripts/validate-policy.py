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
    "common": (
        "RPL-114", "v5.1 필수 계약의 보존", "명시적 구현 위임 전 작성 금지",
        "Invariant·Pseudocode·Test Criteria·Skeleton", "Jira-first", "Confluence",
        "Context-aware Lazy Loading", "Independent Review", "/핵심정리", "/한글화",
        "Luna Max", "CODEX_DIR", "## 5.2 F4 작업별 실제 모델",
        "기존에 확인된 PR/Jira가 있을 때만", "**문서 배치:**", "gpt-6-sol",
        "ROUTING_UNVERIFIED", "## 5.3 F4 Goal Closure", "`READY`",
        "`REVIEW_ONLY`", "`BLOCKED`", "`OWNER_GATE`", "QUICK", "STANDARD",
        "DEEP", "30~60분", "Checkpoint/Resume", "Runner 한도",
        "AUTO_INTENT=ON", "AUTO_PREFLIGHT=DEVELOPMENT-only",
        "AUTO_INTENT=ON`: 자연어에서 기존 승인 Objective의 완료·재개 의도를 감지한다. 의도 분류만으로 Skill을 로드·호출하거나 실행·위임·원격 쓰기 권한을 얻지 않는다.",
        "AUTO_PREFLIGHT=DEVELOPMENT-only`: 개발 요청에는 READ-ONLY Preflight를 자동 적용한다.",
        "일반 질문·설명·조회(READ)는 답변만 하며 Jira·Task·Writer를 만들거나 시작하지 않는다.",
        "AUTO_EXECUTION=GATED", "Skill을 로드·호출",
        "Skill 호출은 계속 명시적으로 요구",
        "기존 승인 Objective·Scope·AC, Primary Jira/Task, 단일 Writer/Worktree, 현재 Repo/PR/Base/HEAD, 쓰기 권한, 지원 Runtime이 모두 확인된 경우",
        "Jira·Task·Writer를 자동 생성하지 않는다.",
        "격리 로컬 `TECHNICAL_CANDIDATE`는 `AUTO_EXECUTION` 대상 `READY`가 아닌 별도 수동 복구 단계다.",
        "`AUTO_INTENT`는 이를 자동 시작하지 않으며",
    ),
    "chatgpt": (
        "명시적 구현 위임 전 작성 금지", "Invariant·Pseudocode·Test Criteria·Skeleton",
        "[판단·검토 계약]", "[Codex 위임·Git]", "[기존 계약]", "[과설계]",
        "CODEX_HOME", "range-diff", "[업무 시작 — Jira-first]",
        "[정본·컨텍스트 — 필요할 때만]", "[커밋·PR 문장]", "[모델·세션]",
        "Confluence", "/async-batch", "NOT_RUN", "문서 배치: 상위=", "Sol Low(",
        "Runtime 설치·전역 AGENTS·Symlink 변경 및 설치 복구는 Private Policy·실환경 확인 후 Owner 승인 필요.",
        "작업 목적 제목", "미확인 UNKNOWN", "AUTO_INTENT=ON",
        "AUTO_PREFLIGHT=DEVELOPMENT-only", "AUTO_EXECUTION=GATED",
        "AUTO_INTENT=ON(자연어로 기존 승인 Goal 완료·재개 의도 감지; 권한 아님).",
        "AUTO_PREFLIGHT=DEVELOPMENT-only(개발 요청 READ-ONLY; Jira/Task Create 없음).",
        "Intent≠Load/Invoke", "explicit-only",
        "기존 Objective/Scope/AC·Primary Jira/Task·단일 Writer/Worktree·Repo/PR/Base/HEAD·권한·지원 Runtime이 모두 확인된 기존 READY만",
        "신규 Jira/Task/Writer 금지", "질문/READ는 실행·Jira/Writer 생성 금지",
        "검토 전용 세션은 원격 쓰기 금지", "READY/REVIEW_ONLY/BLOCKED/OWNER_GATE",
        "TECHNICAL_CANDIDATE 자동 작성 금지, 승인 Scope의 명시 요청만 별도 격리 가능.",
        "QUICK/STANDARD/DEEP", "≤60분", "Checkpoint", "Resume",
        "개인 사이드프로젝트만", "회사 자동 적용 금지",
    ),
    "codex": (
        "v5.1 필수 계약 복원", "명시적 구현 위임 전 작성 금지",
        "Invariant·Pseudocode·Test Criteria·Skeleton", "[기존 계약]", "[필수 구현]",
        "[제품 결정 필요]", "API 하위호환", "Auth/IDOR", "Luna Max + Fast ON",
        "Jira-first", "Codex Cloud", "Codex Local", "ChatGPT", "독립 Reviewer",
        "Confluence", "성과", "Source Merge", "NOT_RUN", "**문서 계층 배치:**",
        "**실제 Task 생성 계약:**", "기존에 확인된 PR/Jira가 있을 때만",
        "gpt-6-luna", "effective: UNKNOWN",
        "AUTO_INTENT·F4 Adaptive Goal Closure", "adaptive-goal-closure",
        "`AUTO_INTENT=ON`은 자연어에서 기존 승인 Objective의 완료·재개 의도를 분류할 뿐 Skill 로드·호출, 실행·위임, 원격 쓰기 권한을 부여하지 않는다.",
        "`AUTO_PREFLIGHT=DEVELOPMENT-only`는 개발 요청에 READ-ONLY Preflight를 적용하며, 질문·설명·READ에는 Jira·Task·Writer 생성을 금지한다.",
        "수동 GitHub 파일 Read를 실제 Codex Skill 활성화로 보고하지 않는다",
        "F4 Goal Closure 실행·증거", "READY/REVIEW_ONLY/BLOCKED/OWNER_GATE",
        "QUICK/STANDARD/DEEP", "Checkpoint", "60분", "원격 Source Write",
        "AUTO_INTENT=ON", "AUTO_PREFLIGHT=DEVELOPMENT-only",
        "AUTO_EXECUTION=GATED", "Skill 로드·호출",
        "명시적으로 요청된 경우에만 허용",
        "기존 Objective·Scope·AC, Primary Jira/Task, 단일 Writer/Worktree, 현재 Repo/PR/Base/HEAD, 권한과 지원 Runtime이 모두 확인된 READY만 실행한다.",
        "Jira·Task·Writer를 자동 생성하지 않는다.",
        "`TECHNICAL_CANDIDATE`는 `AUTO_EXECUTION` 대상 READY가 아니다.",
        "`AUTO_INTENT`는 후보를 자동 시작하지 않으며",
        "명시적으로 요청하면 고정 Source·별도 임시 디렉터리",
        "Owner Recovery 추가 승인 없이",
    ),
}
# CLI transport failure is distinct from Writer ownership failure.
V52_SOURCE_FETCH_FALLBACK_MARKERS = {
    "common": ("SOURCE_FETCH_UNAVAILABLE", "`git fetch`", "GitHub Connector/API", "Blob/Tree", "격리 로컬 Patch 후보", "다른 독립 READY",),
    "codex": ("SOURCE_FETCH_UNAVAILABLE", "`git fetch`", "GitHub Connector/API", "Blob/Tree", "후보 Patch", "Owner 예외 Gate",),
}

# F4 source-boundary regression guards: structural markers, not Runtime behavior.
V52_SOURCE_FETCH_BOUNDARY_MARKERS = {
    "common": ("Blob/Tree의 바이트·SHA·변경 범위", "API READ ≠ Git WRITE", "승인된 Scope의 비-Reviewer", "원본 PR/Worktree와 분리된 임시 디렉터리", "TECHNICAL_CANDIDATE", "같은 Primary Jira의 Writer 승계·원격 Source Write는 별도 Owner 예외 Gate"),
    "codex": ("Blob/Tree의 바이트·SHA·변경 범위", "API READ ≠ Git WRITE", "승인된 Scope의 비-Reviewer", "원본 PR/Worktree와 분리된 임시 디렉터리", "TECHNICAL_CANDIDATE", "같은 Primary Jira의 Writer 승계·원격 Source Write는 별도 Owner 예외 Gate"),
}

# F4 recovery and feature-level review regression guards (structural, not Runner E2E).
V52_F4_RECOVERY_MARKERS = {
    "common": ("ACTIVE_CONFIRMED", "RELEASED_CONFIRMED", "WRITER_UNKNOWN", "RUNTIME_DISPATCH_UNAVAILABLE", "다른 독립 Primary Jira", "원본 PR/Worktree", "**논리 Writer·Git Source·Codex Task 분리:**", "Feature/Slice 단위 검증·검수", "각 PR의 독립 Review Gate는 유지", "조기 종료 방지와 READY 재배정",),
    "codex": ("ACTIVE_CONFIRMED", "RELEASED_CONFIRMED", "WRITER_UNKNOWN", "RUNTIME_DISPATCH_UNAVAILABLE", "**논리 PR Writer와 실제 Codex Task 구분:**", "다른 독립 READY", "기존 PR/Worktree",),
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
        for marker in V52_MARKERS[name] + V52_F4_RECOVERY_MARKERS.get(name, ()) + V52_SOURCE_FETCH_FALLBACK_MARKERS.get(name, ()) + V52_SOURCE_FETCH_BOUNDARY_MARKERS.get(name, ()):
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
