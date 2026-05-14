# High-Frequency Skill Promotion

## Phase scope

This phase promotes only the first-wave high-frequency skills into the
target-architecture `skills/` tree.

It does not authorize:

- full `.github/skills/` to `skills/` migration
- repo-wide active-path cutover
- creator / reviewer / template contract changes
- runtime/tooling blocker changes

## First-wave skill set

The first-wave promotion set is locked to:

1. `business-intent-alignment`
2. `business-to-technical-translation`
3. `plan-creator`
4. `plan-reviewer`

No additional skill is promoted by this phase.

## Promotion result

The promoted target-architecture locations are:

- `skills/business-intent-alignment/`
- `skills/business-to-technical-translation/`
- `skills/plan-creator/`
- `skills/plan-reviewer/`

These folders are materialized from the current transition-era active path:

- `.github/skills/business-intent-alignment/`
- `.github/skills/business-to-technical-translation/`
- `.github/skills/plan-creator/`
- `.github/skills/plan-reviewer/`

## Source-authority rule

For this first wave, source authority is intentionally one-way and bounded:

- `skills/<skill-name>/` is the target-architecture canonical promotion
  location for the selected first-wave skill.
- `.github/skills/<skill-name>/` remains the current active
  authored/reviewed workflow path during the runway.
- `.github/skills/<skill-name>/` is the transition-era promotion input for
  this phase, not a second canonical source for the promoted target tree.

This phase does not declare `skills/` to be the repo-wide current active path.

## Planning spine interpretation

`business-intent-alignment` and `business-to-technical-translation` are
promoted in this first wave because they are high-frequency planning-spine
skills.

Their promotion does not change their dependency classification:

- they remain planning/workflow and artifact dependencies
- they are not reclassified here as runtime/tooling blockers
- their importance does not authorize repo-wide current-path cutover

## Transition boundary

During this runway:

- `.github/skills/` remains the current active authored/reviewed workflow path
- `skills/` remains the target architecture
- this phase performs selective promotion only
- Copilot transition behavior remains intact because `.github/skills/` is not
  removed or downgraded as the current active path
