# Agent Skills Published Asset Hygiene Baseline

## Analysis-Layer Routing

**Semantic warning:** neither
`analysis/agent-skills-published-asset-hygiene-baseline/requirements.md` nor
`analysis/agent-skills-published-asset-hygiene-baseline/technical-spec.md`
exists. This plan therefore uses the explicit human-frozen correction direction
as its planning input; it does not infer any further implementation scope from
an absent analysis layer.

## Goal / Outcome

Establish a hygiene baseline for all published Agent Skill assets.  Every
in-scope canonical asset under `skills/` must have only trailing-whitespace and
EOF normalization, and its existing compatibility projections must receive the
same hygiene result. A consumer-like Git workspace must run the root hooks
without modifying published assets.

## Scope

- **In scope**:
  - The completed final-reconciliation route is historical evidence: Commit C
    changed the three `version-pinning.md` surfaces, then dependent Commit D
    refreshed the canonical inventory and its affected Codex provenance row.
  - The completed `PASS:` E6/F2 repair is historical evidence. The sole active
    PR #120 correction restores the intended `SOFT FAIL:` Markdown line break
    in `git-branch-naming` and `git-commit-convention`
    across their canonical, GitHub, and Codex surfaces, then refreshes the two
    derived records whose canonical hashes change. It does not reopen any
    earlier Commit A--D write set.
  - Retain the earlier 24-path full-repository result and the current 17-path
    non-skill inventory as historical expected-failure evidence. The feature
    worktree must retain zero diff for those 17 paths.
  - Run the consumer-like temporary workspace gate and require it to pass
    without hook rewrites.

- **Out of scope**:
  - Any independent Implementer write outside the exact Commit E and dependent Commit F paths
    named by the current correction contract, including planning artifacts,
    old correction artifacts, PR metadata, and the frozen hygiene-baseline
    implementation. Planner and Reviewer records remain separately owned.
  - Any semantic edit: skill names, paths, Markdown structure,
    cross-references, instructions, functionality, projection mechanisms, or
    release workflow.
- Fixing any of the 24 non-skill hygiene blockers, adding exclusions, CI,
  fixtures, README/VERSION changes, tags, releases, pushes, or PR creation.
  The two contract-specified commits are the sole exception.

## Locked Decisions

- `skills/` is the only canonical source. `.github/skills/` and
  `.codex/skills/` are compatibility/projection surfaces and never determine
  source truth.
- The root config uses `pre-commit/pre-commit-hooks` at `v4.6.0`, contains only
  `trailing-whitespace` and `end-of-file-fixer`, and has no `exclude`; it is a
  locked validation input. Its active correction adds only
  `--markdown-linebreak-ext=md` to `trailing-whitespace`.
- The active correction replaces only the intended `SOFT FAIL:` Markdown
  trailing-double-space break in each canonical `git-branch-naming` and
  `git-commit-convention` skill with literal `<br>`, and synchronizes exact
  canonical bytes to its two existing projections. It does not authorize any
  other Markdown or semantic rewrite.
- Commit C/D and the completed `PASS:` E6/F2 repair are historical facts. The
  next independent Implementer route is the final `SOFT FAIL:` E6 (the six
  named Markdown surfaces) followed by dependent F2 (the inventory and
  provenance records for the two changed canonical skills).
- The pre-existing GitHub-specific Python CLI path divergence in
  `.github/skills/plan-step-tracker/examples.md` is preserved. Full-file
  equality is not required; the affected line pairs must be byte-identical.
- The earlier PR-feedback correction and four-`<br>` follow-up artifacts are
  immutable historical truth, not current authority. The exclusive current
  Implementer and Reviewer handoff is
  `agent-skills-published-asset-hygiene-baseline.pr-feedback-final-reconciliation-plan.md`.
- The earlier 24-path and current 17-path all-files inventories are historical
  expected-failure evidence. Neither may be repaired, suppressed, retained, or
  re-run in the feature worktree.
- This is a non-stable-library topic: `README.md` and `VERSION` do not change;
  there is no release action.
- Correction severity is `medium`, routing state is `PLANNER_REPLAN`, and the
  parent plan remains the execution-facing current truth.

## Boundaries / Exclusions

- The Implementer may edit only the implementation paths in `Artifact Paths`,
  and only within the locked normalization rules. Any new canonical defect,
  missing projection, or semantic divergence other than the named exception
  stops work for Planner routing.
