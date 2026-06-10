# phase-2-planning-spine-exceptions

## Goal / Outcome

Produce a repo-visible planning and execution baseline for the final Phase 2
slice that isolates planning-spine exceptions to `skills/plan-creator/**` and
`skills/plan-reviewer/**`, without widening into compatibility surfaces,
projection work, runtime adaptation, or unrelated governance rewrite.

When this topic is complete:

- the bounded skill set is frozen exactly to `plan-creator` and
  `plan-reviewer`,
- the canonical convergence target remains `skills/`,
- later execution is explicitly limited to those two canonical skill surfaces,
- high-impact authority, workflow, handoff, and blocked-behavior questions are
  carried forward as `human_review_required`,
- and no downstream actor needs to guess whether this slice authorizes edits to
  `.github/**`, `.codex/**`, or unrelated skills.

## Scope

- **In scope**:
  - create `analysis/phase-2-planning-spine-exceptions/requirements.md`
  - create `analysis/phase-2-planning-spine-exceptions/technical-spec.md`
  - create `plan/phase-2-planning-spine-exceptions/phase-2-planning-spine-exceptions.plan.md`
  - create `plan/phase-2-planning-spine-exceptions/phase-2-planning-spine-exceptions.step.md`
  - freeze the exact skill set:
    - `skills/plan-creator/**`
    - `skills/plan-reviewer/**`
  - define canonical convergence rules for those two skill surfaces inside
    `skills/`
  - define which decisions remain `human_review_required` before later
    execution may change behavior

- **Out of scope**:
  - editing `.github/**`
  - editing `.codex/**`
  - editing `.github/agents/**`
  - editing `.codex/agents/**`
  - projection materialization
  - runtime adaptation
  - copilot-only convergence
  - direct convergence for unrelated skills
  - repo-level workflow or contract rewrites unless a later explicitly
    approved scope change authorizes them

## Locked Decisions

### 1. This is the final Phase 2 execution slice

- `phase-2-planning-spine-exceptions` is the remaining final Phase 2 slice
  after:
  - `phase-2-safe-canonical-batch`
  - `phase-2-merge-into-skills-batch`
- It is not a replacement umbrella topic.
- It does not reopen broad Phase 2 framing.

### 2. Canonical and compatibility surfaces are fixed

- `skills/` is the canonical convergence target.
- `.github/**` and `.codex/**` are read-only reference inputs only.
- `.codex/skills/` remains a partial projection surface only.

### 3. Bounded execution targets are fixed

Later execution under this topic may modify only:

- `skills/plan-creator/**`
- `skills/plan-reviewer/**`

No other skill surface may be added by analogy or convenience.

### 4. Repo-level authority ordering remains above the skills

Use this order when planning-spine authority questions arise:

1. `AGENTS.md`
2. `plan/agent-handoff-workflow.md`
3. `plan/topic-plan-contract.md`
4. `plan/<topic>/<topic>.plan.md`
5. `skills/plan-creator/**` and `skills/plan-reviewer/**`

The skills are consumer guidance and convergence targets here, not repo-level
authority owners.

### 5. Human-review-required items are preserved, not guessed

The following remain `human_review_required` until later execution gathers
enough evidence to prove they are wording-only:

- exact fallback wording in `plan-creator` where shared contract sources are
  absent
- exact blocked behavior in `plan-reviewer` when plan or shared contract
  sources are unreadable
- any skill-local instruction that appears to reinterpret repo-level workflow,
  handoff, or close semantics
- any change that would move behavior rather than merely neutralize
  platform-specific wording

### 6. Stable-library intent is explicitly absent

- This topic is not a stable-library release topic.
- No `README.md` update belongs here.
- No `VERSION` update belongs here.
- No release note, tag, or post-merge release work belongs here.

## Boundaries / Exclusions

- Do not edit `.github/**` or `.codex/**`.
- Do not widen into `agent-skill-creator`, `agent-skill-reviewer`,
  `agent-skill-template`, `python-blueprint-review`, or unrelated skills.
- Do not widen into projection build-out or runtime adaptation.
- Do not silently collapse semantic, behavior, or authority drift.
- Do not rewrite repo-level workflow or plan-contract meaning under this topic
  unless a later approved scope change explicitly authorizes it.
- Do not use `docs/status.md` as execution truth or a success prerequisite.

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

- The planning baseline under this topic was approved and used as the execution
  parent for the completed bounded convergence work.
