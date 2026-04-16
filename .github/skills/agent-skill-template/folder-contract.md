# Skill folder contract

This document mirrors the canonical repository policy in
`.github/copilot-instructions.md`.

## Required core
- `SKILL.md`: the executable instruction contract for the skill
- `reference.md` or `examples.md`: local detail, examples, or edge cases needed
  to use the skill well

## Optional additions
- `checklist.md`: repeatable verification or operation steps
- scripts: local automation used by this skill
- `references/`: split topic-specific reference files when one `reference.md`
  would become too broad
- local subfolders such as `assets/`: fixtures, templates, or resources used only
  by this skill

## Responsibility matrix
- `SKILL.md`: executable instruction contract with concise positive and negative examples
- `reference.md`: stable local knowledge, constraints, and edge cases
- `references/`: topic-specific reference files with one clear role per file
- `examples.md`: detailed inputs, outputs, anti-patterns, and usage patterns
- `checklist.md`: repeatable verification steps
- scripts: one explicit local automation job
- `assets/`, `templates/`, `fixtures/`: local-only supporting resources with a
  fixed role

## Example policy
- `SKILL.md` must contain one concise correct example and one concise incorrect example
- `examples.md` may stay optional when the concise `SKILL.md` examples already cover about 80% of routine usage
- `examples.md` is required for:
  - code refactoring
  - branching or multi-path decisions
  - script or external-tool usage
  - higher-risk outputs
- reviewer may still require `examples.md` when the concise examples are not enough

## Reference policy
- keep `reference.md` focused when one file is enough
- `references/` is a split-reference supplement, not by itself a replacement for
  the required companion-file rule
- split into `references/` when `reference.md` grows beyond about 1,000 tokens
  or more than 3 logical topics
- if `reference.md` is the chosen companion file and becomes too broad, keep it
  focused or reduce it to a short overview while moving detailed topics into
  `references/`
- list each split file in `Local references` and state its role

## Role declaration rule
- every optional file or folder must have one clear job
- list local files and folders in `Local references`
- state what each local file or folder is for
- reviewer should reject optional additions with no declared role
- avoid vague catch-all names such as `docs/`, `misc/`, or `helpers/`

## Lifecycle note
- creator stops at `review-ready`
- reviewer returns `approved` or `needs-rework`
