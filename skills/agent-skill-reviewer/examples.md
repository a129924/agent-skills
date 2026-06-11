# Reviewer examples

## Approved example: lightweight skill stays lightweight

A folder with:
- `SKILL.md`
- `reference.md`
- one clear trigger family
- concise positive and negative examples in `SKILL.md`
- a narrow output pattern
- no unnecessary heavyweight validation copied from a release or reviewer skill

Typical verdict:
- approved

## Approved example: transition mirror review stays a mirror review

A transition-scope review where:
- canonical authoring intent points to `skills/<skill-name>/`
- a `.<platform>/skills/...` artifact is reviewed only because context or
  prompt explicitly injects that transition mirror / projection surface
- the reviewed text does not claim `.<platform>/skills/` is the canonical
  source

Typical verdict:
- approved

Typical reasons:
- reviewer distinguishes canonical source from mirror/projection semantics
- reviewer does not assume a concrete platform surface unless it was explicitly
  put in scope
- transition wording preserves the current active path without collapsing source
  of truth

## Approved example: higher-risk skill has stronger guardrails

A folder with:
- `SKILL.md`
- `examples.md`
- `checklist.md`
- a gatekeeping or higher-risk responsibility
- concise positive and negative examples in `SKILL.md`
- explicit verification or equivalent misuse-prevention guidance

Typical verdict:
- approved

Typical reasons:
- validation weight matches downstream impact
- reviewer can see how ambiguity and misuse are handled

## Needs-rework example

A folder whose `SKILL.md` says it can "create, review, refactor, and publish any
skill" with no negative example and no `examples.md` for the refactor paths.

Typical verdict:
- needs-rework

Typical reasons:
- more than one responsibility
- trigger is too broad
- missing required example depth

## Needs-rework example: higher-risk skill with weak validation

A folder for release or reviewer gating that has only a bare `SKILL.md`, no
stronger misuse-prevention guidance, and no local material that explains how to
verify or safely route ambiguous cases.

Typical verdict:
- needs-rework

Typical reasons:
- validation weight is too weak for the risk
- higher-risk behavior is easy to misuse
- reviewer cannot see enough evidence that the gate is safe

## Needs-rework example: oversized reference file

A folder with one `reference.md` that mixes multiple rule systems, exceptions,
and decision tables without splitting them into `references/`.

Typical verdict:
- needs-rework

Typical reasons:
- `reference.md` is too broad
- split reference files are needed
- local reference roles are not explicit enough

## Needs-rework example: mirror review collapses source of truth

A transition-scope review where a `.<platform>/skills/...` artifact says it is
both the current mirror and the canonical source of truth for new authoring
work.

Typical verdict:
- needs-rework

Typical reasons:
- canonical source and mirror/projection roles are conflated
- the review would silently re-promote `.<platform>/skills/` as the only source
  of truth
