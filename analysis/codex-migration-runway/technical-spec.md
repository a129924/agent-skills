# codex-migration-runway technical specification

Status: READY FOR PLAN AUTHORING
Topic: `codex-migration-runway`
Source baseline: `analysis/codex-migration-runway/requirements.md`
Primary execution branch: `feat/andrew/copilot-to-codex-migration`

## Source baseline summary

The frozen baseline requires a runway-only global planning layer for the
repository's Copilot-to-Codex migration effort. The current topic must not
perform migration. It must define a bounded operating model, source-of-truth
order, branch/worktree rules, and an executable first-phase plan for
`positioning-freeze`.

Human override:

- The runway analysis artifacts live under `analysis/codex-migration-runway/`.
- The first bounded phase plan lives at
  `plan/positioning-freeze/positioning-freeze.plan.md`.
- This split topology is intentional and overrides the repository's usual
  same-topic analysis/plan pairing for this one runway setup.

## Requirement traceability

| Requirement | Technical realization | Dependencies | Cost / burden | Status |
| --- | --- | --- | --- | --- |
| R1 Runway-only goal | Repeat the runway-only boundary in all three artifacts and forbid wording that implies migration execution | `AGENTS.md`, `docs/repo-positioning.md`, user-locked assumptions | Low | feasible |
| R2 Agent model | Define Setup Agent and Bounded Implement Agent responsibilities in the runway analysis docs and first phase plan | Repo workflow semantics from `plan/agent-handoff-workflow.md` | Low | feasible |
| R3 Planning spine | Name `.github/skills/business-intent-alignment` and `.github/skills/business-to-technical-translation` as required planning-spine inputs in requirements, spec, and plan | Existing skill contracts | Low | feasible |
| R4 Source-of-truth order | Define authority ordering and handoff-field precedence in the runway analysis docs and reflect them in the first phase plan | Repo-visible artifact structure | Low | feasible |
| R5 Big Feature Branch model | Create the branch/worktree and encode merge routing: phase branch -> Big Feature Branch -> later human-controlled integration | Git worktree support and repo branch policy | Low to medium | feasible |
| R6 First executable phase | Author `plan/positioning-freeze/positioning-freeze.plan.md` in strict mode against this spec | Analysis artifacts and plan template | Medium | feasible |
| R7 Boundary enforcement | Encode forbidden areas for `positioning-freeze`, especially creator / reviewer / template contracts and `.github/skills/*` skill contracts | `AGENTS.md`, `docs/repo-positioning.md`, user-locked exclusions | Low | feasible |
| R8 Current-state wording preservation | Copy forward transition wording without promoting `skills/` to active path | `AGENTS.md`, `docs/repo-positioning.md`, `README.md`, `.github/copilot-instructions.md` | Low | feasible |
| R9 Implementer handoff contract | Define required handoff fields and stop conditions in the spec and phase plan | Repo workflow contract and planning rules | Medium | feasible |
| R10 Explicit contradiction handling | Add an unresolved-gaps section and require surfaced contradictions instead of silent reconciliation | Human-locked decisions and current repo docs | Low | feasible |

## Required technical artifacts

| Artifact | Path | Purpose |
| --- | --- | --- |
| Business baseline | `analysis/codex-migration-runway/requirements.md` | Frozen requirement baseline for the runway |
| Technical baseline | `analysis/codex-migration-runway/technical-spec.md` | Execution-facing technical source of truth for the runway |
| First phase plan | `plan/positioning-freeze/positioning-freeze.plan.md` | Repo-visible execution contract for the first bounded implement phase |

## Operating model

### Setup Agent responsibilities

- create and maintain the runway-level analysis artifacts
- define the global goal and non-goals
- define the planning spine
- define the observer / planner operating model
- define branch/worktree routing
- define implementer handoff contract
- prepare the first bounded phase context

### Bounded Implement Agent responsibilities

- execute exactly one authorized phase plan
- modify only the listed allowed paths
- stop on contradiction, missing authority, or scope drift
- avoid authoring adjacent phase plans or widening the branch mission

### Observer / planner operating model

- treat repo-visible artifacts as the planning authority
- verify alignment before implementation starts and before any scope repair
- route contradictions back to planning instead of self-healing them inside
  execution
- maintain strict separation between global baseline work and bounded phase work

## Planning spine realization

The runway planning spine is mandatory and ordered:

1. `.github/skills/business-intent-alignment`
2. `.github/skills/business-to-technical-translation`
3. repo-visible plan authoring at `plan/<topic>/<topic>.plan.md`

For this topic, the first two steps are embodied by:

- `analysis/codex-migration-runway/requirements.md`
- `analysis/codex-migration-runway/technical-spec.md`

The third step is embodied by:

- `plan/positioning-freeze/positioning-freeze.plan.md`

## Source-of-truth and artifact authority

