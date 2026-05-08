# worktree-skill

Analysis-layer routing: **strict mode**. `analysis/worktree-skill/technical-spec.md`
is the execution-facing source of truth for this topic, and
`analysis/worktree-skill/requirements.md` remains the business-intent guardrail.
This plan maps 100% to the technical spec and does not allow chat-time scope to
silently widen the topic.

## Goal / Outcome

- Produce a review-ready `.github/skills/worktree-manager/` skill folder that
  safely manages worktree lifecycle operations for this repository's agent-driven
  workflows.
- Preserve the locked lifecycle model: create, get, release, and remove remain
  distinct operations; release is non-destructive by default; unmanaged
  worktrees remain inspect-only unless the human explicitly authorizes a
  destructive path.
- Keep the topic repo-visible and handoff-safe through analysis artifacts plus a
  strict execution plan before creator work starts.

## Scope

- **In scope**:
  - `analysis/worktree-skill/requirements.md`
  - `analysis/worktree-skill/technical-spec.md`
  - `plan/worktree-skill/worktree-skill.plan.md`
  - `.github/skills/worktree-manager/SKILL.md`
  - `.github/skills/worktree-manager/examples.md`
  - `.github/skills/worktree-manager/checklist.md`
  - `.github/skills/worktree-manager/reference.md`

- **Out of scope**:
  - `.github/skills/worktree-manager/scripts/`
  - `README.md`
  - `VERSION`
  - `.github/copilot-instructions.md`
  - repository release / tag actions
  - merge / PR workflow automation beyond worktree-state evidence and guidance
  - environment bootstrapping such as `.env.local`, port, database, or compose
    setup

## Locked Decisions

- This topic is **review-ready-only with no stable-library surfaces**.
- Managed worktrees MUST use the canonical path family:
  `../<repo-name>.worktrees/<prefix>-YYYYMMDD-<worktree-name>`.
- Default managed prefix is `agent`; an explicit human override may replace it.
- Vocabulary stays locked as `create`, `get-worktree`, `release worktree`, and
  `remove worktree`.
- `release worktree` means safe offboarding from the active working set and MUST
  NOT imply deletion.
- `remove worktree` is the only destructive directory / registration removal
  path and requires a separate explicit destructive-action gate.
- Managed / unmanaged ownership is decided by path policy in v1; metadata or
  plan context may inform notes but do not replace path policy.
- Create output must explicitly return the managed worktree path, attached
  branch, and immediate next-step action for continuing work in that worktree.
- Inspect output must explicitly return `path`, `branch`, `status`, `dirty
  state`, `recommendation`, `reason`, and `next safe action` for every reported
  worktree.
- Any create / get / release / remove request outside a valid Git repository
  must block with no worktree mutation.
- Branch-name collisions must stop for an explicit reuse-or-rename decision; the
  skill must not silently reuse the branch lineage.
- Shared-file coordination risk must be surfaced as a planner / observer warning
  when create, inspect, or release may touch files shared across worktrees.
- Missing-path-but-still-registered worktrees must route to `prune-candidate`
  during inspect; the skill must not auto-prune them.
- v1 is instruction-first. No destructive scripts are included in this topic.
- If creator concludes a read-only status helper script is required, stop and
  repair this plan before widening artifact paths.

## Boundaries / Exclusions

- Planning actor owns only the analysis artifacts and topic plan contract.
- Creator owns only the worktree skill folder draft and must not self-approve.
- Reviewer owns only the independent verdict and must not author the final
  implementation directly.
- Publish, merge, release, README/VERSION updates, and stable-library promotion
  belong to separate later topics and are not executed here.
- Do not broaden this topic into stable-library promotion, README/VERSION
  updates, or generic Git release management.
- If the implementation needs files outside the listed artifact paths, stop and
  repair the plan instead of silently widening scope.

## Status / Allowed Transitions

- **Current**: `planned`
- **Execution model**: follow the canonical creator -> reviewer -> publish ->
  merge path for status vocabulary, but this topic stops at `approved` and does
  not execute publish / PR / merge work.
- **Allowed transitions**:
  - `planned` -> `creator-in-progress`
  - `creator-in-progress` -> `review-ready`
  - `review-ready` -> `reviewer-in-progress`
  - `reviewer-in-progress` -> `approved`
  - `reviewer-in-progress` -> `needs-rework`
  - `needs-rework` -> `creator-in-progress`
  - `approved` -> `creator-in-progress`
  - `approved` -> `publish-in-progress`
  - `publish-in-progress` -> `pr-open`
  - `publish-in-progress` -> `merged`
  - `pr-open` -> `needs-rework`
  - `pr-open` -> `merged`
  - `merged` -> terminal

Routing notes:

- Independent `plan-reviewer` approval is a hard prerequisite before the first
  `planned` -> `creator-in-progress` transition occurs.
- After reviewer `approved`, stop this topic at the review-ready handoff; any
  later canonical publish, PR, merge, or post-merge transitions require a
  separate later topic.
- At all phases, changed files must stay inside the exact artifact paths in this
  plan; if they drift, stop instead of improvising.

## Artifact Paths

| Artifact | Path | Owner | Role |
| --- | --- | --- | --- |
| Topic plan | `plan/worktree-skill/worktree-skill.plan.md` | Planning actor | Repo-visible execution contract for the worktree skill topic |
| Business baseline | `analysis/worktree-skill/requirements.md` | Planning actor | Frozen measurable baseline for worktree lifecycle behavior |
| Technical baseline | `analysis/worktree-skill/technical-spec.md` | Planning actor | Strict execution-facing technical source of truth |
| Skill contract | `.github/skills/worktree-manager/SKILL.md` | Creator | Primary lifecycle instructions, safety gates, and routing contract |
| Skill examples | `.github/skills/worktree-manager/examples.md` | Creator | Positive, negative, and exception-path examples for creator and reviewer use |
| Skill checklist | `.github/skills/worktree-manager/checklist.md` | Creator | Repeatable pre-create, pre-release, pre-remove, and unmanaged-worktree checks |
| Skill reference | `.github/skills/worktree-manager/reference.md` | Creator | Stable local detail for selectors, recommendation matrix, release evidence, and managed-path policy |

