# step-creator Release Plan

> Semantic warning: `analysis/step-creator-release/requirements.md` and
> `analysis/step-creator-release/technical-spec.md` are absent. This bounded
> release plan uses the explicit human release override and the merged PR #116
> as its planning baseline. Those missing analysis artifacts are not execution
> prerequisites and must not be recreated or inferred during this topic.

## Goal / Outcome

- Release the merged `skills/step-creator/` stable skill as repository version
  `0.77.0` with exact annotated tag `v0.77.0`.
- Add the locked, minimal README release history entry and Current skills table
  row, and synchronize every version source discovered to be authoritative at
  release time.
- Preserve the normal release gates: a planning-artifact Ready PR and human
  merge precede post-merge release changes; no tag exists before all release
  gates pass and a separate explicit human tag approval is recorded.

## Scope

- **In scope**:
  - create and review this topic's two planning artifacts;
  - run two separately managed, non-`dev` lineages: a planning-artifact Ready
    PR followed by a release-diff Ready PR;
  - after the first verified merge, STOP POINT 2 resume, FF-only default sync,
    and a distinct new explicit destructive approval, clean up the first
    managed worktree, then create a second managed release-diff
    worktree/branch from the FF-synced default branch;
  - in the second worktree only, dynamically inventory version sources, update
    the discovered authoritative sources to `0.77.0`, make the two locked
    README additions, independently review, commit/push the release diff, and
    open the second Ready PR;
  - after the second verified merge and default-branch FF-only sync, run the
    full normal release gate, then create and push annotated `v0.77.0` only
    after explicit tag approval;
  - perform bounded cleanup for each managed worktree only after its applicable
    destructive approval.

- **Out of scope**:
  - any edit to `skills/step-creator/**`, its original topic artifacts, or the
    merged implementation from PR #116;
  - README restructuring beyond the two locked additions;
  - changing the branch, workflow, release, version-source, or tag policy;
  - changing a version source that is not discovered as authoritative at
    release time;
  - a tag-only fallback while one or more authoritative version sources exist;
  - direct merge, tag mutation, remote-branch deletion, worktree removal, or
    local-branch deletion without their respective gates.

## Locked Decisions

- This is a stable-library-affecting, normal-path release topic initiated by a
  human override of the earlier explicit no-release outcome for merged PR
  #116. It is not an emergency release and no normal gate may be waived.
- The first Ready PR contains only
  `plan/step-creator-release/step-creator-release.plan.md` and
  `plan/step-creator-release/step-creator-release.step.md`. README, VERSION,
  and tag actions are deferred until after that PR is merged, STOP POINT 2 is
  explicitly resumed, merge state is verified, the default branch is FF-only
  synchronized, and a second managed release-diff worktree exists.
- **Lineage 1 selector** is fixed to
  `topic=step-creator-release; branch=release/andrew/step-creator-0.77.0;
  managed-path-intent=/Users/andrew/code/python/agent-skills.worktrees/agent-20260717-step-creator-release;
  primary-worktree=false`. It starts from the existing managed worktree and
  contains only the planning artifacts.
- **Lineage 2 construction** is fixed: after Lineage 1 is merged, explicitly
  resumed, verified, and the dynamically detected default branch has been
  FF-only synchronized, create a *new* managed worktree from that exact synced
  default-branch HEAD. Its selector is
  `topic=step-creator-release-diff; branch=release/andrew/step-creator-0.77.0-release-diff;
  managed-path-intent=/Users/andrew/code/python/agent-skills.worktrees/agent-20260717-step-creator-release-diff;
  primary-worktree=false`. The second branch must not be created from an
  unmerged branch, and neither README nor VERSION may be written in `dev` or
  any primary worktree.
- After Lineage 1 merged state, explicit resume, and FF-only default sync are
  verified, a distinct new explicit human destructive approval is required
  before removing that managed worktree and then its local branch. Its remote
  deletion remains a separately explicit decision. Lineage 2 cleanup remains a
  separate later destructive approval boundary.
- The exact intended release value is `0.77.0`; the exact eventual Git tag is
  the annotated tag `v0.77.0`. The tag is a post-merge external action, not a
  repository file.
- Current planning evidence finds only root `VERSION`, with current value
  `0.76.1`, as the sole authoritative version source. This is a current fact,
  not a cross-repository hardcode: post-merge execution must rediscover
  `VERSION`, `pyproject.toml`, `src/<package>/__version__.py`, `package.json`,
  and other relevant release sources. Multiple discovered authorities must
  agree before editing and all must be synchronized to `0.77.0`; disagreement
  is `BLOCKED`. Tag-only mode is allowed only when none exists, which current
  facts do not support.
