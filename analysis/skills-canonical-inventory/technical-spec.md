# Skills Canonical Inventory Technical Spec

Status: READY FOR IMPLEMENTATION PLANNING
Topic: `skills-canonical-inventory`
Last Updated: `2026-06-11`
Source Baseline: `analysis/skills-canonical-inventory/requirements.md`

## Technical Goal

Implement a bounded, deterministic inventory pipeline for canonical `skills/` only, using:
- `scripts/build_skills_inventory.py`
- `artifacts/skills-inventory.jsonl`

No other implementation target is in scope for this topic.

## Translation Summary

The business baseline requires a local-only inventory that covers every canonical skill exactly once, excludes projection and agent surfaces, emits a deterministic `tree_hash`, and fails safely when output cannot be completed. The minimum technical realization is a single repository-local builder script that scans canonical skill roots, computes deterministic hashes, serializes stable JSONL, and writes the final artifact without presenting partial success as complete.

## Requirement Traceability

| Requirement | Technical realization | Bounded work | Artifact / evidence | Dependencies | Cost / burden | Status |
| --- | --- | --- | --- | --- | --- | --- |
| `R1. Canonical Coverage` | Recursively walk canonical `skills/` only, treat each directory containing `SKILL.md` as one skill root, normalize to canonical repo-relative paths, de-duplicate, and sort deterministically | Implement discovery and canonical path normalization in `scripts/build_skills_inventory.py` | `artifacts/skills-inventory.jsonl` contains one record per canonical skill root; record count matches discovered roots | Local filesystem access to `skills/` | Medium build effort; low run burden | Feasible |
| `R2. Scope Exclusion` | Hard-bound discovery root to `skills/`; reject or ignore paths outside canonical root, including projection surfaces and agent paths | Add explicit scope guardrails in discovery logic and record validation | All emitted paths start with `skills/`; out-of-scope path count is `0` | Repository governance remains unchanged for canonical source | Low build effort; low run burden | Feasible |
| `R3. Deterministic Skill Identity` | Compute one `tree_hash` per skill root using the fixed skill-root-relative SHA-256 stream with junk exclusions; include the canonical skill-root path in each record | Implement deterministic file enumeration, contract-conforming hash calculation, and per-record assembly | Every record contains canonical path plus `tree_hash`; recomputation matches | Fixed `tree_hash` contract and junk exclusions | Medium build effort; medium verification burden | Feasible |
| `R4. Artifact Validity` | Serialize the inventory as UTF-8 JSON Lines with one complete JSON object per skill record | Implement stable JSONL writer with one object per line and newline termination | JSON parser accepts every line in `artifacts/skills-inventory.jsonl` | Writable `artifacts/` path | Low build effort; low run burden | Feasible |
| `R5. Repeatable Output` | Apply stable record ordering and deterministic JSON serialization so unchanged inputs yield byte-identical outputs | Fix record ordering, field ordering, and newline behavior in writer | Two runs against unchanged inputs produce byte-identical artifact bytes | No nondeterministic data sources | Low build effort; low run burden | Feasible |
| `R6. Local-Only Generation` | Use repository-local filesystem inspection only; no network fetches or external service calls | Keep implementation within Python standard-library or already-local runtime capabilities used only against the checkout | Offline execution still generates and validates the artifact | Local checkout only | Low build effort; low operational burden | Feasible |
| `R7. Safe Failure on Partial or Unauthorized Writes` | Stage output in a temporary file and publish the final artifact only after full validation succeeds; return a visible failure when write permissions or completion guarantees are missing | Implement temp-file write, final validation, atomic replace, and non-success exit path | Failure leaves previous valid artifact untouched and prevents a new partial artifact from masquerading as success | Write access to target directory and atomic replace support on local filesystem | Low-to-medium build effort; low run burden | Feasible |

## Minimum Record Contract

The artifact needs only the minimum deterministic fields required by the frozen baseline:

| Field | Meaning | Requirement coverage |
| --- | --- | --- |
| canonical skill-root path | Repo-relative canonical path for the in-scope skill root under `skills/` | `R1`, `R2`, `R5` |
| `tree_hash` | Deterministic hash for the in-scope skill tree using the fixed contract | `R3`, `R5` |

