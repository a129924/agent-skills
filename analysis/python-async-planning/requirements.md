# python-async-planning requirements baseline

Status: FROZEN for technical translation
Topic: `python-async-planning`
Primary path: `analysis/python-async-planning/requirements.md`
Source context: human-approved planning discussion on 2026-05-14, executed from `feat/andrew/python-async-planning-spec` based on `dev@77fa194`

## Business problem statement

The repository already supports Python async implementation guidance, but it does
not yet provide a reliable planning-stage control point for async-capable topics.
As a result, multiple actors can reach implementation or late review without a
frozen decision on async boundary, resource lifecycle, concurrency model,
failure handling, or cancellation behavior. The business cost is avoidable
implementation rework, runtime reliability risk, and architecture pollution
across layers.

## Actors and permission boundaries

| Actor | Role in this topic | Permission boundary |
| --- | --- | --- |
| Plan author | Writes or updates the initial plan for a Python topic | May propose async-planning coverage but must not self-approve its sufficiency |
| Plan reviewer | Verifies whether async-capable plans contain the required async decision baseline | May block or require retrofit, but may not silently rewrite the plan baseline |
| Downstream implementer | Implements from the approved plan baseline | Must follow the frozen async decisions and must not silently override them |
| Technical lead / architect | Resolves contradiction, portability, and layer-boundary disputes when needed | May approve re-plan or override by explicit decision, not by silent drift |

## In-scope measurable requirements

### BR-1 Trigger async planning when async-capable evidence is present

- **Actor**: plan author and plan reviewer
- **Condition**: a Python topic's plan, code, or discussion contains async-capable evidence
- **Observable result**: the workflow requires explicit async-planning coverage before implementation continues
- **Decision rule**: async-capable evidence includes one or more of the following:
  - `async def`, `await`, `asyncio`, or AnyIO usage
  - FastAPI async endpoints
  - `httpx.AsyncClient` or `aiohttp`
  - SQLAlchemy `AsyncSession` or async engine
  - async repository or async Unit of Work design
  - background task, queue, worker, or scheduler ownership
  - connection pool, session pool, semaphore, or rate-limit design
  - timeout, retry, cancellation, or backpressure policy
  - multiple external I/O calls that require a decision among sequential, concurrent, batch, or streaming execution
  - an existing sync pipeline being evaluated for async conversion
- **Acceptance signal**: another reviewer can point to the async-capable evidence and the required async-planning coverage without relying on hidden chat context
- **Failure meaning**: async lifecycle and concurrency risks are missed until implementation or late review

### BR-2 Do not over-trigger on syntax-only or non-architectural work

- **Actor**: plan author and plan reviewer
- **Condition**: a Python topic mentions async syntax or minor coroutine mechanics but does not introduce async boundary, lifecycle, concurrency, or failure-model risk
- **Observable result**: the workflow does not force `python-async-planning`
- **Decision rule**: exempt cases include:
  - syntax-only async/await teaching
  - a single missing `await` or local coroutine bug
  - lint, formatting, or typing-only issues
  - pure CPU-bound work without offload, worker, or process-pool design
  - ordinary synchronous refactors without I/O concurrency, lifecycle, cancellation, or transaction-boundary risk
  - topics where a complete async decision baseline already exists and the current change does not alter async boundary, resource lifecycle, or failure model
- **Acceptance signal**: the reviewer can explain why the topic stayed outside the async-planning gate by citing one or more exemption rules
- **Failure meaning**: routine planning work is burdened by false-positive blocking

### BR-3 Freeze a named async decision baseline for async-capable topics

- **Actor**: plan author
- **Condition**: an async-capable topic is being prepared for implementation
- **Observable result**: the plan contains named async-planning sections covering:
  - async boundary decision
  - resource lifecycle decision
  - concurrency model
  - failure model
  - cancellation / timeout policy
  - validation plan
  - handoff notes for the implementer
- **Decision rule**: an async-capable plan is incomplete until each required section exists in a repo-visible artifact
- **Acceptance signal**: a downstream implementer can locate each async decision in the plan baseline without rediscovering it from chat
- **Failure meaning**: implementation proceeds with hidden assumptions about lifecycle, concurrency, and failure semantics

### BR-4 Use both plan and review as evidence, not either one alone

- **Actor**: plan reviewer and downstream implementer
- **Condition**: an async-capable topic enters review or implementation
- **Observable result**: the plan records the async decision baseline and review verifies conformance to it
- **Decision rule**: plan and review are both required evidence sources
- **Acceptance signal**: if plan and review conflict, the conflict is recorded and routed instead of silently overridden
- **Failure meaning**: baseline drift becomes invisible and the wrong async behavior can pass through the workflow

