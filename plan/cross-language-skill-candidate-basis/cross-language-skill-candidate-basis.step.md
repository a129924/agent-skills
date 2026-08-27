---
topic: cross-language-skill-candidate-basis
status: needs-rework
created: 2026-08-27
---

# Cross-Language Skill Candidate Basis — Progression

## Workflow Stages

- [X] planned (historical/suspect; not evidence of compliant ordering)
- [ ] creator-in-progress
- [ ] review-ready
- [ ] reviewer-in-progress
- [ ] approved
- [X] needs-rework
- [ ] publish-in-progress
- [X] pr-open (PR exists; recovery supersedes normal PR-loop advance)
- [ ] merged

## Actionable Steps

### needs-rework — recovery pending

- [X] Preserve the original five compatible PR fixes in the parent artifacts:
  synchronized PR state and summary, PR feedback loop, separated verdict
  ownership, and one publish action containing STOP POINT 1.
- [ ] Commit the recovery planning baseline containing the synchronized parent
  artifacts and both correction artifacts; do not amend, rebase, reset, or
  force-push historical commits.
- [ ] Independent Plan-Reviewer reviews the committed recovery baseline and
  returns the canonical JSON verdict.
- [ ] Dispatcher records the actual Phase 2 evidence in the correction step and
  confirms every pre-creator requirement before routing an Implementer.

### creator-in-progress

- [ ] Independent Implementer repairs only the frozen
  `python-implementation-review` portable-core wording in the candidate-basis
  document; do not change the 11-candidate scope or correction artifacts.

### review-ready

- [ ] Implementer hands the bounded repair to an independent Reviewer.

### reviewer-in-progress

- [ ] Reviewer returns the canonical JSON verdict. A `needs-rework` result
  remains in the normal loop; `approved` allows PR routing only after parent
  and correction acceptance checks pass.

### approved

- [ ] Reserved for the post-recovery independent Reviewer verdict.

### publish-in-progress

- [ ] Reserved for a separately authorized post-recovery repair publication.

### needs-rework

- [X] Recovery is pending; do not change the candidate set, create a language
  appendix, or alter history.

### pr-open

- [ ] After recovery and re-review, Main Agent may commit/push the reviewed
  repair and resolve only threads addressed by evidence. Do not merge, release,
  tag, or poll after a merge handoff.

### merged

- [ ] STOP POINT 2: only a new explicit human resume may initiate post-merge
  local sync and creation of the topic close summary.

## Handoff / Gate Notes

- Optional analysis inputs are absent. This plan contains the required semantic
  warning; no actor may create, regenerate, or infer an analysis layer in this
  topic.
- Existing Phase 1 artifacts and the current repository positioning topic are
  read-only evidence. They are not part of this topic's write set.
- This is a non-stable documentation/planning topic: `README.md`, `VERSION`,
  `skills/**`, `.github/**`, and `.codex/**` are prohibited writes.
- Current truth is `needs-rework`; the PR is open, but its earlier history and
  approvals are historical/suspect because no committed planned baseline
  preceded the original implementation sequence.
- Swift and TypeScript entries are future-validation requirements or blockers,
  never claims of verified target-project behavior.
- Pre-creator Phase 2 is a Status/Gate prerequisite, not Implementer work:
  recovery baseline commit -> independent Plan-Reviewer `approved` ->
  Dispatcher-recorded branch/HEAD/worktree/clean-state/untracked disposition/
  baseline-SHA evidence -> `needs-rework` -> `creator-in-progress`.
- The correction step starts entirely pending. Do not insert a claimed clean
  status, SHA, or completed gate before Dispatcher directly observes it.