Additional fields are optional only if they are derived locally, deterministic, and do not change topic scope.

## Bounded Implementation Workstreams

### W1. Canonical Skill Discovery

- Enumerate only under top-level `skills/`.
- Define one inventory unit as a directory containing `SKILL.md`.
- Normalize discovered paths into canonical repo-relative skill-root paths.
- De-duplicate and stable-sort before any hashing or writing begins.

Cost of realization:
- Medium implementation effort because discovery must be exact and must not bleed into projection or agent surfaces.
- Low operational burden after implementation because the repository layout is local and bounded.

### W2. Deterministic Tree Hashing

- For each discovered skill root, enumerate in-scope files according to the fixed junk-exclusion rules.
- Convert file paths to skill-root-relative form before hashing.
- Feed the stable path-content stream into SHA-256 exactly once per skill record.

Cost of realization:
- Medium implementation effort because determinism failures will create false inventory drift.
- Medium verification burden because hash behavior must be independently checkable.

### W3. Stable JSONL Emission

- Assemble one JSON object per skill record.
- Serialize in deterministic key order.
- Emit newline-delimited UTF-8 output in stable record order.

Cost of realization:
- Low implementation effort.
- Low operational burden because JSONL is easy to inspect and parse.

### W4. Safe Publish and Failure Signaling

- Write into a temporary file inside the target directory.
- Validate line count, parseability, and required fields before publish.
- Replace the final artifact atomically only after validation passes.
- Exit with visible failure when the target path is not writable or when generation is interrupted.

Cost of realization:
- Low-to-medium implementation effort because safe publish semantics require care.
- Low ongoing burden once the write path is hardened.

## Acceptance Checks

1. Coverage check:
   Count directories under canonical `skills/` that contain `SKILL.md`; verify the artifact contains exactly the same number of records and no duplicate canonical paths.
2. Scope check:
   Verify every emitted canonical path starts with `skills/` and that no record references `agents/`, `.github/skills/`, `.codex/skills/`, or another `.<platform>/skills/` root.
3. Hash contract check:
   Recompute `tree_hash` for every record, or for a full deterministic sample if execution constraints require batching, and confirm exact equality with the artifact value.
4. Format check:
   Parse every JSONL line as a JSON object and verify required fields are present and non-empty.
5. Repeatability check:
   Run the builder twice on unchanged in-scope contents and verify the artifact bytes are identical.
6. Offline check:
   Confirm the builder does not require network access and still succeeds against a local checkout.
7. Safe-failure check:
   Simulate an unwritable target or interrupted publish path and confirm that no truncated final artifact is accepted as success.

## Architecture-Compliance Self-Check

| Area | Result | Notes |
| --- | --- | --- |
| Canonical source boundary | Fits existing architecture | `skills/` is the repository source of truth; projection surfaces remain compatibility-only and are excluded |
| Topic scope boundary | Fits existing architecture | The implementation remains limited to canonical skills inventory and does not expand into agent or runtime work |
| Artifact target | Fits with prerequisites | `artifacts/skills-inventory.jsonl` is acceptable if the working tree has write access to `artifacts/` |
| Hash contract | Fits with prerequisites | The `tree_hash` contract is already fixed; implementation must follow it exactly rather than reinterpret it |
| Dependency model | Fits existing architecture | A local Python script operating on repository files only stays within bounded repo-local workflow expectations |

No waiver is currently required.

## Conflict and Rollback Triggers

Rollback to business alignment is required if any of the following becomes true:

1. Repository governance changes and canonical skill source is no longer limited to top-level `skills/`.
2. The fixed `tree_hash` contract or junk exclusions are not available in a form the implementation can apply deterministically.
3. Downstream consumers require projection-surface, agent, or runtime inventory in the same artifact.
4. The repository contains path patterns under `skills/` that make the canonical skill-root definition ambiguous and materially change record coverage.

For each rollback case, the renegotiation question is the same:
- Is the business promise still "canonical `skills/` inventory only", or has the topic scope changed and therefore requires a new frozen baseline?

## Blockers

- None at this stage. Every frozen business requirement maps to bounded technical work or an explicit rollback trigger.
