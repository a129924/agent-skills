# same-name-direct-canonicalize

## Goal

Freeze the canonical-authority decision for the two same-name business skills
 that are already content-equivalent across `skills/` and `.github/skills/`.

## Candidate set

- `business-intent-alignment`
- `business-to-technical-translation`

## Required outcomes

| ID | Requirement | Acceptance signal |
| --- | --- | --- |
| R1 | Both candidates are recorded as equivalent | The report states `file_set_match: yes` and `content_status: equivalent` for both rows |
| R2 | Canonical authority is explicitly assigned to `skills/` | Both rows state `canonical authority = skills/` |
| R3 | `.github/skills/` is retained as compatibility only | The report states transition-era compatibility role without claiming active-path cutover |
| R4 | No skill content merge or overwrite is performed | No files under `skills/` or `.github/skills/` are edited |
| R5 | No projection mutation is performed | `.codex/skills` symlinks, README, and provenance stay unchanged |

## Topic boundaries

### In scope

- repo-visible decision artifacts for the two locked candidates
- read-only evidence from the existing same-name divergence review and live
  projection state

### Out of scope

- any skill content edit
- any `.codex/skills` change
- any repo-wide governance wording change
- any planning-spine candidate

## Evidence sources

- `docs/migration/same-name-divergence-review.md`
- `docs/migration/codex-readability-baseline.md`
- `.codex/skills/README.md`
- `.codex/skills/provenance.md`

## Stop conditions

- If either candidate shows any hidden content diff, stop and reclassify the
  topic into bounded remediation instead of direct canonicalization.
- If the authority decision would require editing skill content or projection
  state, stop and re-plan.
