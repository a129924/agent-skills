# Topic Plan Contract

`contract_version`: `1.0`

This file is the shared repo-local authority for topic-plan structure,
review basis, fallback behavior, and contract-level blocking semantics.

It complements `plan/agent-handoff-workflow.md`:

- `plan/agent-handoff-workflow.md` defines repo-level workflow states,
  ownership, stop points, and artifact semantics.
- this file defines the canonical topic-plan section contract and the contract
  rules that both `plan-creator` and `plan-reviewer` must apply.

Neither `plan-creator` nor `plan-reviewer` may treat the other skill as a
required contract source.

## Required Sections

Every repo-visible topic plan must include these sections exactly:

1. `Goal / Outcome`
2. `Scope`
3. `Locked Decisions`
4. `Boundaries / Exclusions`
5. `Status / Allowed Transitions`
6. `Artifact Paths`
7. `Implementation Steps`
8. `Validation / Acceptance Checks`
9. `Reviewer Handoff`
10. `Post-merge / release actions`
11. `Open Questions / Unresolved Items`

If stable-library or release behavior applies, the plan must also include:

- `Stable library metadata`

If stable-library or release behavior does not apply, the plan must make that
absence explicit rather than leaving it implied.

## Shared Review Basis

Both planning skills must evaluate topic plans against this shared basis:

1. `plan/agent-handoff-workflow.md`
2. `plan/topic-plan-contract.md`
3. the local skill's own examples, checklist, template, and references

Local skill files may add implementation guidance or review heuristics, but
they must not redefine required sections, role ownership, fallback authority,
or blocking semantics away from this file.

## Artifact Path Rules

`Artifact Paths` is an executable contract.

Each listed artifact must include:

- exact repo-visible path
- owner
- role

Do not use vague labels such as `docs`, `skill folder`, `maybe version files`,
or other non-executable path descriptions.

If execution needs files outside the listed paths, repair the topic plan before
continuing.

## Reviewer Handoff Contract

`Reviewer Handoff` must be a single machine-consumable JSON object.

At minimum it must support:

- reviewer decision routing
- blocking issues
- follow-up ownership

Do not replace the JSON object with prose notes, tables, or mixed formats.

## Stable-Library Contract

If the topic affects stable-library surfaces, the plan must state:

- whether `README.md` changes
- whether `VERSION` changes
- when those changes occur
- whether post-merge release or tagging work exists

Do not defer these decisions with placeholders such as `TBD`, `later`, or
`follow normal process`.

## Fallback Rules

If the local topic-plan template is absent:

- `plan-creator` must fall back to the required section list in this file
- `plan-reviewer` must review against the required section list in this file

Neither skill may invent a new topic-plan shape when the template is absent.

## Blocking Semantics

Treat these as contract-breaking issues:

- missing required sections
- non-canonical or invalid status transitions
- vague or drifting `Artifact Paths`
- undeclared or mixed stable-library intent
- non-JSON reviewer handoff
- wrong post-merge or release timing
- mixed role ownership
- placeholders where explicit contract is required

`plan-creator` must stop and ask when required planning inputs are missing or
would require guessing.

`plan-reviewer` must return `needs-rework` when any contract-breaking issue is
found in an otherwise reviewable plan.

If the plan file or required shared contract sources cannot be read, stop and
record that the review could not proceed on valid contract grounds.

## Authority Boundaries

- Keep this contract repo-local.
- Do not externalize it to `~/.` or cross-repo shared storage in this topic.
- Do not let compatibility surfaces redefine this contract.
- Do not infer authority from `.github/skills/` or `.codex/skills/` presence.
