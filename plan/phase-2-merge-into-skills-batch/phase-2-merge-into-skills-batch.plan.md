# phase-2-merge-into-skills-batch

## Goal / Outcome

Produce repo-visible execution truth for the merge-required Phase 2 batch after
bounded canonical convergence under `skills/`, without silently collapsing
semantic, alias, or behavior drift or widening into compatibility-surface
materialization.

When this topic is complete:

- the exact ten-candidate merge batch is frozen,
- bounded convergence remains limited to canonical `skills/` content only,
- completed canonical edits and no-edit-needed determinations are recorded
  truthfully for the frozen candidates,
- compatibility-surface differences do not block progress when `skills/` is
  already canonical,
- and the topic is ready for the remaining human-check gate on the committed
  execution truth.

## Scope

- **In scope**:
  - create `analysis/phase-2-merge-into-skills-batch/requirements.md`
  - create `analysis/phase-2-merge-into-skills-batch/technical-spec.md`
  - create `plan/phase-2-merge-into-skills-batch/phase-2-merge-into-skills-batch.plan.md`
  - create `plan/phase-2-merge-into-skills-batch/phase-2-merge-into-skills-batch.step.md`
  - freeze the exact merge-batch candidate set
  - execute bounded canonical convergence only under `skills/<skill-name>/...`
  - allow path convergence, semantic convergence, or both together when the
    canonical `skills/` content requires it
  - record evidence-backed semantic / alias / behavior drift concerns
  - record completed canonical edits and `no canonical edit needed`
    determinations for the frozen candidates
  - treat `.github/**` and `.codex/**` as read-only reference inputs only

- **Out of scope**:
  - editing `.github/skills/**`
  - editing `.codex/skills/**`
  - editing `.github/agents/**`
  - editing `.codex/agents/**`
  - editing shared contract files
  - editing umbrella topic artifacts
  - `phase-2-safe-canonical-batch`
  - `phase-2-planning-spine-exceptions`
  - projection materialization
  - runtime adaptation
  - copilot-only work

## Locked Decisions

### 1. Current workflow stage is merged and terminal

- This topic is no longer planning-only.
- Bounded canonical convergence under `skills/` has completed for the current
  execution slice.
- Formal review and final verification are complete on the committed execution
  truth.
- Human-check completed before merge.
- PR `#107` merged this topic into `feat/andrew/phase-2-umbrella` at merge
  commit `a07c015`.

### 2. Parent umbrella baseline is fixed

- This topic branches from approved umbrella coordination baseline.
- Umbrella decisions about canonical target, non-authority surfaces, and slice
  ordering are treated as frozen planning inputs here.
- This topic remains a child slice under that approved coordination baseline.

### 3. Canonical and non-authority surface model is fixed

- `skills/` is the canonical convergence target.
- `.github/skills/` is a read-only compatibility surface, not an authority
  source tree.
- `.codex/skills/` is a read-only compatibility surface, not an authority
  source tree.
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

### 5. Current bounded execution outcome is frozen

- Canonical edits were completed only for:
  - `agent-skill-template` at commit `0528a54`
  - `agent-skill-creator` at commit `0f841da`
- The following candidates were checked and required no canonical edit:
  - `python-pyproject-toolconfig`
  - `python-blueprint-authoring`
  - `python-library-architecture`
  - `python-package-layout`
  - `python-plan-authoring`
  - `python-pre-commit`
  - `python-tdd-test-authoring`
  - `python-blueprint-review`
- Remaining compatibility-surface differences under `.github/**` or `.codex/**`
  do not block progress when the canonical `skills/` content is already
  correct.

### 6. Bounded convergence must stay within canonical `skills/` and the frozen candidate set only

- Execution under this topic may target only the exact ten listed candidates.
- No additional skill may be added by analogy or convenience.
- Only canonical `skills/<skill-name>/...` files may be edited under this
  topic.
- `.github/**` and `.codex/**` remain read-only reference inputs.

### 7. Drift discussion remains mandatory where canonical content actually needs change

- Phase 1 evidence classifies this batch as merge-required rather than safe
  canonical adoption.
