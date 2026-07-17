---
topic: step-creator-release
source_plan: plan/step-creator-release/step-creator-release.plan.md
created: 2026-07-17
---

# step-creator-release — Step Tracking

## Workflow Stages

| Current status | Allowed next transitions | Next actor |
| --- | --- | --- |
| Pre-execution planning-publication review: `reviewer-in-progress` | `approved` \| `needs-rework` outside the release lifecycle | Independent Plan-Reviewer |

## Actionable Steps

### Main Agent — Fixed Head (Lineage 1: Planning Artifacts)

- [X] **Actor:** Main Agent — **Action:** create-worktree — **Selector:** topic=step-creator-release; branch=release/andrew/step-creator-0.77.0; managed-path-intent=/Users/andrew/code/python/agent-skills.worktrees/agent-20260717-step-creator-release; primary-worktree=false
- [X] **Actor:** Main Agent — **Action:** prepare-topic-branch — **Selector:** topic=step-creator-release; branch=release/andrew/step-creator-0.77.0; managed-path-intent=/Users/andrew/code/python/agent-skills.worktrees/agent-20260717-step-creator-release; primary-worktree=false

### Planning Review and Lineage 1 Ready-PR Gate

- [X] **Actor:** Plan-Creator — **Action:** Create or correct only `plan/step-creator-release/step-creator-release.plan.md` and `plan/step-creator-release/step-creator-release.step.md` in Lineage 1.
- [ ] **Actor:** Plan-Reviewer — **Action:** Independently review the uncommitted planning draft; return only `approved` or `needs-rework` JSON. It must remain `reviewer-in-progress` until this result.
- [ ] **Actor:** Main Agent — **Action:** On `approved`, obtain explicit human STOP POINT 1 authorization before Lineage 1 commit, push, or Ready PR. The reviewed planning artifacts become a committed artifact fact only; this pre-execution gate does not enter the release lifecycle or synthesize any release status transition.
- [ ] **Actor:** Main Agent — **Action:** Commit and push exactly the two planning artifacts on Lineage 1, then open the first Ready PR. Do not stage `README.md`, `VERSION`, or release changes.
- [ ] **Actor:** Human — **Action:** Merge the first Ready PR. This is STOP POINT 2; automated execution stops after the human merge handoff.

### Lineage 1 Post-merge Resume and Cleanup

- [ ] **Actor:** Human — **Action:** Send a new explicit resume that confirms the first Ready PR merged and requests release continuation.
- [ ] **Actor:** Main Agent — **Action:** Verify first PR is `MERGED` (not merely closed), detect default branch/remote, and FF-only sync the default branch; preserve and report any local state.
- [ ] **Actor:** Main Agent — **Action:** Obtain a distinct new explicit human destructive approval, then verify Lineage 1 worktree clean, remove it, and only then delete its local branch. Keep the remote branch unless separately authorized for deletion; preserve all stashes.

### Main Agent — Fixed Head (Lineage 2: Release Diff)

- [ ] **Actor:** Main Agent — **Action:** create-worktree — **Selector:** topic=step-creator-release-diff; branch=release/andrew/step-creator-0.77.0-release-diff; managed-path-intent=/Users/andrew/code/python/agent-skills.worktrees/agent-20260717-step-creator-release-diff; primary-worktree=false; source=exact synced default-branch HEAD
- [ ] **Actor:** Main Agent — **Action:** prepare-topic-branch — **Selector:** topic=step-creator-release-diff; branch=release/andrew/step-creator-0.77.0-release-diff; managed-path-intent=/Users/andrew/code/python/agent-skills.worktrees/agent-20260717-step-creator-release-diff; primary-worktree=false; source=exact synced default-branch HEAD
- [ ] **Actor:** Main Agent — **Action:** Start the actual Lineage 2 release lifecycle at `planned`, then route canonically to `creator-in-progress`.

### Lineage 2 Release-diff Implementation and Ready-PR Gate

