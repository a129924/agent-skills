# Requirements: skills-canonical-positioning

## Status

- **Status**: frozen for technical translation
- **Topic**: `skills-canonical-positioning`
- **Date**: 2026-06-02
- **Scope**: planning baseline for repository-positioning correction limited to four core documents

## Problem Statement

The repository still contains positioning wording that can be read as if
Copilot-era surfaces define repository truth. The missing outcome is a
repo-visible plan that corrects the positioning model without reopening broader
skill-contract or workflow-contract migration.

The corrected model for this topic is:

1. `skills/` is the repository's current canonical truth for skill content.
2. `.github/copilot-instructions.md` is a GitHub/Copilot compatibility surface,
   not the repo-wide policy owner.
3. `.github/skills/...`, `.codex/skills/...`, and other `.<platform>/...`
   layouts may exist, but they are not to be edited or re-described in this
   topic.
4. This topic must stop at core positioning wording in four files and must not
   expand into skill-bundle contracts, workflow guides, runtime/tooling, or
   directory migration.

## Evidence Read

The baseline uses the following repo-visible evidence:

- `AGENTS.md`
- `docs/repo-positioning.md`
- `.github/copilot-instructions.md`
- `README.md`

## Actors

| Actor | Role | What must be true after this topic |
| --- | --- | --- |
| Repository maintainer | Owns repo positioning | Can read four core documents and reach one clear authority order |
| Human reader | Needs a quick repo summary | Can read `README.md` and not infer that Copilot surfaces own repository truth |
| Platform-specific consumer | Reads `.github/copilot-instructions.md` | Can see that the file is compatibility guidance and defers to canonical governance |
| Future implementer | Executes the eventual file edits | Has explicit editable scope and forbidden scope without making scope decisions |

## Frozen Requirements

| ID | Requirement | Acceptance signal |
| --- | --- | --- |
| R1 | `AGENTS.md` must state that `skills/` is the current canonical truth. | Another agent can read `AGENTS.md` alone and not conclude that `skills/` is target-only. |
| R2 | `docs/repo-positioning.md` must define one current authority model rather than a transition-era split between current state and target architecture. | The file presents `skills/` as current truth and `.<platform>/...` as compatibility/projection only. |
| R3 | `.github/copilot-instructions.md` must be explicitly bounded to GitHub/Copilot compatibility guidance. | The file no longer reads as repo-wide policy ownership. |
| R4 | `README.md` must summarize the same canonical-truth model as the other three files. | A human reader reaches the same positioning conclusion from `README.md` as from `AGENTS.md`. |
| R5 | The editable scope for this topic is only the four core files. | The eventual plan names exactly four editable files and treats anything else as out of scope. |
| R6 | `.github/skills/**`, `.codex/skills/**`, and `skills/**` descriptions are frozen for this topic and must not be edited. | The eventual plan names those paths as forbidden scope. |
| R7 | This topic must not turn into contract migration, workflow-guide repair, or runtime/tooling work. | The eventual plan excludes `agent-skill-*`, workflow guides, runtime/tooling, installer, sync, and directory-move work. |

## Resolved Contradictions

### C1 - Canonical truth versus platform guidance

- Conflict: Copilot-era wording can be read as if platform surfaces still define
  repository truth.
- Resolution: only the four core positioning documents are corrected; platform
  surfaces are described from those documents as compatibility only.

### C2 - Positioning correction versus broader migration

- Conflict: core positioning wording could tempt downstream edits in
  `.github/skills/**`, `.codex/skills/**`, or workflow contracts.
- Resolution: this topic explicitly forbids those edits and treats them as
  separate topics.

## Explicit Assumptions

- A1: `skills/` is already the desired current truth, even if other repo files
  still contain older transition-era descriptions.
- A2: It is acceptable for this topic to correct the four core documents first
  while leaving broader contract alignment for later topics.
- A3: Historical migration notes may remain historical as long as the four core
  files clearly outrank them.

## Extreme-Boundary Checks

| Boundary | Requirement result |
| --- | --- |
| A reader opens only `README.md` | The reader must still conclude that `skills/` is current truth |
| A GitHub/Copilot consumer opens only `.github/copilot-instructions.md` | The file must defer to `AGENTS.md` and `docs/repo-positioning.md` |
| An implementer sees contradictory old wording in `.github/skills/**` | The implementer must treat that as forbidden scope, not as permission to expand this topic |
| A future topic wants contract migration | That work must be routed to a separate topic rather than folded into this one |

## Success Signals

This topic is frozen successfully when:

1. the four core files can be updated to one consistent positioning model,
2. the eventual topic plan names only those four files as editable scope,
3. forbidden scope explicitly includes `.github/skills/**`, `.codex/skills/**`,
   and `skills/**`, and
4. no downstream implementer needs to infer whether broader contract migration
   is allowed.
