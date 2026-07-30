# Agent Skills Published Asset Hygiene Baseline — PR #120 Final Reconciliation

## Classification

- **Status transition:** `pr-open` -> `needs-rework`
- **Severity / route:** `medium` / `PLANNER_REPLAN`
- **Current truth:** Commit C and dependent Commit D are completed historical
  truth. This plan is the sole active correction contract for Commit E and
  dependent Commit F; all earlier correction artifacts grant no implementation
  authority.

## Locked Scope

`skills/` remains canonical. `.github/skills/` and `.codex/skills/` are
compatibility projections and must follow canonical content.

Completed historical work was ordered as Commit C (the three
`version-pinning.md` paths) then dependent Commit D
(`artifacts/skills-inventory.jsonl` and `.codex/skills/provenance.md`). Commit
C replaced the source-of-truth break with `<br>` and synchronized projections;
Commit D rebuilt the 57-record inventory and updated the one eligible
`python-pre-commit` Codex provenance row to cite Commit C. These completed
paths are not reopened.

The independent Implementer may now modify exactly these six Commit E paths:

- `skills/git-branch-naming/SKILL.md`
- `.github/skills/git-branch-naming/SKILL.md`
- `.codex/skills/git-branch-naming/SKILL.md`
- `skills/git-commit-convention/SKILL.md`
- `.github/skills/git-commit-convention/SKILL.md`
- `.codex/skills/git-commit-convention/SKILL.md`

In each canonical source, replace only the intended `PASS:` Markdown
trailing-double-space break with literal `<br>`, then synchronize the exact
canonical bytes to both projections.

After Commit E is committed, the independent Implementer may modify exactly these
two dependent Commit F paths: `artifacts/skills-inventory.jsonl` and
`.codex/skills/provenance.md`. Commit F must deterministically rebuild the 57
canonical inventory records and update only the `git-branch-naming` and
`git-commit-convention` tree hashes and corresponding Codex provenance rows,
each citing Commit E. No other content, Markdown structure, name, path,
cross-reference, hook, planning artifact, or provenance row may be changed by
the Implementer.

## Final PR-Base Contract

Use merge-base `d177401ff56a221ce104555687655a8ea1a55fae` (`origin/dev` at
the time of this contract) for the final PR-base check.

- The published-skill diff contains exactly 46 assets: 34 hygiene-only assets
  and 12 explicit rendering-preservation exceptions.
- The 12 exception assets are the canonical, GitHub, and Codex copies of
  `git-branch-naming/SKILL.md`, `git-commit-convention/SKILL.md`,
  `plan-step-tracker/examples.md`, and
  `python-pre-commit/references/version-pinning.md`. The first two groups each
  contain one restored `PASS:` `<br>` marker; the step-tracker copies
  retain six `<br>` markers each; and the version-pinning copies retain one
  `<br>` marker each.
- The remaining 34 published-skill assets may differ from the PR base only by
  trailing-whitespace removal, terminal-blank-line removal, or final-LF
  normalization. Existing GitHub CLI-path and GitHub-only serialization
  semantic divergences remain locked and are not normalized into canonical
  authority.
- Root `.pre-commit-config.yaml`, the completed C/D generated artifacts, the
  active F two-row provenance update, and the exact planning artifact paths are
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

- Require `pre-commit validate-config`, a targeted six-file Commit E hook run,
  a targeted two-file Commit F generated-artifact validation, and `git diff
  --check` to pass without rewrite.
- Require byte equality between each canonical Commit E skill and both
  projections; each has exactly one literal `<br>` on its intended `PASS:`
  line. Retain the already-validated byte equality and one literal
  `<br>` after `Source of truth` in `version-pinning.md`.
- Require Commit F to produce 57 sorted unique inventory records, change only
  the two named canonical tree hashes, and update exactly their two Codex
  provenance rows to cite Commit E. A second deterministic build must be
  byte-identical.
- In a consumer-like temporary Git workspace containing published assets and
  `.pre-commit-config.yaml`, baseline then run all hooks; require success,
  empty `git status --short`, and successful `git diff --exit-code`.
- The Reviewer verifies the completed C3/D2 boundary, the active E6/F2
  implementation boundary, the exact 17-path temporary inventory, the 34/12
  PR-base asset classification, and absence of unclassified PR-base diff
  paths. Then it appends its JSON verdict to the review log.

```json
{"verdict":"approved|needs-rework","blocking_issues":[],"pr_base":"d177401ff56a221ce104555687655a8ea1a55fae","completed_commit_boundaries":{"C":3,"D":2},"active_commit_boundaries":{"E":6,"F":2},"published_asset_classification":{"hygiene_only":34,"rendering_exceptions":12}}
```

## Exclusions / Stop Rule

This is a non-stable-library correction: no CI, fixture, README, VERSION, tag,
release, merge, or new projection is authorized. A missing projection, a
different temporary inventory, a non-format asset diff, or any unclassified
PR-base path stops the route and returns to Planner. On `approved`, the Main
Agent resumes PR thread handling; it resolves only satisfied threads and
leaves scoped replies for unresolved actionable threads.
