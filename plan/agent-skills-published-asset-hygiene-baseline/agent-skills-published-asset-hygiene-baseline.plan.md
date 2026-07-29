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
  - The sole active correction is the current PR #120 contract: Commit A
    preserves two Markdown `PASS:` soft breaks and configures the existing hook
    to recognize them; Commit B rebuilds canonical inventory and revalidates
    existing Codex projection provenance.
  - Retain the earlier 24-path full-repository result as historical evidence.
    The final reconciliation instead reproduces its exact current 17-path
    non-skill inventory in a disposable workspace and requires zero
    feature-worktree diff for those 17 paths.
  - Run the consumer-like temporary workspace gate and require it to pass
    without hook rewrites.

- **Out of scope**:
  - Any write outside the exact Commit A and Commit B paths named by the
    current correction contract, including planning artifacts, old correction
    artifacts, PR metadata, and the frozen hygiene-baseline implementation.
    The only exception is the sequenced post-Commit-B Planner correction-step
    write followed by the independent Reviewer review-log append.
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
- The active correction restores the one intended `PASS:` Markdown soft break
  in each canonical `git-branch-naming` and `git-commit-convention` skill and
  its two existing projections. It does not authorize other Markdown or
  semantic rewrites.
- The pre-existing GitHub-specific Python CLI path divergence in
  `.github/skills/plan-step-tracker/examples.md` is preserved. Full-file
  equality is not required; the affected line pairs must be byte-identical.
- The earlier PR-feedback correction and four-`<br>` follow-up artifacts are
  immutable historical truth, not current authority. The active Implementer
  and Reviewer handoff is exclusively
  `agent-skills-published-asset-hygiene-baseline.pr-feedback-follow-up-correction-plan.md`.
- The earlier 24-path all-files inventory is historical evidence. The final
  17-path all-files inventory is the current temporary-workspace expected
  failure; neither inventory may be repaired, suppressed, or retained in the
  feature worktree.
- This is a non-stable-library topic: `README.md` and `VERSION` do not change;
  there is no release action.
- Correction severity is `medium`, routing state is `PLANNER_REPLAN`, and the
  parent plan remains the execution-facing current truth.

## Boundaries / Exclusions

- The Implementer may edit only the implementation paths in `Artifact Paths`,
  and only within the locked normalization rules. Any new canonical defect,
  missing projection, or semantic divergence other than the named exception
  stops work for Planner routing.
- The full repository `pre-commit run --all-files` is expected to rewrite these
  24 non-skill files. They are an isolated inventory only: none may remain in
  the final feature diff, and none may be hygiene-fixed by this topic:
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

- **Current**: `needs-rework`; human publish authorization was received, the
  bounded changes were committed and pushed, and Ready PR #120 remains open.
  All earlier hard-break repairs are historical. The active route preserves two
  `PASS:` soft breaks across canonical and projection surfaces, locks the
  hook's Markdown-linebreak behavior, then performs deterministic inventory
  regeneration and Codex-provenance revalidation in two ordered commits.
- **Execution model**: the frozen correction is complete, its second
  correction record is resolved, and Phase 4.5 parent current-truth
  reconciliation is independently approved. The completed publish route is
  `approved` -> `publish-in-progress` -> `pr-open` -> `needs-rework`.
  PR #120 remains open while the independent Implementer and Reviewer complete
  the bounded feedback route; this plan does not authorize merge or release
  action.
- **Allowed transitions**:
  - `planned` -> `creator-in-progress`
  - `creator-in-progress` -> `review-ready`
  - `review-ready` -> `reviewer-in-progress`
  - `reviewer-in-progress` -> `approved`
  - `reviewer-in-progress` -> `needs-rework`
  - `needs-rework` -> `creator-in-progress`
  - `approved` -> `creator-in-progress`
  - `approved` -> `publish-in-progress`
  - `publish-in-progress` -> `pr-open`
  - `publish-in-progress` -> `merged`
  - `pr-open` -> `needs-rework`
  - `pr-open` -> `merged`
  - `merged` -> terminal
