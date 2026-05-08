# worktree-skill technical specification

Status: READY FOR PLAN AUTHORING
Topic: `worktree-skill`
Source baseline: `analysis/worktree-skill/requirements.md`
Target skill: `.github/skills/worktree-manager/`

## Source baseline summary

The frozen business baseline requires a single-purpose skill that manages
worktree lifecycle operations for agent-driven work without silently destroying
state. The skill must create managed worktrees at a canonical external path,
inspect worktree state with a recommendation matrix, release worktrees without
implying deletion, and separate destructive remove flows behind explicit human
approval and safety gates.

## Requirement traceability

| Requirement | Technical realization | Dependencies | Cost / burden | Status |
| --- | --- | --- | --- | --- |
| R1 Create managed worktree | Encode canonical path rule, branch-creation path, and next-step output contract in `SKILL.md`; add create examples and checklist gating | Git CLI, repo path detection, branch naming policy | Medium: path validation, branch-collision handling, and cross-worktree state checks | feasible |
| R2 Inspect worktrees with structured recommendation | Define a fixed inspect output contract and recommendation matrix in `SKILL.md`; reinforce with `examples.md` and checklist items | `git worktree list`, per-worktree status inspection, selector resolution | Medium: multi-state branching and reasoned output formatting | feasible |
| R3 Release without deletion | Define release evidence schema, release-only trigger vocabulary, and non-destructive default in `SKILL.md`; add release checklist | Git state inspection, PR/branch state interpretation, human intent capture | Medium: evidence normalization and ambiguity handling | feasible |
| R4 Remove only after explicit destructive gate | Keep remove path separate in `SKILL.md` and checklist; require explicit human approval and safe-state checks before any destructive action | Human confirmation, worktree status checks, Git remove behavior | Medium: destructive-path safeguards and failure handling | feasible |
| R5 Managed / unmanaged path-based ownership | Treat canonical path family as the v1 managed boundary; put unmanaged inspect-only rule in `SKILL.md` and examples | Canonical path comparison | Low: simple rule, high safety value | feasible |
| R6 Block non-repo invocation | Require repo-root validation before create / inspect / release / remove; describe blocked behavior in `SKILL.md` | Git repo detection | Low | feasible |
| R7 Risky states escalate to `needs-human-decision` | Encode dirty, untracked, unpushed, detached, locked, and unknown-state routing in recommendation matrix and checklist | Git status inspection, branch / HEAD checks | Medium | feasible |
| R8 Shared-file coordination warning | Add planner / observer coordination boundary language in `SKILL.md`, examples, and checklist | Human workflow contract only; no automation required | Low | feasible |
| R9 Branch collision requires reuse-or-rename decision | Encode branch conflict as a stop-and-ask path in `SKILL.md`; add example and checklist item | Branch lookup, human decision | Low to medium | feasible |
| R10 Stale registration becomes `prune-candidate` | Treat missing-path-but-registered worktrees as inspect output only; do not auto-prune | `git worktree list`, path existence check | Low | feasible |

## Required technical artifacts

| Artifact | Path | Purpose |
| --- | --- | --- |
| Business baseline | `analysis/worktree-skill/requirements.md` | Frozen measurable baseline for the topic |
| Technical baseline | `analysis/worktree-skill/technical-spec.md` | Execution-facing technical source of truth |
| Topic plan | `plan/worktree-skill/worktree-skill.plan.md` | Repo-visible execution contract |
| Skill contract | `.github/skills/worktree-manager/SKILL.md` | Primary lifecycle instructions and safety gates |
| Skill examples | `.github/skills/worktree-manager/examples.md` | Positive, negative, and exception-path examples |
| Skill checklist | `.github/skills/worktree-manager/checklist.md` | Repeatable create / release / remove / unmanaged verification gates |
| Skill reference | `.github/skills/worktree-manager/reference.md` | Stable local detail such as selectors, evidence fields, and managed-path policy |

## Technical tasks and sequencing

1. Author the frozen analysis artifacts (`requirements.md`, `technical-spec.md`)
   and keep them repo-visible before creator work begins.
