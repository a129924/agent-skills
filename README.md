# agent-skills

A personal-first GitHub repository for collecting, creating, and reviewing
reusable Agent Skills.

## What this repository is
This repository is an Agent Skills workbench.
It is not a Python package, app, or DDD codebase.

It is optimized for three equal jobs:
1. keep a portable library of ready-to-use skills
2. create new skills quickly
3. review skills before they join the stable library

## Layout
```text
.github/
├── copilot-instructions.md
└── skills/
    ├── agent-skill-creator/
    ├── agent-skill-reviewer/
    └── agent-skill-template/
```

## Repository rules
Every stable skill should:
- solve one job
- stay self-contained and copy-friendly
- declare an explicit `Trigger / When to use` section
- include concise positive and negative examples in `SKILL.md`
- include example or reference material in the same folder
- pass the reviewer flow before it is treated as complete

Each skill folder uses:
- a required core: `SKILL.md` plus `reference.md` or `examples.md`
- optional additions only when each file or folder has a clear declared role

## Canonical ownership
- `.github/copilot-instructions.md` is the canonical source for the compliant
  Skill Folder definition
- `README.md` is the human summary
- `agent-skill-template` mirrors the structure
- `agent-skill-creator` applies the structure
- `agent-skill-reviewer` enforces the structure

## Responsibility matrix
| Item | Responsibility |
| --- | --- |
| `SKILL.md` | executable instruction contract with concise positive/negative examples |
| `reference.md` | stable local reference knowledge |
| `examples.md` | detailed inputs, outputs, anti-patterns, and patterns |
| `checklist.md` | repeatable verification steps |
| scripts | local automation with one explicit job |
| `assets/` / `templates/` / `fixtures/` | local resources with a fixed role |

Generic catch-all names such as `docs/`, `misc/`, or `helpers/` should not grow
inside a skill folder unless the repository spec gives them a fixed role.

## Example policy
- `SKILL.md` should include one concise positive example and one concise
  negative example
- `examples.md` becomes required for higher-complexity skills, such as
  refactoring, branching workflows, script/tool usage, or higher-risk outputs
- reviewer may still require `examples.md` when the concise examples are not
  enough

## Lifecycle
1. `draft` — still being shaped
2. `review-ready` — creator finished the structural minimum
3. `approved` — reviewer passed the skill
4. `needs-rework` — reviewer rejected it with blocking issues

## Ownership
- `agent-skill-creator` may create or revise a skill until it is `review-ready`.
- `agent-skill-reviewer` may approve or reject it.
- creator may not self-approve.
- reviewer may not generate the final implementation directly.
- human or external workflow moves the handoff between them.

## Workflow
1. Start from `agent-skill-creator` or `agent-skill-template`.
2. Draft the new skill in `.github/skills/<skill-name>/`.
3. Keep examples, checklists, and helper files inside the same folder and state
   each local file or folder role clearly.
4. Stop creator work at `review-ready`.
5. Send the draft to `agent-skill-reviewer` through a human or external
   workflow.
6. Promote the skill to the stable library only after it returns `approved`.

## Versioning
- The root `VERSION` file is the canonical version baseline for this repository.
- It versions the Agent Skills project itself, not a Python package.
- Versioning follows SemVer:
  - `MAJOR`: breaking repository policy or skill-usage changes
  - `MINOR`: new stable skills or backward-compatible capabilities
  - `PATCH`: non-breaking fixes and wording corrections

## Current skills
| Skill | Role |
| --- | --- |
| `agent-skill-creator` | creates new repo-compliant skills |
| `agent-skill-reviewer` | checks skills against the repository rules |
| `agent-skill-template` | provides the canonical template and reference shape |
| `python-naming` | defines Python naming rules for identifiers, files, folders, and visibility |
| `python-type-hints-strict` | defines Python type-hint rules for projects that require `pyright --strict` |
| `python-model-selection` | defines general Python construct-selection rules for Enum, dataclass, ABC, and Protocol |
| `python-control-flow` | defines general Python control-flow rules for `if/elif`, `match/case`, guard clauses, and truthiness checks |

## Notes
- Use `.github/copilot-instructions.md` for always-on repository guidance.
- Use `.github/skills/<skill-name>/SKILL.md` for task-specific instructions.
