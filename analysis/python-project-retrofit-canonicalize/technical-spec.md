# Technical Specification: python-project-retrofit-canonicalize

**Status**: READY FOR EXECUTION PLANNING
**Topic**: `python-project-retrofit-canonicalize`
**Date**: 2026-06-01
**Baseline Reference**: `analysis/python-project-retrofit-canonicalize/requirements.md`

---

## Source Baseline Summary

The frozen baseline requires one bounded child topic that promotes
`python-project-retrofit` into `skills/` as a canonical copy while preserving
the existing `.github/skills/...` execution contract during transition.

This is intentionally not a runtime-path migration or executor-behavior repair
topic.

## Requirement Traceability

| Requirement | Technical realization | Dependencies | Cost / burden | Status |
| --- | --- | --- | --- | --- |
| R1 Single-candidate scope | Lock edits to `python-project-retrofit` only | umbrella Wave 1 sequence | Low | feasible |
| R2 Create canonical copy | Create `skills/python-project-retrofit/` with the full file set | current `.github/skills/python-project-retrofit/` contents | Low | feasible |
| R3 Preserve runtime execution contract | Leave `.github/skills/...` acceptance handoff and executor behavior in place | existing runtime/tooling blocker evidence | Low | feasible |
| R4 Copy full surface | Copy docs and all executor references together | current file inventory | Low | feasible |
| R5 Preserve compatibility layer | Keep `.github/skills/python-project-retrofit/` unchanged as the transition surface | repo positioning freeze | Low | feasible |
| R6 Defer blocker repair | Record deferred acceptance-path, provenance, and delta-contract transition lanes | `docs/migration/platform-coupling-inventory.md`, `docs/migration/migration-runway-checklist.md` | Low | feasible |
| R7 Protect shared governance | Forbid edits outside candidate-local surfaces and topic-local evidence | repo governance boundaries | Low | feasible |
| R8 Leave explicit migration evidence | Emit a topic-local report describing the copy and deferrals | implementation topic boundary | Low | feasible |

## Allowed Artifacts for the Future Execution Topic

This technical spec authorizes a later execution topic to edit only:

- `skills/python-project-retrofit/`
- optionally one topic-local migration report under `docs/migration/`

This technical spec does **not** authorize edits to:

- `.github/skills/python-project-retrofit/`
- `sense-env-scaffold`
- `python-project-init-greenfield`
- `AGENTS.md`
- `docs/repo-positioning.md`
- `README.md`
- `VERSION`
- `.codex/skills/`

## Copy Boundary

Source root:

- `.github/skills/python-project-retrofit/`

Target root:

- `skills/python-project-retrofit/`

Required copied paths:

- `SKILL.md`
- `examples.md`
- `references/retrofit-conflict-resolution.md`
- `references/retrofit-plan-v2-contract.md`
- `references/retrofit-safety-guidelines.md`
- `references/sensing-delta-contract.md`

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
2. create `skills/python-project-retrofit/`
3. copy the full required file set into the target tree
4. verify the target tree preserves structure and file presence
5. confirm `.github/skills/python-project-retrofit/` remains unchanged
6. emit explicit evidence of deferred runtime/tooling blockers and preserved confirmed-blocker context

## Verification Contract for the Future Execution Topic

The execution topic should verify at minimum:

- `skills/python-project-retrofit/SKILL.md` exists
- `skills/python-project-retrofit/examples.md` exists
- `skills/python-project-retrofit/references/` contains all four reference files
- `.github/skills/python-project-retrofit/` still exists after the copy
- no acceptance handoff path was changed from
  `.github/skills/sense-env-scaffold/scripts/sense_env.py`
- no downstream runtime or provenance artifact was changed in this topic

## Deferred Blocker Inventory

This topic intentionally defers these runtime/tooling blocker lanes:

- updating the acceptance handoff path away from
  `.github/skills/sense-env-scaffold/scripts/sense_env.py`
- introducing a compatibility alias, wrapper, or alternate active executor path
- changing delta-report schema or provenance semantics
- changing active-path assumptions in `python-project-init-greenfield`
- changing stable-library metadata, projection, or release surfaces

## Recommended Topic-local Evidence

If the future execution topic emits a migration report, it should state:

- candidate name
- source root
- target root
- copied file set
- compatibility layer preserved: yes
- active runtime path changed: no
- confirmed-blocker context preserved: yes
- deferred blocker lanes

## Cost-of-Realization Assessment

| Workstream | Complexity | Main burden | Ongoing operational cost |
| --- | --- | --- | --- |
| candidate inventory verification | Low | confirming the source tree still matches the frozen file set | low |
| canonical tree creation | Low | copying the bounded executor surface without drift | low |
| compatibility preservation | Low | avoiding accidental edits to `.github/skills/` | low |
| deferred-blocker evidence | Low | documenting exactly what was not solved yet | low |

## Architecture / Governance Compliance Check

| Dimension | Result | Notes |
| --- | --- | --- |
| target-architecture alignment | fits existing governance | creates `skills/` copy without claiming active-path cutover |
| runtime contract preservation | fits existing blocker evidence | keeps `.github/skills/...` acceptance handoff as the active path |
| bounded child-topic scope | fits umbrella sequencing | only one Wave 1 candidate |
| shared governance protection | fits existing governance | no repo-wide contract or release changes |

## Rollback-to-Alignment Triggers

Return to alignment before execution if any of the following becomes true:

1. creating the canonical copy requires modifying
   `.github/skills/python-project-retrofit/` behavior
2. the source tree gains additional required files that change the bounded copy
   surface materially
3. a stakeholder wants this topic to rewrite acceptance handoff, provenance,
   or downstream runtime/tooling callers
4. the topic cannot complete honestly without touching shared governance or
   release surfaces

## Ready-for-next-step Decision

This technical specification is complete enough to drive the next planning or
execution step for this candidate:

- author an execution topic plan for the bounded copy
- keep runtime/tooling transition and downstream caller rewrites as separate future work
