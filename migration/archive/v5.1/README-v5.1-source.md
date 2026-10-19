# Ranikun Labs AI Instructions — Cloud/Local v5 (Optional Async Batch + Jira Governance Gate)

## 적용 범위

- 공통 Senior Policy는 관리용 원본이며 ChatGPT와 Codex 전용 지침에 핵심 정책을 이미 내장했습니다. **서로 더해 붙이지 않습니다.**
- ChatGPT: `ranikun-chatgpt-custom-instructions-v5.1.txt`만 개인 지침에 적용합니다.
- Codex Cloud / Codex CLI / IDE: `ranikun-codex-AGENTS-cloud-local-v5.1.md`의 내용을 해당 Repository의 `AGENTS.md`에 병합해 적용합니다. Codex가 실제로 해당 경로를 읽는지 확인하세요.
- 로컬에서 모든 Repository에 공통 적용하려면 `$CODEX_HOME/AGENTS.md` (기본 `~/.codex/AGENTS.md`)에 둘 수 있습니다. **전역과 프로젝트 양쪽에 같은 전문을 복제하지 마세요.** 프로젝트별 기존 AGENTS.md와 하위 Override를 검토해야 합니다.
- Codex Cloud Environment 선택은 `AGENTS.md` 배포가 아닙니다. Cloud Workspace에 파일이 실제 있는지 검증해야 합니다.

## 네 가지 요청 모드

`/senior`: 위험도별 설계 검토·Preflight·독립 PR Review·Agent Finding Delta/Closure 자동 선택.
`/핵심정리`: 제3자 보고서형 정리; 디테일·근거·수치 보존.
`/한글화` (`/한국어` 별칭): 내용 보존형 자연스러운 기술 한국어.
`/async-batch` (`/Async-Batch` 별칭): **개인 사이드프로젝트 전용 선택 모드**. Issue별 독립 Writer·Branch·PR로 Fan-out하고 독립 Reviewer·Owner 일괄 판단으로 Fan-in.

이는 **대화에서 해석하는 텍스트 키워드**입니다. 로컬 CLI의 내장 Slash Commands로 등록하거나 메뉴에 나타나게 하지 않습니다. `/senior` 단독 입력이 명령 파서에 막히면 `이 변경을 /senior 방식으로 검토해줘`, 또는 `senior: 검토해줘` 같은 일반 문장으로 입력합니다.

`korean-humanizer`의 GitHub 링크는 참고 지침입니다. Cloud/Local에 해당 Skill이 자동 설치되는 것이 아니며, 파일 접근이 불가능하면 전용 지침에 내장된 한국어 원칙으로 처리합니다.

## 개인 사이드프로젝트용 Async Batch — 활성화와 안전성

- **기본값 아님:** 회사 업무·일반 개발에서는 `/async-batch`를 적용하지 않습니다. 개인 사이드프로젝트에서 명시적 호출 또는 해당 작업에 대한 명확한 Owner Batch 위임이 필요합니다. Ranikun Labs 등의 이름만으로 개인 프로젝트임을 자동 판정하지 않습니다.
- **Fan-out:** Owner가 SSOT·승인 Scope·Acceptance·Dependency Graph를 정의한 뒤, 원칙적으로 `1 Primary Issue = 1 Writer = 1 Branch/Worktree = 1 PR`로 분리합니다. 실제 도구가 지원할 때에만 병렬 Agent 실행을 시도합니다.
- **Writer:** 권한을 따로 명시한 범위에서 구현·테스트·Finding 수정·PR/Evidence까지 진행합니다. 위험·Owner Decision·차단 상황은 해당 작업만 분리합니다.
- **Fan-in:** PR별 고정 HEAD 독립 리뷰 후 상태·테스트·통합 충돌·추천 Merge 순서를 일괄 확인합니다. Writer PASS, Reviewer PASS, Combined Tree/Release PASS는 다릅니다.
- **별도 승인:** Git Commit/Push는 작업별 명시적 권한이 필요합니다. Merge, 운영 배포, DB Cutover, Secret/권한 확대, 파괴적 Git 작업은 별도 Owner Gate입니다.
- **설치 유의:** README·개인 지침·AGENTS 파일을 생성해도 클라우드 세션, 다른 저장소, 기존 Local 지침에 자동 반영되지는 않습니다.

## Jira Governance 확인 방식

- **정본 SSOT:** GitHub `ranikun-labs/harness-foundation-docs/main`의 승인·발효된 `docs/governance/portfolio-work-management-governance.md` 및 `docs/governance/ai-session-governance.md`; 신규 `docs/governance/jira-field-taxonomy.md`는 **승인·발효된 이후에만** 공식 허용값으로 사용합니다. PR #38은 최초 Draft/미승인 제안이므로 사용 시 최신 상태를 확인합니다.
- **읽기와 쓰기 구분:** Jira 읽기·일반 코드 개발에는 매번 정책 전문을 읽지 않습니다. **Jira 원격 쓰기 직전**에 적용 중인 문서 SHA와 Jira Field/Option·대상 Issue·권한을 검증합니다. 새 세션/정책 변경/일괄 작업에서 정본을 다시 읽습니다.
- **필수 권한:** Product=주 소유 시스템 1개, Component/Concern은 **적용된** Taxonomy가 허용하는 옵션만 사용합니다. Reviewer/Portfolio Audit은 Jira 쓰기 불가. 소유권 이전·삭제·대량 작업·Jira Admin 적용은 별도 Owner 승인 대상입니다.
- **중단 조건:** GitHub 정본에 접근할 수 없거나 실제 Jira 설정과 충돌하면 WRITE STOP. 승인되지 않은 Product 9개 옵션을 자유 입력 Labels에 먼저 써 넣지 않습니다.
- **배포 범위:** ChatGPT에는 개인 지침 전문, Codex에는 저장소의 `AGENTS.md` 또는 충돌 없는 로컬 전역 지침을 적용합니다. GitHub 문서 PR을 작성하거나 GitHub 저장소 하나에 `AGENTS.md`를 추가해도 다른 세션·Repo에 자동 설치되지는 않습니다.

