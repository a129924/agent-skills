# Agent-Skills Transition Overlay

## Purpose

Define the repository-specific gate that applies when a migration workflow runs
inside the `agent-skills` transition from `.github/skills/` toward `skills/`.

This overlay exists to keep migration execution compatible with the repository's
frozen positioning and governance rules while generic migration workflows remain
repository-agnostic.

## When This Overlay Is Bound

Bind this overlay when both are true:

- the workflow run uses a migration workflow under `docs/process/workflows/`
- the approved topic changes, verifies, or classifies artifacts whose meaning
  depends on the transition-era boundary between `.github/skills/` and
  `skills/`

Typical bound topics include:

- direct-move or rewrite-spec migration topics for skill folders
- same-name or contract-surface remediation topics that compare `.github/skills/`
  and `skills/`
- transition topics whose acceptance depends on preserving current-path versus
  target-architecture wording

Do not bind this overlay for topics whose approved scope is unrelated to the
transition boundary. In that case, record:

- `overlay_bound: false`
- `overlay_result: skipped-not-bound`

## Required Read Basis

When this overlay is bound, review against:

- `AGENTS.md`
- `docs/repo-positioning.md`
- the approved topic plan
- any topic-owned `requirements.md`, `technical-spec.md`, `step.md`, and
  `summary.md` that the approved plan declares as current truth

Hidden chat context must not override these repo-visible inputs.

## Required Overlay Output

The workflow run must record a repo-visible overlay result at:

- `.workflow-runs/<run-id>/overlay-gate.md`

The overlay result must include at minimum:

- topic
- workflow
- run id
- `overlay_result`
- gate checks performed
- final decision

The workflow `status.json` should also record:

- `overlay_bound`
- `overlay_result`
- `overlay_gate_path` when `overlay_bound=true`

## Gate Checks

When bound, the overlay must check all of the following.

### 1. Topic scope stayed inside the approved writable set

- No file outside the approved topic plan write set was modified except the
  workflow-run evidence files for the active run.
- No shared governance file was edited unless the approved topic plan listed it
  explicitly as writable scope.

### 2. Transition-era positioning stayed intact

- No artifact claims `skills/` is already the current active authored or
  reviewed workflow path unless an approved topic explicitly owns that
  governance change.
- No artifact claims `.github/skills/` has already ceased to be the current
  active Copilot path unless an approved topic explicitly owns that governance
  change.
- No artifact implies repo-wide cutover by silence or shorthand.

### 3. Migration meaning stayed bounded

- The implementation does not silently widen from the approved candidate set to
  additional skills, folders, or governance surfaces.
- The implementation does not redefine planner-locked exclusions such as
  C-class skills or forbidden shared files.
- The implementation does not treat verification, checklisting, or remediation
  as permission to perform a broader skill migration than the approved topic
  allows.

### 4. Skill-authority boundaries stayed intact

- No `SKILL.md` authority or source-of-truth change was introduced unless the
  approved topic explicitly owns that contract change.
- No creator / reviewer / template path transition was introduced unless the
  approved topic explicitly owns it.

## Decision Rules

### `passed`

Record `overlay_result: passed` only when all gate checks pass and the topic's
implemented result remains compatible with `AGENTS.md`, `docs/repo-positioning.md`,
and the approved topic contract.

### `blocked`

Record `overlay_result: blocked` when any gate check fails, including:

- out-of-scope file edits
- unauthorized shared-governance edits
- unauthorized active-path cutover claims
- silent candidate-set widening
- unauthorized `SKILL.md` authority change

When blocked, the workflow must stop with `human-feedback-required` or route to
the planner according to the parent workflow's stop rules.

### `deferred`

Record `overlay_result: deferred` only when the workflow cannot determine pass
or block from repo-visible evidence alone and a planner or human decision is
required to resolve an authority ambiguity.

Use `deferred` sparingly. Missing repo-visible evidence is not a pass.

## Minimal Decision Template

Use this shape in `.workflow-runs/<run-id>/overlay-gate.md`:

```md
# Overlay Gate Result

- topic: `<topic>`
- workflow: `<workflow>`
- run_id: `<run-id>`
- overlay_result: `passed|blocked|deferred`

## Gate Checks

- [result of check 1]
- [result of check 2]
- [result of check 3]
- [result of check 4]

## Decision

[One short paragraph stating why the topic passed, blocked, or deferred.]
```

## What This Overlay Must Not Do

- Do not choose the migration topic.
- Do not replace the approved topic plan.
- Do not authorize implementation work beyond the approved topic.
- Do not redefine generic migration workflow states.
- Do not treat the target architecture as permission to declare cutover
  complete today.
