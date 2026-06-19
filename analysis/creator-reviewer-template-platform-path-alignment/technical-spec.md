# Technical Specification: creator-reviewer-template-platform-path-alignment

**Status**: `READY FOR EXECUTION PLANNING`  
**Topic**: `creator-reviewer-template-platform-path-alignment`  
**Source baseline**: `analysis/creator-reviewer-template-platform-path-alignment/requirements.md`

---

## Baseline Summary

The frozen baseline requires a bounded path-language correction across three
existing skill families:

- `skills/agent-skill-creator/**`
- `skills/agent-skill-reviewer/**`
- `skills/agent-skill-template/**`

The required semantic split is:

- `skills/...` remains valid only for canonical-source or authoring-only
  statements
- `.<platform>/...` becomes the default for output-facing, runnable, and
  copy-pasteable paths
- `skills/...` may appear again only as an explicitly labeled bootstrap
  fallback when the projected entrypoint does not yet exist
- concrete platform defaults such as `.codex/...` are not allowed without
  rollback to alignment

This topic is wording alignment only. It does not rematerialize `.codex/**`,
`.github/**`, or other projection surfaces, and it does not update downstream
regular skills.

---

## Translation Stance

This spec uses a pessimistic implementer posture:

- assume readers will copy the first visible path literally
- assume a mixed source/output path model will be misread unless named
  explicitly
- assume downstream consumers may try to hardcode `.codex/...` for convenience
  unless the contract forbids it
- assume any wording that conflicts with `platform-projection-adapter` will
  create later implementation churn and must therefore trigger rollback early

If implementation cannot preserve the placeholder-based projection model or must
expand into rematerialization, runtime, installer, sync, or downstream skill
changes, stop and roll back to alignment.

## Exact Implementation Write Set

Future implementation should modify only existing files inside the three scoped
skill families. No new files are required for this topic.

### Allowed to modify

- `skills/agent-skill-creator/SKILL.md`
- `skills/agent-skill-creator/blueprint.md`
- `skills/agent-skill-creator/folder-contract.md`
- `skills/agent-skill-creator/examples.md`
- `skills/agent-skill-reviewer/SKILL.md`
- `skills/agent-skill-reviewer/review-checklist.md`
- `skills/agent-skill-reviewer/examples.md`
- `skills/agent-skill-template/SKILL.md`
- `skills/agent-skill-template/template.md`
- `skills/agent-skill-template/folder-contract.md`
- `skills/agent-skill-template/reference.md`

### Read-only during implementation

- `analysis/creator-reviewer-template-platform-path-alignment/requirements.md`
- `analysis/creator-reviewer-template-platform-path-alignment/technical-spec.md`
- `analysis/platform-projection-adapter/requirements.md`
- `analysis/platform-projection-adapter/technical-spec.md`
- all downstream regular skills outside the three scoped families
- `.codex/**`
- `.github/**`
- other `.<platform>/**` surfaces

Implementation note:

- if a scoped file is re-audited and found not to contain affected path
  semantics, it may remain unchanged, but the write set must not expand beyond
  the files above.

## Requirement Traceability

