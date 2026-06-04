# Requirements: agent-skills-convergence-phase-1

## Status

- **Status**: frozen for technical translation
- **Topic**: `agent-skills-convergence-phase-1`
- **Date**: 2026-06-03
- **Scope**: Phase 1 inventory, drift analysis, runtime dependency assessment, and report generation only

## Problem Statement

The repository currently presents multiple skill-related surfaces:

- `skills/`
- `.github/skills/`
- `.codex/skills/`

The missing outcome is a repo-visible, evidence-backed Phase 1 baseline that:

1. inventories the actual state of those surfaces,
2. classifies drift and runtime dependency risk without modifying skill content,
3. prepares bounded inputs for later convergence and projection work, and
4. preserves a clear stop boundary before any canonicalization, projection, or runtime adaptation begins.

Phase 1 must not silently convert governance intent into implementation. The
current governance target is that later phases should make `skills/` the
canonical skill source of truth, but this phase only gathers evidence and must
not enforce that target.

## Evidence Read

The baseline uses the following repo-visible evidence:

- `AGENTS.md`
- `docs/repo-positioning.md`
- `.codex/skills/README.md`
- `.codex/skills/provenance.md`
- `.github/prompts/create-analysis.prompt.md`
- `.github/prompts/create-agent-plan.prompt.md`
- `plan/agent-handoff-workflow.md`
- `plan/skills-canonical-positioning/skills-canonical-positioning.plan.md`
- `plan/codex-readability-baseline/codex-readability-baseline.plan.md`

## Actors

| Actor | Role | What must be true after this topic |
| --- | --- | --- |
| Human reviewer | Approves whether Phase 1 evidence is sufficient before convergence work | Can inspect one bounded report set and see exactly what was observed, what was inferred, and what remains uncertain |
| Main Agent | Orchestrates bounded subAgent work and preserves workflow stop rules | Can point to repo-visible analysis, plan, and Phase 1 report paths instead of hidden chat decisions |
| Explorer subAgent | Gathers read-only evidence | Returns evidence, not conclusions without support |
| Implementer subAgent | Materializes Phase 1 reports only under `docs/agent-skills-convergence/phase-1/` | Does not touch skill source surfaces |
| Reviewer / final gate subAgents | Validate evidence sufficiency, classification consistency, and scope compliance | Can reject unsupported classifications and missing coverage from repo-visible artifacts |

## Frozen Requirements

| ID | Requirement | Acceptance signal |
| --- | --- | --- |
| R1 | Phase 1 must create exactly 9 Phase 1 files under `docs/agent-skills-convergence/phase-1/`: 1 summary plus 8 analysis reports. | Another agent can enumerate the directory and find `00-summary.md` through `08-phase-3-inputs.md` with no missing file. |
| R2 | Phase 1 must inventory all detectable skills across `skills/`, `.github/skills/`, and `.codex/skills/` using evidence rather than assumptions. | `01-skill-inventory.md` lists every detected skill identity and presence by surface. |
| R3 | Phase 1 must classify textual, semantic, and behavior drift conservatively and record uncertainty as `human_review_required` when evidence is insufficient. | No drift classification relies only on directory location or guesswork. |
| R4 | Phase 1 must treat `.github/skills/` and `.codex/skills/` as projection, compatibility, provenance, or platform-adapter surfaces unless evidence proves otherwise or human review is required. | Reports do not treat those surfaces as canonical by default. |
| R5 | Phase 1 must not modify existing skill content or runtime/tooling surfaces. | The only repo changes outside planning artifacts are the 9 report files under `docs/agent-skills-convergence/phase-1/`. |
| R6 | Phase 1 must explicitly preserve stop rules against convergence behavior. | Plan and reports state that no copy, move, delete, rename, overwrite, normalize, reformat, projection creation, or alias auto-resolution occurs in this phase. |
| R7 | Phase 1 must produce concrete Phase 2 inputs for canonical convergence around `skills/` without selecting or enforcing canonical status in this phase. | `07-phase-2-inputs.md` lists candidates, risks, and blockers, and repeats that Phase 1 does not decide canonical truth by execution. |
| R8 | Phase 1 must produce concrete Phase 3 inputs for projection and runtime adaptation without implementing them. | `08-phase-3-inputs.md` lists projection candidates, path rewrite needs, adapter needs, and no implementation work. |
| R9 | Phase 1 must use evidence-based subAgent handoffs. | Repo-visible planning artifacts require subAgent outputs to include evidence, bounded scope, modified files, uncertainty, and status. |

## Resolved Contradictions

### C1 - Governance target versus Phase 1 authority

- Conflict: repository governance already points toward `skills/` as canonical
  truth, but Phase 1 is defined as evidence-only.
- Resolution: Phase 1 records the target direction as later-phase intent while
  forbidding current-phase enforcement or content convergence.

### C2 - `.codex/skills/` listed as inspected surface versus current materialized state

- Conflict: the requested inspection set includes `.codex/skills/`, but current
  repo evidence shows it may operate as projection/provenance documentation
  rather than a fully materialized third skill tree.
- Resolution: Phase 1 must inspect it, but reports must describe its actual
  observed state instead of assuming parity with the other two surfaces.

### C3 - Broad comparison goals versus conservative evidence threshold

- Conflict: the user wants semantic and behavior drift classification across
  many skills, but some cases may not be provable from file text alone.
- Resolution: uncertain classifications are preserved as
  `human_review_required` rather than flattened into overconfident labels.

## Explicit Assumptions

- A1: The intended topic output is documentation and planning artifacts only.
- A2: Later phases may use `skills/` as the intended canonical target, but
  Phase 1 must not perform that convergence.
- A3: A missing or non-materialized `.codex/skills/<skill-name>/` path is still
  meaningful evidence and must be reported as observed state, not repaired.
- A4: Existing migration and positioning topics provide context, but do not
  replace this Phase 1 topic because they do not deliver the required 9-file
  report set for full skill-surface inventory and drift assessment.

## Non-Goals

- copying skill content between `skills/` and `.github/skills/`
- deleting, renaming, normalizing, or reformatting any existing skill file
- creating `.codex/skills/<skill-name>/`
- creating `.codex/agents/` or `.github/agents/`
- modifying scripts, hooks, templates, tests, or agent files
- implementing convergence, projection, runtime adaptation, or sync tooling
- resolving alias candidates automatically

## Extreme-Boundary Checks

| Boundary | Requirement result |
| --- | --- |
| `skills/` and `.github/skills/` disagree materially for a skill | Phase 1 must classify the disagreement and preserve evidence without rewriting either side |
| `.codex/skills/` has metadata but no materialized skill directories | Phase 1 must record that exact state rather than fabricating third-surface parity |
| Alias evidence is plausible but not provable | The item must be marked `human_review_required` |
| A script or path reference suggests runtime coupling | The skill must be classified at least for runtime dependency review, not silently treated as portable |
| A reviewer later disputes a classification | The repo-visible evidence trail must make the dispute inspectable without hidden chat context |

## Success Signals

This topic is frozen successfully when:

1. the Phase 1 report scope is fixed to the 9 required files,
2. read-only and stop-rule boundaries are explicit,
3. later convergence intent toward `skills/` is documented without present-phase
   enforcement,
4. subAgent evidence contracts are part of the execution baseline, and
5. downstream plan authoring can proceed without guessing scope, write set, or
   classification posture.
