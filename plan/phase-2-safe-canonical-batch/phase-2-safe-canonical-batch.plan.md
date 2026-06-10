# phase-2-safe-canonical-batch

## Goal / Outcome

Produce a repo-visible planning baseline for the first execution slice after
umbrella so later canonical convergence work can proceed for the exact frozen
nine-skill safe list without widening into other Phase 2 buckets.

When this topic is complete:

- the first execution slice is defined as planning-stage only in the current
  workflow,
- the exact nine-skill safe list is frozen,
- later execution under this topic is bounded to that safe list only,
- and no downstream actor needs to guess whether merge-into-skills,
  planning-spine exceptions, projection work, runtime adaptation, or
  copilot-only work belong here.

## Scope

- **In scope**:
  - create `analysis/phase-2-safe-canonical-batch/requirements.md`
  - create `analysis/phase-2-safe-canonical-batch/technical-spec.md`
  - create `plan/phase-2-safe-canonical-batch/phase-2-safe-canonical-batch.plan.md`
  - create `plan/phase-2-safe-canonical-batch/phase-2-safe-canonical-batch.step.md`
  - freeze the exact nine-skill safe canonical batch
  - define first-slice planning boundaries for later canonical convergence work
  - state the parent umbrella baseline and current planning-only status
  - record where later implementation scope remains `human_review_required`

- **Out of scope**:
  - editing `skills/**`
  - editing `.github/skills/**`
  - editing `.codex/skills/**`
  - editing `.github/agents/**`
  - editing `.codex/agents/**`
  - editing shared contract files
  - editing umbrella topic artifacts
  - any canonical convergence implementation in this turn
  - `phase-2-merge-into-skills-batch`
  - `phase-2-planning-spine-exceptions`
  - projection materialization
  - runtime adaptation
  - copilot-only work

## Locked Decisions

### 1. Current workflow stage is planning only

- This turn is planning only.
- No canonical convergence implementation starts in the current workflow stage.
- Later creator execution under this topic requires separate downstream review
  and human gates.

### 2. Parent umbrella baseline is fixed

- This topic branches from approved umbrella baseline
  `feat/andrew/phase-2-umbrella` at `9d1d784`.
- This topic is the first execution slice after umbrella.
- Umbrella decisions about canonical target, non-authority surfaces, and slice
  ordering are treated as frozen planning inputs here.

### 2.5 Analysis baseline tracking is fixed

- `analysis/phase-2-safe-canonical-batch/requirements.md`
  - SHA-256: `bf353acc1363515478e8c33426ce2fced9d4961f99aff672a569334511175daf`
- `analysis/phase-2-safe-canonical-batch/technical-spec.md`
  - SHA-256: `0cb30c82634d40c7c68f51ad28b8be3353367e41beae044913918415d16898cc`

These analysis artifacts are frozen read-only prerequisites for later
execution unless a separately approved scope change reopens them.

### 3. Canonical and non-authority surface model is fixed

- `skills/` is the canonical convergence target.
- `.github/skills/` is not an authority source tree.
- `.codex/skills/` is not an authority source tree.
- `.codex/skills/` is only a partial projection surface.

### 4. Safe canonical batch list is frozen exactly

The safe canonical batch skill list is frozen to:

- `agent-skill-reviewer`
- `business-intent-alignment`
- `business-to-technical-translation`
- `git-branch-naming`
- `git-commit-convention`
- `git-post-merge-workflow`
- `python-project-init-greenfield`
- `python-project-retrofit`
- `worktree-manager`

### 5. Low-risk planning assumption is fixed

- Phase 1 classified the frozen nine-skill list as low-risk canonical
  candidates.
- This planning topic may assume no semantic-drift reconciliation work is
  needed inside this topic unless later evidence contradicts that assumption.
- This assumption does not authorize guessing exact later implementation write
  scope.

### 6. Later implementation must stay bounded to the frozen safe list only

- Later execution under this topic may target only the exact nine listed safe
  skills.
- No tenth skill may be added by analogy or convenience.
- If later implementation would require scope beyond the frozen list, stop and
  route to `human_review_required`.

### 7. Out-of-scope slices and work types are fixed

