**Analysis-layer routing**: Strict mode with one explicit human override. Both `analysis/python-step-tracking-integration/requirements.md` and `analysis/python-step-tracking-integration/technical-spec.md` exist and are FROZEN. `technical-spec.md` remains the execution-facing source of truth and `requirements.md` remains the business-intent guardrail, except for the explicit 2026-05-07 override recorded in `Locked Decisions`: the step gate must scope to the `## Implementation Steps` section only, superseding the whole-file grep described in technical-spec T2-B. All other plan content maps to the frozen analysis artifacts and does not invent extra scope from chat context.

## Goal / Outcome

- Integrate `*.step.md` into the Python plan-authoring and implementation-review workflow so `python-plan-authoring` always emits `plan/<topic>/<topic>.step.md`, and `python-implementation-review` performs a backward-compatible pre-review step gate before building the traceability matrix.
- When this topic is complete, the repository-visible result is limited to the topic plan, two existing Python workflow skill contracts, and a MINOR `VERSION` bump reflecting the new stable capability integration.

## Scope

- **In scope**:
  - Create `plan/python-step-tracking-integration/python-step-tracking-integration.plan.md`.
  - Update `.github/skills/python-plan-authoring/SKILL.md` so `*.step.md` is a required co-artifact of `*.plan.md`.
  - Update `.github/skills/python-plan-authoring/SKILL.md` Process step 4 to produce `plan/<topic>/<topic>.step.md`.
  - Add the canonical `plan/<topic>/<topic>.step.md` template to `.github/skills/python-plan-authoring/SKILL.md` exactly per `analysis/python-step-tracking-integration/technical-spec.md`.
  - Update `.github/skills/python-implementation-review/SKILL.md` so `*.step.md` is an optional input.
  - Insert a step gate as Process step 1.5 in `.github/skills/python-implementation-review/SKILL.md`.
  - Add the BLOCKED plain-text refusal format to `.github/skills/python-implementation-review/SKILL.md`.
  - Bump `VERSION` from `0.48.0` to `0.49.0` during `publish-in-progress`.

- **Out of scope**:
  - Any change under `.github/skills/plan-step-tracker/`.
  - Any change to skills other than `python-plan-authoring` and `python-implementation-review`.
  - Adding scripts, tests, or a new skill.
  - Retroactively generating `*.step.md` for existing topic plans.
  - Updating `README.md`, `.github/copilot-instructions.md`, or release notes for this topic.

## Locked Decisions

- This topic affects stable-library surfaces through `VERSION` only; `README.md` stays unchanged and timing is declared below.
- The `*.step.md` path is fixed at `plan/<topic>/<topic>.step.md` and must stay aligned with `plan-step-tracker`.
- `## Workflow Stages` in `*.step.md` is fixed to six stages: `plan-authoring`, `plan-review`, `tdd-test-authoring`, `implementation`, `implementation-review`, `code-review`.
- Initial `*.step.md` state is fixed: `plan-authoring` starts as `[X]`; all other workflow stages start as `[ ]`.
- `python-plan-authoring` must reproduce the canonical `*.step.md` template inline in `SKILL.md` exactly per technical-spec mapping T1-B.
- `python-implementation-review` uses a grep-first portable gate; the `plan-step-tracker` CLI path is optional and must not become a hard dependency.
- Backward compatibility is fixed: if `plan/<topic>/<topic>.step.md` is missing, `python-implementation-review` emits WARN and proceeds; missing `*.step.md` is not BLOCKED.
- Pending step items produce a BLOCKED plain-text refusal output only; they do not modify the existing YAML verdict schema.
- **override (2026-05-07)** — Step gate MUST scope to `## Implementation Steps` section only. Do NOT scan `## Workflow Stages`. The portable implementation uses `sed -n '/^## Implementation Steps/,/^## /p' plan/<topic>/<topic>.step.md | grep '^\- \[[ x]\]'`. This override supersedes the whole-file grep in `analysis/python-step-tracking-integration/technical-spec.md` T2-B, which was found to produce false BLOCKs from the Workflow Stages `[ ]` entries.
- Lowercase `[x]` is treated as **pending**, not done, for both the portable fallback and the optional `plan-step-tracker` CLI path. This topic explicitly aligns with `plan-step-tracker/reference.md` on that behavior.
- `VERSION` is fixed to `0.49.0` for this topic and is applied at `publish-in-progress`, not deferred to a later release topic.

## Boundaries / Exclusions

