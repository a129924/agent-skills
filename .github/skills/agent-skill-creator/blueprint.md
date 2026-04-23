# Creator blueprint

Use this as the default folder shape for a `review-ready` skill.

```text
.github/skills/<skill-name>/
├── SKILL.md
├── reference.md            # required unless examples.md already covers local detail
├── references/             # optional, for split topic-specific reference files
├── examples.md            # required for high-complexity or clearly higher-risk skills
├── checklist.md           # optional, useful for repeatable higher-risk validation
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
- Add stronger validation guidance only when the skill's risk warrants it.

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

# Verification
- ...                       <!-- optional for higher-risk or easier-to-misuse skills -->

# Red Flags
- ...                       <!-- optional for higher-risk skills -->

# Common Rationalizations
- ...                       <!-- optional for higher-risk skills -->

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
- Classify validation weight before drafting: lightweight, medium-complexity, or higher-risk.
- Keep the skill single-purpose.
- Keep supporting material in the same folder.
- Split oversized reference material into `references/` by topic.
- If `reference.md` is the chosen companion file and becomes too broad, keep it
  focused or reduce it to a short overview while moving detailed topics into
  `references/`.
- Put concise positive and negative examples in `SKILL.md`.
- Add `examples.md` when the skill is high complexity or the brief examples are not enough for about 80% of routine usage.
- Add stronger validation signals only when risk, branching, tooling, or downstream impact justify them.
- Add optional files or folders only when each one has a clear role.
- Stop at `review-ready`.
- Tell the user when the draft is `review-ready`, then let a human or external workflow send it to `agent-skill-reviewer`.
