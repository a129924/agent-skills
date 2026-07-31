# Requirements Baseline: python-retrofit-plan-review

> Status: **FROZEN** — ready for `business-to-technical-translation`.
> Frozen by: business-intent-alignment session (2026-04-30).
> Analysis scope: requirement baseline only; technical translation not yet produced.

---

## Problem Statement (Business Terms)

The repository now has a retrofit authoring lane and a retrofit execution lane,
but it still lacks a dedicated review gate between them. As a result, malformed
or unsafe Retrofit V2 contracts can drift from authoring into execution without
a domain-specific reviewer that checks contract validity before
`python-project-retrofit` consumes the plan.

A focused skill is needed to review an already-authored `retrofit-plan.md`
against the locked Retrofit V2 contract, reject unsafe or incomplete plans with
machine-consumable blocking issues, and keep review ownership separate from both
authoring and execution.

---

## Actors and Permission Boundaries

| Actor | Role |
| --- | --- |
| Retrofit plan author | Drafts or revises `retrofit-plan.md` via authoring flow |
| Retrofit plan reviewer | Reviews the authored contract and returns an independent verdict |
| Retrofit executor | Consumes only approved Retrofit V2 contracts during runtime execution |
| Repository maintainer / human operator | Decides whether to send failed review output back for rework and later authorizes publish / merge workflow gates |

---

## In-Scope Requirements

### R1 — Review the correct artifact and reject wrong-lane work

- **Actor**: Retrofit plan reviewer
- **Condition**: A drafted `retrofit-plan.md` exists and is presented for review
  before execution
- **Observable result**: The reviewer evaluates the retrofit contract itself and
  rejects requests that are actually greenfield blueprint work, generic skill
  review, or implementation diff review
- **Metric / decision rule**: The review output names the failing lane-fit or
  scope problem explicitly instead of silently approving or absorbing the wrong
  job
- **Failure meaning**: Wrong-lane requests bypass the intended repository review
  boundary and the retrofit review skill becomes a vague catch-all reviewer

### R2 — Enforce the locked Retrofit V2 heading contract

- **Actor**: Retrofit plan reviewer
- **Condition**: The authored plan claims to be a Retrofit V2 contract
- **Observable result**: The reviewer confirms the exact heading order:
  1. `## Survey Summary`
  2. `## Gap Analysis`
  3. `## Target Transformation`
  4. `## Migration Strategy`
  5. `## Acceptance Criteria`
- **Metric / decision rule**: Any missing heading, reordered heading, mixed
  heading set, or old-heading compatibility attempt produces a blocking issue
- **Failure meaning**: The executor would need to guess or reinterpret plan
  structure, breaking the locked Retrofit V2 contract

### R3 — Validate `yaml [migration-strategy]` as the execution-facing source of truth

- **Actor**: Retrofit plan reviewer
- **Condition**: The plan contains `## Migration Strategy`
- **Observable result**: The reviewer confirms a parseable fenced
  `yaml [migration-strategy]` block exists and includes at least
  `risk_level`, `destructive_actions`, and `backup_required`
- **Metric / decision rule**:
  - `risk_level` must be `LOW` or `HIGH`
  - `MEDIUM` is treated as unsupported for current execution
  - `destructive_actions` must be a YAML sequence, even when empty
  - `backup_required` must be the YAML boolean `true` or `false`
- **Failure meaning**: Runtime execution would receive incomplete or ambiguous
  risk metadata and could not safely apply the correct gate behavior

### R4 — Validate `yaml [sensing-assertions]` and supported assertion kinds

- **Actor**: Retrofit plan reviewer
- **Condition**: The plan contains `## Acceptance Criteria`
- **Observable result**: The reviewer confirms a fenced
  `yaml [sensing-assertions]` block exists and that every assertion record
  includes `kind`, `target`, and `expected`
- **Metric / decision rule**: Any malformed assertion, missing required field, or
  unsupported assertion kind produces a blocking issue; the currently supported
  subset remains `path_exists`, `path_type`, and `command_available`
- **Failure meaning**: The downstream `sense_env.py --mode acceptance` handoff
  would receive an assertion contract it cannot evaluate correctly

### R5 — Surface risk-alignment contradictions before executor handoff

- **Actor**: Retrofit plan reviewer
- **Condition**: The written target transformation, risk prose, and
  `migration-strategy` block can be compared as one contract
- **Observable result**: The reviewer blocks plans whose declared risk metadata
  contradicts the destructive reality implied by moves, deletes, overwrites,
  reshaping, or multi-toolchain replacement
- **Metric / decision rule**: A plan may not pass review when it claims `LOW`
  while its described changes imply destructive execution or while
  `destructive_actions` is empty or incomplete for a destructive path
- **Failure meaning**: The executor would be forced to discover a plan-level risk
  lie at runtime instead of receiving a review-safe contract

