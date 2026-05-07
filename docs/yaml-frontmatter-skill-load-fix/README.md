# YAML frontmatter skill load fix

## Summary

Three skills failed to load because their `SKILL.md` YAML frontmatter contained
list items written as unquoted plain scalars even though the values included
characters that YAML parsers treat specially.

Affected files:

- `.github/skills/business-intent-alignment/SKILL.md`
- `.github/skills/plan-reviewer/SKILL.md`
- `.github/skills/sense-env-scaffold/SKILL.md`

## Symptom

The loader reported YAML frontmatter parse failures similar to:

- `failed to parse YAML frontmatter`
- `Plain value ...`

## Root cause

Several frontmatter list values contained YAML-sensitive content such as:

- inline colon usage like `the run mode: ...`
- backtick-wrapped paths or fenced-label fragments at the start of the value

Those entries were written as plain scalars, for example:

```yaml
inputs:
  - the run mode: `discovery` (fact collection) or `acceptance` (contract assertion)
```

In YAML, a plain scalar with `:` in that position can be interpreted as a
mapping boundary instead of a literal string value, which causes parsing to fail.

## Fix applied

All affected frontmatter list items were rewritten as explicit quoted strings,
for example:

```yaml
inputs:
  - "the run mode: `discovery` (fact collection) or `acceptance` (contract assertion)"
```

The same quoting fix was applied to other frontmatter entries that contained
paths, backticks, or punctuation likely to confuse a YAML parser.

## Why this works

Quoting forces YAML to treat the whole list item as a single string literal
instead of trying to infer mapping structure from punctuation inside the value.

## Validation

After the edits, the repository's `SKILL.md` frontmatter files were parsed again
with a YAML parser and the previously failing skill files loaded cleanly.

## Prevention

When writing `SKILL.md` frontmatter:

- quote list items if the value contains `:`
- quote list items that begin with or heavily use backticks
- prefer explicit strings over YAML plain scalars for descriptive sentences
