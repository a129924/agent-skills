# Workflow Recovery Alignment — Requirements

## Status

- **Status**: frozen for implementation planning
- **Topic**: `workflow-recovery-alignment`
- **Scope**: bounded workflow-contract recovery for existing Markdown-first
  migration process documents
- **Target repository**: `agent-skills`

## Problem Statement

The repository now has the requested Markdown-first migration workflow
documents under `docs/process/`, but the first implementation path drifted from
the intended workflow discipline.

The missing contract is not a new workflow architecture. The missing contract
is a repo-visible recovery topic that:

1. records the workflow recovery intent before further edits,
2. keeps work out of repo-root `dev`,
3. applies only reviewer-bounded documentation patches, and
4. closes through independent review rather than Main Agent self-approval.

## Evidence Read

The recovery baseline used these existing repository artifacts:

- `plan/agent-handoff-workflow.md`
- `skills/plan-creator/SKILL.md`
- `skills/plan-creator/checklist.md`
- `skills/plan-reviewer/SKILL.md`
- `skills/plan-reviewer/checklist.md`
- `.github/skills/worktree-manager/SKILL.md`
- `.github/skills/git-branch-naming/SKILL.md`
- `docs/process/policies/migration-workflow-common-policy.md`
- `docs/process/overlays/agent-skills-transition-overlay.md`
- `docs/process/workflows/topic-bootstrap.workflow.md`
- `docs/process/workflows/migration-implementation.workflow.md`
- `docs/process/workflows/pr-comment-correction.workflow.md`
- `docs/process/workflows/release-cleanup.workflow.md`

## Actors and Boundaries

| Actor | Role | Boundary |
| --- | --- | --- |
| Planner | Owns topic intent, scope freeze, and execution contract | Must not skip repo-visible requirements and topic plan artifacts |
| Worktree role | Owns worktree routing and lifecycle handling | Must not absorb planning or reviewer approval |
| Creator / correction role | Applies bounded documentation patches | Must not redefine topic scope or self-approve the result |
| Reviewer | Produces independent contract verdicts | Must not implement the documentation patch directly |
| Main Agent | Orchestrates the recovery flow | Must not collapse reviewer or worktree roles into itself |

## Measurable Requirements

### R1. Recovery must become a repo-visible topic before further implementation

| Element | Requirement |
| --- | --- |
| Actor | Planner |
| Condition | A workflow recovery changes repo-visible workflow documents after prior execution drift |
| Observable result | The repository contains `analysis/workflow-recovery-alignment/requirements.md` and `plan/workflow-recovery-alignment/workflow-recovery-alignment.plan.md` before further bounded workflow patching continues |
| Metric / decision rule | Hidden chat intent alone is insufficient; recovery must have named repo-visible planning artifacts |
| Failure meaning | Later reviewers cannot tell whether the implementation followed a frozen contract or another implicit rewrite |

### R2. Recovery work must not keep repo-root `dev` dirty

| Element | Requirement |
| --- | --- |
| Actor | Worktree role |
| Condition | Recovery work starts on repo-root `dev` with uncommitted documentation changes |
| Observable result | Recovery changes are moved into a dedicated external worktree and repo-root `dev` returns to a clean state |
| Metric / decision rule | `git status --short` on repo-root `dev` is empty after rescue; active recovery changes live only in the dedicated recovery worktree |
| Failure meaning | Other worktree branches cannot be merged or managed cleanly because `dev` remains blocked by unrelated recovery work |

### R3. Recovery implementation must stay bounded to declared documentation patches

| Element | Requirement |
| --- | --- |
| Actor | Creator / correction role |
| Condition | Reviewer has already identified specific workflow-document gaps |
| Observable result | Only the declared workflow and policy files are updated, and each patch maps to a named reviewer request or an explicit optional patch accepted into this topic |
| Metric / decision rule | No new systems, no `.codex/skills`, no runner, no installer/platform adapter design, and no broad workflow redesign are introduced |
| Failure meaning | The recovery topic becomes another hidden redesign instead of a bounded repair |

### R4. Independent review gates must remain explicit

| Element | Requirement |
| --- | --- |
| Actor | Reviewer + Main Agent |
| Condition | Recovery plan or implementation reaches a gate requiring approval |
| Observable result | Review is performed by an independent reviewer role, and Main Agent only records or routes the verdict |
| Metric / decision rule | Main Agent must not self-approve plan readiness or implementation correctness |
| Failure meaning | The original workflow mismatch remains unresolved procedurally even if wording improves |

### R5. Common policy must preserve bounded role authority