- The historical full-repository `pre-commit run --all-files` rewrote these
  24 non-skill files. They remain an isolated historical inventory only: none
  may remain in the final feature diff, and none may be hygiene-fixed by this
  topic:
  - `.github/guides/MAIN-AGENT-WORKFLOW.md`
  - `.github/guides/REFERENCE-INTAKE-PROCESS.md`
  - `.github/prompts/create-agent-plan.prompt.md`
  - `.gitignore`
  - `analysis/agent-skill-migration-sequencing/requirements.md`
  - `analysis/creator-reviewer-template-platform-path-alignment/technical-spec.md`
  - `analysis/phase-2-planning-spine-exceptions/requirements.md`
  - `analysis/phase-2-planning-spine-exceptions/technical-spec.md`
  - `analysis/plan-step-tracker/requirements.md`
  - `analysis/plan-step-tracker/technical-spec.md`
  - `analysis/platform-projection-adapter/technical-spec.md`
  - `analysis/python-descriptors-attribute-access/requirements.md`
  - `analysis/python-descriptors-attribute-access/technical-spec.md`
  - `analysis/python-implementation-workflow-sdd-tdd/technical-spec.md`
  - `analysis/python-retrofit-plan-review/requirements.md`
  - `analysis/python-tooling-skills/technical-spec.md`
  - `analysis/python-workflow-enhancement/requirements.md`
  - `analysis/spec-docs-mvp-generator/requirements.md`
  - `analysis/spec-docs-mvp-generator/technical-spec.md`
  - `docs/process/next-agent-follow-up.md`
  - `plan/agent-handoff-workflow.md`
  - `plan/python-docstrings/python-docstrings.plan.md`
  - `plan/python-retrofit-plan-review/python-retrofit-plan-review.plan.md`
  - `plan/reference-intake-workflow/reference-intake-workflow.plan.md`
- The first correction restored these eight paths, which were newly modified
  by the actual all-files run:
  `.gitignore`, `analysis/agent-skill-migration-sequencing/requirements.md`,
  `analysis/phase-2-planning-spine-exceptions/requirements.md`,
  `analysis/phase-2-planning-spine-exceptions/technical-spec.md`,
  `analysis/python-retrofit-plan-review/requirements.md`,
  `analysis/python-workflow-enhancement/requirements.md`,
  `docs/process/next-agent-follow-up.md`, and
  `plan/python-retrofit-plan-review/python-retrofit-plan-review.plan.md`.
  That completed historical action does not authorize any remaining
  non-skill change.
- The completed second correction authorized restore-only return to the `HEAD`
  pre-hook baseline for exactly these remaining 16 paths; it does not repair
  them:
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

## Status / Allowed Transitions

- **Current**: `needs-rework`; Ready PR #120 remains open after review
  identified a current-truth drift. Commits C and D are complete historical
  work. The active route is the final `SOFT FAIL:` E6, which restores two
  intended presentation breaks across six canonical/projection skill paths,
  followed by dependent F2, which refreshes the two derived records for the
  two canonical hash changes.
- **Execution model**: the frozen correction is complete, its second
  correction record is resolved, and Phase 4.5 parent current-truth
  reconciliation is independently approved. The completed publish route is
  `approved` -> `publish-in-progress` -> `pr-open` -> `needs-rework`.
  PR #120 remains open while the independent Implementer and Reviewer complete
  the bounded feedback route; this plan does not authorize merge or release
  action.
- **Allowed transitions**:
  - `planned` -> `creator-in-progress` (independent Implementer)
  - `creator-in-progress` (independent Implementer) -> `review-ready`
  - `review-ready` -> `reviewer-in-progress`
  - `reviewer-in-progress` -> `approved`
  - `reviewer-in-progress` -> `needs-rework`
  - `needs-rework` -> `creator-in-progress` (independent Implementer)
  - `approved` -> `creator-in-progress` (independent Implementer)
  - `approved` -> `publish-in-progress`
  - `publish-in-progress` -> `pr-open`
  - `publish-in-progress` -> `merged`
  - `pr-open` -> `needs-rework`
  - `pr-open` -> `merged`
  - `merged` -> terminal
- **Routing note**: the active bounded correction supersedes only the completed
  final-reconciliation execution authority. The final E6 contains the six
  `SOFT FAIL:` Markdown rendering-preservation writes; dependent F2 contains the
  deterministic canonical inventory rebuild and exactly the two eligible
  Codex-provenance row updates, each referencing Commit E. After independent
  review accepts both commits, return to `pr-open`; merge and release remain
  outside this route.

