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
  - The 42 previously identified published-skill asset paths, the root
    `.pre-commit-config.yaml`, and the four published-skill correction targets
    declared in `Artifact Paths`.
  - Only trailing-whitespace removal and final-LF normalization.
  - The bounded PR #120 correction declared below: in each of the three
    `plan-step-tracker/examples.md` copies, replace the two hard-break
    trailing-double-space markers in the `Output` / `Exit code` / `Note`
    three-line block with `<br>`.
  - Recording the all-files result as a 24-path non-skill blocker inventory;
    this is evidence only, not authorization to fix those files. The final
    feature diff must contain none of those 24 paths.

- **Out of scope**:
  - Any semantic edit: skill names, paths, Markdown structure,
    cross-references, instructions, functionality, projection mechanisms, or
    release workflow.
  - Fixing any of the 24 non-skill hygiene blockers, adding exclusions, CI,
    fixtures, README/VERSION changes, tags, releases, commits, pushes, or PRs.
  - Replacing the GitHub-only semantic divergence in
    `.github/skills/python-serialization-boundaries/REVIEW.md` with a
    canonical or Codex copy.

## Locked Decisions

- `skills/` is the only canonical source. `.github/skills/` and
  `.codex/skills/` are compatibility/projection surfaces and never determine
  source truth.
- The root config uses `pre-commit/pre-commit-hooks` at `v4.6.0`, contains only
  `trailing-whitespace` and `end-of-file-fixer`, and has no `exclude`.
- The PR #120 correction is a rendering-preservation exception to the original
  hygiene-only write rule: it replaces exactly two Markdown hard-break markers
  with `<br>` in each listed `plan-step-tracker` example. It preserves the
  affected three rendered lines and does not authorize a broader Markdown or
  semantic rewrite.
- The original 42 asset paths plus root config remain in scope. The correction
  adds final-LF-only normalization for the three published
  `python-pre-commit` template paths, and hygiene-only normalization for the
  GitHub-only `python-serialization-boundaries` review file.
- `.github/skills/python-serialization-boundaries/REVIEW.md` has a pre-existing
  GitHub-specific Date semantic divergence. It is a projection-hygiene-only
  exception: normalize whitespace/EOF only; do not require byte equality and
  do not modify a canonical or `.codex` counterpart.
- This is a non-stable-library topic: `README.md` and `VERSION` do not change;
  there is no release action.
- Correction severity is `medium`, routing state is `PLANNER_REPLAN`, and the
  correction artifacts are historical truth. This parent plan remains the
  execution-facing current truth.

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
  Of its three P2 comments, only the canonical Markdown rendering defect (P2-1)
  remains for independent implementation and review. The workflow-state
  correction (P2-2) and portable verification prerequisite (P2-3) are
  Planner-owned and resolved in the parent plan and topic step.
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
- **Routing note**: PR #120 returned three distinct P2 comments. P2-1 is the
  canonical Markdown rendering defect and is accepted for the bounded
  three-projection `<br>` repair below. P2-2 required the published human
  authorization / `needs-rework` state to be made current; the parent plan and
  topic step now do so. P2-3 required portable `pre-commit` / writable-cache
  criteria; the parent plan now defines them. The prior Copilot quota
  limitation remains an external-review limitation. After independent review
  accepts the P2-1 implementation, return to `pr-open`; merge and release
  remain outside this route.

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
- Current phase is `needs-rework`; active step is
  `pr-feedback-correction-implementation`. The human publish authorization,
  commit, push, and Ready PR creation remain completed historical facts.
- The only active repair is P2-1: replace the two removed hard-break markers
  with `<br>` in the affected three-line block of each example, so the three
  rendered lines remain distinct. It does not alter the pre-existing
  GitHub-specific CLI path.
- The exact correction contract is
  `agent-skills-published-asset-hygiene-baseline.pr-feedback-correction-plan.md`.
  Its step artifact and the review log control the Implementer and Reviewer
  handoffs; no other PR comment is implied by this route.

## Artifact Paths

