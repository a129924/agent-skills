# Cross-Language Skill Candidate Basis

## Purpose and evidence boundary

This document is a first-pass, read-only evidence basis for the 11 locked
skills below. It identifies where a future topic could separate a portable
core from Python, Swift, and TypeScript language appendices.

It is **not** validation of a Swift or TypeScript project, a final portability
classification, or authority to change a skill, its name or path, a platform
projection, workflow binding, runtime behavior, or stable-library surface.
`skills/` remains the canonical source of reusable skill behavior under the
repository authority model in [Repository Positioning](../repo-positioning.md).

The only evidence used here is the locked current repository material:

- [governance](../../AGENTS.md), [repository positioning](../repo-positioning.md),
  [workflow contract](../../plan/agent-handoff-workflow.md), and
  [topic-plan contract](../../plan/topic-plan-contract.md);
- the accepted [Phase 1 summary](phase-1/00-summary.md),
  [inventory](phase-1/01-skill-inventory.md),
  [convergence candidates](phase-1/06-convergence-candidates.md), and
  [human review verdict](phase-1/09-human-review-verdict.md); and
- the 11 linked canonical `skills/<name>/SKILL.md` files below.

“Swift appendix needed” and “TypeScript appendix needed” therefore mean
future validation/design work, never observed project behavior.

## Candidate model

For a later, separately approved topic, a portable core would state the
language-independent decision or behavior. A language appendix would map that
core to a language's error model, type system, test framework, documentation
format, tooling, and idioms. A language-specific blocker prevents treating the
current Python instructions as that core without further evidence.

Scope risk describes the chance that a follow-up accidentally crosses this
topic's boundary; it is not an implementation priority or a release decision.

## Testing and validation

| Candidate | Portable core | Python evidence | Swift appendix needed | TypeScript appendix needed | Language-specific blockers | Recommended action | Scope risk |
| --- | --- | --- | --- | --- | --- | --- | --- |
| [`python-tdd-test-authoring`](../../skills/python-tdd-test-authoring/SKILL.md) | Before implementation, map approved behavior to observable tests; preserve an explicit readiness or blocked result. | Requires RED tests, a requirement-to-test mapping, production-code guard, and structured verdicts. | Define plan/spec evidence, test-first mechanics, async and actor-isolation treatment, and the chosen native test surface. | Define plan/spec evidence, runner and assertion conventions, async Promise behavior, and module-mocking treatment. | The current contract requires `pytest`, Python plan-routing names, Python test discovery, and Python-specific commands. | Defer; first design a language-neutral test-authoring contract, then validate separate appendices. | High: its workflow gates and file contracts can drift. |
| [`python-testing-pytest`](../../skills/python-testing-pytest/SKILL.md) | Prefer isolated behavior tests; use reusable setup, data-driven cases, and interaction assertions only when the interaction is contractual. | Specifies pytest fixtures, parametrization, `unittest.mock`, and `monkeypatch`. | Map setup, parameterization, mocks/fakes, async tests, and isolation to the selected Swift testing framework. | Map setup, table-driven cases, mocks/fakes, async tests, and isolation to the selected TypeScript test runner. | Framework APIs and language concurrency/module semantics determine how the principles can be expressed. | Candidate for a small generic unit-test-design core with separately validated language appendices. | Medium: avoid silently selecting test frameworks. |
| [`python-implementation-review`](../../skills/python-implementation-review/SKILL.md) | Verify an implementation against an approved plan: trace steps, enforce non-goals, compare public contract, and confirm planned tests before quality review. | Uses Python plan-review/code-review routing, `*.step.md` semantics, and Python API examples. | Define public-contract evidence for Swift modules, visibility, errors, and concurrency where relevant. | Define public-contract evidence for exported APIs, type declarations, runtime errors, and package boundaries. | Current sequencing and reviewer names are Python-specific; exact plan-section and progression rules are repository workflow contracts. | Defer until a future topic defines a language-neutral implementation-review handoff that defers to repository workflow authority. | High: workflow/contract ownership must not be duplicated. |

