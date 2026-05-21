# planning-spine-bounded-remediation

## Goal / Outcome

- Produce a planning-only remediation contract for the planning-spine same-name
  pair.
- Lock a bounded execution subset for the units that can be aligned safely now.
- Isolate the remaining units that still require human policy lock so a later
  Implement Agent does not need to invent authority or behavior decisions.

## Scope

- **In scope**:
  - `analysis/planning-spine-bounded-remediation/requirements.md`
  - `plan/planning-spine-bounded-remediation/planning-spine-bounded-remediation.plan.md`
  - read-only inspection of:
    - `skills/plan-creator/`
    - `.github/skills/plan-creator/`
    - `skills/plan-reviewer/`
    - `.github/skills/plan-reviewer/`
    - `docs/migration/planning-spine-divergence-review.md`
    - `docs/migration/same-name-direct-canonicalize.md`
    - `plan/agent-handoff-workflow.md`

- **Out of scope**:
  - any skill content edit in this topic
  - any `.codex/skills` change
  - any business same-name topic
  - any low-risk move topic
  - any runtime/tooling blocker topic
  - any README / VERSION / tag / release action
  - any repo-wide governance rewrite

## Locked Decisions

- This topic is planning-only and must not execute remediation edits.
- The topic is classified as `partially executable`.
- The bounded execution subset is limited to support-material drift that can be
  aligned without settling unresolved workflow-authority questions.
- The blocked subset is limited to units that still require human policy lock on
  fallback source, review-basis authority, or blocked reviewer behavior.
- Readability from `skills/` is supporting evidence only; it is not sufficient
  to force-overwrite planning-spine contracts by itself.
- No unit may be left partially specified; each unit is exactly
  `implementation-ready` or `explicitly-blocked`.
- This topic does not create implementation artifacts or a migration report.

## Boundaries / Exclusions

- Do not reopen same-name discovery.
- Do not assume force-overwrite is safe.
- Do not assign canonical workflow authority where current repo-visible evidence
  still supports more than one defensible interpretation.
- Do not authorize any file outside the exact editable paths listed below for
  the implementation-ready subset.
- If a later remediation attempt would need a file not listed here, that is a
  plan-alignment failure and requires replanning.

## Status / Allowed Transitions

- **Current**: `review-ready`
- **Execution model**: planning artifacts are drafted and now waiting for the
  reviewer/planner approval loop before publish / PR work begins
- **Allowed transitions**:
  - `review-ready` -> `reviewer-in-progress`
  - `reviewer-in-progress` -> `approved`
  - `reviewer-in-progress` -> `needs-rework`
  - `needs-rework` -> `creator-in-progress`
  - `creator-in-progress` -> `review-ready`
  - `approved` -> `creator-in-progress`
  - `approved` -> `publish-in-progress`
  - `publish-in-progress` -> `pr-open`
  - `publish-in-progress` -> `merged`
  - `pr-open` -> `needs-rework`
  - `pr-open` -> `merged`
  - `merged` -> terminal

Routing notes:

- Standard Phase 4.5 planner-alignment routing applies.
- Any later implementation topic derived from this plan must inherit the blocked
  subset as out of execution scope unless a new human policy lock removes the
  block.

## Artifact Paths

| Artifact | Path | Owner | Role |
| --- | --- | --- | --- |
| Requirements baseline | `analysis/planning-spine-bounded-remediation/requirements.md` | Planning actor | Locks remediation units, classification rules, and stop conditions |
| Topic plan | `plan/planning-spine-bounded-remediation/planning-spine-bounded-remediation.plan.md` | Planning actor | Repo-visible bounded remediation execution contract |
| Upstream divergence report | `docs/migration/planning-spine-divergence-review.md` | Existing repo artifact | Row-level evidence source for all eight remediation units |
| Prior canonicalization decision | `docs/migration/same-name-direct-canonicalize.md` | Existing repo artifact | Authority-handling reference for the already-equivalent business pair |

Artifact path notes:

- This topic does **not** modify `README.md`, `VERSION`, or
  `.github/copilot-instructions.md`.
- No skill content path is writable in this plan; skill folders are read-only
  evidence sources here.