## Approved Verification Record — 2026-07-29

- `pre-commit validate-config` and `git diff --check` passed. The root
  configuration contains only the locked two hooks.
- `git diff -w --exit-code` is not a pass criterion for this topic: it returns
  nonzero for the permitted removal of terminal blank lines in the three
  `python-pre-commit` templates and
  `.github/skills/python-serialization-boundaries/REVIEW.md`. It is therefore
  not claimed to pass.
- To prove that the 46 tracked published-skill asset diffs are hygiene-only,
  compare each `HEAD` version and its worktree version after applying the same
  restricted normalizer to both: remove only horizontal spaces or tabs
  immediately before a line ending or EOF; remove only blank lines at EOF; and
  end the result with exactly one LF. The 46 normalized byte streams compare
  equal. This transformation does not alter inline text, non-terminal blank
  lines, Markdown structure, or any other semantic content.
- Canonical/projection checks passed, retaining the documented GitHub
  `plan-step-tracker` CLI-path divergence and GitHub-only serialization Date
  exception.
- The frozen 24-path non-skill inventory is absent from the final feature
  diff. The prior isolated full-repository inventory evidence remains
  consistent with that frozen list.
- A consumer-like temporary Git workspace passed all hooks with empty
  `git status --short` and a successful `git diff --exit-code`.

## Phase 4.5 Current-Truth Reconciliation — 2026-07-29

- The second-correction step's statement that
  `git diff -w --exit-code` passed is retained only as a historical evidence
  statement. A direct current-state rerun returns exit status `1` because the
  allowed changes remove terminal blank lines; it is superseded by this parent
  plan and is not a current acceptance claim.
- The only valid format-only proof for all 46 tracked published-skill assets
  is restricted-normalizer equality between `HEAD` and the worktree: remove
  only horizontal spaces or tabs immediately before a line ending or EOF,
  remove only blank lines at EOF, and end with exactly one LF. All 46
  normalized byte streams compare equal.
- That proof is supplemented, not replaced, by the existing dynamic evidence:
  `pre-commit validate-config`, `git diff --check`, the frozen isolated
  24-path all-files inventory, canonical/projection consistency checks, and
  the consumer-like temporary Git workspace gate. No other format-only proof
  is accepted for this topic.
- This reconciliation changes no implementation write set, 24-path
  out-of-scope inventory, two semantic exceptions, or root hook contract. The
  historical first/second correction artifacts and review log remain
  untouched.

## Phase 4.5 Plan-Reviewer Approval — 2026-07-29

- Independent Plan Reviewer returned an `approved` JSON result for the parent
  current-truth reconciliation.
- The approval confirms the parent plan is current truth for the
  `git diff -w --exit-code` result and the 46-asset restricted-normalizer
  proof, without expanding the write set, 24-path inventory, semantic
  exceptions, or hook contract.
- Route completed: `approved` -> `publish-in-progress`.
- Next gate: STOP POINT 1 human publish authorization. Until explicit approval
  is received, do not commit, push, create a PR, merge, or release.

## PR Feedback Correction — 2026-07-29

- STOP POINT 1 completed: the human authorized the bounded publish, the
  validated scope was committed and pushed, and Ready PR #120 was opened.
- PR #120 returned three distinct P2 comments:
  - P2-1: the canonical `skills/plan-step-tracker/examples.md` lost two
    Markdown hard-break markers from the consecutive `Output`, `Exit code`,
    and `Note` lines. The bounded implementation must synchronize the same
    `<br>` repair to its two existing projections.
  - P2-2: the planning artifacts had to record that human publish
    authorization, commit, push, and Ready PR creation had completed, and
    that the topic returned from `pr-open` to `needs-rework`. This
    Planner-owned correction is complete in the parent plan and topic step.
  - P2-3: current dynamic verification could not depend on machine-local
    absolute paths. This Planner-owned correction is complete in the parent
    plan through a `PATH`-resolvable `pre-commit` and writable
    `PRE_COMMIT_HOME` prerequisite.
- The original P2-1 repair completed: it restored the two hard-break markers
  in the `read_all` block of each projection. Its implementation and review
  route are historical; the human publish authorization, commit, push, and
  Ready PR creation remain completed historical facts.