- The completed convergence target was canonical wording and path convergence
  under `skills/plan-creator/**` and `skills/plan-reviewer/**`.
- Execution remains bounded to canonical `skills/` only; `.github/**` and
  `.codex/**` remain read-only compatibility surfaces.
- Execution review and final verification found no new contract-breaking
  blocker in the committed bounded convergence truth.
- Human approval completed on the committed bounded convergence truth.
- PR `#108` merged this topic into `feat/andrew/phase-2-umbrella` at merge
  commit `8305177`.
- This topic is now merged and terminal under the current execution policy.
- No additional execution remains authorized under this topic branch.
- Any attempt to widen beyond the two frozen canonical skill surfaces is plan
  drift.

## Artifact Paths

| Artifact | Path | Owner | Role |
| --- | --- | --- | --- |
| Requirements baseline | `analysis/phase-2-planning-spine-exceptions/requirements.md` | Planning actor | Frozen requirements baseline for the planning-spine exception slice |
| Technical baseline | `analysis/phase-2-planning-spine-exceptions/technical-spec.md` | Planning actor | Frozen technical translation for bounded convergence and preserved exception handling |
| Topic plan | `plan/phase-2-planning-spine-exceptions/phase-2-planning-spine-exceptions.plan.md` | Planning actor | Repo-visible execution contract for the final Phase 2 exception slice |
| Topic progression artifact | `plan/phase-2-planning-spine-exceptions/phase-2-planning-spine-exceptions.step.md` | Planning actor | Current-truth workflow progression status for this topic |
| Governance canonical source | `AGENTS.md` | Existing repo artifact | Read-only governance authority source |
| Positioning contract | `docs/repo-positioning.md` | Existing repo artifact | Read-only positioning evidence for canonical and projection boundaries |
| Repo workflow contract | `plan/agent-handoff-workflow.md` | Existing repo artifact | Read-only workflow-phase and truth-artifact authority |
| Shared topic-plan contract | `plan/topic-plan-contract.md` | Existing repo artifact | Read-only topic-plan structure and blocking-semantics authority |
| Umbrella parent plan | `plan/phase-2-umbrella/phase-2-umbrella.plan.md` | Existing repo artifact | Read-only parent coordination baseline for slice ordering and boundaries |
| Umbrella parent progression artifact | `plan/phase-2-umbrella/phase-2-umbrella.step.md` | Existing repo artifact | Read-only evidence that umbrella approval exists and this final slice may be planned |
| Safe-batch progression artifact | `plan/phase-2-safe-canonical-batch/phase-2-safe-canonical-batch.step.md` | Existing repo artifact | Read-only evidence that the first execution slice is complete |
| Merge-batch plan | `plan/phase-2-merge-into-skills-batch/phase-2-merge-into-skills-batch.plan.md` | Existing repo artifact | Read-only evidence for the completed second execution slice and canonical-only policy |
| Merge-batch progression artifact | `plan/phase-2-merge-into-skills-batch/phase-2-merge-into-skills-batch.step.md` | Existing repo artifact | Read-only evidence that the second execution slice is complete and merged |
| Canonical planning skill surface | `skills/plan-creator/**` | Existing repo artifact | Later bounded execution target for creator-side planning-spine convergence |
| Canonical planning skill surface | `skills/plan-reviewer/**` | Existing repo artifact | Later bounded execution target for reviewer-side planning-spine convergence |
| Semantic drift evidence | `docs/agent-skills-convergence/phase-1/04-semantic-drift-report.md` | Existing repo artifact | Read-only evidence that both planning-spine skills remain high-risk human-review items |
| Runtime dependency evidence | `docs/agent-skills-convergence/phase-1/05-runtime-dependency-inventory.md` | Existing repo artifact | Read-only evidence that both planning-spine skills are projection-required and path-sensitive |
| Convergence candidates evidence | `docs/agent-skills-convergence/phase-1/06-convergence-candidates.md` | Existing repo artifact | Read-only evidence that both skills were frozen for human review rather than earlier convergence |
| Phase 2 inputs evidence | `docs/agent-skills-convergence/phase-1/07-phase-2-inputs.md` | Existing repo artifact | Read-only evidence that both skills require human decision before convergence |
| Human-review verdict evidence | `docs/agent-skills-convergence/phase-1/09-human-review-verdict.md` | Existing repo artifact | Read-only evidence that shared plan-contract authority moved above both skills |
| Analysis prompt guidance | `.github/prompts/create-analysis.prompt.md` | Existing repo artifact | Read-only evidence for analysis-layer output expectations |
| Plan prompt guidance | `.github/prompts/create-agent-plan.prompt.md` | Existing repo artifact | Read-only evidence for repo-visible topic-plan expectations |

