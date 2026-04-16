# Reviewer examples

## Approved example

A folder with:
- `SKILL.md`
- `examples.md`
- one clear trigger family
- concise positive and negative examples in `SKILL.md`
- a narrow output pattern

Typical verdict:
- approved

## Needs-rework example

A folder whose `SKILL.md` says it can "create, review, refactor, and publish any
skill" with no negative example and no `examples.md` for the refactor paths.

Typical verdict:
- needs-rework

Typical reasons:
- more than one responsibility
- trigger is too broad
- missing required example depth

## Needs-rework example: oversized reference file

A folder with one `reference.md` that mixes multiple rule systems, exceptions,
and decision tables without splitting them into `references/`.

Typical verdict:
- needs-rework

Typical reasons:
- `reference.md` is too broad
- split reference files are needed
- local reference roles are not explicit enough