- The original correction contract at
  `agent-skills-published-asset-hygiene-baseline.pr-feedback-correction-plan.md`
  and its step artifact are historical. The later follow-up contract controls
  the current Implementer and Reviewer handoffs; no other PR comment is
  implied by this route.

## Artifact Paths

| Artifact | Path | Owner | Role |
| --- | --- | --- | --- |
| Parent topic plan | `plan/agent-skills-published-asset-hygiene-baseline/agent-skills-published-asset-hygiene-baseline.plan.md` | Planning actor | Current execution contract |
| First correction plan | `plan/agent-skills-published-asset-hygiene-baseline/agent-skills-published-asset-hygiene-baseline.correction-plan.md` | Planning actor | Historical first `medium` correction contract; immutable historical truth |
| First correction step | `plan/agent-skills-published-asset-hygiene-baseline/agent-skills-published-asset-hygiene-baseline.correction-step.md` | Planning actor / Implementer | Historical first-correction progression evidence; immutable historical truth |
| Second correction plan | `plan/agent-skills-published-asset-hygiene-baseline/agent-skills-published-asset-hygiene-baseline.second-correction-plan.md` | Planning actor | Resolved second `medium` restore-only correction record |
| Second correction step | `plan/agent-skills-published-asset-hygiene-baseline/agent-skills-published-asset-hygiene-baseline.second-correction-step.md` | Planning actor / Implementer | Resolved second-correction progression and closure evidence |
| PR-feedback correction plan | `plan/agent-skills-published-asset-hygiene-baseline/agent-skills-published-asset-hygiene-baseline.pr-feedback-correction-plan.md` | Planning actor | Historical bounded PR #120 correction contract |
| PR-feedback correction step | `plan/agent-skills-published-asset-hygiene-baseline/agent-skills-published-asset-hygiene-baseline.pr-feedback-correction-step.md` | Planning actor / Implementer | Historical bounded implementation progression and validation evidence |
| PR-feedback follow-up correction plan | `plan/agent-skills-published-asset-hygiene-baseline/agent-skills-published-asset-hygiene-baseline.pr-feedback-follow-up-correction-plan.md` | Planning actor | Historical Commit A/B correction contract; superseded by final reconciliation |
| PR-feedback follow-up correction step | `plan/agent-skills-published-asset-hygiene-baseline/agent-skills-published-asset-hygiene-baseline.pr-feedback-follow-up-correction-step.md` | Planning actor | Historical Commit A/B progression and evidence handoff |
| PR-feedback final reconciliation plan | `plan/agent-skills-published-asset-hygiene-baseline/agent-skills-published-asset-hygiene-baseline.pr-feedback-final-reconciliation-plan.md` | Planning actor | Current bounded PR #120 correction contract |
| PR-feedback final reconciliation step | `plan/agent-skills-published-asset-hygiene-baseline/agent-skills-published-asset-hygiene-baseline.pr-feedback-final-reconciliation-step.md` | Planning actor / Implementer | Current bounded progression, verification, and reviewer handoff |
| Topic step | `plan/agent-skills-published-asset-hygiene-baseline/agent-skills-published-asset-hygiene-baseline.step.md` | Planning actor / Main Agent | Multi-role workflow progression truth |
| Review log | `plan/agent-skills-published-asset-hygiene-baseline/agent-skills-published-asset-hygiene-baseline.review-log.md` | Reviewer / Main Agent | Persisted reviewer verdicts and routing evidence |
| Root hook config | `.pre-commit-config.yaml` | Implementer | All-repository hygiene hook contract |
| Original published assets | `skills/git-branch-naming/SKILL.md`; `.github/skills/git-branch-naming/SKILL.md`; `.codex/skills/git-branch-naming/SKILL.md` | Implementer | Canonical asset and existing projections |
| Original published assets | `skills/git-commit-convention/SKILL.md`; `.github/skills/git-commit-convention/SKILL.md`; `.codex/skills/git-commit-convention/SKILL.md` | Implementer | Canonical asset and existing projections |
| Original published assets | `skills/plan-step-tracker/examples.md`; `.github/skills/plan-step-tracker/examples.md`; `.codex/skills/plan-step-tracker/examples.md` | Implementer | Canonical asset and existing projections |
| Original published assets | `skills/python-docstrings/SKILL.md`; `.github/skills/python-docstrings/SKILL.md`; `.codex/skills/python-docstrings/SKILL.md` | Implementer | Canonical asset and existing projections |
| Original published assets | `skills/python-docstrings/examples.md`; `.github/skills/python-docstrings/examples.md`; `.codex/skills/python-docstrings/examples.md` | Implementer | Canonical asset and existing projections |
| Original published assets | `skills/python-docstrings/references/dataclass-patterns.md`; `.github/skills/python-docstrings/references/dataclass-patterns.md`; `.codex/skills/python-docstrings/references/dataclass-patterns.md` | Implementer | Canonical asset and existing projections |
| Original published assets | `skills/python-docstrings/references/error-semantics.md`; `.github/skills/python-docstrings/references/error-semantics.md`; `.codex/skills/python-docstrings/references/error-semantics.md` | Implementer | Canonical asset and existing projections |
| Original published assets | `skills/python-docstrings/references/google-style-template.md`; `.github/skills/python-docstrings/references/google-style-template.md`; `.codex/skills/python-docstrings/references/google-style-template.md` | Implementer | Canonical asset and existing projections |
| Original published assets | `skills/python-docstrings/references/semantic-intent.md`; `.github/skills/python-docstrings/references/semantic-intent.md`; `.codex/skills/python-docstrings/references/semantic-intent.md` | Implementer | Canonical asset and existing projections |
| Original published assets | `skills/python-generators-iterators/examples.md`; `.github/skills/python-generators-iterators/examples.md`; `.codex/skills/python-generators-iterators/examples.md` | Implementer | Canonical asset and existing projections |
| Original published assets | `skills/python-plan-authoring/templates/spec-template.md`; `.github/skills/python-plan-authoring/templates/spec-template.md`; `.codex/skills/python-plan-authoring/templates/spec-template.md` | Implementer | Canonical asset and existing projections |
| Original published assets | `skills/python-pre-commit/references/version-pinning.md`; `.github/skills/python-pre-commit/references/version-pinning.md`; `.codex/skills/python-pre-commit/references/version-pinning.md` | Implementer | Canonical asset and existing projections |
| Original published assets | `skills/python-tdd-test-authoring/checklist.md`; `.github/skills/python-tdd-test-authoring/checklist.md`; `.codex/skills/python-tdd-test-authoring/checklist.md` | Implementer | Canonical asset and existing projections |
| Original published assets | `skills/python-tdd-test-authoring/references/behavior-change-classifier.md`; `.github/skills/python-tdd-test-authoring/references/behavior-change-classifier.md`; `.codex/skills/python-tdd-test-authoring/references/behavior-change-classifier.md` | Implementer | Canonical asset and existing projections |
| Correction published assets | `skills/python-pre-commit/templates/pre-commit-config.yaml`; `.github/skills/python-pre-commit/templates/pre-commit-config.yaml`; `.codex/skills/python-pre-commit/templates/pre-commit-config.yaml` | Implementer | Final-LF-only canonical asset and projections |
| Projection hygiene-only exception | `.github/skills/python-serialization-boundaries/REVIEW.md` | Implementer | Final-LF hygiene only; retain existing GitHub semantic divergence |
| Historical PR #120 feedback target | `skills/plan-step-tracker/examples.md`; `.github/skills/plan-step-tracker/examples.md`; `.codex/skills/plan-step-tracker/examples.md` | Implementer | Completed hard-break repair; retained only as historical evidence |
| Historical correction Commit A | `.pre-commit-config.yaml`; `skills/git-branch-naming/SKILL.md`; `.github/skills/git-branch-naming/SKILL.md`; `.codex/skills/git-branch-naming/SKILL.md`; `skills/git-commit-convention/SKILL.md`; `.github/skills/git-commit-convention/SKILL.md`; `.codex/skills/git-commit-convention/SKILL.md` | Implementer | Historical hook argument and `PASS:` soft-break correction |
| Historical correction Commit B | `artifacts/skills-inventory.jsonl`; `.codex/skills/provenance.md` | Implementer | Historical deterministic 57-record rebuild and eight provenance-row update referencing Commit A |
| Historical final-reconciliation Commit C | `skills/python-pre-commit/references/version-pinning.md`; `.github/skills/python-pre-commit/references/version-pinning.md`; `.codex/skills/python-pre-commit/references/version-pinning.md` | Implementer | Completed rendering-preservation repair: literal `<br>` at the source-of-truth break |
| Historical final-reconciliation Commit D | `artifacts/skills-inventory.jsonl`; `.codex/skills/provenance.md` | Implementer | Completed dependent deterministic rebuild: one `python-pre-commit` canonical hash and one corresponding Codex provenance row reference Commit C |
| Active correction Commit E | `skills/git-branch-naming/SKILL.md`; `.github/skills/git-branch-naming/SKILL.md`; `.codex/skills/git-branch-naming/SKILL.md`; `skills/git-commit-convention/SKILL.md`; `.github/skills/git-commit-convention/SKILL.md`; `.codex/skills/git-commit-convention/SKILL.md` | Independent Implementer | Replace only each intended `SOFT FAIL:` Markdown hard break with literal `<br>` and synchronize projections from canonical |
| Active correction Commit F | `artifacts/skills-inventory.jsonl`; `.codex/skills/provenance.md` | Independent Implementer | Dependent deterministic rebuild: update only `git-branch-naming` and `git-commit-convention` canonical hashes and their two Codex provenance rows to the final `SOFT FAIL:` Commit E |
| Second-correction restore-only paths | `.github/guides/MAIN-AGENT-WORKFLOW.md`; `.github/guides/REFERENCE-INTAKE-PROCESS.md`; `.github/prompts/create-agent-plan.prompt.md`; `analysis/creator-reviewer-template-platform-path-alignment/technical-spec.md`; `analysis/plan-step-tracker/requirements.md`; `analysis/plan-step-tracker/technical-spec.md`; `analysis/platform-projection-adapter/technical-spec.md`; `analysis/python-descriptors-attribute-access/requirements.md`; `analysis/python-descriptors-attribute-access/technical-spec.md`; `analysis/python-implementation-workflow-sdd-tdd/technical-spec.md`; `analysis/python-tooling-skills/technical-spec.md`; `analysis/spec-docs-mvp-generator/requirements.md`; `analysis/spec-docs-mvp-generator/technical-spec.md`; `plan/agent-handoff-workflow.md`; `plan/python-docstrings/python-docstrings.plan.md`; `plan/reference-intake-workflow/reference-intake-workflow.plan.md` | Implementer | Restore only to the `HEAD` pre-hook baseline; no hygiene repair |

