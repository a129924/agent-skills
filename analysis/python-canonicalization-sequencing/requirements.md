# Requirements: python-canonicalization-sequencing

**Status**: FROZEN — planning baseline ready; canonicalization execution remains future work
**Topic**: `python-canonicalization-sequencing`
**Date**: 2026-06-01

---

## Problem Statement

The repository already has active `.github/skills/` equivalents for the 12
salvage candidates, so the current gap is not missing capability.

The missing contract is a repo-visible sequencing baseline that:

- prioritizes canonicalization work by future `skills/` backbone value
- separates core-lane work from governance and specialist follow-up
- defines a minimum viable sequencing wave that can unlock later child topics
- keeps repo-root `dev` clean by requiring topic work to live in a dedicated
  worktree

## Actors

| Actor | Role |
| --- | --- |
| Sequencing planning actor | Freezes the ordering model, wave structure, and follow-up topic backlog |
| Main Agent | Creates and uses the dedicated worktree, then authors the analysis artifacts there |
| Future child-topic planner | Uses this baseline to author per-candidate canonicalization topics later |
| Human operator | Approves sequencing direction and preserves the no-cutover boundary |

## Frozen Requirements

### R1 — Worktree-first materialization is mandatory

When this topic starts, all repo-visible writes for this topic MUST occur only
inside a dedicated external worktree, not on repo-root `dev`.

- Actor: Main Agent
- Condition: topic bootstrap begins
- Observable: `analysis/python-canonicalization-sequencing/requirements.md` and
  `analysis/python-canonicalization-sequencing/technical-spec.md` exist only in
  the dedicated worktree during authoring
- Acceptance: repo-root `dev` stays free of this topic's planning artifacts
- Failure meaning: the sequencing topic contaminates the shared root workspace

### R2 — The topic must classify a canonicalization problem, not a capability gap

The baseline MUST state that all 12 candidates already have active
`.github/skills/` counterparts and therefore the current problem is ordering
for canonicalization, not feature creation.

- Actor: sequencing planning actor
- Condition: the baseline explains why the topic exists
- Observable: the document explicitly distinguishes `canonicalization /
  migration ordering` from `missing skill capability`
- Acceptance: a future implementer cannot mistake this topic for skill-gap
  backfill work
- Failure meaning: later work may incorrectly prioritize new behavior over
  source-of-truth consolidation

### R3 — Ordering must be driven by future canonical backbone value

The primary prioritization rule MUST be whether a candidate helps form a
complete future canonical backbone under `skills/`, not whether the skill is
already usable today.

- Actor: sequencing planning actor
- Condition: candidate ordering is frozen
- Observable: each candidate has a rationale tied to backbone value, dependency
  centrality, or chain completeness
- Acceptance: the resulting order is explainable without referencing current
  active-path usability
- Failure meaning: the sequence optimizes for the wrong problem and weakens the
  migration spine

### R4 — Retrofit spine is the first mandatory wave

The first canonicalization wave MUST be the Retrofit core chain, in this order:

1. `sense-env-scaffold`
2. `python-retrofit-plan-authoring`
3. `python-retrofit-plan-review`
4. `python-project-retrofit`

- Actor: sequencing planning actor
- Condition: Wave 1 is defined
- Observable: all four candidates are grouped as one ordered spine
- Acceptance: the wave forms a self-consistent environment-sensing and retrofit
  execution chain
- Failure meaning: future canonicalization begins from a fragmented lane

### R5 — Greenfield execution stays adjacent but not inside the core wave

`python-project-init-greenfield` MUST be classified immediately after the
Retrofit core wave as `Wave 1.5`, not merged into the core ordering and not
deferred behind governance-only work.

- Actor: sequencing planning actor
- Condition: the greenfield executor is classified
- Observable: the candidate appears as a first-follow-up completion item after
  Wave 1
- Acceptance: the baseline preserves backbone adjacency without diluting the
  Retrofit-first core
- Failure meaning: the first canonicalization sequence either widens too early
  or leaves the Python project lane structurally incomplete

### R6 — Governance and review chain must be a separate second wave

The second wave MUST group governance and review-chain candidates after the
core execution spine stabilizes:

- `copilot-instructions-init`
- `python-implementation-review`
- `python-code-review`
- `python-async-planning`

- Actor: sequencing planning actor
- Condition: post-core waves are frozen
- Observable: these candidates are grouped separately from Wave 1 and Wave 1.5
- Acceptance: downstream governance work is explicitly shown to depend on a
  stable canonical core rather than compete with it
- Failure meaning: governance work may displace the higher-value backbone work

### R7 — Horizontal and specialist skills must remain the third wave