The runway must freeze this authority order for bounded implementation:

1. `plan/positioning-freeze/positioning-freeze.plan.md`
2. `analysis/codex-migration-runway/technical-spec.md`
3. `analysis/codex-migration-runway/requirements.md`
4. handoff prompt fields: worktree path, current branch, target branch, allowed
   paths, locked decisions, stop conditions

Authority notes:

- Hidden chat context must not outrank repo-visible artifacts.
- If handoff wording conflicts with the plan or analysis artifacts, execution
  stops and returns to planning.
- Allowed-path drift is a contract violation, not a minor implementation detail.

## Big Feature Branch realization

- Create and use `feat/andrew/copilot-to-codex-migration` as the runway's main
  feature line.
- Host the runway baseline on a dedicated worktree so later phases can branch
  from a stable baseline.
- Route phase integration as:
  - phase worktree / phase branch
  - merge back into `feat/andrew/copilot-to-codex-migration`
  - do not merge phase work directly into `dev`
- Preserve `dev` as the clean baseline during runway execution.

## Technical tasks and sequencing

1. Create the Big Feature Branch and dedicated worktree for the runway.
2. Author `analysis/codex-migration-runway/requirements.md` as the frozen
   global requirement baseline.
3. Author `analysis/codex-migration-runway/technical-spec.md` as the execution
   baseline for later bounded implement work.
4. Author `plan/positioning-freeze/positioning-freeze.plan.md` in strict mode
   so it maps 100% to this technical specification.
5. Freeze the implementer handoff contract inside the plan with:
   - exact worktree path expectation
   - current branch expectation
   - target phase branch naming pattern
   - exact allowed paths
   - locked decisions
   - stop conditions
6. Use an independent review pass on the authored plan artifacts before
   downstream execution starts.

## First phase design: positioning-freeze

The first bounded implement phase must:

- freeze repository positioning only
- clarify current operating state, target architecture, and migration boundary
- prepare documentation-level alignment without performing path migration

The first bounded implement phase must not:

- migrate skill directories
- edit creator / reviewer / template contracts
- edit `.github/skills/*` skill contract bodies
- author `platform-coupling-inventory.plan.md`
- author transition or promotion phases
- add `.codex/`, `.claude/`, or script-based migration helpers

## Implementer handoff contract

Each bounded phase handoff must explicitly include:

- worktree path
- current branch
- target phase branch
- PR target branch
- allowed file paths
- locked decisions
- out-of-scope work
- stop conditions
- required source-of-truth artifacts in authority order

Minimum stop conditions:

- requested change falls outside allowed paths
- requested change would alter creator / reviewer / template contracts when the
  phase does not authorize it
- requested change would modify `.github/skills/*` contract content during
  `positioning-freeze`
- requested change implies full migration or active-path cutover
- phase instructions contradict repo-visible artifacts

## Cost-of-realization assessment

| Workstream | Complexity | Main burden | Ongoing operational cost |
| --- | --- | --- | --- |
| Runway analysis authoring | Low | freezing terms precisely enough to prevent phase drift | low |
| Branch / worktree setup | Low | keeping a clean integration line outside `dev` | low |
| Phase-plan authoring | Medium | encoding enough handoff detail that a bounded implementer does not guess | low |
| Contract review | Medium | validating role boundaries and contradiction handling before execution | low |

## Architecture-compliance self-check

| Dimension | Result | Notes |
| --- | --- | --- |
| Governance alignment | fits existing architecture | preserves `AGENTS.md` and `docs/repo-positioning.md` authority |
| Current-vs-target wording | fits existing architecture | keeps `.github/skills/` current and `skills/` target only |
| Branch isolation | fits with prerequisites | requires later phases to merge back into the Big Feature Branch first |
| Scope control | fits existing architecture | first phase is documentation/planning only |
| Platform neutrality | fits existing architecture | no `.codex/` or `.claude/` layout is added |
| Installer boundary | fits existing architecture | external installer work remains out of scope |

## Conflicts, blockers, and rollback triggers

Creator or implementer work must roll back to planning if any of the following
becomes true:

1. `positioning-freeze` needs to change creator / reviewer / template contract
   content to achieve its stated goal.
2. A later implementer claims `skills/` must become the current active path
   inside this runway-only topic.
3. A phase requires inventory, promotion, installer, or script work to proceed,
   but that work has no frozen plan artifact yet.
4. The Big Feature Branch model conflicts with an existing branch strategy that
   the human wants to preserve.
5. Repo-visible artifacts disagree about current operating state or migration
   boundary.
6. A later agent tries to normalize this runway into a same-topic analysis/plan
   spine without explicit human approval, despite the locked split-topology
   override.

## Ready-for-plan decision

This technical specification is complete enough to drive strict-mode authoring
of `plan/positioning-freeze/positioning-freeze.plan.md`.
