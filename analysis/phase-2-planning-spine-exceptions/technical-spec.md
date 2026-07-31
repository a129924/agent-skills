# phase-2-planning-spine-exceptions technical spec

## Technical outcome

Produce a repo-visible planning baseline for the final Phase 2 execution slice
that is narrow enough to permit later bounded canonical convergence inside
`skills/plan-creator/**` and `skills/plan-reviewer/**` without reopening
generic Phase 2 framing.

## Read-only evidence basis

This topic relies on:

- `AGENTS.md`
- `docs/repo-positioning.md`
- `plan/agent-handoff-workflow.md`
- `plan/topic-plan-contract.md`
- `plan/phase-2-umbrella/phase-2-umbrella.plan.md`
- `plan/phase-2-umbrella/phase-2-umbrella.step.md`
- `plan/phase-2-safe-canonical-batch/phase-2-safe-canonical-batch.step.md`
- `plan/phase-2-merge-into-skills-batch/phase-2-merge-into-skills-batch.plan.md`
- `plan/phase-2-merge-into-skills-batch/phase-2-merge-into-skills-batch.step.md`
- `docs/agent-skills-convergence/phase-1/04-semantic-drift-report.md`
- `docs/agent-skills-convergence/phase-1/05-runtime-dependency-inventory.md`
- `docs/agent-skills-convergence/phase-1/06-convergence-candidates.md`
- `docs/agent-skills-convergence/phase-1/07-phase-2-inputs.md`
- `docs/agent-skills-convergence/phase-1/09-human-review-verdict.md`

## Frozen execution targets

Later execution under this topic may modify only:

- `skills/plan-creator/**`
- `skills/plan-reviewer/**`

Initial planning under this topic may modify only:

- `analysis/phase-2-planning-spine-exceptions/requirements.md`
- `analysis/phase-2-planning-spine-exceptions/technical-spec.md`
- `plan/phase-2-planning-spine-exceptions/phase-2-planning-spine-exceptions.plan.md`
- `plan/phase-2-planning-spine-exceptions/phase-2-planning-spine-exceptions.step.md`

## Convergence model

Canonical convergence for this topic means:

1. keeping `skills/` as the only execution target
2. removing skill-local wording that still treats `.github/skills/` or
   `.codex/skills/` as required authority roots
3. removing direct cross-skill authority coupling between `plan-creator` and
   `plan-reviewer`
4. aligning skill-local wording so that repo-level workflow and plan-contract
   files remain the authority basis
5. preserving explicit stop-and-ask behavior where behavior drift would
   otherwise be guessed

Canonical convergence does not mean:

- editing `.github/**`
- editing `.codex/**`
- generating `.<platform>/skills/...`
- generating `.<platform>/agents/...`
- rewriting repo-level workflow or contract meaning inside this topic without a
  separately approved scope change

## Workstreams

### Workstream A: topic baseline

Create the four topic-local planning artifacts and freeze the bounded skill
set, read-only evidence basis, and non-stable intent.

### Workstream B: convergence-ready decision surface

Define which later edits are presumptively safe inside `skills/`:

- path-neutralization away from `.github/skills/...` or `.codex/skills/...`
  references
- wording cleanup that points authority back to repo-level contract files
- removal of wording that makes either skill depend on the other as a required
  authority source

### Workstream C: preserved high-risk exceptions

Record `human_review_required` for any item that would change:

- workflow-phase semantics
- reviewer handoff meaning
- blocked behavior when required sources are unreadable
- close or progression truth semantics
- repo-level authority ordering

## Expected later execution constraints

If execution is later approved, it must:

- work one bounded skill at a time
- modify only `skills/plan-creator/**` or `skills/plan-reviewer/**`
- keep `.github/**` and `.codex/**` read-only
- stop for human review whenever canonical wording would implicitly redefine
  repo-level workflow or contract meaning

## Explicit unresolved items

These remain unresolved by design at planning time:

- whether `plan-creator` fallback language can be canonicalized without
  changing failure behavior
- whether `plan-reviewer` blocked behavior when shared sources are missing
  already conflicts with repo-level contract semantics
- whether either skill's local examples/checklists/reference material encode
  behavior that should stay local versus move entirely to repo-level contract
  interpretation

Each unresolved item must remain `human_review_required` until later execution
provides evidence that the change is wording-only and does not alter behavior.

## Validation targets

- The topic plan must explicitly declare non-stable intent.
- The topic plan must use canonical required sections from
  `plan/topic-plan-contract.md`.
- The topic plan must state that planning-spine exception execution is limited
  to `skills/plan-creator/**` and `skills/plan-reviewer/**`.
- The topic step artifact must stop no later than `human-check`.
- No planning artifact may imply permission to edit `.github/**` or `.codex/**`.
