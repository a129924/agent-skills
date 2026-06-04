# Projection Adapter Design

## Purpose

Define how canonical content under `skills/` may be projected into
platform-facing surfaces without treating those surfaces as authority.

This document is Phase 3 design only. It does not declare projection
materialization complete.

## Shared Rules

- `skills/` is the only canonical skill-content tree.
- `.github/skills/` and `.codex/skills/` are compatibility or projection
  surfaces only.
- `.codex/skills/` is a partial projected allowlist, not a symmetric authority
  tree.
- `copilot-instructions-init` is excluded from the generic projection set.
- If a projected surface cannot express canonical behavior safely, leave that
  skill unprojected and require human review.

## Projection Modes

### Copy

Use direct projection when the projected skill is instruction-only and has no
surface-sensitive runtime path assumptions.

Current low-risk candidates:

- `business-intent-alignment`
- `business-to-technical-translation`
- `git-branch-naming`
- `git-commit-convention`
- `git-post-merge-workflow`
- `worktree-manager`
- `agent-skill-reviewer`

### Rewrite

Use projection-time path rewrite when the canonical skill is portable, but the
projected surface requires local path adjustments in examples, references, or
CLI invocation snippets.

Current rewrite candidates:

- `plan-creator`
- `plan-reviewer`
- `python-blueprint-authoring`
- `python-blueprint-review`
- `python-plan-authoring`
- `python-pre-commit`
- `python-pyproject-toolconfig`

Rewrite constraints:

- preserve canonical section meaning and blocking semantics
- rewrite only surface-facing paths, not authority ownership
- never point the projected skill at a different contract source

### Adapter

Use an explicit adapter boundary when projection needs more than deterministic
path rewrite.

Current adapter candidates:

- `agent-skill-creator`
- `agent-skill-template`
- `plan-step-tracker`
- `sense-env-scaffold`
- `python-project-init-greenfield`
- `python-project-retrofit`

Adapter triggers include:

- script runtime behavior that changes by surface
- path-sensitive authoring or review contracts
- execution flows that depend on platform-specific supporting files

### Excluded / Blocked

Do not include these in generic projection:

- `copilot-instructions-init`

Reason:

- it remains platform-specific
- it writes `.github/copilot-instructions.md`
- future core/adapter split is separate work

## `.codex/skills/` Rules

- Keep `.codex/skills/` as an explicit allowlist.
- Do not add entries solely because the canonical skill now exists in
  `skills/`.
- Each projected entry must name exactly one upstream source path.
- Symlink or copied projection provenance must remain traceable in
  `.codex/skills/provenance.md`.
- If upstream changes are not yet committed, do not rewrite provenance to
  pretend commit-level validation already happened.

## Materialization Gate

A skill may be materialized into a projected surface only when all are true:

- its projection mode is known
- any required rewrite or adapter rule is documented
- projected behavior still matches canonical semantics
- provenance can be revalidated without guessing
