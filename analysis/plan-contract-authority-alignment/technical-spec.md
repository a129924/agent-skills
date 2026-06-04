# Technical Specification: plan-contract-authority-alignment

**Status**: frozen — ready for plan authoring
**Topic**: `plan-contract-authority-alignment`
**Source baseline**: `analysis/plan-contract-authority-alignment/requirements.md`
**Upstream evidence manifest**: `analysis/plan-contract-authority-alignment/upstream-decision-basis.md`

---

## Baseline Summary

The frozen business baseline requires a governance-only planning topic that
stabilizes planning authority before any canonical convergence work begins.

The implementation-facing translation is:

- define one shared repo-level plan-contract authority surface,
- define explicit source-of-truth ordering for planning artifacts,
- define a human-facing `contract_version` strategy,
- keep `skills/plan-creator/**` and `skills/plan-reviewer/**` read-only by
  default in this topic,
- and encode all convergence, projection, runtime, and platform work as
  deferred follow-up rather than current scope.

This is not a convergence topic. It is a governance baseline topic.

---

## Requirement Traceability

| Requirement | Technical realization | Dependencies | Cost / burden | Status |
| --- | --- | --- | --- | --- |
| R1 repo-visible topic plan exists | Create `plan/plan-contract-authority-alignment/plan-contract-authority-alignment.plan.md` plus required workflow truth artifacts | analysis files, workflow contract | low | feasible |
| R2 shared authority surface is repo-level | Reserve `plan/topic-plan-contract.md` as the future shared contract path and treat it as repo-level governance artifact | workflow contract, accepted human verdict | medium | feasible |
| R3 authority precedence is explicit | Topic plan defines exact source-of-truth ordering among governance, workflow, shared contract, topic plan, and skill-local guidance | `AGENTS.md`, `plan/agent-handoff-workflow.md`, accepted verdict | medium | feasible |
| R4 human-facing `contract_version` exists | Topic plan requires a readable version field in the shared contract and may defer strict hash validation | accepted verdict | low | feasible |
| R5 exact upstream evidence paths are preserved | Create a repo-visible manifest `analysis/plan-contract-authority-alignment/upstream-decision-basis.md` and cite it from the plan | accepted Phase 1 worktree evidence | low | feasible |
| R6 governance-only scope stays bounded | Topic plan forbids convergence, projection, runtime adaptation, and skill moves | accepted Phase 1 verdict and prompt | low | feasible |
| R7 downstream effects stay deferred | Topic plan records `python-blueprint-review` absorption and `copilot-instructions-init` handling as follow-up dependencies only | accepted human verdict | low | feasible |
| R8 writable scope stays exact | Topic plan lists exact writable paths for topic-local planning artifacts and future repo-level governance surfaces only | workflow contract | low | feasible |
| R9 skill-local planning surfaces stay read-only by default | Topic plan treats `skills/plan-creator/**` and `skills/plan-reviewer/**` as evidence surfaces unless later plan repair expands scope | current coupling evidence | medium | feasible |

---

## Required Technical Tasks and Artifacts

### Workstream A - Upstream evidence freeze

Create and preserve exact upstream evidence routing through:

- `analysis/plan-contract-authority-alignment/upstream-decision-basis.md`
- `analysis/plan-contract-authority-alignment/requirements.md`
- `analysis/plan-contract-authority-alignment/technical-spec.md`

This removes dependence on hidden chat context and captures the accepted Phase 1
bundle and human review verdict as explicit planning inputs.

### Workstream B - Shared contract authority definition

The future topic plan should define one shared repo-level contract surface:

- `plan/topic-plan-contract.md`

That surface should govern:

- topic-plan required sections
- authority / precedence ordering for topic-plan contract semantics
- human-facing `contract_version`
- reviewer handoff contract expectations that are repo-level rather than
  skill-local ownership

### Workstream C - Repo workflow alignment

The future topic plan should allow bounded repo-level workflow alignment in:

- `plan/agent-handoff-workflow.md`

Only to the extent required to:

- reference the shared plan contract explicitly,
- distinguish repo-level workflow semantics from repo-level topic-plan contract
  semantics,
- prevent `plan-creator` and `plan-reviewer` from remaining implicit authority
  owners.

