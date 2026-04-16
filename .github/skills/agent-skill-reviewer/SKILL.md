---
name: agent-skill-reviewer
description: Review a review-ready Agent Skill folder for required core files, concise positive and negative examples, declared local file roles, single responsibility, portability, independence, and explicit trigger clarity. Use this when a skill draft is ready to be approved or sent back for rework.
---

# Purpose
Review a `review-ready` skill before it becomes part of the stable library.

# Trigger / When to use
Use this skill when:
- a new skill has been drafted
- an existing skill has changed materially
- someone wants an `approved` or `needs-rework` review against repository rules

Do not use this skill when:
- the request is to author a new skill from scratch
- the task is only to browse the library without judging quality

# Inputs
- the target skill folder
- the repository rules for stable skills

# Process
1. Read `review-checklist.md`.
2. Confirm the required core exists.
3. Inspect frontmatter and required sections in `SKILL.md`, including concise positive and negative examples.
4. Confirm each optional file or folder has a clear declared role, including each file inside `references/` when that folder exists.
5. Confirm the skill has one clear responsibility.
6. Confirm the skill is portable, independent, and self-contained.
7. Treat `references/` as a split-reference supplement, not by itself as a replacement for the required companion-file rule.
8. If `reference.md` is too broad, require it to be split into `references/`.
9. If the skill is high complexity or the concise examples are not enough for about 80% of routine usage, require `examples.md`.
10. Confirm it has an explicit `Trigger / When to use` section.
11. Return `approved` or `needs-rework` with concrete fixes.

# Examples
- Positive: Review a refactoring skill whose `SKILL.md` has brief positive and negative examples and whose `examples.md` covers the complex branches.
- Negative: Approve a draft that has no negative example in `SKILL.md`, no `examples.md` for a branching refactor skill, or one oversized `reference.md` with unlabeled topics.

# Outputs
- `approved` or `needs-rework`
- blocking issues, if any
- concise follow-up fixes when the skill fails

# Boundaries
- Do not rewrite the skill's purpose to force a pass.
- Do not approve a skill that lacks required core files, required examples, or clear local roles.
- Do not ignore vague triggers or bundled responsibilities.
- Do not author the final implementation directly.

# Local references
- `review-checklist.md`: approval criteria, lifecycle rules, and reject signals
- `examples.md`: approved and needs-rework examples
