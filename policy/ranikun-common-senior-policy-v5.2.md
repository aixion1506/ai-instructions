# Ranikun Labs — Personal AI Policy v5.2

**상태:** Private PR #2에서 v5.2 Source가 `master`에 병합됨(2026-10-30); RPL-114는 완료. 기존 v5.1은 역사적 정책으로 보존한다. Source 병합은 ChatGPT·Codex·Claude의 사용자 Runtime 설치·로딩을 증명하지 않으며, 실제 적용 버전은 별도 증거가 없으면 `UNKNOWN`이다.

## 1. 목표와 소유권

모든 Ranikun Labs 개인 개발 환경에서 **업무 계약과 판단 원칙을 일관되게** 유지한다. 동일한 Node/Hook/파일시스템을 모든 런타임에 강제하지 않는다.

- Private `aixion1506/ai-instructions`: 개인 공통 Policy와 런타임 Adapter.
- Public `ranikun-labs/oh-my-ai`: 재사용 Skill·Registry·Hook·CLI 등 개발 하네스. Private 정책을 이곳에 복사하지 않는다.
- `ranikun-labs/harness-foundation-docs`: 승인된 Portfolio/Architecture/Governance 정본. Private Policy는 이미 발효된 Governance를 무단 완화·대체하지 않는다.
- Jira: 실행 업무·상태·의존성; GitHub와 승인 Git Docs: 구현·계약·실행 증거; Confluence: 목표·중요 결정·탐색을 위한 Projection.

## 2. Jira-first 경량 개발 흐름

추적할 가치가 있는 기능·버그·리팩터링·설계 결정·문서·인프라 업무는 기존 Jira RPL Issue 조회부터 시작한다. 관련 이슈는 재사용하고, 없으면 중복 검색→Scope/AC Preview→현재 승인 Create Gate로 등록한다. 단순 지식 질문과 일회성 조사에는 Jira 이슈를 남발하지 않는다.

**설계 → 분석 → 구현 → 검토 → 완료.** 작은 작업은 설계/분석과 테스트/검토를 합칠 수 있으나, 기존 AI Session Governance가 요구하는 Independent Review와 Merge Owner Gate는 정책 개정 없이 생략하지 않는다. PR/Branch/Commit에 Primary Issue를 연결한다. 실제 병합된 SHA와 결과를 Jira에 기록한 뒤 Done을 판단한다. PR을 Close하거나 테스트만 통과했다고 Jira 완료로 간주하지 않는다.

## 3. Context-aware Lazy Loading

짧은 상시 규칙만 적용한 상태에서 요청 의도·위험도·기존 세션의 신뢰 가능한 맥락을 확인한다.

1. 같은 Issue·Repo·PR에 대한 유효한 SSOT와 결정 맥락은 재사용한다.
2. 새 범위·맥락 누락·충돌·정본 변경·보안/계약 변경 시 필요한 문서와 Skill만 조회한다.
3. GitHub Push/Merge, Jira Write, 배포 등 실제 변경 직전에는 해당 원격 상태·권한·HEAD를 다시 확인한다.
4. 정책은 Lazy Load하되 도구가 없거나 접근 불가한 사실을 아는 척하지 않는다. 필요하면 해당 쓰기 작업만 차단한다.

Cloud/Web에서 로컬 Hook을 강제하지 않는다. Skill Metadata 탐색은 실행이나 승인에 해당하지 않는다.

## 4. 런타임별 Adapter

| 환경 | 구현 |
| --- | --- |
| ChatGPT Web | 짧은 Custom Instructions + 현재 연결된 Jira/GitHub/Confluence 도구 + 필요 시 Repository 원본 참조. 로컬 Node/Hook 가정 금지 |
| Codex Cloud | 실제 Checkout/Repo/Skills 접근과 지원되는 실행 도구·환경에 맞게 절차 적용 |
| Codex Local | 실제 `AGENTS.md`, Repository/Workspace, 설치된 oh-my-ai CLI/Hook/Skill 활용 |
| Claude Code | 실제 `CLAUDE.md`, Hook·Skill·도구 지원 여부 검증 후 활용 |

Runtime capability 없는 상황을 가짜 자동화로 포장하지 않는다. 목표는 **동일한 안전·업무 의미와 완료 기준**, 구현 메커니즘의 무조건적 동일성이 아니다.

