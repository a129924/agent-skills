# Skills Canonical Inventory Planning Checklist

Use this checklist during independent plan review and planner final gate for
topic `skills-canonical-inventory`.

## Analysis Traceability

- [ ] `plan/skills-canonical-inventory/skills-canonical-inventory.plan.md`
      declares strict-mode analysis routing.
- [ ] The plan names both frozen analysis inputs exactly:
      `analysis/skills-canonical-inventory/requirements.md` and
      `analysis/skills-canonical-inventory/technical-spec.md`.
- [ ] The plan records SHA-256 values for both analysis inputs.
- [ ] The plan states that later creator work must map 100% to
      `analysis/skills-canonical-inventory/technical-spec.md`.

## Scope and Boundary Integrity

- [ ] Goal / Outcome stays bounded to canonical `skills/` inventory only.
- [ ] In-scope implementation is limited to canonical discovery, deterministic
      hashing, deterministic JSONL emission, and safe publish behavior.
- [ ] Out-of-scope text explicitly excludes:
      `agents/`, custom agents, `.github/skills/`, `.codex/skills/`,
      other `.<platform>/skills/`, runtime work, projection work, README work,
      and VERSION work.
- [ ] `skills/**` is declared read-only input surface, not an editable surface.
- [ ] The plan explicitly marks this topic as non-stable and non-release.
- [ ] The plan contains explicit Non-goals, Modify, and Read-only boundaries.

## Artifact Contract

- [ ] `Artifact Paths` lists exact repo-visible paths only.
- [ ] Every artifact path is role-labeled with owner and role.
- [ ] The only later implementation targets listed are:
      `scripts/build_skills_inventory.py` and
      `artifacts/skills-inventory.jsonl`.
- [ ] The plan does not authorize README, VERSION, `.github/**`, `.codex/**`,
      or `agents/**` edits.
- [ ] The plan explains why
      `plan/skills-canonical-inventory/skills-canonical-inventory.review-log.md`
      is not yet present.

## Workflow Contract

- [ ] `Status / Allowed Transitions` uses canonical workflow transitions only.
- [ ] The plan and `*.step.md` reflect the exact locked planning workflow:
      worktree -> analysis -> create-agent-plan -> draft plan commit ->
      plan review -> plan fix -> planner final gate -> human check.
- [ ] `plan/skills-canonical-inventory/skills-canonical-inventory.step.md`
      includes `Workflow Stages`, `Actionable Steps`, and `Handoff / Gate Notes`.
- [ ] The step artifact stops before implementation and marks remaining gates as
      pending.
- [ ] The step artifact states that implementation may not begin before human
      check.

## Implementation Mapping

- [ ] `Implementation Steps` map directly to the technical baseline workstreams:
      canonical discovery, deterministic hashing, stable JSONL emission, and
      safe publish / failure signaling.
- [ ] The plan does not invent implementation files beyond the two locked
      targets.
- [ ] The plan states that extra implementation paths require replanning.

## Reviewer and Gate Outputs

- [ ] `Reviewer Handoff` is exactly one JSON object with
      `verdict`, `blocking_issues`, and `copilot_feedback_triage`.
- [ ] `Post-merge / release actions` explicitly says that no release action,
      VERSION bump, or README update is allowed.
- [ ] `Open Questions / Unresolved Items` does not hide unresolved blocking
      ambiguity.
- [ ] No placeholder wording such as `TBD`, `later`, or `follow normal process`
      remains anywhere in the plan artifacts.