- **Routing note**: the active bounded correction supersedes only the current
  follow-up execution authority. Commit A contains the hook and soft-break
  changes; Commit B contains the complete canonical inventory rebuild and the
  eight affected Codex-provenance rows, each pointing to Commit A. A requested
  ninth provenance row is a human governance check, not an inferred change.
  After independent review accepts both commits, return to `pr-open`; merge and
  release remain outside this route.

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
| Current correction Commit A | `.pre-commit-config.yaml`; `skills/git-branch-naming/SKILL.md`; `.github/skills/git-branch-naming/SKILL.md`; `.codex/skills/git-branch-naming/SKILL.md`; `skills/git-commit-convention/SKILL.md`; `.github/skills/git-commit-convention/SKILL.md`; `.codex/skills/git-commit-convention/SKILL.md` | Implementer | Add only `--markdown-linebreak-ext=md` and restore the one intended `PASS:` soft break per skill/surface |
| Current correction Commit B | `artifacts/skills-inventory.jsonl`; `.codex/skills/provenance.md` | Implementer | Deterministic 57-record canonical rebuild and exactly eight provenance-row updates referencing Commit A |
| Second-correction restore-only paths | `.github/guides/MAIN-AGENT-WORKFLOW.md`; `.github/guides/REFERENCE-INTAKE-PROCESS.md`; `.github/prompts/create-agent-plan.prompt.md`; `analysis/creator-reviewer-template-platform-path-alignment/technical-spec.md`; `analysis/plan-step-tracker/requirements.md`; `analysis/plan-step-tracker/technical-spec.md`; `analysis/platform-projection-adapter/technical-spec.md`; `analysis/python-descriptors-attribute-access/requirements.md`; `analysis/python-descriptors-attribute-access/technical-spec.md`; `analysis/python-implementation-workflow-sdd-tdd/technical-spec.md`; `analysis/python-tooling-skills/technical-spec.md`; `analysis/spec-docs-mvp-generator/requirements.md`; `analysis/spec-docs-mvp-generator/technical-spec.md`; `plan/agent-handoff-workflow.md`; `plan/python-docstrings/python-docstrings.plan.md`; `plan/reference-intake-workflow/reference-intake-workflow.plan.md` | Implementer | Restore only to the `HEAD` pre-hook baseline; no hygiene repair |

If work needs a path not listed here, stop and return to Planner; it is not an
implicit extension of this mission.

## Implementation Steps

The earlier hygiene baseline and PR-feedback correction are historical evidence
only. The current Implementer handoff is governed exclusively by
`agent-skills-published-asset-hygiene-baseline.pr-feedback-follow-up-correction-plan.md`.

1. Commit A changes only `.pre-commit-config.yaml` and the six canonical /
   projection `SKILL.md` paths for `git-branch-naming` and
   `git-commit-convention`, exactly as frozen by the current correction plan.
2. Commit B follows Commit A and changes only
   `artifacts/skills-inventory.jsonl` and `.codex/skills/provenance.md`.
   Rebuild the complete 57-record canonical inventory, update exactly eight
   eligible provenance rows to Commit A, and do not create a ninth row.
3. Preserve every other byte, including completed historical hard-break
   repairs and all locked projection exceptions. Do not edit planning
   artifacts, older correction artifacts, or PR metadata.
4. The Implementer returns factual validation evidence only; it does not write
   planning artifacts. The named Planner updates the correction step
   after implementation, and the independent Reviewer updates the review log
   after review. These are the only non-A/B writes: the Planner write is allowed
   only after Commit B and the Reviewer append only after that record is
   complete. Do not widen either implementation write set to remedy the
   expected temporary all-files failure.

## Validation / Acceptance Checks

- Current dynamic verification prerequisite: `pre-commit` must resolve on
  `PATH`, and `PRE_COMMIT_HOME` must name a writable cache directory. Do not
  encode a machine-specific interpreter or cache path in current acceptance
  criteria.
- `pre-commit validate-config` succeeds.
- Run `pre-commit` against exactly the six scoped `SKILL.md` paths and require
  it to pass without rewrite. The two `PASS:` lines retain exactly two trailing
  spaces before LF in canonical and both projections. `git diff --check` also
  succeeds.
