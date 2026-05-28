# Agent Skill Migration Sequencing Result

## Purpose

Freeze a repo-visible next-wave sequencing view for agent-skill migration work
without performing any skill move, shared-governance edit, or workflow-baseline
implementation.

This artifact uses only existing repo-visible planning and migration artifacts
as evidence. It is the creator-stage output for the
`agent-skill-migration-sequencing` topic.

## Evidence Basis

- `analysis/agent-skill-migration-sequencing/requirements.md`
- `plan/agent-skill-migration-sequencing/agent-skill-migration-sequencing.plan.md`
- `plan/agent-skill-migration-sequencing/agent-skill-migration-sequencing.step.md`
- `docs/migration/migration-runway-checklist.md`
- `docs/migration/codex-readability-baseline.md`
- `docs/migration/codex-migration-direct-move-report.md`
- `docs/migration/codex-migration-copilot-residue-medium-report.md`
- `docs/migration/codex-migration-copilot-residue-high-report.md`
- `docs/migration/codex-migration-copilot-specific-report.md`
- `docs/migration/worktree-manager-move.md`
- `docs/migration/agent-skill-contract-surface-move.md`
- `docs/migration/plan-step-tracker-move.md`
- `analysis/planning-spine-divergence-review/requirements.md`
- `plan/planning-spine-bounded-remediation/planning-spine-bounded-remediation.plan.md`
- `plan/git-post-merge-workflow-enhancement/git-post-merge-workflow-enhancement.plan.md`
- `docs/repo-positioning.md`

## Next-Wave Queue

Rows are ordered for scheduling. The `primary_classification` field is the main
queue gate. `gap_classes` may be empty when the current evidence already gives a
bounded execution contract.

| Queue order | Topic / candidate | Primary classification | Gap classes | Evidence basis | Scheduling note |
| --- | --- | --- | --- | --- | --- |
| 1 | `planning-spine-bounded-remediation/ready-subset` | `can_start_now` | `sequencing-gap` | `plan/planning-spine-bounded-remediation/planning-spine-bounded-remediation.plan.md`, `analysis/planning-spine-divergence-review/requirements.md`, `docs/migration/codex-readability-baseline.md` | The ready subset is already decomposed into exact remediation units and exact editable files. It is queueable only as the bounded ready subset, not as a direct same-name canonicalization of `plan-creator` / `plan-reviewer`, because `diff -qr` still shows multi-file drift on both pairs. |
| 2 | `git-post-merge-workflow-enhancement` | `can_start_now` | `sequencing-gap` | `plan/git-post-merge-workflow-enhancement/git-post-merge-workflow-enhancement.plan.md`, `docs/migration/codex-migration-copilot-residue-high-report.md` | The redesign topic already has a bounded plan, exact writable paths, and an explicit post-merge stop condition. It should be sequenced after the planning-spine ready subset because it is a redesign lane, not a low-risk copy lane. |
| 3 | `agent-skill-active-path-transition/contract-surfaces` | `after-workflow-baseline` | `bootstrap-artifact-gap`, `step-gap`, `summary-gap`, `close-semantics-gap`, `sequencing-gap` | `docs/repo-positioning.md`, `docs/migration/agent-skill-contract-surface-move.md`, `docs/migration/codex-migration-copilot-residue-medium-report.md` | The direct copy result already exists for `agent-skill-creator`, `agent-skill-reviewer`, and `agent-skill-template`, but the current active authored/reviewed path still remains `.github/skills/`. A later active-path transition should wait for the workflow-baseline topic to freeze step / summary / close semantics before a new bounded cutover topic is authored. |
| 4 | `planning-spine-bounded-remediation/blocked-subset` | `shared-governance-blocked` | `shared-governance-gap`, `sequencing-gap` | `plan/planning-spine-bounded-remediation/planning-spine-bounded-remediation.plan.md` | The blocked subset still needs human policy lock on fallback contract authority, review-basis authority, and reviewer blocked behavior. Those are workflow-authority decisions, so they remain visible but out of execution scope. |
| 5 | `runtime-tooling-transition/sense-env-scaffold` | `shared-governance-blocked` | `bootstrap-artifact-gap`, `shared-governance-gap` | `docs/migration/migration-runway-checklist.md` | The runway checklist still classifies `.github/skills/sense-env-scaffold/` as a confirmed runtime/tooling blocker. No bounded topic contract exists yet, and the remaining dependency is repo-wide enough to stay blocked here. |
| 6 | `runtime-tooling-transition/plan-step-tracker-active-path` | `shared-governance-blocked` | `bootstrap-artifact-gap`, `step-gap`, `shared-governance-gap` | `docs/migration/migration-runway-checklist.md`, `docs/migration/plan-step-tracker-move.md` | The move topic already copied `plan-step-tracker` into `skills/`, but the runway checklist still tracks `.github/skills/plan-step-tracker/` as a confirmed runtime/tooling blocker. The remaining work is no longer a folder move; it is active-path and workflow-contract alignment, so it is blocked here. |
| 7 | `runtime-tooling-transition/python-project-init-greenfield` | `shared-governance-blocked` | `bootstrap-artifact-gap`, `shared-governance-gap` | `docs/migration/migration-runway-checklist.md` | The candidate is still a confirmed runtime/tooling blocker with no bounded migration topic and no evidence that it can be decoupled from repo-wide workflow assumptions yet. |
| 8 | `runtime-tooling-transition/python-project-retrofit` | `shared-governance-blocked` | `bootstrap-artifact-gap`, `shared-governance-gap` | `docs/migration/migration-runway-checklist.md` | The candidate is still a confirmed runtime/tooling blocker with no bounded migration topic and no evidence that it can be decoupled from repo-wide workflow assumptions yet. |

