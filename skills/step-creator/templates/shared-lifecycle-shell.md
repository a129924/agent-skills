# Shared lifecycle shell

This is the sole non-authoritative fixed lifecycle renderer for all profiles.
Resolve `<marker>` to `[X]` only with exact evidence; otherwise resolve it to
`[ ]`. The literal template marker is never emitted in a generated tracker.

## Selector inputs

Freeze and repeat one selector tuple:

```text
topic=<topic>; branch=<governed topic-branch selector>; managed-path-intent=<worktree-manager path intent>; primary-worktree=false
```

It is a planned selector, not a claim that the worktree exists. Initial
generation may render the worktree actions pending.

## Fixed head

```markdown
### Main Agent — Fixed Head

- <marker> **Actor:** Main Agent — **Action:** create-worktree — **Selector:** <selector tuple without primary-worktree>
- <marker> **Actor:** Main Agent — **Action:** prepare-topic-branch — **Selector:** <same selector tuple without primary-worktree>
```

`create-worktree` is complete only when exact inventory proves the selected
managed worktree and attached branch. The primary worktree is never a target.

## Fixed tail

Render after `## Implementation Steps` under
`## Main Agent Actionable Steps — Fixed Tail` in exactly this order:

```markdown
- <marker> **Actor:** Main Agent — **Action:** Validate the approved Written set and perform bounded staging only.
- <marker> **Actor:** Main Agent — **Action:** Obtain explicit human approval at STOP POINT 1 before commit, push, or PR creation.
- <marker> **Actor:** Main Agent — **Action:** Commit the approved bounded changes.
- <marker> **Actor:** Main Agent — **Action:** Push the topic branch.
- <marker> **Actor:** Main Agent — **Action:** Open the pull request.
- <marker> **Actor:** Main Agent — **Action:** Review and observe the pull request and route actionable feedback.
- <marker> **Actor:** Main Agent — **Action:** Hand off for human merge at STOP POINT 2 and completely stop.
- <marker> **Actor:** Main Agent — **Action:** Record exact human merge evidence after a new execution begins.
- <marker> **Actor:** Main Agent — **Action:** Require a new explicit human resume before post-merge work.
- <marker> **Actor:** Main Agent — **Action:** Verify the pull request is merged.
- <marker> **Actor:** Main Agent — **Action:** Fast-forward-only sync the target/default branch.
<slot-12 remote resolution>
<slot-13 release resolution>
<release branch: slots 14–21 or one release-not-applicable sentinel>
- <marker> **Actor:** Main Agent — **Action:** Inspect the selected managed topic worktree and prove clean/release evidence — **Selector:** <selector tuple without primary-worktree>
- <marker> **Actor:** Main Agent — **Action:** Obtain exact destructive approval to remove the selected managed topic worktree — **Selector:** <selector tuple without primary-worktree>
- <marker> **Actor:** Main Agent — **Action:** Remove the selected managed topic worktree and verify removal — **Selector:** <selector tuple without primary-worktree>
- <marker> **Actor:** Main Agent — **Action:** Delete the local topic branch after verified managed worktree removal.
- <marker> **Actor:** Main Agent — **Action:** Perform final verification and record close-semantics evidence without equating merged with closed.
```

## Conditional renderings

Slot 12 is exactly one of:

```markdown
- <marker> **Actor:** Main Agent — **Action:** Delete the remote topic branch when policy permits.
```

or:

```markdown
- [X] remote-retained — source plan or retention policy requires keeping the remote branch
```

When release is required, render slots 14–21 in order:

```markdown
- <marker> **Actor:** Main Agent — **Action:** Discover current authoritative version sources.
- <marker> **Actor:** Main Agent — **Action:** Synchronize discovered authoritative version sources.
- <marker> **Actor:** Main Agent — **Action:** Update README when stable-skill, public-contract, or index change requires it.
- <marker> **Actor:** Main Agent — **Action:** Commit release changes.
- <marker> **Actor:** Main Agent — **Action:** Push release changes.
- <marker> **Actor:** Main Agent — **Action:** Obtain exact human approval for annotated tag creation and tag push.
- <marker> **Actor:** Main Agent — **Action:** Create the annotated git tag.
- <marker> **Actor:** Main Agent — **Action:** Push the git tag.
```

For this branch, slot 13 is:

```markdown
- <marker> **Actor:** Main Agent — **Action:** Resolve whether release work is required from the source plan.
```

Replace slot 15 with the exact tag-only line when the authoritative inventory is
empty:

```markdown
- [X] tag-only — no authoritative version source discovered
```

Replace slot 16 with the exact README sentinel when evidence permits:

```markdown
- [X] README-not-required — stable-library metadata or explicit non-stable/no-README declaration requires no README change
```

When exact source truth declares terminal at merged, slot 13 is:

```markdown
- [X] Determine release requirement — release not required
```

Then omit slots 14–21 and render only:

```markdown
- [X] release-not-applicable — source plan declares terminal at merged
```

No unknown branch may be rendered as completed. STOP POINT 1 precedes commit,
push, and PR; STOP POINT 2 stops before merge follow-up; release push precedes
tag approval; worktree removal precedes local branch deletion.
