# agent-skills

This repository is moving toward `skills/` as the canonical skill source.

During transition, `.github/skills/` remains the current Copilot active
authored and reviewed workflow path.

See [docs/repo-positioning.md](docs/repo-positioning.md) for the full current
state, target architecture, and migration boundary.

## What this repository is
This repository is an Agent Skills workbench.
It is not a Python package, app, or DDD codebase.

It is optimized for three equal jobs:
1. keep a portable library of ready-to-use skills
2. create new skills quickly
3. review skills before they join the stable library

## Layout
```text
Current workflow layout:
AGENTS.md
docs/
.github/
└── skills/                      # current Copilot active workflow path

Target architecture after separate migration:
skills/                          # intended canonical skill source
└── ...
```

## Positioning Summary

- `AGENTS.md` is the governance canonical source.
- `skills/` is the intended canonical skill source / target architecture.
- `.github/skills/` remains the current Copilot active authored/reviewed
  workflow path during transition.
- `.<platform>/skills/...` is the future projection / adapter / compatibility
  mirror layer, not source of truth.
- external installer repositories or tools own fetch / install / sync / deploy.

## Current Migration Snapshot

- This repository now contains the spec-worktree validation surface for
  `.codex/skills/` as a projection-only adapter layout.
- Five branch-local migration topics were merged into the repository as
  planning/reporting artifacts:
  - `codex-migration-direct-move`
  - `codex-migration-copilot-residue-low`
  - `codex-migration-copilot-residue-medium`
  - `codex-migration-copilot-residue-high`
  - `codex-migration-copilot-specific`
- The repository now also contains the `codex-readability-baseline` topic as a
  repo-visible first-wave inventory artifact for `move_status`,
  `codex_readability`, same-name pass backlog, and follow-up routing.
- These merged topics do not declare repo-wide active-path cutover. They record
  candidate classification, bounded remediation, and follow-up routing only.
- These artifacts record a transition-planning lane and should not be read as a
  formal release declaration or active-path cutover.
- As of version `0.59.0`, PR #84 merged the codex skills spec-worktree lane
  back into `dev`, so this snapshot now lives on the main repository branch
  rather than on a separate long-lived worktree branch.
- As of version `0.60.0`, PR #85 merged the codex readability baseline back
  into `dev`, so the first-wave Codex readability inventory now also lives on
  the main repository branch rather than on a separate short-lived worktree
  branch.
- As of version `0.61.0`, PR #86 merged the first low-risk move topic back
  into `dev`, so `git-commit-convention` and `git-branch-naming` now also
  exist under `skills/` as target-architecture copies while `.github/skills/`
  remains the transition-era compatibility surface and `.codex/skills`
  projection stays deferred.
- As of version `0.62.0`, PR #87 and PR #88 merged the same-name follow-up
  topics back into `dev`, so the business-intent pair is now explicitly
  canonicalized to `skills/`, while the planning-spine pair now has a
  remediation-ready divergence breakdown that points to the next topic:
  `planning-spine-bounded-remediation`.
- As of version `0.64.0`, PR #89 merged the bounded remediation planning topic
  back into `dev`, so the planning-spine pair now has a partial execution
  contract that isolates three policy-lock units from five support/reference
  units that can be remediated safely in a later execution topic.
- As of version `0.64.0`, PR #90 also merged the workflow recovery alignment
  follow-up, adding repo-visible workflow policy and workflow documents that
  tighten PR-comment correction, topic bootstrap, migration implementation, and
  release-cleanup routing.
- As of version `0.65.0`, PR #91 merged the agent-skill contract-surface move
  back into `dev`, so the creator/reviewer/template surfaces now also exist
  under `skills/` as target-architecture copies while `.github/skills/`
  remains the transition-era compatibility surface and the publish handoff
  workflow is explicitly split from implementation.
- As of version `0.65.0`, PR #92 also merged the `worktree-manager` move back
  into `dev`, so the helper skill now also exists under `skills/` as a
  target-architecture copy while `.github/skills/worktree-manager/` remains the
  transition-era compatibility surface.
- As of version `0.66.0`, PR #94 merged the workflow artifact standardization
  topic back into `dev`, so the repository now contains repo-visible
  `requirements.md`, `plan.md`, and `step.md` baselines for workflow artifacts
  without changing the active skill-path transition boundary.
