# Requirements: phase-2-merge-into-skills-batch

## Status

- **Status**: frozen for technical translation
- **Topic**: `phase-2-merge-into-skills-batch`
- **Date**: 2026-06-10
- **Scope**: bounded canonical convergence slice under `skills/`, now merged and terminal

## Problem Statement

The approved umbrella baseline freezes `phase-2-merge-into-skills-batch` as a
later Phase 2 slice after the safe canonical batch. Phase 1 evidence already
shows that this candidate set is not low-risk same-name convergence. Instead,
these skills carry semantic drift, path/alias drift, reference-set drift, or
runtime / projection concerns that make blind collapse unsafe.

The required outcome for this topic is a repo-visible bounded canonical
convergence result that:

1. freezes the exact merge-batch candidate set,
2. preserves `skills/` as canonical and `.github/**` / `.codex/**` as read-only
   reference inputs,
3. allows bounded path convergence, semantic convergence, or both together only
   under canonical `skills/<skill-name>/...`,
4. records that only `agent-skill-template` and `agent-skill-creator` needed
   canonical edits,
5. records that the other eight frozen candidates required no canonical edit,
6. and confirms that remaining compatibility-surface differences do not block
   progress when canonical `skills/` content is already correct.

## Evidence Read

The baseline uses the following repo-visible evidence:

- `AGENTS.md`
- `docs/repo-positioning.md`
- `plan/agent-handoff-workflow.md`
- `plan/topic-plan-contract.md`
- `plan/phase-2-umbrella/phase-2-umbrella.plan.md`
- `plan/phase-2-umbrella/phase-2-umbrella.step.md`
- `docs/agent-skills-convergence/phase-1/06-convergence-candidates.md`
- `docs/agent-skills-convergence/phase-1/07-phase-2-inputs.md`
- `docs/agent-skills-convergence/phase-1/04-semantic-drift-report.md`
- `docs/agent-skills-convergence/phase-1/05-runtime-dependency-inventory.md`
- `.github/prompts/create-analysis.prompt.md`
- `.github/prompts/create-agent-plan.prompt.md`

## Actors

| Actor | Role | What must be true after this topic |
| --- | --- | --- |
| Repository maintainer | Owns merge-batch execution truth | Can point to one bounded canonical convergence topic without implying projection or runtime execution |
| Planning actor | Authored the merge-batch topic plan and truth artifacts | Can show the frozen candidates, bounded execution policy, and non-goals without collapsing semantics by assumption |
| Reviewer | Reviews the execution truth | Can verify that only canonical `skills/` changed, that drift was handled explicitly, and that compatibility-surface deltas do not block progress |
| Creator | Executed bounded canonical convergence only where canonical `skills/` required change | Can show exactly which candidates changed and which required no canonical edit |
| Human operator | Confirms merged close-out truth after completed human-check | Can see the bounded execution result, that human-check completed before merge, and that no broader policy or surface expansion was introduced |

## Frozen Requirements

| ID | Requirement | Acceptance signal |
| --- | --- | --- |
| R1 | This topic must preserve repo-visible execution truth for the merge-required batch. | The topic-local analysis, plan, and step artifacts describe the completed bounded canonical convergence result coherently. |
| R2 | Execution must stay bounded to canonical `skills/` only. | The topic truth states that only canonical `skills/<skill-name>/...` may be edited and that `.github/**` / `.codex/**` remain read-only. |
| R3 | The exact merge-batch candidate set must be frozen. | The topic plan lists exactly: `agent-skill-creator`, `agent-skill-template`, `python-blueprint-authoring`, `python-library-architecture`, `python-package-layout`, `python-plan-authoring`, `python-pre-commit`, `python-pyproject-toolconfig`, `python-tdd-test-authoring`, `python-blueprint-review`. |
| R4 | `skills/` must remain canonical and `.github/**` / `.codex/**` must remain read-only compatibility surfaces. | The topic truth records the canonical / compatibility model explicitly. |
| R5 | `.codex/skills/` must remain a partial projection surface only. | The topic truth records that `.codex/skills/` is not canonical and that projection work is not part of this topic. |
| R6 | Canonical convergence may be path, semantic, or both together, but only where canonical `skills/` content actually needs change. | The topic truth explicitly allows bounded convergence modes while forbidding silent drift collapse. |
| R7 | Later slices and non-merge work remain out of scope. | The topic plan excludes safe canonical batch, planning-spine exceptions, projection materialization, runtime adaptation, and copilot-only work. |
| R8 | The only candidates requiring canonical edits must be recorded exactly. | The topic truth records only `agent-skill-template` and `agent-skill-creator` as requiring canonical edits, with their commits. |
| R9 | Checked candidates requiring no canonical edit must be recorded exactly. | The topic truth records exactly eight `no canonical edit needed` determinations. |
| R10 | Compatibility-surface differences must not block progress once canonical `skills/` truth is correct. | The topic truth states that remaining `.github/**` / `.codex/**` differences do not block this topic. |

