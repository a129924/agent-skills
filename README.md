# agent-skills

This repository uses `skills/` as the primary canonical skill source for
reusable skill behavior.

It also uses `agents/` as the canonical source for repo-defined workflow agent
artifacts.

`.github/**`, `.codex/**`, and other `.<platform>/**` layouts may still exist
as compatibility or projection surfaces for specific tools or platforms.

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
Current repository layout:
AGENTS.md
docs/
skills/                           # current canonical skill source
agents/                           # canonical repo-defined workflow agent artifacts
.github/
├── skills/                      # GitHub/Copilot compatibility surface
└── agents/                      # GitHub/Copilot compatibility surface
```

## Positioning Summary

- `AGENTS.md` is the governance canonical source.
- `skills/` is the primary canonical skill source for reusable skill behavior.
- `agents/` is the canonical source for repo-defined workflow agent artifacts.
- `docs/repo-positioning.md` defines repository positioning and migration
  boundary.
- `.github/copilot-instructions.md` is GitHub/Copilot compatibility guidance
  that defers to canonical governance.
- `.github/**`, `.codex/**`, and other `.<platform>/**` paths are compatibility
  / projection layers, not source of truth.
- the repository does not own runtime loading / execution, registry behavior,
  or fetch / install / sync / deploy orchestration.

## Observer / Dispatcher Baseline

- `agents/observer-dispatcher.agent.md` is a bounded routing-only workflow
  agent artifact.
- It does not make the repository a runtime orchestration system.
- It does not encode existing human-operated workflows.
- When workflow-derived state is needed, only a topic-local artifact such as
  `plan/<topic>/<topic>.step.md` may be used as bounded evidence.

## Historical Migration Snapshot

- As of version `0.77.0`, PR #116 was merged into `dev`, adding the stable
  `skills/step-creator/` skill, which creates one
  caller-selected `base-plan`, `agent-skill-plan`, or
  `python-implementation-plan` `plan/<topic>/<topic>.step.md` from an eligible
  plan with fixed worktree, PR, release, and cleanup gates.
- As of version `0.76.1`, PR #115 merged the
  `creator-reviewer-template-platform-path-alignment` topic into `dev`,
  aligning the stable `agent-skill-creator`, `agent-skill-reviewer`, and
  `agent-skill-template` skill families around canonical-source,
  output-facing `.<platform>/...`, and explicit bootstrap-fallback path
  roles while adding the bounded analysis / plan artifacts for that topic.
- As of version `0.76.0`, PR #114 merged the
  `spec-docs-mvp-generator` topic into `dev`, adding the stable skill
  `skills/spec-docs-mvp-generator/` and the bounded analysis / plan artifacts
  for the `spec-docs-mvp-generator` topic.
- As of version `0.75.0`, PR #112 merged the
  `platform-projection-adapter` topic into `dev`, adding the canonical
  projection skill and CLI under `skills/platform-projection-adapter/` with
  explicit dry-run / apply / force gates, source/target overlap and symlink
  protections, generated-cache filtering, projected `.codex/skills/...`
  standalone entrypoint support, and bounded pytest coverage for both
  canonical and projected execution paths without committing any projection
  outputs.
- As of version `0.74.0`, PR #111 merged the
  `skills-canonical-inventory` topic into `dev`, adding the bounded canonical
  `skills/` inventory builder at `scripts/build_skills_inventory.py`, the
  deterministic `artifacts/skills-inventory.jsonl` snapshot, bounded pytest
  coverage for the inventory contract, and the topic-local analysis / plan
  evidence set while keeping scope limited to top-level canonical `skills/`
  only.
- As of version `0.73.0`, PR #110 merged the
  `codex-skills-canonical-retarget` topic into `dev`, replacing the first-wave
  `.codex/skills/` top-level symlink surface with 11 `.codex`-local
  materialized compatibility entries sourced from canonical `skills/`
  directories, while updating `.codex/skills/README.md`,
  `.codex/skills/provenance.md`, and the topic review trail without modifying
  `skills/**` or `.github/skills/**`.
- This repository contains repo-visible migration artifacts for Codex and
  Copilot compatibility/projection work, including `.codex/skills/`
  projection experiments and multiple topic-local plan/report trails.
- Versions `0.59.0` through `0.69.0` merged several migration-planning and
  bounded-remediation topics back into `dev`, making those artifacts part of
  the main repository history.
- As of version `0.72.0`, PR #106, PR #107, and PR #108 completed the three
  serialized Phase 2 child slices under the approved umbrella baseline, and
  PR #109 merged the `phase-2-umbrella` close-out into `dev`, adding the full
  Phase 2 analysis / plan evidence set while landing the bounded canonical
  convergence and platform-path wording cleanup in canonical `skills/`.
- As of version `0.71.0`, PR #103 and PR #104 merged the
  `agent-skills-convergence-phase-1` reporting bundle and the
  `plan-contract-authority-alignment` governance alignment into `dev`,
  adding the phase-1 / phase-3 convergence evidence set under `docs/` and
  `plan/` while establishing `plan/topic-plan-contract.md` as the shared
  repo-level topic-plan contract surface.
- As of version `0.70.0`, PR #102 merged the
  `observer-dispatcher-canonical-baseline` topic into `dev`, adding the
  bounded `agents/observer-dispatcher.agent.md` contract and three supporting
  skills under `skills/` while keeping `.github/**`, `.codex/**`, and other
  platform-specific paths as compatibility/projection surfaces rather than
  canonical authority.
- As of version `0.69.1`, PR #101 merged the
  `skills-canonical-positioning` topic into `dev`, so `AGENTS.md`,
  `docs/repo-positioning.md`, `.github/copilot-instructions.md`, and
  `README.md` aligned on `skills/` as canonical skill truth while
  platform-specific paths remained compatibility/projection surfaces.
- Some of those topics also materialized or aligned specific skills under
  `skills/`; those historical merges do not make `.github/skills/...` or other
  platform paths canonical.
- Read those migration artifacts as historical background only. Current
  repository truth is defined by `AGENTS.md` and
  `docs/repo-positioning.md`.

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
- `skills/` is the primary canonical skill source for reusable skill behavior
- `agents/` is the canonical source for repo-defined workflow agent artifacts
- `.github/copilot-instructions.md` is GitHub/Copilot compatibility guidance
- `.github/**`, `.codex/**`, and other `.<platform>/...` paths are
  compatibility / projection surfaces
- `README.md` is the human summary

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
2. Keep examples, checklists, and helper files with the skill they belong to,
   and state each local file or folder role clearly.
3. Stop creator work at `review-ready`.
4. Send the draft to `agent-skill-reviewer` through a human or external
   workflow.
5. Promote the skill to the stable library only after it returns `approved`.
6. Prepare and verify the semantic execution branch before creator work starts.
7. In publish flow, stage only the topic's allowed file set; broad staging
   defaults such as `git add -A` or `git add .` are not allowed.
8. At manual merge handoff, stop completely and resume only after a new explicit
   human message.
9. If a platform-specific workflow references `.github/skills/...` or another
   `.<platform>/...` path, treat that path as compatibility or projection
   context rather than repo-wide authority.

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
| `boundary-outcome-design` | guides semantic Outcome and exception design across Domain, Application, Port, Adapter, Repository, and Unit of Work boundaries |
| `copilot-instructions-init` | generates or refreshes target-project `.github/copilot-instructions.md` from sensed facts, installed skills, and plan contracts, with stale-fact and overwrite-choice hard stops |
| `context-package-builder` | builds one minimal handoff package for a real subAgent dispatch, keeping only frozen truth, bounded evidence, and explicit unknowns while excluding whole-chat history, registry hints, and workflow reconstruction |
| `git-branch-naming` | names or repairs development branches with semantic prefixes, `<type>/<username>/<short-description>` structure, and migration guidance |
| `git-commit-convention` | drafts semantic commit messages from staged changes and recommends split or amend repair paths |
| `git-post-merge-workflow` | standardizes post-merge cleanup and local synchronization, including safe branch deletion defaults and verification checks |
| `git-release-management` | enforces strict PR/release gates, version synchronization, and safe tagging or emergency release handling |
| `handoff-routing-policy` | routes the next allowed role after one explicit subAgent result using the frozen verdict set, or stops when bounded routing cannot continue |
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
| `step-creator` | creates one caller-selected `base-plan`, `agent-skill-plan`, or `python-implementation-plan` `plan/<topic>/<topic>.step.md` from an eligible plan with fixed worktree, PR, release, and cleanup gates |
| `subagent-dispatch-policy` | chooses the next allowed role for one bounded task slice, or stops, without turning file paths, registries, or runtime semantics into dispatch targets |
| `worktree-manager` | manages Git worktree lifecycle operations with safe create, get-worktree, release, and remove routing; enforces managed-path policy, release/remove separation, and risky-state escalation |

## Notes
- Use `AGENTS.md` for governance guidance.
- Use `docs/repo-positioning.md` for repository positioning and migration
  boundary.
- For skill-path authority questions, treat `skills/` as canonical truth and
  `.github/skills/...` as a compatibility entrypoint only.
- For workflow-agent authority questions, treat `agents/` as canonical truth
  and `.github/agents/...` as a compatibility entrypoint only.
