# Migration Plan Review Protocol

## Purpose

This document defines a repeatable plan-review protocol for the Codex migration
branches that are based on `feat/andrew/codex-skills-spec-worktree`.

It is an orchestration-layer protocol. It does not replace:

- `plan/agent-handoff-workflow.md`
- `skills/plan-reviewer/*`
- `skills/plan-creator/*`

## Audience

- branch owner
- planning actor
- review subagent
- implement agent

## Protocol scope

This first version applies to these migration branches:

- `feat/andrew/codex-migration-direct-move`
- `feat/andrew/codex-migration-copilot-residue-low`
- `feat/andrew/codex-migration-copilot-residue-medium`
- `feat/andrew/codex-migration-copilot-residue-high`
- `feat/andrew/codex-migration-copilot-specific`

Each branch must complete:

1. branch-local `analysis/<topic>/requirements.md`
2. branch-local `plan/<topic>/<topic>.plan.md`
3. this review protocol
4. only then implementer handoff

## Layer model

### Layer 1: Contract Review

Use `skills/plan-reviewer` as the only formal review subagent.

The review subagent must:

- read the target `plan/<topic>/<topic>.plan.md`
- read all four contract sources named by `skills/plan-reviewer`
- return exactly one JSON verdict object
- keep the existing repository schema unchanged

The review subagent must not:

- rewrite the plan directly
- invent a new reviewer schema
- expand scope on behalf of the planner

### Layer 2: Planner Review Loop

The planner owns the plan and owns the review loop.

The planner must:

- read the reviewer JSON
- accept only comments that improve correctness, feasibility, scope control,
  acceptance clarity, or contract compliance
- reject comments that only reflect architecture preference, style preference,
  or unnecessary scope expansion
- revise only the necessary parts of the plan

## Reviewer output contract

The formal reviewer output stays locked to the repository contract:

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

### Meaning of fields

- `verdict: approved`
  - the plan is safe to proceed to implementation
- `verdict: needs-rework`
  - the plan must be revised before implementation
- `blocking_issues`
  - implementation-blocking plan problems that must be fixed first
- `copilot_feedback_triage.ADDRESS`
  - required attention items that are important to keep visible, even when they
    are not the primary contract break
- `copilot_feedback_triage.DISCUSS`
  - non-blocking discussion items or useful improvements
- `copilot_feedback_triage.SKIP`
  - explicitly inapplicable comments

### Blocker rule

There is no third external verdict such as `blocked`.

If the reviewer finds a blocker:

- it still returns `verdict: needs-rework`
- the blocker must appear in `blocking_issues`

## Planner review loop

Use a maximum of 3 rounds.

### Round 1

1. Planner produces Plan v1.
2. Review subagent reviews Plan v1 with `skills/plan-reviewer`.

### Round 2

1. If verdict is `needs-rework`, planner revises only the necessary parts.
2. Planner produces Plan v2.
3. Review subagent reviews Plan v2.

### Round 3

1. If verdict is still `needs-rework`, planner revises only the necessary parts.
2. Planner produces Plan v3.
3. Review subagent reviews Plan v3.

### Stop rule after Round 3

If Round 3 still returns `needs-rework`, stop the loop.

The planner must then produce:

1. latest plan
2. unresolved review issues
3. planner recommendation
4. whether it is safe to hand to implementer

Do not continue into an unbounded review loop.

## Planner acceptance rules

The planner should accept review comments only when they improve:

- requirement correctness
- scope boundaries
- acceptance clarity
- implementation feasibility
- risk visibility
- decision clarity for the implementer
- contract compliance with repo workflow

The planner should reject comments that only introduce:

- unnecessary scope expansion
- reviewer-preferred architecture without a real feasibility problem
- implementation convenience bias
- naming or style preference that does not affect the contract

If the planner rejects a reviewer suggestion, it should record the reason in the
branch-local changelog or handoff note.

## Migration branch usage rules

For every migration branch listed above:

1. finish the branch-local `requirements.md`
2. finish the branch-local `plan.md`
3. send only the `plan.md` to the formal review subagent
4. use `requirements.md` as supporting source-of-truth context when plan intent
   must be checked
5. do not hand work to the implementer until the plan is `approved`, or until a
   human accepts the unresolved-issues state after Round 3

### Branch-local review checklist

- the target `plan.md` path exists and is the exact branch topic path
- the branch-local `requirements.md` exists and does not contradict the plan
- the review verdict is stored or reported without paraphrasing away the JSON
- the branch owner can state the current round: 1, 2, or 3
- implementer handoff does not happen from a `needs-rework` plan unless a human
  explicitly accepts that risk

## Standard Review SubAgent Prompt

Use this prompt when invoking the formal review subagent:

```text
You are a Plan Review SubAgent.

Use the repository skill `skills/plan-reviewer` as the formal review contract.

Review the target repo-visible topic plan at:
`{{PLAN_PATH}}`

You must read and apply all required contract sources named by
`skills/plan-reviewer/SKILL.md`, including:
- `plan/agent-handoff-workflow.md`
- `skills/plan-creator/reference.md`
- `skills/plan-creator/checklist.md`
- `skills/plan-creator/templates/topic-plan-template.md`

Review this plan as a contract between Planner and Implementer.

Focus on:
- requirement correctness
- scope boundaries
- acceptance criteria clarity
- implementation feasibility
- non-goals
- risk visibility
- decision clarity for the Implementer

Do not rewrite the plan.
Do not expand scope.
Do not invent a new reviewer schema.
Do not output prose outside the formal JSON.

Return exactly one JSON object that matches the `skills/plan-reviewer` contract.
```

## Standard Planner Receives Review Prompt

Use this prompt when the planner receives the review verdict:

```text
You are the Planner.

You have received a review from the formal Plan Review SubAgent.

Your job is to decide whether to revise the plan.

Rules:
- You own the plan.
- The reviewer does not rewrite the plan.
- Accept review comments only when they improve correctness, feasibility, scope control, acceptance clarity, or contract compliance.
- Reject review comments that introduce unnecessary scope, architectural preference, implementation bias, or non-essential wording churn.
- Preserve the original user intent.
- Do not let the plan drift toward the reviewer's preferred solution.
- This protocol allows a maximum of 3 review rounds.

Interpret the review as follows:
- `approved` -> finalize the plan and mark it Approved for Implementation
- `needs-rework` -> revise only the necessary parts and send the revised plan for the next review round
- if the review contains blockers, treat them as mandatory before implementation

If this is the third review round and the plan is still not approved:
- stop the loop
- produce:
  1. latest plan
  2. unresolved review issues
  3. planner recommendation
  4. whether it is safe to hand to Implementer
```

## Escalation rule

Escalate to a human when:

- Round 3 still returns `needs-rework`
- the reviewer identifies a blocker that changes branch classification
- `requirements.md` and `plan.md` disagree on a material branch boundary
- the planner believes a reviewer request would violate user intent or widen the
  topic beyond the branch scope

## Validation

This protocol is working as intended only if:

- the reviewer still emits the existing repository JSON schema
- the planner does not run more than 3 rounds
- `DISCUSS` items are not treated as blockers by default
- every migration branch uses the same review gate before implementer handoff
- branch owners can reuse the prompts in this document without recreating the
  workflow in chat
