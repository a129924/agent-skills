# Canonical skill template

Use this as the default starting point for a `review-ready` skill.

```text
.github/skills/<skill-name>/
├── SKILL.md
├── reference.md            # required unless examples.md already covers local detail
├── references/             # optional, for split topic-specific reference files
├── examples.md             # required for high-complexity skills
├── checklist.md           # optional
├── run-task.sh            # optional
└── assets/                # optional
```

- Use `reference.md` or `examples.md` as the required companion file.
- Use `references/` only as a split-reference supplement, not as a replacement
  for the required companion file.
- Add `references/` when one `reference.md` would exceed about 1,000 tokens or
  more than 3 logical topics.
- Add `examples.md` when the skill is high complexity or the `SKILL.md`
  examples are not enough.

## `SKILL.md` skeleton

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
- `reference.md`: local examples, constraints, or edge cases
- `references/topic-a.md`: split reference file with one clear topic and role
- `checklist.md`: repeatable verification steps (optional)
- `assets/`: local-only material used by this skill (optional)
```

## Companion file guidance
- Use `reference.md` or `examples.md` for reusable detail.
- Split oversized reference material into `references/` when one file becomes too broad.
- If `reference.md` is the chosen companion file and becomes too broad, keep it
  focused or reduce it to a short overview while moving detailed topics into
  `references/`.
- Add `checklist.md` only when the skill has repeatable review steps.
- Keep scripts local to the skill that needs them.
- Optional files or folders must declare their role in `Local references`.
- Add `examples.md` when the skill is high complexity or when the concise
  examples in `SKILL.md` are not enough.
