---
name: agent-skill-creator
description: Create a new single-purpose Agent Skill folder that reaches review-ready with a clear trigger, concise positive and negative examples, and explicit roles for any local additions. Use this when asked to draft or scaffold a new Agent Skill for this repository.
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
- any local assets the skill truly needs
- the complexity level, if it is already known

# Process
1. If the responsibility, trigger, or boundaries are ambiguous, stop and ask the user before drafting.
2. Start from `blueprint.md` and `folder-contract.md`.
3. Create `.github/skills/<skill-name>/`, where `<skill-name>` must use lowercase kebab-case.
4. Keep the skill focused on one job.
5. Write `SKILL.md` with an explicit `Trigger / When to use` section and concise positive and negative examples.
6. Add `reference.md` or `examples.md`.
7. Add `examples.md` when the skill is high complexity or the concise examples are not enough.
8. If you add optional files or subfolders, declare each role in `Local references`.
9. When the draft is `review-ready`, tell the user: `This skill is review-ready. Please hand it to agent-skill-reviewer for review.`

# Examples
- Positive: Draft `release-note-shortener` with a clear trigger, brief positive and negative examples in `SKILL.md`, and local file roles.
- Negative: Draft a skill when the responsibility is still vague or mixes creation, review, and publishing.

# Outputs
- a new `.github/skills/<skill-name>/` folder, using lowercase kebab-case
- `SKILL.md` with concise positive and negative examples
- `examples.md` for high-complexity skills, or `reference.md` for local detail
- optional local additions with explicit roles
- a `review-ready` skill draft and explicit handoff message

# Boundaries
- Do not draft when the responsibility, trigger, or boundaries are still ambiguous.
- Do not create multi-purpose skills.
- Do not rely on hidden context outside the skill folder.
- Do not claim `approved` or `stable`.
- Do not approve your own output.

# Local references
- `blueprint.md`: starter shape and section skeleton for new skills
- `folder-contract.md`: required core and optional role rules
- `examples.md`: creation patterns, complexity triggers, and review-ready examples