Artifact path notes:

- This topic does **not** modify `README.md`, `VERSION`, or
  `.github/copilot-instructions.md`.
- `.github/skills/worktree-manager/scripts/` is explicitly out of scope for this
  topic. If creator proves a read-only helper is necessary, repair the plan
  first.
- Treat the listed paths as an executable contract; if work drifts outside them,
  stop and repair the plan before continuing.

## Implementation Steps

1. Keep the analysis layer repo-visible and unchanged except for explicit plan
   repair:
   - `analysis/worktree-skill/requirements.md`
   - `analysis/worktree-skill/technical-spec.md`
2. Send the locked plan plus analysis artifacts to
   `/fleet @.github/skills/plan-reviewer/` and require an independent verdict
   before any creator work starts.
3. If plan-reviewer returns `needs-rework`, repair only the repo-visible planning
   artifacts and re-run plan-reviewer until the verdict is `approved`.
4. Send the independently approved plan contract plus analysis artifacts to
   `/fleet @.github/skills/agent-skill-creator/` and require the creator to stay
   inside the listed artifact paths.
5. Creator drafts `.github/skills/worktree-manager/` so the folder contains:
   - `SKILL.md`
   - `examples.md`
   - `checklist.md`
   - `reference.md`
6. The draft must encode these locked behaviors:
    - canonical managed path rule
    - create output contract: worktree path, branch, immediate next-step action
    - inspect output contract: `path`, `branch`, `status`, `dirty state`,
      `recommendation`, `reason`, `next safe action`
    - `release` vs `remove` boundary
    - recommendation matrix summary
    - release evidence format
    - managed / unmanaged inspect-only boundary
    - block-outside-repo behavior
    - `needs-human-decision` escalation for risky states
    - branch collision reuse-or-rename decision gate
    - stale registration -> `prune-candidate` routing
    - shared-file coordination warning
7. Assign file-level responsibilities explicitly:
   - `SKILL.md`: lifecycle contract, blocking rules, and concise positive /
     negative examples
   - `examples.md`: clean, dirty, unmanaged, stale-registration,
     branch-collision, and destructive-confirmation scenarios
   - `checklist.md`: pre-create, pre-release, pre-remove, unmanaged-worktree,
     and non-repo / ambiguous-state checks
   - `reference.md`: managed-path policy, recommendation matrix detail, release
     evidence fields, and selector / terminology notes
8. Send the creator result to `/fleet @.github/skills/agent-skill-reviewer/` for
   an independent verdict.
9. If reviewer returns `needs-rework`, route findings back to creator and repeat
   step 5 until the verdict is `approved`.
10. At planner alignment, verify the approved draft still maps 100% to
   `analysis/worktree-skill/technical-spec.md`.
11. Stop after reviewer verdict; do not commit, push, open a PR, merge, or touch
    stable-library surfaces in this topic.

## Validation / Acceptance Checks

- `analysis/worktree-skill/requirements.md` and
  `analysis/worktree-skill/technical-spec.md` both exist and remain aligned.
- All changed files stay within the exact artifact paths listed above.
- `.github/skills/worktree-manager/SKILL.md` keeps a single responsibility:
  worktree lifecycle management only.
- The draft includes the create next-step output contract with worktree path,
  branch, and immediate next action.
- The draft includes the inspect output contract with `path`, `branch`, `status`,
  `dirty state`, `recommendation`, `reason`, and `next safe action`.
- The draft preserves the locked distinction between `release` and `remove`.
- The draft treats unmanaged worktrees as inspect-only by default.
- The draft blocks use outside a valid Git repository with no worktree mutation.
- The draft routes branch collisions to an explicit reuse-or-rename decision.
- The draft surfaces shared-file coordination warnings where required.
- The draft routes missing-path-but-registered worktrees to
  `prune-candidate` without auto-pruning.
- The draft includes a recommendation matrix summary and release evidence fields
  without hiding destructive gates behind optimistic wording.
- `checklist.md` exists and covers pre-create, pre-release, pre-remove, and
  unmanaged-worktree checks plus non-repo and ambiguous-state checks.
- `examples.md` covers clean, dirty, unmanaged, stale-registration,
  branch-collision, and destructive-confirmation scenarios.
- No scripts are added in this topic unless the plan is repaired first.
- `agent-skill-reviewer` returns a machine-consumable `approved` or
  `needs-rework` verdict.
- No commit, push, PR, merge, post-merge cleanup, README/VERSION update, or
  stable publish action is part of this topic.
- No changes appear in `README.md`, `VERSION`, `.github/copilot-instructions.md`,
  or unrelated skill folders.

## Reviewer Handoff

```json
{
  "verdict": "approved|needs-rework",
  "blocking_issues": [],
  "copilot_feedback_triage": {
    "ADDRESS": [],
    "DISCUSS": [],
    "SKIP": []
  }
}
```

## Post-merge / release actions

- Not applicable in this topic.
- Publish, PR, merge, post-merge cleanup, repository release actions,
  README/VERSION updates, and stable-library promotion require separate later
  topics after reviewer-approved implementation exists.

## Open Questions / Unresolved Items

- None for planning. If creator proves that instruction-only execution cannot
  express inspect output or safety gates safely enough, stop and repair this
  plan before adding any script artifact.
