# Authoring vs Executor Boundaries

Use this reference to keep Retrofit V2 planning scope separate from runtime
execution scope.

## Ownership split

| Question | Authoring skill | Executor skill |
| --- | --- | --- |
| Draft the Retrofit V2 contract headings and machine-readable blocks | Yes | No |
| Stop when the requested contract is too abstract to locate affected surfaces | Yes | No |
| Decide whether the request is retrofit or greenfield | Yes | No |
| Parse the approved V2 plan and execute filesystem changes | No | Yes |
| Run Shadow File Detection, Implicit Config Mining, and Git safety gates | No | Yes |
| Hard-block a `LOW` plan when runtime scanning discovers destructive actions | No | Yes |
| Run `sense-env-scaffold` acceptance | No | Yes |

## What authoring may declare

Authoring may declare:

- current observed facts in `## Survey Summary`
- concrete target-state paths, entrypoints, and config outcomes
- `Migration Direction` as strategy declaration
- candidate destructive surfaces in `destructive_actions`
- verifiable acceptance assertions

Authoring must not declare:

- that runtime gate answers are already decided
- that the executor may skip human confirmation because the plan is clear
- that the executor may auto-delete, auto-overwrite, or auto-merge conflicts

## Migration Direction boundary

Allowed:

```text
Migration Direction: staged package relocation with compatibility shim retained during transition
```

Not allowed as a runtime shortcut:

```text
Migration Direction: delete app.py automatically and ignore coexistence questions
```

`Migration Direction` explains strategy. It does not replace Gate 1 or Gate 2
outcomes, and it does not bypass destructive preview or authorization.

## Stop-and-ask triggers owned by authoring

Stop before drafting when any of these is true:

- the request lacks concrete paths, filenames, or tool names
- the target state cannot be verified with concrete sensing assertions
- the task is actually greenfield work
- the requested transformation contradicts current facts in a way that changes the contract materially
- the risk lane cannot be classified from observable physical traits

## Runtime matters that stay downstream

These belong to `python-project-retrofit`, not to authoring:

- current live conflict prompts such as `move | delete | coexist | abort`
- current live config decisions such as `migrate | delete | preserve | abort`
- destructive preview generation from the approved plan plus runtime scan
- dirty-worktree handling, backup creation, or commit-before-destructive sequencing
- acceptance execution and resulting pass/fail state

## Lifecycle boundary

This skill stops at `review-ready` and hands the draft forward. It does not
approve the plan and does not execute it.
