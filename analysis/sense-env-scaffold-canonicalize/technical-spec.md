# Technical Specification: sense-env-scaffold-canonicalize

**Status**: READY FOR EXECUTION PLANNING
**Topic**: `sense-env-scaffold-canonicalize`
**Date**: 2026-06-01
**Baseline Reference**: `analysis/sense-env-scaffold-canonicalize/requirements.md`

---

## Source Baseline Summary

The frozen baseline requires one bounded child topic that promotes
`sense-env-scaffold` into `skills/` as a canonical copy while preserving the
existing `.github/skills/.../sense_env.py` execution contract during transition.

This is intentionally not a runtime-path migration topic.

## Requirement Traceability

| Requirement | Technical realization | Dependencies | Cost / burden | Status |
| --- | --- | --- | --- | --- |
| R1 Single-candidate scope | Lock edits to `sense-env-scaffold` only | umbrella Wave 1 sequence | Low | feasible |
| R2 Create canonical copy | Create `skills/sense-env-scaffold/` with the full file set | current `.github/skills/sense-env-scaffold/` contents | Medium | feasible |
| R3 Preserve runtime command path | Leave `.github/skills/sense-env-scaffold/scripts/sense_env.py` in place and do not retarget callers | existing runtime/tooling blocker evidence | Low | feasible |
| R4 Copy full surface | Copy docs, references, CLI script, and local runtime package together | current file inventory | Medium | feasible |
| R5 Preserve compatibility layer | Keep `.github/skills/sense-env-scaffold/` unchanged as the transition surface | repo positioning freeze | Low | feasible |
| R6 Defer blocker repair | Record deferred downstream path callers and runtime-policy changes | `docs/migration/platform-coupling-inventory.md`, `docs/migration/migration-runway-checklist.md` | Low | feasible |
| R7 Protect shared governance | Forbid edits outside candidate-local surfaces and topic-local evidence | repo governance boundaries | Low | feasible |
| R8 Leave explicit migration evidence | Emit a topic-local report describing the copy and deferrals | implementation topic boundary | Low | feasible |

## Allowed Artifacts for the Future Execution Topic

This technical spec authorizes a later execution topic to edit only:

- `skills/sense-env-scaffold/`
- optionally one topic-local migration report under `docs/migration/` if the
  execution plan chooses to require it

This technical spec does **not** authorize edits to:

- `.github/skills/sense-env-scaffold/`
- downstream caller skills or plans
- `AGENTS.md`
- `docs/repo-positioning.md`
- `README.md`
- `VERSION`
- `.codex/skills/`

## Copy Boundary

The future execution topic must copy this full source tree into the canonical
target location:

Source root:

- `.github/skills/sense-env-scaffold/`

Target root:

- `skills/sense-env-scaffold/`

Required copied paths:

- `SKILL.md`
- `examples.md`
- `references/env-manifest-schema.md`
- `references/sense-env-cli-contract.md`
- `scripts/sense_env.py`
- `scripts/sense_env_runtime/__init__.py`
- `scripts/sense_env_runtime/contract.py`
- `scripts/sense_env_runtime/models.py`
- `scripts/sense_env_runtime/runtime.py`

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
2. create `skills/sense-env-scaffold/`
3. copy the full required file set into the target tree
4. verify the target tree preserves structure and file presence
5. confirm `.github/skills/sense-env-scaffold/` remains unchanged
6. emit explicit evidence of deferred runtime/tooling blockers

## Verification Contract for the Future Execution Topic

The execution topic should verify at minimum:

- `skills/sense-env-scaffold/SKILL.md` exists
- `skills/sense-env-scaffold/references/` contains both reference files
- `skills/sense-env-scaffold/scripts/sense_env.py` exists
- `skills/sense-env-scaffold/scripts/sense_env_runtime/` contains all runtime files
- `.github/skills/sense-env-scaffold/` still exists after the copy
- no downstream caller path was changed from `.github/skills/.../sense_env.py`

## Deferred Blocker Inventory

This topic intentionally defers these runtime/tooling blocker lanes:

- updating downstream callers that reference
  `.github/skills/sense-env-scaffold/scripts/sense_env.py`
- introducing a compatibility alias, wrapper, or alternate active CLI path
- changing manifest output policy or snapshot policy
- changing the active-path assumptions in:
  - `python-project-init-greenfield`
  - `python-retrofit-plan-authoring`
  - `python-retrofit-plan-review`
  - `python-project-retrofit`

## Recommended Topic-local Evidence

If the future execution topic emits a migration report, it should state:

- candidate name
- source root
- target root
- copied file set
- compatibility layer preserved: yes
- active runtime path changed: no
- deferred blocker lanes

## Cost-of-Realization Assessment

| Workstream | Complexity | Main burden | Ongoing operational cost |
| --- | --- | --- | --- |
| candidate inventory verification | Low | confirming the source tree still matches the frozen file set | low |
| canonical tree creation | Low to medium | copying script + runtime package without drift | low |
| compatibility preservation | Low | avoiding accidental edits to `.github/skills/` | low |
| deferred-blocker evidence | Low | documenting exactly what was not solved yet | low |

## Architecture / Governance Compliance Check

| Dimension | Result | Notes |
| --- | --- | --- |
| target-architecture alignment | fits existing governance | creates `skills/` copy without claiming current active-path cutover |
| runtime contract preservation | fits existing blocker evidence | keeps `.github/skills/.../sense_env.py` as the active path |
| bounded child-topic scope | fits umbrella sequencing | only one Wave 1 candidate |
| shared governance protection | fits existing governance | no repo-wide contract or release changes |

## Rollback-to-Alignment Triggers

Return to alignment before execution if any of the following becomes true:

1. creating the canonical copy requires modifying `.github/skills/sense-env-scaffold/`
   behavior
2. the source tree gains additional required files that change the bounded copy
   surface materially
3. a stakeholder wants this topic to rewrite downstream callers or change the
   active CLI path
4. the topic cannot complete honestly without touching shared governance or
   release surfaces

## Ready-for-next-step Decision

This technical specification is complete enough to drive the next planning or
execution step for this candidate:

- author an execution topic plan for the bounded copy
- keep runtime-path migration and downstream caller rewrites as separate future work