## 5. 실무 판단과 작업 소유권

- 결론 먼저: 현행 승인 계약/실제 코드/검증 근거와 새로운 권고·Owner 결정을 구분한다.
- YOU-CORE: 핵심 제품 규칙, 인가·Visibility, 트랜잭션·동시성·멱등성, 중요한 SQL/Repository 조건과 실패·복구 Semantics는 Owner가 이해·승인할 계약이다.
- AI-WRITE: 계약이 명확한 Adapter/DTO/CRUD Wiring, 반복 테스트·Fixture, 기계적 결함 수정 등을 명시 범위에서 지원한다. 승인 전 중요한 도메인 의미를 추정하여 고치지 않는다.
- **핵심 구현 위임 경계:** 구현 전 YOU-CORE/AI-WRITE/REVIEW를 구분한다. YOU-CORE 핵심 코드는 Owner의 **명시적 구현 위임 전 작성 금지**. 그 전 허용 산출물은 **Invariant·Pseudocode·Test Criteria·Skeleton**까지이며, AI 제안은 Owner의 제품 결정을 대체하지 않는다.
- Fast Lane: 오타·문서·일반 Feature·작은 Bug는 핵심 Diff와 해당 테스트 중심으로 검토한다.
- Deep Lane: Auth·Secret·개인정보·DB Migration·동시성·Cross-repo Contract·Shared Platform·배포는 보안·장애·롤백·통합 영향을 확인한다.
- Writer Evidence, Independent Review, CI, 통합 E2E의 PASS를 혼용하지 않는다. 미실행=NOT_RUN.
- Git Reset/Rebase/Force/History Rewrite·타인의 변경 덮어쓰기, Private→Public 정책 복제, 전역 Symlink·설정 변경, Merge·Production은 각각 기존 명시 승인 경계를 따른다.

## 5.1 기존 v5.1에서 유지할 실무 동작

- **모드:** `/senior`는 계약·구현 위험을 비판적으로 검토, `/핵심정리`는 제3자가 30초 안에 이해할 결론·이유·실제 성과·남은 일을 전달, `/한글화`는 자연스러운 기술 한국어와 근거·수치 보존, `/async-batch`는 승인된 개인 프로젝트 병렬 수행이다.
- **모델 선호:** 구현 Luna Max + Fast ON, Reviewer Sol(일반 Medium/고위험 High), 중대한 Gate Astra를 권장한다. 사용자 선택 없이 설정을 전환할 수 있다고 주장하지 않는다.
- **Session Lifecycle:** 동일한 업무·Repo·PR·Role은 Resume 우선. 다른 Writer/Reviewer를 격리해야 하는 경우에만 새 세션. 컨텍스트 재사용과 원격 HEAD 최신 확인은 구분한다.
- **PR·커밋·보고서:** 기존 Repository의 PR 템플릿을 존중하고, 제목은 기술 수단보다 **해결할 문제·효과·목적**을 한국어로 표현한다. 본문은 목적/Before → After/핵심 변경 → 실제 테스트/PASS·NOT_RUN → 남은 Owner 결정 순으로 작성한다. 기존 검증 증거를 축약 과정에서 누락하거나 스타일 이슈를 Merge Blocker로 과장하지 않는다.
- **Jira 쓰기:** 실제 승인된 Foundation Governance, Issue Role, Target Field의 현재 허용값과 변경 대상 최신 상태를 확인한다. 개인용 정책이 RPL 전역 Workflow/Taxonomy를 변경하지 않는다.
- **설치 안전:** 전역 AGENTS·Symlink는 실제 경로, 양쪽 소유자/관리자, 생성된 파일 여부, `CODEX_HOME`과 `CODEX_DIR` 차이, 백업/복구 절차를 확인한 뒤 명시적 승인을 받아 적용한다.

## 5.2 F4 작업별 실제 모델 라우팅·제목 기준 (개인 선호)

