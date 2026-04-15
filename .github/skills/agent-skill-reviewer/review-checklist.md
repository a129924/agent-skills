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

## Quality
- the skill has one responsibility
- the trigger is explicit and narrow enough to be useful
- the folder is portable and mostly self-contained
- the skill does not depend on hidden repo-global context
- the skill includes example or reference material in the same folder
- `SKILL.md` includes at least one concise correct example
- `SKILL.md` includes at least one concise incorrect example

## Example depth
- `examples.md` exists when the skill is high complexity
- `examples.md` exists when the concise `SKILL.md` examples are not enough
- detailed examples match the skill's main paths and anti-patterns

## High-complexity triggers
- code refactoring
- branching or multi-path decisions
- script or external-tool usage
- higher-risk outputs or larger downstream impact

## Ownership and lifecycle
- creator stops at `review-ready`
- reviewer returns `approved` or `needs-rework`
- reviewer does not produce the final implementation directly

## Reject signals
- multiple unrelated trigger families
- "do everything" language
- missing required core files
- missing concise positive or negative examples in `SKILL.md`
- missing `examples.md` for a high-complexity skill
- optional additions with no declared role
- vague boundaries
- review comments that would require inventing a different skill
