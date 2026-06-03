# Technical Specification: skills-canonical-positioning

**Status**: frozen — ready for plan authoring
**Topic**: `skills-canonical-positioning`
**Source baseline**: `analysis/skills-canonical-positioning/requirements.md`

---

## Baseline Summary

The frozen business baseline requires a positioning-only correction for four
core files:

- `AGENTS.md`
- `docs/repo-positioning.md`
- `.github/copilot-instructions.md`
- `README.md`

The implementation-facing translation is:

- restate `skills/` as current canonical truth,
- demote Copilot/platform surfaces to compatibility guidance,
- keep `.github/skills/**`, `.codex/skills/**`, and `skills/**` untouched in
  this topic,
- and stop if execution tries to widen into contract migration or workflow
  repair.

This is a wording and authority-order topic. It does not move directories,
update skill bundles, or change runtime/tooling behavior.

---

## Requirement Traceability

| Requirement | Technical realization | Dependencies | Cost / burden | Status |
| --- | --- | --- | --- | --- |
| R1 `AGENTS.md` declares current truth | Rewrite `Skill source model` and `Topic boundary` so `skills/` is current truth and the topic is positioning-only | `AGENTS.md` current wording | low | feasible |
| R2 `docs/repo-positioning.md` defines one current model | Remove target-only split language and present a single current authority model | `docs/repo-positioning.md` current sections | medium | feasible |
| R3 `.github/copilot-instructions.md` becomes bounded compatibility guidance | Rewrite ownership and always-on wording so the file clearly defers repo truth elsewhere | `.github/copilot-instructions.md` current wording | medium | feasible |
| R4 `README.md` matches the same model | Update summary, layout description, and migration snapshot framing | `README.md` current wording | medium | feasible |
| R5 Editable scope stays bounded | Topic plan lists exactly four editable files | analysis artifacts and topic plan | low | feasible |
| R6 Platform/skill paths remain untouched | Topic plan declares `.github/skills/**`, `.codex/skills/**`, and `skills/**` as forbidden scope | analysis artifacts and topic plan | low | feasible |
| R7 No contract/runtime expansion | Topic plan and validation checks block workflow-guide, contract, and tooling drift | analysis artifacts and topic plan | low | feasible |

---

## Required Technical Tasks and Artifacts

### Workstream A - Governance truth correction

Update `AGENTS.md` and `docs/repo-positioning.md` so both files express the
same current-truth model:

- `skills/` is the current canonical skill source
- platform-specific surfaces are compatibility/projection only
- this topic is positioning-only and does not authorize broader migration

### Workstream B - Copilot compatibility-surface correction

Update `.github/copilot-instructions.md` so it:

- identifies itself as GitHub/Copilot compatibility guidance
- defers authority to `AGENTS.md` and `docs/repo-positioning.md`
- stops implying repo-wide policy ownership

### Workstream C - Human-facing summary correction

Update `README.md` so it:

- summarizes `skills/` as current canonical truth
- presents `.github/skills/...` and other `.<platform>/...` paths as
  compatibility surfaces
- keeps historical migration notes as history rather than current authority

### Workstream D - Scope enforcement in the plan

The topic plan must carry executable scope controls:

- **Editable paths**:
  - `AGENTS.md`
  - `docs/repo-positioning.md`
  - `.github/copilot-instructions.md`
  - `README.md`
- **Forbidden paths**:
  - `.github/skills/**`
  - `.codex/skills/**`
  - `skills/**`
  - `.github/guides/MAIN-AGENT-WORKFLOW.md`
  - any `agent-skill-*`
  - runtime/tooling/install/sync/projection automation surfaces

---

## Dependency and Integration Notes

- `AGENTS.md` remains the governance canonical source.
- `docs/repo-positioning.md` remains the positioning contract.
- `.github/copilot-instructions.md` remains present, but only as compatibility
  guidance.
- `README.md` remains the human summary and must not contradict the governance
  files.
- No other file becomes editable because of this topic.

---

## Cost-of-Realization Assessment

| Workstream | Complexity | Sequencing pressure | Operational / maintenance burden |
| --- | --- | --- | --- |
| Governance truth correction | low-to-medium | must land first to anchor the other two files | low |
| Copilot compatibility-surface correction | medium | depends on authority wording being stable | low |
| Human-facing summary correction | medium | depends on the same authority model | low |
| Scope enforcement in the plan | low | must be explicit before implementation handoff | very low |

Estimated effort is low-to-moderate. The main risk is accidental scope drift,
not code or tooling complexity.

---

## Architecture Compliance Self-Check

| Dimension | Result | Notes |
| --- | --- | --- |
| Repository positioning | fits | Topic directly corrects positioning wording |
| Governance ownership | fits | `AGENTS.md` remains canonical |
| Canonical skill source | fits | `skills/` is asserted as current truth |
| Platform-surface role | fits | Platform paths remain compatibility-only |
| Runtime / tooling scope | fits | No runtime/tooling change is introduced |
| Contract migration scope | bounded | Skill/workflow contracts remain forbidden scope |

### Compliance notes

- Fit: this topic can be completed entirely within the four core files.
- Fit: the user explicitly froze `.github/skills/**` and `.codex/skills/**` as
  non-editable for this topic.
- Mismatch risk: if any later implementer tries to "fix consistency" by editing
  skill bundles or workflow guides, that is plan drift, not required work.

---

## Conflicts, Blockers, and Rollback-to-Alignment Triggers

### Current blockers

None from the current evidence set. The topic is implementable as a bounded
four-file positioning correction.

### Rollback triggers

Return to alignment before implementation proceeds if any of the following
becomes true:

1. a required outcome cannot be achieved without editing `.github/skills/**`,
   `.codex/skills/**`, or `skills/**`;
2. a reviewer insists that workflow-guide or contract migration is part of the
   same topic;
3. runtime/tooling/install behavior must change to keep the new wording honest;
4. the four-file scope cannot express a truthful authority model without adding
   new editable files.

### Conflict handling note

If downstream review finds inconsistency outside the four editable files, record
it as follow-up only. Do not silently widen this topic.

---

## Recommended Next Step

Author `plan/skills-canonical-positioning/skills-canonical-positioning.plan.md`
in strict mode, using these analysis artifacts as prerequisites and encoding
both editable scope and forbidden scope as executable contract sections.
