# Planning-Spine Divergence Review

## Branch

- `feat/andrew/planning-spine-divergence-review`

## Topic result

- Branch-local execution mode: evidence-only planning-spine review
- Candidate set reviewed: 2
- Skill content edit performed: no
- `.codex/skills` projection change performed: no

## Divergence decision table

| skill | difference_area | current_skills_behavior | current_github_skills_behavior | risk_if_force_overwrite | recommended_resolution_unit | recommended_authority_now | follow_up_topic |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `plan-creator` | `fallback contract source` | Fallback stays local to `references/required-section-meaning.md` | Fallback points to repo-level `folder-contract.md` | Overwriting either side changes what the authoring contract treats as the last-resort schema source. | `fallback-contract-alignment` | `unresolved` | `planning-spine-bounded-remediation` |
| `plan-creator` | `reference body expansion` | Narrower reference body focused on stable local rules | Expanded reference body adds correction-lifecycle and future-extraction guidance | Force-overwrite may silently adopt or drop policy that affects correction-plan authoring expectations. | `reference-body-alignment` | `unresolved` | `planning-spine-bounded-remediation` |
| `plan-creator` | `examples drift` | Examples reflect the `skills/` contract set | Examples include newer correction-lifecycle patterns and extended cases | Force-overwrite may misalign examples with the active contract source and mis-teach plan authors. | `examples-reconciliation` | `unresolved` | `planning-spine-bounded-remediation` |
| `plan-creator` | `template support / auxiliary references` | Local support stays bounded to the narrower `skills/` reference set | Auxiliary guidance expands through additional reference expectations in `.github/skills/` | Force-overwrite may create hidden coupling between template use and guidance not present on the other surface. | `template-support-alignment` | `unresolved` | `planning-spine-bounded-remediation` |
| `plan-reviewer` | `review basis path` | Reviews against `skills/plan-creator/...` | Reviews against `.github/skills/plan-creator/...` | Force-overwrite changes which authoring contract is treated as canonical during plan review. | `review-basis-alignment` | `unresolved` | `planning-spine-bounded-remediation` |
| `plan-reviewer` | `blocked behavior for missing sources/plan` | Returns `needs-rework` JSON when sources or target plan are missing | Stops before issuing a verdict when critical sources are missing | Force-overwrite changes whether downstream automation receives a machine-readable failure or a hard stop. | `blocked-behavior-alignment` | `unresolved` | `planning-spine-bounded-remediation` |
| `plan-reviewer` | `reference review rules` | Narrower reference rules aligned to the `skills/` planning surface | Expanded reference rules add correction-lifecycle-specific review expectations | Force-overwrite may change what counts as a blocking issue in plan review. | `reference-rule-alignment` | `unresolved` | `planning-spine-bounded-remediation` |
| `plan-reviewer` | `examples/checklist drift` | Examples and checklist reflect the narrower `skills/` contract | Examples and checklist reflect the broader `.github/skills/` review expectations | Force-overwrite may misalign reviewer guidance, checklist expectations, and actual verdict behavior. | `review-example-checklist-alignment` | `unresolved` | `planning-spine-bounded-remediation` |

## Why this topic does not recommend direct overwrite

- Both skills are planning-spine surfaces, so even a seemingly local overwrite
  changes downstream plan authoring or review behavior.
- The current `skills/` and `.github/skills/` versions disagree on contract
  source, blocked behavior, and reference guidance rather than only on prose.
- This topic relies on previously established repo evidence for `.codex/skills`
  routing and does not independently prove current projection authority.
- Even if existing repo evidence points at `skills/`-backed readability,
  projection state alone is not enough to settle overwrite authority for
  planning-spine workflow contracts.

## Routing conclusion

- No row is safe for immediate force-overwrite in this topic.
- The next appropriate implementation lane is:
  - `planning-spine-bounded-remediation`
- That later topic should consume this report row-by-row instead of reopening
  high-level same-name discovery.

## Deferred items

- Any edit to `skills/plan-creator/`
- Any edit to `.github/skills/plan-creator/`
- Any edit to `skills/plan-reviewer/`
- Any edit to `.github/skills/plan-reviewer/`
- Any `.codex/skills` projection or provenance change
