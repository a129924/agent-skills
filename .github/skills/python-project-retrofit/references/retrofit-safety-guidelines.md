# Retrofit Safety Guidelines

Use this reference for every destructive or potentially destructive retrofit
operation.

## Gate 3: Git safety is mandatory

Before any move, deletion, or overwrite, inspect the Git working tree.

### Clean state

If the working tree is clean:

- continue to the human-approved destructive step
- keep the planned rollback or backup note alongside the operation record

### Dirty state

If the working tree is dirty:

- hard-block the retrofit
- explain which destructive step was about to run
- require one of the following human-approved recovery paths before continuing:
  - commit the existing changes
  - produce a backup

This gate cannot be bypassed.

## Destructive-operation list

Treat these actions as destructive and gate them accordingly:

- moving files or directories when the source path would disappear
- deleting legacy files, directories, or local environments
- overwriting config files such as `pyproject.toml`, `setup.cfg`, or `requirements.txt`
- replacing entrypoints or package roots
- collapsing two config surfaces into one survivor file

If an action could lose information or make rollback harder, treat it as
pre-destructive even when the filesystem command looks simple.

## Backup expectations

A backup path is acceptable only when it is explicit and human-approved.

Minimum expectations:

- the backup target is named clearly enough for the human to find later
- the backup happens before the destructive step
- the skill confirms the backup completed
- the skill reruns the pre-destructive safety check after the backup path is ready

Backup does not replace the gate answers for shadow or config conflicts.

## Recommended safety sequence

1. resolve Gate 1 shadow conflicts
2. resolve Gate 2 config-remnant decisions
3. identify the exact destructive step to run next
4. inspect Git state immediately before that step
5. if dirty, stop for commit-or-backup handling
6. if clean or backed up, perform only the approved step
7. record the operation for the Delta Report

## Clear blocking language

Prefer explicit wording such as:

```text
Retrofit blocked: Git working tree is dirty.
Pending destructive step: move app.py -> src/weather_service/main.py
Required next action: commit current changes or create a backup before retrying.
```

Avoid soft wording such as “warning” or “recommended”.

## Failure handling

If a destructive step fails after approval:

- stop immediately
- report what changed and what did not
- preserve enough context for rollback or manual recovery
- do not continue to later destructive steps just because some work succeeded

## Non-goals

This skill does not:

- invent backup locations without human awareness
- bypass Git safety because the diff seems small
- rewrite Git history
- treat untracked local environments such as `.venv` as safe to delete without an explicit decision