The third wave MUST contain the cross-cutting or specialist candidates:

- `git-post-merge-workflow`
- `git-release-management`
- `python-serialization-boundaries`

- Actor: sequencing planning actor
- Condition: the long-tail wave is frozen
- Observable: all three candidates are grouped as later horizontal /
  specialist work
- Acceptance: the baseline preserves focus on the canonical Python backbone
  before workflow helpers and specialist design skills
- Failure meaning: the sequence dilutes core migration progress with lower-leverage work

### R8 — Every candidate must be decision-complete enough for later routing

Each of the 12 candidates MUST carry enough metadata for a later child-topic
planner to route work without rediscovering the sequence.

Required fields:

- candidate
- wave
- why-now rationale
- upstream dependencies
- downstream unlocks
- can-start-now or blocked state
- recommended follow-up topic name

- Actor: sequencing planning actor
- Condition: the inventory table is authored
- Observable: every row has the full routing field set
- Acceptance: later topic planning can start from the table directly
- Failure meaning: the umbrella topic still leaves hidden sequencing decisions

### R9 — MVP output must stop at sequencing and task backlog

This topic's minimum viable outcome MUST freeze:

- the 12-candidate sequence
- the wave model
- the first-wave task backlog
- the follow-up topic backlog

This topic MUST NOT directly perform:

- skill moves
- active-path cutover
- creator / reviewer / template contract changes
- runtime / tooling path changes
- `.github/skills/` or `skills/` content edits

- Actor: Main Agent / sequencing planning actor
- Condition: the topic is implemented
- Observable: only the two analysis artifacts are added
- Acceptance: the topic remains a planning baseline, not execution-by-stealth
- Failure meaning: the topic silently performs migration work outside its
  stated boundary

## Candidate Wave Freeze

| Candidate | Wave | Role in sequence |
| --- | --- | --- |
| `sense-env-scaffold` | Wave 1 | environment-sensing foundation |
| `python-retrofit-plan-authoring` | Wave 1 | retrofit planning entrypoint |
| `python-retrofit-plan-review` | Wave 1 | retrofit planning gate |
| `python-project-retrofit` | Wave 1 | retrofit execution lane |
| `python-project-init-greenfield` | Wave 1.5 | greenfield executor adjacent to the core lane |
| `copilot-instructions-init` | Wave 2 | governance output dependent on sensed facts |
| `python-implementation-review` | Wave 2 | plan-driven implementation gate |
| `python-code-review` | Wave 2 | quality gate after implementation review |
| `python-async-planning` | Wave 2 | specialist planning overlay for async risk |
| `git-post-merge-workflow` | Wave 3 | horizontal repo workflow helper |
| `git-release-management` | Wave 3 | release governance helper |
| `python-serialization-boundaries` | Wave 3 | specialist design boundary skill |

## Non-goals

- Do not move any candidate from `.github/skills/` to `skills/` in this topic.
- Do not declare `skills/` as the current active authored / reviewed path.
- Do not edit creator, reviewer, template, runtime, or installer contracts.
- Do not create child-topic plans in this umbrella topic.
- Do not treat repo-root `dev` as an allowed write surface for this topic.

## Resolved Contradictions

### C1 — active usability vs canonical backbone value

- Conflict: current usability could imply all 12 items are equally low urgency
- Resolution: prioritize by future canonical backbone value, not by today's
  active-path availability

### C2 — greenfield executor in core wave vs later governance wave

- Conflict: `python-project-init-greenfield` is important to the Python lane,
  but widening Wave 1 too early weakens the Retrofit-first chain
- Resolution: classify it as `Wave 1.5`

### C3 — umbrella topic vs per-candidate topic depth

- Conflict: pushing into per-candidate implementation detail now would create a
  hidden execution topic
- Resolution: freeze only sequencing, task backlog, and child-topic backlog in
  this umbrella topic

## Explicit Assumptions

- A1: `.github/skills/` remains the current active authored / reviewed path
  during this topic
- A2: `skills/` remains target architecture only during this topic
- A3: all 12 candidates have a usable active counterpart already, so no skill
  capability backfill is required first
- A4: future child topics may use separate worktrees, but this umbrella topic
  only needs its own dedicated worktree to stay valid

## Success Signals

This topic is ready for downstream child-topic planning when:

1. both analysis artifacts exist in the dedicated worktree
2. all 12 candidates are assigned to explicit waves
3. Wave 1 is frozen as the ordered Retrofit spine
4. `python-project-init-greenfield` is frozen as `Wave 1.5`
5. each candidate row includes routing metadata for future child-topic planning
6. no repo-visible edits occur outside the two analysis artifacts
