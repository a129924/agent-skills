# planning-spine-bounded-remediation

## Goal

Freeze a bounded remediation contract for the planning-spine same-name pair so a
later Implement Agent can align the safely decidable drift now and stop cleanly
on the units that still require human policy lock.

## Candidate set

- `plan-creator`
- `plan-reviewer`

## Fixed remediation units

### plan-creator

- `fallback-contract-source`
- `reference-body-expansion`
- `examples-drift`
- `template-support-and-auxiliary-references`

### plan-reviewer

- `review-basis-path`
- `blocked-behavior-for-missing-sources-or-plan`
- `reference-review-rules`
- `examples-and-checklist-drift`

## Classification rule

Each remediation unit must be classified as exactly one of:

- `implementation-ready`
- `explicitly-blocked`

### implementation-ready

A unit may be marked `implementation-ready` only when current repo-visible
evidence is sufficient to lock all of the following without later guesswork:

- a temporary implementation source
- a target resolution:
  - `adopt skills/`
  - `adopt .github/skills/`
  - `synthesize merged contract`
- exact editable files
- exact untouched files
- validation that proves post-remediation alignment

### explicitly-blocked

A unit must be marked `explicitly-blocked` when current repo-visible evidence is
not enough to lock the remediation safely. A blocked unit must record:

- why it is unsafe to proceed now
- what missing policy or evidence is still required
- the exact file set implicated by the blocked decision

## Executability classification rule

The topic must be classified as exactly one of:

- `fully executable now`
  - only if all eight remediation units are `implementation-ready`
- `partially executable`
  - if any remediation unit is `explicitly-blocked`

If the topic is `partially executable`, the plan must explicitly identify:

- the bounded execution subset that may proceed now
- the blocked units that are out of execution scope
- the exact reason each blocked unit cannot safely proceed

## Locked evidence interpretation

- The prior divergence review is the routing baseline, not the only evidence.
- The four in-scope skill folders must be inspected directly before classifying
  any remediation unit.
- Readability from `.codex/skills` is only supporting evidence that the
  `skills/` surface is usable; it is not by itself authority to force-overwrite
  planning-spine contracts.
- The current topic is planning-only and must not perform remediation edits.

## Required outcomes

| ID | Requirement | Acceptance signal |
| --- | --- | --- |
| R1 | All eight remediation units are classified exactly once | No unit is missing, duplicated, or given mixed status |
| R2 | Every `implementation-ready` unit has locked file-level execution data for a partial support-material subset only | Each ready unit has source, target resolution, exact editable files, exact untouched files, and validation, and none of the ready units requires resolving `SKILL.md`-owned authority drift |
| R3 | Every blocked unit names the missing decision or evidence and carries the implicated `SKILL.md` file set when authority drift is involved | Each blocked unit has a concrete policy/evidence gap instead of vague caution, and blocked workflow-authority units explicitly surface the relevant `skills/.../SKILL.md` and `.github/skills/.../SKILL.md` implications |
| R4 | The plan leaves no hidden decision to the Implement Agent | The bounded execution subset is explicit, blocked units are out of scope, and the plan does not imply whole-skill planning-spine alignment while `SKILL.md`-owned authority drift remains blocked |
| R5 | The topic remains planning-only | No skill surface, `.codex/skills`, README, VERSION, or tag action is authorized here |

## Expected classification baseline

The current evidence is strong enough to expect this topic to be
`partially executable`.

Expected `implementation-ready` candidates:

- `plan-creator/reference-body-expansion`
- `plan-creator/examples-drift`
- `plan-creator/template-support-and-auxiliary-references`
- `plan-reviewer/reference-review-rules`
- `plan-reviewer/examples-and-checklist-drift`

These ready candidates are limited to support/reference surfaces only. They do
not resolve or override any `SKILL.md`-owned workflow-authority drift.

Expected `explicitly-blocked` candidates:

- `plan-creator/fallback-contract-source`
- `plan-reviewer/review-basis-path`
- `plan-reviewer/blocked-behavior-for-missing-sources-or-plan`

These blocked candidates must carry the corresponding `SKILL.md` implications
forward so a later Implement Agent cannot treat the remaining authority drift
as already aligned.

These expectations are planning hypotheses only. The plan must still verify
them against the direct file inspection results.

## Topic boundaries

### In scope

- planning-only remediation classification for the two planning-spine skills
- file-level bounded execution contract for the support/reference units that are
  safe now
- explicit isolation of the units that still need policy lock

### Out of scope

- any remediation edit to `skills/plan-creator/`
- any remediation edit to `.github/skills/plan-creator/`
- any remediation edit to `skills/plan-reviewer/`
- any remediation edit to `.github/skills/plan-reviewer/`
- any attempt to treat `SKILL.md`-owned authority drift as part of the ready
  execution subset
- any `.codex/skills` mutation
- any business same-name topic
- any README, VERSION, tag, release, or governance rewrite

## Stop conditions

- If direct inspection shows a hidden divergence area outside the fixed eight
  units, record it as a blocker and do not widen the topic.
- If a supposedly ready unit requires choosing canonical workflow authority
  beyond current repo-visible evidence, reclassify it as blocked.
- If a unit would require editing a file not explicitly listed in the later
  plan, keep it blocked rather than using a broad directory allowance.
