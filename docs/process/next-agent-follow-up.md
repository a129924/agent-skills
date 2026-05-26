# Next Agent Follow-Up

This guide is the handoff note for the next agent after PR #93
(`plan-step-tracker-move`) is reviewed and merged.

## Current State To Assume

- `plan-step-tracker-move` was executed as a one-to-one skill-folder move into
  `skills/plan-step-tracker/`.
- `step_tracker.py` was treated as normal skill content and moved with the rest
  of the skill folder.
- `dev` must remain clean.
- Topic work must live only inside a managed worktree, not in the repo-root
  `dev` worktree.
- `migration-implementation.workflow.md` now stops at
  `MIGRATION_STATUS_CONFIRMED` and hands off later publish actions instead of
  doing commit / push / PR work inside the implementation workflow body.

## Recommended Next Skill

- Next recommended runtime/tooling blocker: `sense-env-scaffold`

Why this one first:

- It is already classified as a `confirmed-blocker` in
  `docs/migration/migration-runway-checklist.md`.
- It is upstream of other blocker surfaces:
  - `python-project-init-greenfield`
  - `python-project-retrofit`
- Its coupling is executable-path and local-runtime specific, so solving it
  first reduces ambiguity for later blocker topics.

## Do Not Pick Yet

- Do not start with `python-project-init-greenfield` before deciding the
  `sense-env-scaffold` runtime/tooling transition contract.
- Do not start with `python-project-retrofit` before the same upstream
  `sense-env-scaffold` path contract is addressed.
- Do not jump to `.codex/skills`, installer, README, VERSION, or repo-wide
  active-path cutover as part of the next topic unless a separate plan
  explicitly owns that scope.

## Required Workflow For The Next Agent

1. Confirm whether PR #93 is merged.
2. If PR #93 is merged, start from `origin/dev`.
3. Create a fresh topic and fresh approved plan before implementation.
4. Decide the target branch before worktree creation.
5. Create a new managed worktree outside the repo root.
6. Do all topic implementation only inside that managed worktree.
7. Stop implementation workflow at `MIGRATION_STATUS_CONFIRMED`; use publish
   handoff separately for commit / push / PR.

## Mistakes Not To Repeat

- Do not implement in the repo-root `dev` worktree.
- Do not let `dev` accumulate topic-local uncommitted changes.
- Do not treat mistaken uncommitted work on `dev` as valid topic output.
- Do not invent a shim, forwarder, alias, wrapper, bridge, or compatibility
  layer unless the topic plan explicitly authorizes it.
- Do not introduce `importlib`-based dynamic loading to preserve an old path
  unless a dedicated runtime/tooling topic explicitly requires that design.
- Do not silently widen a skill-folder move into runtime/tooling repair,
  publish work, or `.codex/skills` maintenance.

## Topic-Shaping Guidance For `sense-env-scaffold`

- Treat it as a runtime/tooling blocker topic, not a low-risk direct copy.
- Plan around:
  - executable CLI path assumptions
  - local runtime package assumptions
  - downstream callers that invoke the current `.github/...` script path
- The next agent must first inspect:
  - `docs/migration/migration-runway-checklist.md`
  - `docs/migration/platform-coupling-inventory.md`
  - `.github/skills/sense-env-scaffold/`
  - downstream references in `python-project-init-greenfield` and
    `python-project-retrofit`
- If the next topic cannot avoid downstream contract decisions, the plan must
  say so explicitly before implementation starts.

## Recommended Skills

- `worktree-manager` for the new managed worktree
- `plan-creator` and `plan-reviewer` for the next bounded topic
- `agent-skill-creator` and `agent-skill-reviewer` only if the next topic
  actually changes skill contract files

## Copy-Paste Prompt

Use this when briefing the next agent:

> Current state: PR #93 (`plan-step-tracker-move`) should be treated as the
> latest completed blocker-follow-up topic once merged. Start from `origin/dev`,
> not from the old worktree. Keep `dev` clean. Create a fresh topic, decide the
> target branch before worktree creation, and do implementation only inside a
> new managed worktree. The next recommended skill is `sense-env-scaffold`
> because it is a confirmed runtime/tooling blocker upstream of
> `python-project-init-greenfield` and `python-project-retrofit`. Do not repeat
> the old mistake of implementing on `dev`, and do not invent shim / importlib
> compatibility layers unless the approved topic explicitly requires them.
