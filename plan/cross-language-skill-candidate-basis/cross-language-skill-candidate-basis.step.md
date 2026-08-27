---
topic: cross-language-skill-candidate-basis
status: review-ready
created: 2026-08-27
---

# Cross-Language Skill Candidate Basis — Progression

## Workflow Stages

- [X] historical `pr-open` returned to `needs-rework` through current PR feedback
- [X] `needs-rework` -> `creator-in-progress`
- [X] `creator-in-progress` -> `review-ready` for the prospective five-artifact
  historical-remediation baseline
- [ ] `review-ready` -> `reviewer-in-progress`
- [ ] `reviewer-in-progress` -> `approved|needs-rework`
- [ ] `approved` -> `publish-in-progress`
- [ ] `publish-in-progress` -> `pr-open`
- [ ] `pr-open` -> `merged` (STOP POINT 2 applies after human merge handoff)

## Actionable Steps

### review-ready

- [X] Plan-Creator prepared only the five parent/correction planning artifacts
  listed in the correction progression.
- [ ] Main Agent directly validates the Phase 2 branch/worktree state and exact
  five-path diff, then creates and pushes the first additive baseline commit.

### reviewer-in-progress

- [ ] Main Agent routes the committed baseline to `reviewer-in-progress` and
  dispatches independent Plan-Reviewer review.
- [ ] Plan-Reviewer appends only its canonical JSON verdict to the existing
  review log. It reviews prospective governance of the fixed current tree and
  explicitly records that `python-code-review`'s historical remediation remains
  suspect.
- [ ] Main Agent creates and pushes the second commit containing only that
  review-log verdict; the five-path baseline commit remains its ancestor.

### approved / needs-rework

- [ ] An independent `approved` verdict permits the canonical
  `approved` -> `publish-in-progress` -> `pr-open` path.
- [ ] An independent `needs-rework` verdict returns the topic to
  `creator-in-progress`; no direct status jump is allowed.

### pr-open

- [ ] Main Agent triages current PR review comments, issue comments, and
  threads. Resolve only a thread supported by prospective correction evidence.

## Handoff / Gate Notes

- The fixed candidate set remains 11 candidates in four groups. Swift and
  TypeScript entries are future-validation requirements or blockers, not
  asserted target-project evidence.
- This is a non-stable documentation/planning topic: `README.md`, `VERSION`,
  `skills/**`, `.github/**`, and `.codex/**` are prohibited writes.
- The `python-code-review` change in `c285c3a` is preserved as historical
  remediation but lacks preceding repo-visible implementation authorization.
  It remains suspect and is not retrospectively certified or re-executed.
- Plan-Creator owns baseline authorship. Main Agent owns direct Phase 2
  verification, both commits, and both pushes. Plan-Reviewer acts only after
  the first commit and writes only its JSON verdict to the existing review log.
- Planner may close the correction only after future compliant routing is
  evidenced and the historical limitation remains explicitly recorded.