- `phase-2-merge-into-skills-batch` remains out of scope.
- `phase-2-planning-spine-exceptions` remains out of scope.
- Projection materialization remains out of scope.
- Runtime adaptation remains out of scope.
- Copilot-only work remains out of scope.
- `docs/status.md` remains optional only.

### 8. Later implementation write scope is not fully frozen by current evidence

- Current evidence is sufficient to freeze topic boundaries and safe-batch
  membership.
- Current evidence is not sufficient to invent an exact per-file implementation
  write set for later creator execution without guessing.
- Exact later implementation write scope is therefore
  `human_review_required` if downstream work cannot derive it honestly from
  then-current evidence.

## Boundaries / Exclusions

- Do not edit any skill surface in this planning turn.
- Do not widen into merge-into-skills candidate handling.
- Do not widen into planning-spine exception handling.
- Do not widen into `.codex/skills/` projection or adapter design.
- Do not widen into runtime adaptation or path-rewrite work.
- Do not widen into copilot-only legacy handling.
- Do not use `docs/status.md` as execution truth or success prerequisite.
- Do not treat the current planning artifact set as implementation approval.

## Status / Allowed Transitions

- **Current**: `merged`
- **Execution model**: the planning baseline and bounded execution bootstrap for
  this slice are complete, PR `#106` has merged into the umbrella parent
  branch, and this topic is now terminal under the current closeout model
- **Allowed transitions**:
  - `planned` -> `creator-in-progress`
  - `creator-in-progress` -> `review-ready`
  - `review-ready` -> `reviewer-in-progress`
  - `reviewer-in-progress` -> `approved`
  - `reviewer-in-progress` -> `needs-rework`
  - `needs-rework` -> `creator-in-progress`
  - `approved` -> `publish-in-progress`
  - `publish-in-progress` -> `pr-open`
  - `publish-in-progress` -> `merged`
  - `pr-open` -> `needs-rework`
  - `pr-open` -> `merged`
  - `merged` -> terminal

Routing notes:

- Planning artifacts were the only outputs in the original planning turn.
- Later bounded creator work did begin from this topic plan rather than chat
  summary alone.
- PR `#106` merged this topic into `feat/andrew/phase-2-umbrella` on
  2026-06-10.
- This topic is now merged and terminal under the current closeout model.

## Artifact Paths

| Artifact | Path | Owner | Role |
| --- | --- | --- | --- |
| Requirements baseline | `analysis/phase-2-safe-canonical-batch/requirements.md` | Planning actor | Frozen business / coordination baseline for the first safe canonical slice |
| Technical baseline | `analysis/phase-2-safe-canonical-batch/technical-spec.md` | Planning actor | Frozen technical translation for exact safe-list scope and deferred implementation write-scope handling |
| Topic plan | `plan/phase-2-safe-canonical-batch/phase-2-safe-canonical-batch.plan.md` | Planning actor | Repo-visible execution contract for the first safe canonical slice |
| Topic progression artifact | `plan/phase-2-safe-canonical-batch/phase-2-safe-canonical-batch.step.md` | Planning actor | Current-truth workflow progression status for this topic |
| Governance canonical source | `AGENTS.md` | Existing repo artifact | Read-only governance authority source |
| Positioning contract | `docs/repo-positioning.md` | Existing repo artifact | Read-only positioning evidence for canonical and projection boundaries |
| Repo workflow contract | `plan/agent-handoff-workflow.md` | Existing repo artifact | Read-only workflow-phase and truth-artifact authority |
| Shared topic-plan contract | `plan/topic-plan-contract.md` | Existing repo artifact | Read-only topic-plan structure and blocking-semantics authority |
| Umbrella parent plan | `plan/phase-2-umbrella/phase-2-umbrella.plan.md` | Existing repo artifact | Read-only parent planning baseline for slice order and umbrella scope boundaries |
| Umbrella parent progression artifact | `plan/phase-2-umbrella/phase-2-umbrella.step.md` | Existing repo artifact | Read-only evidence that umbrella human-check completed and this topic is next |
| Phase 1 summary | `docs/agent-skills-convergence/phase-1/00-summary.md` | Existing repo artifact | Read-only evidence that Phase 1 did not implement convergence and preserved `skills/` as canonical target |
| Convergence candidates | `docs/agent-skills-convergence/phase-1/06-convergence-candidates.md` | Existing repo artifact | Read-only evidence for the exact low-risk safe canonical candidates |
| Phase 2 inputs | `docs/agent-skills-convergence/phase-1/07-phase-2-inputs.md` | Existing repo artifact | Read-only evidence for first-slice safe-list membership |
| Analysis prompt guidance | `.github/prompts/create-analysis.prompt.md` | Existing repo artifact | Read-only evidence for analysis-layer output expectations |
| Plan prompt guidance | `.github/prompts/create-agent-plan.prompt.md` | Existing repo artifact | Read-only evidence for repo-visible topic-plan expectations |