- Planning actor owns this topic plan only; creator implementation must be performed by an independent `/fleet @.github/skills/agent-skill-creator/` subagent.
- Topic-plan review must be performed by an independent `/fleet @.github/skills/plan-reviewer/` subagent before creator execution starts.
- Skill review must be performed by an independent `/fleet @.github/skills/agent-skill-reviewer/` subagent; reviewer must not author the implementation directly.
- Main Agent owns branch/worktree routing, planner contract alignment, publish routing, and stop-point enforcement; Main Agent must not self-approve or self-perform creator / reviewer work.
- STOP POINT 1 remains in force before any commit, push, or PR creation.
- STOP POINT 2 remains terminal after manual merge handoff; no polling or implied resume is allowed without a new explicit human message confirming merge completion and asking to continue.
- This topic must not expand into `plan-step-tracker` changes, broader Python workflow refactors, or non-Python workflow skills.

## Status / Allowed Transitions

- **Current**: `pr-open`
- **Execution model**: follow the canonical creator -> reviewer -> publish -> merge path, but stop at `merged`; this topic does not declare a separate release action.
- **Allowed transitions**:
  - `planned` -> `creator-in-progress`
  - `creator-in-progress` -> `review-ready`
  - `review-ready` -> `reviewer-in-progress`
  - `reviewer-in-progress` -> `approved`
  - `reviewer-in-progress` -> `needs-rework`
  - `needs-rework` -> `creator-in-progress`
  - `approved` -> `creator-in-progress`
  - `approved` -> `publish-in-progress`
  - `publish-in-progress` -> `pr-open`
  - `publish-in-progress` -> `merged`
  - `pr-open` -> `needs-rework`
  - `pr-open` -> `merged`
  - `merged` -> terminal

Routing notes:

- Before entering `creator-in-progress`, run an independent `/fleet @.github/skills/plan-reviewer/` pass against this topic plan and fix any blocking contract issues first.
- Creator execution for this topic is delegated to `/fleet @.github/skills/agent-skill-creator/` and stays within the locked artifact paths below.
- Independent skill review for this topic is delegated to `/fleet @.github/skills/agent-skill-reviewer/`.
- After reviewer approval, required `ADDRESS` feedback must be applied before the Main Agent runs the Phase 4.5 planner contract alignment checkpoint defined in `plan/agent-handoff-workflow.md`.
- Current repo-visible state: independent creator implementation is complete, independent reviewer returned `approved` with no blocking issues, Main Agent Phase 4.5 planner contract alignment passed, and PR #67 is now open for this topic.
- If Phase 4.5 finds drift in locked decisions, strict-mode mapping, or artifact paths, route the topic back to `creator-in-progress` before any publish work.

## Artifact Paths

| Artifact | Path | Owner | Role |
| --- | --- | --- | --- |
| Topic plan | `plan/python-step-tracking-integration/python-step-tracking-integration.plan.md` | Planning actor | Repo-visible execution contract for this topic |
| Business requirements | `analysis/python-step-tracking-integration/requirements.md` | Planning actor | Frozen business-intent baseline for strict-mode planning |
| Technical spec | `analysis/python-step-tracking-integration/technical-spec.md` | Planning actor | Frozen technical mapping for strict-mode execution, subject to the recorded human override |
| Python plan-authoring skill contract | `.github/skills/python-plan-authoring/SKILL.md` | Creator | Add required `*.step.md` co-artifact production and canonical step-tracking template |
| Python implementation-review skill contract | `.github/skills/python-implementation-review/SKILL.md` | Creator | Add optional `*.step.md` input, step gate, WARN path, and BLOCKED refusal output |
| Repo version baseline | `VERSION` | Main Agent | Bump `0.48.0` -> `0.49.0` at `publish-in-progress` |

Artifact path notes:

- Strict-mode read-only authority comes from `analysis/python-step-tracking-integration/requirements.md` and `analysis/python-step-tracking-integration/technical-spec.md`; they guide execution but are not modified by creator work.
- `README.md`: no change for this topic.
- `.github/copilot-instructions.md`: no change for this topic.
- `.github/skills/plan-step-tracker/`: read-only reference surface; any modification there is a plan-alignment failure.
- If later work appears outside the listed writable paths, stop and repair the topic plan before continuing.

## Stable library metadata

- **Status**: this topic affects stable-library surfaces.
- `README row`: no change; this topic integrates new behavior into existing stable skills and does not add, remove, or rename a stable-library row.
- `VERSION bump`: MINOR, `0.48.0` -> `0.49.0`.
- `timing`: `publish-in-progress`
- `rationale`: this is a backward-compatible workflow capability integration across two existing stable Python skills. `VERSION` marks the repository capability increase; no deferred release topic is required.

## Implementation Steps

Creator work for this topic must stay inside the strict-mode technical-spec mapping and produce only the locked artifact paths.

### T1: Integrate `*.step.md` production into `python-plan-authoring`

