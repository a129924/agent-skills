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
| `docs/process/wsl-native-pre-commit-validation.md` | run pre-commit for a Windows linked worktree commit from WSL-native Git metadata |

## Current skills
| Skill | Role |
| --- | --- |
| `agent-skill-creator` | Draft a new single-purpose repository skill for independent review; not for small edits to an existing skill. |
| `agent-skill-reviewer` | Independently approve or request rework on a new or materially changed repository skill. |
| `agent-skill-template` | Supply the repository scaffold when creating a new single-purpose skill manually. |
| `business-intent-alignment` | Resolve ambiguous business intent into measurable requirements before technical planning. |
| `business-to-technical-translation` | Translate a frozen business baseline into a technical specification; surface feasibility conflicts. |
| `boundary-outcome-design` | Design or review Outcome and exception translation when results cross application, domain, or persistence boundaries. |
| `copilot-instructions-init` | Create or refresh a project's Copilot instructions from current repository facts and declared contracts. |
| `context-package-builder` | Build a minimal context package for one already-bounded, real subagent handoff. |
| `git-branch-naming` | Choose a semantic development branch name or repair work started on the wrong branch. |
| `git-commit-convention` | Draft or review semantic commits, topic splits, and message-only amends; also answer commit-policy questions. |
| `git-post-merge-workflow` | Inspect and perform authorized cleanup and fast-forward sync after a PR has merged. |
| `git-release-management` | Assess draft-PR, merge, or release readiness using endpoint-specific gates; tagging needs release authorization. |
| `handoff-routing-policy` | Choose the next allowed role or stop after one explicit subagent result. |
| `plan-creator` | Author a repository topic plan with explicit scope, artifacts, workflow gates, and handoff criteria. |
| `plan-reviewer` | Independently review an authored repository topic plan before execution. |
| `plan-step-tracker` | Query topic step status or check completion; reject invalid completion evidence. |
| `python-implementation-workflow` | orchestrates the end-to-end Python implementation workflow with active gates across plan review, TDD assessment, implementation, implementation review, code review, and medium/high-severity drift correction handling |
| `python-naming` | Define or review Python identifier, file, and visibility naming conventions. |
| `python-package-layout` | Design or review Python src-layout, packaging, CLI placement, and tests that exercise installed code. |
| `python-type-hints-strict` | Design or review annotations for Python projects that explicitly require Pyright strict mode. |
| `python-model-selection` | Choose Enum, dataclass, ABC, or Protocol for Python structured data and contracts. |
| `python-control-flow` | Design or review Python branching, guard clauses, match/case, and truthiness choices. |
| `python-testing-pytest` | Design or review pure pytest unit tests, fixtures, assertions, and mocks without real I/O or async-runner configuration. |
| `python-error-handling` | Design or review Python exception types, translation, chaining, and propagation; not retry orchestration or logging policy. |
| `python-class-design` | Design or review ordinary Python classes, instance state, constructors, and public member placement. |
| `python-comprehensions` | Choose comprehensions, explicit loops, or map/filter when Python collection transformation needs readability review. |
| `python-data-model-methods` | Choose Python foundational dunder methods and container protocols; distinguish dataclass-generated behavior. |
| `python-operator-overloading` | Design Python arithmetic, reflected, in-place, unary, or ordering operators and NotImplemented dispatch. |
| `python-api-signature` | Design or review Python function signatures, defaults, parameter ordering, and call-site contracts. |
| `python-module-boundaries` | Design or review Python module boundaries, public exports, import behavior, and internal contracts. |
| `python-context-management` | Design synchronous with-blocks and context managers for resource cleanup or temporary state restoration. |
| `python-docstrings` | Write or review contract-first Python docstrings in Google Style. |
| `python-decorators` | Design transparent function decorators and decorator factories; not class decorators or hidden resource lifetimes. |
| `python-descriptors-attribute-access` | Choose Python properties, descriptors, or attribute hooks; require justification for dynamic interception. |
| `python-async-await` | Design or review Python async boundaries, task ownership, cancellation, and async protocols. |
| `python-async-planning` | Freeze async lifecycle, concurrency, failure, and cancellation decisions before risky Python implementation. |
| `python-generators-iterators` | Choose collections versus lazy Python iteration and design generators or custom iterators. |
| `python-library-architecture` | Design or review reusable Python libraries or SDKs with isolated themes, a side-effect-free core, and facades. |
| `python-project-init-greenfield` | Initialize a greenfield Python repository from a locked blueprint and verify its sensing assertions. |
| `python-blueprint-authoring` | Author a greenfield Python blueprint using the existing six-section execution contract. |
| `python-blueprint-review` | Review a greenfield Python blueprint against its locked schema before project initialization. |
| `python-project-retrofit` | Execute a locked Python Retrofit V2 plan with risk-aligned human gates and acceptance checks. |
| `python-retrofit-plan-authoring` | Author a Retrofit V2 migration contract for an existing Python repository; do not execute it. |
| `python-retrofit-plan-review` | Review a Python Retrofit V2 plan for schema, risk, locatability, and executable acceptance assertions. |
| `python-plan-authoring` | Author a nontrivial Python implementation contract from intent and inspected facts; exclude isolated trivial edits. |
| `python-plan-review` | Review a Python implementation plan for executable decisions, contracts, async applicability, and test coverage. |
| `python-tdd-test-authoring` | Author behavior-mapped tests from an approved Python plan before production changes; verify declared initial states. |
| `python-implementation-review` | Check a Python implementation against an approved plan; enforce valid step evidence before tracing. |
| `python-code-review` | Review Python code quality in a standalone diff or formal workflow; standalone reviews need no approved plan. |
| `python-serialization-boundaries` | Design or review Python API, database, or message serialization as explicit semantic translation. |
| `python-pre-commit` | Create or merge pre-commit configuration for uv-based Python projects while preserving existing hooks. |
| `python-pyproject-toolconfig` | Append missing Ruff, Pyright, and pytest sections to pyproject.toml; preserve existing configuration. |
| `sense-env-scaffold` | Discover repository facts as structured JSON or evaluate a contract with the sense_env.py CLI. |
| `semantic-first-design` | Resolve one material Python design ambiguity in contracts, states, policies, boundaries, or failure semantics. |
| `step-creator` | Create a topic step artifact from an eligible plan and an explicitly selected workflow profile. |
| `subagent-dispatch-policy` | Select a permitted role or stop for one bounded task before a real subagent dispatch. |
| `worktree-manager` | Create, inspect, release, or remove Git worktrees with separate authorization and safety gates. |

## Notes
- Use `AGENTS.md` for governance guidance.
- Use `docs/repo-positioning.md` for repository positioning and migration
  boundary.
- For skill-path authority questions, treat `skills/` as canonical truth and
  `.github/skills/...` as a compatibility entrypoint only.
- For workflow-agent authority questions, treat `agents/` as canonical truth
  and `.github/agents/...` as a compatibility entrypoint only.