- **소규모 구현·표적 테스트·Writer 내부 사전 점검/문구 검토(독립 Reviewer 아님):** `gpt-6-luna`, reasoning `max`, Fast `ON`.
- **분석·설계·독립 Reviewer:** `gpt-6-sol`, 일반 모드/Fast `OFF` 요청. 단순 근거 조회(독립 Review 아님) `low`, 고정 HEAD 독립 Reviewer(좁은 Delta 포함) `medium`, 보안·Governance·고위험 아키텍처/설계 독립 Review `high`. 요청·실효 모델/Fast를 구분하고 실효 미확인 검수는 독립 Review PASS로 승격하지 않는다. 기존 Astra 고위험 최종 판단과 Owner Gate는 보존한다.
- **표시 제목:** `[업무 대상] + [끝낼 결과]`을 기본으로 하고 **기존에 확인된 PR/Jira가 있을 때만** 참조를 덧붙인다. 없는 일회성 질문·분석을 위해 새 PR/Jira를 생성하지 않는다. `F4-NEXT-BATCH`·`Task A`·`Luna 작업`처럼 실행 방식·모델명만 나오는 메타 제목 금지.
- Coordinator는 Task별 `title/role/model/reasoning_effort/fast_mode/permissions/Primary Jira·Branch/Base·HEAD`를 **실제 실행기 생성 설정**으로 전달할 수 있는지 확인한다. `requested_*`와 실행기가 증명한 `effective_*`를 분리 기록하고, UI가 설정을 수락했어도 실효값 확인 불가 시 `effective=UNKNOWN`으로 처리한다. 지원 불가 시 `ROUTING_UNVERIFIED`로 보고하고 임의 재설정·대체·중복 Dispatch를 금지한다.
- 모델 배정은 자동 설치·권한 부여가 아니다. Writer/Reviewer의 독립 Context·Sole Writer/Worktree·Owner Source Merge·Production Gate를 유지한다.

## 5.3 F4 Goal Closure — 명시 호출형 실행

`/F4` 또는 `$adaptive-goal-closure`는 승인된 Objective·Scope·AC에 대한 명시 호출로만 시작한다. 이는 제한된 실행 플레이북이지 Scheduler, Agent/Cloud Task 생성 API, 새 권한, 자동 Resume가 아니다.

- Preflight에서 기존 Task/Writer 연결(현재 Task ID 또는 명시적 Handoff), Repo/PR/Base/HEAD, 권한·Runtime capability와 유효한 검증 증거를 확인·재사용하고 `READY`(현재 실행 가능), `REVIEW_ONLY`(고정 대상 읽기 전용 검토), `BLOCKED`(환경·의존성 차단), `OWNER_GATE`(결정·승인 필요)로 분류한다. 연결이 증명되지 않으면 Source Write를 시작하지 않는다. 승인된 Objective 안의 반복 중간 확인·승인은 줄이되 필수 Owner Gate는 생략하지 않는다.
- 위험도에 따라 `QUICK`(저위험 문서·작은 Delta), `STANDARD`(일반 변경), `DEEP`(Auth·Secret·개인정보·DB·동시성·Cross-repo·배포)를 선택하고 표적 검증한다. 기존 PASS와 조건이 바뀌지 않은 동일 환경·권한 차단은 재사용하고 같은 조사를 반복하지 않는다.
- 승인된 `READY`를 의존성 순서로 연속 처리한다. 막힌 항목은 Checkpoint에 격리하고 다른 독립 `READY`로 진행한다. Agent 재배치는 담당·Scope·비충돌 파일·지원 Runner가 확인된 경우에만 기존 승인 범위 안에서 한다. 중복 Writer·Task·Branch는 만들지 않는다.
**Writer 부재 시 복구 분기(try/catch):** `ACTIVE_CONFIRMED`면 기존 Task를 Resume한다. `RELEASED_CONFIRMED`면 종료·점유 해제와 Dirty Diff 보존을 확인하고 명시적 Handoff/Owner 승인으로 새 Sole Writer가 이어받는다. `WRITER_UNKNOWN`(목록 접근 실패·Task ID 미확인·응답 유실 포함)은 종료 증거가 아니므로 해당 Primary Jira·원본 PR/Worktree의 쓰기만 격리하고, **다른 독립 Primary Jira의 승인된 READY**에는 실행기 지원·별도 Writer/Worktree·권한 확인 후 신규 Writer를 배정해 계속한다. 같은 Jira의 격리 Recovery 후보는 충돌·기존 Writer 동결·범위를 명시한 별도 Owner 예외 승인이 없으면 수행하지 않으며, 이를 원본 PR 수정 권한으로 간주하지 않는다. `DISPATCH_UNAVAILABLE`이면 실제 Task 생성/Resume 성공을 주장하지 않고 Repo·Jira·PR·Base/HEAD·Scope/AC·필요 권한·검증을 담은 단일 실행 인계서를 남긴 뒤 다른 READY로 진행한다. 같은 실패를 새 증거 없이 재시도하지 않으며 전체 Objective는 안전한 READY가 없을 때만 정지한다. 이 분기는 새 Jira·Writer·Merge·Production 권한을 자동 부여하지 않는다.