- Each scoped canonical skill is byte-identical to its `.github` and `.codex`
  projection. The root configuration remains the locked two-hook configuration
  with the sole `markdown-linebreak-ext=md` argument addition.
- The rebuilt inventory has 57 sorted unique canonical records and is
  byte-identical to a second builder run. Only the eight named canonical
  records receive new hashes. Exactly the corresponding eight Codex provenance
  rows change and each cites Commit A; GitHub-only serialization remains absent
  from both generated change sets.
- In an isolated full-repository Git workspace with a baseline commit,
  `pre-commit run --all-files` is expected to fail and rewrite exactly the 24
  frozen non-skill inventory paths, with no published-skill rewrite. Discard
  that workspace after recording the result; do not retain its changes.
- Before review, `git diff --name-only` restricted to the complete 24-path
  blocker inventory must produce no output in the feature worktree.
- In a consumer-like temporary Git workspace, copy every published in-scope
  asset and `.pre-commit-config.yaml`, make a baseline commit, run
  `pre-commit run --all-files`, then require empty `git status --short` and a
  successful `git diff --exit-code`.
- The Reviewer must verify both commit boundaries, each exact write set, the
  57/8 inventory and provenance invariants, temporary-workspace 24-path
  boundary, consumer-like passing gate, and persisted review routing.

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

## Current PR Correction — 2026-07-29

- **Current status:** `needs-rework`; current active step is
  `pr-feedback-current-correction-implementation`.
- The single active contract is
  `agent-skills-published-asset-hygiene-baseline.pr-feedback-follow-up-correction-plan.md`.
  It supersedes only the uncommitted follow-up execution route; all earlier
  PR-feedback artifacts remain immutable historical truth.
- Commit A is the seven-path hook / soft-break correction. Commit B is the
  two-path generated artifact update and must cite Commit A's actual SHA.
- `artifacts/skills-inventory.jsonl` remains the full 57-record canonical
  inventory: exactly eight eligible records may change. `.codex/skills/provenance.md`
  updates exactly the corresponding eight rows. A ninth row, including the
  GitHub-only serialization projection, requires human governance direction.
- The frozen 24-path full-repository hook result remains out of scope. Capture
  it only in a discarded temporary Git workspace; the consumer-like workspace
  is the passing dynamic gate.

## Final PR Reconciliation — 2026-07-29

This section supersedes earlier text that names the follow-up correction as
active or treats the 24-path inventory as the current expected all-files
result. The parent plan remains current truth; all earlier correction artifacts
and the 24-path inventory remain retained historical truth.

- **Current status:** `needs-rework`; the sole active authority is
  `agent-skills-published-asset-hygiene-baseline.pr-feedback-final-reconciliation-plan.md`.
- **Bounded repair:** only canonical
  `skills/python-pre-commit/references/version-pinning.md` and its existing
  `.github/skills/` and `.codex/skills/` projections may change. Replace the
  intended Markdown trailing-double-space source-of-truth break with `<br>` in
  all three byte-identical copies. No other implementation path is authorized.
- **Final PR-base proof:** compare against merge-base
  `d177401ff56a221ce104555687655a8ea1a55fae` (`origin/dev` at planning time).
  The 46 changed published-skill assets are exactly 40 hygiene-only assets and
  six explicit rendering-preservation exception assets: three
  `plan-step-tracker/examples.md` copies and three `version-pinning.md` copies.
  The config, inventory, provenance, and explicitly listed planning artifacts
  are reviewed separately; no unclassified path may enter the PR diff.
- **Temporary all-files boundary:** an isolated baseline workspace reproduces
  exactly 17 non-skill rewrites. That expected failure is evidence only, must
  be discarded, and must have zero feature-worktree diff. The consumer-like
  workspace remains a passing no-rewrite gate.
- **Routing:** after independent review accepts this bounded repair and final
  PR-base proof, return to `pr-open` for thread handling. Resolve only
  satisfied PR threads; leave a scoped reply on any still-actionable thread.
