# python-async-planning technical specification

Status: READY for topic-plan authoring
Topic: `python-async-planning`
Primary path: `analysis/python-async-planning/technical-spec.md`
Source baseline: `analysis/python-async-planning/requirements.md`
Traceability base: generated in `feat/andrew/python-async-planning-spec` from `dev@77fa194`

## Source baseline summary

The business baseline requires a reusable Python-specific planning control point
that prevents async-capable topics from reaching implementation without a frozen
async decision baseline. The required behavior is:

- detect async-capable evidence consistently
- avoid false-positive routing for syntax-only or non-architectural work
- require named async-planning sections for async-capable plans
- use both plan and review as evidence
- surface contradictions explicitly
- require minimal retrofit when async risk is discovered late
- keep the result portable across general Python async I/O planning

## Requirement traceability

| Requirement | Technical realization | Dependencies | Cost / burden | Status |
| --- | --- | --- | --- | --- |
| BR-1 Trigger async planning when async-capable evidence is present | Create `.github/skills/python-async-planning/SKILL.md` with an explicit trigger section and trigger-evidence table; update `python-plan-authoring` routing text to invoke the new skill when trigger evidence is present; update `python-plan-review` to recognize the same trigger evidence during review | New skill folder; edits to existing planning and review skills | Medium: cross-skill consistency work and wording precision are required | feasible |
| BR-2 Do not over-trigger on syntax-only or non-architectural work | Encode exemption list inside the new skill and in reviewer gating guidance; ensure examples show both trigger and non-trigger cases | `python-async-planning/examples.md`; `python-plan-review/examples.md`; `python-plan-review/checklist.md` | Medium: false-positive control requires careful examples and reviewer wording | feasible |
| BR-3 Freeze a named async decision baseline for async-capable topics | Define the required async-planning output sections in the new skill; update `python-plan-authoring` examples and template guidance so those sections are required when async-capable evidence exists | New skill contract; edits to plan-authoring guidance | Medium: multiple files must agree on the exact section names | feasible |
| BR-4 Use both plan and review as evidence | In the topic plan and reviewer guidance, require plan baseline plus reviewer conformance check; prohibit silent reviewer override of plan decisions | `python-plan-review/SKILL.md`; topic plan contract; contradiction-log guidance | Medium: contract wording must separate review from silent plan mutation | feasible |
| BR-5 Record contradictions instead of smoothing them over | Add a contradiction-log requirement to the new skill and reviewer behavior; provide examples where plan, review, and implementation disagree | `python-async-planning/SKILL.md`; `reference.md`; `examples.md`; reviewer examples | Low-to-medium: mostly documentation consistency, but high misuse risk if omitted | feasible |
| BR-6 Require minimal retrofit when async risk is discovered late | Add `retrofit required` handling to reviewer guidance and examples; require minimal backfill set instead of full re-plan for already-started work | `python-plan-review/SKILL.md`; `checklist.md`; `examples.md` | Medium: must avoid both silent continuation and uncontrolled scope expansion | feasible |
| BR-7 Keep the skill portable across Python async I/O planning | Keep core rules framework-neutral; use FastAPI/SQLAlchemy/httpx only in examples; explicitly protect domain layers from infra async leakage | New skill core files and examples | Low-to-medium: mostly a scope-discipline requirement | feasible |

## Required technical tasks and artifacts

### Workstream A — New skill artifact

Create `.github/skills/python-async-planning/` with at least:

- `SKILL.md`
- `reference.md`
- `examples.md`

Expected content:

- trigger evidence rule
- exemption list
- required async-planning output sections
- contradiction-log contract
- minimal retrofit rule
- portability boundary
- PASS / SOFT FAIL / BLOCKED validation guidance

Optional artifact:

- `checklist.md` only if draft review shows misuse-prevention remains too weak without it

### Workstream B — Planning-surface routing

Update `.github/skills/python-plan-authoring/` so async-capable topics are routed
to `python-async-planning` and so plan-authoring examples or prompts reference
the named async-planning sections when the trigger evidence exists.

Likely artifacts:

- `.github/skills/python-plan-authoring/SKILL.md`
- `.github/skills/python-plan-authoring/templates/python-plan-template.md`
- `.github/skills/python-plan-authoring/examples.md`

