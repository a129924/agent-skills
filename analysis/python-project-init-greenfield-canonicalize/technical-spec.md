# Technical Specification: python-project-init-greenfield-canonicalize

**Status**: READY FOR EXECUTION PLANNING
**Topic**: `python-project-init-greenfield-canonicalize`
**Date**: 2026-06-01
**Baseline Reference**: `analysis/python-project-init-greenfield-canonicalize/requirements.md`

---

## Source Baseline Summary

The frozen baseline requires one bounded child topic that promotes
`python-project-init-greenfield` into `skills/` as a canonical copy while
preserving the existing transition-era `.github/...` output and acceptance
contract during transition.

This is intentionally not a runtime-path migration, `.github` output redesign,
or greenfield-init behavior repair topic.

## Requirement Traceability

| Requirement | Technical realization | Dependencies | Cost / burden | Status |
| --- | --- | --- | --- | --- |
| R1 Single-candidate scope | Lock edits to `python-project-init-greenfield` only | umbrella Wave 1.5 sequence | Low | feasible |
| R2 Create canonical copy | Create `skills/python-project-init-greenfield/` with the full file set | current `.github/skills/python-project-init-greenfield/` contents | Low | feasible |
| R3 Preserve transition-era contracts | Leave `.github/skills/`, `.github/skills-provenance.json`, `.github/copilot-instructions.md`, and canonical acceptance CLI assumptions in place | existing blocker evidence in source skill | Low | feasible |
| R4 Copy full surface | Copy docs and both references together | current file inventory | Low | feasible |
| R5 Preserve compatibility layer | Keep `.github/skills/python-project-init-greenfield/` unchanged as the transition surface | repo positioning freeze | Low | feasible |
| R6 Defer blocker repair | Record deferred `.github` output, provenance, Copilot-placeholder, and acceptance-path transition lanes | current source skill contract | Low | feasible |
| R7 Protect shared governance | Forbid edits outside candidate-local surfaces and topic-local evidence | repo governance boundaries | Low | feasible |
| R8 Leave explicit migration evidence | Emit a topic-local report describing the copy and deferrals | implementation topic boundary | Low | feasible |

## Allowed Artifacts for the Execution Topic

This technical spec authorizes edits only to:

- `analysis/python-project-init-greenfield-canonicalize/requirements.md`
- `analysis/python-project-init-greenfield-canonicalize/technical-spec.md`
- `plan/python-project-init-greenfield-canonicalize/python-project-init-greenfield-canonicalize.plan.md`
- `skills/python-project-init-greenfield/`
- `docs/migration/python-project-init-greenfield-canonicalize.md`

This technical spec does **not** authorize edits to:

- `.github/skills/python-project-init-greenfield/`
- `sense-env-scaffold`
- `python-project-retrofit`
- `copilot-instructions-init`
- `AGENTS.md`
- `docs/repo-positioning.md`
- `README.md`
- `VERSION`
- `.codex/skills/`

## Copy Boundary

Source root:

- `.github/skills/python-project-init-greenfield/`

Target root:

- `skills/python-project-init-greenfield/`

Required copied paths:

- `SKILL.md`
- `examples.md`
- `references/baseline-generation-rules.md`
- `references/blueprint-parsing-contract.md`

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
2. create `skills/python-project-init-greenfield/`
3. copy the full required file set into the target tree
4. verify the target tree preserves structure and file presence
5. confirm `.github/skills/python-project-init-greenfield/` remains unchanged
6. emit explicit evidence of deferred runtime/tooling blockers and preserved
   confirmed-blocker context

## Verification Contract

The execution topic should verify at minimum:

- `skills/python-project-init-greenfield/SKILL.md` exists
- `skills/python-project-init-greenfield/examples.md` exists
- `skills/python-project-init-greenfield/references/` contains both required files
- `.github/skills/python-project-init-greenfield/` still exists after the copy
- no source artifact under `.github/skills/python-project-init-greenfield/` was modified
- no artifact in this topic claims active-path cutover or downstream output
  cutover away from `.github/...`

## Deferred Blocker Inventory

This topic intentionally defers these runtime/tooling and downstream output lanes:

- changing required-skill installation away from `.github/skills/`
- moving governance provenance away from `.github/skills-provenance.json`
- changing `.github/copilot-instructions.md` output policy or destination
- updating the acceptance handoff path away from
  `.github/skills/sense-env-scaffold/scripts/sense_env.py`
- changing active-path assumptions in downstream greenfield bootstrap consumers
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
| transition-era contract preservation | fits existing blocker evidence | keeps `.github/...` deployment and acceptance assumptions in place |
| bounded child-topic scope | fits umbrella sequencing | only one Wave 1.5 candidate |
| shared governance protection | fits existing governance | no repo-wide contract or release changes |

## Rollback-to-Alignment Triggers

Return to alignment before execution if any of the following becomes true:

1. creating the canonical copy requires modifying
   `.github/skills/python-project-init-greenfield/` behavior
2. the source tree gains additional required files that change the bounded copy
   surface materially
3. a stakeholder wants this topic to rewrite `.github/skills/` output,
   provenance, Copilot placeholder, or acceptance-path behavior
4. the topic cannot complete honestly without touching shared governance or
   release surfaces

## Ready-for-next-step Decision

This technical specification is complete enough to drive the next planning or
execution step for this candidate:

- execute the bounded copy into `skills/python-project-init-greenfield/`
- keep runtime/tooling transition and downstream output rewrites as separate future work
