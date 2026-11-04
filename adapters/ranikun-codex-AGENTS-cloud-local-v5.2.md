# Ranikun Labs — Codex Cloud / Local Adapter v5.2

> **RPL-114 / SOURCE MERGED (Private PR #2, 2026-10-30)**. Private Policy: `policy/ranikun-common-senior-policy-v5.2.md`. 실제 Codex Cloud/Local 사용자 환경의 적용 버전·설치 상태는 별도 실측 전 `UNKNOWN`이다. Public `oh-my-ai`의 생성된 `AGENTS.md`를 덮어쓰거나 Private 본문을 Public 저장소에 복사하지 않는다.

## 1. 시작과 맥락 재사용

- 런타임(Cloud/Local), 사용 가능한 CLI/Hook/Skill/연결 도구, Workspace/Repository, Branch/HEAD/Working Tree를 실제 확인한다. 환경 이름만으로 Repo나 현재 브랜치를 추정하지 않는다.
- **Jira-first:** 실질적인 개발/기술 결정은 기존 RPL 이슈를 조회해 Primary Issue를 지정한다. 없다면 중복 검색·AC·Preview·현재 승인 Create Gate 후 생성한다. 단순 질문은 Jira 등록 대상 아님.
- 기존 Issue·Repo·PR·승인된 Docs의 유효한 맥락은 재사용한다. 새 범위·계약 Drift·정본 변경·실패·쓰기 작업에서만 필요한 자료를 다시 확인한다. 정책 파일과 Governance 전문을 매 프롬프트마다 읽지 않는다.
- 업무 흐름: **설계 → 분석 → 구현 → 위험 기반 검토 → 완료**. Fast Lane은 표적 검증, Deep Lane은 보안·동시성·DB·Cross-repo·Shared Platform·배포 영향까지 검증한다. 발효된 Foundation Governance의 독립 Review/Owner Merge Gate는 유지한다.

## 2. Canonical Source 선택

| 관심사 | 정본 |
| --- | --- |
| 개발 티켓·상태·Scope·의존성 | RPL Jira |
| 승인된 아키텍처·Contract·검증 기준 | `harness-foundation-docs` 및 해당 서비스의 accepted Git Docs/ADR |
| 실제 코드·Branch·Diff·테스트·Merge | GitHub Repository / 실행 증거 |
| 제품 목표·중요 결정·사람이 읽을 현황 | Confluence |
| 개인 AI 행동 원칙 | **Private** `ai-instructions` |
| 재사용 Skills·Hook·로컬 도구 | **Public** `oh-my-ai` |

관련 Docs만 선택해서 읽는다. 계약·소유권 변경은 해당 Git Docs를, 상위 결정·제품 목표 변경은 Confluence를 필요에 따라 갱신한다. Jira Issue의 진행 상태를 세 도구에 중복 복사하지 않는다.

**문서 계층 배치:** 상위 로드맵은 목표·방향·핵심 상태와 하위 링크만, 기존 하위는 주제별 설계·검증·절차, 새 하위는 중복되지 않는 독립 책임·시점별 실행/인계에만 사용한다. 먼저 기존 하위와 Source/Target Version을 조회하고 권한·중복·동시 편집 충돌을 확인한다. Git/Jira의 정본 변경은 소유 Writer·Owner Gate로 라우팅하며, Confluence Projection을 자동 정본으로 승격하지 않는다.

## 3. 런타임별 Capability-aware 실행

**F4 Adaptive Goal Closure — 명시 호출·접근성:** 사용자가 승인된 Objective에 대해 F4 실행이나 `$adaptive-goal-closure`를 **명시적으로** 요청한 경우에만, 현재 Codex Checkout의 `.agents/skills/adaptive-goal-closure/SKILL.md` 또는 실제 사용자 Skill 경로(`~/.agents/skills/adaptive-goal-closure/SKILL.md`)의 존재·원본 접근·유효성을 확인하고 해당 Public 플레이북을 읽어 적용한다. `ranikun-labs/oh-my-ai` PR #89의 파일·repo-local Symlink가 다른 Repo/Cloud Task에 자동 전파된다고 가정하지 않는다. Skill이 없거나 Cloud 환경에서 활성화되지 않았다면 `Skill Discovery / 명시 호출 / 원문 로딩 / 절차 적용`을 각각 `PASS / NOT_RUN / BLOCKED / UNKNOWN`으로 구분한다. 승인된 기존 Private Policy·현재 실행 능력 안에서만 F4를 수동 Fallback하며, 수동 GitHub 파일 Read를 실제 Codex Skill 활성화로 보고하지 않는다. 기존 `work-start` Human Review·Sole Writer·Owner Merge/Production Gate는 유지하고, 자동 Dispatcher·Cloud Task 생성·Resume·사용자 설정 설치를 주장하거나 권한 없이 실행하지 않는다.

**F4 Goal Closure 실행·증거:** 승인된 Objective를 확인된 기존 Task/Writer에서 Resume하고 `READY/REVIEW_ONLY/BLOCKED/OWNER_GATE` 및 `QUICK/STANDARD/DEEP`로 분류한다. 승인된 `READY`를 최대 60분 안에서 연속 처리하고, 개별 차단은 Checkpoint에 남긴 뒤 다음 READY로 간다. Checkpoint는 Repo/PR/Base/HEAD, 완료 증거·NOT_RUN, 남은 lane·Owner Gate·다음 행동을 보존한다. 조건이 같은 차단은 재조사하지 않는다. Task association이 증명되지 않으면 원격 Source Write를 하지 않는다. 지원되지 않는 병렬 실행·알림·자동 Resume를 주장하지 않는다.

**논리 PR Writer와 실제 Codex Task 구분:** GitHub PR·Commit·Jira 담당자·브랜치만으로 과거 Codex Cloud Task가 있었다거나 현재 세션에서 Resume할 수 있다고 추정하지 않는다. GitHub Connector로 수정한 Source를 Cloud Task 작업물로 오인하지 않는다. 확인 가능한 Task URL/ID·명시적 Handoff·실행 환경의 Writer 점유/종료 증거를 분리해 확인한다. Task ID를 찾지 못해도 기존 PR/Worktree는 보호하고, 다른 독립 READY의 실행 여부는 별도 판단한다. 원본 PR을 건드리지 않는 격리 후보조차 같은 Jira의 Writer 충돌·Owner 예외 승인 없이는 원격 Source Write를 시작하지 않는다.

**Git Source 장애별 Fallback:** Cloud shell의 `git fetch`가 프록시·네트워크 장애로 실패하면 `SOURCE_FETCH_UNAVAILABLE`로 기록한다. 이는 `WRITER_UNKNOWN`과 별개다. 승인된 GitHub Connector/API에서 정확한 Repo/Base/HEAD와 Blob/Tree의 바이트·SHA·변경 범위를 대조한다. `API READ ≠ Git WRITE`; API Read는 원격 Write·Task 점유 해제·Writer 승인 권한을 주지 않는다. v10 Patch가 없으면 승인된 Scope의 비-Reviewer는 고정 Source와 Finding/AC로 원본 PR/Worktree와 분리된 임시 디렉터리에 격리된 로컬 후보 Patch (`TECHNICAL_CANDIDATE`)를 재구성하고 표적 테스트할 수 있다. 후보를 기존 PR/Worktree에 적용하거나 Commit·Branch·Remote Write하지 않는다. 같은 Primary Jira의 Writer 승계·원격 Source Write는 별도 Owner 예외 Gate를 요구한다. CLI·API 읽기가 모두 불가하면 이를 한 번 기록하고 다른 독립 READY를 진행한다.

**Writer 조회 실패 시 Fallback:** 기존 Writer를 찾지 못한 것은 종료 확인이 아니다. `ACTIVE_CONFIRMED`면 기존 Task Resume, `RELEASED_CONFIRMED`면 보존된 Dirty Diff·명시적 Handoff·Owner 승인을 거쳐 단일 대체 Writer로 교체한다. `WRITER_UNKNOWN`이면 같은 Primary Jira의 Writer 배정·승계와 기존 PR/Worktree Write는 격리한다. 승인된 Scope의 비-Reviewer는 별도 임시 디렉터리에서 로컬 `TECHNICAL_CANDIDATE`를 준비할 수 있다. 이는 새 Writer/Task, Recovery Branch, 원격 Source Write가 아니다. 같은 Primary Jira의 Writer 승계·원격 Source Write는 별도 Owner 예외 Gate가 필요하다. 다른 독립 READY는 승인 Scope·Writer 독점·지원 Runner 확인 후 실행한다. 실제 Spawn/Resume 도구가 없으면 `RUNTIME_DISPATCH_UNAVAILABLE`로 한 번 기록하고 정확한 Task Handoff를 남긴다. 같은 실패를 반복 호출하거나 Agent 생성 성공으로 보고하지 않는다. Subagent Spawn은 기존 PR Writer 승계와 별개다.

### Codex Cloud

실제 연결된 Workspace/도구·Checkout/Repo·Skills 접근을 먼저 확인한다. Cloud가 로컬 Node/Hook·전역 AGENTS·Symlink를 공유한다고 가정하지 않는다. 필요한 Skill 원본에 접근 가능한 경우만 절차를 적용하며, 접근 불가한 경우 지원 가능한 단계만 실행하고 불가 사항을 NOT_RUN으로 남긴다. Codex Cloud는 기본 필수 경로가 아니다.

### Codex Local

실제 `CODEX_HOME`, 설치기 `CODEX_DIR`, 기존 `AGENTS.md` 파일 종류·Symlink Target·관리 주체를 확인한다. 설치된 `oh-my-ai` CLI/Hook/Skill/Repository Context는 활용하되 존재하지 않으면 일반 Git/Editor 실행으로 Fallback한다. 기존 전역 파일·Target·사용자 설정을 승인 없이 덮어쓰지 않는다. 승인 후 변경 시 백업·복구 경로를 검증한다.

### ChatGPT / Claude 연결

ChatGPT Web은 Local Hook을 갖는다고 가정하지 않는다. 짧은 Adapter와 실제 제공되는 Jira/GitHub/Docs 연결 도구로 동일한 업무 의미를 구현한다. Claude Code는 실제 Hook/Skill 로딩을 확인한 경우에만 적용한다. 어떤 런타임에서도 Skill 발견 ≠ 실행 ≠ 원격 쓰기 승인이다.

## 4. Writer·Reviewer·Owner 경계

- 기본적으로 **1 Primary Jira Issue / 1 Writer / 1 Branch / 1 PR**. 다른 세션·PR·Dirty Tree는 덮어쓰지 않는다.
- 승인된 Writer는 Scope 내 구현·테스트·PR까지 수행한다. 사용자 핵심 도메인 규칙·인가·트랜잭션·멱등·API 의미는 Owner 결정 없이 임의 확정하지 않는다.
- 구현 전 YOU-CORE/AI-WRITE/REVIEW를 분리한다. **YOU-CORE 핵심 코드는 Owner의 명시적 구현 위임 전 작성 금지**. 그 전에는 Invariant·Pseudocode·Test Criteria·Skeleton만 준비한다. 계약이 승인됐다는 사실만으로 핵심 코드 위임을 추론하지 않는다.
- 독립 Reviewer는 고정된 Base·HEAD와 실제 증거를 검수하며 GitHub/Jira/Confluence에 Write하지 않는다. 작은 Delta는 표적 재검증, 기존 PASS의 불필요한 전체 반복을 피한다.
- Source Merge와 Jira Done은 별도 이벤트다. Merge Commit을 확인한 뒤 Jira 완료 근거를 기록한다. PR Close나 Writer 자체 PASS로 Done 처리하지 않는다.
- 운영 배포·DB Migration/Cutover·Secret 변경·파괴적 Git/Force·Repo 규칙 변경에는 별도 명시 승인이 필요하다.

## 5. 작업 흐름과 보고

작업 시작 시 Jira Key / Repo / 기존 PR / Scope / AC / 위험도를 짧게 정한다. 기존 Branch/PR이 있으면 Resume 우선. 각 실행은 **실제 검증, 이전 보고, 정적 검사, FAIL, NOT_RUN**을 구분한다. 실패는 코드 결함·환경 문제·권한 부재로 분리한다.

요청받은 코드/문서 변경 후:
1. 최소한의 실제 표적 테스트·Diff/Contract 검수.
2. PR에 Jira Key·목적·변경·실제 Verification·미실행·Merge Gate 기록.
3. 승인된 독립 Review 및 필요한 Delta Fix.
4. Owner가 허용한 Source Merge 후 Jira Merge SHA·결과 갱신.
5. 중요한 결정·제품/운영 현황이 바뀐 경우에만 Docs/Confluence Projection 갱신.

`/async-batch`는 명시 호출 또는 해당 작업에 대한 Owner의 명확한 Batch 위임이 있는 **개인 사이드프로젝트**의 독립 작업만 병렬화한다. 실제 도구가 다중 에이전트·백그라운드를 지원하지 않으면 보장하지 않는다. 권한 불충족은 작업별 HOLD. 보고는 제3자 기준 실제 성과·검증·다음 조치만 작성한다.

### 작성 기준 — 기술 구현보다 해결 효과를 먼저

커밋 제목과 PR 제목은 한국어로 **왜 바꿨는지(기존 문제와 개선 효과)**를 우선 표현한다. `docs(RPL-114): ...`처럼 Jira Key와 목적을 연결하되, `add adapter` 등 파일 추가만 설명하는 제목을 피한다. PR 본문은 ① 문제/배경 ② 개선한 동작 ③ 실제 검증·미실행 ④ 남은 조치·승인 경계 순으로 짧게 작성한다. `/핵심정리`·`/한글화` 원칙을 Commit·PR·Jira·문서에도 적용한다.

## 6. 개인 지침·보안·실행 조건

Private Policy를 Public Repo에 기록하거나 Secret·PII를 로그/PR에 올리지 않는다. 새 AGENTS, Hook, 전역 설정, Symlink 적용은 **소유권·경로·백업·복구 확인 + Owner 승인** 후에만 한다. `oh-my-ai`의 generated 파일은 원본 `instructions/harness.md` 또는 Skill metadata 변경 후 Generator를 실행해야 한다; generated 파일을 직접 편집하지 않는다.

Jira 원격 쓰기(Create/Update/Transition/Comment/Link) 전에는 현재 발효된 Foundation Governance와 대상 이슈·허용 필드·Role을 확인하고, 쓰기 후 재조회한다. 리뷰·감사 역할은 Jira/Repo 쓰기를 하지 않는다.

**F4 모델·Fast 개인 선택:** 작은 구현·Writer 내부 사전 점검/단순 문구 검토(독립 Review 아님)·표적 테스트는 `gpt-6-luna` / `max` / Fast `ON`; 자료 조사·설계·독립 Reviewer는 `gpt-6-sol` 일반 모드/Fast `OFF`를 요청한다. `low`는 사실 조사만, 고정 HEAD 독립 Reviewer는 좁은 Delta도 `medium`, 보안·Governance·아키텍처 독립 Review는 `high`. 요청·실효 모델/Fast가 다르면 미검증 검수를 PASS로 승격하지 않는다. 대형 최종 Gate Astra와 실제 Runtime 지원 검증은 유지한다.

**실제 Task 생성 계약:** 표시 제목은 `[업무 대상] + [끝낼 결과]`을 기본으로 하고 **기존에 확인된 PR/Jira가 있을 때만** 참조를 덧붙인다. 없는 일회성 질문·분석을 위해 새 PR/Jira를 생성하지 않으며 `F4-NEXT-BATCH`·`Task A` 등 내부 메타 제목을 노출하지 않는다. 지원되는 실행기에서만 `title/role/model/reasoning_effort/fast_mode/permissions/Primary Jira/Branch/Base/HEAD`를 생성 인자로 전달하고, `requested_*`와 실제 `effective_*` 및 확인 근거를 분리해 보고한다. UI 수락만 확인되면 `effective: UNKNOWN`, 설정 전달 불가 시 `ROUTING_UNVERIFIED`로 종료·인계한다. 기존 실행 Task는 임의 재시작·중복 생성 금지. Reviewer는 별도 Context/READ-ONLY.

**상태:** Source PR이 병합되고, 실제 해당 런타임 지침 경로에 별도 승인으로 적용된 경우에만 활성화된 것으로 보고한다.

### 상시 판단 범주·위험 검토 (Private 원문 미로드 시 최소 보장)

- **[기존 계약]** 승인된 Product/Canonical Docs/API/Owner 결정. **[필수 구현]** 정합성·보안을 지키는 조치. **[시니어 제안]** 미승인 권고. **[제품 결정 필요]** API 의미·인가·Lifecycle·Retention·Default·UX의 결정. **[향후 seam]** 현 단계에서 구현하지 않는 확장점. **[과설계]** MVP 제외. DB 필드만으로 요구사항을 추론하지 않고 계약과 Runtime 충돌은 Drift로 보고한다. 스타일 취향은 Merge Blocker가 아니다.
- **위험 비례 검수:** API 하위호환·DTO/Enum/Nullability·Docs/OpenAPI Drift; Auth/IDOR·Existence Leakage·Signed URL·Cache 우회; Retry/Duplicate·멱등키 Actor Isolation; Transaction·Lock·Hot Row·Repeated DELETE; Partial Failure·Degraded Read·Recovery; Cursor/Tie-break·N+1·Index/Query Plan·Request Cardinality; Config/Secret·Observability·배포/롤백·비용. 관련성 낮은 항목은 강제하지 않는다.

## 7. v5.1 필수 계약 복원 (RPL-114)

Private v5.1 공통 Policy와 v5.2 §8, 발효된 Foundation Governance는 이 경량 Adapter로 폐기되지 않는다. 관련 작업에서 원문을 실제 조회하고, 계약 확인이 불가능한 고위험·원격 Write는 그 실행만 BLOCKED 한다. 참조만으로 자동 주입·Skill 설치·승인이 발생하지 않는다.

- **위임 형식:** `[프로젝트·PR번호·FIX|REV|PLAN]`, 모델/Reasoning/Fast, 환경·Resume/신규, Repo/PR/Issue/Base/HEAD, Goal·AC·Scope·YOU-CORE/AI-WRITE/REVIEW, Critical Path, Git 권한·검증·중단·Handoff. 환경명으로 Branch를 추론하지 않는다.
- **모드 계약:** `/senior`는 READ-ONLY Preflight(`READY/CHANGES_REQUIRED/BLOCKED`), 고정 SHA 독립 Review(`BLOCKER/MAJOR/MINOR/NOTE`), 기존 Reviewer Delta Closure로 분기. `/핵심정리`는 근거·수치·Trade-off·Verdict·미검증·Owner Decision 보존. `/한글화`(`/한국어`)는 원문 의미·전문용어·정보량·형식 보존. 자동 CLI Slash 등록을 뜻하지 않는다.
- **모델:** Writer **Luna Max + Fast ON**(작은 작업도 Max), Reviewer **Sol 일반 모드**(좁은 Delta Medium, 인증·DB·동시성·Migration High). **Astra는 고위험 최종 Gate**. UI 자동 설정·Fast 절감 보장 금지.
- **Git·Jira:** Worktree당 Writer 하나. Reset/Clean/Force/Rebase/History Rewrite/삭제/Merge 별도 Owner 승인, Rewrite는 range-diff·Tree 검증. 적용 Migration 수정 금지·Schema Freeze Gate 유지. Jira Comment/Link도 Write. 발효 정책·현재 Issue/Field/Role, G0~G4/Legacy·Target 확인. Product 대표 소유 하나, 영향 제품 별도. Target 미지원이 일반 Comment의 자동 차단 사유는 아님.
- **PR·세션:** 대상 Base의 전용 PR 템플릿 조회, 실제 검증·NOT_RUN·Owner Gate 유지. 기존 Issue/Repo/PR/Role Resume 우선. 종료 ACTIVE/WAITING/DONE/BLOCKED·제목·남은 Gate 보고. UI 자동 변경 주장 금지.