2. Author `plan/worktree-skill/worktree-skill.plan.md` in strict mode, mapping
   all plan steps to this technical specification.
3. Draft `.github/skills/worktree-manager/SKILL.md` so it captures:
   - create / get / release / remove vocabulary
   - canonical managed path rule
   - release evidence schema
   - recommendation matrix summary
   - managed / unmanaged routing
   - blocked and `needs-human-decision` behavior
4. Draft `.github/skills/worktree-manager/examples.md` with concrete scenarios
   for clean, dirty, unmanaged, and destructive-confirmation paths.
5. Draft `.github/skills/worktree-manager/checklist.md` with:
   - pre-create checks
   - pre-release checks
   - pre-remove checks
   - unmanaged-worktree checks
6. Draft `.github/skills/worktree-manager/reference.md` for stable operational
   detail that would make `SKILL.md` too dense.
7. Send the skill folder to `agent-skill-reviewer` after creator work reaches
   `review-ready`.

## Automation decision

v1 stays instruction-first.

- No destructive automation script is part of the initial artifact set.
- If later evidence shows instruction-only inspect output is too unstable, the
  only script family eligible for a plan repair is a read-only status helper
  such as `.github/skills/worktree-manager/scripts/worktree_status.py`.
- Any script addition requires plan repair because it would widen the artifact
  path contract.

## Dependency and integration notes

- Git CLI is the only required external tool family.
- The skill depends on repository-relative path detection and correct repo-root
  discovery.
- Branch naming should follow existing repo conventions, but the worktree skill
  must not own generic branch policy beyond its immediate create path.
- Release evidence may rely on Git branch state, PR state known from the user,
  and explicit human intent; it must not invent external confirmation signals.

## Cost-of-realization assessment

| Workstream | Complexity | Main burden | Ongoing operational cost |
| --- | --- | --- | --- |
| Analysis artifacts | Low | converting resolved chat decisions into frozen repo-visible files | minimal |
| SKILL.md contract authoring | Medium | encoding lifecycle distinctions and blocked paths without over-broad scope | low |
| Recommendation matrix and examples | Medium | keeping branching behavior explicit and testable by another agent | low |
| Checklist design | Medium | making destructive-path checks repeatable without duplicating the entire skill body | low |
| Optional script path | Deferred | not part of v1 unless instruction-only execution proves insufficient | deferred |

## Architecture-compliance self-check

| Dimension | Result | Notes |
| --- | --- | --- |
| Repository boundaries | fits existing architecture | topic is analysis + plan + future single skill folder under `.github/skills/` |
| Single responsibility | fits with prerequisites | remains valid if the skill stays focused on worktree lifecycle and does not absorb merge/release policy |
| Stable-library surfaces | fits existing architecture | `README.md` and `VERSION` stay out of scope for this topic |
| Destructive-path handling | fits with prerequisites | requires checklist-backed gates and explicit human confirmation |
| Optional automation | fits existing architecture | only if kept local to the skill and widened through plan repair |
| Role boundaries | fits existing architecture | planning actor, creator, reviewer, and later observer roles remain distinct |

## Conflicts, blockers, and rollback triggers

No current blocker prevents plan authoring, but creator work must roll back to
alignment if any of the following becomes true:

1. The skill cannot keep `release` and `remove` meaningfully separate without
   inventing unstated policy.
2. Path-policy-only ownership proves too weak to distinguish managed from
   unmanaged worktrees for safe routing.
3. Instruction-only execution cannot express inspect output and safety gates
   reliably enough, and a script path becomes necessary without plan repair.
4. The four lifecycle operations together force the skill beyond a single
   trigger family and require splitting into multiple skills.
5. A stable-library surface (`README.md`, `VERSION`) becomes required for the
   first implementation topic despite the current out-of-scope decision.

If any rollback trigger fires, stop creator work and return to planning instead
of improvising the missing rule inside the draft skill.

## Ready-for-plan decision

This technical specification is complete enough to drive strict-mode topic plan
authoring at `plan/worktree-skill/worktree-skill.plan.md`.