## Code review

| Candidate | Portable core | Python evidence | Swift appendix needed | TypeScript appendix needed | Language-specific blockers | Recommended action | Scope risk |
| --- | --- | --- | --- | --- | --- | --- | --- |
| [`python-code-review`](../../skills/python-code-review/SKILL.md) | After plan conformance review, assess code quality with explicit findings, severity, evidence location, and project-tooling-aware judgment. | Defines seven Python-focused dimensions and detects `pyproject.toml`, Python linters, and strict typing. | Define Swift package/tooling detection, ownership/concurrency checks, error conventions, test style, and observability expectations. | Define `tsconfig`/linter detection, type-safety policy, Promise/error behavior, test style, and observability expectations. | The seven dimensions contain Python syntax, PEP conventions, and `pyright`/`mypy`/`ruff` thresholds; no target policies are evidenced. | Defer; retain the generic review-process idea only, pending per-language quality policies. | High: genericizing severity rules would invent project policy. |

## Design boundaries

| Candidate | Portable core | Python evidence | Swift appendix needed | TypeScript appendix needed | Language-specific blockers | Recommended action | Scope risk |
| --- | --- | --- | --- | --- | --- | --- | --- |
| [`semantic-first-design`](../../skills/semantic-first-design/SKILL.md) | Resolve one caller-relevant ambiguity with the smallest explicit distinction; route concrete design choices to their specialized owner. | Uses Python APIs, types, and named Python-specialist skills as routing examples. | Relate distinctions to `Optional`, `Result`, protocol/value semantics, and ownership or concurrency only when target context requires it. | Relate distinctions to `undefined`/`null`, discriminated unions, thrown errors, and structural typing only when target context requires it. | Existing routing targets and examples are Python-specific; target-language design conventions are not in evidence. | Strong candidate for a language-neutral semantic guardrail; validate appendix routing separately. | Low: preserve its one-ambiguity boundary. |
| [`boundary-outcome-design`](../../skills/boundary-outcome-design/SKILL.md) | At each architectural boundary, preserve, translate, compress, promote, or propagate distinctions according to the receiving caller's decision needs. | Refers to Python `Result`, exceptions, `Protocol`, and Python-layer examples while the layer vocabulary rules are broader. | Define the relationship of `Error`, `Result`, async throws, and protocol-based ports to the generic outcome vocabulary. | Define the relationship of thrown values, discriminated unions, rejected Promises, and structural ports to that vocabulary. | Outcome representation and error propagation differ materially; no target architecture or caller-decision evidence is available. | Candidate for a generic boundary-semantics core; defer representation rules to language appendices. | Medium: do not prescribe one universal result/error taxonomy. |
| [`python-error-handling`](../../skills/python-error-handling/SKILL.md) | Distinguish known domain failures from programmer misuse; translate known controllable failures once at a meaningful boundary and preserve causal context. | Requires `Exception` inheritance, Python chaining syntax, built-in exceptions, and excludes Python multi-error features. | Define `Error` conformance, typed/unchecked error conventions, `throws`, `Result`, and causal diagnostic preservation. | Define typed error policy, thrown values, rejected Promises, error causes, and runtime validation boundaries. | Python exception hierarchy and chaining cannot be carried unchanged; application error policy is not supplied for either target language. | Candidate for a generic error-semantics core after each language's error-model appendix is evidenced. | Medium: do not accidentally decide framework mapping, retry, or logging policy. |
| [`python-serialization-boundaries`](../../skills/python-serialization-boundaries/SKILL.md) | Translate raw transport data at the boundary; preserve missing/null/update intent, normalize values deeply, and keep inbound and outbound contracts independently semantic. | Uses Python `dict`, `None`, `UUID`, `datetime`, `Decimal`, DTO examples, and Python-adjacent routing. | Define `Codable` and custom decoding rules, `Optional` versus missing semantics, date/decimal identifiers, and coding-key behavior. | Define runtime decoding/validation, `undefined` versus `null`, JSON shape rules, and type-only versus runtime guarantees. | Swift and TypeScript represent absence and runtime validation differently; no transport contract or codec policy is supplied. | Candidate for a generic serialization-semantics core; validate per-language boundary appendices against real transports. | Medium: PATCH semantics must not be guessed. |

