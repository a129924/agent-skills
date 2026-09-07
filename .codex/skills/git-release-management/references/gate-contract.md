# Release gate contract

Select draft PR, merge readiness, or release/tag first. A draft may request CI and human review; it must honestly disclose pending signals, not claim release readiness. Merge uses applicable repository gates. The normal/emergency conditions below apply to release/tag.

## Normal path

The normal path is green only when all of these are true:

- at least one reviewer approval
- CI green
- base tests passing
- project-required type checks passing
- lint passing
- relevant documentation updated
- versions synchronized across existing release sources
- clean workspace
- target tag does not already exist

## Emergency path

The emergency path may bypass exactly one normal-path condition:

- missing pre-release reviewer approval

The emergency path still requires all of these:

- CI green
- base tests passing
- project-required type checks passing
- lint passing
- relevant documentation updated
- versions synchronized across existing release sources
- clean workspace
- target tag does not already exist
- explicit emergency marker
- recorded human confirmation
- release-note or equivalent anomaly record

## Skill-signature rule

Use applicable repository tooling and upstream review signals; do not impose Python skills on non-Python work or strict mode on a project that does not require it.

- `python-testing-pytest`: PASS means test expectations are satisfied for release gating
- `python-type-hints-strict`: PASS means strict typing is satisfied for release gating

Do not substitute intuition or partial logs for those outcomes when the workflow already exposes them.

## Failure reporting

When the gate fails, name each failed condition directly and give the shortest useful repair path.
