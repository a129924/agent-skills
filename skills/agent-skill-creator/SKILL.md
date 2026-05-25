---
name: agent-skill-creator
description: Create a new single-purpose Agent Skill folder that reaches review-ready with a clear trigger, risk-appropriate validation, concise positive and negative examples, and explicit roles for all local files. Use this when asked to draft or scaffold a new Agent Skill for this repository.

complexity: high

risk_profile:
  - ambiguity_sensitive
  - code_modification

use_when:
  - a recurring task deserves its own Agent Skill
  - an existing skill is too broad and should be split
  - the user asks for a new skill scaffold or starter folder

do_not_use_when:
  - the task only needs a small edit to an existing skill
  - the change belongs in a local example or checklist file
---

# Purpose
Create a new skill that reaches `review-ready`.

# Trigger / When to use
Use this skill when:
- a recurring task deserves its own Agent Skill
- an existing skill is too broad and should be split
- the user asks for a new skill, scaffold, or starter folder

Do not use this skill when:
- the task only needs a small edit to an existing skill
- the change belongs in a local example or checklist file

# Inputs
- the skill's single responsibility
- the situations that should trigger the skill
- the skill's boundaries
- the reference material, if any
- any local assets the skill truly needs
- the complexity level, if it is already known
- whether the skill is lightweight, medium-complexity, or higher-risk
- any branching, external-tool, or downstream-impact signals that increase validation needs
- any `risk_profile` tags that apply

# Process
1. If the responsibility, trigger, or boundaries are ambiguous, stop and ask the user before drafting.
2. Start from `blueprint.md` and `folder-contract.md`.
3. Decide the validation weight before drafting:
   - lightweight: low-risk, low-branching guidance can stay concise
   - medium-complexity: decision-heavy guidance may need clearer process detail
   - higher-risk: gatekeeping, release, tool-driven, or high-impact guidance needs stronger misuse prevention
4. Propose `complexity` in YAML frontmatter. Propose applicable `risk_profile` tags for medium and high complexity skills.
5. If a topic plan locks a creator/reviewer-first rollout, keep the work inside creator, reviewer, and the minimum supporting policy/template files. Defer downstream regular skills to later topics instead of broadening the current one.
6. Create `skills/<skill-name>/`, where `<skill-name>` must use lowercase kebab-case. During transition, `.github/skills/` may remain the current active authored/reviewed workflow path, but this creator contract uses `skills/` as the canonical authoring target.
7. Keep the skill focused on one job.
8. Write `SKILL.md` with an explicit `Trigger / When to use` section and concise positive and negative examples.
9. Add `reference.md` or `examples.md`.
10. Use `references/` only as a split-reference supplement, not as a replacement for the required companion-file rule.
11. Split oversized reference material into `references/` when one `reference.md` would exceed about 1,000 tokens or more than 3 logical topics.
12. If `reference.md` is the chosen companion file and becomes too broad, keep it focused or reduce it to a short overview while moving detailed topics into `references/`.
13. Add `examples.md` when the skill is high complexity or the concise examples are not enough for about 80% of routine usage.
14. When the skill is higher-risk or easy to misuse, add stronger validation signals in `SKILL.md` or local files, such as explicit verification guidance, red flags, rationalizations, or a checklist.
15. Do not force heavyweight validation onto a simple low-risk skill just because another skill needed it.
16. If you add optional files or subfolders, declare each role in `Local references`.
17. If downstream planning-spine skills or future transition consumers would be affected by later path migration, record that as a follow-up implication instead of editing those surfaces in this phase.
18. When the draft is `review-ready`, tell the user: `This skill is review-ready. Please hand it to agent-skill-reviewer for review.`

# Examples
- Positive: Draft `release-note-shortener` with a clear trigger, brief positive and negative examples in `SKILL.md`, and stronger verification guidance only if the skill can materially affect release output.
- Negative: Draft a skill when the responsibility is still vague, mixes creation, review, and publishing, or forces release-grade validation onto a simple naming rule.

# Outputs
- a new `skills/<skill-name>/` folder, using lowercase kebab-case
- `SKILL.md` with concise positive and negative examples
- `examples.md` for high-complexity skills, or `reference.md` for local detail
- `references/` when local reference detail must be split by topic
- optional local additions with explicit roles
- validation weight aligned to the skill's risk and complexity
- a `review-ready` skill draft and explicit handoff message

# Validation

## Required Checks
- target skill folder does not exist before creation begins
- responsibility, trigger, and boundaries are unambiguous before drafting
- `SKILL.md` contains `name`, `description`, `complexity`, `Purpose`, `Trigger / When to use`, `Inputs`, `Process`, `Examples`, `Outputs`, `Boundaries`, and `Local references`
- at least one concise positive example and one concise incorrect example are present in `SKILL.md`

## Quality Checks (best effort)
- `risk_profile` tags match the actual skill behavior
- `examples.md` is present when the skill is high complexity, involves branching or code modification, or the SKILL.md examples cover less than ~80% of routine usage
- stronger validation signals are present when risk warrants it
- `Validation` and `Failure Handling` sections are present for high complexity output

## On Soft Fail
- mark status as INCOMPLETE
- continue with best-effort draft
- list missing information explicitly in the handoff message

# Failure Handling

## Missing Context
- mark output as INCOMPLETE
- list required additional inputs explicitly before proceeding

## Ambiguous Requirement
- if blocking: stop and ask the user before drafting
- if non-blocking: proceed with stated assumptions, list them in the handoff message

## Execution Limitation
- state the limitation explicitly in output
- do not fabricate content to fill gaps

# Workflow State Contract

When participating in a multi-agent skill creation workflow, include:
- current_step: <step name from Process>
- next_step: <next step or DONE>
- status: IN_PROGRESS | COMPLETE | INCOMPLETE | BLOCKED

Omit this section when the skill is created outside a multi-agent handoff flow.

# Boundaries
- Do not draft when the responsibility, trigger, or boundaries are still ambiguous.
- Do not create multi-purpose skills.
- Do not leave oversized multi-topic reference material in one undifferentiated file.
- Do not rely on hidden context outside the skill folder.
- Do not expand a creator/reviewer-first topic into downstream regular-skill rollout; defer those changes to a later topic plan.
- Do not add heavyweight validation to a lightweight skill unless the risk truly warrants it.
- Do not treat `.github/skills/` projection, promotion, or runtime/tooling follow-up as part of this drafting step.
- Do not claim `approved` or `stable`.
- Do not approve your own output.

# Local references
- `blueprint.md`: starter shape and section skeleton for new skills
- `folder-contract.md`: required core and optional role rules
- `examples.md`: creation patterns, complexity triggers, and review-ready examples
