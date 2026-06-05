# phase-2-umbrella

## Goal / Outcome

Produce a repo-visible Phase 2 coordination baseline that freezes later slice
planning inputs without authorizing direct convergence implementation.

When this topic is complete:

- later Phase 2 execution slices are explicit and ordered,
- the safe canonical batch membership is frozen exactly,
- the repository has one umbrella planning baseline to branch later slices
  from,
- and no downstream actor needs to guess whether umbrella scope itself permits
  skill edits, projection work, or runtime adaptation.

## Scope

- **In scope**:
  - create `analysis/phase-2-umbrella/requirements.md`
  - create `analysis/phase-2-umbrella/technical-spec.md`
  - create `plan/phase-2-umbrella/phase-2-umbrella.plan.md`
  - create `plan/phase-2-umbrella/phase-2-umbrella.step.md`
  - freeze Phase 2 slice names, order, and safe canonical batch membership
  - define umbrella-only coordination rules for later slice planning
  - state that later slices branch from umbrella baseline and each needs its
    own plan, review, human check, and PR

- **Out of scope**:
  - editing `skills/**`
  - editing `.github/skills/**`
  - editing `.codex/skills/**`
  - editing `.github/agents/**`
  - editing `.codex/agents/**`
  - any direct skill canonical convergence
  - any projection materialization
  - any runtime adaptation
  - any shared-contract-file edits
  - treating umbrella scope as a fourth implementation line
  - requiring `docs/status.md` for topic success

## Locked Decisions

### 1. Topic type is coordination-only

- `phase-2-umbrella` is a governance / coordination topic.
- It is not a fourth implementation line.
- It does not approve direct convergence work under umbrella scope.

### 2. Canonical and non-authority surfaces are fixed

- `skills/` is the canonical convergence target.
- `.github/skills/` is not an authority source tree.
- `.codex/skills/` is not an authority source tree.
- `.codex/skills/` is only a partial projection surface.

### 3. Later execution slices and order are fixed

The later execution slices are:

1. `phase-2-safe-canonical-batch`
2. `phase-2-merge-into-skills-batch`
3. `phase-2-planning-spine-exceptions`

Additional ordering rules:

- `phase-2-safe-canonical-batch` is the first execution slice.
- Slice PR order is strictly serialized.
- No later slice may assume umbrella completion equals slice approval.

### 4. Safe canonical batch membership is frozen

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

### 5. Artifact-role model is fixed

- `plan/<topic>/<topic>.summary.md` is topic close outcome / handoff truth.
- `plan/<topic>/<topic>.step.md` is topic progression truth.
- `docs/status.md` is optional cross-topic overview only.

### 6. Later slices need their own workflow contract

Each later slice must:

- branch from this umbrella baseline,
- create its own topic plan,
- complete its own review,
- complete its own human-check gate,
- and open its own PR in serialized order.

The umbrella topic does not satisfy those slice-specific gates on their behalf.

### 7. Write-set boundary is fixed

This topic may modify only:

- `analysis/phase-2-umbrella/requirements.md`
- `analysis/phase-2-umbrella/technical-spec.md`
- `plan/phase-2-umbrella/phase-2-umbrella.plan.md`
- `plan/phase-2-umbrella/phase-2-umbrella.step.md`

If later work under this topic would require any additional path or any shared
contract file, stop and route to `human_review_required`.

## Boundaries / Exclusions

- Do not start the safe canonical batch implementation here.
- Do not start merge-into-skills implementation here.
- Do not start planning-spine exception implementation here.
- Do not create or require `docs/status.md` as current-truth execution state.
- Do not infer permission to edit skill surfaces from Phase 1 reports alone.
- Do not use umbrella topic completion as substitute for later slice review or
  human approval.
- Do not widen into projection or runtime work for `.codex/skills/`.

## Status / Allowed Transitions

- **Current**: `planned`
- **Execution model**: planning baseline only, followed by later slice plan
  authoring and separate execution topics
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

- This umbrella topic covers planning artifacts only.
- Later slices must begin again from their own `plan/<topic>/<topic>.plan.md`.
- Any attempt to skip later slice planning or run slice PRs in parallel is plan
  drift.

## Artifact Paths