If work needs a path not listed here, stop and return to Planner; it is not an
implicit extension of this mission.

## Implementation Steps

These are independent-Implementer-only implementation steps. Planning-current-truth updates,
review verdict recording, PR replies, and thread resolution are deliberately
outside this section and must not be inferred as Implementer authority.

1. The final Commit E changes only the six `git-branch-naming` and
   `git-commit-convention` canonical/projection paths listed in `Artifact
   Paths`. In each canonical source, replace only the intended `SOFT FAIL:`
   Markdown hard break with literal `<br>`, then copy those exact canonical
   bytes to the corresponding GitHub and Codex projections.
2. After Commit E is committed, Commit F changes only
   `artifacts/skills-inventory.jsonl` and `.codex/skills/provenance.md`.
   Rebuild the complete canonical inventory deterministically; update only the
   two canonical records and two eligible Codex provenance rows for
   `git-branch-naming` and `git-commit-convention`, with both rows citing
   the final Commit E.
3. Preserve every other byte. Do not modify planning artifacts, historical
   correction artifacts, review-log content, PR metadata, or any non-skill
   expected-failure inventory path.

## Validation / Acceptance Checks

- Current dynamic verification prerequisite: `pre-commit` must resolve on
  `PATH`, and `PRE_COMMIT_HOME` must name a writable cache directory. Do not
  encode a machine-specific interpreter or cache path in current acceptance
  criteria.