## Resolved Contradictions

### C1 - This batch is merge-required, but bounded canonical convergence still completed without broad surface expansion

- Conflict: Phase 1 classified these candidates as `Need merge into skills/`,
  but this topic may not widen into `.github/**`, `.codex/**`, projection, or
  runtime work.
- Resolution: converge only canonical `skills/` content where needed, keep all
  compatibility surfaces read-only, and record remaining compatibility-surface
  differences as non-blocking.

### C2 - Phase 1 gives reasons for merge-required status, but not every candidate required a canonical edit

- Conflict: the evidence shows multiple kinds of drift, including path drift,
  reference-set expansion, templates/scripts/tests addition, and missing
  canonical counterpart.
- Resolution: record the two candidates that actually needed canonical edits
  and the eight candidates that were checked and required no canonical edit.

### C3 - Some candidates carry runtime/projection concerns, but this topic must not widen into projection or runtime work

- Conflict: runtime dependency inventory shows `projection_required` or helper
  drift for some candidates, but current topic must remain bounded to canonical
  `skills/` convergence rather than designing projection/runtime changes.
- Resolution: preserve those concerns as read-only evidence while keeping
  projection materialization and runtime adaptation out of scope.

## Explicit Assumptions

- A1: the umbrella coordination baseline is approved and may serve as the
  parent planning baseline for this topic.
- A2: the exact candidate set above is frozen from Phase 1 and should not be
  widened in this topic.
- A3: semantic drift / merge policy discussion is expected because Phase 1
  evidence shows behavior-changing differences for at least part of this batch.
- A4: remaining compatibility-surface differences do not by themselves require
  canonical edits once the canonical `skills/` content is correct.

## Non-goals

- Do not modify `.github/skills/**`.
- Do not modify `.codex/skills/**`.
- Do not modify `.github/agents/**`.
- Do not modify `.codex/agents/**`.
- Do not modify shared contract files.
- Do not modify umbrella topic artifacts.
- Do not modify any canonical skill outside:
  - `skills/agent-skill-template/**`
  - `skills/agent-skill-creator/**`
- Do not perform projection materialization.
- Do not perform runtime adaptation.
- Do not handle planning-spine exceptions.
- Do not handle copilot-only work.

## Extreme-Boundary Checks

| Boundary | Requirement result |
| --- | --- |
| A planner sees `merge_required` candidates and wants to widen beyond canonical `skills/` | The topic truth must still keep `.github/**` and `.codex/**` read-only and bounded to canonical `skills/` only |
| A creator wants to treat `.github/skills/` as authority because it has newer content | The topic truth must still state that `.github/**` is a read-only compatibility surface, not the canonical source |
| A maintainer wants to collapse alias/path drift silently into `skills/` | The topic plan must still require explicit semantic drift discussion rather than silent collapse |
| A maintainer sees residual `.github/**` or `.codex/**` differences after canonical edits | The topic truth must still allow progress when canonical `skills/` content is already correct |

## Success Signals

This topic is frozen successfully when:

1. the merge-batch execution truth is repo-visible,
2. the exact ten-candidate set is frozen,
3. bounded convergence is limited to canonical `skills/` only,
4. only `agent-skill-template` and `agent-skill-creator` are recorded as
   requiring canonical edits,
5. the remaining eight candidates are recorded as `no canonical edit needed`,
6. compatibility-surface differences are acknowledged as non-blocking when
   canonical `skills/` is already correct,
7. projection/runtime/copilot-only work remains excluded.
