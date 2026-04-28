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
    ├── agent-skill-template/
    ├── git-branch-naming/
    ├── git-commit-convention/
    ├── git-post-merge-workflow/
    ├── git-release-management/
    ├── python-api-signature/
    ├── python-class-design/
    ├── python-control-flow/
    ├── python-error-handling/
    ├── python-model-selection/
    ├── python-module-boundaries/
    ├── python-naming/
    ├── python-testing-pytest/
    └── python-type-hints-strict/
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
- `references/` as an explicit split-reference folder when one `reference.md`
  would become too broad

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
| `references/` | split topic-specific reference files when one reference file is too broad |
| `examples.md` | detailed inputs, outputs, anti-patterns, and patterns |
| `checklist.md` | repeatable verification steps |
| scripts | local automation with one explicit job |
| `assets/` / `templates/` / `fixtures/` | local resources with a fixed role |

Generic catch-all names such as `docs/`, `misc/`, or `helpers/` should not grow
inside a skill folder unless the repository spec gives them a fixed role.

## Example policy
- `SKILL.md` should include one concise positive example and one concise
  negative example
- `examples.md` may stay optional when the concise `SKILL.md` examples already
  cover about 80% of routine usage
- `examples.md` becomes required for higher-complexity skills, such as
  refactoring, branching workflows, script/tool usage, or higher-risk outputs
- reviewer may still require `examples.md` when the concise examples are not
  enough

## Reference policy
- keep `reference.md` focused when one file is enough
- `references/` is a split-reference supplement, not by itself a replacement for
  the required companion-file rule
- split into `references/` when `reference.md` grows beyond about 1,000 tokens
  or more than 3 logical topics
- if `reference.md` is the chosen companion file and becomes too broad, keep it
  focused or reduce it to a short overview while moving detailed topics into
  `references/`
- list each split file and its role in `SKILL.md` → `Local references`

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
7. Prepare and verify the semantic execution branch before creator work starts.
8. In publish flow, stage only the topic's allowed file set; broad staging
   defaults such as `git add -A` or `git add .` are not allowed.
9. At manual merge handoff, stop completely and resume only after a new explicit
   human message.

## Versioning
- The root `VERSION` file is the canonical version baseline for this repository.
- It versions the Agent Skills project itself, not a Python package.
- Versioning follows SemVer:
  - `MAJOR`: breaking repository policy or skill-usage changes
  - `MINOR`: new stable skills or backward-compatible capabilities
  - `PATCH`: non-breaking fixes and wording corrections

## Guides

Process documentation and workflow guidance for repository operations:

| Guide | Purpose |
| --- | --- |
| `MAIN-AGENT-WORKFLOW.md` | canonical agent handoff workflow; defines phases 1-10 for topic planning, creation, review, PR, and post-merge cleanup |
| `COPILOT-CLI-WORKFLOW.md` | practical Copilot CLI operating guide for workflow-gated prompting, reduced repeated context, and when to use `/pr`, `/review`, `/fleet`, and `/tasks` with the repo agent |
| `REFERENCE-INTAKE-PROCESS.md` | lightweight 5-layer process for evaluating, triaging, and adopting ideas from external Agent Skills repositories |
| `OTHER-PROJECT-EXAMPLES.md` | changelog of external ideas adopted into this repository's stable library via the reference intake workflow |

## Current skills
| Skill | Role |
| --- | --- |
| `agent-skill-creator` | creates new repo-compliant skills |
| `agent-skill-reviewer` | checks skills against the repository rules |
| `agent-skill-template` | provides the canonical template and reference shape |
| `git-branch-naming` | names or repairs development branches with semantic prefixes and migration guidance |
| `git-commit-convention` | drafts semantic commit messages from staged changes and recommends split or amend repair paths |
| `git-post-merge-workflow` | standardizes post-merge cleanup and local synchronization, including safe branch deletion defaults and verification checks |
| `git-release-management` | enforces strict PR/release gates, version synchronization, and safe tagging or emergency release handling |
| `plan-creator` | creates repo-visible topic plans with strict workflow, artifact, and stable-library timing contracts |
| `plan-reviewer` | independently reviews repo-visible topic plans before execution, returning structured JSON verdicts against workflow and plan-authoring rules |
| `python-naming` | defines Python naming rules for identifiers, files, folders, and visibility |
| `python-type-hints-strict` | defines Python type-hint rules for projects that require `pyright --strict` |
| `python-model-selection` | defines general Python construct-selection rules for Enum, dataclass, ABC, and Protocol |
| `python-control-flow` | defines general Python control-flow rules for `if/elif`, `match/case`, guard clauses, and truthiness checks |
| `python-testing-pytest` | defines pure Python pytest unit-testing rules for fixtures, parametrization, assertions, mocks, and coverage as a quality target |
| `python-error-handling` | defines general Python exception-handling rules for custom errors, translation boundaries, chaining, propagation, and benign suppression |
| `python-class-design` | defines ordinary Python class-design rules for public surfaces, thin constructors, disciplined instance state, properties, factories, and limited name mangling |
| `python-data-model-methods` | defines general Python data-model method rules for choosing foundational dunder methods, base container protocols, dataclass-generated behavior boundaries, and safe equality/hash semantics |
| `python-api-signature` | defines public Python function and method signature rules for safe defaults, clear parameter ordering, keyword-only clarity, and explicit call-site contracts |
| `python-module-boundaries` | defines regular Python package and module boundary rules for explicit public surfaces, internal-module contracts, import style, and safe import behavior |
| `python-context-management` | defines synchronous Python context-manager rules for resource lifetime, `@contextmanager` versus class-based choice, cleanup-failure handling, ambient-state restoration, and `ExitStack` usage |
| `python-docstrings` | guides contract-first docstring writing in Google Style format with explicit intent derivation, error semantics documentation, and dataclass field-level contracts |
| `python-decorators` | defines ordinary Python decorator rules for when to use decorators, how to preserve signature transparency, and when explicit calls or context managers are clearer |
| `python-async-await` | defines general Python async/await rules for choosing async boundaries, preserving structured concurrency, and handling cancellation, async protocols, and grouped task failure explicitly |
| `python-generators-iterators` | defines general Python generator and iterator rules for choosing concrete collections versus generators, generator functions versus custom iterators, lazy evaluation discipline, and iterator-protocol design |
| `python-project-init-greenfield` | executes Greenfield project initialization from blueprint contracts, including required skill installation, toolchain configuration, structural scaffolding, and acceptance handoff |
| `python-project-retrofit` | retrofits existing Python projects with safe structural conflict detection (Shadow File Detection), implicit configuration discovery (Implicit Config Mining), Git safety checks, and Sensing Delta Report for transparent state transformation |
| `sense-env-scaffold` | scaffolds environmental-constraint check scripts with JSON manifest output |

## Notes
- Use `.github/copilot-instructions.md` for always-on repository guidance.
- Use `.github/skills/<skill-name>/SKILL.md` for task-specific instructions.
