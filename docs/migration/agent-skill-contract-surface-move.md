# Agent Skill Contract Surface Move

## Scope

This document records Topic A implementation for
`agent-skill-contract-surface-move`.

In scope:
- copy `.github/skills/agent-skill-creator/` to `skills/agent-skill-creator/`
- copy `.github/skills/agent-skill-reviewer/` to `skills/agent-skill-reviewer/`
- copy `.github/skills/agent-skill-template/` to `skills/agent-skill-template/`
- preserve relative local references inside each copied skill folder

Out of scope:
- changing the current active authored/reviewed workflow path
- editing `.github/skills/agent-skill-*`
- updating runtime, installer, projection, or planning-spine surfaces
- touching any files outside the approved write set

## Candidate Set

Source folders selected for direct copy:
- `.github/skills/agent-skill-creator/`
  - `SKILL.md`
  - `blueprint.md`
  - `folder-contract.md`
  - `examples.md`
- `.github/skills/agent-skill-reviewer/`
  - `SKILL.md`
  - `review-checklist.md`
  - `examples.md`
- `.github/skills/agent-skill-template/`
  - `SKILL.md`
  - `template.md`
  - `reference.md`
  - `folder-contract.md`

Selection basis:
- the approved topic scope names these three contract surfaces only
- each folder is self-contained and uses local relative companion references
- no additional `.github/skills/*` folders were pulled into this topic

## Copied Result

Created target-architecture mirrors under `skills/`:
- `skills/agent-skill-creator/`
  - `SKILL.md`
  - `blueprint.md`
  - `folder-contract.md`
  - `examples.md`
- `skills/agent-skill-reviewer/`
  - `SKILL.md`
  - `review-checklist.md`
  - `examples.md`
- `skills/agent-skill-template/`
  - `SKILL.md`
  - `template.md`
  - `reference.md`
  - `folder-contract.md`

Copy behavior:
- content was first copied as-is from the `.github/skills/` source folders
- after independent review found canonical-target wording drift, bounded
  target-side contract rework aligned:
  - `skills/agent-skill-creator/SKILL.md`
  - `skills/agent-skill-template/template.md`
  so the `skills/` tree now points new authoring/output to
  `skills/<skill-name>/` while still preserving `.github/skills/` as a
  transition-era active compatibility surface
- local companion filenames remain unchanged, so relative in-folder references
  such as `template.md`, `folder-contract.md`, `review-checklist.md`,
  `reference.md`, `examples.md`, and `blueprint.md` remain valid after the move
- no source-folder edits were made as part of this topic

## Compatibility Preserved

`.github/skills/` compatibility is preserved in this phase:
- source folders remain in place and were not modified
- target-side contract wording now distinguishes:
  - `skills/` as the canonical authoring target for this transition topic
  - `.github/skills/` as a preserved current active authored/reviewed workflow
    path until a later cutover topic changes that contract
- this topic does not claim active-path cutover or rewrite shared runtime,
  installer, projection, or planning-spine surfaces
- the copied `skills/` folders now exist as target-architecture surfaces while
  `.github/skills/` continues to serve current compatibility needs

## Deferred Follow-up Lanes

The following lanes are explicitly deferred:
- runtime/tooling cutover to make `skills/` the active workflow path
- installer or projection-surface updates, including any `.<platform>/skills/`
  adapters
- downstream planning-spine or other skill updates that still reference
  `.github/skills/`
- mirror cleanup, deduplication, or eventual source-of-truth consolidation
- any README, VERSION, or repo-positioning updates

## Notes

Observed implementation constraints:
- the topic began as a source-faithful copy
- reviewer-driven rework was limited to target-side canonical contract wording
  inside the approved `skills/agent-skill-*` write set
- no `.github/skills/agent-skill-*` source file was edited, and no active-path
  cutover was claimed