- Path drift, semantic drift, or both together are allowed convergence modes
  when the canonical `skills/` content actually needs repair.
- This topic must not silently collapse semantic, alias, or behavior drift by
  convenience.

### 8. Out-of-scope work types remain fixed

- `phase-2-safe-canonical-batch` remains out of scope.
- `phase-2-planning-spine-exceptions` remains out of scope.
- Projection materialization remains out of scope.
- Runtime adaptation remains out of scope.
- Copilot-only work remains out of scope.
- `docs/status.md` remains optional only.

## Boundaries / Exclusions

- Do not edit `.github/**`, `.codex/**`, or non-topic skill surfaces.
- Do not widen into safe canonical batch handling.
- Do not widen into planning-spine exception handling.
- Do not widen into `.codex/skills/` materialization or projection repair.
- Do not widen into runtime adaptation or adapter design.
- Do not widen into copilot-only legacy handling.
- Do not use `docs/status.md` as execution truth or success prerequisite.
- Do not treat compatibility-surface drift by itself as a blocker when
  canonical `skills/` content is already correct.

## Status / Allowed Transitions

- **Current**: `merged`
- **Execution model**: bounded canonical convergence under `skills/` completed
  for this slice and the topic is now merged into the umbrella parent branch
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

- The planning baseline under this topic was used as the execution parent for
  the completed bounded canonical convergence slice.
- Further execution under this topic must still begin from this topic plan, not
  from a chat summary or from raw Phase 1 reports alone.
- This topic branch no longer carries active execution after merge.
- Any attempt to widen beyond canonical `skills/` edits or beyond the frozen
  candidate set is plan drift.

## Artifact Paths

| Artifact | Path | Owner | Role |
| --- | --- | --- | --- |
| Requirements baseline | `analysis/phase-2-merge-into-skills-batch/requirements.md` | Planning actor | Frozen requirements baseline for the merge-required candidate batch |
| Technical baseline | `analysis/phase-2-merge-into-skills-batch/technical-spec.md` | Planning actor | Frozen technical translation for candidate drift handling and bounded canonical convergence policy |
| Topic plan | `plan/phase-2-merge-into-skills-batch/phase-2-merge-into-skills-batch.plan.md` | Planning actor | Repo-visible execution contract for the merge-required batch |
| Topic progression artifact | `plan/phase-2-merge-into-skills-batch/phase-2-merge-into-skills-batch.step.md` | Planning actor | Current-truth workflow progression status for this topic |
| Governance canonical source | `AGENTS.md` | Existing repo artifact | Read-only governance authority source |
| Positioning contract | `docs/repo-positioning.md` | Existing repo artifact | Read-only positioning evidence for canonical and projection boundaries |
| Repo workflow contract | `plan/agent-handoff-workflow.md` | Existing repo artifact | Read-only workflow-phase and truth-artifact authority |
| Shared topic-plan contract | `plan/topic-plan-contract.md` | Existing repo artifact | Read-only topic-plan structure and blocking-semantics authority |
| Umbrella parent plan | `plan/phase-2-umbrella/phase-2-umbrella.plan.md` | Existing repo artifact | Read-only parent coordination baseline for slice ordering and boundaries |
| Umbrella parent progression artifact | `plan/phase-2-umbrella/phase-2-umbrella.step.md` | Existing repo artifact | Read-only evidence that umbrella approval exists and this slice may be planned |
| Canonical skill surface | `skills/agent-skill-template/` | Existing repo artifact | Canonical skill folder edited in bounded convergence commit `0528a54` |
| Canonical skill surface | `skills/agent-skill-creator/` | Existing repo artifact | Canonical skill folder edited in bounded convergence commit `0f841da` |
| Merge-batch candidates evidence | `docs/agent-skills-convergence/phase-1/06-convergence-candidates.md` | Existing repo artifact | Read-only evidence that this exact batch is merge-required |
| Phase 2 inputs evidence | `docs/agent-skills-convergence/phase-1/07-phase-2-inputs.md` | Existing repo artifact | Read-only evidence that these candidates belong to the merge batch |
| Semantic drift evidence | `docs/agent-skills-convergence/phase-1/04-semantic-drift-report.md` | Existing repo artifact | Read-only evidence for semantic / behavior-changing drift that blocks blind collapse |
| Runtime dependency evidence | `docs/agent-skills-convergence/phase-1/05-runtime-dependency-inventory.md` | Existing repo artifact | Read-only evidence for projection-required or runtime-sensitive candidates |
| Analysis prompt guidance | `.github/prompts/create-analysis.prompt.md` | Existing repo artifact | Read-only evidence for analysis-layer output expectations |
| Plan prompt guidance | `.github/prompts/create-agent-plan.prompt.md` | Existing repo artifact | Read-only evidence for repo-visible topic-plan expectations |

