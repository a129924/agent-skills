# Reviewer checklist

A skill is `approved` only if all of these are true:

## Required core
- `SKILL.md` exists
- `reference.md` or `examples.md` exists

## Structure
- `SKILL.md` has `name` and `description` frontmatter
- `SKILL.md` includes `Purpose`
- `SKILL.md` includes `Trigger / When to use`
- `SKILL.md` includes `Inputs`
- `SKILL.md` includes `Process`
- `SKILL.md` includes `Examples`
- `SKILL.md` includes `Outputs`
- `SKILL.md` includes `Boundaries`
- `SKILL.md` includes `Local references`
- local references name local files or folders and state what each one is for

## Optional additions
- each optional file or folder has a clear local job
- optional additions stay local to the skill
- optional additions are justified by the skill's scope
- optional additions follow the responsibility matrix
- generic catch-all names such as `docs/`, `misc/`, or `helpers/` are rejected
  unless the repository spec gives them a fixed role
- each file inside `references/` has a clear topic and role

## Quality
- the skill has one responsibility
- the trigger is explicit and narrow enough to be useful
- the folder is portable and mostly self-contained
- the skill does not depend on hidden repo-global context
- the skill includes example or reference material in the same folder
- `SKILL.md` includes at least one concise correct example
- `SKILL.md` includes at least one concise incorrect example

## Example depth
- `examples.md` may stay optional when the concise `SKILL.md` examples already cover about 80% of routine usage
- `examples.md` exists when the skill is high complexity
- `examples.md` exists when the concise `SKILL.md` examples are not enough
- detailed examples match the skill's main paths and anti-patterns

## Risk-based validation fit
- validation weight matches the skill's risk, branching, external-tool usage, and
  downstream impact
- lightweight skills are not burdened with heavyweight validation that does not
  improve real misuse prevention
- higher-risk or gatekeeping skills include stronger validation signals or
  equivalent local guidance
- stronger validation may appear as explicit verification guidance, red flags,
  rationalizations, a checklist, or another clearly declared local mechanism
- when ambiguity would materially change the output, the draft tells the agent to
  stop and ask instead of silently guessing

## Reference depth
- `reference.md` stays focused when one file is enough
- `references/` supplements split reference detail and does not replace the required companion-file rule
- split into `references/` when local reference detail grows beyond about 1,000 tokens
- split into `references/` when local reference detail covers more than 3 logical topics
- each split reference file is listed in `Local references` with its role

## High-complexity triggers
- code refactoring
- branching or multi-path decisions
- script or external-tool usage
- higher-risk outputs or larger downstream impact

## Ownership and lifecycle
- creator stops at `review-ready`
- reviewer returns `approved` or `needs-rework`
- reviewer does not produce the final implementation directly

## Topic plan alignment
- locked `Artifact paths` are valid and align with the actual output locations
- repo-visible artifacts are not mixed with session-only or local-only artifacts
- path drift is sent back for plan repair instead of being silently tolerated
- when a topic plan locks creator/reviewer-first rollout, downstream regular skills
  must remain untouched in that topic
- scope drift from a creator/reviewer-first topic into downstream regular-skill
  rollout returns `needs-rework`

## Reviewer independence
- Reviewer is a **separate agent** (SubAgent in VS Code; `/fleet` in CLI)
  - Must not inherit creator's session context or assumptions
  - Must apply checklist objectively
- Reviewer outputs: `approved` or `needs-rework` only
  - Includes explicit reasoning and blocking issues (if `needs-rework`)
- Creator may patch PR after reviewer approves (Phase 7)
  - Direct-apply fixes only (style, typo, meta, formatting)
  - Reviewer does NOT re-check these patches
  - Major changes require reviewer to re-evaluate

## Stable library metadata (if applicable)
When the skill is intended for the stable library, review-checklist.md must verify:
- Topic plan includes `Stable library metadata` section
- README row format is complete and matches repo table schema
- README row positioned correctly (alphabetical order or policy-defined position)
- VERSION bump direction is specified and justified
- VERSION direction aligns with commit semantics (MINOR for new skill, PATCH for correction)
- timing for README / VERSION actions is declared explicitly
- if timing is `release`, the topic plan also declares a release action that will
  execute Phase 10

## Reject signals
- multiple unrelated trigger families
- "do everything" language
- missing required core files
- missing concise positive or negative examples in `SKILL.md`
- missing `examples.md` for a high-complexity skill
- missing stronger validation for a higher-risk or gatekeeping skill
- scope drift into downstream regular-skill rollout when the topic plan locks a
  creator/reviewer-first phase
- oversized multi-topic `reference.md` left unsplit
- split reference files missing role labels in `Local references`
- optional additions with no declared role
- vague boundaries
- review comments that would require inventing a different skill
