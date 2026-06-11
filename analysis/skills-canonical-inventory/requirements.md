# Skills Canonical Inventory Requirements

Status: FROZEN
Topic: `skills-canonical-inventory`
Last Updated: `2026-06-11`

## Problem Statement

Repository maintainers and downstream consumers need one deterministic inventory of the canonical reusable skills in this repository. The inventory must reflect only the canonical `skills/` source tree, remain locally verifiable, and avoid mixing in compatibility or projection surfaces that are not the repository source of truth.

## Scope Boundary

In scope:
- Canonical skill inventory derived only from top-level `skills/`.
- Inventory units defined as directories under `skills/` that contain `SKILL.md`.
- A deterministic inventory artifact for downstream review and consumption.
- A deterministic `tree_hash` per in-scope skill using the already-fixed contract: skill-root-relative SHA-256 stream with junk exclusions.

Out of scope:
- `agents/` or custom-agent inventory.
- `.github/skills/`, `.codex/skills/`, or any other `.<platform>/skills/` projection surface.
- Runtime orchestration, projection sync, release automation, or non-skill artifact inventory.

## Actors

- Repository maintainer: generates the canonical skills inventory from a repository snapshot.
- Reviewer: checks that the inventory matches canonical scope and does not include out-of-scope sources.
- Downstream consumer: reads the inventory artifact and uses it as a deterministic description of canonical skills.

## Measurable Requirements

### R1. Canonical Coverage

- Actor: repository maintainer
- Condition: when generating inventory from a repository snapshot
- Observable outcome: every in-scope skill root under canonical `skills/` appears exactly once in the inventory
- Metric / decision rule: inventory record count equals the number of in-scope skill roots; duplicate canonical skill-root paths equal `0`
- Evidence signal: a reviewer can compare the emitted canonical paths against the enumerated in-scope skill roots in `skills/`
- Failure meaning: missing or duplicate records make the inventory unusable as the canonical baseline

### R2. Scope Exclusion

- Actor: reviewer
- Condition: when validating the emitted inventory
- Observable outcome: no record originates from any out-of-scope source
- Metric / decision rule: record count for `agents/`, custom-agent locations, `.github/skills/`, `.codex/skills/`, and other `.<platform>/skills/` locations equals `0`
- Evidence signal: every emitted record path is rooted under canonical `skills/`
- Failure meaning: the inventory stops being a trustworthy statement of canonical repository truth

### R3. Deterministic Skill Identity

- Actor: downstream consumer
- Condition: when reading a generated skill record
- Observable outcome: each record exposes the canonical skill-root path and a `tree_hash` that matches the fixed contract for that skill tree
- Metric / decision rule: `100%` of records include a non-empty canonical skill-root path and a non-empty `tree_hash`; independent recomputation under the fixed contract matches the stored `tree_hash` for every checked record
- Evidence signal: a reviewer or consumer can recompute the hash from the same repository snapshot and observe an exact match
- Failure meaning: consumers cannot verify whether a skill changed or whether the inventory is current

### R4. Artifact Validity

- Actor: downstream consumer
- Condition: when consuming the inventory artifact
- Observable outcome: the artifact is valid UTF-8 JSON Lines with one complete skill record per line
- Metric / decision rule: `100%` of lines parse as JSON objects; successful generation yields exactly one line per in-scope skill root
- Evidence signal: a line-by-line JSON parser accepts the artifact without correction or skipped lines
- Failure meaning: downstream tooling cannot consume the inventory deterministically

### R5. Repeatable Output

- Actor: repository maintainer
- Condition: when generating the inventory twice from the same in-scope repository contents
- Observable outcome: both runs produce byte-identical inventory output
- Metric / decision rule: byte diff between the two artifact files equals `0` when no in-scope files or relevant paths changed
- Evidence signal: checksum or binary comparison of the two generated artifacts
- Failure meaning: reviewers cannot distinguish meaningful skill changes from inventory noise

### R6. Local-Only Generation

- Actor: repository maintainer
- Condition: when external network access is unavailable
- Observable outcome: inventory generation and verification still complete from local repository state alone
- Metric / decision rule: successful generation does not require fetching remote metadata or calling external services
- Evidence signal: the inventory can be generated and validated in an offline environment from the repository checkout
- Failure meaning: the inventory cannot serve as a local canonical baseline

### R7. Safe Failure on Partial or Unauthorized Writes

- Actor: repository maintainer
- Condition: when generation is interrupted or the target artifact path is not writable
- Observable outcome: the process fails explicitly and does not leave a result that can be mistaken for a successful complete inventory
- Metric / decision rule: failure is observable through a non-success outcome, and a previously valid artifact is not replaced by truncated or partial content
- Evidence signal: the maintainer observes a failure signal and no newly accepted partial inventory artifact
- Failure meaning: consumers may trust an incomplete or corrupted inventory

## Resolved Contradictions

1. Statement A: some tools consume `.github/skills/`, `.codex/skills/`, or other platform-specific surfaces.
2. Statement B: repository governance says `skills/` is the canonical source of truth and platform paths are compatibility surfaces only.
3. Why both cannot be true at once for this topic: including projection surfaces would collapse compatibility copies into canonical inventory and make the output non-authoritative.
4. Decision: only canonical `skills/` content is in scope for this inventory.

1. Statement A: the repository contains workflow-agent artifacts and related bounded agent definitions.
2. Statement B: this topic is explicitly limited to canonical skill inventory.
3. Why both cannot be true at once for this topic: mixing agent inventory into the same artifact would change the actor model, output meaning, and downstream acceptance checks.
4. Decision: agent and custom-agent inventory are excluded from this topic.

## Extreme-Boundary Decisions

- No network or degraded external dependency:
  Inventory generation must remain successful from local repository contents only; external reachability cannot change coverage, scope, or hashing results.
- Wrong role or missing write permission:
  An unwritable artifact target is a visible failure state, not a partial success; the output must not be treated as a completed inventory.
- Interrupted or partially completed generation:
  Partial emission must not be accepted as a successful inventory result.
- Lowest-volume and peak-volume repository snapshots:
  The same rules apply whether the repository snapshot contains one in-scope skill or the full canonical `skills/` set; coverage must still be exact and out-of-scope records must remain zero.

## Assumptions

- The canonical unit of inventory is a directory under `skills/` that contains `SKILL.md`.
- The fixed `tree_hash` contract remains unchanged for this topic: skill-root-relative SHA-256 stream with junk exclusions.
- Downstream consumers accept a canonical inventory artifact located at `artifacts/skills-inventory.jsonl`.

## Non-Goals

- Defining projection-sync behavior between canonical skills and compatibility surfaces.
- Designing or implementing runtime skill loading, release packaging, or registry semantics.
- Expanding scope to agents, custom agents, or non-skill repository artifacts.
- Changing or renegotiating the fixed `tree_hash` contract.

## Blockers

- None. This baseline is frozen for technical translation within the bounded topic intent above.