| Requirement | Technical realization | Dependencies | Cost / burden | Status |
| --- | --- | --- | --- | --- |
| R1 Source-model wording stays on `skills/...` only | Rewrite source-of-truth and authoring-target text so `skills/...` is retained only in source-model / authoring-only statements | creator/template/reviewer wording audit | medium | feasible |
| R2 Output-facing wording defaults to `.<platform>/...` | Replace copy-pasteable folder shapes, commands, examples, and review targets that currently default to `skills/...` | scoped files with path examples | medium | feasible |
| R3 No concrete platform default | Remove or block any new `.codex/...`-style default and add explicit rollback guidance when a concrete platform root is demanded | platform-projection-adapter baseline | low | feasible |
| R4 Fallback is explicit and conditional | Add a named bootstrap fallback pattern tied to missing projected entrypoint conditions | source/output/fallback taxonomy | medium | feasible |
| R5 Reviewer enforces distinctions | Update reviewer process, checklist, and examples to detect conflation between source path, projection path, and fallback path | reviewer skill files | medium | feasible |
| R6 Scope stays bounded | Keep implementation limited to the three skill families and their necessary local reference files | topic-local governance | low | feasible |
| R7 Projection contract remains compatible | Cross-check all aligned wording against `platform-projection-adapter` placeholder and projection-only rules | analysis/platform-projection-adapter/* | medium | feasible |

## Required Technical Workstreams

### Workstream A - Define one path-role taxonomy

Establish a consistent three-role vocabulary across creator, reviewer, and
template artifacts:

- `canonical source` or `authoring-only` -> `skills/...`
- `output-facing` / `runnable` / `copy-pasteable` -> `.<platform>/...`
- `bootstrap fallback` -> `skills/...` only when the projected entrypoint is
  missing and the text labels it as fallback

This taxonomy must be explicit enough that a future reader can classify a path
without inferring intent from surrounding history.

### Workstream B - Align creator artifacts

Update creator materials so they no longer teach `skills/<skill-name>/` as the
default path a reader should copy into platform-facing output. Expected areas:

- `SKILL.md` process and outputs
- `blueprint.md` folder shape and creation rules
- `folder-contract.md` transition boundary language
- `examples.md` scenarios that currently treat `skills/<skill-name>/` as the
  ordinary operational destination

Creator still needs to preserve `skills/...` when the text is truly about
canonical source or authoring-only location.

### Workstream C - Align template artifacts

Update template materials so the copyable skeleton and companion guidance use
the same taxonomy. Expected areas:

- `SKILL.md` purpose/process/boundaries
- `template.md` folder tree and authoring-target wording
- `folder-contract.md` transition boundary
- `reference.md` authoring-target rule

The template must remain usable as a starting point without implying that
projection promotion or concrete-platform cutover happened inside this topic.

### Workstream D - Align reviewer artifacts

Update reviewer materials so review behavior matches the new path model instead
of preserving the older transition-only distinction. Expected areas:

- `SKILL.md` process and boundaries
- `review-checklist.md` topic-plan alignment and reject signals
- `examples.md` approved / needs-rework path scenarios

Reviewer guidance must explicitly detect:

- source-path text incorrectly used as the default runnable path
- output-facing text that hardcodes `.codex/...` or another concrete platform
  root without injected scope
- fallback text that is missing an explicit missing-entrypoint condition

### Workstream E - Add rollback instructions where semantics can fail

Implementation must add wording-level rollback instructions for at least these
cases:

- a consumer needs a concrete platform root such as `.codex/...`
- the placeholder `.<platform>/...` form is insufficient for the promised task
- the only way to keep examples truthful would be to edit `.codex/**`,
  `.github/**`, or downstream regular skills
- the requested semantics would contradict `platform-projection-adapter`

These rollback notes belong in scoped guidance and review logic, not in
projection tooling.

## Dependency and Integration Notes

- `AGENTS.md` keeps `skills/` as canonical source; this topic must not weaken
  that rule.
- `analysis/platform-projection-adapter/*` remains the governing contract for
  projection semantics.
- `skills-canonical-positioning` already froze `.<platform>/**` as compatibility
  surfaces, not canonical owners.
- No projection artifact is created, updated, or validated directly here; this
  topic only changes how creator/reviewer/template materials describe those
  paths.

## Cost-of-Realization Assessment

| Workstream | Complexity | Main burden | Ongoing operational cost |
| --- | --- | --- | --- |
| Path-role taxonomy definition | medium | preventing ambiguous mixed wording | low |
| Creator artifact alignment | medium | many authoring examples currently assume `skills/...` | low |
| Template artifact alignment | medium | folder tree and skeleton text must stay copyable | low |
| Reviewer artifact alignment | medium | checklist and examples must detect nuanced misuse | low |
| Rollback wording integration | low-to-medium | keeping rollback precise without reopening broader scope | low |

Overall effort is moderate. The main risk is semantic drift, not code
complexity.

## Architecture / Governance Compliance Self-Check

| Dimension | Result | Notes |
| --- | --- | --- |
| `skills/` remains canonical source | fits existing governance | source-model wording still points to `skills/...` only |
| `.<platform>/**` remains projection / compatibility only | fits existing governance | output-facing defaults use placeholder projection paths without re-promoting them to canonical source |
| `platform-projection-adapter` placeholder contract | fits with prerequisites | only if placeholder form stays generic and no concrete platform root becomes default |
| Bootstrap fallback rule | fits with prerequisites | only if fallback is explicitly labeled and conditioned on missing projected entrypoint |
| Concrete platform defaulting | conflicts with current architecture | `.codex/...` or similar as the default would violate frozen inputs and requires rollback |
| Scope boundary against rematerialization | fits existing governance | no `.codex/**` or `.github/**` edits are required or allowed |
| Downstream regular-skill rollout | bounded / out of scope | follow-up only; not part of this topic |

## Conflicts, Blockers, and Rollback-to-Alignment Triggers

### Current blockers

None from the current evidence set. The topic is implementable as a bounded
wording-alignment change.

### Rollback triggers

Return to alignment before implementation proceeds if any of the following
becomes true:

1. a required output-facing example cannot remain truthful unless it hardcodes a
   concrete platform root such as `.codex/...`
2. a fallback instruction cannot be expressed without effectively restoring
   `skills/...` as the ordinary operational path
3. a reviewer rule cannot enforce the new semantics without editing downstream
   regular skills or projection surfaces
4. a proposed wording change would contradict the placeholder projection or
   projection-only rules in `analysis/platform-projection-adapter/*`
5. a stakeholder requires `.codex/**` or `.github/**` rematerialization as part
   of making these three skills usable

### Conflict handling note

If implementation discovers additional path drift in downstream regular skills,
record it as follow-up inventory only. Do not silently widen this topic.

## Recommended Next Step

Author a bounded topic plan for
`creator-reviewer-template-platform-path-alignment` that encodes:

- the exact writable file set above
- the source/output/fallback taxonomy as implementation contract
- rollback gates for concrete platform defaulting and projection-contract drift
