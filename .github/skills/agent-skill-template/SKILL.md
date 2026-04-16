---
name: agent-skill-template
description: Provide the canonical structure for a review-ready, portable, single-purpose Agent Skill in this repository, including layered example guidance. Use this when asked for the standard shape of a new skill or when building a new skill manually from a template.
---

# Purpose
Provide the reference shape for a `review-ready` skill.

# Trigger / When to use
Use this skill when:
- a new skill needs a clean starting point
- you want the canonical section layout for `SKILL.md`
- you need the minimum companion files for a stable skill

Do not use this skill when:
- the task is to review a finished skill
- the task only needs a small edit to an existing skill

# Inputs
- the skill name
- the single responsibility
- the trigger situations
- any truly local assets

# Process
1. Read `template.md` and `folder-contract.md`.
2. Copy the folder shape and section layout.
3. Replace placeholders with one clear responsibility.
4. Add concise positive and negative examples to `SKILL.md`.
5. Add `reference.md` or `examples.md`.
6. Use `references/` only as a split-reference supplement, not as a replacement for the required companion-file rule.
7. Split oversized reference material into `references/` when one `reference.md` would exceed about 1,000 tokens or more than 3 logical topics.
8. If `reference.md` is the chosen companion file and becomes too broad, keep it focused or reduce it to a short overview while moving detailed topics into `references/`.
9. Add `examples.md` when the skill is high complexity or the concise examples are not enough for about 80% of routine usage.
10. If you add optional files or folders, declare each role in `Local references`.
11. Stop at `review-ready`.
12. Let a human or external workflow pass the draft to `agent-skill-reviewer`.

# Examples
- Positive: Use this template to draft a focused skill with concise positive and negative examples in `SKILL.md`.
- Negative: Use this template as if it could approve or review a finished skill.

# Outputs
- a copyable skill folder shape
- a `SKILL.md` skeleton
- a minimal companion file set
- a `review-ready` draft target

# Boundaries
- Do not use this as a broad catch-all skill.
- Do not remove the explicit trigger section.
- Do not depend on repository-global reference files when a local file will do.
- Do not claim `approved` or `stable`.

# Local references
- `template.md`: copyable folder and section skeleton
- `folder-contract.md`: required core and optional role rules
- `reference.md`: lifecycle, split signals, promotion rules, and example depth rules