## Excluded From The Next-Wave Queue

These existing topic results are intentionally not mixed into the queue rows
above.

| Existing topic / result | Why excluded |
| --- | --- |
| `codex-migration-direct-move` result for `business-intent-alignment`, `business-to-technical-translation`, `plan-creator`, `plan-reviewer` | `docs/migration/codex-migration-direct-move-report.md` marks all four as `already satisfied` in that verification-only topic. They still have later cutover or convergence follow-up, but they are not next-wave move rows here. |
| `worktree-manager-move` | `docs/migration/worktree-manager-move.md` already records a completed `skills/worktree-manager/` copy result. The remaining issues belong to later runtime/tooling or cutover work, not to this completed move topic. |
| `agent-skill-contract-surface-move` | `docs/migration/agent-skill-contract-surface-move.md` already records completed target-side copies for the three contract surfaces. The remaining active-path issue is represented separately as `agent-skill-active-path-transition/contract-surfaces`. |
| `plan-step-tracker-move` | `docs/migration/plan-step-tracker-move.md` already records the completed copy result. The remaining issue is the runtime/tooling active-path dependency, represented separately as `runtime-tooling-transition/plan-step-tracker-active-path`. |
| `git-commit-convention` and `git-branch-naming` low-residue report rows | `docs/migration/codex-migration-copilot-residue-low-report.md` leaves no bounded next-wave migration topic for either row. `git-commit-convention` needs only later projection work; `git-branch-naming` already received bounded wording cleanup. |
| `copilot-instructions-init` | `docs/migration/codex-migration-copilot-specific-report.md` gives a final verdict of `reference-only`, so it is not queued as a migration candidate. |
| `business-intent-alignment` / `business-to-technical-translation` same-name follow-up | `docs/migration/codex-readability-baseline.md` kept these in a same-name backlog, but the direct-move verification report later froze them as already satisfied for the current move branch. No new bounded next-wave topic is evidenced in the requested source set. |

## Flow Verification

The creator-stage result was checked against the topic boundary:

| Check | Result |
| --- | --- |
| Start from `requirements.md`, `plan.md`, and `step.md` first | passed |
| Use repo-visible artifacts as the only evidence basis | passed |
| Keep rows at `topic / candidate` granularity | passed |
| Keep primary classifications limited to `can_start_now`, `after-workflow-baseline`, `shared-governance-blocked` | passed |
| Keep gap classes limited to the six approved classes | passed |
| Do not move any skill folder | passed |
| Do not modify shared governance surface | passed |
| Do not assume the workflow baseline is already implemented | passed |
| Stop at sequencing / inventory / gap classification only | passed |

## Frozen Output

- Immediate next-wave candidates:
  - `planning-spine-bounded-remediation/ready-subset`
  - `git-post-merge-workflow-enhancement`
- Deferred until workflow baseline:
  - `agent-skill-active-path-transition/contract-surfaces`
- Visible but blocked:
  - `planning-spine-bounded-remediation/blocked-subset`
  - `runtime-tooling-transition/sense-env-scaffold`
  - `runtime-tooling-transition/plan-step-tracker-active-path`
  - `runtime-tooling-transition/python-project-init-greenfield`
  - `runtime-tooling-transition/python-project-retrofit`
