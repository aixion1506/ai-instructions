# aixion1506/ai-instructions

Private source of truth for personal AI work preferences and safety policy.

This repository owns the personal policy. The public ranikun-labs/oh-my-ai repository owns the reusable harness, Skills, and installation/runtime tools. Personal policy files must not be copied into the public repository.

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
- **Global Codex path:** do not replace an existing global AGENTS.md owned or managed by oh-my-ai. At the audited oh-my-ai revision, setup.sh manages the Codex link under the directory selected by CODEX_DIR (default $HOME/.codex), at AGENTS.md, and uses a conflict-aware link helper. It does not read CODEX_HOME directly. This private repository does not install to either path. A future shared global setup needs an explicit integration design that preserves the public harness source and its generated instructions.

## Current scope

The v5.1 files are the active policy set. The supplied v4 files and original v5.1 README are archived under migration/archive/. The v5.1 README described the private repository as not yet created; that status is superseded by this repository.

The source documents identify spec-to-implementation as a planned Skill. In the audited oh-my-ai checkout, that Skill is absent; do not assume that a GitHub policy file installs or invokes it. Reusable procedures remain the public harness's responsibility.

No runtime installation or settings update is recorded by this change.