- As of version `0.67.0`, PR #95 merged the `agent-skill-migration-sequencing`
  topic back into `dev`, so the repository now contains a repo-visible
  next-wave migration sequencing baseline and topic-local publish handoff
  artifacts without authorizing active-path cutover, skill moves, or shared
  workflow edits.
- As of version `0.68.0`, PR #96 merged the planning-spine ready-subset
  remediation back into `dev`, so the support/reference alignment for
  `plan-creator` and `plan-reviewer` now lives under `skills/` while the
  blocked workflow-authority units remain unresolved and the publish handoff
  stops at topic-local `STOP POINT 1`.
- As of version `0.69.0`, PR #100 merged the
  `python-canonicalization-sequencing` topic back into `dev`, so multiple
  existing transition-era skills now also exist under `skills/` as canonical
  copies with repo-visible analysis, plan, and migration-report artifacts,
  while `.github/skills/` remains the transition compatibility and active
  workflow surface and no active-path cutover is declared by this release.

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
- `AGENTS.md` is the governance canonical source
- `skills/` is the intended canonical skill source / target architecture
- `.github/skills/` remains the current Copilot active workflow path during
  transition
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

## Correction / delta lifecycle contract refresh — complete

As of version `0.58.0`, the repository now standardizes correction / delta
lifecycle handling as a repo-level workflow capability instead of leaving the
rules split across ad hoc plan wording.

This release refreshes:

- `plan/agent-handoff-workflow.md` so the workflow body keeps only correction
  lifecycle / routing contract
- `plan-creator` guidance so correction topics must use exact artifact paths,
  explicit parent-sync closure, and clear creator / reviewer ownership
- `plan-reviewer` guidance so review can reject workflow-body schema bloat,
  unconditional review-log rules, vague evidence paths, and repository-wide
  round-cap drift
- `.github/agents/python-implementation-workflow.agent.md` so it stays a
  consumer of the repo-level contract rather than the sole owner of the rule

This release does **not** introduce a new standalone correction skill.
Detailed correction artifact schema and examples now belong in reference /
example surfaces, while future standalone extraction remains a separate topic if
repeated instability or cross-workflow reuse later justifies it.

## Skill schema v2 migration — complete

As of version `0.54.0`, all **50 stable skills** in this library are fully
schema v2 compliant. This statement covers the skill-schema migration only; it
does not mean repository path migration is complete. The skill-schema migration
is considered closed and final.

Skill-schema v2 updates applied across every skill include:

- complexity-gated sections aligned to the canonical `SKILL.md` contract
- risk-appropriate validation signals in `Trigger / When to use` and `Boundaries`
- concise positive and negative examples required in every `SKILL.md`
- `reference.md` or `examples.md` companion file required per skill
- local file roles explicitly declared in `Local references`

The migration covered all seven tiers:

| Tier | Description | Skills |
| --- | --- | --- |
| 1 | Python Planning / Review | 9 |
| 2 | Python Implementation / Code-modification | 5 |
| 3 | Python Helper / Reference | 20 |
| 4 | Git Workflow / Review / Commit | 3 |
| 5 | Git Helper | 1 |
| 6 | Other — high-risk | 5 |
| 7 | Other — low-risk | 2 |
| **Total** | | **50** |

The final deferred-skill closure was completed via PR #63 before this release.
Full skill-schema migration history is tracked in
`files/migration-tracker.md`.

## Guides

Process documentation and workflow guidance for repository operations:

| Guide | Purpose |
| --- | --- |
| `MAIN-AGENT-WORKFLOW.md` | canonical agent handoff workflow; defines phases 1-10 for topic planning, creation, review, PR, and post-merge cleanup |
| `COPILOT-CLI-WORKFLOW.md` | practical Copilot CLI operating guide for workflow-gated prompting, reduced repeated context, and when to use `/pr`, `/review`, `/fleet`, and `/tasks` with the repo agent |
| `REFERENCE-INTAKE-PROCESS.md` | lightweight 5-layer process for evaluating, triaging, and adopting ideas from external Agent Skills repositories |
| `OTHER-PROJECT-EXAMPLES.md` | changelog of external ideas adopted into this repository's stable library via the reference intake workflow |
| `docs/migration/codex-skills-spec-worktree.md` | branch-local spec-worktree validation contract for `.codex/skills/` projection experiments |
| `docs/migration/plan-review-protocol.md` | repeatable planner/reviewer protocol for migration-branch `plan.md` review |