### BR-5 Record contradictions instead of smoothing them over

- **Actor**: plan reviewer and technical lead / architect
- **Condition**: plan, review, or implementation disagree on an async decision
- **Observable result**: the disagreement is recorded in a contradiction log
- **Decision rule**: each contradiction record must include:
  - contradiction
  - source A
  - source B
  - risk impact
  - decision owner / next action
  - blocking or non-blocking classification
- **Acceptance signal**: another person can inspect the contradiction log and see what decision is still needed
- **Failure meaning**: hidden plan drift causes rework, unsafe implementation, or architecture erosion

### BR-6 Require minimal retrofit when async risk is discovered late

- **Actor**: plan reviewer
- **Condition**: an existing plan lacks async-planning sections and async risk is discovered after plan authoring has started
- **Observable result**: the workflow requires a minimal retrofit before normal implementation continues
- **Decision rule**: the retrofit must add:
  - async boundary decision
  - resource lifecycle decision
  - concurrency model
  - failure / timeout / cancellation policy
  - validation plan
- **Acceptance signal**: the reviewer marks the case as `retrofit required` instead of letting the omission pass silently
- **Failure meaning**: late-discovered risk enters implementation without a controlled backfill step

### BR-7 Keep the skill portable across Python async I/O planning

- **Actor**: technical lead / architect and plan author
- **Condition**: the new skill is authored for repository use and future reuse
- **Observable result**: the core rule set remains applicable to general Python async I/O planning, while examples may use FastAPI, SQLAlchemy, httpx, DDD, or workflow runners
- **Decision rule**:
  - FastAPI and SQLAlchemy may appear as examples, not prerequisites
  - domain layers must not be forced async by default
  - domain layers must not depend directly on `asyncio`, `httpx`, SQLAlchemy session objects, or FastAPI runtime objects
- **Acceptance signal**: another Python team can apply the core rules without depending on FastAPI- or SQLAlchemy-specific assumptions
- **Failure meaning**: the skill becomes framework-bound and encourages architecture pollution

## Assumptions

- The topic remains Python-specific rather than becoming a language-agnostic async planning skill.
- A repo-visible plan and reviewer verdict are the primary evidence surfaces for this workflow topic.
- High-risk async design may later justify a separate `analysis/<topic>/requirements.md`, but the topic does not fail solely because that artifact is absent in smaller cases.

## Non-goals

- This topic will not redesign the repository's entire Python planning framework.
- This topic will not turn `python-async-await` into the main planning skill.
- This topic will not require async planning checks for every Python plan.
- This topic will not force domain models or domain services to become async by default.

## Contradiction log

| Contradiction | Source A | Source B | Risk impact | Decision owner / next action | Status |
| --- | --- | --- | --- | --- | --- |
| Strong blocking gate can conflict with the need to avoid false positives on syntax-only work | Desire to block missed async risk before implementation | Desire to keep routine planning lightweight | Over-trigger reduces adoption; under-trigger misses risk | Resolved by BR-1 trigger evidence and BR-2 exemption list | resolved / non-blocking |
| Stable-library ambition can conflict with a narrow, topic-specific trigger | Skill should be reusable and stable | Trigger should remain intentionally narrow | Scope creep can turn the skill into a generic async checklist | Resolved by BR-7 portability rule and example-only framework usage | resolved / non-blocking |
| Review may detect async risk after a plan already exists | Existing plan may look complete | Late-discovered async risk changes implementation safety | Silent continuation causes rework and runtime risk | Resolved by BR-6 minimal retrofit rule | resolved / blocking until retrofit |

## Extreme-boundary checks

- **Wrong-role / missing authority**: implementers must not silently override trigger or blocker decisions; only explicit human re-plan or authorized decision may do so.
- **Interrupted planning flow**: if a plan exists but lacks async sections, treat the case as `retrofit required` rather than silently expanding scope during implementation.
- **Lowest-volume case**: syntax-only async questions and local coroutine bugs remain outside the new planning gate.
- **Peak-risk case**: async endpoint orchestration, pooled clients, transaction scope, cancellation, retry safety, and backpressure count as trigger-worthy evidence even when they look small at first glance.
- **Audit / reconstruction case**: contradiction handling must leave enough traceability that a reviewer can explain why the topic was gated or exempted.

## Blockers

None. The baseline is frozen for technical translation using the current decisions.

## Freeze decision

This baseline is ready for `analysis/python-async-planning/technical-spec.md`.