- `pre-commit validate-config` succeeds.
- Run `pre-commit` against exactly the six final Commit E `SKILL.md` paths and
  require it to pass without rewrite. Each intended `SOFT FAIL:` line ends in
  literal `<br>` in canonical and both projections. `git diff --check` also
  succeeds.
- Each scoped canonical skill is byte-identical to its `.github` and `.codex`
  projection. The root configuration remains the locked two-hook configuration
  with the sole `markdown-linebreak-ext=md` argument addition.
- The rebuilt inventory has 57 sorted unique canonical records and is
  byte-identical to a second builder run. Only `git-branch-naming` and
  `git-commit-convention` receive new canonical hashes. Exactly their two
  Codex provenance rows change and each cites the final Commit E; GitHub-only
  serialization remains absent from both generated change sets.
- Do not run `pre-commit run --all-files` in the feature worktree. The retained
  exact 17-path temporary-workspace inventory remains expected-failure evidence
  only; neither it nor the older 24-path inventory is an active write set.
- In a consumer-like temporary Git workspace, copy every published in-scope
  asset and `.pre-commit-config.yaml`, make a baseline commit, run
  `pre-commit run --all-files`, then require empty `git status --short` and a
  successful `git diff --exit-code`.
- The Reviewer must verify the completed `PASS:` E6/F2 boundary, final
  `SOFT FAIL:` E6/F2 exact write set, 57-record/two-row inventory and
  provenance invariants, retained temporary-workspace inventory boundary,
  consumer-like passing gate, and persisted review routing before the Main
  Agent resolves the remaining thread.

