# aixion1506/ai-instructions

Private source of truth for personal AI work preferences and safety policy.

This repository owns the personal policy. The public ranikun-labs/oh-my-ai repository owns the reusable harness, Skills, and installation/runtime tools. Personal/private AI policy and settings must not be copied, committed, or pushed into tracked files of a public repository.

## v5.2 — Lean cross-runtime proposal (RPL-114)

**Status:** Review candidate on a feature branch; v5.1 remains the applied reference until a separate source merge and explicit runtime installation. This PR does **not** modify live ChatGPT Custom Instructions, Codex/Claude global files, runtime hooks, or the public oh-my-ai repository.

| Layer | v5.2 candidate | Design |
| --- | --- | --- |
| Common normative source | `policy/ranikun-common-senior-policy-v5.2.md` | Jira-first development; context reuse; risk-aware verification and permissions |
| ChatGPT Web | `adapters/ranikun-chatgpt-custom-instructions-v5.2.txt` | Thin always-on instructions; under 3,500 Unicode code points, hard max 5,000 |
| Codex Cloud / Local | `adapters/ranikun-codex-AGENTS-cloud-local-v5.2.md` | Capability-aware execution; local hooks optional, not assumed in Cloud/Web |
| Runtime-neutral reusable Skills | `ranikun-labs/oh-my-ai` | Shared process/Skill source and supported local execution, not the private policy authority |
| Work trace | Jira `RPL-114` | Source, review, and runtime-installation gates tracked separately |

**Common workflow:** Check/reuse relevant Jira Issue → Design → Analyze applicable Canonical Docs/Code → Implement → Risk-appropriate review → Merge → Jira completion evidence. Only fetch needed Skills/Docs when context is missing, stale, or changed; always refresh mutable targets immediately before a write. Docs repo and Confluence are updated when architecture/contract or important product decisions materially change, not at every step.

**Boundaries:** GitHub source PR merge is not a ChatGPT/Codex runtime settings change. Previous v5.1 policy and adapters are kept unchanged for comparison and rollback. If a runtime cannot fetch private sources or use local hooks, use its connected tools/manual procedure and state the gap; never claim silent automatic injection.

**Validation:** Run `python3 scripts/validate-policy.py` on this PR branch. It checks v5.2's required behavior, ChatGPT character budget, and continued presence of v5.1. Git/CI source validation does not prove runtime installation.

## Policy ownership

| Layer | Owner | Role |
|---|---|---|
| Common personal policy | policy/ranikun-common-senior-policy-v5.1.md | Normative source for shared judgment, review, governance, and writing principles |
| ChatGPT adapter | adapters/ranikun-chatgpt-custom-instructions-v5.1.txt | Standalone text for the ChatGPT Custom Instructions field |
| Codex adapter | adapters/ranikun-codex-AGENTS-cloud-local-v5.1.md | Codex-specific instruction text for Cloud and Local contexts |
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

The v5.1 files remain the current applied reference. v5.2 is proposed, not installed or activated. The supplied v4 files and original v5.1 README are archived under migration/archive/. The v5.1 README described the private repository as not yet created; that status is superseded by this repository.

The source documents identify spec-to-implementation as a planned Skill. In the audited oh-my-ai checkout, that Skill is absent; do not assume that a GitHub policy file installs or invokes it. Reusable procedures remain the public harness's responsibility.

No runtime installation or settings update is recorded by this change.
