# codex-migration-runway requirements baseline

Status: FROZEN
Topic: `codex-migration-runway`
Primary execution branch: `feat/andrew/copilot-to-codex-migration`

## Problem statement

This repository needs a global planning baseline for a Codex migration runway.
The current task is not the migration itself. The repository needs a bounded,
repo-visible runway that lets one Setup Agent define the frozen global contract
and lets later Bounded Implement Agents execute one phase at a time without
guessing scope, source of truth, or branch rules.

## Global goal

This topic exists to establish the migration runway only.

- The goal is to create a minimal viable global planning baseline for
  `copilot-to-codex-migration`.
- This topic does **not** perform the full migration.

## Primary actors

- Primary actor: Setup Agent
- Secondary actor: Bounded Implement Agent
- Control actor: Human decision-maker

## Planning spine

The runway planning spine MUST explicitly anchor on these two existing skills:

- `.github/skills/business-intent-alignment`
- `.github/skills/business-to-technical-translation`

They are first-class planning inputs, not optional side references.

## In-scope outcomes

- Create `analysis/codex-migration-runway/requirements.md`
- Create `analysis/codex-migration-runway/technical-spec.md`
- Create `plan/positioning-freeze/positioning-freeze.plan.md`
- Freeze the runway-level operating model for:
  - Global Goal
  - observer / planner operating model
  - planning spine
  - Big Feature Branch rules
  - implementer handoff contract
- Prepare execution context for the first bounded phase: `positioning-freeze`

## Non-goals

- Full Copilot-to-Codex migration
- External installer repository work
- Adding `.codex/` or `.claude/`
- Generator, renderer, or installer scripts
- Full `.github/skills/` to `skills/` migration
- Declaring `skills/` as the current active workflow path
- Authoring `platform-coupling-inventory.plan.md`
- Authoring `skill-authoring-path-transition`
- Mixing inventory, promotion, or release work into this runway baseline

## Locked repository assumptions

- `AGENTS.md` remains the governance canonical source.
- `docs/repo-positioning.md` remains the positioning authority for current
  state, target architecture, and migration boundary.
- `.github/skills/` remains the current Copilot active authored and reviewed
  workflow path during transition.
- `skills/` is the intended canonical skill source and target architecture, but
  this runway must not declare it active today.
- This runway may prepare later migration work, but must not silently perform
  that migration.
- Human override for artifact topology: the runway analysis topic is
  `codex-migration-runway`, while the first executable phase plan is
  `positioning-freeze`. This split is intentional for this runway and does not
  imply that the first plan owns a separate analysis layer.

## Measurable requirements

| ID | Actor | Condition | Observable result | Metric / decision rule | Failure meaning |
| --- | --- | --- | --- | --- | --- |
| R1 | Setup Agent | The runway baseline is authored | The artifacts explicitly state that this topic creates a runway only and does not do the full migration | PASS only if all three artifacts repeat the runway-only boundary without contradictory wording | Later agents may treat the baseline as authorization for unbounded migration |
| R2 | Setup Agent | The global planning model is frozen | The artifacts define Setup Agent vs Bounded Implement Agent roles with explicit scope boundaries | PASS only if Setup Agent owns baseline / phase planning / handoff contract, and Bounded Implement Agent owns exactly one phase without self-expanding scope | Implementers may re-plan the migration during execution |
| R3 | Setup Agent | Planning authority is documented | The artifacts elevate `.github/skills/business-intent-alignment` and `.github/skills/business-to-technical-translation` as the planning spine | PASS only if both skills are named as spine inputs, not optional background references | Later planning may drift into chat-only intuition |
| R4 | Setup Agent | Source-of-truth order is frozen | The runway artifacts define artifact authority ordering plus handoff prompt fields | PASS only if authority order includes `plan/<topic>/<topic>.plan.md`, `analysis/<topic>/technical-spec.md`, `analysis/<topic>/requirements.md`, and handoff prompt fields for worktree / allowed paths / stop conditions | Implementers may privilege hidden chat context over repo-visible contracts |
| R5 | Setup Agent | Branch and worktree rules are defined | The runway artifacts define the Big Feature Branch model and forbid direct merge to `dev` from phase branches | PASS only if `feat/andrew/copilot-to-codex-migration` is named as the main line, phase work merges back there first, and `dev` is kept clean | Phase work may bypass the runway and pollute `dev` |
| R6 | Setup Agent | The first bounded phase is prepared | `plan/positioning-freeze/positioning-freeze.plan.md` exists and is executable as a single-phase contract | PASS only if the plan freezes repo positioning only, distinguishes current state / target architecture / migration boundary, and forbids migration work | The first implementer may widen into path transition or contract edits |
| R7 | Setup Agent | `positioning-freeze` boundaries are frozen | The plan forbids creator / reviewer / template contract changes and forbids `.github/skills/*` contract edits | PASS only if these prohibitions are explicit and repeated in boundaries and acceptance checks | The first phase may accidentally rewrite adjacent systems |
| R8 | Setup Agent | Current-state wording is preserved | The artifacts do not declare `skills/` to be the current active path | PASS only if `.github/skills/` remains the current active authored/reviewed path during transition in all relevant wording | The baseline would contradict existing governance documents |
| R9 | Setup Agent | Implementer handoff is actionable | The runway artifacts define required handoff fields for worktree path, branch, allowed paths, locked decisions, and stop conditions | PASS only if a later implementer could execute the phase without inferring those values from memory | Execution may drift because the contract is underspecified |
| R10 | Setup Agent + Human | Contradictions or unresolved policy gaps exist | The artifacts surface them explicitly instead of smoothing them over | PASS only if any unresolved governance ambiguity is written into artifacts as a gap or decision point | Hidden contradictions may reappear during implementation |

