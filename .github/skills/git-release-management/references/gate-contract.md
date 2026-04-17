# Release gate contract

A release or PR is green only when all required signals are present.

## Hard conditions

- at least one reviewer approval, unless the emergency path explicitly bypasses only reviewer timing
- CI green
- base tests passing
- strict type checks passing
- lint passing
- relevant documentation updated
- versions synchronized across existing release sources
- clean workspace

## Skill-signature rule

Treat upstream skills as explicit gate signals.

- `python-testing-pytest`: PASS means test expectations are satisfied for release gating
- `python-type-hints-strict`: PASS means strict typing is satisfied for release gating

Do not substitute intuition or partial logs for those outcomes when the workflow already exposes them.

## Failure reporting

When the gate fails, name each failed condition directly and give the shortest useful repair path.
