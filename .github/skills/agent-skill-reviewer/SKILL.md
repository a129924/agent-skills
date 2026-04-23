---
name: agent-skill-reviewer
description: Review a review-ready Agent Skill folder for required core files, risk-appropriate validation, concise positive and negative examples, declared local file roles, single responsibility, portability, independence, and explicit trigger clarity. Use this when a skill draft is ready to be approved or sent back for rework.
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
- the topic plan, if the review is running under a repo-visible topic workflow
- any risk signals, such as gatekeeping responsibility, external-tool usage, branching, or larger downstream impact

# Process
1. Read `review-checklist.md`.
2. Confirm the required core exists.
3. Inspect frontmatter and required sections in `SKILL.md`, including concise positive and negative examples.
4. Confirm each optional file or folder has a clear declared role, including each file inside `references/` when that folder exists.
5. Confirm the skill has one clear responsibility.
6. Confirm the skill is portable, independent, and self-contained.
7. Assess whether the skill's validation weight matches its risk, branching, external-tool usage, and downstream impact.
8. Treat `references/` as a split-reference supplement, not by itself as a replacement for the required companion-file rule.
9. If `reference.md` is too broad, require it to be split into `references/`.
10. If the skill is high complexity or the concise examples are not enough for about 80% of routine usage, require `examples.md`.
11. If the skill is higher-risk or acts as a gatekeeper, require stronger validation signals or equivalent local guidance that makes misuse harder.
12. Confirm it has an explicit `Trigger / When to use` section.
13. Return `approved` or `needs-rework` with concrete fixes.

# Examples
- Positive: Review a refactoring or release-gating skill whose `SKILL.md` has brief positive and negative examples, whose local files justify stronger validation, and whose `examples.md` covers the complex branches.
- Negative: Approve a draft that has no negative example in `SKILL.md`, no `examples.md` for a branching refactor skill, or no stronger misuse-prevention guidance for a higher-risk gatekeeping skill.

# Outputs
- `approved` or `needs-rework`
- blocking issues, if any
- concise follow-up fixes when the skill fails

# Boundaries
- Do not rewrite the skill's purpose to force a pass.
- Do not approve a skill that lacks required core files, required examples, or clear local roles.
- Do not ignore vague triggers or bundled responsibilities.
- Do not require heavyweight validation on a lightweight skill unless the risk clearly warrants it.
- Do not author the final implementation directly.

# Local references
- `review-checklist.md`: approval criteria, lifecycle rules, and reject signals
- `examples.md`: approved and needs-rework examples
