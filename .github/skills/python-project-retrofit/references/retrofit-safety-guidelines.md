# Retrofit Safety Guidelines

Use this reference for every destructive or potentially destructive retrofit
operation under Retrofit V2.

## Risk metadata drives the confirmation lane

Read `yaml [migration-strategy]` before executing anything:

- `LOW` means additive or non-destructive work only
- `HIGH` means the retrofit includes destructive actions that require preview and explicit authorization
- `MEDIUM` is not executable in the current contract version

Expected current pairing:

- `LOW` -> `destructive_actions: []` and `backup_required: false`
- `HIGH` -> non-empty `destructive_actions` and `backup_required: true`

## Risk Alignment Check is mandatory

Before Gate 1 or Gate 2 proceeds, compare the declared risk metadata to the
runtime scan.

If the contract says `LOW` but execution would require a move, delete,
overwrite, directory relocation, or equivalent destructive step:

- hard-block the retrofit
- explain the mismatch concretely
- require plan or risk correction before continuing

Do not silently promote the plan to `HIGH` inside execution.

## LOW lane

If the contract remains aligned to `LOW` after scanning:

- use the lightweight confirmation path
- keep work additive or non-destructive
- if scanning or later analysis shows any move, delete, overwrite, relocation, or equivalent destructive action would occur, stop before Gate 3 or any destructive flow
- require plan and risk metadata repair before retrying, for example by updating the contract to `HIGH` and populating `destructive_actions`

## HIGH lane

If the contract is `HIGH`:

- build a destructive preview from `destructive_actions` plus the current scan
- show the preview before any destructive step runs
- require explicit human authorization for the approved destructive scope
- keep the preview concrete enough that the human can see which files or directories are at risk

Example preview language:

```text
Planned destructive actions:
- move app.py -> src/weather_service/main.py
- replace requirements.txt with pyproject.toml
Required next step: explicit approval for this destructive scope.
```

`backup_required: true` means the executor must verify a recovery path exists
before destructive execution. In practice, that recovery path is satisfied by a
clean committed state or a human-approved backup created before retrying.

## Gate 3: Git safety is mandatory

Before any move, deletion, or overwrite, inspect the Git working tree.

### Clean state

If the working tree is clean:

- continue to the approved destructive step
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

Backup does not replace Gate 1 answers, Gate 2 answers, destructive preview,
or explicit authorization.

## Failure handling

If a destructive step fails after approval:

- stop immediately
- report what changed and what did not
- preserve enough context for rollback or manual recovery
- do not continue to later destructive steps just because some work succeeded

## Non-goals

This skill does not:

- invent backup locations without human awareness
- bypass Risk Alignment Check because the draft “looks close enough”
- bypass Git safety because the diff seems small
- rewrite Git history
- treat untracked local environments such as `.venv` as safe to delete without an explicit decision
