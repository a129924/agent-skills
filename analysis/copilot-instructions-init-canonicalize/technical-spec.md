# Technical Specification: copilot-instructions-init-canonicalize

**Status**: READY FOR EXECUTION PLANNING
**Topic**: `copilot-instructions-init-canonicalize`
**Date**: 2026-06-01
**Baseline Reference**: `analysis/copilot-instructions-init-canonicalize/requirements.md`

---

## Source Baseline Summary

The frozen baseline requires one bounded child topic that promotes
`copilot-instructions-init` into `skills/` as a canonical copy while
preserving the existing transition-era target output, stale-fact, and
merge-policy contract during transition.

This is intentionally not a target output-path migration, stale-gate redesign,
or merge-policy behavior repair topic.

## Requirement Traceability

| Requirement | Technical realization | Dependencies | Cost / burden | Status |
| --- | --- | --- | --- | --- |
| R1 Single-candidate scope | Lock edits to `copilot-instructions-init` only | umbrella Wave 2 sequence | Low | feasible |
| R2 Create canonical copy | Create `skills/copilot-instructions-init/` with the full file set | current `.github/skills/copilot-instructions-init/` contents | Low | feasible |
| R3 Preserve transition-era contracts | Leave target `.github/copilot-instructions.md`, stale-fingerprint rules, and merge-choice policy in place | existing blocker evidence in source skill | Low | feasible |
| R4 Copy full surface | Copy checklist, examples, and all three references together | current file inventory | Low | feasible |
| R5 Preserve compatibility layer | Keep `.github/skills/copilot-instructions-init/` unchanged as the transition surface | repo positioning freeze | Low | feasible |
| R6 Defer blocker repair | Record deferred target output, stale-gate, merge-policy, and projection lanes | current source skill contract | Low | feasible |
| R7 Protect shared governance | Forbid edits outside candidate-local surfaces and topic-local evidence | repo governance boundaries | Low | feasible |
| R8 Leave explicit migration evidence | Emit a topic-local report describing the copy and deferrals | implementation topic boundary | Low | feasible |

## Allowed Artifacts for the Execution Topic

This technical spec authorizes edits only to:

- `analysis/copilot-instructions-init-canonicalize/requirements.md`
- `analysis/copilot-instructions-init-canonicalize/technical-spec.md`
- `plan/copilot-instructions-init-canonicalize/copilot-instructions-init-canonicalize.plan.md`
- `skills/copilot-instructions-init/`
- `docs/migration/copilot-instructions-init-canonicalize.md`

This technical spec does **not** authorize edits to:

- `.github/skills/copilot-instructions-init/`
- `python-project-init-greenfield`
- `python-implementation-review`
- `python-code-review`
- `AGENTS.md`
- `docs/repo-positioning.md`
- `README.md`
- `VERSION`
- `.codex/skills/`

## Copy Boundary

Source root:

- `.github/skills/copilot-instructions-init/`

Target root:

- `skills/copilot-instructions-init/`

Required copied paths:

- `SKILL.md`
- `checklist.md`
- `examples.md`
- `references/input-sources-and-priority.md`
- `references/instruction-layering.md`
- `references/merge-and-conflict-policy.md`

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
2. create `skills/copilot-instructions-init/`
3. copy the full required file set into the target tree
4. verify the target tree preserves structure and file presence
5. confirm `.github/skills/copilot-instructions-init/` remains unchanged
6. emit explicit evidence of deferred runtime/tooling and policy-coupling blockers

## Verification Contract

The execution topic should verify at minimum:

- `skills/copilot-instructions-init/SKILL.md` exists
- `skills/copilot-instructions-init/checklist.md` exists
- `skills/copilot-instructions-init/examples.md` exists
- `skills/copilot-instructions-init/references/` contains all three required files
- `.github/skills/copilot-instructions-init/` still exists after the copy
- no source artifact under `.github/skills/copilot-instructions-init/` was modified
- no artifact in this topic claims active-path cutover or target output-path
  cutover away from `.github/...`

## Deferred Blocker Inventory

This topic intentionally defers these runtime/tooling and policy-coupling lanes:

- changing the target output destination away from target-project
  `.github/copilot-instructions.md`
- changing stale-fact coupling away from `.github/skills/` summary fingerprints
- changing managed-block marker policy or materially-different classification rules
- changing overwrite / keep / manual-merge decision policy
- changing downstream active-path assumptions for instruction generation
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
| transition-era contract preservation | fits existing blocker evidence | keeps target `.github/copilot-instructions.md`, stale-fact, and merge-policy assumptions in place |
| bounded child-topic scope | fits umbrella sequencing | only one Wave 2 candidate |
| shared governance protection | fits existing governance | no repo-wide contract or release changes |

## Rollback-to-Alignment Triggers

Return to alignment before execution if any of the following becomes true:

1. creating the canonical copy requires modifying
   `.github/skills/copilot-instructions-init/` behavior
2. the source tree gains additional required files that change the bounded copy
   surface materially
3. a stakeholder wants this topic to rewrite target output, stale-fingerprint,
   merge-policy, or projection behavior
4. the topic cannot complete honestly without touching shared governance or
   release surfaces

## Ready-for-next-step Decision

This technical specification is complete enough to drive the next planning or
execution step for this candidate:

- execute the bounded copy into `skills/copilot-instructions-init/`
- keep target output, stale-gate, and merge-policy rewrites as separate future work