## Coding style

| Candidate | Portable core | Python evidence | Swift appendix needed | TypeScript appendix needed | Language-specific blockers | Recommended action | Scope risk |
| --- | --- | --- | --- | --- | --- | --- | --- |
| [`python-naming`](../../skills/python-naming/SKILL.md) | Use one consistent, repository-owned naming and visibility convention for each code surface; reject ambiguous mixed conventions. | Maps modules, classes, constants, and private helpers to Python `snake_case`, `PascalCase`, `UPPER_CASE`, and leading underscores. | Define Swift API, type, member, file, acronym, and access-control conventions from the target repository. | Define TypeScript package, file, type, value, export, and private-convention rules from the target repository. | The actual naming matrix is language and repository specific; no Swift/TypeScript policy is provided. | Preserve only the policy-selection method as a possible core; defer all naming rules to language/repository appendices. | Medium: no style-guide assumptions. |
| [`python-control-flow`](../../skills/python-control-flow/SKILL.md) | Choose the clearest branch form for the decision shape; make meaningful absence/value distinctions explicit; use early exits when they improve readability. | Specifies `if`/`elif`, `match`/`case`, `None`, Python truthiness, and Python `Enum` examples. | Define `switch` exhaustiveness, pattern matching, `Optional`, guards, `if case`, and `defer` interaction. | Define union narrowing, `switch`, truthiness, `null`/`undefined`, guards, and Promise control-flow considerations. | Branch syntax, exhaustiveness, cleanup, and nullability rules differ; no target-language style policy is evidenced. | Candidate for a limited branching-principles core with language-specific decision matrices. | Medium: avoid abstract rules that hide safety differences. |
| [`python-docstrings`](../../skills/python-docstrings/SKILL.md) | Document public contracts from explicit signals: purpose, caller-relevant conditions, outputs, and error behavior, without inventing rationale. | Requires Google Style docstrings, Python signatures, `Raises`, generators, and dataclass-specific guidance. | Define DocC syntax, symbol linking, parameters/returns/throws conventions, and public/internal documentation expectations. | Define TSDoc/JSDoc format, exported API documentation, Promise/rejection treatment, and generated declaration interplay. | Documentation syntax, toolchain integration, and public-surface norms are language-specific; no target documentation policy is provided. | Candidate for a contract-first documentation core; defer format and tooling as language appendices. | Low: retain the explicit-evidence rule and avoid dictating a format. |

## Deferred and out of scope

- This inventory does not assess the excluded Python runtime/toolchain,
  project-lifecycle, object-model, syntax-specific, API/module, or async
  skills.
- It does not choose a canonical generic skill name, folder layout, appendix
  schema, migration path, projection strategy, implementation order, or
  release policy.
- It does not read a Swift or TypeScript project, select a test runner,
  linter, serializer, documentation tool, error representation, or coding
  convention.
- It does not alter the accepted Phase 1 evidence or authorize Phase 2/3
  convergence or projection work. Those boundaries remain stated in the
  [Phase 1 human verdict](phase-1/09-human-review-verdict.md) and
  [projection-adapter design](phase-3/projection-adapter-design.md).

## Human-review handoff

Human review should decide only whether this first-pass candidate set is a
useful basis for a later, separately scoped discovery/design topic. That later
topic must supply target Swift and TypeScript repository evidence before
selecting any generic core, language appendix, implementation sequence, or
skill change.
