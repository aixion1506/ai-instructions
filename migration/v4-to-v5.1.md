# v4 → v5.1 Migration Record

Date: 2026-10-19  
Inputs: the four supplied v4 originals and four supplied v5.1 originals  
Target: private repository aixion1506/ai-instructions

## Evidence and method

All eight supplied files were readable. The v4 files are preserved byte-for-byte under migration/archive/v4/. The original v5.1 README is preserved under migration/archive/v5.1/README-v5.1-source.md. The three active v5.1 policy and adapter files are copied unchanged into policy/ and adapters/.

The comparison used UTF-8 text, headings, and line-level diffs. It identifies textual preservation and changes in the supplied files; it does not claim that the policies were installed or exercised in ChatGPT or Codex.

## Decision by file

| v4 input | v5.1 destination | Decision |
|---|---|---|
| ranikun-common-senior-policy-v4.md | policy/ranikun-common-senior-policy-v5.1.md | Keep all existing sections unchanged; append PR authoring, model routing, spec-to-implementation, and session lifecycle sections |
| ranikun-chatgpt-custom-instructions-v4.txt | adapters/ranikun-chatgpt-custom-instructions-v5.1.txt | Preserve the core safety and working principles while tightening wording; replace model defaults and add PR, spec, and session guidance |
| ranikun-codex-AGENTS-cloud-local-v4.md | adapters/ranikun-codex-AGENTS-cloud-local-v5.1.md | Keep the v4 policy and execution addendum; add PR authoring, model routing, optional spec workflow, and session lifecycle; add the PR-template lookup to Writer responsibilities |
| README-v4.md | README.md plus archived source | Replace the operational README with this repository's ownership, paths, and installation boundaries; preserve v4 source for history |

## Clause comparison

### Retained from v4

The common policy's v4 sections are unchanged in the v5.1 common policy:

- Source of truth and decision principles.
- Proactive Senior review and risk checks.
- Core logic ownership and the /async-batch personal-side-project boundary.
- Review, verification, and release gates.
- Jira Governance and AI CRUD write gates.
- Explanation and documentation principles.

The Codex adapter retains the v4 Cloud/Local environment detection, preflight, Jira write gate, execution modes, infrastructure safety, mode definitions, and Korean reporting. The ChatGPT adapter retains the corresponding /senior, /핵심정리, /한글화, /async-batch, Git/delegation, Jira, verification, and safety boundaries in condensed form.

### Added or changed in v5.1

- **PR authoring:** read the target repository's actual PR template before authoring; use /핵심정리 and /한글화; distinguish writer evidence, independent review, CI, source merge, and deployment gates.
- **Model defaults:** Writer uses Luna Max with Fast ON; Sol is an independent Reviewer with risk-based reasoning. Policy text does not switch UI settings or guarantee lower usage.
- **Spec to implementation:** make the workflow optional for material feature, API, domain, database, or architecture work. Planning approval does not grant implementation authority.
- **Session lifecycle:** resume the same repository, PR, role, and objective where possible; recheck current base, head, permissions, and unfinished work.
- **ChatGPT wording:** v5.1 shortens several sections and updates the model policy. The v4 input is 4,955 Unicode code points; the v5.1 adapter is 4,944, leaving 56 characters under 5,000. The checked-in v5.1 adapter passes the current limit, but has little room for future edits.
- **README status:** the supplied v5.1 README says the private repository has not been created and describes the spec-to-implementation Skill as planned. Repository creation supersedes the first statement. At the audited oh-my-ai checkout, spec-to-implementation is still absent.

### Duplication and authority

The common policy is the normative personal source. ChatGPT and Codex need usable standalone instruction text, so some common rules remain repeated in the adapters. Those repetitions are controlled runtime copies, not separate sources of truth. Changes must start in the common policy and then be reflected in the adapters.

No adapter renderer is introduced in this migration. The included script validates the files and ChatGPT length only. It must not be described as a generator.

Common reusable procedures and Skills remain owned by ranikun-labs/oh-my-ai. Personal policy stays private. No Skill is added to oh-my-ai; no Skill or settings are installed or overwritten.

## Public harness and reusable Skill audit

The audit used the local oh-my-ai checkout at HEAD 7eb130a9ae73e0b740767139e6dcf96415e674d7, branch work, clean at inspection. It contains 32 SKILL.md directories. The inventory includes harness-automation, project-context, git-work-preflight, and handoff-prompt. The proposed senior-review, core-summary, korean-writing, pr-authoring, skill-authoring, and spec-to-implementation Skills are absent from this checkout. harness-automation refers to a writing-skills procedure, but no writing-skills Skill is present. This migration adds none of these Skills.

The root AGENTS.md is generated by make instructions from oh-my-ai instruction sources and Skill metadata. setup.sh defaults CODEX_DIR to $HOME/.codex, renders instructions during install, links the generated Codex AGENTS.md, and installs work-start as an individual Skill. Other shared Skills are not all auto-linked; private Skills are gitignored and are not installed automatically. Its safe_link helper skips an existing destination rather than overwriting it; it can relink a stale dangling symlink. The private policy repository does not run this installer or alter the public harness.

## Audit notes and remaining gates

- The private repository had an initial README-only commit on master at migration start. This change is intended for a separate branch and a PR back to master.
- No PR template exists at .github/PULL_REQUEST_TEMPLATE.md or at the repository root in the inspected base.
- The audited oh-my-ai checkout is at 7eb130a9ae73e0b740767139e6dcf96415e674d7. Its setup.sh defaults CODEX_DIR to $HOME/.codex, links its generated AGENTS.md through a conflict-aware helper, and installs only selected runtime components. It does not use CODEX_HOME directly.
- This change does not install policy into ChatGPT, Codex Cloud, Codex Local, or $CODEX_HOME/AGENTS.md.
- Before any later installation, decide how private policy should coexist with the public harness's generated global Codex instructions, then verify the actual Cloud and Local instruction paths.
