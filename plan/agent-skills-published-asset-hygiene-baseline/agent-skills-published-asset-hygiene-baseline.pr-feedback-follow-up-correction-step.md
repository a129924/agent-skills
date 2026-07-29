# Agent Skills Published Asset Hygiene Baseline — PR #120 Current Correction Steps

## Correction Workflow

- [X] Planner classified the current route as `medium` `PLANNER_REPLAN` and
  synchronized the parent plan and topic step.
- [X] Independent Implementer completed Commit A's exact seven-path change in
  `86184c96ca5d8236d1ce7102b29992ad71d467d4`.
- [X] Independent Implementer completed Commit B's exact two-path generated
  artifact update in `6a255979e05cafcfe5dd991b951cb3af9f0ac9da`, referencing
  Commit A.
- [X] Planner recorded the factual validation evidence for both commits, the
  57-record / eight-row invariants, temporary full-repository inventory, and
  consumer-like passing gate below.
- [X] Review routing returned `needs-rework`: the original three
  `version-pinning.md` Markdown source-of-truth breaks require explicit
  `<br>` preservation in canonical and both projections.
- [X] Planner transferred the remaining work to the final-reconciliation
  contract; this historical step has no remaining write authority.

## Post-implementation Record Ownership

- The Implementer returns validation evidence only and must not edit this
  correction step, the parent plan, review log, or any other planning artifact.
- The named Planner records the Implementer's factual progression and
  evidence in this correction step after both implementation commits exist.
- The independent Reviewer records only its JSON verdict and review rationale
  in `agent-skills-published-asset-hygiene-baseline.review-log.md` after the
  Planning actor's evidence record is complete.
- These record-ownership actions are post-implementation workflow writes. They
  are not part of Commit A's seven-path set or Commit B's two-path set. They
  are the only non-A/B writes authorized: Planner may write this correction
  step only after Commit B, then Reviewer may append only its JSON verdict and
  rationale to the review log. No other non-A/B write is authorized.

## Implementer Scope

### Commit A

- `.pre-commit-config.yaml`
- `skills/git-branch-naming/SKILL.md`
- `.github/skills/git-branch-naming/SKILL.md`
- `.codex/skills/git-branch-naming/SKILL.md`
- `skills/git-commit-convention/SKILL.md`
- `.github/skills/git-commit-convention/SKILL.md`
- `.codex/skills/git-commit-convention/SKILL.md`

Add only `args: [--markdown-linebreak-ext=md]` to `trailing-whitespace` and
restore exactly the one `PASS:` Markdown soft break in each copy of each named
skill. The two projections of each skill must become byte-identical to its
canonical source.

### Commit B

- `artifacts/skills-inventory.jsonl`
- `.codex/skills/provenance.md`

Run the existing canonical inventory builder after Commit A. The complete
artifact must have 57 sorted unique records, with changed tree hashes only for
the eight canonical skills named in the correction plan. Update exactly the
same eight existing Codex provenance rows to reference Commit A. GitHub-only
serialization is not canonical and must not create a ninth record or row.

## Required Validation Evidence

- `pre-commit validate-config`, targeted six-file hook run, and
  `git diff --check` pass without rewrites.
- Each named canonical SKILL.md is byte-identical to its two projections; only
  its `PASS:` line has two trailing spaces before LF.
- A second inventory builder run is byte-identical to Commit B's 57-record
  artifact; exactly the required eight hashes and eight provenance rows differ
  from the Commit-A baseline.
- In a temporary full-repository Git workspace, all-files hooks do not rewrite
  published skill assets and may affect only the frozen 24 non-skill paths;
  discard it. The feature worktree has zero diff for those 24 paths.
- In a consumer-like temporary Git workspace, baseline then run all hooks;
  hooks pass, `git status --short` is empty, and `git diff --exit-code`
  succeeds.

## Post-implementation Evidence

- Commit A changes exactly its seven authorized paths. At the Commit B
  configuration, `pre-commit validate-config` and `git diff --check` passed.
  In a temporary checkout at Commit B, the targeted `pre-commit run --files`
  over the six scoped `SKILL.md` paths passed without rewrite. `cmp` confirmed each canonical
  `git-branch-naming` and `git-commit-convention` `SKILL.md` is byte-identical
  to both projections, including the intended `PASS:` Markdown soft break.
- Commit B changes exactly `artifacts/skills-inventory.jsonl` and
  `.codex/skills/provenance.md`. A second
  `python3 scripts/build_skills_inventory.py` run wrote 57 sorted records to a
  temporary output that was byte-identical to the committed inventory. Compared
  with Commit A, exactly these eight canonical records changed tree hash:
  `git-branch-naming`, `git-commit-convention`, `plan-step-tracker`,
  `python-docstrings`, `python-generators-iterators`,
  `python-plan-authoring`, `python-pre-commit`, and
  `python-tdd-test-authoring`. The provenance diff has exactly eight rows
  (16 removed/added table lines), and every updated row references `86184c9`.
- In a temporary full-repository checkout at Commit B,
  `pre-commit run --all-files` exited 1 and rewrote 17 paths, all a subset of
  the frozen 24 non-skill inventory; no path under `skills/`,
  `.github/skills/`, or `.codex/skills/` was rewritten. The temporary workspace
  was discarded. In the feature worktree, the complete frozen 24-path
  restricted diff is empty; the only remaining worktree paths are the five
  authorized planning artifacts.
- In a consumer-like temporary Git workspace containing the published assets
  and root configuration, baseline commit then `pre-commit run --all-files`
  passed. `git status --short` was empty and `git diff --exit-code` succeeded.

## Reviewer Handoff

```json
{"status":"ready-for-independent-review","commit_a":"86184c96ca5d8236d1ce7102b29992ad71d467d4","commit_b":"6a255979e05cafcfe5dd991b951cb3af9f0ac9da","evidence":"recorded","full_repository_result":"expected non-skill-only failure (17 paths, subset of frozen 24)","consumer_gate":"passed"}
```

## Handoff / Gate Notes

- The parent plan is current truth; earlier correction artifacts are immutable
  historical truth. This route is superseded by
  `agent-skills-published-asset-hygiene-baseline.pr-feedback-final-reconciliation-plan.md`.
- Any changed path outside its Commit A/B sets, inventory cardinality or hash
  mismatch, non-identical projection, ninth provenance request, 24-path diff,
  or consumer-gate failure stops the route and returns it to Planner. The only
  exception is the sequenced Planner correction-step update and Reviewer
  review-log append defined above; any other non-A/B write is a blocker. A
  ninth inventory/provenance record requires human governance check.