### Workstream C — Review-surface enforcement

Update `.github/skills/python-plan-review/` so reviewer logic:

- detects async-capable evidence
- requires async-planning coverage for triggered topics
- records contradictions rather than silently overriding the plan
- uses `retrofit required` when async risk is discovered late in an existing plan

Likely artifacts:

- `.github/skills/python-plan-review/SKILL.md`
- `.github/skills/python-plan-review/checklist.md`
- `.github/skills/python-plan-review/examples.md`

### Workstream D — Optional discoverability cross-link

Only if creator review shows discoverability is still weak, add a small
cross-reference in:

- `.github/skills/python-async-await/SKILL.md`, or
- `.github/skills/python-async-await/reference.md`

This is explicitly optional and must not broaden `python-async-await` into a
planning skill.

### Workstream E — Stable-library surfaces

If the topic reaches approved stable state within this topic lifecycle:

- update `README.md` to add `python-async-planning` to `## Current skills`
- bump `VERSION` by MINOR

Timing: `publish-in-progress`, not post-merge release.

## Dependency and integration notes

- The new skill must remain consistent with existing repository governance on:
  - skill folder shape
  - medium/high complexity rules
  - reviewer separation from creator
  - exact artifact-path declarations
- The routing logic must not rely on hidden chat memory; the trigger must be
  explainable from repo-visible artifacts and reviewer-observable evidence.
- Multiple shared planning/governance files are touched, so worktree isolation
  remains required to keep branch intent clean.

## Cost-of-realization assessment

| Workstream | Complexity | Sequencing pressure | Operational / maintenance burden |
| --- | --- | --- | --- |
| New skill artifact | Medium | Must happen before routing copy can be finalized | Ongoing maintenance of one new stable skill |
| Planning-surface routing | Medium | Depends on the new skill's frozen section names | Moderate wording maintenance across planning guidance |
| Review-surface enforcement | Medium | Depends on the same trigger and section names as authoring | Moderate: reviewer drift risk if examples/checklist are incomplete |
| Optional async-await cross-link | Low | Defer until draft clarity is known | Low |
| Stable-library updates | Low | Only after reviewer approval and before publish completion | Low but workflow-sensitive |

## Architecture-compliance self-check

| Dimension | Result | Notes |
| --- | --- | --- |
| Repository positioning and skill path model | fits existing architecture | The topic stays under `.github/skills/` during the transition period |
| Skill responsibility boundary | fits with prerequisites | New skill remains planning-stage only and does not replace implementation-focused async guidance |
| Creator / reviewer separation | fits with prerequisites | Topic must stop at review-ready until `agent-skill-reviewer` issues a verdict |
| Stable-library handling | fits with prerequisites | README and VERSION changes occur only if approved stable promotion is reached |
| Dependency direction and layer hygiene | fits existing architecture | The skill explicitly protects domain layers from infra async leakage rather than encouraging it |
| External tooling | fits existing architecture | No new runtime dependency is required; only repository documentation and workflow artifacts change |

## Conflicts, blockers, and rollback-to-alignment triggers

### Current blockers

None. The baseline is translatable with the current repository constraints.

### Rollback triggers

Return to business alignment before creator implementation proceeds if any of
the following becomes true:

1. The trigger evidence rule cannot be stated precisely enough to distinguish
   real async-capable work from syntax-only questions.
2. Reviewer enforcement cannot support `retrofit required` without either
   silently passing missing async decisions or forcing full re-plan on minor
   late discoveries.
3. Portability cannot be preserved without making FastAPI, SQLAlchemy, or
   DDD-style layering an implicit requirement.
4. Stable-library timing would require README/VERSION behavior that conflicts
   with the repository's publish-versus-release workflow.

### Conflict handling note

If creator output later contradicts the analysis baseline, the contradiction
must be surfaced explicitly in the topic plan or review path rather than silently
rewriting the baseline.

## Recommended next step

Author `plan/python-async-planning/python-async-planning.plan.md` in strict mode,
mapping the topic plan 100% to this technical specification and using
`analysis/python-async-planning/requirements.md` as the business guardrail.
