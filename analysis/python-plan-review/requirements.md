# python-plan-review

## Goal

Freeze a repo-visible migration contract for the single-skill canonical backfill
topic `python-plan-review` so implementation can validate and, if needed,
repair the canonical `skills/` copy without changing the transition-era active
workflow path.

## Required outcomes

| ID | Requirement | Acceptance signal |
| --- | --- | --- |
| R1 | Canonical `skills/python-plan-review/` exists with the full skill file set required by the current `.github/skills/python-plan-review/` source | `skills/python-plan-review/SKILL.md`, `examples.md`, and `checklist.md` exist |
| R2 | Canonical content remains parity-aligned with `.github/skills/python-plan-review/` for this topic | `diff -rq skills/python-plan-review .github/skills/python-plan-review` is empty after allowed exclusions |
| R3 | The topic does not declare active-path cutover | Topic artifacts state that `.github/skills/` remains the current authored/reviewed path during transition |
| R4 | The topic does not widen into neighboring review skills or workflow governance | No edits outside `skills/python-plan-review/`, topic artifacts, and workflow-run artifacts are required |
| R5 | The topic remains a single-topic migration unit | Publish, review, and later cleanup artifacts refer only to `python-plan-review` |

## In scope

- repo-visible planning artifacts for the `python-plan-review` migration topic
- canonical `skills/python-plan-review/` parity validation against the current
  `.github/skills/python-plan-review/` source
- bounded repair inside `skills/python-plan-review/` only if parity drift is
  found during implementation

## Out of scope

- active-path cutover from `.github/skills/` to `skills/`
- edits to `.github/skills/python-plan-review/`
- edits to `python-code-review`, `python-implementation-review`, or other
  neighboring skills
- workflow-governance changes under `docs/process/workflows/`
- publish, PR, merge, or release execution for this topic

## Evidence sources

- `.github/skills/python-plan-review/SKILL.md`
- `.github/skills/python-plan-review/checklist.md`
- `.github/skills/python-plan-review/examples.md`
- `skills/python-plan-review/`
- `docs/repo-positioning.md`
- `docs/process/workflows/topic-bootstrap.workflow.md`
- `docs/process/workflows/migration-implementation.workflow.md`

## Stop conditions

- If `python-plan-review` requires edits outside the single-topic write set,
  stop and repair the topic plan before implementation continues.
- If the canonical file set cannot reach parity without modifying the current
  `.github/skills/python-plan-review/` source, stop and re-plan instead of
  widening scope silently.
- If the topic starts implying active-path cutover, stop and route that work to
  a later transition topic.
