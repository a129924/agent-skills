# agent-skills repository instructions

## Agent Preferences

- **Language**: Respond in Traditional Chinese (繁體中文) by default.

This repository is an Agent Skills workbench, not an application codebase or a
Python package.

## Repository goal
- Collect ready-to-use GitHub Agent Skills.
- Create new skills with `agent-skill-creator`.
- Review skills with `agent-skill-reviewer` before treating them as stable.

## Canonical policy owner
The canonical definition of a compliant Skill Folder lives in this file.

Ownership model:
- `.github/copilot-instructions.md` owns the policy
- `README.md` summarizes it for humans
- `agent-skill-template` mirrors it in reusable form
- `agent-skill-creator` applies it during drafting
- `agent-skill-reviewer` enforces it during review

## Always-on rules
- Focus on GitHub Agent Skills only.
- Store project skills under `.github/skills/<skill-name>/`.
- Keep every skill as self-contained and copy-friendly as possible.
- Prefer small, single-purpose skills over broad helper bundles.
- Treat `.github/copilot-instructions.md` as always-on guidance and
  `.github/skills/*/SKILL.md` as task-specific instructions.

## Required skill shape
Each stable skill directory should contain:
- `SKILL.md`
- `examples.md` or `reference.md`
- optional `checklist.md`, scripts, `references/`, or local subfolders only when
  the skill truly needs them

Optional additions are allowed only when their role is explicit and local to the
skill.

## Skill folder responsibility matrix
| Item | Responsibility | Status |
| --- | --- | --- |
| `SKILL.md` | Executable instruction contract for the skill, including concise positive and negative examples | Required |
| `reference.md` | Stable local knowledge, constraints, edge cases, and usage notes | Required or choose `examples.md` |
| `references/` | Split topic-specific reference files when one `reference.md` would become too broad | Optional |
| `examples.md` | Detailed example inputs, outputs, anti-patterns, and usage patterns | Required for high-complexity skills or when `SKILL.md` examples are not enough |
| `checklist.md` | Repeatable verification or operational checklist | Optional |
| scripts | Local automation with one explicit operational job | Optional |
| `assets/` | Static local resources used only by this skill | Optional |
| `templates/` | Reusable local templates used only by this skill | Optional |
| `fixtures/` | Sample local data or payloads used only by this skill | Optional |

Rules for optional items:
- every optional file or folder must map to one clear responsibility
- `Local references` must name the item and say what it is for
- avoid vague catch-all names such as `docs/`, `misc/`, `helpers/`, or `stuff/`
  unless the repository spec later assigns them a fixed role

## Reference policy
- Keep `reference.md` focused when one file is enough.
- `references/` is a split-reference supplement, not by itself a replacement for
  the required companion-file rule.
- If `reference.md` grows beyond about 1,000 tokens or covers more than 3 logical
  topics, split it into topic files under `references/`.
- If `reference.md` is the chosen companion file and becomes too broad, keep it
  focused or reduce it to a short overview while moving detailed topics into
  `references/`.
- When `references/` exists, `SKILL.md` must list each split file in
  `Local references` and state the role of each file.
- Reviewer may still require a split when the file remains too broad even if the
  rough threshold is not exceeded.

Each `SKILL.md` should contain:
- YAML frontmatter with `name` and `description`
- `Purpose`
- `Trigger / When to use`
- `Inputs`
- `Process`
- `Examples`
- `Outputs`
- `Boundaries`
- `Local references`

In `Local references`, name local files or folders and state what each one is for.

## Example policy
- Every `SKILL.md` must include at least one concise correct example and one
  concise incorrect example.
- `examples.md` may stay optional when the concise `SKILL.md` examples already
  cover about 80% of routine usage.
- `examples.md` is required when the skill:
  - handles code refactoring
  - has branching or multi-path decisions
  - depends on scripts or external tools
  - produces higher-risk outputs or larger downstream impact
- Reviewer may still require `examples.md` when the `SKILL.md` examples are not
  enough.

## Quality bar
A skill is only complete when it is:
- single responsibility
- portable
- independent
- explicit about when it should be triggered
- backed by example or reference material in the same folder
- approved by `agent-skill-reviewer`

## Ownership boundaries
- `agent-skill-creator` may draft or revise a skill until it is `review-ready`.
- `agent-skill-reviewer` may return `approved` or `needs-rework`.
- Creator may not approve its own output.
- Reviewer may not author the final implementation directly.
- A human or external workflow owns the handoff between creator and reviewer.

## Naming
- Directory name: lowercase kebab-case
- Skill name in frontmatter: match the directory when possible
- Avoid vague names such as `general-helper` or `do-everything`

## Working style
- Put reusable detail next to the skill that uses it, not in repo-global
  helper files.
- If a new skill overlaps an existing one, narrow or split scope instead of
  broadening the old skill.
- Do not accept a skill into the stable library until the reviewer flow passes.
