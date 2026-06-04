# Python Blueprint Review Checklist

Use this checklist before returning a verdict for an authored greenfield
`blueprint.md`.

- [ ] The task is really blueprint-contract review, not authoring, execution, retrofit planning, or skill-folder review.
- [ ] The review stays inside the existing blueprint v1 contract already consumed by `python-project-init-greenfield`.
- [ ] The section order is exactly:
  - [ ] `## Project Overview`
  - [ ] `## Required Skills`
  - [ ] `## Toolchain Expectation`
  - [ ] `## Structural Invariants`
  - [ ] `## Quality Thresholds`
  - [ ] `## Acceptance Criteria`
- [ ] No required heading is missing, reordered, renamed, or replaced by a compatibility alias.
- [ ] `## Acceptance Criteria` starts with a parseable fenced `yaml [sensing-assertions]` block.
- [ ] No prose appears before that fenced block.
- [ ] Every sensing assertion includes `kind`, `target`, and `expected`.
- [ ] Every sensing assertion `kind` is one of: `path_exists`, `path_type`, `command_available`; unsupported kinds were treated as blocking issues.
- [ ] Every named required skill resolves to `skills/<skill-name>/SKILL.md` using the exact authored name.
- [ ] No skill name was normalized for case, `_`, or `-`.
- [ ] Abstract, contradictory, or non-locatable `Structural Invariants` were treated as blocking issues.
- [ ] Greenfield-only lane fit is still true; migration, preservation, or retrofit pressure was not silently absorbed.
- [ ] The verdict reports blocking issues instead of rewriting the blueprint on the reviewer's behalf.
- [ ] The final output is exactly one JSON object using the local verdict contract.
