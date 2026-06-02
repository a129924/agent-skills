# Python Retrofit Plan Authoring Checklist

Use this checklist before handing a draft to reviewer.

- [ ] The task is really retrofit-plan authoring, not greenfield init, runtime execution, or review.
- [ ] The draft stays inside Retrofit V2 and uses no compatibility mapping from old section names.
- [ ] The section order is exactly:
  - [ ] `## Survey Summary`
  - [ ] `## Gap Analysis`
  - [ ] `## Target Transformation`
  - [ ] `## Migration Strategy`
  - [ ] `## Acceptance Criteria`
- [ ] `## Survey Summary` records concrete current-state facts.
- [ ] `## Gap Analysis` names concrete gaps and likely conflict surfaces.
- [ ] `## Target Transformation` uses locatable paths, entrypoints, and tool names.
- [ ] `## Migration Strategy` contains a parseable `yaml [migration-strategy]` block.
- [ ] `migration-strategy` includes `risk_level`, `destructive_actions`, and `backup_required`.
- [ ] `risk_level` is only `LOW` or `HIGH`; `MEDIUM` is not authored.
- [ ] `LOW` is used only for pure additions or non-destructive configuration changes.
- [ ] Any move, delete, overwrite, relocation, or core-toolchain replacement is reflected in `destructive_actions` and aligned to `HIGH`.
- [ ] `backup_required` aligns with the recovery expectation implied by the risk lane.
- [ ] `## Acceptance Criteria` contains a parseable `yaml [sensing-assertions]` block.
- [ ] Every sensing assertion includes `kind`, `target`, and `expected`.
- [ ] `Migration Direction` stays a strategy declaration and does not replace runtime gate choices.
- [ ] Abstract, contradictory, or misrouted requests triggered stop-and-ask instead of silent guessing.
- [ ] The draft stops at `review-ready` and does not self-approve.
