# phase-2-merge-into-skills-batch

## Goal / Outcome

Produce a repo-visible planning baseline for the merge-required Phase 2 batch
so later creator execution can evaluate and merge divergent or GitHub-only
material into `skills/` without silently collapsing semantic, alias, or
behavior drift.

When this topic is complete:

- the exact ten-candidate merge batch is frozen,
- the current workflow stage is explicitly planning-only,
- later merge implementation is bounded to those ten candidates only,
- and unsupported exact merge policy or exact later write-scope decisions are
  surfaced as `human_review_required`.

## Scope

- **In scope**:
  - create `analysis/phase-2-merge-into-skills-batch/requirements.md`
  - create `analysis/phase-2-merge-into-skills-batch/technical-spec.md`
  - create `plan/phase-2-merge-into-skills-batch/phase-2-merge-into-skills-batch.plan.md`
  - create `plan/phase-2-merge-into-skills-batch/phase-2-merge-into-skills-batch.step.md`
  - freeze the exact merge-batch candidate set
  - define planning-stage boundaries for later merge-required convergence work
  - record evidence-backed semantic / alias / behavior drift concerns
  - record where later merge policy or exact write scope remains `human_review_required`

- **Out of scope**:
  - editing `skills/**`
  - editing `.github/skills/**`
  - editing `.codex/skills/**`
  - editing `.github/agents/**`
  - editing `.codex/agents/**`
  - editing shared contract files
  - editing umbrella topic artifacts
  - any merge implementation in this turn
  - `phase-2-safe-canonical-batch`
  - `phase-2-planning-spine-exceptions`
  - projection materialization
  - runtime adaptation
  - copilot-only work

## Locked Decisions

### 1. Current workflow stage is planning only

- This turn is planning only.
- No merge implementation starts in the current workflow stage.
- Later creator execution under this topic requires separate downstream review
  and human gates.

### 2. Parent umbrella baseline is fixed

- This topic branches from approved umbrella coordination baseline.
- Umbrella decisions about canonical target, non-authority surfaces, and slice
  ordering are treated as frozen planning inputs here.
- This topic remains a child slice under that approved coordination baseline.

### 3. Canonical and non-authority surface model is fixed

- `skills/` is the canonical convergence target.
- `.github/skills/` is not an authority source tree.
- `.codex/skills/` is not an authority source tree.
- `.codex/skills/` is only a partial projection surface.

### 4. Merge-batch candidate set is frozen exactly

The merge-batch candidate set is frozen to:

- `agent-skill-creator`
- `agent-skill-template`
- `python-blueprint-authoring`
- `python-library-architecture`
- `python-package-layout`
- `python-plan-authoring`
- `python-pre-commit`
- `python-pyproject-toolconfig`
- `python-tdd-test-authoring`
- `python-blueprint-review`

### 5. Drift discussion is expected and mandatory

- Phase 1 evidence classifies this batch as merge-required rather than safe
  canonical adoption.
- Semantic drift, alias/path drift, behavior drift, reference-set expansion,
  template/script/test additions, and missing canonical counterpart risks must
  be surfaced explicitly.
- This topic must not silently collapse those differences into `skills/` by
  convenience.

### 6. Later merge implementation must stay bounded to the frozen candidate set only

- Later execution under this topic may target only the exact ten listed
  candidates.
- No additional skill may be added by analogy or convenience.
- If later merge work would require scope beyond the frozen set, stop and route
  to `human_review_required`.

### 7. Exact merge policy is not fully frozen by current evidence

- Current evidence is sufficient to prove that merge policy discussion is
  required.
- Current evidence is not sufficient to choose one exact merge policy for every
  candidate without some human judgment.
- Exact later merge policy is therefore `human_review_required` where
  evidence does not decide between alternatives honestly.

### 8. Exact later write scope is not fully frozen by current evidence

- Current evidence is sufficient to freeze topic boundaries and candidate
  membership.
- Current evidence is not sufficient to invent one exact per-file later write
  scope across all merge-required candidates without guessing.
- Exact later implementation write scope is therefore
  `human_review_required` if downstream work cannot derive it honestly from
  then-current evidence.

### 9. Out-of-scope work types are fixed

- `phase-2-safe-canonical-batch` remains out of scope.
- `phase-2-planning-spine-exceptions` remains out of scope.
- Projection materialization remains out of scope.
- Runtime adaptation remains out of scope.
- Copilot-only work remains out of scope.
- `docs/status.md` remains optional only.

## Boundaries / Exclusions

- Do not edit any skill or agent surface in this planning turn.
- Do not widen into safe canonical batch handling.
- Do not widen into planning-spine exception handling.
- Do not widen into `.codex/skills/` materialization or projection repair.
- Do not widen into runtime adaptation or adapter design.
- Do not widen into copilot-only legacy handling.
- Do not use `docs/status.md` as execution truth or success prerequisite.
- Do not treat the current planning artifacts as merge implementation approval.

## Status / Allowed Transitions

- **Current**: `planned`
- **Execution model**: planning baseline first, later bounded creator merge
  execution only after normal review and human gates
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

- In the current turn, only planning artifacts are produced.
- Later creator merge execution must begin from this topic plan, not from a
  chat summary or from raw Phase 1 reports alone.
- Any attempt to start merge execution from current planning evidence alone
  without resolving exact merge policy or exact later write scope where needed
  is plan drift.

## Artifact Paths

