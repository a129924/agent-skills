# Technical Specification: agent-skills-convergence-phase-1

**Status**: frozen — ready for plan authoring
**Topic**: `agent-skills-convergence-phase-1`
**Source baseline**: `analysis/agent-skills-convergence-phase-1/requirements.md`

---

## Baseline Summary

The frozen business baseline requires one bounded Phase 1 topic that:

- creates 9 Phase 1 report files under
  `docs/agent-skills-convergence/phase-1/`,
- inventories and compares `skills/`, `.github/skills/`, and `.codex/skills/`
  as observed surfaces,
- classifies drift and runtime dependency evidence conservatively,
- encodes subAgent evidence contracts into the execution workflow, and
- stops before any skill-surface convergence, projection materialization, or
  runtime adaptation.

The implementation-facing translation is documentation and evidence work only.
No skill content, scripts, hooks, templates, tests, or agent files may be
modified by this topic.

---

## Requirement Traceability

| Requirement | Technical realization | Dependencies | Cost / burden | Status |
| --- | --- | --- | --- | --- |
| R1 9 required files | Create `docs/agent-skills-convergence/phase-1/00-summary.md` through `08-phase-3-inputs.md` with consistent wording: `9 Phase 1 files` or `1 summary + 8 analysis reports` | Topic plan, report templates, repository inventory evidence | medium | feasible |
| R2 full inventory | Enumerate detectable skill identities across `skills/`, `.github/skills/`, and `.codex/skills/` and write presence matrix plus file-set comparison evidence | read-only repo scan | medium | feasible |
| R3 conservative drift classification | Apply explicit difference-level rules and route uncertain cases to `human_review_required` | file-content and structure comparison evidence | medium | feasible |
| R4 projection/compatibility posture | Treat `.github/skills/` and `.codex/skills/` as evaluated non-canonical surfaces unless evidence requires escalation | governance docs, repo-positioning evidence, actual directory state | low | feasible |
| R5 read-only skill protection | Constrain all writes to planning artifacts and later `docs/agent-skills-convergence/phase-1/` only | topic plan, git verification | low | feasible |
| R6 explicit stop rules | Encode stop rules in analysis, plan, and report requirements so no downstream agent can claim implicit convergence authority | workflow artifacts and report text | low | feasible |
| R7 Phase 2 inputs | Produce bounded canonical-convergence candidate recommendations centered on later `skills/` truth | inventory + drift outputs | low | feasible |
| R8 Phase 3 inputs | Produce bounded projection/runtime-adaptation candidate recommendations | runtime dependency inventory + `.codex/skills` evidence | low | feasible |
| R9 subAgent evidence contract | Freeze required subAgent output fields and owner/scope discipline in the topic plan and step artifact | user-provided workflow contract | low | feasible |

---

## Required Technical Tasks and Artifacts

### Workstream A - Analysis and workflow freeze

Create and freeze:

- `analysis/agent-skills-convergence-phase-1/requirements.md`
- `analysis/agent-skills-convergence-phase-1/technical-spec.md`

These files must lock:

- read-only scope for skill surfaces,
- the 9 required Phase 1 report files,
- governance target direction toward later `skills/` canonicalization,
- and the conservative evidence threshold for drift, alias, and runtime-mode
  classification.

### Workstream B - Topic planning artifacts

Create topic-local planning artifacts:

- `plan/agent-skills-convergence-phase-1/agent-skills-convergence-phase-1.plan.md`
- `plan/agent-skills-convergence-phase-1/agent-skills-convergence-phase-1.step.md`

The plan must:

- follow `plan/agent-handoff-workflow.md`,
- list exact artifact paths,
- encode the read-only boundary for skill surfaces,
- define subAgent roles and evidence contracts,
- and route final implementation only to
  `docs/agent-skills-convergence/phase-1/`.

### Workstream C - Phase 1 report materialization

Create exactly these report artifacts:

- `docs/agent-skills-convergence/phase-1/00-summary.md`
- `docs/agent-skills-convergence/phase-1/01-skill-inventory.md`
- `docs/agent-skills-convergence/phase-1/02-path-comparison.md`
- `docs/agent-skills-convergence/phase-1/03-copilot-only-classification.md`
- `docs/agent-skills-convergence/phase-1/04-semantic-drift-report.md`
- `docs/agent-skills-convergence/phase-1/05-runtime-dependency-inventory.md`
- `docs/agent-skills-convergence/phase-1/06-convergence-candidates.md`
- `docs/agent-skills-convergence/phase-1/07-phase-2-inputs.md`
- `docs/agent-skills-convergence/phase-1/08-phase-3-inputs.md`

No additional convergence artifact may be substituted for these paths.

### Workstream D - Evidence and review gating

Require repo-visible evidence and gate artifacts for:

- Explorer evidence collection
- Implementer report generation
- Reviewer verification
- Final gate readiness

At minimum, the plan must preserve:

- bounded scope per subAgent,
- explicit files read / modified,
- evidence-tied findings,
- unresolved items,
- and status values from the locked contract.

---

## Dependency and Integration Notes

- `AGENTS.md` is the governance canonical source.
- `docs/repo-positioning.md` states that `skills/` is the current canonical
  source of truth and that platform surfaces are compatibility/projection only.
- `.codex/skills/README.md` and `.codex/skills/provenance.md` are read-only
  projection/provenance evidence, not editable skill sources in this topic.
- Existing topics such as `skills-canonical-positioning` and
  `codex-readability-baseline` provide contextual evidence but do not satisfy
  this topic's required report set.
- The worktree workflow is required before implementation and must remain
  external to the repository root.

---

## Cost-of-Realization Assessment

| Workstream | Complexity | Sequencing pressure | Operational / maintenance burden |
| --- | --- | --- | --- |
| Analysis and workflow freeze | low-to-medium | must complete before topic plan authoring | low |
| Topic planning artifacts | medium | must complete before report implementation | low |
| Report materialization | medium-to-high | depends on inventory and classification evidence | medium |
| Review and final gate | medium | depends on report completeness and evidence traceability | low |

The main burden is comparison and classification discipline, not code or
runtime complexity.

---

## Architecture Compliance Self-Check

| Dimension | Result | Notes |
| --- | --- | --- |
| Repository positioning | fits | Topic treats `skills/` target direction as governance context without enforcing convergence in Phase 1 |
| Governance ownership | fits | `AGENTS.md` and `docs/repo-positioning.md` stay authoritative |
| Workflow compliance | fits | Topic creates analysis, plan, step, review, and final-gate inputs before report implementation |
| Skill-surface protection | fits | `skills/**`, `.github/skills/**`, and `.codex/skills/**` stay read-only |
| Runtime/tooling scope | fits | No projection, sync, or adaptation logic is implemented |
| Evidence rigor | fits with caution | Some semantic or alias cases may require `human_review_required` rather than full automation |

### Compliance notes

- Fit: the topic can be executed as documentation and evidence work only.
- Fit: the user explicitly supplied subAgent interface contracts and stop rules.
- Mismatch risk: if implementation pressure expands into skill edits or path
  fixes, that is plan drift and must stop.

---

## Conflicts, Blockers, and Rollback-to-Alignment Triggers

### Current blockers

None from the current evidence set for planning and report authoring.

### Rollback triggers

Return to alignment before implementation proceeds if any of the following
becomes true:

1. a required report cannot be produced without editing `skills/**`,
   `.github/skills/**`, or `.codex/skills/**`;
2. a classification requires guessing rather than evidence and cannot be safely
   expressed as `human_review_required`;
3. the worktree or topic plan would need to widen into projection creation,
   runtime adaptation, or canonical convergence execution;
4. the required 9-file output contract is changed without explicit human
   direction.

### Conflict handling note

If existing migration or positioning documents disagree with current observed
skill-surface state, record the disagreement as evidence. Do not repair the
underlying skill or projection surface in this topic.

---

## Recommended Next Step

Author `plan/agent-skills-convergence-phase-1/agent-skills-convergence-phase-1.plan.md`
and `plan/agent-skills-convergence-phase-1/agent-skills-convergence-phase-1.step.md`
in strict mode, using these analysis artifacts as prerequisites and encoding
the 9-file report set, read-only scope, stop rules, and subAgent evidence
contracts as executable workflow truth.