- `README.md` is required and may receive only these additions:
  1. a `v0.77.0` / PR #116 / `skills/step-creator/` historical
     migration-and-release entry; and
  2. a `step-creator` Current skills table row between `sense-env-scaffold` and
     `subagent-dispatch-policy`, accurately stating that it creates a
     caller-selected profile-specific `plan/<topic>/<topic>.step.md` with
     fixed worktree, PR, release, and cleanup gates.
- The normal release gate requires independent reviewer approval, green CI,
  passing base tests, passing strict type checks, passing lint, documentation
  synchronization, synchronized version sources, a clean workspace, and tag
  uniqueness on the remote. Missing pytest or any other absent signal is
  `UNCONFIRMED`/`BLOCKED`, never a pass or waiver.
- Remote tag uniqueness for `v0.77.0` must be checked again after the planning
  PR merge, after the release-diff PR merge, and immediately before tag
  creation. The tag is created only after the version/README release commit is
  merged into the default branch, the full gate is PASS, and a distinct human
  tag approval exists. `git tag` and tag push are separate actions; the tag
  must target the merged default-branch release commit, never an unmerged
  release-diff branch commit.
- Worktree removal and local/remote branch deletion are destructive actions.
  They require separate explicit approval; remove the worktree before deleting
  its local branch. No stash is deleted or altered by this topic.

## Boundaries / Exclusions

- Plan-Creator owns only the two planning artifacts. It does not edit README,
  VERSION, tags, GitHub state, or release branches.
- Plan-Reviewer independently reviews the planning artifacts. Release
  Implementer updates only the exact post-merge allowed files; an independent
  Reviewer evaluates that release diff and must not approve its own output.
- Main Agent routes gates, performs bounded Git/GitHub actions, and stops at
  STOP POINT 1, STOP POINT 2, and the explicit tag/destructive-action gates.
- `AGENTS.md` remains the governance authority; canonical content stays under
  `skills/`, so no `.github/**`, `.codex/**`, or other projection is added or
  treated as authoritative.
- If any work requires a path outside `Artifact Paths`, stop and repair this
  plan before writing it. Do not reopen the locked PR #116 skill contract.

## Status / Allowed Transitions

- **Current**: pre-execution planning-publication review is
  `reviewer-in-progress` for the two uncommitted planning artifacts. It is
  outside this release topic's lifecycle and is not `planned`,
  `publish-in-progress`, or executable release authority.
- **Execution model**: pre-execution planning review -> STOP POINT 1 ->
  Lineage 1 planning-artifact Ready PR -> human merge -> STOP POINT 2
  resume/merge verification/default FF-only sync/new explicit destructive
  approval/Lineage 1 cleanup -> new Lineage 2 managed release-diff worktree
  from synced default HEAD ->
  actual canonical release lifecycle (`planned` -> `creator-in-progress` ->
  `review-ready` -> `reviewer-in-progress` -> `approved` ->
  `publish-in-progress` -> `pr-open` -> `merged` -> `released`) with the
  second STOP POINT 2 before post-merge release/tag/cleanup actions.
- **Allowed transitions**:
  - `planned` -> `creator-in-progress`
  - `creator-in-progress` -> `review-ready`
  - `review-ready` -> `reviewer-in-progress`
  - `reviewer-in-progress` -> `approved`
  - `reviewer-in-progress` -> `needs-rework`
  - `needs-rework` -> `creator-in-progress`
  - `approved` -> `creator-in-progress`
  - `approved` -> `publish-in-progress` for the independently approved
    Lineage 2 release-diff
  - `publish-in-progress` -> `pr-open` for the Lineage 2 release-diff Ready PR
  - `pr-open` -> `needs-rework`
  - `pr-open` -> `merged` for the Lineage 2 release-diff Ready PR only
  - `merged` -> `released` only after a second STOP POINT 2,
    new explicit human resume, second merge verification, default FF-only sync,
    full normal gate PASS, explicit tag approval, tag creation/push, and
    approved cleanup
  - `released` -> terminal

Routing notes:

- The planning-artifact PR is a deliberate pre-execution publication gate, not
  a release-topic `pr-open` or `merged` transition. It does not authorize
  README/VERSION edits before its human merge and STOP POINT 2 resume. The
  release-diff is the second Ready PR and the only PR represented by the
  release lifecycle; it is never a default-branch direct write.
- After either independent review, any scope, source-discovery, documentation,
  or contract failure routes to `needs-rework`. After the second merge, any
  failed CI/test/type/lint/docs/version/cleanliness/tag-uniqueness gate blocks
  tag creation; it does not reopen or silently change the merged release diff.
