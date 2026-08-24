# Examples

## Scenario 1: New single-spec generation

Input:

- `spec-name`: `customer-profile-sync`
- context:
  - summary: keep customer profile changes synchronized across internal systems
  - goals: define the minimum v1 sync contract
  - actors: account service, CRM sync worker, support tooling

Expected behavior:

- create `docs/01-specs/customer-profile-sync.md`
- create `docs/02-spec-relations/data-ownership-map.md`
- use the fixed template sections with non-empty starter content
- keep the run limited to the two allowed files

## Scenario 2: Existing spec file missing required sections

Starting state:

- `docs/01-specs/customer-profile-sync.md` already exists
- the file already contains authored `Summary`, `Problem`, and `Goals`
- the file is missing `Data Ownership Notes`, `Acceptance Signals`, and
  `Open Questions`

Expected behavior:

- preserve the existing authored content
- append only the missing fixed sections with starter prompts
- do not duplicate `Summary`, `Problem`, or `Goals`
- do not rewrite the whole file

## Scenario 3: Existing ownership map missing the required table header

Starting state:

- `docs/02-spec-relations/data-ownership-map.md` already exists
- the file has a `## Ownership Table` section
- the required table header is missing or was replaced with free-form notes

Expected behavior:

- preserve the existing notes
- backfill the required header
  `| Data Item | System of Record | Upstream Writers | Downstream Readers | Notes |`
- add one non-empty seed row if the table would otherwise be blank
- do not create a second `Ownership Table` section

## Scenario 4: Out-of-scope request must be refused

Input:

- `spec-name`: `customer-profile-sync`
- extra request: also generate architecture principles, interface inventory,
  and one ADR

Expected behavior:

- refuse or reroute the extra request because it exceeds the v1 contract
- keep the allowed scope limited to:
  - `docs/01-specs/customer-profile-sync.md`
  - `docs/02-spec-relations/data-ownership-map.md`
- do not approximate the request by adding architecture or ADR sections into
  the spec template

## Scenario 5: Missing required `spec-name`

Input:

- no `spec-name` provided

Expected behavior:

- stop and ask for one explicit `spec-name`
- do not guess the filename
- do not create any downstream file before the missing input is resolved
