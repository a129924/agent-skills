# ssh-ops remote actions

## Goal / Outcome

**Goal** Expand the macOS skill to one authorized login check, command, file download, or directory download per task. Accept an account and host from natural language or SSH notation, including aliases and a trusted alternate config. Preserve integrity and exclusive delivery for the previous single-file route.

**Non-Goal** Long-lived shared credentials, deployment automation, or host administration as a separate workflow.

## Scope

- **In-Scope** Native masked password entry, trusted first-use fingerprint pinning, supervised per-task master, reuse of an existing master, Terminal fallback, bounded command output, verified recursive download, and local review views.
- **Out-Of-Scope** Upload, interactive shell, forwarding, automatic reconnection, persistent SSH changes, user-scope installation or projection, stable-library changes, merge, tag, and release.
- The accepted conversation plan is the planning baseline. No optional analysis files are prerequisites.

## Locked Decisions

- Baseline d9b75776ef081d954da0d6612d157e0e871e2fdc, feature branch feat/andrew/ssh-ops-remote-actions, and Draft PR base dev. All tracked writes occur in the isolated feature worktree.
- Confirm effective host, port, account, trusted config and exact operation. Confirm generated remote mutations with their command and impact. Existing authorized masters have user-established identity and lifetime.
- New direct login verifies the host key before a password-only, single masked prompt. A first-use pin must match an independently trusted SHA-256 fingerprint. Any key mismatch stops. The password stays in the askpass-to-OpenSSH pipe. The task supervisor owns a private short-path lease and expires it even when no operation completes. GUI unavailability permits the user-owned Terminal route. Authentication failure, cancellation, and timeout terminate the attempt.
- Run operations in an invocation-scoped sandbox with the exact verified socket, direct network off, and only the approved destination writable for downloads. Verify effective settings and refuse replacement connections. Keep the remote command exact and noninteractive. Retain the first 64 KiB of each output stream, continue draining both after the cap, and report truncation, SSH exit code and outcome. An uncertain remote outcome is never replayed automatically.
- Default login 90 s, command 120 s, download 600 s, task 900 s. Authorized extensions must fit the absolute 1800 s task ceiling.
- Keep single-file SHA-256, private staging and exclusive delivery. Preflight remote Python 3 stdlib and descriptor-relative operations. Walk from the filesystem root with no-follow opens for each component and compare observed identity before and after reads. Use bounded UTF-8 JSON lines with type, root-relative path components, size and manifest digest. A data file header is followed by exactly its declared bytes. Reject special entries, name collisions, incomplete streams and changes. Compare before and after SHA-256 manifests with actual local results, and install same-parent private 0700/0600 staging via macOS renameatx_np with RENAME_EXCL.

## Boundaries / Exclusions

- **ReadOnly** dev checkout and its experiment diffs, previous topics, governance, README.md, VERSION, projections, existing user SSH and Skill configuration, and unrelated files.
- **Written** The exact tracked paths below. Local maps and receipts live in /private/tmp/ssh-ops-remote-actions. Remote acceptance needs a separately authorized host and private local destination.
- **Modify** Only the two existing skill files in the table. Topic-local records may be updated by their owners.
- **Deleted** Zero tracked files. Cleanup is limited to task-owned runtime resources.

## Status / Allowed Transitions

Record observed state in the step artifact. The reviewed and committed planning baseline enables planned → creator-in-progress → review-ready → reviewer-in-progress → approved or needs-rework. Rework returns to creator-in-progress. Contract alignment enables publish-in-progress. Verify the draft before recording pr-open and hand off for human review. The current request authorizes bounded commits, push and one Draft PR.

## Artifact Paths

| Path | Owner | Role |
| --- | --- | --- |
| plan/ssh-ops-remote-actions/ssh-ops-remote-actions.plan.md | Plan-Creator | Execution contract |
| plan/ssh-ops-remote-actions/ssh-ops-remote-actions.step.md | Planning actor and subsequent role owners | Evidence and transitions |
| plan/ssh-ops-remote-actions/ssh-ops-remote-actions.review-log.md | Plan-Reviewer and Reviewer | Independent verdicts and repair evidence |
| plan/ssh-ops-remote-actions/ssh-ops-remote-actions.summary.md | Main Agent | Human handoff |
| skills/ssh-ops/SKILL.md | Implementer | Entry point and authorization |
| skills/ssh-ops/examples.md | Implementer | Runnable usage and scope |
| skills/ssh-ops/scripts/ssh_ops.py | Implementer | Local supervisor, operations and delivery |
| skills/ssh-ops/scripts/ssh_askpass.py | Implementer | Masked password prompt |
| skills/ssh-ops/scripts/ssh_directory.py | Implementer | Read-only remote directory stream |
| skills/ssh-ops/tests/test_ssh_ops.py | Implementer | Focused regression tests |

## Implementation Steps

1. Implement the supervised login lease and documented socket-only invocation. Keep review graphs out of the repository.
2. Add bounded command execution and directory download. Preserve the previous verified single-file behavior and link authorization.
3. Update skill metadata, examples, and locally repeatable tests.

## Validation / Acceptance Checks

| TestCase | Evidence |
| --- | --- |
| Login and trust | Resolve real OpenSSH default/alternate config, test host pin and cancellation, verify GUI under the actual scoped Codex network and desktop permissions with a disposable secret. Check that chat, argv, env, output, logs and temporary files do not contain it. Record any unverified surface. |
| Lifecycle and permissions | Watch supervised shutdown, hard expiry and failed authentication. Verify external master preservation, scope of filesystem/network policy and refusal of direct fallback. |
| Command | Assert separate stdout/stderr, actual exit code, caps, timeout/255 unknown and no replay. Use an explicitly authorized test host for a Docker mutation. |
| Downloads | Exercise single-file regression, empty directories, nested files, symlinks/special files, path traversal/collision, malformed streams, changed hashes, destination contention and verified permissions. |
| Visual review | Before implementation query a fresh existing Graphify graph using the pinned 0.9.73 runtime with GRAPHIFY_NO_AUTO_REFRESH=1 on every invocation. Fall back to targeted source reads when no graph matches. Build the Floorplan blueprint in the private external workspace with Ask off. Show-me Mermaid is in the conversation. Deliver and visually check a local Archify showcase workflow after the flow stabilizes. Run local PR Lens 0.11.0 against distinct real base and implementation head after authorized local commit, before push. Record it as pending while no valid head exists. |

## Reviewer Handoff

{"verdict":"approved|needs-rework","blocking_issues":[],"copilot_feedback_triage":{"ADDRESS":[],"DISCUSS":[],"SKIP":[]}}

## Post-merge / release actions

Stable-library impact is none. This workflow ends at the authorized Draft PR for human review.

## Open Questions / Unresolved Items

Native Codex invocation of the reviewed skill, actual GUI permission and password isolation on the user's desktop, and the external SSH/Docker matrix require recorded environment-specific evidence. Mark unavailable cases pending in the draft.
