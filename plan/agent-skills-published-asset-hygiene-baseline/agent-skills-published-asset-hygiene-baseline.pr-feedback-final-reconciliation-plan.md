# Agent Skills Published Asset Hygiene Baseline — PR #120 Final Reconciliation

## Classification

- **Status transition:** `pr-open` -> `needs-rework`
- **Severity / route:** `medium` / `PLANNER_REPLAN`
- **Current truth:** this is the sole active correction contract. Commit A/B,
  all prior hard-break repairs, and their correction artifacts remain retained
  historical truth and grant no implementation authority.

## Locked Scope

`skills/` remains canonical. `.github/skills/` and `.codex/skills/` are
compatibility projections and must follow canonical content.

The independent Implementer may modify exactly these three paths:

- `skills/python-pre-commit/references/version-pinning.md`
- `.github/skills/python-pre-commit/references/version-pinning.md`
- `.codex/skills/python-pre-commit/references/version-pinning.md`

In the canonical file, replace the single intentional Markdown
trailing-double-space source-of-truth break after `**Source of truth**` with a
literal `<br>`. Synchronize the exact canonical bytes to both projections.
This preserves rendering while allowing the root no-`exclude` hygiene hook to
remain active. No other content, Markdown structure, name, path,
cross-reference, hook, inventory, provenance, or planning artifact may be
changed by the Implementer.

## Final PR-Base Contract

Use merge-base `d177401ff56a221ce104555687655a8ea1a55fae` (`origin/dev` at
the time of this contract) for the final PR-base check.

- The published-skill diff contains exactly 46 assets: 40 hygiene-only assets
  and six explicit rendering-preservation exceptions.
- The six exception assets are the three
  `plan-step-tracker/examples.md` copies (six existing `<br>` markers each)
  and the three `version-pinning.md` copies (one `<br>` marker each after this
  repair).
- The remaining 40 published-skill assets may differ from the PR base only by
  trailing-whitespace removal, terminal-blank-line removal, or final-LF
  normalization. Existing GitHub CLI-path and GitHub-only serialization
  semantic divergences remain locked and are not normalized into canonical
  authority.
- Root `.pre-commit-config.yaml`, the 57-record canonical inventory, the
  eight-row Codex provenance update, and the exact planning artifact paths are
  separate, explicitly reviewed PR diff categories. Any other changed path is
  a blocker.

## Temporary All-Files Boundary

Run `pre-commit run --all-files` only in a disposable baseline Git workspace,
never in the feature worktree. The expected failure inventory is exactly:

- `.github/guides/MAIN-AGENT-WORKFLOW.md`
- `.github/guides/REFERENCE-INTAKE-PROCESS.md`
- `.github/prompts/create-agent-plan.prompt.md`
- `.gitignore`
- `analysis/agent-skill-migration-sequencing/requirements.md`
- `analysis/phase-2-planning-spine-exceptions/requirements.md`
- `analysis/phase-2-planning-spine-exceptions/technical-spec.md`
- `analysis/plan-step-tracker/requirements.md`
- `analysis/plan-step-tracker/technical-spec.md`
- `analysis/python-retrofit-plan-review/requirements.md`
- `analysis/python-tooling-skills/technical-spec.md`
- `analysis/python-workflow-enhancement/requirements.md`
- `docs/process/next-agent-follow-up.md`
- `plan/agent-handoff-workflow.md`
- `plan/python-docstrings/python-docstrings.plan.md`
- `plan/python-retrofit-plan-review/python-retrofit-plan-review.plan.md`
- `plan/reference-intake-workflow/reference-intake-workflow.plan.md`

Do not repair, suppress, retain, or add an `exclude` for any of these paths.
The disposable workspace is discarded; the feature worktree must have no diff
for all 17 paths.

## Validation and Handoff

- Require `pre-commit validate-config`, a targeted three-file hook run, and
  `git diff --check` to pass without rewrite.
- Require byte equality between canonical `version-pinning.md` and both
  projections; each has exactly one literal `<br>` after `Source of truth`.
- In a consumer-like temporary Git workspace containing published assets and
  `.pre-commit-config.yaml`, baseline then run all hooks; require success,
  empty `git status --short`, and successful `git diff --exit-code`.
- The Reviewer verifies the three-path implementation boundary, the exact
  17-path temporary inventory, the 40/6 PR-base asset classification, and
  absence of unclassified PR-base diff paths. Then it appends its JSON verdict
  to the review log.

```json
{"verdict":"approved|needs-rework","blocking_issues":[],"pr_base":"d177401ff56a221ce104555687655a8ea1a55fae","published_asset_classification":{"hygiene_only":40,"rendering_exceptions":6}}
```

## Exclusions / Stop Rule

This is a non-stable-library correction: no CI, fixture, README, VERSION, tag,
release, merge, or new projection is authorized. A missing projection, a
different temporary inventory, a non-format asset diff, or any unclassified
PR-base path stops the route and returns to Planner. On `approved`, the Main
Agent resumes PR thread handling; it resolves only satisfied threads and
leaves scoped replies for unresolved actionable threads.
