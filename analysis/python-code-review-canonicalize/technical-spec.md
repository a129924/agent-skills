# Technical Specification: python-code-review-canonicalize

**Status**: READY FOR EXECUTION PLANNING
**Topic**: `python-code-review-canonicalize`
**Date**: 2026-06-01
**Baseline Reference**: `analysis/python-code-review-canonicalize/requirements.md`

---

## Source Baseline Summary

The frozen baseline requires one bounded child topic that promotes
`python-code-review` into `skills/` as a canonical copy while preserving the
existing transition-era sequencing gate, tooling detection, severity
calibration, verdict mapping, and routing contract during transition.

This is intentionally not a sequencing-gate migration, tooling-detection
redesign, verdict-policy redesign, or release-surface repair topic.

## Requirement Traceability

| Requirement | Technical realization | Dependencies | Cost / burden | Status |
| --- | --- | --- | --- | --- |
| R1 Single-candidate scope | Lock edits to `python-code-review` only | umbrella Wave 2 sequence | Low | feasible |
| R2 Create canonical copy | Create `skills/python-code-review/` with the full file set | current `.github/skills/python-code-review/` contents | Low | feasible |
| R3 Preserve transition-era sequencing/tooling/verdict semantics | Leave sequencing gate, tooling detection order, severity calibration, and verdict rules in place | existing blocker evidence in source skill | Low | feasible |
| R4 Copy full surface | Copy examples, overview reference, and all five split references together | current file inventory | Low | feasible |
| R5 Preserve compatibility layer | Keep `.github/skills/python-code-review/` unchanged as the transition surface | repo positioning freeze | Low | feasible |
| R6 Defer blocker repair | Record deferred sequencing-gate, tooling-detection, verdict, routing, and projection lanes | current source skill contract | Low | feasible |
| R7 Protect shared governance | Forbid edits outside candidate-local surfaces and topic-local evidence | repo governance boundaries | Low | feasible |
| R8 Leave explicit migration evidence | Emit a topic-local report describing the copy and deferrals | implementation topic boundary | Low | feasible |

## Allowed Artifacts for the Execution Topic

This technical spec authorizes edits only to:

- `analysis/python-code-review-canonicalize/requirements.md`
- `analysis/python-code-review-canonicalize/technical-spec.md`
- `plan/python-code-review-canonicalize/python-code-review-canonicalize.plan.md`
- `skills/python-code-review/`
- `docs/migration/python-code-review-canonicalize.md`

This technical spec does **not** authorize edits to:

- `.github/skills/python-code-review/`
- `python-implementation-review`
- `python-async-planning`
- `AGENTS.md`
- `docs/repo-positioning.md`
- `README.md`
- `VERSION`
- `.codex/skills/`

## Copy Boundary

Source root:

- `.github/skills/python-code-review/`

Target root:

- `skills/python-code-review/`

Required copied paths:

- `SKILL.md`
- `examples.md`
- `reference.md`
- `references/anti-patterns.md`
- `references/cross-skill-signposts.md`
- `references/observability.md`
- `references/test-quality.md`
- `references/tooling-detection.md`

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
2. create `skills/python-code-review/`
3. copy the full required file set into the target tree
4. verify the target tree preserves structure and file presence
5. confirm `.github/skills/python-code-review/` remains unchanged
6. emit explicit evidence of deferred runtime/tooling, sequencing-gate, and
   verdict-policy blockers

## Verification Contract

The execution topic should verify at minimum:

- `skills/python-code-review/SKILL.md` exists
- `skills/python-code-review/examples.md` exists
- `skills/python-code-review/reference.md` exists
- `skills/python-code-review/references/` contains all five required files
- `.github/skills/python-code-review/` still exists after the copy
- no source artifact under `.github/skills/python-code-review/` was modified
- no artifact in this topic claims active-path cutover, sequencing-gate cutover,
  or tooling / verdict cutover away from `.github/...`

## Deferred Blocker Inventory

This topic intentionally defers these runtime/tooling and
sequencing/tooling-coupling lanes:

- changing the sequencing gate away from
  `python-implementation-review` approval
- changing tooling detection priority order or strict-mode escalation behavior
- changing verdict mapping from `blocking` findings to `needs-rework`
- changing cross-skill routing or quality-dimension ownership rules
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
| transition-era sequencing/tooling preservation | fits existing blocker evidence | keeps sequencing gate, tooling order, severity calibration, and verdict assumptions in place |
| bounded child-topic scope | fits umbrella sequencing | only one Wave 2 candidate |
| shared governance protection | fits existing governance | no repo-wide contract or release changes |

## Rollback-to-Alignment Triggers

Return to alignment before execution if any of the following becomes true:

1. creating the canonical copy requires modifying
   `.github/skills/python-code-review/` behavior
2. the source tree gains additional required files that change the bounded copy
   surface materially
3. a stakeholder wants this topic to rewrite sequencing-gate,
   tooling-detection, severity, or verdict behavior
4. the topic cannot complete honestly without touching shared governance or
   release surfaces

## Ready-for-next-step Decision

This technical specification is complete enough to drive the next planning or
execution step for this candidate:

- execute the bounded copy into `skills/python-code-review/`
- keep sequencing-gate, tooling-detection, verdict-policy, and routing rewrites
  as separate future work
