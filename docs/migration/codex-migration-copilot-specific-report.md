# Codex Migration Copilot-Specific Report

## Candidate

- `.github/skills/copilot-instructions-init/`

## Final Verdict

- `reference-only`

## Moved / Not Moved

- `not moved`

## Why

- This skill is a Copilot-era instruction-generation surface focused on one
  target-project file: `.github/copilot-instructions.md`.
- Its contract depends on sensed facts, stale-fingerprint checks, overwrite
  decision gates, and target-project instruction management behavior rather than
  a portable Codex skill surface that this branch may approve for migration.
- The skill preserves bounded conceptual value, especially around safety gates
  for fact freshness and overwrite handling, but that value is not evidence that
  the skill itself should migrate from this branch.

## Confirmed-Blocker Context

- Repo-visible evidence in
  `docs/migration/migration-runway-checklist.md` classifies
  `.github/skills/copilot-instructions-init/` as:
  - surface type: `runtime/tooling surface`
  - current status: `inventory-complete`
  - dependency / blocker classification: `confirmed-blocker`
  - owner / next phase: `future runtime/tooling transition phase`
- Within this branch, `confirmed-blocker` is evidence context only.
- `confirmed-blocker` does not replace the final verdict vocabulary and is not a
  third verdict.

## Reusable Reference Notes

- Fact-first input priority is potentially reusable as reference material:
  `sensed facts -> installed skills -> plan contract -> human intent`.
- Stale-fact hard-stop discipline is potentially reusable as reference
  material, including the three-fingerprint gate:
  `Git HEAD`, `pyproject.toml` / `uv.lock`, and `.github/skills/` summary.
- Overwrite safety is potentially reusable as reference material:
  require an explicit choice between `full overwrite`, `keep current content`,
  and `manual merge by the human` when the existing instructions are materially
  different.
- Target-file-only boundary discipline is potentially reusable as reference
  material:
  the skill is constrained to generating or refreshing exactly one target file.
- These notes are conceptual reuse only and do not approve migration of the
  skill itself.

## Follow-up

- No migration action is approved from this branch for
  `.github/skills/copilot-instructions-init/`.
- If future work is needed, route it to a separate runtime/tooling transition
  topic.
- If later repo-visible evidence proves the skill is portable after all, stop
  and reclassify it into an appropriate migration branch before any migration
  work starts.

## Contract Compliance Note

- Candidate content was not modified.
- No runtime/tooling blocker repair was performed.
- No planner or reviewer work was repeated in this report.
- No third verdict was introduced.
- No repo-wide cutover semantics were changed.
- This report stays inside the approved contract for
  `feat/andrew/codex-migration-copilot-specific`.
