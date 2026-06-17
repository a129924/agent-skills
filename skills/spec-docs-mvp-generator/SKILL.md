---
name: spec-docs-mvp-generator
description: Generate or backfill the minimum v1 spec document set for one explicit `spec-name` using only the local templates, while preserving existing authored content and refusing out-of-scope outputs.
complexity: medium
use_when:
  - the caller needs the v1 starter docs for one explicit `spec-name`
  - an existing single-spec doc or shared data ownership map is missing required fixed sections or the required ownership-table header
do_not_use_when:
  - the request asks for multi-spec generation or any artifact outside the two-file v1 contract
  - the request requires projection updates, runtime orchestration, external dependencies, or destructive whole-file rewrite
inputs:
  - required: one explicit `spec-name`
  - optional: summary of the problem or opportunity
  - optional: initial goals and non-goals
  - optional: known actors
  - optional: known requirements or constraints
  - optional: known data ownership facts
  - optional: open questions that should remain visible in the starter docs
outputs:
  - docs/01-specs/<spec-name>.md
  - docs/02-spec-relations/data-ownership-map.md
---

# Purpose
Create or backfill the minimum v1 spec document set for exactly one explicit
`spec-name` using this skill package's local references and templates only.

This skill is bounded to exactly two downstream repo-visible outputs:

- `docs/01-specs/<spec-name>.md`
- `docs/02-spec-relations/data-ownership-map.md`

# Trigger / When to use
Use this skill when:

- the caller needs a stable starting point for one spec and its shared data
  ownership map
- an existing `docs/01-specs/<spec-name>.md` is missing one or more required
  fixed sections
- an existing `docs/02-spec-relations/data-ownership-map.md` is missing one or
  more required fixed sections or the fixed ownership-table header

Do not use this skill when:

- the request asks for multi-spec generation or any output outside the exact
  two-file v1 contract
- the request asks for `docs/00-overview/architecture-principles.md`,
  interfaces, flows, state machines, ADRs, implementation notes, or any
  near-equivalent substitute section
- the request tries to reopen projection, path migration, workflow binding, or
  runtime orchestration scope

# Inputs
Required input:

