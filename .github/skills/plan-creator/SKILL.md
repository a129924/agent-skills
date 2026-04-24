---
name: plan-creator
description: Create a valid, repo-visible `plan/<topic>/<topic>.plan.md` for this repository, with correct workflow phases, status transitions, artifact paths, reviewer handoff contract, and stable-library intent handling. Use this when a new repository topic needs a real execution plan before creator work starts.
---

# Purpose
Create a valid topic plan for this repository's workflow.

# Trigger / When to use
Use this skill when:
- a new repository topic needs `plan/<topic>/<topic>.plan.md`
- an existing topic plan is missing workflow-critical contract sections
- the user wants a repo-visible handoff artifact before creator implementation starts

Do not use this skill when:
- the main task is to implement the skill or code artifact itself
- the task is to review or approve a finished topic plan
- the task is a tiny wording edit to an already-valid topic plan
- the request is for a generic project plan outside this repository

# Inputs
- the topic name
- the intended outcome of the topic
- the in-scope and out-of-scope boundaries
- the expected repo-visible artifact paths
- whether the topic affects stable-library surfaces
- any locked decisions that should not be rediscovered during implementation
- the current workflow contract from `plan/agent-handoff-workflow.md`

# Process
1. Confirm the task is really topic-plan authoring, not creator drafting, review, publish, or release execution.
2. Read the current workflow contract and write the topic plan as a repo-visible execution artifact.
3. Decide whether the topic is:
   - review-ready-only with no stable-library surfaces, or
   - a topic that explicitly affects stable-library surfaces and therefore needs declared timing
4. Lock scope, boundaries, and role ownership before drafting the plan body.
5. Enumerate exact `Artifact Paths`; do not use vague catch-all path descriptions.
6. Write the required topic-plan sections in canonical order.
7. Use only canonical workflow transitions and require machine-consumable reviewer handoff JSON.
8. If scope, artifact paths, role ownership, stable-library timing, or release intent is unclear, stop and ask instead of filling placeholders.

# Examples
- Positive: Draft `plan/python-docstrings/python-docstrings.plan.md` so it explicitly declares non-stable intent, exact artifact paths, canonical transitions, JSON reviewer handoff, and correct post-merge timing before creator implementation begins.
- Negative: Draft a plan that says "README/VERSION maybe later", leaves artifact paths as "skill folder and docs", uses free-form reviewer prose instead of JSON, or mixes planning, creator, and release responsibilities in one topic.

# Outputs
- a repo-visible `plan/<topic>/<topic>.plan.md`
- explicit scope, boundaries, and locked decisions for the topic
- exact artifact paths and workflow transitions
- clear stable-library intent: declared or explicitly absent
- a topic plan that is ready to hand to creator work

# Verification
- confirm all required topic-plan sections are present
- confirm current status and allowed transitions are explicit and canonical
- confirm `Artifact Paths` are exact, bounded, and role-labeled
- confirm reviewer handoff stays a single machine-consumable JSON object
- confirm post-merge / release timing matches the topic's actual scope

# Red Flags
- the plan mixes review-ready-only work with undeclared stable-library publish intent
- the plan says "TBD", "later", or "follow normal process" where the workflow needs an explicit contract
- artifact paths are broad labels instead of concrete repo-visible paths
- creator, reviewer, and main-agent ownership are blended together
- reviewer handoff is written as Markdown notes instead of JSON

# Common Rationalizations
- "Reviewer can infer the missing contract later."
- "We can decide whether this touches README or VERSION after implementation."
- "Artifact paths do not need to be exact as long as the scope sounds right."
- "A rough status model is good enough if the intent is obvious."

# Boundaries
- Do not implement the topic's actual skill or code artifact.
- Do not review, approve, or publish the topic.
- Do not guess stable-library timing or release intent.
- Do not rely on hidden chat context instead of a repo-visible plan.
- Do not generate a generic project-management plan for another repository.

# Local references
- `reference.md`: stable rules for section meaning, stable-library branching, role boundaries, and stop-and-ask triggers
- `examples.md`: detailed good and bad topic-plan scenarios, including stable and non-stable cases
- `checklist.md`: repeatable checks for a higher-risk planning skill
- `templates/topic-plan-template.md`: canonical topic-plan skeleton and section prompts for this repository
