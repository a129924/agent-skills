---
name: plan-reviewer
description: Independently review a repo-visible `plan/<topic>/<topic>.plan.md` for this repository after the plan exists and before execution proceeds. Use this when a topic plan needs a contract-level verdict against the repository workflow and plan-authoring rules.
---

# Purpose
Review a repo-visible topic plan as a planning-contract gate before execution proceeds.

# Trigger / When to use
Use this skill when:
- a repo-visible `plan/<topic>/<topic>.plan.md` already exists
- the plan needs an independent review before branch preparation or creator implementation begins
- an existing topic plan was revised and needs contract re-review
- Main Agent is routing plan review through `/fleet` or an equivalent independent reviewer path

Do not use this skill when:
- the main task is to author or revise the topic plan itself
- the task is to review a skill folder or implementation draft
- the request is for a generic project plan outside this repository
- the task is to rewrite the canonical workflow spec itself

# Inputs
- the target `plan/<topic>/<topic>.plan.md`
- the current workflow contract from `plan/agent-handoff-workflow.md`
- `.github/skills/plan-creator/reference.md`
- `.github/skills/plan-creator/checklist.md`
- `.github/skills/plan-creator/templates/topic-plan-template.md`
- any contextual Copilot feedback, if it exists

# Process
1. Confirm the task is topic-plan review, not plan authoring, skill review, publish routing, or workflow-spec editing.
2. Read the target topic plan plus all four contract sources before judging the plan.
3. Verify the topic plan path, required sections, canonical status model, artifact-path exactness, stable-library intent, reviewer handoff JSON shape, post-merge timing, and role boundaries.
4. Treat placeholders such as `TBD`, `later`, or `follow normal process` as contract failures when the workflow requires explicit decisions.
5. Treat missing sections, invalid transitions, vague artifact paths, undeclared stable intent, wrong timing, non-JSON reviewer handoff, and role-boundary confusion as blocking issues.
6. Keep the review focused on contract-breaking issues rather than wording polish or stylistic preferences that do not change workflow meaning.
7. Return exactly one JSON object with `verdict`, `blocking_issues`, and `copilot_feedback_triage` using `ADDRESS`, `DISCUSS`, and `SKIP`.

# Examples
- Positive: Review `plan/python-docstrings/python-docstrings.plan.md` after the plan exists, reject no contract-breaking issues, and return one JSON object that confirms non-stable intent, exact artifact paths, canonical transitions, and machine-consumable reviewer handoff.
- Negative: Use this skill to draft the topic plan, approve a plan that says `README/VERSION maybe later`, or return Markdown prose instead of the required JSON verdict.

# Outputs
- exactly one machine-consumable JSON object and no trailing prose
- `verdict`: `approved` or `needs-rework`
- `blocking_issues`: only true contract-breaking problems
- `copilot_feedback_triage` with `ADDRESS`, `DISCUSS`, and `SKIP`

# Verification
- confirm the review basis explicitly includes all four contract sources
- confirm required sections are present and named correctly
- confirm transitions stay canonical and execution timing is coherent
- confirm `Artifact Paths` are exact, bounded, and repo-visible
- confirm stable-library intent is explicit: clearly absent or explicitly declared
- confirm the verdict stays JSON-only with no prose outside the object

# Red Flags
- the plan invents a new status model or skips canonical phases
- `Artifact Paths` use broad labels such as `docs`, `skill folder`, or `maybe version files`
- stable-library timing is implied but not declared
- `Reviewer Handoff` is a table, prose note, or mixed-format report instead of one JSON object
- planning actor, creator, reviewer, and Main Agent responsibilities are blended together

# Common Rationalizations
- "The reviewer can infer the missing contract later."
- "The exact paths are obvious from context."
- "We can decide stable-library timing after implementation."
- "A rough status model is good enough if everyone understands the goal."

# Boundaries
- Do not rewrite the topic plan on behalf of the planning actor.
- Do not invent a second topic-plan schema that conflicts with `plan-creator` or the canonical workflow.
- Do not approve a plan that still has contract-breaking ambiguity.
- Do not turn this skill into implementation review, branch preparation, or publish execution.
- Do not emit anything except the single JSON verdict object.

# Local references
- `reference.md`: stable review basis, severity rules, and workflow-position guidance for topic-plan review
- `examples.md`: approved and needs-rework plan-review scenarios, including stable and non-stable cases
- `checklist.md`: repeatable contract checks for this higher-risk planning gate