- `spec-name`
  The value must be a filename-safe slug for one spec file, not a path. Block
  before any write if it contains `/`, `\`, `..`, a leading `.`, an absolute
  path marker, or any other path-like segment. Only continue after resolving
  the candidate output path and confirming its normalized location remains
  inside `docs/01-specs/`.

Optional input:

- summary of the problem or opportunity
- initial goals and non-goals
- known actors
- known requirements or constraints
- known data ownership facts
- open questions that should remain visible in the starter docs

If optional context is sparse, still create a non-empty starter document by
using this skill package's local template prompts instead of leaving blank
sections.

# Process
1. Validate that one explicit `spec-name` is present before any write.
2. Validate that `spec-name` is a filename-safe slug, not a path-like value.
   Reject traversal, absolute-path, separator-containing, or dot-segment
   inputs before any write.
3. Resolve the candidate spec output path from `spec-name`, normalize it, and
   confirm the resolved path stays contained within `docs/01-specs/` before
   writing.
4. Use `templates/spec-template.md` and
   `templates/data-ownership-map-template.md` as the canonical starter
   skeletons.
5. Target only these two files:
   - `docs/01-specs/<spec-name>.md`
   - `docs/02-spec-relations/data-ownership-map.md`
6. When `docs/01-specs/<spec-name>.md` does not exist, create it from the spec
   template with the fixed section order:
   - `Summary`
   - `Problem`
   - `Goals`
   - `Non-goals`
   - `Actors`
   - `Requirements`
   - `Data Ownership Notes`
   - `Acceptance Signals`
   - `Open Questions`
7. When `docs/02-spec-relations/data-ownership-map.md` does not exist, create
   it from the ownership-map template with the fixed section order:
   - `Purpose`
   - `Ownership Table`
   - `Shared or Derived Data`
   - `Boundary Notes`
   - `Open Questions`
8. If a target file already exists, preserve existing authored content and
   backfill only missing fixed sections or the missing ownership-table header.
9. Keep reruns idempotent by avoiding duplicate same-name fixed sections and by
   never clearing or rewriting the whole file just to normalize layout.
10. Refuse or reroute any request that would widen the write set, add excluded
   artifact families, or require destructive rewrite.
11. Stay local-only. Do not depend on network access, external services,
   runtime orchestration, or projection sync.

# Platform Path Policy
- Authoring, templates, and adapter examples may use the placeholder
  `.<platform>/skills/<skill-name>/` when describing projection layouts.
- That placeholder is documentation-only and is not a runtime discovery path.
- Any adapter or installer must resolve the placeholder to a concrete platform
  path before execution begins.
- For Codex projection mapping, `.<platform>/skills/<skill-name>/` resolves to
  `.codex/skills/<skill-name>/`.
- Do not treat `skills/`, `.agents/skills/`, `.github/skills/`, or
  `.claude/skills/` as fixed runtime paths in skill instructions unless the
  instruction is explicitly describing a mapping rule.

# Examples
Positive example:

- Input: `spec-name: customer-profile-sync` with sparse background context.
  Outcome: create or backfill only
  `docs/01-specs/customer-profile-sync.md` and
  `docs/02-spec-relations/data-ownership-map.md`, using non-empty starter
  content and preserving authored text already present.

Negative example:

- Input: `spec-name: customer-profile-sync`, plus a request to also generate
  architecture principles, interfaces, and an ADR. Outcome: refuse or reroute
  the extra request and keep the v1 scope limited to the two allowed files.

# Outputs
This skill may create or update only:

- `docs/01-specs/<spec-name>.md`
- `docs/02-spec-relations/data-ownership-map.md`

`docs/01-specs/<spec-name>.md` must contain the nine fixed non-empty sections
listed in `templates/spec-template.md`.

`docs/02-spec-relations/data-ownership-map.md` must contain the five fixed
non-empty sections listed in
`templates/data-ownership-map-template.md`, including the fixed header:

`| Data Item | System of Record | Upstream Writers | Downstream Readers | Notes |`

# Validation

## Required Checks
- confirm one explicit `spec-name` is present before writing anything
- confirm `spec-name` is a filename-safe slug and reject any path-like,
  traversal, or absolute-path value before writing anything
- confirm the normalized resolved output path for `docs/01-specs/<spec-name>.md`
  remains contained within `docs/01-specs/`
- confirm the run targets only the two allowed output paths
- confirm `docs/01-specs/<spec-name>.md` contains the fixed nine required
  non-empty sections
- confirm `docs/02-spec-relations/data-ownership-map.md` contains the fixed
  five required non-empty sections and the fixed ownership-table header
- confirm existing authored content survives rerun and that no duplicate
  same-name fixed headings were introduced

## Quality Checks
- starter content remains non-empty even when optional context is sparse
- rerun behavior backfills only missing structure and does not approximate
  excluded scope by adding substitute sections
- execution remains local-only and does not depend on network, external
  services, or projection surfaces

## Soft-fail / Blocked Behavior
- Soft fail: if optional context is incomplete, proceed with template starter
  prompts, keep sections non-empty, and make the remaining gaps visible in the
  generated documents.
- Blocked: if `spec-name` is missing, stop and ask for it before writing any
  file.
- Blocked: if `spec-name` is path-like, contains traversal, or resolves
  outside `docs/01-specs/`, stop before writing any file and report the exact
  invalid input.
- Blocked: if the request would widen the two-file contract or requires a
  destructive whole-file rewrite, stop and report the exact blocker instead of
  improvising.

# Failure Handling

## Missing Context
- If `spec-name` is missing, ask for one explicit `spec-name` and do not guess
  the filename.
- If `spec-name` is path-like, traversal-shaped, absolute, or fails normalized
  containment inside `docs/01-specs/`, block instead of sanitizing or
  rewriting it.
- If optional context is missing, continue with starter prompts rather than
  leaving blank sections.

## Ambiguous Requirement
- If it is unclear whether the request exceeds the v1 boundary, clarify before
  writing outside the exact two-file contract.
- If the ambiguity is only about content details inside the allowed files, use
  conservative starter text and keep unresolved items visible as open
  questions.

## Execution Limitation
- If the required local templates are unavailable, unreadable, or inconsistent
  with the fixed contract, stop and report the limitation instead of inventing
  a new skeleton.
- If an existing file can only be changed by destructive rewrite to comply,
  stop and report that limitation rather than overwriting authored content.

# Boundaries
- Do not touch any file outside:
  - `docs/01-specs/<spec-name>.md`
  - `docs/02-spec-relations/data-ownership-map.md`
- Do not generate multi-spec output or any extra document family.
- Do not approximate excluded scope by adding near-equivalent sections to the
  two allowed files.
- Do not require network access, external services, runtime orchestration, or
  projection / compatibility-surface updates.

# Local references
- `reference.md`: deterministic local-only write, merge, rerun, and refusal
  rules
- `examples.md`: scenario coverage for creation, backfill, rerun safety, and
  refusal behavior
- `templates/spec-template.md`: fixed nine-section spec skeleton
- `templates/data-ownership-map-template.md`: fixed five-section ownership-map
  skeleton and table header
