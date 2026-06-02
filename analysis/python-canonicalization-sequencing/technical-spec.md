# Technical Specification: python-canonicalization-sequencing

**Status**: READY FOR CHILD-TOPIC PLANNING
**Topic**: `python-canonicalization-sequencing`
**Date**: 2026-06-01
**Baseline Reference**: `analysis/python-canonicalization-sequencing/requirements.md`

---

## Source Baseline Summary

The frozen baseline requires a worktree-only umbrella topic that converts the
12-candidate salvage inventory into a decision-complete canonicalization
sequence.

The technical outcome is not skill migration. The technical outcome is a
sequencing contract that:

- preserves repo-root `dev` cleanliness
- defines wave ownership and candidate metadata
- emits the first useful child-topic backlog
- prevents hidden cutover, hidden migration, or hidden governance changes

## Requirement Traceability

| Requirement | Technical realization | Dependencies | Cost / burden | Status |
| --- | --- | --- | --- | --- |
| R1 Worktree-first materialization | Keep all writes in a dedicated managed worktree and add only two analysis artifacts | `git worktree`, repo path policy | Low | feasible |
| R2 Canonicalization-not-capability framing | Record active-equivalent status for all 12 candidates in the inventory model | existing `.github/skills/` inventory | Low | feasible |
| R3 Backbone-value ordering | Freeze sequencing rules and rationale fields in the candidate table | user-approved ordering logic | Low | feasible |
| R4 Retrofit-first Wave 1 | Author an ordered Wave 1 core block with non-swappable dependencies | candidate dependency review | Low | feasible |
| R5 Greenfield as Wave 1.5 | Keep `python-project-init-greenfield` adjacent but outside core Wave 1 | Wave 1 completion dependency | Low | feasible |
| R6 Governance / review Wave 2 | Group governance and review candidates behind the core lane | stable sensed-facts and plan core | Low | feasible |
| R7 Specialist Wave 3 | Group horizontal and specialist skills as later work | wave separation rules | Low | feasible |
| R8 Decision-complete candidate routing | Emit one row per candidate with routing fields and follow-up topic names | frozen wave model | Medium | feasible |
| R9 MVP stops at sequencing artifacts | Restrict allowed edits to the two analysis files and forbid skill mutations | repo boundary discipline | Low | feasible |

## Allowed Artifacts and Boundaries

### Allowed writes in this topic

- `analysis/python-canonicalization-sequencing/requirements.md`
- `analysis/python-canonicalization-sequencing/technical-spec.md`

### Forbidden writes in this topic

- any path under `skills/`
- any path under `.github/skills/`
- `AGENTS.md`
- `docs/repo-positioning.md`
- any child-topic `plan/<topic>/...` artifact

### Stop conditions

Stop and return to planning if any of the following becomes necessary:

1. a candidate needs content edits before sequencing can be stated honestly
2. the topic would need to declare `skills/` as the active path
3. the topic would need to edit creator, reviewer, template, runtime, or
   installer contracts
4. a future wave cannot be explained without changing the current repository
   positioning freeze
5. repo-root `dev` becomes the required write surface for this topic

## Execution Model

### Worktree realization

- Managed path: `../agent-skills.worktrees/agent-20260601-python-canonicalization-sequencing`
- Topic branch: `feat/andrew/python-canonicalization-sequencing`
- Execution rule: continue all topic work in the managed worktree only

### Artifact authority

1. `analysis/python-canonicalization-sequencing/technical-spec.md`
2. `analysis/python-canonicalization-sequencing/requirements.md`
3. later child-topic plans derived from this umbrella sequence

Authority notes:

- Hidden chat context does not outrank these repo-visible artifacts.
- If later child-topic planning contradicts the frozen wave model, route back
  here first instead of patching the order ad hoc.

## Candidate Routing Matrix

| Candidate | Current active equivalent | Target role | Wave | Can start now | Dependencies | Unlocks | Rationale | Follow-up topic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `sense-env-scaffold` | yes | canonical sensing foundation | 1 | yes | none | all Wave 1 topics | widest dependency surface; shared sensing base | `sense-env-scaffold-canonicalize` |
| `python-retrofit-plan-authoring` | yes | canonical retrofit entrypoint | 1 | yes | `sense-env-scaffold` sequencing frozen | review and execution lanes | first actionable retrofit planning surface | `python-retrofit-plan-authoring-canonicalize` |
| `python-retrofit-plan-review` | yes | canonical retrofit gate | 1 | yes | authoring topic sequencing frozen | execution lane safety | closes the authoring -> gate loop | `python-retrofit-plan-review-canonicalize` |
| `python-project-retrofit` | yes | canonical retrofit executor | 1 | yes | prior three Wave 1 candidates sequenced first | full retrofit spine | main execution value of the lane | `python-project-retrofit-canonicalize` |
| `python-project-init-greenfield` | yes | adjacent greenfield executor | 1.5 | yes | Wave 1 frozen | complete Python project lane | important, but not allowed to dilute the Retrofit-first core | `python-project-init-greenfield-canonicalize` |
| `copilot-instructions-init` | yes | governance output generator | 2 | blocked-on-wave-1 | stable sensing spine | instruction refresh lane | depends on sensed facts and installed-skill inventory | `copilot-instructions-init-canonicalize` |
| `python-implementation-review` | yes | implementation contract gate | 2 | blocked-on-wave-1 | stable plan-driven core | code review lane | review chain should follow core lane stabilization | `python-implementation-review-canonicalize` |
| `python-code-review` | yes | quality gate | 2 | blocked-on-wave-2 | `python-implementation-review` sequencing frozen | review-chain completeness | explicitly downstream of implementation review | `python-code-review-canonicalize` |
| `python-async-planning` | yes | async-risk overlay | 2 | blocked-on-wave-1 | core planning lane stable | specialist review support | high value but conditional, not backbone-first | `python-async-planning-canonicalize` |
| `git-post-merge-workflow` | yes | horizontal workflow helper | 3 | blocked-on-wave-2 | core and governance lane stable | repo workflow helper wave | useful but not central to Python canonical backbone | `git-post-merge-workflow-canonicalize` |
| `git-release-management` | yes | release governance helper | 3 | blocked-on-wave-2 | governance context stable | release helper wave | horizontal governance, lower backbone leverage | `git-release-management-canonicalize` |
| `python-serialization-boundaries` | yes | specialist design skill | 3 | blocked-on-wave-1 | core canonical lane stable | specialist architecture wave | valuable but topic-specific rather than spine-forming | `python-serialization-boundaries-canonicalize` |

