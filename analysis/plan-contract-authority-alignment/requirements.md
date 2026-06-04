# Requirements: plan-contract-authority-alignment

## Status

- **Status**: frozen for technical translation
- **Topic**: `plan-contract-authority-alignment`
- **Date**: 2026-06-04
- **Scope**: governance-only planning baseline for shared repo-level
  plan-contract authority alignment

## Problem Statement

The repository now has an accepted Phase 1 evidence baseline, but planning
authority is still split across:

- `plan/agent-handoff-workflow.md`
- `skills/plan-creator/**`
- `skills/plan-reviewer/**`

The accepted human decision is that `plan-creator` and `plan-reviewer`
authority must move to one shared repo-level plan contract, but that contract
does not exist yet as a frozen topic baseline.

The missing outcome for this topic is not convergence implementation. The
missing outcome is a repo-visible topic plan that defines:

1. what shared repo-level plan contract authority should govern,
2. what source-of-truth order planning surfaces must follow,
3. how the shared contract should expose versioning,
4. what remains deferred to later convergence and projection topics.

## Evidence Read

The baseline uses the following evidence:

- `AGENTS.md`
- `docs/repo-positioning.md`
- `plan/agent-handoff-workflow.md`
- `skills/plan-creator/SKILL.md`
- `skills/plan-creator/reference.md`
- `skills/plan-creator/checklist.md`
- `skills/plan-creator/templates/topic-plan-template.md`
- `skills/plan-reviewer/SKILL.md`
- `skills/plan-reviewer/reference.md`
- `skills/plan-reviewer/checklist.md`
- `analysis/plan-contract-authority-alignment/upstream-decision-basis.md`

## Actors

| Actor | Role | What must be true after this topic |
| --- | --- | --- |
| Repository maintainer | Owns planning governance | Can point to one repo-level plan-contract authority surface without relying on either planning skill as the owner |
| Planning actor | Authors future topic plans | Can determine authority order without guessing between workflow spec and skill-local contract text |
| Reviewer | Reviews topic plans | Can validate plans against repo-level authority rather than cross-skill coupling |
| Future convergence topic owner | Depends on stable governance baseline | Can treat this topic as prerequisite governance input without widening it into convergence implementation |
| Human operator | Approves scope boundaries | Can see exactly what this topic does not authorize |

## Frozen Requirements

| ID | Requirement | Acceptance signal |
| --- | --- | --- |
| R1 | This topic must produce a repo-visible topic plan for a governance-only authority-alignment topic. | `plan/plan-contract-authority-alignment/plan-contract-authority-alignment.plan.md` exists and is review-ready. |
| R2 | The future shared authority surface for topic-plan contract rules must be defined as a repo-level artifact rather than a skill-local owner. | The eventual topic plan names an exact repo-level shared contract path and does not assign ownership of that authority to `skills/plan-creator/**` or `skills/plan-reviewer/**`. |
| R3 | Planning authority precedence must be explicit. | Another agent can read the eventual plan and identify the authority order among `AGENTS.md`, `plan/agent-handoff-workflow.md`, the shared repo-level plan contract, topic plans, and skill-local planning guidance. |
| R4 | The shared plan contract must expose a human-facing `contract_version` strategy. | The eventual plan requires versioning language that is repo-local and human-readable rather than hidden in tool-only metadata. |
| R5 | This topic must preserve the accepted Phase 1 decision basis using exact upstream evidence paths. | The eventual plan lists exact upstream evidence paths or an exact repo-visible manifest that contains them. |
| R6 | This topic must remain governance / contract alignment only. | The eventual plan explicitly excludes canonical convergence, projection materialization, runtime adaptation, and direct skill-library migration. |
| R7 | `python-blueprint-review` absorption and `copilot-instructions-init` handling must remain deferred downstream consequences rather than current-topic implementation work. | The eventual plan records them as deferred follow-up only and does not add them to current writable scope. |
| R8 | The next topic's writable scope must stay exact and bounded. | The eventual plan names exact writable paths and blocks any unlisted skill or projection path. |
| R9 | Direct edits to `skills/plan-creator/**` and `skills/plan-reviewer/**` must not be assumed as part of this topic's default scope. | The eventual plan treats those skill surfaces as read-only evidence unless a later explicit plan repair and human approval say otherwise. |

## Resolved Contradictions

### C1 - Planning authority must move, but this topic must not become convergence work

- Conflict: the repo needs authority alignment now, but the accepted Phase 1
  verdict explicitly forbids widening into convergence or projection work.
- Resolution: this topic is frozen as governance / contract alignment only and
  records all convergence work as deferred follow-up.

### C2 - The planning skills are involved, but they must not own the shared contract

- Conflict: `plan-creator` and `plan-reviewer` currently contain planning
  contract material, but the accepted human decision says the shared authority
  must not live inside either skill.
- Resolution: the future authority surface must be repo-level, while the skill
  folders are treated as consumers or evidence only in this topic.

### C3 - Phase 1 is accepted, but it is not an approved implementation spec

- Conflict: accepted Phase 1 planning inputs could be misread as permission to
  start convergence work immediately.
- Resolution: this topic must explicitly record that Phase 1 outputs are
  decision inputs only.

## Explicit Assumptions

- A1: `AGENTS.md` remains the governance canonical source during this topic.
- A2: `plan/agent-handoff-workflow.md` remains the repo-level workflow-phase
  contract during this topic.
- A3: the shared plan-contract authority surface can be introduced as a new
  repo-level artifact without requiring immediate skill-local adoption in the
  same topic.
- A4: future skill-local wording alignment, if still needed, can be deferred to
  a later bounded topic after the shared repo-level contract exists.

## Non-goals

- Do not implement canonical convergence.
- Do not implement projection materialization.
- Do not implement runtime adaptation.
- Do not migrate skill libraries between `skills/`, `.github/skills/`, and
  `.codex/skills/`.
- Do not absorb `python-blueprint-review` into `skills/` in this topic.
- Do not perform generic convergence for `copilot-instructions-init`.
- Do not treat accepted Phase 1 planning inputs as an approved implementation
  spec.

## Extreme-Boundary Checks

| Boundary | Requirement result |
| --- | --- |
| A planner reads only `skills/plan-creator/**` | The eventual topic plan must still make clear that skill-local material is not the ultimate authority owner |
| A reviewer reads only `skills/plan-reviewer/**` | The eventual topic plan must still make clear that review basis authority comes from repo-level governance, not cross-skill coupling |
| A later agent sees accepted Phase 1 inputs | The eventual topic plan must still block direct convergence or projection work |
| A future implementation attempt needs skill-local wording changes | The topic must stop and repair the plan rather than silently widening writable scope |

## Success Signals

This topic is frozen successfully when:

1. the accepted Phase 1 evidence basis is captured in exact paths,
2. the future shared plan-contract authority surface is defined as repo-level,
3. authority precedence is explicit,
4. versioning expectations are explicit,
5. deferred work is named explicitly, and
6. no downstream implementer needs to guess whether convergence or skill
   migration is authorized.
