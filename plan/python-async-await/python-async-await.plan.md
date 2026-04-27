# Python Async/Await Skill Plan

## Goal / Outcome

Create a repo-visible execution plan for a new stable skill at
`.github/skills/python-async-await/` that teaches when Python code should stay
synchronous versus become `async`, how to keep coroutine and task boundaries
explicit, and how to apply structured-concurrency discipline on a practical
Python 3.10 baseline. The completed topic should produce a review-ready skill
that covers direct `await`, spawned-task boundaries, cancellation semantics,
grouped task failure, `async with`, `async for`, async iterators, and async
generators without drifting into framework-specific runtime policy.

## Scope

- **In scope**:
  - create `.github/skills/python-async-await/SKILL.md`
  - create `.github/skills/python-async-await/reference.md`
  - create split references under `.github/skills/python-async-await/references/`
    for structured concurrency, cancellation/failure semantics, and async
    protocols
  - create `.github/skills/python-async-await/examples.md`
  - define first-draft rules for:
    - synchronous versus `async def` boundary choice
    - direct `await` versus spawned task choice
    - structured concurrency in a Python 3.10-compatible form
    - cancellation and grouped task-failure semantics
    - `async with`, `async for`, async iterators, and async generators
  - include a supplementary AnyIO note without making AnyIO the required
    mainline dependency
  - declare stable-library promotion timing for `README.md` and `VERSION`
  - declare the post-merge tag action for this new stable skill topic

- **Out of scope**:
  - framework-specific async policy for FastAPI, Starlette, Celery, or similar
    ecosystems
  - event-loop bootstrap, worker runtime setup, deployment, or server process
    management
  - deep async testing policy or pytest plugin guidance
  - Trio / AnyIO / Curio runtime comparison as a first-draft mainline topic
  - queueing, backpressure, stream-processing, or broader async architecture
    policy beyond ordinary async code design

## Locked Decisions

- This topic is a **stable-library-affecting topic** with declared publish and
  release timing.
- The skill's primary scope is **general Python async design**, not framework
  runtime policy.
- First-draft included surface:
  - `async def` versus synchronous function choice
  - direct `await`
  - spawned task boundaries
  - structured concurrency
  - `async with`
  - `async for`
  - async iterators
  - async generators
- First-draft excluded surface:
  - framework-private async internals
  - event-loop bootstrap / deployment policy
  - deep async testing guidance
  - queue-heavy or backpressure-heavy architecture rules
- Practical version baseline:
  - implementation guidance should work on **Python 3.10**
  - the design should still preserve **3.11-grade structured-concurrency
    discipline**
  - the preferred shape should upgrade cleanly to native `TaskGroup` later
    without rewriting higher-level business logic
- Structured concurrency policy:
  - treat structured concurrency as a **mainline rule**, not an optional note
  - reject scattered fire-and-forget `create_task` as a normal pattern
  - prefer a stdlib-first 3.10-compatible wrapper or coordinator pattern whose
    ownership model matches later `TaskGroup` usage
  - AnyIO may appear only as a **supplementary note**, not as the required first
    dependency
- Failure and cancellation policy:
  - cancellation is a first-class contract concern
  - do not normalize swallowing `asyncio.CancelledError`
  - grouped task failures must remain explicit instead of silently collapsing to
    one arbitrary failure
  - concrete examples may mention `BaseAppError` as the semantic project-level
    error family, but the portable rule is to preserve the caller's semantic
    error family rather than silently discarding task failures
- Stable-library timing:
  - update `README.md` and `VERSION` at `publish-in-progress`
  - create and push the repository tag at `release`

## Boundaries / Exclusions

- `python-context-management` owns **synchronous** context managers and `with`
  design; this topic only owns async protocol guidance such as `async with` and
  async lifetime/cancellation notes tied to coroutine behavior.
- `python-error-handling` owns general exception hierarchy, translation, and
  propagation; this topic only owns async-specific semantics such as
  cancellation, grouped task failure, timeout boundaries, and when task
  orchestration must not swallow semantic errors.
- `python-testing-pytest` owns pytest design, fixtures, parametrization, mocks,
  and test-surface policy; this topic must not turn into an async testing skill.
- `python-control-flow` owns branch shape; this topic only decides when async
  orchestration changes the lifetime or ownership model of code.
- `python-type-hints-strict` owns general typing policy; this topic may mention
  async-specific protocol types only as needed for async API guidance.
- If later work needs framework-specific async policy, async test-client rules,
  or runtime-bootstrap rules, stop and split that into a separate topic instead
  of broadening this skill.

## Status / Allowed Transitions

- **Current**: `pr-open`
- **Execution model**: follow the canonical creator -> reviewer -> publish ->
  merge -> release path; this topic reaches `released` because it declares a
  post-merge tag action.