Artifact path notes:

- This topic does not create `plan/phase-2-planning-spine-exceptions/phase-2-planning-spine-exceptions.review-log.md`.
- This topic does not create `plan/phase-2-planning-spine-exceptions/phase-2-planning-spine-exceptions.summary.md`.
- If later workflow routing determines either artifact is required, treat that
  as `human_review_required` rather than widening scope silently.

## Implementation Steps

1. Read repo governance, workflow, shared topic-plan contract, umbrella
   baseline, prior slice artifacts, and Phase 1 planning-spine evidence before
   drafting the topic plan.
2. Freeze the exact bounded skill set to:
   - `skills/plan-creator/**`
   - `skills/plan-reviewer/**`
3. Preserve the rule that `skills/` is canonical while `.github/**` and
   `.codex/**` remain read-only compatibility surfaces.
4. Perform bounded canonical convergence only under those two canonical skill
   surfaces, including:
   - path-neutralization away from platform-specific roots
   - wording cleanup that restores canonical terminology
   - removal of unnecessary platform-bound phrasing where hard behavior stays
     unchanged
5. Record the completed low-risk convergence slices:
   - `skills/plan-reviewer/checklist.md`
   - `skills/plan-reviewer/reference.md`
   - `skills/plan-reviewer/SKILL.md`
   - `skills/plan-creator/checklist.md`
   - `skills/plan-creator/reference.md`
   - `skills/plan-creator/SKILL.md`
   - `skills/plan-creator/examples.md`
6. Record explicit `human_review_required` items for any change that may alter:
   - fallback behavior
   - blocked behavior
   - reviewer handoff semantics
   - workflow or close semantics
7. Preserve explicit exclusions for projection materialization, runtime
   adaptation, copilot-only work, and unrelated skill convergence.
8. Stop and route to `human_review_required` if later topic-local work would
   require:
   - any file outside the declared write set
   - any `.github/**` or `.codex/**` edit
   - any repo-level workflow or contract rewrite

## Validation / Acceptance Checks

- `analysis/phase-2-planning-spine-exceptions/requirements.md` exists and
  freezes the bounded exception topic requirements
- `analysis/phase-2-planning-spine-exceptions/technical-spec.md` exists and
  maps those requirements to bounded later execution
- `plan/phase-2-planning-spine-exceptions/phase-2-planning-spine-exceptions.plan.md`
  exists and uses canonical topic-plan sections
- `plan/phase-2-planning-spine-exceptions/phase-2-planning-spine-exceptions.step.md`
  exists and provides progression truth for this topic
- the topic plan lists only `skills/plan-creator/**` and
  `skills/plan-reviewer/**` as later execution targets
- the topic plan states `skills/` is canonical and `.github/**` plus
  `.codex/**` are read-only compatibility surfaces
- the topic plan states `.codex/skills/` is a partial projection surface only
- the topic plan explicitly records non-stable intent
- the topic plan explicitly preserves `human_review_required` items rather than
  guessing
- completed canonical convergence remains bounded to:
  - `skills/plan-creator/**`
  - `skills/plan-reviewer/**`
- no `.github/**` or `.codex/**` file is modified
- no unrelated skill surface is modified

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

- No stable-library release action belongs to this topic.
- No README, VERSION, release note, or tag work belongs to this topic.
- If later execution is approved, publish routing should remain bounded to this
  topic branch and its parent umbrella branch only.

## Open Questions / Unresolved Items

- `human_review_required`: Can `plan-creator` fallback wording be
  canonicalized without changing failure behavior?
- `human_review_required`: Does `plan-reviewer` blocked behavior when shared
  sources are unreadable already conflict with repo-level contract semantics?
- `human_review_required`: Does `skills/plan-reviewer/examples.md` contain any
  remaining safe wording-only cleanup, or is the rest example-contract-bearing?
- `human_review_required`: Which remaining skill-local examples or references
  are wording-only versus behavior-bearing?
- `human_review_required`: Is any later execution allowed to touch templates or
  references beyond the minimum needed to restore canonical authority wording?
