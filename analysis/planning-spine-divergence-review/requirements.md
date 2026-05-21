# planning-spine-divergence-review

## Goal

Freeze a remediation-ready divergence review for the planning-spine same-name
pair so later implementation topics do not need to rediscover where the two
surfaces disagree.

## Candidate set

- `plan-creator`
- `plan-reviewer`

## Required outcomes

| ID | Requirement | Acceptance signal |
| --- | --- | --- |
| R1 | The report decomposes divergence into resolution units | Each skill has multiple `difference_area` rows instead of one high-level summary |
| R2 | Each row explains overwrite risk | Every row has `risk_if_force_overwrite` |
| R3 | The report avoids making ungrounded canonical-overwrite decisions | `recommended_authority_now` may remain `unresolved` where risk is high |
| R4 | The report is detailed enough to split a later remediation topic | Every row has `recommended_resolution_unit` and `follow_up_topic` |
| R5 | No skill content edit is performed | All skill folders remain unchanged |

## Fixed difference areas

### plan-creator

- fallback contract source
- reference body expansion
- examples drift
- template support / auxiliary references

### plan-reviewer

- review basis path
- blocked behavior for missing sources/plan
- reference review rules
- examples/checklist drift

## Topic boundaries

### In scope

- evidence-only divergence decomposition for the two planning-spine skills
- risk-aware routing into later bounded remediation

### Out of scope

- any skill content edit
- any overwrite or merge action
- any `.codex/skills` mutation
- any business-intent same-name pair

## Evidence sources

- `docs/migration/same-name-divergence-review.md`
- the two `skills/...` folders
- the two `.github/skills/...` folders
- `.codex/skills/README.md`
- `.codex/skills/provenance.md`

## Stop conditions

- If a new divergence area appears that materially changes workflow behavior,
  record it in the report but do not expand into remediation.
- If any conclusion would require skill edits to prove correctness, stop at
  evidence-only and keep `recommended_authority_now` unresolved.
