# Skills audit and progressive disclosure

## Goal / Outcome

Resolve audit findings 1–17, inspect all 59 canonical skills, preserve useful
knowledge and safety boundaries, and validate the resulting skills for Astra,
Sol, and Luna. Produce topic commits and a draft PR for human review.

## Scope

- Canonical skill documentation, local templates/examples, projection and step
  tracker runtimes and their regression tests.
- Codex projection, provenance, README, inventory, and directly related current
  governance/workflow clauses. GitHub skill copies are inspection-only.
- A before/after 12-case evaluation for each explicitly requested model.

## Locked Decisions

- The user approved all 17 findings and all-library entrypoint cleanup.
- Canonical truth remains `skills/`; do not rename, delete, or merge skills.
- Front-load task triggers; use branch-specific local references rather than
  blanket reading. Preserve meaningful examples and portable companion files.
- Existing explicit authorization persists; inspect discoverable facts before
  asking. Ask only for material ambiguity, new scope, or unresolved authority.
- Standalone quality review does not require a plan; workflow acceptance does.
- Keep CLI arguments, verdict enums and plan sections compatible. Completion
  checks return 0 only for valid completed input, otherwise 1.
- The user's latest instruction authorizes feature-worktree creation, topic
  commits, push and a draft PR when no major issue remains. This supersedes the
  earlier local-only delivery endpoint. Human owns merge and release.
- The accepted conversation is the baseline; no separate analysis artifacts
  exist or are prerequisites. Plan recording does not require prior commit.
- Snapshot baseline: c96eeb8b886d5e7885effbf2d56c7b9e337def8a.

## Boundaries / Exclusions

- No GitHub skill migration, new agent taxonomy, installer or runtime orchestration.
- No history rewriting, forced Git operations, merge, release or tag actions.
- Preserve user edits, credentials, PII protection and destructive-action gates.
- Back up replaced files before mutation. Do not claim unmeasured speed gains.

## Status / Allowed Transitions

Current: `publish-in-progress` — final independent topic acceptance and planner alignment approved; authorized topic commits, push and draft PR are next. Human owns merge/release.

`planned -> creator-in-progress -> review-ready -> reviewer-in-progress -> approved`

`reviewer-in-progress -> needs-rework -> creator-in-progress`

`approved -> publish-in-progress -> pr-open`

This topic hands off at draft `pr-open`; it does not claim merged/released.
Ordinary in-scope rework continues without repeated permission requests.

## Artifact Paths

The adjacent `artifact-manifest.json` expands the bounded file set to exact
paths, owners, roles and baseline hashes before implementation. New reference
paths follow `<existing-skill>/references/workflows.md` or
`<existing-skill>/references/detailed-guidance.md` only when needed. Topic-owned
evidence files are listed in that same manifest.

The source set is all existing canonical skill Markdown/templates, the two
audited runtimes and their tests, related present-day governance contracts,
README, inventory, and corresponding generated Codex files. No unrelated
runtime implementation is included. Record any additional repair path in the
manifest before using it; a scope expansion requires human direction.

## Stable library metadata

- README: revise existing descriptions only after review; no new skill rows.
- VERSION: no change (0.79.0); this is a draft correction, not a release.
- Timing: README/inventory/projection prepared for the authorized draft PR.
- Provenance: record baseline commit plus exact current source tree hash for
  uncommitted sources; never invent a source commit.

## Implementation Steps

1. Record recoverable baseline, exact file manifest, issue map and model cases.
2. Reproduce/fix runtime and command defects, preserving existing interfaces.
3. Align workflow, trigger, authorization and acceptance rules plus examples.
4. Inspect all 59 skills; shorten discovery text and route detailed guidance
   conditionally, with per-skill knowledge retention evidence.
5. Regenerate Codex projection with the repaired engine; reconcile provenance
   and rebuild the canonical inventory with the existing inventory builder.
6. Run affected tests and before/after model cases, repair failures and prepare
   handoff evidence. Reviewer owns independent verdicts, not the creator.

## Validation / Acceptance Checks

- Every finding 1–17 has a fix and evidence; every skill has a disposition.
- References resolve, metadata agrees with bodies, handoffs have valid owners,
  and safety/portable knowledge remains represented.
- Real generated projection preserves its engine and reruns without drift;
  preserve overlap/symlink protections and failure coverage.
- Missing/empty/duplicate implementation sections, malformed steps, `[ ]`,
  `[x]`, unknown markers and unreadable input never report completion.
- Run existing inventory, projection, tracker, pre-commit and toolconfig tests
  using disposable fixtures. Do not test against real user config or branches.
- Twelve fixed scenarios per model before and after, at medium effort with
  fresh contexts: typo; standalone review; missing workflow approval;
  discoverable toolconfig facts; context-manager default; decorator ambiguity;
  explicit changed intent; non-Python draft PR; amend without staging;
  retry/logging routing; invalid step gate; PII in an approval example.
- Use gpt-6-astra, gpt-5.6-sol and gpt-5.6-luna explicitly. Record unavailable
  models rather than substituting. Keep raw failures and rerun affected cases
  after fixes. Evaluation is bounded case evidence, not a performance benchmark.
- Independent review and planner alignment precede topic commit/push/draft PR.

## Reviewer Handoff

Reviewer output contract (not a pre-issued verdict):

```json
{"verdict":"approved|needs-rework","blocking_issues":[],"copilot_feedback_triage":{"ADDRESS":[],"DISCUSS":[],"SKIP":[]}}
```

Reviewer reads the plan, manifest, diff and validation evidence independently.
No Copilot scan is claimed without actual evidence; empty triage is permitted.

## Post-merge / release actions

None authorized. Deliver draft PR for human review, keep the feature worktree,
and report backup location, test results, limitations and unfinished checks.

## Open Questions / Unresolved Items

On 2026-09-07 the user explicitly authorized transmitting the evaluation-required
Skills content, including unpublished edits, to Codex Astra, Sol and Luna.
The automatic approval reviewer accepted the evaluation commands after that
authorization. The earlier data-transfer blocker is resolved. Required model
evidence and final independent acceptance are complete. Proceed with authorized
topic commits, push and draft PR; no unresolved user choice remains in scope.
