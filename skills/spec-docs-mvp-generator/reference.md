# Reference

## Local-Only Boundary

- Use only repository-local context plus the templates in `templates/`.
- Do not depend on network fetches, remote templates, external APIs, runtime
  orchestration, or platform installation flows.
- Do not widen the write set beyond:
  - `docs/01-specs/<spec-name>.md`
  - `docs/02-spec-relations/data-ownership-map.md`

## Deterministic First-Creation Rules

When `docs/01-specs/<spec-name>.md` does not exist:

1. Create the file from `templates/spec-template.md`.
2. Keep the fixed nine-section order unchanged.
3. Preserve non-empty starter prompts in every section if caller context is
   still incomplete.

When `docs/02-spec-relations/data-ownership-map.md` does not exist:

1. Create the file from `templates/data-ownership-map-template.md`.
2. Keep the fixed five-section order unchanged.
3. Preserve the fixed ownership-table header and seed content.

If `docs/01-specs/` or `docs/02-spec-relations/` is missing, it is safe to
create the directory before writing the file.

## Safe Rerun Rules

Reruns must be idempotent and non-destructive.

- Preserve existing authored content.
- Backfill only missing fixed sections.
- Backfill the ownership-table header if it is missing.
- Do not insert a second copy of any fixed section heading that already exists.
- Do not delete, clear, or rewrite the entire file just to normalize layout.
- Do not replace authored text inside an existing fixed section with template
  starter text.

## Existing Spec File Update Rules

For `docs/01-specs/<spec-name>.md`:

1. Inspect the file for the fixed headings `Summary`, `Problem`, `Goals`,
   `Non-goals`, `Actors`, `Requirements`, `Data Ownership Notes`,
   `Acceptance Signals`, and `Open Questions`.
2. Keep any existing fixed heading and all authored content already under it.
3. If one or more fixed headings are missing, append only the missing headings
   with starter content from `templates/spec-template.md`.
4. Do not reorder or rename existing headings during v1.
5. Do not create substitute headings for excluded scope such as interfaces,
   flows, or ADRs.

## Existing Ownership Map Update Rules

For `docs/02-spec-relations/data-ownership-map.md`:

1. Inspect the file for the fixed headings `Purpose`, `Ownership Table`,
   `Shared or Derived Data`, `Boundary Notes`, and `Open Questions`.
2. Keep any existing fixed heading and its authored content.
3. If the `Ownership Table` heading exists but the required header row is
   missing, add the header row and one non-empty seed row without deleting
   existing notes.
4. If any fixed heading is missing, append only the missing heading with starter
   content from `templates/data-ownership-map-template.md`.
5. Do not create additional per-spec ownership-map files.

The required header is:

`| Data Item | System of Record | Upstream Writers | Downstream Readers | Notes |`

## Partial-Completion Recovery

If a previous run stopped after creating or patching only one target file:

- rerun the same `spec-name`
- preserve the file that already exists
- create or patch the missing second file
- continue to backfill only missing fixed structure

Partial completion is not a reason to reset or overwrite either file.

## Non-Destructive Update Guardrails

Stop and report a blocker instead of improvising if:

- the caller asks to modify files outside the two-file v1 contract
- the caller asks for multi-spec output in one run
- the requested change requires destructive whole-file rewrite
- the request tries to reopen canonical / projection / runtime boundaries

## Review Checklist

A reviewer should be able to confirm all of the following directly from the
result:

- only the two allowed downstream files were targeted
- the fixed section contracts are present
- each required section is non-empty
- authored content survived rerun
- missing sections or the missing table header were backfilled once
- no duplicate fixed headings were introduced
