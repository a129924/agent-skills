# codex-readability-baseline requirements baseline

Status: LOCKED
Topic: `codex-readability-baseline`
Base branch: `dev`

## Problem statement

After PR #84 merged the Codex spec-worktree artifacts back into `dev`, the
repository has first-wave evidence about which skills are projected into
`.codex/skills/` and which skills were already promoted into `skills/`.

What is still missing is a repo-visible baseline that separates:

- move-to-`skills/` status
- Codex readability through `.codex/skills/`
- same-name dual-surface cases that should be collected but not force-resolved
  in this topic

## Goal

Produce a branch-local baseline that records first-wave skill status across
four fixed dimensions:

- `move_status`
- `codex_readability`
- `source_authority`
- `follow_up`

This topic exists to make low-risk migration evidence explicit without
performing skill content migration or canonical-authority enforcement.

## Frozen candidate set

The baseline is frozen to the first-wave projected skills listed in
`.codex/skills/provenance.md`:

- `business-intent-alignment`
- `business-to-technical-translation`
- `plan-creator`
- `plan-reviewer`
- `agent-skill-creator`
- `agent-skill-reviewer`
- `agent-skill-template`
- `git-commit-convention`
- `git-branch-naming`
- `git-post-merge-workflow`
- `worktree-manager`

## Actors

- Human decision-maker
- Planning / analysis agent
- Reviewer if a plan-review gate is later requested

## Measurable requirements

| ID | Requirement | Observable result | Pass rule |
| --- | --- | --- | --- |
| R1 | Every first-wave skill has all 4 baseline fields recorded | The report includes one row per candidate with `move_status`, `codex_readability`, `source_authority`, and `follow_up` | No candidate is omitted or left implicit |
| R2 | Same-name skills are not silently declared migrated | Same-name skills are marked `same-name-pass` and routed to `divergence-review` | No same-name skill is mislabeled as low-risk complete |
| R3 | Readability and move state remain separate | A skill may be `not-moved + readable`, and the report keeps both fields explicit | The baseline does not collapse two dimensions into one migration verdict |
| R4 | Provenance-backed Codex readability is evidence-based | `readable` is used only when `.codex/skills` projection exists and aligns with `.codex/skills/provenance.md` | No readability verdict depends on intuition-only wording |
| R5 | Higher-risk follow-up is surfaced instead of hidden | Skills that are not low-risk complete are routed to `divergence-review`, `projection-fix`, or `runtime/tooling-blocker` | No candidate is falsely left as `none` when follow-up is required |

## Classification rules

- `move_status`
  - `moved`: upstream canonical exists under `skills/<skill-name>/`
  - `not-moved`: no upstream canonical exists under `skills/<skill-name>/`
  - `same-name-pass`: both `skills/` and `.github/skills/` exist for the same
    candidate; this topic records but does not resolve the dual-surface state
- `codex_readability`
  - `readable`: `.codex/skills/<skill-name>` exists, points to the intended
    upstream path, and the mapping is covered by `.codex/skills/provenance.md`
  - `not-readable`: no usable `.codex/skills/<skill-name>` projection exists
  - `stale-projection`: projection exists but provenance or target verification
    is not trustworthy
- `source_authority`
  - `skills/`
  - `.github/skills/`
  - `mixed/unresolved`
- `follow_up`
  - `none`
  - `divergence-review`
  - `projection-fix`
  - `runtime/tooling-blocker`

## Non-goals

- skill content migration
- runtime/tooling blocker repair
- canonical-authority freeze
- second-wave `.codex/skills` projection
- creator/reviewer/template redesign

## Assumptions and blockers

- `.codex/skills/README.md` and `.codex/skills/provenance.md` are the fixed
  source rule and first-wave mapping evidence for this topic.
- `docs/migration/migration-runway-checklist.md` and the five migration reports
  remain valid supporting evidence for move and residue interpretation.
- If any projected skill cannot be matched to its expected upstream path or
  provenance row, mark it `stale-projection` and route it to `projection-fix`
  instead of repairing the projection in this branch.