- STOP POINT 1 blocks pre-execution Lineage 1 planning publication. STOP POINT
  2 is terminal after each human merge: Lineage 1 requires explicit resume,
  verified FF-only sync, and a distinct new destructive approval before its
  cleanup or Lineage 2 creation, while the actual release lifecycle begins as
  `planned` only after new Lineage 2 worktree creation. Lineage 2 requires a
  new explicit resume before second merge verification, default sync, release
  gate, tag, or cleanup. Release-diff publication, tag approval, and each
  destructive cleanup are distinct subsequent gates.

## Artifact Paths

| Artifact | Path | Owner | Role |
| --- | --- | --- | --- |
| Topic plan | `plan/step-creator-release/step-creator-release.plan.md` | Plan-Creator | Current execution contract for the bounded release topic |
| Topic progression | `plan/step-creator-release/step-creator-release.step.md` | Plan-Creator | Progression and human-gate record for this topic |
| Stable-library summary | `README.md` | Release Implementer | Locked history entry and one Current skills row after verified post-merge resume |
| Version source | `VERSION` | Release Implementer | Current sole discovered authority; update only if post-merge inventory confirms it remains authoritative |

Artifact path notes:

- The exact planned Written set is the two planning files, `README.md`, and
  `VERSION`. The Git tag is an external post-merge action, not an artifact path.
- If post-merge inventory finds an additional authoritative version source,
  execution is `BLOCKED` until this plan is repaired to list that exact path;
  it must not be silently edited outside this contract.
- `skills/step-creator/**`, original `plan/step-creator/**`, inventories,
  projection surfaces, tests, builder scripts, and all unlisted files are
  read-only/excluded for this topic.

## Stable library metadata

- `README row`: add the locked `v0.77.0` / PR #116 / `skills/step-creator/`
  historical migration-and-release entry; add exactly one Current skills row
  between `sense-env-scaffold` and `subagent-dispatch-policy` describing the
  caller-selected profile-specific `plan/<topic>/<topic>.step.md` generator
  with fixed worktree, PR, release, and cleanup gates.
- `VERSION bump`: current discovered `0.76.1` -> locked `0.77.0`; revalidate
  the current source inventory and values after merge before writing. Any
  discovered authoritative sources are synchronized to `0.77.0` only after
  this plan lists their exact paths.
- `timing`: planning artifacts at `publish-in-progress`; README and version
  changes at post-merge `release`; annotated tag after release commit/push,
  full PASS gate, remote uniqueness recheck, and explicit human tag approval.
- `rationale`: merged PR #116 adds the stable `step-creator` capability, a
  feature-level release explicitly locked by the human as `0.77.0`.
- `release notes`: the locked README historical entry is the release-facing
  record; no broad README restructuring or extra changelog is authorized.

## Implementation Steps

1. Plan-Creator creates or corrects only
   `plan/step-creator-release/step-creator-release.plan.md` and
   `plan/step-creator-release/step-creator-release.step.md` in Lineage 1's
   selected managed worktree, then hands the draft to an independent
   Plan-Reviewer. It performs no release implementation, Git publication,
   review verdict, gate routing, or cleanup action.

## Validation / Acceptance Checks

- The uncommitted planning draft changes only the two planning paths and is in
  a pre-execution `reviewer-in-progress` planning-publication review.
  Independent approval plus STOP POINT 1 commit/push makes it a committed
  planning artifact fact; it does not enter the release lifecycle or route to
  `publish-in-progress`. The Lineage 1 Ready PR contains exactly those two
  files.
- Lineage 1 and Lineage 2 each have distinct branch/worktree selectors, Ready
  PRs, human merge evidence, and default-branch FF-only synchronization. No
  README/VERSION edit happens in `dev`, the primary worktree, or Lineage 1.
- Lineage 2 is created only from the exact synced default-branch HEAD after
  Lineage 1's verified merge and explicit STOP POINT 2 resume. Its release-diff
  changes only `README.md` and version paths that are listed and confirmed
  authoritative.
- Independent Plan-Reviewer returns the required JSON `approved` verdict before
  pre-execution Lineage 1 publication. After Lineage 2 worktree creation, the
  release lifecycle begins `planned`; independent Reviewer returns `approved`
  before its valid `approved` -> `publish-in-progress` release-diff
  commit/push/Ready PR.
- Version-source discovery is rerun in Lineage 2 after its creation from synced
  default. Current `VERSION=0.76.1` is confirmed or a plan repair blocks
  changes; every listed/discovered authority is exactly `0.77.0` before the
  Lineage 2 Ready PR is opened.
- README has no restructuring: it contains exactly the locked historical entry
  and the `step-creator` Current skills row at the locked table location with
  accurate description.
- After the second human merge, a second STOP POINT 2 and new explicit human
  resume are required before merged-state verification and default-branch
  FF-only sync. Only then are full normal release signals independently
  evidenced as PASS; absent pytest/test/type/lint/CI evidence is not substituted
  by a warning or intuition.
