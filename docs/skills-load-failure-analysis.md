# Skills load failure analysis

## Conclusion

`docs/repo-positioning.md` is **not the same problem** as the two failing skill
files.

The failures in:

- `.github/skills/python-plan-authoring/SKILL.md`
- `.github/skills/python-tdd-test-authoring/SKILL.md`

were caused by **invalid YAML frontmatter** inside `SKILL.md`.

`docs/repo-positioning.md` is a normal Markdown governance document. It has:

- no YAML frontmatter
- no `name` / `description` skill manifest fields
- no placement under `.github/skills/<skill>/SKILL.md`

So it is not a skill manifest parse failure of the same kind.

## Why they are different

### 1. The two failing skill files

These files are loaded as skill manifests. Their frontmatter must be valid YAML.

The broken pattern was:

```yaml
- D1 structured verdict when available: `{ "verdict": "trivial|non-trivial", "reason": "..." }`
```

and:

```yaml
- D1 structured verdict: `{ "verdict": "trivial|non-trivial", "reason": "..." }`
```

In YAML, the `:` inside an unquoted list item is interpreted as a mapping
separator. Because the value that followed was backtick-delimited text rather
than a valid YAML scalar, the parser failed.

### 2. `docs/repo-positioning.md`

This file is referenced as repository guidance by:

- `AGENTS.md`
- `README.md`
- `.github/copilot-instructions.md`

It is documentation, not a skill manifest. Its role is to define repository
positioning, current state, and migration boundaries.

That means:

- if this file is merely being read as documentation, there is no YAML issue
- if some loader tries to treat this file as a skill, the bug is **discovery
  scope / classification**, not Markdown syntax

## How to solve each case

### Case A: broken `SKILL.md` frontmatter

Fix the YAML itself.

For this repository, the safe fix is to quote the entire list item string:

```yaml
- 'D1 structured verdict when available: `{ "verdict": "trivial|non-trivial", "reason": "..." }`'
```

and:

```yaml
- 'D1 structured verdict: `{ "verdict": "trivial|non-trivial", "reason": "..." }`'
```

This preserves the text while making the frontmatter valid YAML.

### Case B: `docs/repo-positioning.md` is being treated like a skill

Fix the loader or discovery rule.

The loader should only treat files as skills when they match the skill-manifest
path contract, for example:

```text
.github/skills/<skill-name>/SKILL.md
```

or, after migration:

```text
skills/<skill-name>/SKILL.md
```

It should **not** scan generic documentation paths such as:

```text
docs/*.md
analysis/**/*.md
plan/**/*.md
```

## Practical resolution checklist

1. Keep `docs/repo-positioning.md` as plain Markdown documentation.
2. Validate skill loading only against `SKILL.md` manifest paths.
3. If a loader currently scans all Markdown files, restrict it to skill
   directories.
4. If a skill needs repository-positioning context, reference
   `docs/repo-positioning.md` as a local or external reference in prose, not as
   a frontmatter manifest source.