- **Allowed transitions**:
  - `planned` -> `creator-in-progress`
  - `creator-in-progress` -> `review-ready`
  - `review-ready` -> `reviewer-in-progress`
  - `reviewer-in-progress` -> `approved`
  - `reviewer-in-progress` -> `needs-rework`
  - `needs-rework` -> `creator-in-progress`
  - `approved` -> `creator-in-progress`
  - `approved` -> `publish-in-progress`
  - `publish-in-progress` -> `pr-open`
  - `publish-in-progress` -> `merged`
  - `pr-open` -> `needs-rework`
  - `pr-open` -> `merged`
  - `merged` -> `released`
  - `released` -> terminal

Routing notes:

- Use the standard Phase 4.5 planner-alignment checkpoint from
  `plan/agent-handoff-workflow.md`.
- If creator or reviewer drifts into framework-specific async policy, runtime
  bootstrap, or deep async testing guidance, route back to
  `creator-in-progress` and repair scope before publish.

## Artifact Paths

| Artifact | Path | Owner | Role |
| --- | --- | --- | --- |
| Topic plan | `plan/python-async-await/python-async-await.plan.md` | Planning actor | Repo-visible execution contract for this topic |
| Skill contract | `.github/skills/python-async-await/SKILL.md` | Creator | Executable skill instructions for general Python async/await design and boundaries |
| Reference overview | `.github/skills/python-async-await/reference.md` | Creator | Focused overview for the async reference layer and navigation entry for split local guidance |
| Reference split | `.github/skills/python-async-await/references/structured-concurrency.md` | Creator | Detailed rules for Python 3.10-compatible structured concurrency, direct `await` versus spawned-task ownership, and the supplementary AnyIO note |
| Reference split | `.github/skills/python-async-await/references/cancellation-and-failure.md` | Creator | Detailed rules for cancellation, timeout boundaries, grouped task failure, and preserving semantic error-family intent in async flows |
| Reference split | `.github/skills/python-async-await/references/async-protocols.md` | Creator | Detailed rules for `async with`, `async for`, async iterators, async generators, and protocol-boundary anti-patterns |
| Detailed examples | `.github/skills/python-async-await/examples.md` | Creator | Multi-path examples, anti-patterns, and split signals for async boundaries and orchestration choices |
| Stable-library summary | `README.md` | Main Agent | Add the stable-library row for `python-async-await` after approval |
| Repo version baseline | `VERSION` | Main Agent | Bump the repository version for a new stable skill |

Artifact path notes:

- This topic does **not** modify `.github/copilot-instructions.md`,
  `plan/agent-handoff-workflow.md`, or any existing `python-*` skill folder.
- These paths are an executable contract.
- `references/` is intentionally part of this topic because the reference layer
  spans more than three logical topics.
- If later work tries to add async testing subfolders, framework-specific local
  runtime docs, or other repo surfaces outside these paths, stop and repair the
  plan or split the work into a separate topic.

## Stable library metadata

### README row

- Table: `## Current skills`
- Exact row:

  `| \`python-async-await\` | defines general Python async/await rules for choosing async boundaries, preserving structured concurrency, and handling cancellation, async protocols, and grouped task failure explicitly |`

- Position:
  - after `python-decorators`
  - before `sense-env-scaffold`

### VERSION bump

- Current: `0.19.0`
- Direction: `MINOR`
- New: `0.20.0`
- Reason: new stable skill, non-breaking capability addition

### Timing

- README / VERSION timing: `publish-in-progress`
- Reason: the PR should show both the new stable skill and the stable-library
  surfaces it promotes

### Additional release metadata

- Tag action: create and push annotated tag `v0.20.0` at `release`
- Release notes artifact: none in this topic
- GitHub Release object: none in this topic unless a later release-specific topic
  adds one

## Implementation Steps

### Creator Phase (after plan approval)

1. Create `.github/skills/python-async-await/`.
2. Draft `SKILL.md` with the required repository shape:
   - YAML frontmatter
   - Purpose
   - Trigger / When to use
   - Inputs
   - Process
   - Examples
   - Outputs
   - Boundaries
   - Local references
3. Keep the mainline trigger focused on general Python async design, not
   framework runtime policy or deployment setup.
4. In `SKILL.md`, make structured concurrency the normal pattern and treat
   scattered fire-and-forget task spawning as boundary or anti-pattern material.
5. Draft the reference layer as `reference.md` + `references/`:
   - `reference.md` as the focused overview and navigation file
   - `references/structured-concurrency.md` for sync-versus-async choice, direct
     `await` versus spawned task, Python 3.10-compatible structure, and the
     supplementary AnyIO note
   - `references/cancellation-and-failure.md` for cancellation, timeout
     boundaries, grouped task failure, and preserving semantic async error
     meaning
   - `references/async-protocols.md` for `async with`, `async for`, async
     iterators, and async generators
6. Draft `examples.md` because this topic has branching choices, protocol
   variety, and anti-pattern risk.