| Artifact | Path | Owner | Role |
| --- | --- | --- | --- |
| Requirements baseline | `analysis/phase-2-umbrella/requirements.md` | Planning actor | Frozen business / coordination baseline for the Phase 2 umbrella topic |
| Technical baseline | `analysis/phase-2-umbrella/technical-spec.md` | Planning actor | Frozen technical translation for slice ordering, batch freezing, and scope boundaries |
| Topic plan | `plan/phase-2-umbrella/phase-2-umbrella.plan.md` | Planning actor | Repo-visible execution contract for the umbrella coordination topic |
| Topic progression artifact | `plan/phase-2-umbrella/phase-2-umbrella.step.md` | Planning actor | Current-truth workflow progression status for the umbrella topic |
| Governance canonical source | `AGENTS.md` | Existing repo artifact | Read-only governance authority source |
| Positioning contract | `docs/repo-positioning.md` | Existing repo artifact | Read-only positioning evidence for canonical vs projection boundaries |
| Repo workflow contract | `plan/agent-handoff-workflow.md` | Existing repo artifact | Read-only workflow-phase and artifact-role authority |
| Shared topic-plan contract | `plan/topic-plan-contract.md` | Existing repo artifact | Read-only topic-plan structure and blocking-semantics authority |
| Phase 1 summary | `docs/agent-skills-convergence/phase-1/00-summary.md` | Existing repo artifact | Read-only evidence that Phase 1 did not perform convergence and that `skills/` remains canonical |
| Convergence candidates | `docs/agent-skills-convergence/phase-1/06-convergence-candidates.md` | Existing repo artifact | Read-only evidence for safe canonical candidates, merge-needed candidates, and planning-spine exceptions |
| Phase 2 inputs | `docs/agent-skills-convergence/phase-1/07-phase-2-inputs.md` | Existing repo artifact | Read-only evidence for later slice names and safe canonical batch input |
| Plan-contract authority summary | `plan/plan-contract-authority-alignment/plan-contract-authority-alignment.summary.md` | Existing repo artifact | Read-only evidence that repo-level plan-contract authority work is not a current blocker to umbrella planning |
| Analysis prompt guidance | `.github/prompts/create-analysis.prompt.md` | Existing repo artifact | Read-only evidence for analysis-layer output expectations |
| Plan prompt guidance | `.github/prompts/create-agent-plan.prompt.md` | Existing repo artifact | Read-only evidence for repo-visible topic-plan expectations |

Artifact path notes:

- This topic does not create `plan/phase-2-umbrella/phase-2-umbrella.summary.md`.
- This topic does not create `plan/phase-2-umbrella/phase-2-umbrella.review-log.md`.
- If a later workflow stage requires either artifact for this topic, stop and
  request `human_review_required` rather than widening scope silently.
- `docs/status.md` is intentionally not an umbrella success artifact.

## Implementation Steps

1. Read the governing repo-level artifacts and Phase 1 evidence before
   drafting any umbrella planning file.
2. Freeze the umbrella topic as coordination-only and record the exact
   non-authority status of `.github/skills/` and `.codex/skills/`.
3. Encode the three later execution slices exactly and freeze
   `phase-2-safe-canonical-batch` as the first slice.
4. Encode the exact nine-skill safe canonical batch list with no additions or
   removals.
5. State that later slices branch from this umbrella baseline and each needs
   its own plan, review, human check, and PR.
6. Record that later slice PRs are strictly serialized and must not proceed in
   parallel.
7. Preserve the artifact-role model that keeps `summary.md` for close truth,
   `step.md` for progression truth, and `docs/status.md` as optional overview
   only.
8. Stop and route to `human_review_required` if execution under this topic
   would require:
   - any file outside the declared write set
   - any shared contract file edit
   - any skill, projection, or runtime implementation work

## Validation / Acceptance Checks

- `analysis/phase-2-umbrella/requirements.md` exists and states coordination
  baseline requirements
- `analysis/phase-2-umbrella/technical-spec.md` exists and maps those
  requirements to bounded planning work
- `plan/phase-2-umbrella/phase-2-umbrella.plan.md` exists and uses canonical
  topic-plan sections
- `plan/phase-2-umbrella/phase-2-umbrella.step.md` exists and provides
  progression truth for the umbrella topic
- later execution slices are exactly:
  - `phase-2-safe-canonical-batch`
  - `phase-2-merge-into-skills-batch`
  - `phase-2-planning-spine-exceptions`
- `phase-2-safe-canonical-batch` is explicitly first
- the safe canonical batch list contains exactly the nine frozen skills
- the plan states that `skills/` is canonical and `.github/skills/` plus
  `.codex/skills/` are non-authority surfaces
- the plan states that `.codex/skills/` is a partial projection surface only
- the plan states that each later slice needs its own plan, review,
  human-check, and PR
- the plan states that slice PR order is strictly serialized
- `docs/status.md` is treated as optional overview only
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

- This topic does not require stable-library updates.
- This topic does not require `README.md` changes.
- This topic does not require `VERSION` changes.
- This topic does not require release or tagging work.
- Any later slice that affects stable-library surfaces must make its own timing
  decision in its own plan.

## Open Questions / Unresolved Items

- Whether later slice topics will need their own `summary.md` or `review-log.md`
  artifacts depends on their concrete workflow and must be decided per slice.
- Whether `docs/status.md` is worth creating as optional overview remains a
  human coordination choice, not an umbrella baseline requirement.
- If future evidence changes the safe canonical batch list or slice order, a
  separate planning repair topic is required instead of editing slice plans by
  assumption.