- `v0.77.0` is absent from remote immediately before tag creation, the
  README/VERSION release commit is visible on merged default-branch history,
  the tag is annotated against that merged commit, and tag creation and tag
  push are separate verified actions.
- Lineage 1 cleanup needs a distinct new destructive approval after its
  merged/resume/sync evidence; Lineage 2 cleanup needs its own destructive
  approval. For each lineage, worktree removal precedes local branch deletion,
  remote deletion has distinct approval, and final status is clean.

## TestCase

1. Lineage 1 preflight confirms its fixed managed worktree/branch identity;
   `git diff --check` passes and only the two planning artifacts are changed.
2. Independent Plan-Reviewer returns exactly the JSON handoff. A planning draft
   that enters the release lifecycle, a missing two-lineage rule, early
   README/VERSION edit, early tag, or missing STOP gate returns `needs-rework`.
3. Before STOP POINT 1 authorization, Lineage 1 commit/push/Ready PR is
   blocked. After authorization, its staging and PR contain exactly the two
   planning artifacts and neither `README.md` nor `VERSION`.
4. A first PR that is only approved or closed is rejected at STOP POINT 2. Only
   verifiable merged state plus a new explicit human resume permits default
   branch detection and FF-only synchronization; a distinct new explicit human
   destructive approval is then required before Lineage 1 cleanup.
5. Lineage 2 creation fails if it uses `dev`, a primary worktree, an unmerged
   source branch, a non-FF-synced default, or a selector/path different from
   the locked construction. Only after successful creation does the actual
   release lifecycle begin at `planned`; its README/VERSION diff remains
   uncommitted until independent Reviewer approval and its own Ready PR
   publication.
6. Lineage 2 source discovery with only `VERSION=0.76.1` permits the bounded
   update to `0.77.0`; two disagreeing authorities, an unreadable authority,
   or a newly discovered unlisted authority is `BLOCKED` without a version
   write.
7. README verification proves exactly one v0.77.0/PR #116/`skills/step-creator/`
   historical entry and exactly one `step-creator` row between
   `sense-env-scaffold` and `subagent-dispatch-policy`; any other restructure
   fails scope validation.
8. A second PR that is only approved or closed cannot advance to tagging. Even
   after its verified human merge, a second STOP POINT 2 and new explicit human
   resume are required before its merged-state verification and FF-only default
   sync. Thereafter, missing or failing CI, base tests, strict typing, lint,
   documentation sync, reviewer approval, version synchronization, clean
   workspace, or remote tag uniqueness blocks the normal gate; absent pytest is
   not a substitute for passing tests.
9. A pre-existing local or remote `v0.77.0`, a dirty workspace, or a release
   commit absent from merged default history blocks tag creation. With every
   gate PASS and separate tag approval, the annotated tag targets the merged
   default release commit; tag creation and tag push are individually evidenced.
10. Without the applicable destructive approval, each lineage's worktree/branch
    deletion is blocked. With it, cleanup verifies clean worktree, removes it
    before local branch deletion, deletes a remote branch only under separate
    approval, and leaves stashes unchanged.

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

- **Lineage 1 completion**: do not continue because the planning PR is merely
  closed. Verify its merge, require a new explicit human STOP POINT 2 resume,
  detect default branch/remote, and FF-only sync it. Then require a distinct
  new explicit human destructive approval before removing Lineage 1 worktree
  and then its local branch. Keep its remote branch unless separately
  authorized for deletion.
- **Lineage 2 creation and publication**: from that exact synced default HEAD,
  create the locked second managed worktree/branch. Only there may the Release
  Implementer discover sources and modify bounded README/VERSION. After
  independent review and bounded release-diff commit/push, open the second
  Ready PR. No direct default-branch write is allowed.
- **Lineage 2 merge and release**: after second human merge handoff, STOP at a
  second STOP POINT 2. Require a *new* explicit human resume and verified
  second merged state before detecting and FF-only syncing default again; only
  then enforce every normal release gate. No release action is skipped, waived,
  or inferred. The `v0.77.0` tag is created only after full PASS and separate
  human tag approval; it is annotated at the merged default-branch release
  commit and pushed in a distinct action.
- **Lineage 2 cleanup**: after tag verification, wait for its destructive
  approval before cleanup. Remove the managed worktree before local branch
  deletion; delete the remote branch only under explicit approval; retain all
  stashes.

## Open Questions / Unresolved Items

- None for planning. The post-merge version-source inventory is a required
  execution-time verification, not an unresolved design choice. If it finds an
  additional authoritative source, the topic is blocked pending a plan repair.