## Operating model requirements

- Setup Agent owns the global baseline, phase sequencing, and implementer
  handoff contract.
- Bounded Implement Agent owns one phase at a time, modifies only authorized
  paths, and must stop instead of broadening scope.
- The observer / planner role remains above implementation and validates
  alignment against repo-visible artifacts before any scope expansion.
- Repo-visible artifacts outrank hidden chat memory.

## Big Feature Branch requirements

- Main runway branch: `feat/andrew/copilot-to-codex-migration`
- Phase branches merge back into the Big Feature Branch first
- Phase branches do not merge directly into `dev`
- `dev` should remain clean during runway execution

## First-phase requirements: positioning-freeze

The first phase must only freeze repository positioning.

It MUST:

- distinguish current operating state, target architecture, and migration
  boundary
- preserve the current statement that `.github/skills/` remains the active
  Copilot authored/reviewed path during transition
- preserve the statement that `skills/` is target architecture, not current
  active path

It MUST NOT:

- perform migration
- touch creator / reviewer / template contract content
- touch `.github/skills/*` skill contract content
- declare `skills/` already active
- author adjacent phase plans

## Resolved contradictions

1. **Runway vs migration**
   - Conflict: the branch name suggests migration work, but this task is only
     baseline planning
   - Resolution: the branch may host the runway, but the artifacts must state
     explicitly that only runway planning is authorized now
2. **Target architecture vs current operating state**
   - Conflict: `skills/` is the intended canonical source, but `.github/skills/`
     remains the active workflow path today
   - Resolution: the baseline must freeze both statements together and forbid
     language that collapses them into one state
3. **Phase execution vs global authority**
   - Conflict: implementers need autonomy to execute, but must not rediscover
     policy
   - Resolution: the handoff contract must name authority order, allowed paths,
     and stop conditions explicitly
4. **Single-topic spine convention vs human-requested split topology**
   - Conflict: normal repo planning prefers one topic spine, but this runway was
     explicitly requested as umbrella analysis plus one first-phase plan
   - Resolution: treat `analysis/codex-migration-runway/*` as the runway-level
     authority and `plan/positioning-freeze/positioning-freeze.plan.md` as the
     first bounded phase contract by explicit human override

## Extreme-boundary checks

- an implementer attempts to author a second phase plan during
  `positioning-freeze`
- a phase branch targets `dev` directly
- a phase changes `.github/skills/*` contract files because they look related
- a phase implies that `skills/` is already the current active path
- a phase mixes inventory or promotion work into the positioning freeze
- handoff instructions omit allowed paths or stop conditions

## Freeze decision

This baseline is ready for technical translation.