1. Update `.github/skills/python-plan-authoring/SKILL.md` `outputs` frontmatter so `*.step.md` is a required co-artifact alongside `*.plan.md`.
2. Update Process step 4 in `.github/skills/python-plan-authoring/SKILL.md` so plan authoring also produces `plan/<topic>/<topic>.step.md`.
3. Reproduce the canonical `*.step.md` template inline in `.github/skills/python-plan-authoring/SKILL.md` exactly per technical-spec T1-B, including:
   - YAML frontmatter with `topic`, `phase: plan-authoring`, and `created: YYYY-MM-DD`
   - executor instruction note pointing to `plan/<topic>/<topic>.step.md`
   - all 6 fixed workflow stages with `plan-authoring` initialized to `[X]`
   - mirrored `## Implementation Steps` entries initialized to `[ ]`
4. Keep `plan-step-tracker/reference.md` as a read-only format authority; do not introduce scripts, helper files, or additional skill paths.

### T2: Add backward-compatible step gate to `python-implementation-review`

1. Update `.github/skills/python-implementation-review/SKILL.md` `inputs` frontmatter so `*.step.md` is an optional input.
2. Insert Process step 1.5 between the existing step 1 and step 2, resolving the topic from `plan/<topic>/<topic>.plan.md` and checking `plan/<topic>/<topic>.step.md`.
3. Implement the step gate wording so the portable path is primary and checks only the `## Implementation Steps` section, while the optional `plan-step-tracker` CLI path must be described as semantically equivalent for blocking purposes.
4. If `plan/<topic>/<topic>.step.md` is missing, emit the specified WARN message and continue to step 2 without blocking.
5. Pending items are only unresolved checklist lines inside `## Implementation Steps`, matched by `^\- \[[ x]\]`; `## Workflow Stages` are ignored by the gate, and lowercase `[x]` remains pending.
6. If pending Implementation Steps remain, emit the plain-text BLOCKED refusal output from technical-spec T2-C, stop before the traceability matrix, and do not produce a YAML verdict block.
7. Preserve backward compatibility and existing refusal / verdict semantics outside this step gate.

## Validation / Acceptance Checks

- `plan/python-step-tracking-integration/python-step-tracking-integration.plan.md` exists at the exact target path and remains aligned with strict-mode analysis inputs.
- `.github/skills/python-plan-authoring/SKILL.md` `outputs` frontmatter explicitly requires `*.step.md`.
- `.github/skills/python-plan-authoring/SKILL.md` Process step 4 explicitly produces `plan/<topic>/<topic>.step.md`.
- `.github/skills/python-plan-authoring/SKILL.md` contains the canonical `*.step.md` template with:
  - YAML frontmatter fields `topic`, `phase: plan-authoring`, `created`
  - executor note naming `plan/<topic>/<topic>.step.md`
  - all 6 fixed workflow stages
  - `plan-authoring` set to `[X]` and all other stages set to `[ ]`
  - mirrored `## Implementation Steps` lines using `- [ ]`
- `.github/skills/python-implementation-review/SKILL.md` `inputs` frontmatter explicitly lists optional `*.step.md`.
- `.github/skills/python-implementation-review/SKILL.md` contains Process step 1.5 between current steps 1 and 2.
- The step gate behavior matches the locked decisions:
  - missing `*.step.md` -> WARN + proceed
  - gate scans only `## Implementation Steps`, not `## Workflow Stages`
  - pending Implementation Steps matched by `^\- \[[ x]\]` -> BLOCKED plain-text refusal + stop
  - lowercase `[x]` is treated as pending
  - no YAML verdict block on BLOCKED step-gate results
- No changes occur under `.github/skills/plan-step-tracker/`, no other skills are modified, and no scripts are added.
- `README.md` remains unchanged for this topic.
- `VERSION` is `0.49.0` when the topic reaches `publish-in-progress`.

## Reviewer Handoff

```json
{
  "verdict": "approved|needs-rework",
  "blocking_issues": [],
  "copilot_feedback_triage": {
    "ADDRESS": [],
    "DISCUSS": [],
    "SKIP": []
  }
}
```

## Post-merge / release actions

- No separate repository release action is declared for this topic.
- After merge, local cleanup and sync may resume only through `git-post-merge-workflow` after a new explicit human resume message confirms the merge is complete.
- Because stable-library timing is `publish-in-progress`, `VERSION` is handled before merge and `merged` is the terminal state for this topic.

## Open Questions / Unresolved Items

- ~~BLOCKER — strict-mode analysis contradiction~~ **RESOLVED (2026-05-07, override)** — Human selected Option 1: step gate is scoped to `## Implementation Steps` section only (see override in Locked Decisions). Creator work may now proceed.
- ~~BLOCKER — strict-mode analysis still contains an unresolved lowercase `[x]` contradiction~~ **RESOLVED (2026-05-07, human choice)** — Lowercase `[x]` is treated as pending. This topic aligns the portable fallback and optional CLI semantics with `plan-step-tracker/reference.md`.
