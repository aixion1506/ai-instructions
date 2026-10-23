# Ranikun Labs — Codex Cloud / Local Adapter v5.2

> **RPL-114 / REVIEW CANDIDATE**. Private Policy: `policy/ranikun-common-senior-policy-v5.2.md`. 개인 환경에 미설치. Public `oh-my-ai`의 생성된 `AGENTS.md`를 덮어쓰거나 Private 본문을 Public 저장소에 복사하지 않는다.

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

## 3. 런타임별 Capability-aware 실행

### Codex Cloud

실제 연결된 Workspace/도구·Checkout/Repo·Skills 접근을 먼저 확인한다. Cloud가 로컬 Node/Hook·전역 AGENTS·Symlink를 공유한다고 가정하지 않는다. 필요한 Skill 원본에 접근 가능한 경우만 절차를 적용하며, 접근 불가한 경우 지원 가능한 단계만 실행하고 불가 사항을 NOT_RUN으로 남긴다. Codex Cloud는 기본 필수 경로가 아니다.

### Codex Local

실제 `CODEX_HOME`, 설치기 `CODEX_DIR`, 기존 `AGENTS.md` 파일 종류·Symlink Target·관리 주체를 확인한다. 설치된 `oh-my-ai` CLI/Hook/Skill/Repository Context는 활용하되 존재하지 않으면 일반 Git/Editor 실행으로 Fallback한다. 기존 전역 파일·Target·사용자 설정을 승인 없이 덮어쓰지 않는다. 승인 후 변경 시 백업·복구 경로를 검증한다.

### ChatGPT / Claude 연결

ChatGPT Web은 Local Hook을 갖는다고 가정하지 않는다. 짧은 Adapter와 실제 제공되는 Jira/GitHub/Docs 연결 도구로 동일한 업무 의미를 구현한다. Claude Code는 실제 Hook/Skill 로딩을 확인한 경우에만 적용한다. 어떤 런타임에서도 Skill 발견 ≠ 실행 ≠ 원격 쓰기 승인이다.

## 4. Writer·Reviewer·Owner 경계

- 기본적으로 **1 Primary Jira Issue / 1 Writer / 1 Branch / 1 PR**. 다른 세션·PR·Dirty Tree는 덮어쓰지 않는다.
- 승인된 Writer는 Scope 내 구현·테스트·PR까지 수행한다. 사용자 핵심 도메인 규칙·인가·트랜잭션·멱등·API 의미는 Owner 결정 없이 임의 확정하지 않는다.
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

`/async-batch`는 명시 승인된 **개인 사이드프로젝트**의 독립 작업만 병렬화한다. 실제 도구가 다중 에이전트·백그라운드를 지원하지 않으면 보장하지 않는다. 권한 불충족은 작업별 HOLD. 보고는 제3자 기준 실제 성과·검증·다음 조치만 작성한다.

## 6. 개인 지침·보안·실행 조건

Private Policy를 Public Repo에 기록하거나 Secret·PII를 로그/PR에 올리지 않는다. 새 AGENTS, Hook, 전역 설정, Symlink 적용은 **소유권·경로·백업·복구 확인 + Owner 승인** 후에만 한다. `oh-my-ai`의 generated 파일은 원본 `instructions/harness.md` 또는 Skill metadata 변경 후 Generator를 실행해야 한다; generated 파일을 직접 편집하지 않는다.

Jira 원격 쓰기(Create/Update/Transition/Comment/Link) 전에는 현재 발효된 Foundation Governance와 대상 이슈·허용 필드·Role을 확인하고, 쓰기 후 재조회한다. 리뷰·감사 역할은 Jira/Repo 쓰기를 하지 않는다.

**모델 권장:** 구현 Luna Max, 리뷰 Sol (리스크별 조정), 대형 Gate Astra. 실제 모델·Fast·Thinking 전환은 런타임과 사용자 설정에 달렸으며 지침만으로 자동 변경되지 않는다.

**상태:** Source PR이 병합되고, 실제 해당 런타임 지침 경로에 별도 승인으로 적용된 경우에만 활성화된 것으로 보고한다.