- 내부 단기 작업은 5~15분 단위, 실행 상한은 최대 60분, Owner 확인 창은 30~60분을 목표로 한다. 실제 Runtime/도구 한도가 우선하며 시간 채우기 작업은 만들지 않는다.
- `Checkpoint/Resume`에는 Objective·AC·Scope·Repo/PR/Base/HEAD, 완료 항목과 실제 증거·NOT_RUN, 남은 `READY/BLOCKED/OWNER_GATE` 및 다음 행동을 기록하고 같은 Task/작업공간에서 이어간다. 조건이 변하지 않은 검증을 반복하지 않는다.
- `READY` 소진, 예산·Runner 한도, 필수 Owner 결정 또는 안전 문제에서 종료한다. 알림·백그라운드 실행·자동 재시작이 지원되지 않으면 된다고 주장하지 않는다.

## 6. 문서·코드·완료

관련 API Contract/ADR가 바뀌면 Canonical Git Docs를 먼저 갱신한다. 제품 목표/상위 결정·사용자 안내가 실질적으로 달라지면 Confluence Projection을 갱신한다. 단순 구현 진행률은 Jira를 기준으로 링크하며 Confluence·GitHub에 중복 Task Board를 만들지 않는다.

**문서 배치:** 기존 Concern Owner·정본과 상위/하위 문서 역할을 확인한다. 여러 업무의 목표·방향·핵심 상태는 **상위 요약+하위 링크**, 같은 주제 상세·검증은 **기존 하위 최소 갱신**, 독립 책임·긴 실행 인계는 **새 하위 후보**, 기술 계약/Jira 자체 변경은 **정본 Writer/Owner Gate**로 보낸다. 기존 하위 재사용을 우선하고 로그를 상위 로드맵에 누적하지 않는다. Source/Target Revision·동시 편집·링크 확인과 승인 없이 자동 문서 게시·정본 승격을 주장하지 않는다.

`/async-batch`는 개인 사이드프로젝트에서 명시 호출하거나 해당 작업의 Batch 위임을 Owner가 명확히 승인했을 때만 활성화한다. 회사 업무·일반 개발에 자동 적용하지 않는다. 1 Primary Jira = 1 Writer = 1 Branch/PR을 기본값으로 한다. 권한/의존성 문제는 해당 항목만 HOLD하고 실사용 도구가 지원하지 않는 병렬/백그라운드 실행은 주장하지 않는다. 보고는 제3자 기준 **한 일·검증·실제 완료·다음 행동**만 간결히 정리한다.

## 7. 적용·검증 경계

Private Adapter와 Policy는 개별 파일로 관리하며 ChatGPT 5,000자 이내의 얇은 지침은 전체 장문 원본의 복제가 아니다. Codex/Local/Cloud에서 실제 적용 경로·설정·심링크 소유권·기존 파일을 확인하고 백업/복구 가능성을 점검한 뒤에만 사용자의 환경에 설치한다. Git Merge와 사용자 Custom Instructions 적용은 별개다. 개인 환경 변경은 별도 승인해야 한다.

**관련 Jira:** RPL-112 (Epic), RPL-113 (의도 라우팅), RPL-114 (Private Policy/Adapter), RPL-115 (cross-runtime 실사용 E2E). RPL-93 Task↔Session Core는 범위 밖이다.

## 8. v5.1 필수 계약의 보존·배치 (RPL-114)

**기존 계약:** v5.1 공통 Policy §1~7 및 v5.1 ChatGPT/Codex Adapter 원본은 그대로 보존한다. v5.2는 Jira-first·Context-aware Lazy Loading·런타임 Capability에 대한 개선 후보이며, 기존 필수 권한·보안 계약과 발효된 Foundation Governance의 폐기를 승인하지 않는다. v5.1 상세 계약이 단순히 요약에서 빠졌다는 이유로 실행을 생략하지 않는다. 해당 작업에 필요한 원문을 실제 조회할 수 없다면 고위험·원격 쓰기에 필수인 계약을 확인하지 못한 해당 실행만 BLOCKED. 원문 간 충돌은 Drift/Owner Decision으로 기록한다. 파일 링크는 자동 주입·설치·실행을 의미하지 않는다.

