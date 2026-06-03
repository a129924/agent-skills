# Agent Skills Convergence Phase 1 Plan

## Goal / Outcome

Produce one bounded, repo-visible Phase 1 evidence topic that:

- creates the required 9 Phase 1 files under
  `docs/agent-skills-convergence/phase-1/`,
- inventories and compares the current observed state of `skills/`,
  `.github/skills/`, and `.codex/skills/`,
- classifies drift, Copilot-only candidates, and runtime dependency surfaces
  conservatively,
- prepares Phase 2 and Phase 3 inputs without implementing either phase,
- and preserves a hard stop before any skill-content convergence, projection
  materialization, or runtime adaptation.

When this topic is complete:

- the repository has one repo-visible Phase 1 report bundle,
- report scope and stop rules are explicit,
- subAgent evidence contracts are frozen in repo-visible planning artifacts,
- and later human review can decide whether evidence is sufficient to start
  Phase 2.

## Scope

- **In scope**:
  - create `analysis/agent-skills-convergence-phase-1/requirements.md`
  - create `analysis/agent-skills-convergence-phase-1/technical-spec.md`
  - create `plan/agent-skills-convergence-phase-1/agent-skills-convergence-phase-1.plan.md`
  - create `plan/agent-skills-convergence-phase-1/agent-skills-convergence-phase-1.step.md`
  - create `plan/agent-skills-convergence-phase-1/agent-skills-convergence-phase-1.review-log.md` when review routing is needed
  - create the 9 Phase 1 files under `docs/agent-skills-convergence/phase-1/`
  - read and compare `skills/`, `.github/skills/`, `.codex/skills/`, and supporting governance / migration evidence

- **Out of scope**:
  - modifying `skills/**`
  - modifying `.github/skills/**`
  - modifying `.codex/skills/**`
  - modifying scripts, hooks, templates, tests, or agent files
  - creating `.codex/skills/<skill-name>/`
  - creating `.codex/agents/` or `.github/agents/`
  - implementing convergence, projection, sync, or runtime adaptation
  - auto-resolving aliases
  - README, VERSION, release, or stable-library work

## Locked Decisions

### 1. Topic type: Phase 1 reporting only

- This topic is a reporting and evidence topic only.
- It does not perform skill convergence.
- It does not select or enforce canonical truth by implementation.

### 2. Governance target is later-phase only

- Later convergence is expected to center `skills/` as the canonical skill
  source of truth.
- Phase 1 records that target direction as governance context only.
- `.github/skills/` and `.codex/skills/` are evaluated here as projection,
  compatibility, provenance, or platform-adapter surfaces unless evidence
  proves a blocker or requires `human_review_required`.

### 3. Read-only boundary for skill surfaces is fixed

The following surfaces are read-only in this topic:

- `skills/**`
- `.github/skills/**`
- `.codex/skills/**`

No skill, script, hook, template, test, or agent file under those surfaces may
be edited.

### 4. Stop rules are fixed

This topic must not:

- copy skill content between `skills/` and `.github/skills/`
- delete, rename, normalize, or reformat any existing skill file
- overwrite `.codex/skills/`
- create `.codex/skills/<skill-name>/`
- resolve alias candidates automatically
- modify scripts, hooks, templates, tests, or agent files
- infer canonical status from path alone
- classify Copilot-only from location alone

### 5. SubAgent output contract is fixed

All subAgents in this topic must return evidence, not unsupported conclusions.

Every subAgent response must include these general fields:

- `subagent_name`
- `task_scope`
- `inputs_received`
- `files_read`
- `files_modified`
- `findings`
- `risks`
- `unresolved_items`
- `status`

Allowed `status` values:

- `NOT_STARTED`
- `IN_PROGRESS`
- `COMPLETE`
- `INCOMPLETE`
- `BLOCKED`

Role-specific required fields:

- Explorer:
  - `inventory_summary`
  - `compared_surfaces`
  - `evidence_by_skill`
  - `alias_candidates`
  - `uncertain_classifications`
  - `recommended_followup_targets`
- Implementer:
  - `report_files_touched`
  - `sections_completed`
  - `evidence_sources_used`
  - `assumption_free_gaps`
  - `scope_violations_detected`
- Reviewer:
  - `review_scope`
  - `files_reviewed`
  - `findings_critical`
  - `findings_major`
  - `findings_minor`
  - `missing_evidence`
  - `required_fixes`
  - `pass_blockers`
- Plan Reviewer:
  - `reviewed_artifacts`
  - `verdict`
  - `contract_gaps`
  - `artifact_gaps`
  - `decision_gaps`
  - `required_plan_changes`