| Artifact | Path | Owner | Role |
| --- | --- | --- | --- |
| Parent topic plan | `plan/agent-skills-published-asset-hygiene-baseline/agent-skills-published-asset-hygiene-baseline.plan.md` | Planning actor | Current execution contract |
| First correction plan | `plan/agent-skills-published-asset-hygiene-baseline/agent-skills-published-asset-hygiene-baseline.correction-plan.md` | Planning actor | Historical first `medium` correction contract; immutable historical truth |
| First correction step | `plan/agent-skills-published-asset-hygiene-baseline/agent-skills-published-asset-hygiene-baseline.correction-step.md` | Planning actor / Implementer | Historical first-correction progression evidence; immutable historical truth |
| Second correction plan | `plan/agent-skills-published-asset-hygiene-baseline/agent-skills-published-asset-hygiene-baseline.second-correction-plan.md` | Planning actor | Resolved second `medium` restore-only correction record |
| Second correction step | `plan/agent-skills-published-asset-hygiene-baseline/agent-skills-published-asset-hygiene-baseline.second-correction-step.md` | Planning actor / Implementer | Resolved second-correction progression and closure evidence |
| PR-feedback correction plan | `plan/agent-skills-published-asset-hygiene-baseline/agent-skills-published-asset-hygiene-baseline.pr-feedback-correction-plan.md` | Planning actor | Current bounded PR #120 correction contract; historical after independent review closes it |
| PR-feedback correction step | `plan/agent-skills-published-asset-hygiene-baseline/agent-skills-published-asset-hygiene-baseline.pr-feedback-correction-step.md` | Planning actor / Implementer | Current bounded implementation progression and validation evidence |
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
| PR #120 feedback target | `skills/plan-step-tracker/examples.md`; `.github/skills/plan-step-tracker/examples.md`; `.codex/skills/plan-step-tracker/examples.md` | Implementer | Replace only the two hard-break markers in the affected consecutive three-line block with `<br>`; preserve rendered lines and affected-block byte equality |
| Second-correction restore-only paths | `.github/guides/MAIN-AGENT-WORKFLOW.md`; `.github/guides/REFERENCE-INTAKE-PROCESS.md`; `.github/prompts/create-agent-plan.prompt.md`; `analysis/creator-reviewer-template-platform-path-alignment/technical-spec.md`; `analysis/plan-step-tracker/requirements.md`; `analysis/plan-step-tracker/technical-spec.md`; `analysis/platform-projection-adapter/technical-spec.md`; `analysis/python-descriptors-attribute-access/requirements.md`; `analysis/python-descriptors-attribute-access/technical-spec.md`; `analysis/python-implementation-workflow-sdd-tdd/technical-spec.md`; `analysis/python-tooling-skills/technical-spec.md`; `analysis/spec-docs-mvp-generator/requirements.md`; `analysis/spec-docs-mvp-generator/technical-spec.md`; `plan/agent-handoff-workflow.md`; `plan/python-docstrings/python-docstrings.plan.md`; `plan/reference-intake-workflow/reference-intake-workflow.plan.md` | Implementer | Restore only to the `HEAD` pre-hook baseline; no hygiene repair |

If work needs a path not listed here, stop and return to Planner; it is not an
implicit extension of this mission.

## Implementation Steps

The following numbered steps are retained as completed historical evidence for
the resolved second correction. They grant no current implementation authority.
The active PR #120 write set, validation, and Implementer handoff are governed
exclusively by
`agent-skills-published-asset-hygiene-baseline.pr-feedback-correction-plan.md`.

1. Preserve the root hook config and all approved published-asset
   normalizations; do not re-run a broad formatter as a substitute for bounded
   repair.
2. Preserve the three `python-pre-commit` template final-LF changes and the
   hygiene-only final-LF change in the GitHub-only serialization review file;
   do not alter their bytes otherwise.
3. Restore only the 16 paths named for the active second correction to their
   `HEAD` pre-hook baseline. Do not hygiene-fix any non-skill path and do not
   touch the eight paths already restored by the first correction.
4. Update only the second correction step with factual
   completion/validation evidence. Do not edit the parent plan, either
   correction plan, topic step, or review log during implementation.

## Validation / Acceptance Checks

- Current dynamic verification prerequisite: `pre-commit` must resolve on
  `PATH`, and `PRE_COMMIT_HOME` must name a writable cache directory. Do not
  encode a machine-specific interpreter or cache path in current acceptance
  criteria. Historical correction-step command evidence remains unchanged.
- `pre-commit validate-config` succeeds.
- `git diff --check` reports no whitespace errors in the allowed diff.
- Compare every canonical target with its `.github` and `.codex` projection
  byte-for-byte, except that:
  - `.github/skills/plan-step-tracker/examples.md` may retain its existing
    platform-specific CLI-path semantic difference; all three copies still
    pass hygiene; and
  - `.github/skills/python-serialization-boundaries/REVIEW.md` is hygiene-only
    and receives no equality comparison.
- In an isolated full-repository Git workspace with a baseline commit,
  `pre-commit run --all-files` must produce exactly the 24 non-skill blocker
  inventory paths and no published-skill path. Restore that workspace after
  inventory capture; do not retain those non-skill modifications in the topic
  worktree.
- Before review, `git diff --name-only` restricted to the complete 24-path
  blocker inventory must produce no output in the feature worktree, while the
  approved published-skill assets and root config remain in the diff.
- In a consumer-like temporary Git workspace, copy every published in-scope
  asset and `.pre-commit-config.yaml`, make a baseline commit, run
  `pre-commit run --all-files`, then require empty `git status --short` and a
  successful `git diff --exit-code`.
- For the current PR #120 correction, run `pre-commit` against exactly the
  three listed examples and require no file rewrite. Verify that each affected
  `Output` / `Exit code` / `Note` block contains `<br>` after its first two
  lines and renders as three lines. The three affected blocks must be
  byte-identical; full-file equality remains subject to the locked
  GitHub-specific CLI-path divergence.
- The reviewer must verify the correction's parent-sync condition, the exact
  write set, the retained semantic exceptions, and that reviewer routing is
  persisted in the review log.

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