Artifact path notes:

- This topic does not create `plan/phase-2-merge-into-skills-batch/phase-2-merge-into-skills-batch.review-log.md`.
- This topic does not create `plan/phase-2-merge-into-skills-batch/phase-2-merge-into-skills-batch.summary.md`.
- If later review determines either artifact is required for this topic, treat
  that as `human_review_required` rather than widening scope silently.

## Implementation Steps

1. Read repo governance, workflow, topic-plan contract, umbrella baseline, and
   Phase 1 merge-batch evidence before drafting the topic plan.
2. Freeze the exact ten-candidate merge batch with no additions or removals.
3. Preserve the rule that `skills/` is canonical and `.github/skills/` plus
   `.codex/skills/` are read-only compatibility surfaces, with `.codex/skills/`
   only as a partial projection surface.
4. Perform bounded path convergence, semantic convergence, or both together
   only under canonical `skills/<skill-name>/...` when evidence shows the
   canonical content needs change.
5. Record completed canonical edits for `agent-skill-template` and
   `agent-skill-creator`, including their topic-local commits.
6. Record `no canonical edit needed` for the eight remaining checked
   candidates.
7. Preserve explicit exclusions for planning-spine exception handling,
   projection materialization, runtime adaptation, and copilot-only work.
8. Stop and route to `human_review_required` if topic-local work would
   require:
   - any file outside the declared write set
   - any shared contract file edit
   - any umbrella artifact edit
   - any `.github/**` or `.codex/**` edit

## Validation / Acceptance Checks

- `analysis/phase-2-merge-into-skills-batch/requirements.md` exists and
  freezes the merge-batch planning requirements
- `analysis/phase-2-merge-into-skills-batch/technical-spec.md` exists and maps
  those requirements to bounded execution work
- `plan/phase-2-merge-into-skills-batch/phase-2-merge-into-skills-batch.plan.md`
  exists and uses canonical topic-plan sections
- `plan/phase-2-merge-into-skills-batch/phase-2-merge-into-skills-batch.step.md`
  exists and provides progression truth for this execution-active topic
- the exact merge-batch candidate set contains only the ten frozen candidates
- the plan states bounded convergence is limited to canonical `skills/`
- the plan states `skills/` is canonical and `.github/skills/` /
  `.codex/skills/` are read-only compatibility surfaces
- the plan states `.codex/skills/` is a partial projection surface only
- the plan records the two completed canonical edit commits
- the plan records the eight `no canonical edit needed` determinations
- the plan states compatibility-surface differences do not block progress when
  canonical `skills/` is already correct
- the plan lists the two canonical skill surfaces that were actually edited
- the plan states semantic / alias / behavior drift must not be collapsed by
  assumption when canonical content actually needs change
- the plan excludes planning-spine exceptions, projection materialization,
  runtime adaptation, and copilot-only work
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

- This bounded execution slice does not require stable-library updates.
- This bounded execution slice does not require `README.md` changes.
- This bounded execution slice does not require `VERSION` changes.
- This bounded execution slice does not require release or tagging work.
- If later work under this topic would affect stable-library surfaces, that
  timing must be decided in later review rather than inferred here.

## Open Questions / Unresolved Items

- Human-check has not yet been completed on the updated execution truth.
- Whether later workflow conditions require a `review-log.md` or `summary.md`
  artifact remains unresolved and is not widened in this topic-local repair.