- Plan Creator / Revision:
  - `updated_artifacts`
  - `review_items_addressed`
  - `review_items_not_addressed`
  - `reasons_not_addressed`
  - `remaining_blockers`
- Planner / Final Gate:
  - `files_checked`
  - `acceptance_criteria_result`
  - `consistency_result`
  - `residual_risks`
  - `blockers`
  - `final_verdict`
  - `human_handoff_notes`

If evidence is insufficient, the relevant item must be marked
`human_review_required`.

### 6. Analysis-layer priority is fixed

This topic uses strict-mode analysis inputs:

- `analysis/agent-skills-convergence-phase-1/requirements.md`
  - SHA-256: `c1af7545ac4c280d290acbe95a8880ebaf36329f4ae8ab3597b07ccdd5fe364f`
- `analysis/agent-skills-convergence-phase-1/technical-spec.md`
  - SHA-256: `15025ec3c91341336660ea59380a8615fac07e73776e5221679a41035e985f4e`

The plan and later implementation must map 100% to those analysis artifacts.

### 7. Stable-library and release intent are absent

- This topic is not a stable-library publish topic.
- `VERSION` stays unchanged.
- No tag, release, or release-note action exists in this topic.

## Boundaries / Exclusions

- Do not widen this topic into repository migration, contract transition,
  runtime/tooling repair, or projection creation just because prior migration
  evidence exists.
- Do not treat older runway-era migration artifacts as authority over current
  `AGENTS.md` and `docs/repo-positioning.md` truth.
- Do not invent third-surface parity for `.codex/skills/`; report only what is
  actually observed.
- If any required conclusion cannot be supported by evidence, mark it
  `human_review_required` rather than forcing a label.
- If required outputs would need changes outside `Artifact Paths`, stop and
  repair the plan before continuing.

## Status / Allowed Transitions

- **Current**: `review-ready`
- **Execution model**: planning + report implementation topic with independent
  review and final gate before human check
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

- Branch target: `feat/andrew/agent-skills-convergence-phase-1`
- Base branch: `dev`
- Worktree path:
  `/Users/andrew/code/python/agent-skills.worktrees/agent-20260603-agent-skills-convergence-phase-1`
- Human review is required after the planning final gate and again after Phase 1
  report implementation reaches its own final gate.

## Artifact Paths

| Artifact | Path | Owner | Role |
| --- | --- | --- | --- |
| Topic plan | `plan/agent-skills-convergence-phase-1/agent-skills-convergence-phase-1.plan.md` | Planning actor | Repo-visible execution contract for this topic |
| Topic progression artifact | `plan/agent-skills-convergence-phase-1/agent-skills-convergence-phase-1.step.md` | Planning actor / Main Agent | Current-truth workflow progression status for this topic |
| Review routing log | `plan/agent-skills-convergence-phase-1/agent-skills-convergence-phase-1.review-log.md` | Reviewer / Planning actor | Repo-visible routing log when reviewer findings control rework or re-review |
| Topic close summary artifact | `plan/agent-skills-convergence-phase-1/agent-skills-convergence-phase-1.summary.md` | Main Agent | Current-truth close outcome and human handoff semantics for planning close and later topic close when required |
| Requirements baseline | `analysis/agent-skills-convergence-phase-1/requirements.md` | Planning actor | Frozen business baseline for Phase 1 scope and stop rules |
| Technical baseline | `analysis/agent-skills-convergence-phase-1/technical-spec.md` | Planning actor | Frozen technical translation and implementation boundary |
| Phase 1 report root | `docs/agent-skills-convergence/phase-1/` | Implementer | Bounded write root for the 9 required Phase 1 files |
| Phase 1 summary | `docs/agent-skills-convergence/phase-1/00-summary.md` | Implementer | Executive summary and report statistics |
| Skill inventory | `docs/agent-skills-convergence/phase-1/01-skill-inventory.md` | Implementer | Unique skill table and surface inventory |
| Path comparison | `docs/agent-skills-convergence/phase-1/02-path-comparison.md` | Implementer | Presence and file-set comparison by skill |
| Copilot-only classification | `docs/agent-skills-convergence/phase-1/03-copilot-only-classification.md` | Implementer | Evidence-backed Copilot-only decisions |
| Semantic drift report | `docs/agent-skills-convergence/phase-1/04-semantic-drift-report.md` | Implementer | Non-identical drift summaries and candidate authority notes |
| Runtime dependency inventory | `docs/agent-skills-convergence/phase-1/05-runtime-dependency-inventory.md` | Implementer | Portable vs projection-required vs platform-native evidence |
| Convergence candidates | `docs/agent-skills-convergence/phase-1/06-convergence-candidates.md` | Implementer | Phase 2 preparation groups only |
| Phase 2 inputs | `docs/agent-skills-convergence/phase-1/07-phase-2-inputs.md` | Implementer | Canonical-convergence preparation without implementation |
| Phase 3 inputs | `docs/agent-skills-convergence/phase-1/08-phase-3-inputs.md` | Implementer | Projection/runtime-adaptation preparation without implementation |
| Governance source | `AGENTS.md` | Existing repo artifact | Current governance authority for canonical source and boundary language |
| Positioning contract | `docs/repo-positioning.md` | Existing repo artifact | Current authority model for compatibility/projection surfaces |
| Codex projection rule | `.codex/skills/README.md` | Existing repo artifact | Read-only evidence for `.codex/skills` surface role |
| Codex provenance | `.codex/skills/provenance.md` | Existing repo artifact | Read-only projection mapping and validation evidence |
| Supporting migration evidence | `docs/migration/platform-coupling-inventory.md` | Existing repo artifact | Historical runtime/tooling and dependency evidence only; not a write target |
| Supporting migration evidence | `docs/migration/planning-spine-divergence-review.md` | Existing repo artifact | Historical same-name drift evidence only; not a write target |
| Supporting migration evidence | `docs/migration/codex-readability-baseline.md` | Existing repo artifact | Historical `.codex/skills` readability evidence only; not a write target |
| Supporting migration evidence | `docs/migration/codex-migration-direct-move-report.md` | Existing repo artifact | Historical direct-move verification evidence only; not a write target |
| Supporting migration evidence | `docs/migration/migration-runway-checklist.md` | Existing repo artifact | Historical runway and blocker evidence only; not a write target |