| Element | Requirement |
| --- | --- |
| Actor | Workflow / governance maintainer |
| Condition | Generic migration workflow policy is used by bounded execution roles |
| Observable result | Common policy states that Planner owns workflow decision/scope authority and bounded executor/checker roles must stop when inputs, scope, or policy are invalid |
| Metric / decision rule | Implementer, creator, reviewer, and checker roles cannot select topics, change approved plans, expand scope, or redefine repository policy |
| Failure meaning | A bounded role can silently become a second planner during execution |

### R6. Workflow documents must encode optional branches explicitly enough for agents

| Element | Requirement |
| --- | --- |
| Actor | Creator / correction role |
| Condition | A workflow can branch based on overlay gates, no-correction routing, optional release actions, or existing-valid-worktree reuse |
| Observable result | The relevant workflow states, steps, outputs, stop rules, or acceptance checks make those branches explicit |
| Metric / decision rule | An agent reading only the workflow file can locate the branch point and tell whether the path is required, optional, or skippable |
| Failure meaning | Agents misread edge cases and either force unnecessary actions or skip required checks |

### R7. Common status fields must remain stable across workflow-specific extensions

| Element | Requirement |
| --- | --- |
| Actor | Workflow / governance maintainer |
| Condition | A workflow-specific file needs extra `status.json` fields beyond the common contract |
| Observable result | Workflow-specific files may add fields, but do not remove or rename the required common fields |
| Metric / decision rule | The common required field names remain stable while allowing additive workflow-local extension |
| Failure meaning | Shared tooling cannot rely on a stable minimal status contract across workflows |

### R8. Optional release follow-up paths must be visible in state tracking

| Element | Requirement |
| --- | --- |
| Actor | Creator / correction role |
| Condition | Release-cleanup actions such as version update, docs update, or tagging are conditional rather than always required |
| Observable result | The workflow state model or equivalent acceptance signals make skipped optional actions explicitly observable |
| Metric / decision rule | A reviewer or status consumer can distinguish `completed when required` from `explicitly skipped` for optional release follow-up actions |
| Failure meaning | Agents or tooling can misread a skipped optional action as missing execution rather than a deliberate conditional path |

## Required Outcomes

This recovery topic is successful when:

1. repo-visible requirements and plan artifacts exist for the recovery topic;
2. the work remains in a dedicated recovery worktree and repo-root `dev` stays
   clean;
3. `migration-workflow-common-policy.md` explicitly defines bounded role
   authority;
4. the four workflow files encode the reviewer-requested optional branches
   clearly enough for future execution;
5. common status fields remain stable even when workflow-specific extensions are
   added;
6. optional release follow-up actions can be observed as completed or skipped;
7. an independent plan review and an independent implementation review both
   pass without Main Agent self-approval.

## Non-goals

- Do not add `.codex/skills` implementation.
- Do not add an executable runner.
- Do not add installer or platform adapter design.
- Do not rewrite the entire workflow system.
- Do not change `README.md` or `VERSION`.
- Do not move recovery work back onto repo-root `dev`.

## Surfaced Contradictions and Resolutions

| Contradiction | Conflict | Resolution |
| --- | --- | --- |
| The Markdown-first workflow documents already exist, but the user says workflow alignment is still missing | Existing files can look complete while still lacking repo-visible recovery planning artifacts | Treat planning artifacts as missing contract, not as optional process commentary |
| Recovery should be bounded, but reviewer comments still request additional small patches | Each patch could snowball into a redesign | Limit implementation to named reviewer patches plus the optional `Role Execution Model` policy patch accepted into this topic |
| Worktree-first routing was required, but work started on repo-root `dev` | Keeping recovery on `dev` blocks other merge work | Rescue changes into a dedicated external worktree before continuing |

## Extreme-boundary Checks

| Boundary | Requirement result |
| --- | --- |
| Missing topic plan | Must stop and create repo-visible planning artifacts before further bounded implementation |
| Dirty repo-root `dev` | Must rescue work out of `dev` before continued execution |
| Independent review unavailable | Must stop instead of treating Main Agent inspection as approval |
| Optional branch in workflow not explicit | Must patch the workflow file rather than rely on hidden operator memory |

## Success Signals

This topic is complete when:

1. the recovery topic has repo-visible requirements and plan artifacts;
2. repo-root `dev` is clean and recovery work lives in the dedicated worktree;
3. the bounded documentation patches are applied only to declared files;
4. plan review and implementation review both return independent approval; and
5. the resulting workflow set is aligned enough for later execution without
   hidden process assumptions.