## Cloud와 로컬 차이

- Cloud: Carelog/Finance/Ranikun-labs 환경 선택 + 실제 Repo/PR/Checkout + GitHub 접근·권한 확인.
- Local: 실제 Git Root/Branch/Worktree/Toolchain 확인; Cloud Environment 선택을 요구하지 않음.
- 양쪽: Repo의 Owner/Core 정책·READ-ONLY Reviewer·Git 안전·Delta/Release Gate 동일.

## 설치 확인용 테스트

1. Codex에 `현재 적용된 AGENTS.md 경로와 Cloud/Local 환경을 읽기 전용으로 확인해줘`.
2. `이 변경을 /senior 방식으로 READ-ONLY Preflight 해줘; 수정하지 마`.
3. `이 결과를 /핵심정리로 설명해줘. SHA/수치 생략 금지`.
4. `아래 문장을 /한글화 기준으로 다듬어줘. 정보량 보존`.
5. `개인 사이드프로젝트에서 /async-batch 모드의 Fan-out/Fan-in 계획만 READ-ONLY로 작성해줘; 구현·원격 쓰기는 하지 마`.
6. `READ-ONLY로 Jira Governance 문서의 정본 SHA/승인 상태와 PR #38의 최신 승인 여부를 구분해줘; Jira를 수정하지 마`.

위 확인은 실질적인 코드 변경 없이 동작을 확인하는 용도입니다. 실제 독립 리뷰 품질은 고정 PR/HEAD와 실제 테스트 증거로 별도 검증해야 합니다.

## v5 — PR 작성 방식과 모델 기본값

- **형식:** 저장소별 `.github/PULL_REQUEST_TEMPLATE.md` 또는 적절한 유형별 템플릿이 PR 구조의 정본. 아직 병합되지 않은 템플릿은 기본 브랜치에 적용된 것이 아닙니다.
- **원칙:** PR 설명은 `/핵심정리`(제3자가 이해하는 설명·검증 근거)와 `/한글화`(자연스러운 기술 한국어)를 **문서 작성 정책으로 조합**합니다. 이 두 키워드는 실행 가능한 패키지/Skill이 아닙니다.
- **실행:** Codex/ChatGPT가 API로 PR 생성·갱신하는 경우 템플릿 자동 삽입을 가정하지 말고 **조회→내용 작성→검증→제출**합니다. 기존 상세 증거를 보존하고 Writer/Reviewer/CI, Source Merge/Production Gate를 분리합니다.
- **Skill 분리:** 지금은 `pr-authoring`을 별도 Skill로 만들지 않습니다. 템플릿은 형식, `AGENTS.md`는 절차, `/핵심정리`·`/한글화`는 재사용 작성 원칙으로 충분합니다. 필요해지면 검증 자동화용 Skill을 도입할 수 있습니다.
- **모델:** Writer는 **Luna Max / Fast ON**, Reviewer는 **Sol 일반 모드(위험도별 추론 수준)**를 기본 추천. Fast의 토큰 사용량 감소는 보장하지 않으며, 지침만으로 UI 설정이 변경되지는 않습니다.
- **설치:** 파일을 만든 것만으로 GitHub·Codex·ChatGPT 새 세션에 자동 배포되지 않습니다. `AGENTS.md`는 저장소 정책과 병합, ChatGPT 개인 지침은 사용자가 설정에 반영해야 합니다.

## v5.1 — 실행 상태와 적용 구분 (2026-10-19)

- **Spec-to-Implementation:** 큰 기능·계약 변경의 Idea → AC/SSOT → Owner Decision → 승인된 Writer → 독립 Reviewer → PR Gate를 선택형으로 사용한다. `oh-my-ai` 35번째 Skill은 아직 **계획 단계**이며 설치·실행된 것이 아니다.
- **Session Lifecycle:** 같은 Repo/PR/역할/목표는 Resume 우선, 최종 결과를 남긴 DONE 세션만 Archive 권고한다. 이름 변경·보관을 지침만으로 자동 실행할 수 없다.
- **현재 적용 상태:** GitHub 조직 PR 정책은 13개 PR의 독립 검수 PASS 이후에도 **미병합** 상태(별도 Owner 승인 필요). 개인 Private Policy Repo는 미생성, ChatGPT Custom Instructions UI 설정과 Codex Cloud/Local 전역 적용은 미확인이다.
- **정본 분리:** 개인 Private Repo는 향후 개인 정책·v5.1 원본의 SSOT로, `ranikun-labs/oh-my-ai`는 기존 재사용 Skill과 설치/검증 Runtime으로 유지한다. `oh-my-ai`가 `$CODEX_HOME/AGENTS.md`를 소유하는 동안 다른 설치기가 해당 경로를 덮어쓰지 않는다.
- **Platform CI:** 최신 #30+#33+#32 Static Tree PASS이지만 Build/E2E는 NOT_RUN. 기존 Cloud는 Java/JDK·Gradle/Docker 권한 미충족, GitHub Actions 비용·정책 Gate 미확인 상태다. 같은 환경에서 불필요한 재실행을 반복하지 않는다.
- **개인 지침 길이:** 실제 v5.1 ChatGPT 지침 문자 수는 이 README의 수치가 아니라 생성된 파일을 직접 검사해 확인한다.
