# Windows-to-WSL Development Command Skill Progression

## Workflow Stages

| Stage | Current state | Entry evidence | Required next gate | Next owner |
| --- | --- | --- | --- | --- |
| Plan amendment re-review | `approved` | The independent Plan-Reviewer approved the bounded workflow/progression-artifact amendment. | The approved amendment must be committed before a worktree is created. | Main Agent |
| Plan amendment commit | `complete` | Amendment-only commit `2505a508b09a3fcef373b174661aaecc87b60a84` is the verified base. | Create and verify the approved feature worktree from this commit. | Main Agent |
| Feature worktree provisioning | `feature-worktree-ready` | Verified before this state update: branch `feature/andrew/windows-wsl-dev`; worktree `D:\code\python\agent-skills.worktrees\agent-20260730-windows-wsl-dev`; base SHA `2505a508b09a3fcef373b174661aaecc87b60a84`; root `D:\code\python\agent-skills` and feature worktree were clean. The plan blob is `91bdd87a23228c13288dccc1bdf399e481f914f2` and the step blob is `b943f38406cfa987b72f05c6b555c0e3ec556499` in both root and feature indexes. Git blob identity is the equality authority; raw SHA-256 of working-tree bytes is not authoritative because line-ending checkout differences can change it. | Obtain explicit human authorization for external user-profile writes only. | Human |
| External implementation dispatch | `complete` | Human authorization covers only `%USERPROFILE%\.agents\skills\windows-wsl-dev\SKILL.md`, `%USERPROFILE%\.agents\skills\windows-wsl-dev\scripts\wsl-run.ps1`, and one append-only managed section in the effective `%CODEX_HOME%\AGENTS.md`. | Preserve this fixed external-write boundary during independent review. | Acceptance Checks Reviewer |
| External user-profile implementation | `review-ready` | The independent Implementer completed the authorized user-profile work in the actual user context: Ubuntu WSL2 was selected; the distribution-parse defect was repaired; `pwd`, exit-code `17`, stdout/stderr, paths with spaces, and bounded quoting checks passed. | An independent topic-plan Acceptance Checks Reviewer verifies the external implementation and evidence against the approved plan. | Acceptance Checks Reviewer |
| Independent implementation review | `review-ready` | The stable-library review blocker is not applicable: these are non-canonical, user-scoped targets and no shared `skills/**`, repository, or platform projection target is in scope. This is not a topic-complete or topic-closed claim. | Independent topic-plan Acceptance Checks Reviewer returns `approved` or `needs-rework`; rework returns only to an independent Implementer. | Acceptance Checks Reviewer |
| Close and follow-up handoff | `blocked` | Independent implementation review has not completed. | Create or validate the listed summary artifact before any close or human/agent follow-up handoff. | Main Agent |

## Actionable Steps

1. Dispatch an independent topic-plan Acceptance Checks Reviewer to assess the
   authorized external user-profile implementation and its evidence against the
   approved plan. The reviewer must not treat the non-applicable stable-library
   review blocker as a closure decision.
2. A `needs-rework` verdict returns only the bounded repair to an independent
   Implementer; an `approved` verdict still does not close the topic.

## Handoff / Gate Notes

- This is the minimal topic-local progression artifact required because this
  topic has multiple workflow-role handoffs. It is not generated through
  `step-creator`, does not select a reusable-Skill profile, and must not add or
  claim `skills/**` or a platform projection.
- The recorded `feature-worktree-ready` evidence is limited to the branch,
  worktree, base, clean-state, and Git index blob checks completed before this
  state-only update. The update itself is the sole intended feature-worktree
  modification and does not alter a locked decision, implementation scope,
  user-profile path, WSL routing, or security boundary.
- The external Implementer gate received explicit human authorization only for
  `%USERPROFILE%\.agents\skills\windows-wsl-dev\SKILL.md`,
  `%USERPROFILE%\.agents\skills\windows-wsl-dev\scripts\wsl-run.ps1`, and
  the append-only managed section in the effective `%CODEX_HOME%\AGENTS.md`.
  No other user-profile, repository, shared-skill, projection, or macOS path
  is authorized.
- The actual-user evidence is limited to Ubuntu WSL2 selection, the
  distribution-parse repair, and passed `pwd`, exit-code `17`, stdout/stderr,
  path-with-spaces, and bounded quotation checks. The next gate must assess
  that evidence; it does not close the topic.
- The prior stable-library review blocker is inapplicable because the targets
  are non-canonical and user-scoped. That inapplicability does not authorize
  a stable-library claim, repository write, or topic closure.
- No status update authorizes external writes, commit, push, PR creation,
  release work, a WDAC/security-policy bypass, or a change to the plan.
