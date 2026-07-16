# Shared step-creator reference

This file has only shared rules. Upstream workflow, Git, release, Python, Agent
Skill, and tracker documents remain the authorities; profile-specific source
contracts live in the selected profile reference.

## Generation and eligibility

- Source is `plan/<topic>/<topic>.plan.md`; destination is the absent,
  create-only `plan/<topic>/<topic>.step.md`.
- The caller supplies exactly one supported profile. Never infer, fall back,
  content-sniff, repair a source, or update an existing output.
- Validate the complete source and all required branch truth before atomic
  creation. Invalid paths, unreadable source, existing output, incompatible
  profile, contradictory truth, or an unresolved material branch is `BLOCKED`
  with no write.
- Base/Agent source extraction and frozen wires are owned by their profile
  references. Python eligibility is canonical intent plus the 13-section
  `python-plan-authoring` contract only; its fixed contextual action is adapter
  behavior, not a new Python source-plan requirement.
- Freeze exactly one selector tuple: topic, governed topic-branch selector, and
  managed-worktree path intent. Repeat it in fixed head, cleanup slots, and
  Handoff Notes with `primary-worktree=false`. A planned tuple is not evidence
  that the selected worktree exists.

## Evidence and tracker

- `[X]` requires exact one-to-one repo-visible evidence for its rendered
  action. `[ ]` means planned, pending, or unproved; generated output contains
  no `[M]`.
- A source `[x]` is pending input, renders `[ ]`, and produces a warning.
  Partial evidence, a broad commit/status claim, unrelated artifact existence,
  or evidence that cannot map one-to-one is `BLOCKED`.
- Completion-evidence inputs name exact paths and/or exact command, PR, merge,
  release, tag, or worktree identifiers. Progression truth names the source plan
  and each source-declared progression/review/summary artifact actually used.
- Initial generation does not require a worktree. `create-worktree` is `[X]`
  only when exact inventory proves the selected managed worktree and selected
  attached branch; a primary worktree never qualifies. After fixed-head
  completion, absent, conflicting, primary, dirty, detached, locked, or unknown
  selected-worktree state is `BLOCKED` for later update/cleanup execution.
- The tracker parses only top-level `- [.]` checkbox lines. Base/Agent
  `check_all_succeeded` covers head, contextual actions, Implementation Steps,
  and tail; Python additionally covers six Workflow Stages. Every profile's
  `check_impl_steps_succeeded` covers only `## Implementation Steps`.

## Lifecycle rendering

- Use `templates/shared-lifecycle-shell.md` as the sole non-authoritative fixed
  head/tail renderer. Fixed lifecycle work belongs to Main Agent; source-owned
  contextual work and human merge/resume evidence remain outside Implementation
  Steps. This creator never updates output after generation.
- Slot 12 renders exactly one remote outcome. Render `remote-retained` only
  when exact source-plan or retention-policy evidence requires retaining the
  remote topic branch. When exact evidence instead permits deletion, render the
  delete action. Unknown or contradictory retention truth is `BLOCKED`; never
  use `remote-retained` as a speculative fallback.
- Slot 13 always resolves release. When source truth is terminal at merged,
  render exactly `[X] Determine release requirement — release not required`,
  then replace slots 14–21 with the one `release-not-applicable` sentinel. Do
  not leave a pending slot 13 in that branch.
- In the release-required branch, inventory actual authoritative version sources;
  an empty inventory uses `tag-only`, while multiple sources must agree and be
  synchronized. Slot 16 renders the README action or `README-not-required`.
  Release commit and push precede tag approval, tag creation, and tag push.
- Initial cleanup slots are pending. Exact destructive approval precedes
  worktree removal; verified removal precedes local branch deletion; merged or
  released never proves final closure.
