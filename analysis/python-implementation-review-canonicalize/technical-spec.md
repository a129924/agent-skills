# Technical Specification: python-implementation-review-canonicalize

**Status**: READY FOR EXECUTION PLANNING
**Topic**: `python-implementation-review-canonicalize`
**Date**: 2026-06-01
**Baseline Reference**: `analysis/python-implementation-review-canonicalize/requirements.md`

---

## Source Baseline Summary

The frozen baseline requires one bounded child topic that promotes
`python-implementation-review` into `skills/` as a canonical copy while
preserving the existing transition-era approval-gate, step-gate, BLOCKED
refusal, and sequencing contract during transition.

This is intentionally not an approval-policy migration, step-gate redesign, or
review-sequencing repair topic.

## Requirement Traceability

| Requirement | Technical realization | Dependencies | Cost / burden | Status |
| --- | --- | --- | --- | --- |
| R1 Single-candidate scope | Lock edits to `python-implementation-review` only | umbrella Wave 2 sequence | Low | feasible |
| R2 Create canonical copy | Create `skills/python-implementation-review/` with the full file set | current `.github/skills/python-implementation-review/` contents | Low | feasible |
| R3 Preserve transition-era gate semantics | Leave approval proof, optional `*.step.md` gating, BLOCKED refusal, and sequencing rules in place | existing blocker evidence in source skill | Low | feasible |
| R4 Copy full surface | Copy examples, overview reference, and all four split references together | current file inventory | Low | feasible |
| R5 Preserve compatibility layer | Keep `.github/skills/python-implementation-review/` unchanged as the transition surface | repo positioning freeze | Low | feasible |
| R6 Defer blocker repair | Record deferred approval-gate, step-gate, refusal, sequencing, and projection lanes | current source skill contract | Low | feasible |
| R7 Protect shared governance | Forbid edits outside candidate-local surfaces and topic-local evidence | repo governance boundaries | Low | feasible |
| R8 Leave explicit migration evidence | Emit a topic-local report describing the copy and deferrals | implementation topic boundary | Low | feasible |

## Allowed Artifacts for the Execution Topic

This technical spec authorizes edits only to:

- `analysis/python-implementation-review-canonicalize/requirements.md`
- `analysis/python-implementation-review-canonicalize/technical-spec.md`
- `plan/python-implementation-review-canonicalize/python-implementation-review-canonicalize.plan.md`
- `skills/python-implementation-review/`
- `docs/migration/python-implementation-review-canonicalize.md`

This technical spec does **not** authorize edits to:

- `.github/skills/python-implementation-review/`
- `copilot-instructions-init`
- `python-code-review`
- `python-async-planning`
- `AGENTS.md`
- `docs/repo-positioning.md`
- `README.md`
- `VERSION`
- `.codex/skills/`

## Copy Boundary

Source root:

- `.github/skills/python-implementation-review/`

Target root:

- `skills/python-implementation-review/`

Required copied paths:

- `SKILL.md`
- `examples.md`
- `reference.md`
- `references/contract-deviation-rules.md`
- `references/plan-section-structure.md`
- `references/semantic-boundaries.md`
- `references/traceability-status.md`

Copy rule:

- preserve relative structure exactly
- do not summarize or re-author files during the copy topic unless a verified
  portability fix is required and separately authorized

## Execution Model

### Worktree rule

- use the dedicated external worktree already assigned to this topic
- keep repo-root `dev` clean
- do not colocate unrelated Wave 2 or Wave 3 candidate edits in this topic

### Candidate-local execution steps

1. verify the source tree still matches the file inventory frozen in this spec
2. create `skills/python-implementation-review/`
3. copy the full required file set into the target tree
4. verify the target tree preserves structure and file presence
5. confirm `.github/skills/python-implementation-review/` remains unchanged
6. emit explicit evidence of deferred runtime/tooling, approval-gate, and
   step-gate blockers

## Verification Contract

The execution topic should verify at minimum:

- `skills/python-implementation-review/SKILL.md` exists
- `skills/python-implementation-review/examples.md` exists
- `skills/python-implementation-review/reference.md` exists
- `skills/python-implementation-review/references/` contains all four required files
- `.github/skills/python-implementation-review/` still exists after the copy
- no source artifact under `.github/skills/python-implementation-review/` was modified
- no artifact in this topic claims active-path cutover, approval-gate cutover,
  or sequencing cutover away from `.github/...`

## Deferred Blocker Inventory

This topic intentionally defers these runtime/tooling and gate-coupling lanes:

- changing approval proof requirements away from the current
  `python-plan-review` contract
- changing `plan/<topic>/<topic>.step.md` gating semantics or pending-step
  detection rules
- changing BLOCKED refusal output semantics
- changing the sequencing dependency between
  `python-implementation-review` and `python-code-review`
- changing downstream active-path assumptions for review execution
- changing projection, stable-library metadata, or release surfaces

## Recommended Topic-local Evidence

The migration report should state:

- candidate name
- source root
- target root
- copied file set
- compatibility layer preserved: yes
- active path changed: no
- confirmed-blocker context preserved: yes
- deferred blocker lanes

## Cost-of-Realization Assessment

| Workstream | Complexity | Main burden | Ongoing operational cost |
| --- | --- | --- | --- |
| candidate inventory verification | Low | confirming the source tree still matches the frozen file set | low |
| canonical tree creation | Low | copying the bounded skill surface without drift | low |
| compatibility preservation | Low | avoiding accidental edits to `.github/skills/` | low |
| deferred-blocker evidence | Low | documenting exactly what was not solved yet | low |

## Architecture / Governance Compliance Check

| Dimension | Result | Notes |
| --- | --- | --- |
| target-architecture alignment | fits existing governance | creates `skills/` copy without claiming active-path cutover |
| transition-era gate preservation | fits existing blocker evidence | keeps approval, optional step gate, BLOCKED refusal, and sequencing assumptions in place |
| bounded child-topic scope | fits umbrella sequencing | only one Wave 2 candidate |
| shared governance protection | fits existing governance | no repo-wide contract or release changes |

## Rollback-to-Alignment Triggers

Return to alignment before execution if any of the following becomes true:

1. creating the canonical copy requires modifying
   `.github/skills/python-implementation-review/` behavior
2. the source tree gains additional required files that change the bounded copy
   surface materially
3. a stakeholder wants this topic to rewrite approval proof, step-gate,
   refusal, or sequencing behavior
4. the topic cannot complete honestly without touching shared governance or
   release surfaces

## Ready-for-next-step Decision

This technical specification is complete enough to drive the next planning or
execution step for this candidate:

- execute the bounded copy into `skills/python-implementation-review/`
- keep approval-gate, step-gate, refusal-output, and sequencing rewrites as
  separate future work