Artifact path notes:

- The only writable implementation surface after planning is
  `docs/agent-skills-convergence/phase-1/`.
- `skills/**`, `.github/skills/**`, and `.codex/skills/**` are explicitly
  read-only.
- The close summary artifact becomes required before topic close whenever the
  topic reaches a human handoff or required follow-up state.
- Listed migration evidence artifacts may be read as supporting evidence but
  must not be modified by this topic.

## Implementation Steps

1. Confirm worktree, branch, and baseline repository state for this topic.
2. Freeze and keep analysis artifacts aligned to the user-specified Phase 1
   requirements and workflow constraints.
3. Use Explorer subAgent work to confirm whether an exact prior topic already
   exists; if not, preserve prior adjacent topics as supporting evidence rather
   than substitutes.
4. Author the topic plan and step artifact with exact write scope, stop rules,
   and subAgent contracts.
5. Commit the draft planning artifacts for this topic before review routing.
6. After human approval, materialize the 9 Phase 1 files under
   `docs/agent-skills-convergence/phase-1/` only.
7. Gather evidence for skill inventory, drift, Copilot-only classification,
   runtime dependency classification, and later-phase inputs.
8. Revise report content only when reviewer findings are supported by evidence
   and remain inside the locked write scope.

## Validation / Acceptance Checks

- analysis artifacts exist and match this plan's locked topic
- wording is consistent about `9 Phase 1 files` or `1 summary + 8 analysis reports`
- all writes stay inside topic planning artifacts and later
  `docs/agent-skills-convergence/phase-1/`
- no skill content, script, hook, template, test, or agent file is modified
- every detected unique skill appears in `01-skill-inventory.md`
- every non-identical skill appears in `04-semantic-drift-report.md`
- every `projection_required` skill appears in both `05` and `08`
- no alias is auto-resolved
- no canonical or Copilot-only decision relies only on path location
- uncertain cases are marked `human_review_required`
- `.codex/skills/README.md` and `.codex/skills/provenance.md` are treated as
  evidence, not as writable or canonical skill content

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

- No repository release action is part of this topic.
- No VERSION bump or tag creation is allowed in this topic.
- If merged, the next step is human review of the Phase 1 evidence bundle before
  starting Phase 2.

## Open Questions / Unresolved Items

- Whether any still-unread or later-discovered historical migration artifact
  materially changes the Phase 1 evidence boundary must be recorded as
  `human_review_required`; it does not authorize silent scope widening.
- If some semantic or behavior-drift classifications remain unprovable from
  repo-visible evidence, they stay unresolved in reports rather than being
  forced to closure.