| Artifact | Path | Owner | Role |
| --- | --- | --- | --- |
| Requirements baseline | `analysis/phase-2-merge-into-skills-batch/requirements.md` | Planning actor | Frozen planning baseline for the merge-required candidate batch |
| Technical baseline | `analysis/phase-2-merge-into-skills-batch/technical-spec.md` | Planning actor | Frozen technical translation for candidate drift handling and deferred merge-policy / write-scope decisions |
| Topic plan | `plan/phase-2-merge-into-skills-batch/phase-2-merge-into-skills-batch.plan.md` | Planning actor | Repo-visible execution contract for the merge-required batch |
| Topic progression artifact | `plan/phase-2-merge-into-skills-batch/phase-2-merge-into-skills-batch.step.md` | Planning actor | Current-truth workflow progression status for this topic |
| Governance canonical source | `AGENTS.md` | Existing repo artifact | Read-only governance authority source |
| Positioning contract | `docs/repo-positioning.md` | Existing repo artifact | Read-only positioning evidence for canonical and projection boundaries |
| Repo workflow contract | `plan/agent-handoff-workflow.md` | Existing repo artifact | Read-only workflow-phase and truth-artifact authority |
| Shared topic-plan contract | `plan/topic-plan-contract.md` | Existing repo artifact | Read-only topic-plan structure and blocking-semantics authority |
| Umbrella parent plan | `plan/phase-2-umbrella/phase-2-umbrella.plan.md` | Existing repo artifact | Read-only parent coordination baseline for slice ordering and boundaries |
| Umbrella parent progression artifact | `plan/phase-2-umbrella/phase-2-umbrella.step.md` | Existing repo artifact | Read-only evidence that umbrella approval exists and this slice may be planned |
| Merge-batch candidates evidence | `docs/agent-skills-convergence/phase-1/06-convergence-candidates.md` | Existing repo artifact | Read-only evidence that this exact batch is merge-required |
| Phase 2 inputs evidence | `docs/agent-skills-convergence/phase-1/07-phase-2-inputs.md` | Existing repo artifact | Read-only evidence that these candidates belong to the merge batch |
| Semantic drift evidence | `docs/agent-skills-convergence/phase-1/04-semantic-drift-report.md` | Existing repo artifact | Read-only evidence for semantic / behavior-changing drift that blocks blind collapse |
| Runtime dependency evidence | `docs/agent-skills-convergence/phase-1/05-runtime-dependency-inventory.md` | Existing repo artifact | Read-only evidence for projection-required or runtime-sensitive candidates |
| Analysis prompt guidance | `.github/prompts/create-analysis.prompt.md` | Existing repo artifact | Read-only evidence for analysis-layer output expectations |
| Plan prompt guidance | `.github/prompts/create-agent-plan.prompt.md` | Existing repo artifact | Read-only evidence for repo-visible topic-plan expectations |

Artifact path notes:

- This topic does not create `plan/phase-2-merge-into-skills-batch/phase-2-merge-into-skills-batch.review-log.md`.
- This topic does not create `plan/phase-2-merge-into-skills-batch/phase-2-merge-into-skills-batch.summary.md`.
- If planning-stage review later determines either artifact is required for
  this topic, treat that as `human_review_required` rather than widening scope
  silently.

## Implementation Steps

1. Read repo governance, workflow, topic-plan contract, umbrella baseline, and
   Phase 1 merge-batch evidence before drafting the topic plan.
2. Record that this topic is planning-only in the current workflow stage and
   that no merge implementation starts now.
3. Freeze the exact ten-candidate merge batch with no additions or removals.
4. Preserve the rule that `skills/` is canonical and `.github/skills/` plus
   `.codex/skills/` are non-authority surfaces, with `.codex/skills/` only as
   a partial projection surface.
5. Encode that semantic / alias / behavior drift must be discussed explicitly
   and must not be silently collapsed.
6. Encode explicit exclusions for safe canonical batch work, planning-spine
   exception handling, projection materialization, runtime adaptation, and
   copilot-only work.
7. Mark exact later merge policy as `human_review_required` wherever current
   evidence would otherwise force guessing.
8. Mark exact later implementation write scope as `human_review_required`
   wherever current evidence would otherwise force guessing.
9. Stop and route to `human_review_required` if planning-stage work would
   require:
   - any file outside the declared write set
   - any shared contract file edit
   - any umbrella artifact edit
   - any implementation edit under skill or agent surfaces

## Validation / Acceptance Checks

- `analysis/phase-2-merge-into-skills-batch/requirements.md` exists and
  freezes the merge-batch planning requirements
- `analysis/phase-2-merge-into-skills-batch/technical-spec.md` exists and maps
  those requirements to bounded planning work
- `plan/phase-2-merge-into-skills-batch/phase-2-merge-into-skills-batch.plan.md`
  exists and uses canonical topic-plan sections
- `plan/phase-2-merge-into-skills-batch/phase-2-merge-into-skills-batch.step.md`
  exists and provides progression truth for this planning turn
- the exact merge-batch candidate set contains only the ten frozen candidates
- the plan states current work is planning only
- the plan states `skills/` is canonical and `.github/skills/` /
  `.codex/skills/` are non-authority surfaces
- the plan states `.codex/skills/` is a partial projection surface only
- the plan states semantic / alias / behavior drift must not be collapsed by
  assumption
- the plan excludes planning-spine exceptions, projection materialization,
  runtime adaptation, and copilot-only work
- the plan marks unsupported exact later merge policy as
  `human_review_required`
- the plan marks unsupported exact later write scope as
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
- If later creator execution under this topic affects stable-library surfaces,
  that timing must be decided in later execution review, not inferred now.

## Open Questions / Unresolved Items

- Exact later merge policy remains `human_review_required` wherever current
  evidence does not decide among alternatives honestly.
- Exact later per-file write scope remains `human_review_required` unless later
  evidence makes it explicit without guessing.
- Whether later execution under this topic will require a `review-log.md` or
  `summary.md` artifact depends on then-current workflow conditions and is not
  created in this planning turn.
