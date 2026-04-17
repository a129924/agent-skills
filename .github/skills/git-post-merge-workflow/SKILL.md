---
name: git-post-merge-workflow
description: Run post-merge cleanup and local sync safely after a PR is merged, including branch deletion defaults, fast-forward-only sync, and status verification.
---

# Purpose
Standardize post-merge cleanup and local synchronization after a PR is merged.

# Trigger / When to use
Use this skill when:
- a pull request was merged and the user asks what to do next
- the user wants to delete feature branches after merge
- the user wants to sync local mainline state after merge or tagging
- the user wants a safe post-merge checklist with verification steps

Do not use this skill when:
- the main task is naming a development branch
- the main task is drafting commit messages
- the main task is deciding whether a release gate is pass or fail
- the PR is closed without merge

# Inputs
- merge status of the PR (merged vs closed-unmerged)
- feature branch name
- repository default branch name (dynamic, not hardcoded)
- whether remote branch retention is required by policy
- local workspace cleanliness and ahead/behind status

# Process
1. Confirm the PR is actually merged. If it was closed without merge, stop and do not run cleanup deletion steps.
2. Detect the repository default branch dynamically, then switch to it.
3. Sync default branch with `git pull --ff-only`.
4. Verify local workspace status is clean and call out ahead/behind state before deletion.
5. Delete the remote feature branch by default after merge; keep it only when policy or audit retention requires it.
6. Delete the local feature branch with `git branch -d`; use `-D` only when explicitly required and after warning about risk.
7. Verify no stale post-merge branch state remains (for example with `git branch -vv`).
8. Output a concise completion summary plus any follow-up action when an exception path was used.

# Examples
- Positive: After PR merge, detect default branch, run `git pull --ff-only`, delete remote and local feature branches, and confirm no stale branch remains.
- Negative: Delete branches before confirming merge, hardcode `main` in a repo whose default branch is `dev`, or force-delete local branches without warning.

# Outputs
- a post-merge action plan with runnable cleanup and sync commands
- exception guidance when the branch must be retained or cannot be fast-forwarded
- final verification summary of branch and workspace state

# Boundaries
- Do not decide release readiness, tag policy, or version synchronization gates.
- Do not design branch names or commit messages.
- Do not auto-run destructive branch deletion without explicit user confirmation.
- Do not assume a fixed default branch name.

# Local references
- `examples.md`: normal paths, anti-patterns, exception handling, and verification-oriented command playbooks
