# Release and tagging procedure

Read only for an authorized release/tag endpoint, including an emergency release. Draft PR creation uses the entrypoint; merge readiness uses applicable repository gates.

## Procedure

2. Inspect the repository structure with a current-state-first rule. If version files exist, include them in the release check. If no version files exist anywhere relevant, degrade to tag-only mode.
3. If multiple version sources exist, require them to agree with each other and with the intended Git tag before release proceeds.
4. Derive the recommended bump direction from accumulated commit semantics: breaking changes outrank features, and features outrank fixes or maintenance.
5. For the normal path, require the full gate: reviewer approval, CI green, base tests passing, project-required type checks passing, lint passing, documentation updated where contracts changed, versions synchronized, a clean workspace, and no tag conflict.
6. Apply checks for the actual ecosystem and repository policy. Python-specific skills apply only to Python work; strict typing is required only when the project mandates it. Record genuinely inapplicable gates as N/A with evidence, never as a fabricated PASS.
7. If the PR changes more than one ecosystem in one release path, require linked version updates for each touched release surface instead of checking only one stack.
8. For the emergency path, allow exactly one bypass: missing pre-release reviewer approval. All other gates from the normal path still apply unchanged.
9. Require concrete emergency evidence before using the emergency path: an explicit marker such as `[emergency]` or `[skip-gate]`, a recorded human confirmation in the current workflow, a short explanation of why the path is urgent, and a release-note or equivalent anomaly record.
10. Hard-block when the target tag already exists, when the workspace is dirty, when version sources conflict, or when any non-bypassable gate fails.
11. When the gate fails, report each failed condition concretely and give repair guidance. When the gate passes, provide the safe next commands, but do not tag or push without authorization for that action. Existing explicit authorization covers in-scope retries; a material scope or risk change requires a new decision.

# Validation

## PASS (all gates satisfied — safe to provide tagging commands)
All of the following must be confirmed positive:
- All required gate signals are present and confirmed: CI, base tests, project-required type checks, lint, documentation sync, reviewer approval (or valid emergency bypass on record)
- All version sources agree with the intended tag
- No uncommitted changes in the workspace
- The target tag does not yet exist in the repository
- For multi-ecosystem PRs: all touched release surfaces have linked version updates

## Hard-Block Conditions (BLOCKED — do not proceed)
- The target tag already exists in the repository — overwriting a tag is destructive and forbidden.
- The workspace has uncommitted changes — a dirty workspace produces an unreliable release artifact.
- Two or more version sources disagree with each other or with the intended Git tag.
- Any non-bypassable gate is failing: CI, base tests, project-required type checks, lint, documentation sync, or clean workspace.

## Red Flags — Treat as Immediate BLOCKED
- The user invokes `[emergency]` or `[skip-gate]` to bypass tests, a dirty workspace, or an existing tag conflict. The emergency path allows only one bypass: missing pre-release reviewer approval. All other gates remain hard requirements.
- Version sources are present but have not been compared. Version synchronization must be confirmed before any tagging command is provided.
- A commit in the release range includes a breaking change but the proposed bump is `patch` or `minor`. Bump direction must be re-derived from accumulated commit semantics.
- The user asks for safe tagging commands before CI or type-check signals have been provided. Do not provide tag commands under incomplete signal.
- The emergency path is invoked without all four required evidence items: explicit marker, recorded human confirmation, short urgency explanation, and release-note or anomaly record.

## Required Checks Before Gate Decision
1. Confirm release path: normal or emergency.
2. Confirm version-source inventory: list all found version files; verify mutual agreement and agreement with the intended tag.
3. Confirm gate signals received: reviewer approval (or emergency bypass noted), CI, tests, type checks, lint, docs-sync, clean workspace, tag uniqueness.
4. For multi-ecosystem PRs: confirm linked version updates exist for every touched release surface.

## On Soft Fail (SOFT FAIL — proceed with explicit limitation)
- A version file is absent entirely — degrade to tag-only mode; state the degradation explicitly before continuing.
- A gate signal is ambiguous or unconfirmed — list it as UNCONFIRMED and require the user to confirm before providing safe tagging commands.

## Quality Checks (best effort — SOFT FAIL if absent)
- A release-note or changelog entry exists for the intended version.
- PR description or commit messages reference the version bump rationale.
- Commit messages in the release range follow semantic-commit conventions (feat/fix/chore/etc.).
- Migration notes are present when any breaking change is included in the release range.

# Failure Handling

## Existing Tag Conflict
- BLOCKED — hard stop; do not provide tagging commands.
- Report the exact tag name and the commit it currently points to.
- Repair guidance: create a new tag with an incremented patch or pre-release suffix; do not delete or move the existing tag without explicit human decision and a documented reason.

## Dirty Workspace
- BLOCKED — hard stop; do not provide tagging or push commands.
- Repair guidance: `git status` to list changes; `git stash` or `git commit` to clean the workspace before proceeding.

## Version Source Conflict
- BLOCKED — halt gate evaluation; do not produce a release decision until all version sources agree.
- Report each conflicting file and its current value.
- Repair guidance: update the lagging sources to match the intended release version, then re-run the gate.

## Missing or Ambiguous Gate Signals
- If CI, test, type-check, lint, or docs-sync signal is absent: mark that gate as UNCONFIRMED; do not count an absent signal as PASS.
- If the user cannot supply the signal: mark the overall release decision as BLOCKED and list the missing signals explicitly.

## Emergency Path Misuse
- If the emergency path is invoked but any required evidence item is missing: BLOCKED — do not allow the bypass.
- Report which evidence items are absent.
- Repair guidance: supply the missing evidence or revert to the normal path.

## Multi-Ecosystem Missing Version Update
- BLOCKED for the affected release surface — flag each ecosystem whose version file was not updated.
- Repair guidance: update each lagging version file and re-run the gate.

## Failed Normal-Gate Condition
- Report each failed condition with its current value and the required value.
- Provide targeted repair commands for each failure (e.g., `git stash`, bump command, lint fix reference).
- After repair, honor existing explicit authorization for the same bounded action; ask again only if scope or risk materially changes.

## Execution Limitation
- If git commands are unavailable or fail to execute: mark the overall gate as INCOMPLETE; list which checks could not be evaluated; do not issue a release decision.
- If version files cannot be read (permissions, encoding, missing filesystem access): report the inaccessible files; degrade to manual-confirm mode and require the user to supply version values explicitly.
- If CI or external gate signals cannot be retrieved: mark those signals as UNCONFIRMED and treat them as BLOCKED until the user provides them manually.