- [ ] **Actor:** Release Implementer — **Action:** In the selected Lineage 2 worktree only, rediscover authoritative version sources and values. Block on disagreement, unreadable source, unlisted additional authority, or an unexpected tag-only condition; do not write `dev` or a primary worktree.
- [ ] **Actor:** Release Implementer — **Action:** If the inventory confirms the listed authority, set `VERSION` to `0.77.0` and make only the locked README v0.77.0/PR #116/`skills/step-creator/` historical entry plus the `step-creator` Current skills row between `sense-env-scaffold` and `subagent-dispatch-policy`.
- [ ] **Actor:** Reviewer — **Action:** Independently review the Lineage 2 README/version diff against the approved plan. `needs-rework` returns only to Release Implementer.
- [ ] **Actor:** Main Agent — **Action:** After independent approval and explicit publication authorization, commit and push the bounded Lineage 2 release diff, then open the second Ready PR. Never write or commit directly on default branch.
- [ ] **Actor:** Human — **Action:** Merge the second Ready PR. This is a second STOP POINT 2; automated execution stops. Do not tag an unmerged Lineage 2 branch commit.

### Lineage 2 Post-merge Release and Tag Gate

- [ ] **Actor:** Human — **Action:** Send a new explicit resume that confirms the second Ready PR merged and requests tag/release continuation.
- [ ] **Actor:** Main Agent — **Action:** Verify the second PR is `MERGED` (not merely closed), then detect default branch/remote again and FF-only sync default; prove the README/VERSION release commit is visible on merged default-branch history.
- [ ] **Actor:** Main Agent — **Action:** Record PASS for independent reviewer approval, CI, base tests, strict type checks, lint, documentation synchronization, version synchronization, clean workspace, and remote tag uniqueness. Any absent or failing signal—including missing pytest—is BLOCKED.
- [ ] **Actor:** Main Agent — **Action:** Recheck local and remote `v0.77.0` uniqueness immediately before tagging and obtain a distinct explicit human approval to create the tag.
- [ ] **Actor:** Main Agent — **Action:** Create annotated `v0.77.0` at the merged default-branch release commit, push the tag in a separate action, and verify the remote tag target.

### Lineage 2 Cleanup Gate

- [ ] **Actor:** Main Agent — **Action:** Obtain a new destructive approval, verify the selected Lineage 2 worktree clean, remove it, then delete the local branch.
- [ ] **Actor:** Main Agent — **Action:** Delete the Lineage 2 remote branch only with separate explicit approval; preserve all stashes.
- [ ] **Actor:** Main Agent — **Action:** Verify final repository state and record `released` closure.

## Handoff / Gate Notes

- Current progression truth is a pre-execution `reviewer-in-progress`
  planning-publication review, because these planning artifacts are uncommitted
  and under independent plan review. It is outside the release lifecycle;
  neither a draft file nor worktree existence authorizes a release `planned` or
  `publish-in-progress` state.
- There are exactly two PR/merge lineages. Lineage 1 publishes only planning
  artifacts; Lineage 2 publishes README/VERSION from a new managed worktree
  created from the FF-synced default branch. Both PRs require separately
  verified `MERGED` evidence; `closed` is never equivalent to `merged`.
- STOP POINT 1 applies to pre-execution Lineage 1 planning-artifact publication.
  STOP POINT 2 applies after *each* human merge. The first requires a new
  explicit human resume and FF-only default sync, followed by a distinct new
  destructive approval before Lineage 1 cleanup or Lineage 2 creation; only
  then does Lineage 2 begin the canonical release lifecycle at `planned`. The
  second requires a different new explicit human resume before merged
  verification, default sync, release gate, tag, or Lineage 2 cleanup.
- Current planning evidence finds root `VERSION=0.76.1` as the sole authority.
  Lineage 2 revalidates this fact dynamically. Multiple sources disagreeing or
  any newly found unlisted authority is BLOCKED and requires plan repair before
  write.
- Full normal release gate runs only after the second merge/default sync and is
  all-or-blocked: reviewer, CI, base tests, strict types, lint, docs sync,
  versions, clean workspace, and remote tag uniqueness. Missing pytest is not
  a passing test signal.
- The tag may be created only after full PASS, a separate explicit tag approval,
  and proof that the Lineage 2 release commit is in merged default history. Git
  tag and tag push are distinct actions.
- Worktree removal is destructive. Lineage 1 needs a distinct new destructive
  approval after merged/resume/sync evidence; Lineage 2 needs its own
  destructive approval. Each worktree is removed before its local branch;
  remote deletion needs separate approval and stashes remain untouched.
