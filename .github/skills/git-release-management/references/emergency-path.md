# Emergency path

## Allowed bypass

Emergency mode may bypass only the waiting period for ordinary reviewer approval.

It may not bypass:

- failing tests
- failing strict typing
- failing lint
- version conflicts
- dirty workspace
- existing tag conflicts

## Required markers

Require all of these:

- explicit marker such as `[emergency]` or `[skip-gate]`
- human confirmation
- release-note or equivalent anomaly record
- a short explanation of why the path is urgent

## Aftercare

Emergency releases must produce a follow-up reminder for the skipped human-review timing or non-core administrative step that was bypassed.