Artifact path notes:

- This topic does not create `plan/phase-2-safe-canonical-batch/phase-2-safe-canonical-batch.review-log.md`.
- This topic does not create `plan/phase-2-safe-canonical-batch/phase-2-safe-canonical-batch.summary.md`.
- If planning-stage review later determines either artifact is required for
  this topic, treat that as `human_review_required` rather than widening scope
  silently.

## Implementation Steps

1. Read repo governance, workflow, topic-plan contract, umbrella baseline, and
   Phase 1 evidence before drafting the first-slice plan.
2. Record that this topic is the first execution slice after umbrella but that
   the current turn remains planning only.
3. Freeze the exact nine-skill safe canonical batch list with no additions or
   removals.
4. Preserve the rule that `skills/` is canonical and `.github/skills/` plus
   `.codex/skills/` are non-authority surfaces, with `.codex/skills/` only as
   a partial projection surface.
5. Encode that later implementation under this topic may target only the
   frozen safe list and may not widen into later slices or non-safe work.
6. Encode explicit exclusions for merge-into-skills work, planning-spine
   exception handling, projection materialization, runtime adaptation, and
   copilot-only work.
7. Mark exact later implementation write scope as `human_review_required`
   wherever current evidence would otherwise force guessing.
8. Stop and route to `human_review_required` if planning-stage work would
   require:
   - any file outside the declared write set
   - any shared contract file edit
   - any umbrella artifact edit
   - any implementation edit under skill or agent surfaces

## Validation / Acceptance Checks

- `analysis/phase-2-safe-canonical-batch/requirements.md` exists and freezes
  the first-slice planning requirements
- `analysis/phase-2-safe-canonical-batch/technical-spec.md` exists and maps
  those requirements to bounded planning work
- `plan/phase-2-safe-canonical-batch/phase-2-safe-canonical-batch.plan.md`
  exists and uses canonical topic-plan sections
- `plan/phase-2-safe-canonical-batch/phase-2-safe-canonical-batch.step.md`
  exists and provides progression truth for this planning turn
- the exact safe canonical batch list contains only the nine frozen skills
- the plan records parent umbrella baseline `feat/andrew/phase-2-umbrella` at
  `9d1d784`
- the plan states current work is planning only
- the plan states later implementation stays bounded to the frozen safe list
  only
- the plan excludes merge-into-skills, planning-spine exceptions, projection
  materialization, runtime adaptation, and copilot-only work
- the plan treats `docs/status.md` as optional only
- the plan marks guessed later implementation write scope as
  `human_review_required`
- no file outside the declared write set is modified

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

- This planning turn does not require stable-library updates.
- This planning turn does not require `README.md` changes.
- This planning turn does not require `VERSION` changes.
- This planning turn does not require release or tagging work.
- If later implementation under this topic affects stable-library surfaces,
  that timing must be decided in later execution review, not inferred now.

## Open Questions / Unresolved Items

- Exact per-file implementation write scope for later execution remains
  `human_review_required` unless later evidence makes it explicit without
  guessing.
- Whether later execution under this topic will require a `review-log.md` or
  `summary.md` artifact depends on then-current workflow conditions and is not
  created in this planning turn.
- If any of the nine safe-batch skills later shows semantic drift that
  contradicts Phase 1 low-risk classification, the topic must stop and repair
  the plan rather than proceed by assumption.