### Workstream D - Scope enforcement

The future topic plan must encode exact writable scope:

- topic-local planning artifacts under
  `analysis/plan-contract-authority-alignment/`
  and `plan/plan-contract-authority-alignment/`
- repo-level governance artifacts:
  - `plan/topic-plan-contract.md`
  - `plan/agent-handoff-workflow.md`

The future topic plan must encode exact forbidden scope:

- `skills/**`
- `.github/skills/**`
- `.codex/skills/**`
- `.github/agents/**`
- `.codex/agents/**`
- `README.md`
- `VERSION`
- `.github/copilot-instructions.md`

### Workstream E - Deferred downstream routing

The future topic plan must explicitly defer:

- canonical convergence into `skills/`
- `.codex/skills/` projection materialization
- `.codex/agents/` design or materialization
- `python-blueprint-review` absorption work
- generic convergence for `copilot-instructions-init`

---

## Dependency and Integration Notes

- `AGENTS.md` remains the governance canonical source.
- `plan/agent-handoff-workflow.md` remains the repo-level workflow-phase
  contract and should be updated only in bounded governance scope.
- `plan/topic-plan-contract.md` is the proposed future shared authority surface
  for topic-plan contract rules.
- Topic plans remain topic-specific execution contracts and must comply with the
  two repo-level governance surfaces above.
- `skills/plan-creator/**` and `skills/plan-reviewer/**` remain read-only
  evidence surfaces in this topic unless later plan repair and human approval
  explicitly widen scope.

---

## Cost-of-Realization Assessment

| Workstream | Complexity | Sequencing pressure | Operational / maintenance burden |
| --- | --- | --- | --- |
| Upstream evidence freeze | low | must happen first | very low |
| Shared contract authority definition | medium | core topic outcome | low |
| Repo workflow alignment | medium | depends on authority definition staying narrow | low |
| Scope enforcement | low | must be explicit before creator handoff | very low |
| Deferred downstream routing | low | must be explicit before human review | very low |

Estimated effort is low-to-moderate. The main risk is accidental scope drift
into skill edits or convergence work.

---

## Architecture Compliance Self-Check

| Dimension | Result | Notes |
| --- | --- | --- |
| Governance ownership | fits | `AGENTS.md` remains canonical governance source |
| Workflow authority | fits | `plan/agent-handoff-workflow.md` remains repo-level workflow contract |
| Topic-plan authority | fits with new repo-level artifact | requires introducing `plan/topic-plan-contract.md` |
| Skill-local authority | bounded | skill-local planning surfaces are consumers/evidence only in this topic |
| Convergence boundary | fits | convergence remains deferred |
| Projection/runtime boundary | fits | projection and runtime work remain deferred |

### Compliance notes

- Fit: this topic can remain governance-only if writable scope is limited to
  topic-local planning artifacts plus repo-level planning contracts.
- Mismatch risk: if authority ambiguity cannot be resolved honestly without
  changing `skills/plan-creator/**` or `skills/plan-reviewer/**`, the topic
  must stop for plan repair rather than widening by assumption.

---

## Conflicts, Blockers, and Rollback-to-Alignment Triggers

### Current blockers

None from the current evidence set. This topic is plannable as a bounded
governance baseline.

### Rollback triggers

Return to alignment before implementation proceeds if any of the following
becomes true:

1. the shared authority baseline cannot be stated honestly without direct edits
   to `skills/plan-creator/**` or `skills/plan-reviewer/**`;
2. a reviewer or implementer tries to treat accepted Phase 1 planning inputs as
   permission for convergence or projection work;
3. a required outcome would force edits to `skills/**`, `.github/skills/**`,
   `.codex/skills/**`, `.github/agents/**`, or `.codex/agents/**`;
4. the repo-level shared contract path cannot be fixed exactly.

### Conflict handling note

If later work reveals that bounded skill-local wording updates are necessary,
record that as a follow-up governance topic or explicit plan repair. Do not
silently expand this topic.

---

## Recommended Next Step

Author `plan/plan-contract-authority-alignment/plan-contract-authority-alignment.plan.md`
in strict mode, using these analysis artifacts as prerequisites and encoding
repo-level planning authority, versioning strategy, exact writable scope, and
deferred downstream work as executable contract sections.
