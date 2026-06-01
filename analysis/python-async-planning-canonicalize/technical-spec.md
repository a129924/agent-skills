# Technical Specification: python-async-planning-canonicalize

**Status**: READY FOR EXECUTION PLANNING
**Topic**: `python-async-planning-canonicalize`
**Date**: 2026-06-01
**Baseline Reference**: `analysis/python-async-planning-canonicalize/requirements.md`

---

## Source Baseline Summary

The frozen baseline requires one bounded child topic that promotes
`python-async-planning` into `skills/` as a canonical copy while preserving the
existing `.github/skills/...` contract during transition.

This is intentionally not a runtime-path migration or async-rule redesign topic.

## Requirement Traceability

| Requirement | Technical realization | Dependencies | Cost / burden | Status |
| --- | --- | --- | --- | --- |
| R1 Single-candidate scope | Lock edits to `python-async-planning` only | umbrella sequencing | Low | feasible |
| R2 Create canonical copy | Create `skills/python-async-planning/` with the full file set | current source inventory | Low | feasible |
| R3 Preserve async contract | Leave trigger/exemption, subsection names, contradiction log, and retrofit rules in place | existing source contract | Low | feasible |
| R4 Copy full surface | Copy `SKILL.md`, `reference.md`, and `examples.md` together | current file inventory | Low | feasible |
| R5 Preserve compatibility layer | Keep `.github/skills/python-async-planning/` unchanged as the transition surface | repo positioning freeze | Low | feasible |
| R6 Defer broader repairs | Record deferred path-governance or workflow-integration lanes | repo governance boundaries | Low | feasible |
| R7 Protect shared governance | Forbid edits outside candidate-local surfaces and topic-local evidence | repo governance boundaries | Low | feasible |
| R8 Leave explicit migration evidence | Emit a topic-local report describing the copy and deferrals | implementation topic boundary | Low | feasible |

## Allowed Artifacts for the Future Execution Topic

This technical spec authorizes a later execution topic to edit only:

- `skills/python-async-planning/`
- optionally one topic-local migration report under `docs/migration/`

This technical spec does **not** authorize edits to:

- `.github/skills/python-async-planning/`
- `AGENTS.md`
- `docs/repo-positioning.md`
- `README.md`
- `VERSION`
- `.codex/skills/`

## Copy Boundary

Source root:

- `.github/skills/python-async-planning/`

Target root:

- `skills/python-async-planning/`

Required copied paths:

- `SKILL.md`
- `reference.md`
- `examples.md`

Copy rule:

- preserve relative structure exactly
- do not summarize or re-author files during the copy topic

## Execution Model

### Worktree rule

- use a dedicated external worktree for the future execution topic
- keep repo-root `dev` clean
- do not colocate unrelated canonicalization candidates in the same execution topic

### Candidate-local execution steps

1. verify the source tree still matches the file inventory frozen in this spec
2. create `skills/python-async-planning/`
3. copy the full required file set into the target tree
4. verify the target tree preserves structure and file presence
5. confirm `.github/skills/python-async-planning/` remains unchanged
6. emit explicit evidence of deferred broader workflow repair and preserved contract context

## Verification Contract for the Future Execution Topic

The execution topic should verify at minimum:

- `skills/python-async-planning/SKILL.md` exists
- `skills/python-async-planning/reference.md` exists
- `skills/python-async-planning/examples.md` exists
- `.github/skills/python-async-planning/` still exists after the copy
- no async trigger / exemption semantics were changed in this topic

## Deferred Blocker Inventory

This topic intentionally defers these broader transition lanes:

- changing active-path assumptions for this skill
- updating projection or release surfaces
- any repo-wide governance or workflow integration changes

## Recommended Topic-local Evidence

If the future execution topic emits a migration report, it should state:

- candidate name
- source root
- target root
- copied file set
- compatibility layer preserved: yes
- active runtime path changed: no
- preserved contract context: yes
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
| runtime contract preservation | fits existing blocker evidence | keeps `.github/skills/...` as the active transition surface |
| bounded child-topic scope | fits umbrella sequencing | only one canonicalization candidate |
| shared governance protection | fits existing governance | no repo-wide contract or release changes |

## Rollback-to-Alignment Triggers

Return to alignment before execution if any of the following becomes true:

1. creating the canonical copy requires modifying `.github/skills/python-async-planning/`
2. the source tree gains additional required files that change the bounded copy surface materially
3. a stakeholder wants this topic to rewrite active-path or workflow-integration behavior
4. the topic cannot complete honestly without touching shared governance or release surfaces

## Ready-for-next-step Decision

This technical specification is complete enough to drive the next planning or
execution step for this candidate:

- author an execution topic plan for the bounded copy
- keep broader workflow and governance changes as separate future work
