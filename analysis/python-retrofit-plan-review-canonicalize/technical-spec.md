# Technical Specification: python-retrofit-plan-review-canonicalize

**Status**: READY FOR EXECUTION PLANNING
**Topic**: `python-retrofit-plan-review-canonicalize`
**Date**: 2026-06-01
**Baseline Reference**: `analysis/python-retrofit-plan-review-canonicalize/requirements.md`

---

## Source Baseline Summary

The frozen baseline requires one bounded child topic that promotes
`python-retrofit-plan-review` into `skills/` as a canonical copy while
preserving the existing `.github/skills/` transition surface and all current
Retrofit V2 review semantics.

This is intentionally not a review-contract repair or coupled executor-sync
topic.

## Requirement Traceability

| Requirement | Technical realization | Dependencies | Cost / burden | Status |
| --- | --- | --- | --- | --- |
| R1 Single-candidate scope | Lock edits to `python-retrofit-plan-review` only | umbrella Wave 1 sequence | Low | feasible |
| R2 Create canonical copy | Create `skills/python-retrofit-plan-review/` with the full file set | current `.github/skills/python-retrofit-plan-review/` contents | Low | feasible |
| R3 Preserve current semantics | Copy without rewriting review-verdict or Retrofit V2 review semantics | current planning-spine contract | Low | feasible |
| R4 Copy full surface | Copy contract, examples, checklist, and references together | current file inventory | Low | feasible |
| R5 Preserve compatibility layer | Keep `.github/skills/python-retrofit-plan-review/` unchanged as the transition surface | repo positioning freeze | Low | feasible |
| R6 Defer coupled-lane work | Record deferred authoring / executor / sensing synchronization lanes | existing downstream topic inventory | Low | feasible |
| R7 Protect shared governance | Forbid edits outside candidate-local surfaces and topic-local evidence | repo governance boundaries | Low | feasible |
| R8 Leave explicit migration evidence | Emit a topic-local report describing the copy and deferrals | implementation topic boundary | Low | feasible |

## Allowed Artifacts for the Future Execution Topic

This technical spec authorizes a later execution topic to edit only:

- `skills/python-retrofit-plan-review/`
- optionally one topic-local migration report under `docs/migration/`

This technical spec does **not** authorize edits to:

- `.github/skills/python-retrofit-plan-review/`
- `python-retrofit-plan-authoring`
- `python-project-retrofit`
- `sense-env-scaffold`
- `AGENTS.md`
- `docs/repo-positioning.md`
- `README.md`
- `VERSION`
- `.codex/skills/`

## Copy Boundary

Source root:

- `.github/skills/python-retrofit-plan-review/`

Target root:

- `skills/python-retrofit-plan-review/`

Required copied paths:

- `SKILL.md`
- `examples.md`
- `checklist.md`
- `references/lane-fit-and-reroute.md`
- `references/retrofit-v2-review-checks.md`
- `references/review-verdict-contract.md`
- `references/risk-boundary-and-locatability-checks.md`

Copy rule:

- preserve relative structure exactly
- do not summarize or re-author files during the copy topic unless a verified
  portability fix is required and separately authorized

## Execution Model

### Worktree rule

- use a dedicated external worktree for the future execution topic
- keep repo-root `dev` clean
- do not colocate unrelated Wave 1 candidate edits in the same execution topic

### Candidate-local execution steps

1. verify the source tree still matches the file inventory frozen in this spec
2. create `skills/python-retrofit-plan-review/`
3. copy the full required file set into the target tree
4. verify the target tree preserves structure and file presence
5. confirm `.github/skills/python-retrofit-plan-review/` remains unchanged
6. emit explicit evidence of deferred coupled planning-spine lanes

## Verification Contract for the Future Execution Topic

The execution topic should verify at minimum:

- `skills/python-retrofit-plan-review/SKILL.md` exists
- `skills/python-retrofit-plan-review/examples.md` exists
- `skills/python-retrofit-plan-review/checklist.md` exists
- `skills/python-retrofit-plan-review/references/` contains all four reference files
- `.github/skills/python-retrofit-plan-review/` still exists after the copy
- no downstream authoring or executor artifact was changed in this topic

## Deferred Coupled-lane Inventory

This topic intentionally defers these coupled lanes:

- `python-retrofit-plan-authoring` canonicalization synchronization beyond bounded copy
- `python-project-retrofit` canonicalization or contract synchronization beyond bounded copy
- any change to `sense-env-scaffold` assertion execution semantics
- any update to stable-library metadata or release surfaces

## Recommended Topic-local Evidence

If the future execution topic emits a migration report, it should state:

- candidate name
- source root
- target root
- copied file set
- compatibility layer preserved: yes
- active authored/reviewed path changed: no
- deferred coupled lanes

## Cost-of-Realization Assessment

| Workstream | Complexity | Main burden | Ongoing operational cost |
| --- | --- | --- | --- |
| candidate inventory verification | Low | confirming the source tree still matches the frozen file set | low |
| canonical tree creation | Low | copying the bounded documentation/reference surface without drift | low |
| compatibility preservation | Low | avoiding accidental edits to `.github/skills/` | low |
| deferred-coupling evidence | Low | documenting exactly what was not solved yet | low |

## Architecture / Governance Compliance Check

| Dimension | Result | Notes |
| --- | --- | --- |
| target-architecture alignment | fits existing governance | creates `skills/` copy without claiming active-path cutover |
| planning-spine preservation | fits existing governance | keeps Retrofit V2 review semantics unchanged |
| bounded child-topic scope | fits umbrella sequencing | only one Wave 1 candidate |
| shared governance protection | fits existing governance | no repo-wide contract or release changes |

## Rollback-to-Alignment Triggers

Return to alignment before execution if any of the following becomes true:

1. creating the canonical copy requires modifying
   `.github/skills/python-retrofit-plan-review/` semantics
2. the source tree gains additional required files that change the bounded copy
   surface materially
3. a stakeholder wants this topic to rewrite `python-retrofit-plan-authoring`,
   `python-project-retrofit`, or `sense-env-scaffold`
4. the topic cannot complete honestly without touching shared governance or
   release surfaces

## Ready-for-next-step Decision

This technical specification is complete enough to drive the next planning or
execution step for this candidate:

- author an execution topic plan for the bounded copy
- keep downstream coupled-lane synchronization as separate future work
