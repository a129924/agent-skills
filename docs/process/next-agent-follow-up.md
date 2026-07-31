# Next Agent Follow-Up

This guide is the handoff note for the next agent after PR #91 and PR #92 have
been merged, `v0.65.0` has been tagged, and the feature branches / worktrees
have been cleaned up.

## What To Watch

- Treat the current repository state as post-merge, post-cleanup baseline.
- Do not re-run the completed migration implementation, publish handoff, or
  release cleanup flows for the merged topics.
- Start from `origin/dev`, not from the deleted topic branches or removed
  worktrees.
- If the next task is another repo change, isolate it into a new topic and a
  new plan instead of extending the merged migration topics.
- If the next task is post-merge follow-up, use the post-merge workflow only
  after an explicit human resume signal.

## Recommended Skills

- `git-post-merge-workflow` for any cleanup, sync, or branch-retention work
  after a merge.
- `worktree-manager` for creating, inspecting, or releasing a new worktree.
- `plan-creator` and `plan-reviewer` for a new topic that needs a locked plan
  before implementation.
- `agent-skill-creator` and `agent-skill-reviewer` for skill changes or new
  skill authoring.

## What To Avoid

- Do not reopen PR #91 or PR #92 for the already-merged scope.
- Do not reuse the deleted `feat/andrew/*` branches.
- Do not treat the previous migration publish handoff as an invitation to keep
  advancing the old run.
- Do not mix future path-transition work into the already-completed migration
  topics unless the new topic explicitly owns that migration.
- Do not let a future follow-up silently broaden into `.codex/*`, README,
  VERSION, or shared workflow governance without a new plan.

## Copy-Paste Prompt

Use this when briefing the next agent:

> Current state: PR #91 and PR #92 are merged, `v0.65.0` is tagged, and the
> merged branches / worktrees were removed. Start from `origin/dev`. Do not
> reopen the completed migration topics. If you need a post-merge action, use
> `git-post-merge-workflow`. If you need a new topic, create a fresh plan and
> keep the scope bounded. Recommended skills: `git-post-merge-workflow`,
> `worktree-manager`, `plan-creator`, `plan-reviewer`, `agent-skill-creator`,
> `agent-skill-reviewer`.
