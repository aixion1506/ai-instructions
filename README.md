# aixion1506/ai-instructions

Private source of truth for personal AI work preferences and safety policy.

This repository owns the personal policy. The public ranikun-labs/oh-my-ai repository owns the reusable harness, Skills, and installation/runtime tools. Personal/private AI policy and settings must not be copied, committed, or pushed into tracked files of a public repository.

## v5.2 — Lean cross-runtime source (RPL-114)

**Status:** Private PR #2 was Rebase Merged into `master` at `d9e960f7e3e4d8113fbd9b9d2d7275421c1cc719` on 2026-10-30. The source merge does not install runtime settings. The applied policy version for ChatGPT, Codex, and Claude is **UNKNOWN**; Runtime Installation and Smoke are **NOT_RUN**. This source merge did not modify live ChatGPT Custom Instructions, Codex/Claude global files, runtime hooks, or the public oh-my-ai repository.

| Layer | v5.2 merged source | Design |
| --- | --- | --- |
| Common normative source | `policy/ranikun-common-senior-policy-v5.2.md` | Jira-first development; context reuse; risk-aware verification and permissions |
| ChatGPT Web | `adapters/ranikun-chatgpt-custom-instructions-v5.2.txt` | Thin always-on instructions; under 3,500 Unicode code points, hard max 5,000 |
| Codex Cloud / Local | `adapters/ranikun-codex-AGENTS-cloud-local-v5.2.md` | Capability-aware execution; local hooks optional, not assumed in Cloud/Web |
| Runtime-neutral reusable Skills | `ranikun-labs/oh-my-ai` | Shared process/Skill source and supported local execution, not the private policy authority |
| Work trace | Jira `RPL-114` | Source, review, and runtime-installation gates tracked separately |

**Common workflow:** Check/reuse relevant Jira Issue → Design → Analyze applicable Canonical Docs/Code → Implement → Risk-appropriate review → Merge → Jira completion evidence. Only fetch needed Skills/Docs when context is missing, stale, or changed; always refresh mutable targets immediately before a write. Docs repo and Confluence are updated when architecture/contract or important product decisions materially change, not at every step.

**Boundaries:** PR #2 Source Merge changes repository files only; it does not update ChatGPT settings, Codex/Claude configuration, runtime hooks, or automatically inject policy. The supplied v5.1 Policy and ChatGPT/Codex Adapter originals remain byte-for-byte preserved for traceability and rollback. If a runtime cannot fetch private sources or use local hooks, use its connected tools/manual procedure and state the gap; never claim silent automatic injection.

**Validation:** Run `python3 scripts/validate-policy.py` on the branch under review. It checks v5.2's required behavior, ChatGPT character budget, and the exact v5.1 original Git blob identities. Python/CI source validation does not identify the policy version applied in any runtime or prove runtime installation.

## Policy ownership

| Layer | Owner | Role |
|---|---|---|
| Common personal policy | policy/ranikun-common-senior-policy-v5.2.md | Normative source for the merged v5.2 policy on shared judgment, review, governance, and writing principles |
| ChatGPT adapter | adapters/ranikun-chatgpt-custom-instructions-v5.2.txt | Standalone ChatGPT Custom Instructions source; actual applied version is UNKNOWN |
| Codex adapter | adapters/ranikun-codex-AGENTS-cloud-local-v5.2.md | Codex Cloud/Local instruction source; actual runtime loading is UNKNOWN |
| Public harness and reusable Skills | ranikun-labs/oh-my-ai | Runtime, reusable procedures, shared Skills, and their installation/validation |
| Migration evidence | migration/ | v4 originals, the supplied v5.1 README, and the v4-to-v5.1 decision record |

The adapters contain some repeated rules so each runtime can receive a self-contained instruction. They are downstream adapters, not independent policy authorities. Update the common source first, then review and update both adapters where the shared rule applies. Preserve platform-specific behavior in the corresponding adapter.

The current adapters are maintained text files copied from the supplied v5.1 originals. This repository does not claim they are generated. scripts/validate-policy.py checks required files and limits; it does not render adapters.

## Files and updates

- policy/ contains the normative personal policy.
- adapters/ contains deployable ChatGPT and Codex text.
- migration/archive/ preserves the supplied source files for traceability.
- migration/v4-to-v5.1.md records retained, changed, and added policy.
- scripts/validate-policy.py checks file presence, required policy markers, and the ChatGPT character limit.

When changing policy:

1. Edit the common source.
2. Update applicable adapters and record any deliberate difference.
3. Run python3 scripts/validate-policy.py.
4. Review the exact Cloud and Local instruction paths before applying anything.

## Applying the adapters

No automatic installer is included. This repository contains policy text and a validator only; it does not change ChatGPT settings, Codex settings, global instruction files, or the public harness.

- **ChatGPT:** copy the ChatGPT adapter into the intended Custom Instructions field. The validator counts Unicode code points in the checked-in text; keep it below the 5,000-character limit.
- **Codex Cloud and Local:** apply the Codex adapter only through an instruction layer chosen by the user. Cloud and Local can use different paths, so confirm the active path in each environment.
- **Global Codex path:** before applying any adapter, inspect the active path, existing AGENTS.md type, symlink and resolved target, and each owner's/manager's and generated-file status. Do not overwrite or relink oh-my-ai-generated or managed global files or targets. If ownership is unclear or a conflict exists, stop pending an integration design and Owner approval. Before an Owner-authorized apply, back up the file, target, and symlink metadata; verify a restore path and never restore over later changes. At the audited oh-my-ai revision, setup.sh manages the AGENTS.md link under CODEX_DIR (default $HOME/.codex) and does not read CODEX_HOME. Codex's actual CODEX_HOME may point elsewhere; verify the runtime path, installer setting, and revision. This repository changes neither path and establishes no global installation method.

## Current scope

The supplied v5.1 Policy, ChatGPT Adapter, and Codex Adapter originals remain byte-for-byte preserved. PR #2 Rebase Merged v5.2 into `master`; this is a source state only and does not establish the version applied in ChatGPT, Codex, or Claude. Applied policy versions are UNKNOWN; Runtime Installation and Smoke are NOT_RUN. The supplied v4 files and original v5.1 README are archived under migration/archive/. The v5.1 README described the private repository as not yet created; that status is superseded by this repository.

The source documents identify spec-to-implementation as a planned Skill. In the audited oh-my-ai checkout, that Skill is absent; do not assume that a GitHub policy file installs or invokes it. Reusable procedures remain the public harness's responsibility.

Runtime installation and Smoke are NOT_RUN; this README/source update changes no ChatGPT, Codex, or Claude settings.

## RPL-114 v5.1 → v5.2 정책 보존 기준

v5.2는 기존 v5.1의 필수 계약을 삭제하는 새 정책이 아니라, Jira-first·맥락 재사용·런타임별 실행 차이를 추가하는 **병합된 정책**이다. v5.1 공통·ChatGPT·Codex 원본은 Git blob SHA로 보존한다. v5.2 Policy §8에서 상시 Kernel, 위험 기반 상세 조회, 단순 중복 제거를 구분한다. ChatGPT 상시 지침은 3,000~3,500자 범위이며 Codex의 실행 세부 계약은 별도 Adapter에 둔다.

Validator는 원본 SHA와 양 버전의 핵심 표지·문자 수를 검사하는 **구조 검증**이다. Python 실행 성공만으로 정책 의미 동등성, 독립 Review, ChatGPT/Codex/Claude 실제 설치를 입증하지 않는다. Native Validator 결과와 런타임 Smoke를 별도 기록한다.
