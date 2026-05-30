# codex-skill-direct-move-impl-ab requirements baseline

Status: PLANNED
Topic: `codex-skill-direct-move-impl-ab`
Risk level: `medium`
Planned target branch: `feat/andrew/codex-skill-direct-move-impl-ab`
Planned worktree: `/Users/andrew/code/python/agent-skills.worktrees/agent-20260529-codex-skill-direct-move-impl-ab`

## Problem statement

The repository has a committed bootstrap baseline for the A/B migration set,
but it still lacks a dedicated implementation-topic contract that a later
`migration-implementation` run can load without rediscovering scope,
write-boundaries, or the transition-era positioning that keeps
`.github/skills/` active.

## Goal

Create a repo-visible implementation-topic contract that:

- consumes the committed `codex-skill-direct-move-ab` baseline as current truth
- authorizes only A/B migration work under a later implementation workflow
- keeps `.github/skills/` read-only source context during this topic
- requires repo-visible progression truth through `step.md`
- records a pre-launch summary that tells the next agent exactly what remains
  blocked before implementation can start

## Source baseline inputs

The following committed artifacts are hard prerequisites and outrank chat-only
intent:

- `analysis/codex-skill-direct-move-ab/requirements.md`
- `analysis/codex-skill-direct-move-ab/technical-spec.md`
- `plan/codex-skill-direct-move-ab/codex-skill-direct-move-ab.plan.md`
- `plan/codex-skill-direct-move-ab/codex-skill-direct-move-ab.migration-checklist.md`
- `plan/codex-skill-direct-move-ab/codex-skill-direct-move-ab.summary.md`
- `docs/process/overlays/agent-skills-transition-overlay.md`

## In-scope writable targets for the later implementation topic

- `skills/python-package-layout/`
- `skills/python-library-architecture/`
- `skills/python-plan-authoring/`
- `skills/python-blueprint-authoring/`
- `skills/python-pre-commit/`
- `skills/python-pyproject-toolconfig/`
- `skills/python-tdd-test-authoring/`
- `analysis/codex-skill-direct-move-impl-ab/`
- `plan/codex-skill-direct-move-impl-ab/`
- `.workflow-runs/<run-id>/` for the later workflow run only

## Explicitly out of scope

- any modification under `.github/skills/`
- any C-class skill
- `AGENTS.md`
- `docs/repo-positioning.md`
- shared workflow or policy files under `docs/process/`
- any commit, push, PR, release, or cleanup action
- repo-wide path cutover claims

## Measurable requirements

| ID | Requirement | Observable result | Pass rule |
| --- | --- | --- | --- |
| R1 | The implementation topic stays bounded to the 2 A-class and 5 B-class skills frozen by the bootstrap baseline | Topic plan and step artifact name only those 7 skills as implementation scope | No C-class or shared governance path enters writable scope |
| R2 | A-class work is treated as semantic direct-move implementation | Topic plan states that `python-package-layout` and `python-library-architecture` are implemented in `skills/` without new workflow coupling | A-class output does not require reviewer JSON, acceptance command, or executor handoff semantics |
| R3 | B-class work is treated as semantic rewrite implementation | Topic plan states that the 5 B-class skills are implemented as Codex-oriented semantic skills in `skills/` | B-class output removes the frozen workflow / artifact coupling named in the bootstrap baseline |
| R4 | `.github/skills/` remains source context, not writable migration output | Plan, step, and summary all mark `.github/skills/` as read-only for this topic | No implementation step authorizes edits under `.github/skills/` |
| R5 | A required `step.md` exists before any later implementation run starts | Repo-visible progression artifact is present at the implementation-topic path | Main Agent can satisfy the workflow's required `step.md` precondition without chat-only inference |
| R6 | The implementation topic exposes unresolved launch blockers explicitly | Summary artifact records overlay uncertainty and worktree-preparation dependency | A later agent can tell whether launch is blocked without rereading chat |
| R7 | The implementation topic remains transition-era compliant | No artifact claims current-path cutover or `.github/skills/` retirement | The topic can implement `skills/` outputs without redefining repository positioning |

## Non-goals

- performing the actual skill migration in this planning turn
- validating or inventing repository-specific overlay rules
- selecting a different candidate set than the committed A/B baseline
- reopening bootstrap planning for candidate discovery
- altering baseline artifacts from `codex-skill-direct-move-ab`

## Assumptions

- The committed bootstrap baseline remains the approved source of truth for A/B
  membership and per-skill migration intent.
- The later implementation topic may target a new branch and worktree even
  though this planning turn does not create either.
- The reviewed overlay document is part of the same topic-bounded planning
  artifact set, but whether the overlay is actually bound for a later run is
  still determined from the approved topic scope at launch time.
