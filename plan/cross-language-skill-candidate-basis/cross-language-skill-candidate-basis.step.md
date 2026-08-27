---
topic: cross-language-skill-candidate-basis
status: needs-rework
created: 2026-08-27
---

# Cross-Language Skill Candidate Basis — Progression

## Workflow Stages

Historical entries are retained only as suspect evidence. They do not satisfy
the current recovery loop or authorize a direct status jump.

- [X] historical `pr-open` returned to `needs-rework` through current PR feedback
- [ ] `needs-rework` -> `creator-in-progress`
- [ ] `creator-in-progress` -> `review-ready`
- [ ] `review-ready` -> `reviewer-in-progress`
- [ ] `reviewer-in-progress` -> `approved`
- [ ] `approved` -> `publish-in-progress`
- [ ] `publish-in-progress` -> `pr-open`
- [ ] `pr-open` -> `merged` (STOP POINT 2 applies after human merge handoff)

## Actionable Steps

### needs-rework — override-owned recovery gate

- [X] Preserve the original five compatible PR fixes in the parent artifacts:
  synchronized PR state and summary, PR feedback loop, separated verdict
  ownership, and one publish action containing STOP POINT 1.
- [ ] Main Agent directly verifies and records that `c285c3a` is the published
  branch/HEAD baseline, then records the execution-worktree comparison: exactly
  five permitted recovery artifacts, no untracked file, no unrelated change.
  Dispatcher may route the result but cannot substitute for it.

### creator-in-progress

- [ ] After the direct Phase 2 verification, record the canonical
  `needs-rework` -> `creator-in-progress` transition. Plan-Creator's prepared
  work remains limited to the five permitted recovery artifacts.

### review-ready

- [ ] Record `creator-in-progress` -> `review-ready`; freeze the exact five-file
  edit set for Main Agent staging and the additive baseline commit.

### reviewer-in-progress

- [ ] Main Agent stages and commits exactly the five permitted artifacts with no
  other staged, unstaged, or untracked change, then records
  `review-ready` -> `reviewer-in-progress`.
- [ ] Independent Plan-Reviewer reviews that committed baseline and returns the
  canonical JSON verdict.

### approved

- [ ] Record `reviewer-in-progress` -> `approved` only for an independent
  Plan-Reviewer `approved` verdict; a `needs-rework` verdict restarts this
  canonical loop.

### publish-in-progress

- [ ] Main Agent records `approved` -> `publish-in-progress` and pushes the
  approved additive baseline without rewriting history.

### pr-open

- [ ] Record `publish-in-progress` -> `pr-open` only after PR observation.
  Then Main Agent triages current PR review comments, issue comments, and
  threads. Resolve only threads addressed by evidence. Do not merge, release,
  tag, or poll after a merge handoff.

### merged

- [ ] STOP POINT 2: only a new explicit human resume may initiate post-merge
  local sync and update of the existing topic close summary.

## Handoff / Gate Notes

- Optional analysis inputs are absent. This plan contains the required semantic
  warning; no actor may create, regenerate, or infer an analysis layer in this
  topic.
- Existing Phase 1 artifacts and the current repository positioning topic are
  read-only evidence. They are not part of this topic's write set.
- This is a non-stable documentation/planning topic: `README.md`, `VERSION`,
  `skills/**`, `.github/**`, and `.codex/**` are prohibited writes.
- Current truth is `needs-rework`; the latest published corrective baseline is
  `c285c3a11be3a26dfaa661f88e4ace4973829d1f`. Main Agent must distinguish the
  clean published baseline from the intentionally modified five-file recovery
  set. No PR thread is resolved. Earlier history and approvals are
  historical/suspect because no committed planned baseline preceded the
  original implementation sequence.
- Swift and TypeScript entries are future-validation requirements or blockers,
  never claims of verified target-project behavior.
- Pre-creator Phase 2 is a Status/Gate prerequisite, not Implementer work.
  Under the explicit human override, Main Agent directly verifies and confirms
  the published `c285c3a` branch/HEAD baseline and the exact five-file
  execution-worktree comparison (no untracked or unrelated change) in the
  correction step; then the full canonical loop proceeds through creator,
  review-ready, reviewer, approved, publish, and pr-open. Dispatcher may route
  the result only. Independent Plan-Reviewer approval is required before the
  topic can enter `publish-in-progress`.
- The correction step is the authoritative record of the direct observations.
  The old repair, re-review, and publication remain historical; they do not
  satisfy the override-owned gate or assert post-recovery thread resolution.
