# python-plan-review topic plan

**Semantic warning**:
No analysis-layer `technical-spec.md` exists for this topic. This bootstrap plan
uses `analysis/python-plan-review/requirements.md` as the frozen business and
scope baseline and does not enter strict-mode technical-spec mapping.

## Goal / Outcome

- Freeze a single-topic execution contract for `python-plan-review` so the
  canonical `skills/python-plan-review/` surface can be validated and, only if
  needed, repaired to match the current `.github/skills/python-plan-review/`
  source without changing the transition-era active path.

## Scope

- **In scope**:
  - `analysis/python-plan-review/requirements.md`
  - `plan/python-plan-review/python-plan-review.plan.md`
  - `plan/python-plan-review/python-plan-review.step.md`
  - `.workflow-runs/topic-bootstrap-python-plan-review-20260601/`
  - `skills/python-plan-review/SKILL.md`
  - `skills/python-plan-review/checklist.md`
  - `skills/python-plan-review/examples.md`

- **Out of scope**:
  - `.github/skills/python-plan-review/`
  - other review or planning skills
  - `README.md`
  - `VERSION`
  - `.github/copilot-instructions.md`
  - workflow-governance files under `docs/process/workflows/`
  - active-path cutover or projection changes

## Locked Decisions

- This topic is review-ready-only and does not affect stable-library surfaces.
- `.github/skills/python-plan-review/` remains the current authored and reviewed
  workflow path during transition.
- `skills/python-plan-review/` is the canonical target surface being validated
  and repaired by this topic.
- Implementation must stay inside the single-topic write set and must not widen
  into neighboring skills or shared workflow governance.
- If canonical parity is already satisfied, implementation records validation
  evidence instead of inventing new skill changes.
- If drift is found, repair is allowed only inside `skills/python-plan-review/`.
- This topic stops at `MIGRATION_STATUS_CONFIRMED` in the later
  `migration-implementation` workflow and requires a separate publish-handoff
  run for commit / push / PR progression.

## Boundaries / Exclusions

- Planning actor owns the requirements baseline, topic plan, and progression
  artifact.
- Creator owns only canonical-surface validation and bounded repair inside
  `skills/python-plan-review/`.
- Reviewer owns only the independent implementation verdict and must not author
  the final skill changes directly.
- Main Agent owns workflow orchestration, status convergence, later publish
  handoff, and cleanup routing.
- This topic must not reinterpret repository positioning or declare that
  `skills/` is already the active workflow path today.

## Status / Allowed Transitions

- **Current**: `planned`
- **Execution model**: follow the canonical creator -> reviewer -> publish ->
  merge path; this topic is expected to stop at `merged` if publish later
  happens, and no release action is declared
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

- Topic bootstrap creates and uses the managed worktree rooted at
  `/Users/andrew/code/python/agent-skills.worktrees/agent-20260601-python-plan-review`.
- Later implementation work must stop and repair the plan if any write is
  needed outside the listed artifact paths.
- STOP POINT 1 applies only in the later publish phase, not during bootstrap.

## Artifact Paths

| Artifact | Path | Owner | Role |
| --- | --- | --- | --- |
| Requirements baseline | `analysis/python-plan-review/requirements.md` | Planning actor | Frozen business and scope baseline for this migration topic |
| Topic plan | `plan/python-plan-review/python-plan-review.plan.md` | Planning actor | Repo-visible execution contract for this topic |
| Topic progression artifact | `plan/python-plan-review/python-plan-review.step.md` | Planning actor | Workflow progression and handoff truth for this topic before summary/close time |
| Bootstrap status | `.workflow-runs/topic-bootstrap-python-plan-review-20260601/status.json` | Main Agent | Repo-visible workflow status for the bootstrap run |
| Worktree routing audit | `.workflow-runs/topic-bootstrap-python-plan-review-20260601/worktree-routing-audit.txt` | Independent worktree role | Records worktree creation and routing result before implementation starts |
| Plan review result | `.workflow-runs/topic-bootstrap-python-plan-review-20260601/plan-review.json` | Independent reviewer role | Fixed-schema plan review verdict for bootstrap readiness |
| Planner final review | `.workflow-runs/topic-bootstrap-python-plan-review-20260601/planner-final-review.md` | Planning actor | Final scope-drift check after plan review |
| Canonical skill contract | `skills/python-plan-review/SKILL.md` | Creator | Canonical skill contract to validate or repair in implementation |
| Canonical skill checklist | `skills/python-plan-review/checklist.md` | Creator | Canonical local checklist surface kept in parity with the current source |
| Canonical skill examples | `skills/python-plan-review/examples.md` | Creator | Canonical examples surface kept in parity with the current source |

Artifact path notes:

- This topic does not modify `README.md`, `VERSION`, or
  `.github/copilot-instructions.md`.
- This topic treats `.github/skills/python-plan-review/` as read-only evidence.
- Any later work outside these exact paths is out of contract and must stop for
  plan repair before continuing execution.

## Implementation Steps

1. Inspect `skills/python-plan-review/` against
   `.github/skills/python-plan-review/` and record whether the canonical file
   set already satisfies parity.
2. If parity drift exists, repair only
   `skills/python-plan-review/SKILL.md`, `checklist.md`, and `examples.md`
   until the canonical surface matches the current source contract.
3. Capture implementation review evidence that the topic stayed inside the
   single-topic write set and did not imply active-path cutover.
4. Record migration status only after canonical parity and bounded-scope review
   both pass.

## Validation / Acceptance Checks

- `analysis/python-plan-review/requirements.md`,
  `plan/python-plan-review/python-plan-review.plan.md`, and
  `plan/python-plan-review/python-plan-review.step.md` all exist before
  implementation starts.
- The bootstrap worktree routing record clearly shows the managed worktree path,
  attached branch, and safe next step.
- Plan review returns one machine-consumable JSON object and no blocking issues.
- The topic plan declares non-stable intent explicitly and does not leave
  README/VERSION timing implicit.
- Later implementation stays bounded to `skills/python-plan-review/` plus
  topic-owned workflow artifacts only.
- Canonical parity is proven by `diff -rq` or equivalent evidence with no
  active-path cutover claim.

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

- After merge, a later explicit post-merge workflow may sync and clean up the
  topic worktree.
- No repository release action is required for this topic.
- This topic does not declare README or VERSION updates.

## Open Questions / Unresolved Items

- None. The topic scope is frozen to a single canonical backfill unit for
  `python-plan-review`.
