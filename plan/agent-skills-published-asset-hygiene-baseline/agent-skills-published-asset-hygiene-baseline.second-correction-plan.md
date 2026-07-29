# Agent Skills Published Asset Hygiene Baseline — Second Correction Plan

## Classification

- **Severity:** `medium`
- **Routing state:** `PLANNER_REPLAN`
- **Closure status:** `resolved`
- **Trigger:** The historical first correction restored eight newly observed
  non-skill hook rewrites, but 16 of the frozen 24-path isolated all-files
  blocker inventory remain in the feature diff. This makes the first
  correction's restore-only scope insufficient for the final-diff contract.
- **Parent truth:**
  `agent-skills-published-asset-hygiene-baseline.plan.md` and its `.step.md`
  remain the execution-facing current truth. The first correction plan and
  step remain immutable historical truth. This second correction plan and its
  step are a separate historical correction record.

## Frozen Correction Direction

1. Treat all 24 non-skill paths as isolated `pre-commit run --all-files`
   blocker inventory only. They are out of scope for hygiene repair and must
   not remain in the final feature diff.
2. Preserve the approved root `.pre-commit-config.yaml` and every approved
   published-skill asset normalization, including the first correction's three
   `python-pre-commit` template final-LF changes and GitHub-only serialization
   review hygiene change.
3. Restore only the following remaining 16 paths to their `HEAD` pre-hook
   baseline. This is restoration, not a hygiene fix:
   - `.github/guides/MAIN-AGENT-WORKFLOW.md`
   - `.github/guides/REFERENCE-INTAKE-PROCESS.md`
   - `.github/prompts/create-agent-plan.prompt.md`
   - `analysis/creator-reviewer-template-platform-path-alignment/technical-spec.md`
   - `analysis/plan-step-tracker/requirements.md`
   - `analysis/plan-step-tracker/technical-spec.md`
   - `analysis/platform-projection-adapter/technical-spec.md`
   - `analysis/python-descriptors-attribute-access/requirements.md`
   - `analysis/python-descriptors-attribute-access/technical-spec.md`
   - `analysis/python-implementation-workflow-sdd-tdd/technical-spec.md`
   - `analysis/python-tooling-skills/technical-spec.md`
   - `analysis/spec-docs-mvp-generator/requirements.md`
   - `analysis/spec-docs-mvp-generator/technical-spec.md`
   - `plan/agent-handoff-workflow.md`
   - `plan/python-docstrings/python-docstrings.plan.md`
   - `plan/reference-intake-workflow/reference-intake-workflow.plan.md`
4. Do not re-run or retain a broad all-files rewrite in the feature worktree.
   The existing isolated-workspace inventory evidence remains the validation
   record for the 24 blockers.

## Boundaries

- The Implementer may change only the 16 restore-only paths and
  `agent-skills-published-asset-hygiene-baseline.second-correction-step.md`.
- It must not modify either first-correction artifact, the parent plan, the
  topic step, or the review log.
- It must not repair any of the 24 non-skill files, change a skill asset or
  projection, alter root hook configuration, or make semantic, structural,
  release, CI, fixture, README, VERSION, tag, commit, push, or PR changes.
- Any mismatch between the frozen 24-path inventory and the post-restore diff,
  or any change outside these 16 paths plus the second correction step, stops
  work and returns to Planner.

## Required Handoff and Closure

- A separate Implementer restores the 16 named paths and updates only the
  second correction step with command output and the 24-path empty-diff
  evidence.
- Review readiness requires `git diff --name-only` over the complete 24-path
  inventory to produce no output, while approved published-skill assets and
  `.pre-commit-config.yaml` remain in the feature diff.
- A separate Reviewer returns the exact parent-plan JSON verdict and appends
  its result to the review log. Planner may mark this second correction
  `resolved` only after review and parent synchronization; neither correction
  record may be deleted.

## Resolution Record — 2026-07-29

The independent Reviewer returned the parent-plan `approved` verdict with no
blocking issues. The exact JSON and its validation basis are retained in
`agent-skills-published-asset-hygiene-baseline.review-log.md`. Parent current
truth and this historical correction record are synchronized: the correction
is resolved, while Phase 4.5 planner contract alignment remains the next
workflow gate. No historical correction fact has been replaced or deleted.