## Current skills
| Skill | Role |
| --- | --- |
| `agent-skill-creator` | creates new repo-compliant, single-purpose skills with complexity classification, risk-appropriate validation, and explicit local-file roles |
| `agent-skill-reviewer` | reviews skills for complexity-gated sections, YAML-body alignment, risk-appropriate validation, severity-labeled findings, and lifecycle compliance |
| `agent-skill-template` | provides the canonical template with complexity-gated sections and risk-based validation guidance |
| `business-intent-alignment` | aligns ambiguous business intent into measurable requirements baselines at `analysis/<topic>/requirements.md` through Socratic questioning, contradiction surfacing, and extreme-boundary checks before technical translation starts |
| `business-to-technical-translation` | translates frozen business baselines into technical specs with feasibility checks, architecture-compliance analysis, cost-of-realization warnings, and rollback-to-alignment triggers |
| `copilot-instructions-init` | generates or refreshes target-project `.github/copilot-instructions.md` from sensed facts, installed skills, and plan contracts, with stale-fact and overwrite-choice hard stops |
| `git-branch-naming` | names or repairs development branches with semantic prefixes, `<type>/<username>/<short-description>` structure, and migration guidance |
| `git-commit-convention` | drafts semantic commit messages from staged changes and recommends split or amend repair paths |
| `git-post-merge-workflow` | standardizes post-merge cleanup and local synchronization, including safe branch deletion defaults and verification checks |
| `git-release-management` | enforces strict PR/release gates, version synchronization, and safe tagging or emergency release handling |
| `plan-creator` | creates repo-visible topic plans with canonical workflow transitions, analysis-layer routing, exact artifact paths, and stable-library timing contracts |
| `plan-reviewer` | independently reviews repo-visible topic plans against workflow contracts and returns fixed-schema JSON verdicts before execution |
| `plan-step-tracker` | queries `pending` / `done` step status in `plan/<topic>/<topic>.step.md`, including implementation-only gate checks, with minimal token cost and explicit blocking when incomplete |
| `python-implementation-workflow` | orchestrates the end-to-end Python implementation workflow with active gates across plan review, TDD assessment, implementation, implementation review, code review, and medium/high-severity drift correction handling |
| `python-naming` | defines Python naming rules for identifiers, files, folders, and visibility |
| `python-package-layout` | defines conservative Python package layout rules for `src/`, `pyproject.toml`, library-vs-CLI placement, packaged data, extras, and tests that exercise installed package structure instead of repo-root import accidents |
| `python-type-hints-strict` | defines Python type-hint rules for projects that require `pyright --strict`, including boundary-only `object` use and preservation of stronger repo-owned types |
| `python-model-selection` | defines general Python construct-selection rules for Enum, dataclass, ABC, and Protocol |
| `python-control-flow` | defines general Python control-flow rules for `if/elif`, `match/case`, guard clauses, and truthiness checks |
| `python-testing-pytest` | defines pure Python pytest unit-testing rules for fixtures, parametrization, assertions, mocks, and coverage as a quality target |
| `python-error-handling` | defines general Python exception-handling rules for custom errors, translation boundaries, chaining, propagation, and benign suppression |
| `python-class-design` | defines ordinary Python class-design rules for public surfaces, thin constructors, disciplined instance state, properties, factories, and limited name mangling |
| `python-comprehensions` | defines Python comprehension readability rules for single-level list/dict/set comprehensions, nested comprehensions, generator expressions, filter/map trade-offs, and when to use explicit loops instead |
| `python-data-model-methods` | defines general Python data-model method rules for choosing foundational dunder methods, base container protocols, dataclass-generated behavior boundaries, and safe equality/hash semantics |
| `python-operator-overloading` | defines Python operator overloading rules for binary arithmetic contracts, reflected operator pairing, in-place return semantics, unary operator purity, comparison ordering consistency, and the NotImplemented dispatch protocol |
| `python-api-signature` | defines public Python function and method signature rules for safe defaults, clear parameter ordering, keyword-only clarity, and explicit call-site contracts |
| `python-module-boundaries` | defines regular Python package and module boundary rules for explicit public surfaces, internal-module contracts, import style, and safe import behavior |
| `python-context-management` | defines synchronous Python context-manager rules for resource lifetime, `@contextmanager` versus class-based choice, cleanup-failure handling, ambient-state restoration, and `ExitStack` usage |
| `python-docstrings` | guides contract-first docstring writing in Google Style format with explicit intent derivation, error semantics documentation, and dataclass field-level contracts |
| `python-decorators` | defines ordinary Python decorator rules for when to use decorators, how to preserve signature transparency, and when explicit calls or context managers are clearer |
| `python-descriptors-attribute-access` | chooses and designs Python attribute access mechanisms using the least-powerful-sufficient ladder — from plain attributes through `@property`, `@cached_property`, custom descriptors, and attribute hook methods — with strict discouragement of `__getattr__`, `__setattr__`, and `__getattribute__` |
| `python-async-await` | defines general Python async/await rules for choosing async boundaries, preserving structured concurrency, and handling cancellation, async protocols, and grouped task failure explicitly |
| `python-async-planning` | defines planning-stage Python async architecture and risk-freezing rules for trigger evidence, lifecycle decisions, contradictions, retrofit handling, and portability boundaries before implementation |
| `python-generators-iterators` | defines general Python generator and iterator rules for choosing concrete collections versus generators, generator functions versus custom iterators, lazy evaluation discipline, and iterator-protocol design |
| `python-library-architecture` | defines clean Python library/package architecture rules for theme isolation, `core` contracts, facade/client composition, and zero-exception cross-theme dependency direction |
| `python-project-init-greenfield` | executes Greenfield project initialization from blueprint contracts, including required skill installation, toolchain configuration, structural scaffolding, and acceptance handoff |
| `python-blueprint-authoring` | authors review-ready greenfield `blueprint.md` contracts with locked section order, exact Required Skills library validation, stop-and-ask handling for abstract structure, and strict greenfield-only lane boundaries |
| `python-blueprint-review` | reviews authored greenfield `blueprint.md` contracts against the locked blueprint v1 schema, exact Required Skills validity, structural locatability, and greenfield-only lane fit before executor handoff |
| `python-project-retrofit` | retrofits existing Python projects with safe structural conflict detection (Shadow File Detection), implicit configuration discovery (Implicit Config Mining), Git safety checks, and Sensing Delta Report for transparent state transformation |
| `python-retrofit-plan-authoring` | authors review-ready Retrofit V2 contracts with locked section order, migration-strategy risk metadata, stop-and-ask handling for abstract plans, and strict separation between planning strategy and runtime gate decisions |
| `python-retrofit-plan-review` | reviews authored Retrofit V2 `retrofit-plan.md` contracts against the locked section order, machine-readable risk metadata, supported sensing assertion kinds, locatability, and retrofit lane fit before executor handoff |
| `python-plan-authoring` | creates an executable Python implementation plan (`*.plan.md`) that freezes scope, decisions, affected files, tests, and validation commands before coding begins — an implementation contract, not a todo list |
| `python-plan-review` | reviews a Python implementation plan against executability criteria, returning `approved`, `needs-rework`, or `insufficient-context` before any coding begins |
| `python-tdd-test-authoring` | creates RED tests from an approved Python implementation plan before implementation begins, enforcing TDD discipline and preventing test-as-afterthought |
| `python-implementation-review` | reviews a Python implementation against its approved plan, verifying all tasks are complete, no scope creep occurred, and no contracts were broken — not a code quality check |
| `python-code-review` | reviews Python code quality across 7 dimensions (typing, lint, readability, error handling, anti-patterns, test quality, observability) with tool auto-detection and ordering gate after implementation-review |
| `python-serialization-boundaries` | defines Python serialization boundaries as semantic translation gates for API, database, and message payloads, including missing/null intent preservation, type normalization, deep conversion, and asymmetric input/output contracts |
| `python-pre-commit` | configures pre-commit hooks for uv-based Python projects by producing a valid `.pre-commit-config.yaml` with the canonical hook set (ruff, ruff-format, pre-commit-hooks); keeps slow hooks (pytest, pyright) on `manual` stage; includes `scripts/apply_precommit.py` for automated template-based config generation |
| `python-pyproject-toolconfig` | appends missing ruff, pyright, and pytest configuration sections to an existing pyproject.toml without overwriting existing settings |
| `sense-env-scaffold` | runs the `sense_env.py` scaffold to discover environment facts or evaluate sensing assertions with JSON manifest output and defined exit codes |
| `worktree-manager` | manages Git worktree lifecycle operations with safe create, get-worktree, release, and remove routing; enforces managed-path policy, release/remove separation, and risky-state escalation |

## Notes
- Use `AGENTS.md` for governance guidance.
- Use `docs/repo-positioning.md` for repository positioning and migration
  boundary.
- Use `.github/skills/<skill-name>/SKILL.md` for task-specific instructions.