## Reviewer Handoff

```json
{"verdict":"approved|needs-rework","blocking_issues":[],"copilot_feedback_triage":{"ADDRESS":[],"DISCUSS":[],"SKIP":[]}}
```

## Post-merge / release actions

No repository release action is required. Any commit, push, PR, merge, or
post-merge action requires separate Main Agent routing and the applicable human
authorization gates.

## Open Questions / Unresolved Items

None. The 24-path all-files failure is an explicit out-of-scope blocker
inventory, not an unresolved requirement for this topic.

## Historical PR Correction — 2026-07-29

- The follow-up correction contract, Commit A/B boundaries, eight-row
  provenance result, and frozen 24-path full-repository inventory are
  historical evidence only. They grant no active implementation authority.
- The sole current authority is the final-reconciliation plan's independent
  Implementer final `SOFT FAIL:` E6/F2 route and retained 17-path temporary
  all-files inventory.

## Final PR Reconciliation — 2026-07-29

This section supersedes earlier text that names the follow-up correction as
active or treats the 24-path inventory as the current expected all-files
result. The parent plan remains current truth; all earlier correction artifacts
and the 24-path inventory remain retained historical truth.

- **Current status:** `needs-rework`; the sole active authority is
  `agent-skills-published-asset-hygiene-baseline.pr-feedback-final-reconciliation-plan.md`.
- **Completed historical repair:** Commit C changed only canonical
  `skills/python-pre-commit/references/version-pinning.md` and its existing
  `.github/skills/` and `.codex/skills/` projections; dependent Commit D then
  changed only `artifacts/skills-inventory.jsonl` and
  `.codex/skills/provenance.md` for the resulting `python-pre-commit` hash.
  Neither boundary is reopened.
- **Completed historical repair:** the preceding E6/F2 changed only the six
  canonical/projection `git-branch-naming/SKILL.md` and
  `git-commit-convention/SKILL.md` paths, replacing each intended `PASS:`
  Markdown hard break with `<br>`, then refreshed their two derived records.
  That repair is not reopened.
- **Active bounded repair:** final Commit E changes only the same six
  canonical/projection
  `git-branch-naming/SKILL.md` and `git-commit-convention/SKILL.md` paths,
  replacing each intended `SOFT FAIL:` Markdown hard break with `<br>`.
  Dependent Commit F then changes only `artifacts/skills-inventory.jsonl` and
  `.codex/skills/provenance.md`, updating the two affected canonical hashes and
  their two provenance rows to cite the final Commit E.
- **Final PR-base proof:** compare against merge-base
  `d177401ff56a221ce104555687655a8ea1a55fae` (`origin/dev` at planning time).
  The 46 changed published-skill assets are exactly 34 hygiene-only assets and
  12 explicit rendering-preservation exception assets: canonical, GitHub, and
  Codex copies of `git-branch-naming/SKILL.md`,
  `git-commit-convention/SKILL.md`, `plan-step-tracker/examples.md`, and
  `python-pre-commit/references/version-pinning.md`.
  The config, inventory, provenance, and explicitly listed planning artifacts
  are reviewed separately; no unclassified path may enter the PR diff.
- **Temporary all-files boundary:** the isolated 17-path expected-failure
  inventory remains evidence only and must not be re-run in the feature
  worktree. The consumer-like workspace remains a passing no-rewrite gate.
- **Routing:** after independent review accepts this bounded repair and final
  PR-base proof, return to `pr-open` for thread handling. Resolve only
  satisfied PR threads; leave a scoped reply on any still-actionable thread.