- If later work appears outside the exact editable files listed in the unit
  table below, stop and re-plan.

## Implementation Steps

1. Reconfirm the eight fixed remediation units against the four in-scope skill
   folders.
2. Classify each unit as exactly `implementation-ready` or
   `explicitly-blocked`.
3. For every ready unit, lock:
   - temporary implementation source
   - target resolution
   - exact editable files
   - exact untouched files
   - validation
4. For every blocked unit, lock:
   - the missing policy or evidence
   - the implicated files
   - the reason it remains out of execution scope
5. Keep the later bounded execution subset limited to the ready units below.

## Validation / Acceptance Checks

- The topic remains planning-only and does not authorize remediation edits here.
- All eight remediation units are classified exactly once.
- Every ready unit has exact file-level execution data.
- Every blocked unit has an explicit missing policy/evidence statement.
- The plan clearly separates the bounded execution subset from the blocked
  subset.
- No hidden authority decision is deferred to the Implement Agent.

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

- No repository release action is required for this planning-only topic.
- After merge, this topic should hand off to a later execution topic that
  implements only the ready subset, or to a human policy-lock decision for the
  blocked subset.

## Open Questions / Unresolved Items

- Which fallback contract source should ultimately govern `plan-creator` when
  the topic-plan template is absent:
  - local `references/required-section-meaning.md`
  - repo-level `folder-contract.md`
- Which planning surface should remain the review-basis authority for
  `plan-reviewer`:
  - `skills/plan-creator/...`
  - `.github/skills/plan-creator/...`
- Should missing-plan / missing-source review failure stay machine-consumable as
  `needs-rework`, or stay as a hard stop with no verdict object

## Remediation Unit Contract