## Wave Model

### Wave 1 — Retrofit spine core

Ordered, non-swappable sequence:

1. `sense-env-scaffold`
2. `python-retrofit-plan-authoring`
3. `python-retrofit-plan-review`
4. `python-project-retrofit`

Why the order is fixed:

- sensing must be available before canonical retrofit planning is stabilized
- authoring must exist before review can act as a true gate
- review must be positioned before the retrofit executor if the lane is meant to
  be self-consistent

### Wave 1.5 — Greenfield adjacency completion

- `python-project-init-greenfield`

Reason:

- it belongs near the core Python lane
- it benefits from the same canonicalization framing
- it is not a prerequisite for the Retrofit-first spine

### Wave 2 — Governance and review chain

- `copilot-instructions-init`
- `python-implementation-review`
- `python-code-review`
- `python-async-planning`

Reason:

- these candidates gain clarity from a stable canonical core
- they are important governance surfaces, but they are not the first backbone

### Wave 3 — Horizontal and specialist follow-up

- `git-post-merge-workflow`
- `git-release-management`
- `python-serialization-boundaries`

Reason:

- these candidates are horizontal helpers or specialist overlays
- delaying them does not block formation of the canonical Python backbone

## Minimum Viable Task Backlog

This umbrella topic emits the following first useful downstream tasks:

| Task | Scope | Output |
| --- | --- | --- |
| T1 | freeze canonicalization topic for `sense-env-scaffold` | child-topic requirements/spec or plan, owned separately |
| T2 | freeze canonicalization topic for `python-retrofit-plan-authoring` | child-topic requirements/spec or plan, owned separately |
| T3 | freeze canonicalization topic for `python-retrofit-plan-review` | child-topic requirements/spec or plan, owned separately |
| T4 | freeze canonicalization topic for `python-project-retrofit` | child-topic requirements/spec or plan, owned separately |
| T5 | author a cross-topic dependency map for the four Wave 1 candidates | explicit ordering and non-swappable dependency notes |

T5 is required because:

- the Wave 1 order is the core migration claim of this umbrella topic
- later child-topic authors should not re-argue dependency direction

## Child-topic Backlog Emitted by This Spec

1. `sense-env-scaffold-canonicalize`
2. `python-retrofit-plan-authoring-canonicalize`
3. `python-retrofit-plan-review-canonicalize`
4. `python-project-retrofit-canonicalize`
5. `python-project-init-greenfield-canonicalize`
6. `governance-review-chain-sequencing`
7. `workflow-specialist-skill-sequencing`

Backlog note:

- items 6 and 7 are grouping topics, not immediate per-skill execution topics
- this umbrella topic does not require any of those plans to be authored yet

## Cost-of-Realization Assessment

| Workstream | Complexity | Main burden | Ongoing operational cost |
| --- | --- | --- | --- |
| umbrella analysis authoring | Low | freezing the order clearly enough to avoid later resequencing | low |
| candidate routing matrix | Medium | making every row decision-complete for downstream use | low |
| Wave 1 dependency freeze | Medium | defending non-swappable ordering up front | low |
| later child-topic expansion | Medium | each child topic still needs its own bounded planning pass | medium |

## Architecture / Governance Compliance Check

| Dimension | Result | Notes |
| --- | --- | --- |
| repo positioning alignment | fits existing governance | keeps `.github/skills/` current and `skills/` target-only |
| topic boundary control | fits existing governance | analysis-only umbrella topic |
| worktree isolation | fits existing governance | keeps repo-root `dev` clean |
| active-path preservation | fits existing governance | no cutover language introduced |
| child-topic readiness | fits with prerequisites | later plans can route from the matrix directly |

## Rollback-to-Alignment Triggers

Route back to `business-intent-alignment` style clarification if:

1. any candidate is found not to have an active `.github/skills/` equivalent
2. a stakeholder wants to optimize by immediate usability instead of backbone value
3. `python-project-init-greenfield` is proposed for promotion into Wave 1 core
4. a Wave 2 or Wave 3 candidate is argued to be a hard prerequisite for the
   Retrofit spine
5. a child-topic planner cannot route from the candidate matrix without adding
   new hidden sequencing rules

## Ready-for-next-step Decision

This technical specification is complete enough to drive the next step:

- author child-topic planning artifacts for the Wave 1 candidates
- keep `python-project-init-greenfield` queued as the first adjacent follow-up
- defer Wave 2 and Wave 3 until the core child-topic lane is frozen
