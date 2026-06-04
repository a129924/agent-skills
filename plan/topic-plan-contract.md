# Topic Plan Contract

## Purpose

Define the shared repo-level contract for topic-plan authority in this
repository.

This document governs topic-plan contract semantics. It does not replace:

- `AGENTS.md` as the governance canonical source
- `plan/agent-handoff-workflow.md` as the repo-level workflow-phase contract
- `plan/<topic>/<topic>.plan.md` as the topic-specific execution contract

## Scope

- This document defines the repo-level authority ordering for topic-plan
  contract semantics.
- This document defines the required section contract for
  `plan/<topic>/<topic>.plan.md`.
- This document defines repo-level reviewer handoff expectations for topic
  plans.
- This document does not define workflow phases, stop points, release routing,
  or PR-loop behavior.
- This document does not authorize convergence, projection, runtime
  adaptation, or skill-surface migration work.

## Contract Version

- `contract_version`: `1.0`
- Versioning is human-facing and repo-local.
- Future strict verification may add `contract_hash`, but `contract_version`
  remains the primary contract-language field for this repository topic-plan
  surface.

## Authority Ordering

When topic-plan authority questions arise, use this order:

1. `AGENTS.md`
2. `plan/agent-handoff-workflow.md`
3. `plan/topic-plan-contract.md`
4. `plan/<topic>/<topic>.plan.md`
5. `skills/plan-creator/**` and `skills/plan-reviewer/**`

Interpretation rules:

- `AGENTS.md` governs repo-level governance and source-of-truth boundaries.
- `plan/agent-handoff-workflow.md` governs repo-level workflow phases, stop
  points, roles, and status transitions.
- This document governs repo-level topic-plan contract semantics.
- Each topic plan governs one topic's bounded execution contract inside the
  repo-level governance and workflow constraints above.
- `skills/plan-creator/**` and `skills/plan-reviewer/**` are consumer guidance
  and evidence surfaces only; they do not own repo-level contract authority.

## Required Topic-Plan Sections

Every `plan/<topic>/<topic>.plan.md` must include these sections:

1. `Goal / Outcome`
2. `Scope`
3. `Locked Decisions`
4. `Boundaries / Exclusions`
5. `Status / Allowed Transitions`
6. `Artifact Paths`
7. `Implementation Steps`
8. `Validation / Acceptance Checks`
9. `Reviewer Handoff`
10. `Post-merge / release actions`
11. `Open Questions / Unresolved Items`

Section rules:

- Section names must stay canonical.
- A topic plan may add bounded topic-specific sections only when they do not
  contradict the required section set above.
- Topics that affect stable-library surfaces must add `Stable library metadata`
  and define timing explicitly.
- Topics that do not affect stable-library surfaces must state that intent
  explicitly instead of leaving it implicit.

## Topic-Plan Contract Rules

- `Artifact Paths` is an executable contract and must use exact repo-visible
  paths with owner and role.
- If a topic uses correction artifacts, each parent artifact, correction
  artifact, and any routing-controlling `review-log` or equivalent handoff
  path must be listed explicitly.
- `Implementation Steps` stay creator-owned; reviewer verdict logging,
  reviewer acceptance work, and Main Agent routing work do not belong there.
- `Reviewer Handoff` must be one machine-consumable JSON object.
- `Post-merge / release actions` must match the topic's actual stable-library
  and release timing.
- Unsafe placeholders such as `TBD`, `later`, or `follow normal process` are
  contract failures when explicit workflow decisions are required.

## Reviewer Handoff Contract

The repo-level reviewer handoff contract for topic-plan review is:

```json
{
  "verdict": "approved|needs-rework",
  "blocking_issues": [],
  "copilot_feedback_triage": {
    "ADDRESS": [],
    "DISCUSS": [],
    "SKIP": []
  }
}
```

Rules:

- The delivered reviewer handoff must be exactly one JSON object.
- `blocking_issues` is reserved for true contract-breaking problems.
- `copilot_feedback_triage` may be empty, but its three arrays must still be
  present.
- No prose may wrap or trail the final JSON reviewer verdict.

## Boundaries

- This document does not rewrite `skills/plan-creator/**` or
  `skills/plan-reviewer/**`.
- This document does not authorize edits under `skills/**`,
  `.github/skills/**`, `.codex/skills/**`, `.github/agents/**`, or
  `.codex/agents/**`.
- This document does not treat accepted Phase 1 planning inputs as approved
  implementation spec.
- Convergence, projection, runtime adaptation, `python-blueprint-review`
  absorption, and generic `copilot-instructions-init` convergence remain
  deferred to later bounded topics.