7. Ensure the examples set covers at minimum:
   - a boundary case where code should remain synchronous
   - a direct `await` example
   - a Python 3.10-compatible structured-concurrency example
   - an anti-pattern using scattered `create_task`
   - cancellation propagation that does not swallow `CancelledError`
   - grouped task failure with a semantic error-family example using
     `BaseAppError`
   - `async with`
   - `async for` or async generator usage
   - a supplementary AnyIO note that does not replace the stdlib-first mainline

### Reviewer Phase (after creator delivers review-ready)

1. Verify the skill stays within general Python async design scope.
2. Verify the full reference layer exists at the locked paths:
   `SKILL.md`, `reference.md`, `references/`, and `examples.md`.
3. Verify structured concurrency is treated as the default and scattered
   fire-and-forget task spawning is not normalized.
4. Verify the practical baseline remains Python 3.10-compatible while preserving
   a clear upgrade path toward native `TaskGroup`.
5. Verify AnyIO is presented only as a supplementary note, not as the required
   first-draft runtime.
6. Verify cancellation and grouped task failure are explicit and do not normalize
   swallowing `CancelledError` or semantic task failures.
7. Verify async protocols stay in scope without drifting into framework runtime
   policy or async testing guidance.

### Main Agent Publish Phase (after approval + planner alignment)

1. Update `README.md` with the exact locked `python-async-await` row at the
   locked position.
2. Update `VERSION` from `0.19.0` to `0.20.0`.
3. Stage only the locked artifact set for this topic; do not stage unrelated
   files.
4. Open the PR with the skill files plus stable-library surfaces visible
   together, because timing is locked to `publish-in-progress`.

## Validation / Acceptance Checks

- [ ] The topic plan remains valid at
  `plan/python-async-await/python-async-await.plan.md`.
- [ ] `Status / Allowed Transitions` uses canonical workflow transitions only,
  including `merged` -> `released`.
- [ ] `Artifact Paths` remain exact and bounded to the listed repo-visible files.
- [ ] Stable-library intent is explicit and executable:
  - [ ] `README.md` row text is locked
  - [ ] `VERSION` bump is locked
  - [ ] publish timing is declared as `publish-in-progress`
  - [ ] release timing is declared for the tag action
- [ ] Creator output is limited to:
  - [ ] `.github/skills/python-async-await/SKILL.md`
  - [ ] `.github/skills/python-async-await/reference.md`
  - [ ] `.github/skills/python-async-await/references/structured-concurrency.md`
  - [ ] `.github/skills/python-async-await/references/cancellation-and-failure.md`
  - [ ] `.github/skills/python-async-await/references/async-protocols.md`
  - [ ] `.github/skills/python-async-await/examples.md`
- [ ] Main Agent publish output is limited to:
  - [ ] `README.md`
  - [ ] `VERSION`
- [ ] Release output is limited to:
  - [ ] annotated tag `v0.20.0`
- [ ] `SKILL.md` contains concise positive and negative examples.
- [ ] `examples.md` covers sync-vs-async choice, structured concurrency,
  cancellation, grouped failure, async protocols, and anti-patterns.
- [ ] Structured concurrency guidance is explicit:
  - [ ] no scattered `create_task` normalization as a routine pattern
  - [ ] Python 3.10-compatible ownership pattern is stated
  - [ ] future migration to native `TaskGroup` is preserved
  - [ ] AnyIO stays supplementary
- [ ] Boundary integrity holds:
  - [ ] no framework-runtime drift
  - [ ] no deep async testing drift into `python-testing-pytest`
  - [ ] no general error-hierarchy drift into `python-error-handling`
  - [ ] no synchronous context-manager drift back into `python-context-management`
- [ ] Reviewer handoff remains a single machine-consumable JSON object.

## Reviewer Handoff

```json
{
  "verdict": "approved|needs-rework",
  "blocking_issues": [
    {
      "issue": "example",
      "file": "relative/path",
      "fix": "specific required correction"
    }
  ],
  "copilot_feedback_triage": {
    "ADDRESS": [
      {
        "comment": "required copilot feedback to apply",
        "location": "relative/path:line",
        "why": "why this feedback is required"
      }
    ],
    "DISCUSS": [
      {
        "comment": "optional or ambiguous feedback",
        "optional": true,
        "why": "why this is discussion-level only"
      }
    ],
    "SKIP": [
      {
        "comment": "feedback to skip",
        "why": "why this is not applicable"
      }
    ]
  }
}
```

## Post-merge / release actions

- After merge and an explicit human resume signal, Main Agent runs post-merge
  local sync on the default branch.
- Then Main Agent runs the release gate for the declared version/tag context.
- If the release gate passes, Main Agent creates and pushes annotated tag
  `v0.20.0`.
- No separate GitHub Release object or release-notes artifact is required in
  this topic.

## Open Questions / Unresolved Items

- None. The first-draft scope, stable-library timing, and release contract are
  locked in this plan.
