---
name: platform-projection-adapter
description: Project the canonical `skills/` library into a caller-specified platform root by running the local CLI in dry-run mode by default and only enabling writes with explicit `--apply` and `--force`.
complexity: high
risk_profile:
  - ambiguity_sensitive
  - destructive_action
  - external_tooling
  - code_modification
inputs:
  - the explicit `--platform-root` destination
  - whether the caller wants dry-run only or an actual apply
  - whether differing managed target files may be overwritten with `--force`
outputs:
  - a CLI summary with mode, target root, source count, action counts, and conflicts
  - a platform-root projection under `<platform-root>/skills/` when apply is explicitly authorized
use_when:
  - the task is to project the whole canonical `skills/` library into a concrete platform projection surface such as `.<platform>/skills/`
  - the caller needs a safe dry-run before any platform projection write
  - the caller needs to re-run projection and verify whether force is required
do_not_use_when:
  - the task is to edit canonical `skills/` content directly
  - the task is to project only one skill subset instead of the whole library
  - the task requires repo-visible edits under `.github/**`, `.<platform>/**`, `README.md`, or `VERSION`
---

# Purpose
Run the local projection CLI against the whole canonical `skills/` library without creating a second transformation path in the skill text.

# Trigger / When to use
Use this skill when:
- the task is to project the whole canonical `skills/` library into a caller-specified platform root
- the caller needs the default dry-run summary before deciding whether to apply
- the caller needs explicit `--apply` / `--force` gating for managed target files

Do not use this skill when:
- the task is to modify canonical `skills/` files directly
- the task wants partial-scope projection for only one skill folder
- the task expects target pruning, delete-sync behavior, or repo-visible platform-surface edits

# Inputs
- the explicit `--platform-root` destination
- whether the caller wants dry-run only or an actual apply
- whether differing managed target files may be overwritten with `--force`

# Process
1. Confirm the request is still within the bounded topic: whole-library projection from canonical `skills/`, explicit `--platform-root`, and no canonical-source rewrites.
2. Default to dry-run and invoke the projected local script path:
   `uv run .<platform>/skills/platform-projection-adapter/scripts/platform_projection_adapter.py --platform-root <path>`
3. Read the CLI summary and report `mode`, `platform_root`, `source_count`, `create`, `update`, `noop`, and `conflicts`.
4. Add `--apply` only when the caller explicitly authorizes writes.
5. Add `--force` only when the caller explicitly authorizes overwriting differing managed target files.
6. Treat the CLI as the only transformation core. Do not restate or fork placeholder rewrite, traversal, or conflict rules in this skill.
7. If the CLI reports `BLOCKED`, surface the reason and stop instead of improvising a second write path.

# Examples
- Positive: Run a dry-run against a caller-specified platform root, report the summary, then wait for explicit human authorization before adding `--apply`.
- Negative: Re-implement projection rules in `SKILL.md`, guess a platform root without `--platform-root`, or overwrite target files without explicit `--force`.

# Outputs
- a CLI summary with mode, target root, source count, action counts, and conflicts
- a platform-root projection under `<platform-root>/skills/` when apply is explicitly authorized

# Validation

## Required Checks
- `--platform-root` is explicit before invoking the CLI
- dry-run remains the default unless the caller explicitly requested `--apply`
- `--force` is used only with explicit overwrite authorization
- the skill delegates all transformation behavior to the CLI instead of duplicating logic

## Quality Checks (best effort)
- the summary explains whether apply is safe or blocked
- blocked runs surface the exact CLI reason instead of paraphrasing away the risk
- whole-library scope is preserved; no partial-skill routing is introduced

## On Soft Fail
- mark status as INCOMPLETE
- continue with the best available CLI summary
- list any missing authorization or path input explicitly

# Failure Handling

## Missing Context
- mark output as INCOMPLETE
- ask for `--platform-root` or missing apply/force authorization before proceeding

## Ambiguous Requirement
- if the caller mixes canonical-source edits with platform projection, stop and ask which task is in scope
- if the caller asks for subset projection or delete-sync behavior, stop and note that the request is outside this v1 skill boundary

## Execution Limitation
- state the CLI failure or local tooling limitation explicitly
- do not fabricate a projection result when the CLI did not complete successfully

# Workflow State Contract

When participating in multi-agent workflows, include:
- current_step: one short statement of the CLI phase being executed
- next_step: the next required authorization or `DONE`
- status: IN_PROGRESS | COMPLETE | INCOMPLETE | BLOCKED

Omit this section if the skill is not being used in a multi-agent handoff.

# Verification
- Re-read the CLI summary before claiming apply succeeded.
- If apply failed mid-run, re-run dry-run and report the recomputed state rather than assuming completion.

# Red Flags
- guessing a concrete platform surface without `--platform-root`
- editing canonical `skills/` because a target file conflicts
- treating `--force` as permission to delete extras or widen the source scope

# Boundaries
- Do not create a second projection algorithm in the skill text.
- Do not modify canonical `skills/` content as part of projection.
- Do not narrow the scope to one skill subset.
- Do not delete extra files under the target root.
- Do not claim success when the CLI reports `BLOCKED` or local execution failed.

# Local references
- `reference.md`: CLI contract, summary fields, and bounded behavior notes
- `examples.md`: dry-run, apply, force, and blocked usage patterns
- `scripts/platform_projection_adapter.py`: the sole projection core used by this skill; it must remain runnable from both `skills/...` and `.<platform>/skills/...`
