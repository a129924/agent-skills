# Creator blueprint

Use this as the default folder shape for a `review-ready` skill.

```text
.github/skills/<skill-name>/
├── SKILL.md
├── reference.md            # required unless examples.md already covers local detail
├── references/             # optional, for split topic-specific reference files
├── examples.md            # required for high-complexity skills
├── checklist.md           # optional
├── run-task.sh            # optional
└── assets/                # optional
```

- Use `reference.md` or `examples.md` as the required companion file.
- Add `references/` when one `reference.md` would exceed about 1,000 tokens or
  more than 3 logic topics.
- Add `examples.md` when the skill is high complexity or the `SKILL.md`
  examples are not enough.

## Minimum `SKILL.md` shape

```md
---
name: <skill-name>
description: <what the skill does and when to use it>
---

# Purpose
<one clear job>

# Trigger / When to use
Use this skill when:
- ...

Do not use this skill when:
- ...

# Inputs
- ...

# Process
1. ...
2. ...
3. ...

# Examples
- Positive: ...
- Negative: ...

# Outputs
- ...

# Boundaries
- ...

# Local references
- `reference.md`: stable constraints, notes, or edge cases
- `references/decision-rules.md`: topic-specific reference file when reference content is split
- `examples.md`: detailed patterns and anti-patterns for complex tasks
- `checklist.md`: repeatable verification steps (optional)
- `assets/`: local-only material used by this skill (optional)
```

## Creation rules
- Use lowercase kebab-case for `<skill-name>`.
- If responsibility, trigger, or boundaries are ambiguous, ask before drafting.
- Keep the skill single-purpose.
- Keep supporting material in the same folder.
- Split oversized reference material into `references/` by topic.
- Put concise positive and negative examples in `SKILL.md`.
- Add `examples.md` when the skill is high complexity or the brief examples are not enough for about 80% of routine usage.
- Add optional files or folders only when each one has a clear role.
- Stop at `review-ready`.
- Tell the user when the draft is `review-ready`, then let a human or external workflow send it to `agent-skill-reviewer`.