### R6 — Preserve the authoring-versus-executor boundary

- **Actor**: Retrofit plan reviewer
- **Condition**: The plan includes strategy prose such as migration direction,
  replacement intent, or cleanup intent
- **Observable result**: The reviewer rejects language that treats planning prose
  as if it already granted runtime answers for move/delete/coexist decisions,
  destructive authorization, or conflict resolution
- **Metric / decision rule**: Strategy declaration may explain intent, but it may
  not substitute for runtime gate choices owned by the executor
- **Failure meaning**: Human runtime gates become pre-decided by planning text,
  defeating the executor's safety contract

### R7 — Require locatable, executable retrofit targets

- **Actor**: Retrofit plan reviewer
- **Condition**: The authored plan describes current state, target state, and
  acceptance state
- **Observable result**: The reviewer can point to concrete source paths, target
  paths, entrypoints, config surfaces, and tool names without inferring missing
  structure
- **Metric / decision rule**: Abstract phrases such as `modernize the layout`,
  `clean it up`, or `reorganize the project` are blocking unless paired with
  concrete locators and verifiable target facts
- **Failure meaning**: The executor or a later creator would need to invent plan
  content that should already be explicit in the reviewed contract

### R8 — Return a machine-consumable review verdict only

- **Actor**: Retrofit plan reviewer
- **Condition**: The review completes
- **Observable result**: The reviewer returns exactly one machine-consumable JSON
  object with a verdict in the `approved | needs-rework` family and concrete
  blocking issues when it fails
- **Metric / decision rule**: The output contains no trailing prose, no rewritten
  plan draft, and no blended implementation advice outside the verdict object
- **Failure meaning**: Downstream workflow routing cannot reliably consume the
  reviewer output and role boundaries blur between reviewer and author

---

## Explicit Non-Goals

| Item | Reason excluded |
| --- | --- |
| Authoring `retrofit-plan.md` | Owned by `python-retrofit-plan-authoring` |
| Executing retrofit work | Owned by `python-project-retrofit` |
| Running acceptance assertions | Owned by `sense-env-scaffold` and `sense_env.py` |
| Broadening supported assertion kinds | Requires a separate planning topic |
| Reviewing skill folders or implementation diffs | Owned by other review paths such as `agent-skill-reviewer` or `/review` |
| Redesigning Retrofit V2 itself | Outside this topic; reviewer must reuse the locked existing contract |

---

## Acceptance Criteria (Success Signals)

**AC-1 (Contract safety)** — A maintainer can review the JSON output and tell in
one read whether the authored `retrofit-plan.md` is structurally valid and safe
to hand off to `python-project-retrofit`.

**AC-2 (Boundary preservation)** — No reviewed plan passes when planning prose is
being used as if it already granted runtime delete/move/coexist or destructive
authorization decisions.

**AC-3 (Executable acceptance)** — No reviewed plan passes when its
`yaml [sensing-assertions]` block contains malformed records or unsupported
assertion kinds outside `path_exists`, `path_type`, and `command_available`.

---

## Explicit Assumptions

- The review target is an already-authored Retrofit V2 `retrofit-plan.md`.
- The current execution contract remains Retrofit V2 only; no compatibility layer
  for older headings will be introduced here.
- `python-project-retrofit` remains the downstream consumer of approved retrofit
  plans.
- `sense-env-scaffold` v1 remains the acceptance executor and still supports only
  `path_exists`, `path_type`, and `command_available`.

---

## Extreme-Boundary Checks Applied

The baseline was challenged against these boundary cases and requires explicit
review handling for each:

1. missing or malformed `yaml [migration-strategy]`
2. missing or malformed `yaml [sensing-assertions]`
3. unsupported `risk_level` such as `MEDIUM`
4. destructive execution implied while `destructive_actions` is empty or partial
5. retrofit request that is actually greenfield in shape
6. abstract target transformation with no concrete files, packages, or configs
7. acceptance assertions too vague or unsupported for current `sense_env.py`
   evaluation

---

## Contradiction Log

No contradictions survived review. The following contradiction families were
explicitly resolved into blocking reviewer behavior:

| Potential conflict | Resolution |
| --- | --- |
| `LOW` risk vs destructive reality | Reviewer must fail the plan instead of letting runtime discover the mismatch |
| strategy declaration vs runtime authorization | Reviewer treats pre-authorized runtime choices as a contract error |
| retrofit review vs generic review | Reviewer stays inside `retrofit-plan.md` contract review only |
| acceptance intent vs tooling limits | Reviewer blocks unsupported assertion kinds instead of widening the acceptance contract |

---

## Remaining Blockers

None. This baseline is ready for `business-to-technical-translation`.

---

## Handoff Boundary

Next step: `business-to-technical-translation` →
`analysis/python-retrofit-plan-review/technical-spec.md`
