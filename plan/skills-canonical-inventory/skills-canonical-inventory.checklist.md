# Skills Canonical Inventory Planning Checklist

Use this checklist during independent plan review and planner final gate for
topic `skills-canonical-inventory`.

## Analysis Traceability

- [X] `plan/skills-canonical-inventory/skills-canonical-inventory.plan.md`
      declares strict-mode analysis routing.
- [X] The plan names both frozen analysis inputs exactly:
      `analysis/skills-canonical-inventory/requirements.md` and
      `analysis/skills-canonical-inventory/technical-spec.md`.
- [X] The plan records SHA-256 values for both analysis inputs.
- [X] The plan states that later creator work must map 100% to
      `analysis/skills-canonical-inventory/technical-spec.md`.

## Scope and Boundary Integrity

- [X] Goal / Outcome stays bounded to canonical `skills/` inventory only.
- [X] In-scope implementation is limited to canonical discovery, deterministic
      hashing, deterministic JSONL emission, and safe publish behavior.
- [X] Out-of-scope text explicitly excludes:
      `agents/`, custom agents, `.github/skills/`, `.codex/skills/`,
      other `.<platform>/skills/`, runtime work, projection work, README work,
      and VERSION work.
- [X] `skills/**` is declared read-only input surface, not an editable surface.
- [X] The plan explicitly marks this topic as non-stable and non-release.
- [X] The plan contains explicit Non-goals, Modify, and Read-only boundaries.

## Artifact Contract

- [X] `Artifact Paths` lists exact repo-visible paths only.
- [X] Every artifact path is role-labeled with owner and role.
- [X] The only later implementation targets listed are:
      `scripts/build_skills_inventory.py` and
      `artifacts/skills-inventory.jsonl`, and
      `tests/test_build_skills_inventory.py`.
- [X] The plan does not authorize README, VERSION, `.github/**`, `.codex/**`,
      or `agents/**` edits.
- [X] The plan explains why
      `plan/skills-canonical-inventory/skills-canonical-inventory.review-log.md`
      is not yet present.

## Workflow Contract

- [X] `Status / Allowed Transitions` uses canonical workflow transitions only.
- [X] The plan and `*.step.md` reflect the exact locked planning workflow:
      worktree -> analysis -> create-agent-plan -> draft plan commit ->
      plan review -> plan fix -> planner final gate -> human check.
- [X] `plan/skills-canonical-inventory/skills-canonical-inventory.step.md`
      includes `Workflow Stages`, `Actionable Steps`, and `Handoff / Gate Notes`.
- [X] The step artifact records human check as an explicit gating condition
      before implementation.
- [X] If implementation has begun, the step artifact reflects that human check
      has passed in repo-visible truth.

## Implementation Mapping

- [X] `Implementation Steps` map directly to the technical baseline workstreams:
      canonical discovery, deterministic hashing, stable JSONL emission, and
      safe publish / failure signaling.
- [X] The plan locks the exact `tree_hash` byte-stream contract to
      skill-root-relative POSIX paths in lexicographic order, hashed as
      `relative_path + NUL + file_bytes + NUL`.
- [X] The plan explicitly permits one bounded test file for the inventory
      builder and limits that test scope to canonical discovery, stable output,
      hash sensitivity, and junk exclusion.
- [X] The plan does not invent implementation files beyond the three locked
      targets.
- [X] The plan states that extra implementation paths require replanning.

## Reviewer and Gate Outputs

- [X] `Reviewer Handoff` is exactly one JSON object with
      `verdict`, `blocking_issues`, and `copilot_feedback_triage`.
- [X] `Post-merge / release actions` explicitly says that no release action,
      VERSION bump, or README update is allowed.
- [X] `Open Questions / Unresolved Items` does not hide unresolved blocking
      ambiguity.
- [X] No placeholder wording such as `TBD`, `later`, or `follow normal process`
      remains anywhere in the plan artifacts.
