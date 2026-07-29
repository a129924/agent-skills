# Agent Skills Published Asset Hygiene Baseline — PR #120 Feedback Correction

## Classification

- **Status transition:** `pr-open` -> `needs-rework`
- **Severity / route:** `medium` / `PLANNER_REPLAN`
- **Trigger:** P2-1 on Ready PR #120 identifies a Markdown rendering regression
  in canonical `skills/plan-step-tracker/examples.md`: hygiene normalization
  removed two hard-break markers from its `Output` / `Exit code` / `Note`
  three-line block. The locked canonical/projection model requires the same
  bounded `<br>` repair in its two existing projections.
- **Other P2 disposition:** P2-2 (human publish authorization and current
  `needs-rework` state) and P2-3 (portable `pre-commit` / writable cache
  prerequisite) are Planner-owned and resolved in the parent plan and topic
  step. They create no Implementer write path.
- **Current truth:** the parent plan remains the execution authority. This
  correction freezes only the PR-feedback delta below and becomes historical
  after independent Reviewer approval.

## Locked Implementation Contract

The independent Implementer may modify only these files:

- `skills/plan-step-tracker/examples.md`
- `.github/skills/plan-step-tracker/examples.md`
- `.codex/skills/plan-step-tracker/examples.md`

In each file, modify only the consecutive block immediately following the
`read_all` Python CLI example:

1. Replace the two trailing-double-space Markdown hard-break markers after the
   `**Output**: 11 lines ...` and `**Exit code**: 0` lines with literal `<br>`.
2. Leave the following `**Note**: ...` line unchanged, so the block still
   renders as three separate lines: Output, Exit code, Note.
3. Make the affected three-line block byte-identical in all three files.

The pre-existing GitHub-specific Python CLI path elsewhere in its example file
is a locked semantic divergence and must remain untouched. No other hard-break
region, asset, root config, planning architecture, workflow artifact, or PR
metadata is in scope for Implementer modification.

## Validation Contract

- Prerequisite: `pre-commit` resolves on `PATH`, and `PRE_COMMIT_HOME` names a
  writable cache directory.
- `pre-commit validate-config` succeeds.
- Run `pre-commit` against exactly the three implementation paths; it succeeds
  without modifying them.
- `git diff --check` succeeds.
- Verify the three affected blocks are byte-identical and contain exactly two
  `<br>` tags, after the Output and Exit code lines respectively.
- Verify the three-line rendered result is preserved. Full-file equality is
  not required because the locked GitHub CLI-path divergence remains.
- Verify the diff contains no implementation path outside the three files and
  no root `.pre-commit-config.yaml` change.

## Handoff / Stop Rules

- Implementer records only factual command and result evidence in
  `agent-skills-published-asset-hygiene-baseline.pr-feedback-correction-step.md`.
- An independent Reviewer evaluates the exact write set and validation record,
  then appends its JSON verdict to
  `agent-skills-published-asset-hygiene-baseline.review-log.md`.
- Any required path outside this contract, a changed GitHub CLI path, a
  non-identical affected block, a failed hook, or a new unresolved PR issue
  stops the correction and returns to the Planning actor.
