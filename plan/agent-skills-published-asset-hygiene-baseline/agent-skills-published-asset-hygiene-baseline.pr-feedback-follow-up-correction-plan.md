# Agent Skills Published Asset Hygiene Baseline — PR #120 Current Correction

## Classification

- **Status transition:** `pr-open` -> `needs-rework`
- **Severity / route:** `medium` / `PLANNER_REPLAN`
- **Historical status:** Commit A and Commit B completed and were pushed. The
  subsequent review routing found that the three `version-pinning.md` surfaces
  must preserve their rendered source-of-truth break explicitly. This contract
  is superseded by
  `agent-skills-published-asset-hygiene-baseline.pr-feedback-final-reconciliation-plan.md`.
  It grants no further implementation or PR-thread authority.

## Locked Scope

The correction preserves Markdown soft breaks that are meaningful published
skill content while keeping the hygiene hook active for every repository path.
`skills/` remains canonical. `.github/skills/` and `.codex/skills/` are only
existing compatibility projections and must be synchronized from canonical.

### Commit A — hook policy and source/projection correction

The independent Implementer may modify exactly these seven paths:

- `.pre-commit-config.yaml`
- `skills/git-branch-naming/SKILL.md`
- `.github/skills/git-branch-naming/SKILL.md`
- `.codex/skills/git-branch-naming/SKILL.md`
- `skills/git-commit-convention/SKILL.md`
- `.github/skills/git-commit-convention/SKILL.md`
- `.codex/skills/git-commit-convention/SKILL.md`

Required changes:

1. Add `args: [--markdown-linebreak-ext=md]` only to the existing
   `trailing-whitespace` hook. Retain `pre-commit/pre-commit-hooks` `v4.6.0`,
   the existing two hooks, their order, and no `exclude`.
2. In each `git-branch-naming` copy, restore exactly one Markdown soft break:
   the `PASS:` validation-result line must end with exactly two ASCII spaces
   before its final LF. `SOFT FAIL:` and `BLOCKED:` remain single physical
   lines without a trailing double-space marker.
3. Apply the corresponding one-line `PASS:` soft-break restoration to each
   `git-commit-convention` copy under the same rule.
4. The canonical copy is edited first. Its `.github` and `.codex` copies must
   be byte-identical to it after the change. No other text, Markdown structure,
   naming, cross-reference, behavior, or projection-specific exception changes.

Commit A contains exactly those seven paths and is committed before provenance
is written. Its immutable SHA is the upstream source reference for Commit B.

### Commit B — deterministic inventory and projection provenance

After Commit A exists, the Implementer may modify exactly these two generated
artifacts:

- `artifacts/skills-inventory.jsonl`
- `.codex/skills/provenance.md`

1. Rebuild `artifacts/skills-inventory.jsonl` with
   `python3 scripts/build_skills_inventory.py`. It must remain a complete,
   sorted 57-record canonical inventory; it is not a nine-line subset. Only
   the eight affected canonical skill records may receive new tree hashes:
   `git-branch-naming`, `git-commit-convention`, `plan-step-tracker`,
   `python-docstrings`, `python-generators-iterators`, `python-plan-authoring`,
   `python-pre-commit`, and `python-tdd-test-authoring`.
2. Revalidate exactly these eight existing provenance rows against Commit A and
   update only their `source_commit` and `validation_basis` fields:
   `git-branch-naming`, `git-commit-convention`, `plan-step-tracker`,
   `python-docstrings`, `python-generators-iterators`, `python-plan-authoring`,
   `python-pre-commit`, and `python-tdd-test-authoring`. The GitHub-only
   `python-serialization-boundaries/REVIEW.md` hygiene change has no canonical
   source change and must not receive an inventory or Codex-provenance update.
   Any request for a ninth record or row stops for human governance check.
3. Commit B contains exactly these two paths. Its provenance references the
   actual Commit A SHA, not a placeholder and not Commit B's self SHA.

## Out of Scope

- The completed `plan-step-tracker/examples.md` `<br>` repairs and all earlier
  correction artifacts.
- The frozen 24 non-skill hygiene paths: do not repair them, add an exclusion,
  or retain their rewrites in the feature worktree.
- Any CI, fixture, README, VERSION, tag, release, PR metadata, or workflow
  redesign.
- Any implementation path outside the Commit A or Commit B write sets. The
  only post-implementation exceptions are: after Commit B, the named Planner
  may update this paired correction-step artifact with factual evidence; after
  that record is complete, the independent Reviewer may append its JSON verdict
  and rationale to the topic review log. No other non-A/B write is authorized.

## Validation and Handoff

- `pre-commit validate-config` passes. With the revised hook configuration,
  `pre-commit run --files` over the six SKILL.md paths passes without rewrite
  and preserves the two intended `PASS:` soft breaks per three projections.
- `git diff --check` passes. The canonical and both projection copies are
  byte-identical for each of the two scoped skills.
- The inventory rebuild parses as 57 sorted unique canonical records and is
  byte-identical to a second builder run. Its changed-record set is exactly the
  eight named canonical skills; all other inventory rows are byte-identical to
  the pre-Commit-B artifact.
- Exactly the eight named provenance table rows change; each source commit is
  Commit A and each validation basis records the bounded hygiene
  revalidation. No other provenance row changes.
- In an isolated full-repository Git workspace with a baseline commit,
  `pre-commit run --all-files` may fail only on the frozen 24 non-skill paths;
  it must not rewrite published skill assets. Discard the workspace. The
  feature worktree has no diff among the 24 paths.
- In a consumer-like temporary Git workspace, copy the published assets and
  root config, create a baseline commit, run `pre-commit run --all-files`, and
  require success, empty `git status --short`, and `git diff --exit-code`.
- The Implementer returns factual command and validation evidence only; it does
  not edit planning artifacts. After implementation, the named Planner
  records factual progression and evidence in the paired correction step. The
  independent Reviewer verifies both commit boundaries, all exact write sets,
  and the returned evidence, then appends its JSON verdict to the review log.
  Any mismatch stops the correction and returns to Planner; no PR thread is
  resolved before approval. A non-A/B write other than the two named
  post-implementation records is a blocker, not an implied exception.