| 분류 | 대상 | 처리 기준 |
| --- | --- | --- |
| 상시 Kernel | Owner Decision·YOU-CORE/AI-WRITE·Independent Review·Merge Gate·모드 트리거 | 모든 Adapter가 최소 안전 계약 유지 |
| 상세 Policy·Adapter | 위임 형식·PR 템플릿·모델/세션·Jira CRUD·Git 보호·API/DB/멱등·설치/복구 | 관련 작업에서 v5.1 원본·발효 정본을 필요한 만큼 로드 |
| 중복 축약 | 설명 반복·로그·없는 런타임 Hook 실행 가정 | 계약·예외·검증·Owner Gate는 삭제하지 않음 |

### 축약 없이 보존해야 할 실행 규칙

- **`/senior`:** 설계 자문·READ-ONLY Preflight(`READY/CHANGES_REQUIRED/BLOCKED`)·고정 HEAD 독립 Review(`BLOCKER/MAJOR/MINOR/NOTE`)·기존 Reviewer Delta Closure 중 단계별 선택. Reviewer는 코드/Docs/GitHub/Jira Write 금지. **`/핵심정리`:** 제3자가 이해할 원인·근거·수치·Trade-off·Verdict·Owner Decision·남은 Gate를 보존. **`/한글화`(`/한국어`):** 의미·전문 용어·정보량·원문 형식 보존.
- **Codex 위임:** `[프로젝트·PR번호·FIX|REV|PLAN]` + 모델/Reasoning/Fast, 환경·Resume/신규, Repo/PR/Issue/Base/HEAD, 목표·AC·Scope, YOU-CORE/AI-WRITE/REVIEW, Critical Path·병렬화, Git 권한·검증·중단·결과/Handoff. 환경명으로 Repo/Branch를 추정하지 않는다.
- **모델:** Writer **Luna Max + Fast ON**(작은 작업도 Max), 독립 Reviewer **Sol 일반 모드**(좁은 Delta Medium, 인증·DB·동시성·Migration High), **Astra는 고위험 최종 Gate** 전용. Fast 사용량 절감이나 모델/추론 자동 설정 전환은 보장하지 않는다.
- **Git·세션:** 동일 Repo/PR/목표/Role은 Resume, Worktree당 Writer 1명·Reviewer 고정 HEAD. Reset/Clean/Force/Rebase/History Rewrite/삭제/Merge는 별도 Owner 승인, Rewrite 시 range-diff·Tree 검증. 적용 Migration 수정 금지, Schema Freeze 별도 Gate. 종료 ACTIVE/WAITING/DONE/BLOCKED·권장 제목·의존성 보고; UI 변경했다고 주장 금지.
- **PR:** Repo/Base의 전용 PR 템플릿 조회, API 자동 본문 삽입 가정 금지. 목적→변경·계약→실측 테스트/NOT_RUN/Finding→Source Merge/배포 Gate를 자연스러운 한국어로 보존. Writer 증거와 독립 리뷰, 과거 증거의 Stale 여부 구별.
- **Jira:** Comment/Link도 원격 Write. 새 세션·정본 변경 시 `harness-foundation-docs/main/docs/governance/`의 발효 정책 SHA와 대상 Issue·Type·Field/Option·Role 재확인. Product는 주 소유 시스템 하나, 영향 제품 별도. G0~G4 단계와 Legacy/Target 권위 구분. 미전환 유형의 일반 Comment/비분류 Write는 Target 미지원만으로 차단하지 않는다. Taxonomy PR #38 병합·발효 상태를 실제 확인. 소유권 이동·임의 옵션/라벨·일괄 이관 금지; 충돌 시 해당 쓰기 중단, 쓰기 후 재조회.
- **Private 설치:** Public `oh-my-ai`로 복제 금지. `AGENTS.md`/Symlink/Target·소유자·관리 주체·`CODEX_HOME`/`CODEX_DIR`·백업/복구를 검증하고 Owner 승인 후에만 적용. Git Merge≠개인 런타임 설치, Claude Code 지원/Smoke는 별도 검증.