| Skill | Difference area | Status | Temporary implementation source | Target resolution | Exact editable files if ready | Exact untouched files | Validation | Missing policy/evidence if blocked |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `plan-creator` | `fallback-contract-source` | `explicitly-blocked` | none | none | none | `skills/plan-creator/SKILL.md`, `.github/skills/plan-creator/SKILL.md`, `skills/plan-creator/references/required-section-meaning.md`, `.github/skills/plan-creator/references/required-section-meaning.md` | none | Missing human policy lock on whether fallback section authority is local-skill-owned or repo-governance-owned. Current evidence shows two incompatible fallback contracts, and choosing one would settle workflow authority rather than support-material drift only. |
| `plan-creator` | `reference-body-expansion` | `implementation-ready` | `.github/skills/plan-creator/reference.md` | `adopt .github/skills/` | `skills/plan-creator/reference.md` | `skills/plan-creator/SKILL.md`, `skills/plan-creator/checklist.md`, `skills/plan-creator/examples.md`, `skills/plan-creator/references/artifact-path-rule.md`, `skills/plan-creator/references/required-section-meaning.md`, `skills/plan-creator/references/role-boundary-rule.md`, `skills/plan-creator/references/stable-library-rule.md`, `skills/plan-creator/references/stop-and-ask-triggers.md`, `skills/plan-creator/references/template-usage-rule.md`, `skills/plan-creator/templates/topic-plan-template.md` | `diff -u skills/plan-creator/reference.md .github/skills/plan-creator/reference.md` is empty after remediation; the updated `skills/` reference still points only to files that exist locally. | none |
| `plan-creator` | `examples-drift` | `implementation-ready` | `.github/skills/plan-creator/examples.md` | `adopt .github/skills/` | `skills/plan-creator/examples.md` | `skills/plan-creator/SKILL.md`, `skills/plan-creator/checklist.md`, `skills/plan-creator/reference.md`, `skills/plan-creator/references/artifact-path-rule.md`, `skills/plan-creator/references/required-section-meaning.md`, `skills/plan-creator/references/role-boundary-rule.md`, `skills/plan-creator/references/stable-library-rule.md`, `skills/plan-creator/references/stop-and-ask-triggers.md`, `skills/plan-creator/references/template-usage-rule.md`, `skills/plan-creator/templates/topic-plan-template.md` | `diff -u skills/plan-creator/examples.md .github/skills/plan-creator/examples.md` is empty after remediation; added examples stay within current workflow semantics and do not require new files outside the local surface. | none |
| `plan-creator` | `template-support-and-auxiliary-references` | `implementation-ready` | `.github/skills/plan-creator/` support files | `adopt .github/skills/` | `skills/plan-creator/checklist.md`, `skills/plan-creator/references/artifact-path-rule.md`, `skills/plan-creator/references/role-boundary-rule.md`, `skills/plan-creator/templates/topic-plan-template.md` | `skills/plan-creator/SKILL.md`, `skills/plan-creator/reference.md`, `skills/plan-creator/examples.md`, `skills/plan-creator/references/required-section-meaning.md`, `skills/plan-creator/references/stable-library-rule.md`, `skills/plan-creator/references/stop-and-ask-triggers.md`, `skills/plan-creator/references/template-usage-rule.md` | Each edited support file matches the `.github/skills/` peer exactly, and no untouched local reference path becomes dangling. | none |
| `plan-reviewer` | `review-basis-path` | `explicitly-blocked` | none | none | none | `skills/plan-reviewer/SKILL.md`, `.github/skills/plan-reviewer/SKILL.md`, `skills/plan-reviewer/reference.md`, `.github/skills/plan-reviewer/reference.md`, `skills/plan-reviewer/checklist.md`, `.github/skills/plan-reviewer/checklist.md` | none | Missing human policy lock on which plan-creator surface (`skills/` or `.github/skills/`) is the current authoritative review basis for planner review. This is workflow authority, not support-only drift. |
| `plan-reviewer` | `blocked-behavior-for-missing-sources-or-plan` | `explicitly-blocked` | none | none | none | `skills/plan-reviewer/SKILL.md`, `.github/skills/plan-reviewer/SKILL.md` | none | Missing human policy lock on whether reviewer failure for missing sources/plan must return machine-consumable `needs-rework` JSON or must stop without a verdict. This decision affects orchestration and downstream automation behavior. |
| `plan-reviewer` | `reference-review-rules` | `implementation-ready` | `.github/skills/plan-reviewer/reference.md` | `adopt .github/skills/` | `skills/plan-reviewer/reference.md` | `skills/plan-reviewer/SKILL.md`, `skills/plan-reviewer/checklist.md`, `skills/plan-reviewer/examples.md` | `diff -u skills/plan-reviewer/reference.md .github/skills/plan-reviewer/reference.md` is empty after remediation; the updated `skills/` reference distinguishes projection readability from overwrite authority and keeps output JSON rules intact. | none |
| `plan-reviewer` | `examples-and-checklist-drift` | `implementation-ready` | `.github/skills/plan-reviewer/` support files | `adopt .github/skills/` | `skills/plan-reviewer/checklist.md`, `skills/plan-reviewer/examples.md` | `skills/plan-reviewer/SKILL.md`, `skills/plan-reviewer/reference.md` | `diff -u` is empty for both edited files after remediation; checklist rules and examples align with the updated reference-review guidance without changing reviewer runtime behavior in `SKILL.md`. | none |

## Bounded Execution Subset That May Proceed Now

The later Implement Agent may execute only these ready units:

- `plan-creator/reference-body-expansion`
- `plan-creator/examples-drift`
- `plan-creator/template-support-and-auxiliary-references`
- `plan-reviewer/reference-review-rules`
- `plan-reviewer/examples-and-checklist-drift`

Execution of that later topic must stay within these exact editable files only:

- `skills/plan-creator/reference.md`
- `skills/plan-creator/examples.md`
- `skills/plan-creator/checklist.md`
- `skills/plan-creator/references/artifact-path-rule.md`
- `skills/plan-creator/references/role-boundary-rule.md`
- `skills/plan-creator/templates/topic-plan-template.md`
- `skills/plan-reviewer/reference.md`
- `skills/plan-reviewer/checklist.md`
- `skills/plan-reviewer/examples.md`

## Blocked Units That Remain Out of Execution Scope

The later Implement Agent must not execute these units in the bounded
remediation topic unless a new human policy lock is added first:

- `plan-creator/fallback-contract-source`
- `plan-reviewer/review-basis-path`
- `plan-reviewer/blocked-behavior-for-missing-sources-or-plan`
