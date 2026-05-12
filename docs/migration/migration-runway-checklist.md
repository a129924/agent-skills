# Migration Runway Checklist

## Runway Summary

- Runway topic: `copilot-to-codex-migration`
- Checklist role: repo-visible Setup Agent support artifact for runway-wide
  status, frozen boundaries, and authority-chain checks
- Runway mode: migration runway only; not full migration
- Current active authored/reviewed workflow path: `.github/skills/`
- Target architecture path: `skills/`
- Big Feature Branch: `feat/andrew/copilot-to-codex-migration`
- Forbidden direct merge branch: `dev`
- Branch rule: bounded phase branches merge back into
  `feat/andrew/copilot-to-codex-migration` first
- Current Big Feature Branch release version: `0.52.0`
- Current Big Feature Branch release tag: `v0.52.0`
- Current checklist snapshot status: `partial-source-of-truth`
- Source-of-truth note:
  - The following requested source artifacts are missing in this worktree:
    - `plan/platform-coupling-inventory/platform-coupling-inventory.plan.md`
  - This checklist does not infer their missing contract contents from evidence
    artifacts.

## Phase Status

Status model used here:

- `planned`
- `in-progress`
- `merged-to-big-feature-branch`
- `reflected-in-checklist`
- `source-of-truth-incomplete`
- `blocked`

Notes:

- `merged-to-big-feature-branch` does not by itself prove authority-chain
  completeness.
- `inventory-complete` is never treated as `transition-complete`.

| Phase / Topic | Purpose | Status | Evidence status | Plan contract status | Working / merge target | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| `positioning-freeze` | Freeze current state, target architecture, and migration boundary wording without active-path cutover | `reflected-in-checklist` | evidence present in frozen docs and phase plan | present | merged into `feat/andrew/copilot-to-codex-migration` | Source-of-truth complete for this checklist |
| `platform-coupling-inventory` | Inventory path / workflow / artifact / blocker coupling without performing migration | `source-of-truth-incomplete` | evidence present: `docs/migration/platform-coupling-inventory.md` | missing: `plan/platform-coupling-inventory/platform-coupling-inventory.plan.md` | intended merge target: `feat/andrew/copilot-to-codex-migration` | Evidence cannot replace upstream phase contract |
| `skill-authoring-path-transition` | Transition creator / reviewer / template contracts only; no full promotion | `reflected-in-checklist` | merged contract-surface changes visible in creator / reviewer / template artifacts | present: `plan/skill-authoring-path-transition/skill-authoring-path-transition.plan.md` | merged into `feat/andrew/copilot-to-codex-migration` | Current phase contract is readable; upstream inventory plan contract is still missing, so inherited authority remains partially incomplete |

## Surface / Skill Status

Surface status model used here:

- `not-inventoried`
- `inventory-complete`
- `transition-planned`
- `transition-complete`
- `tracked-dependency`
- `confirmed-blocker`
- `source-of-truth-incomplete`

Notes:

- `inventory-complete` means the surface was classified by inventory evidence.
- `transition-complete` requires a readable transition contract and completed
  phase output; evidence alone is insufficient.
- Planning spine skills default to `tracked-dependency`, not blocker, unless
  there is explicit evidence.

| Surface / Skill | Surface type | Current role | Current status | Dependency / blocker classification | Owner / next phase | Evidence / contract note |
| --- | --- | --- | --- | --- | --- | --- |
| `.github/skills/business-intent-alignment` | planning spine skill | downstream producer / consumer of analysis-layer requirements | `tracked-dependency` | primary tracked dependency: `workflow dependency`, `artifact dependency`; secondary: `contract dependency`, `source/path dependency`; not a default blocker | downstream to later transition work | Inventory evidence still applies; no merged transition evidence promoted this skill to blocker status |
| `.github/skills/business-to-technical-translation` | planning spine skill | downstream producer / consumer of analysis-layer technical spec | `tracked-dependency` | primary tracked dependency: `workflow dependency`, `artifact dependency`; secondary: `contract dependency`, `source/path dependency`; not a default blocker | downstream to later transition work | Inventory evidence still applies; no merged transition evidence promoted this skill to blocker status |
| `.github/skills/agent-skill-creator/` | creator contract surface | current authoring-path producer | `transition-complete` | contract-transition target; workflow + artifact dependency | follow-up runtime/tooling and later cutover phases | Contract-transition phase is planned and merged; creator surface was updated without declaring active-path cutover |
| `.github/skills/agent-skill-reviewer/` | reviewer contract surface | current review-path validator | `transition-complete` | contract-transition target; workflow + artifact dependency | follow-up runtime/tooling and later cutover phases | Reviewer surface was updated and merged in PR #72 as part of the bounded transition phase |
| `.github/skills/agent-skill-template/` | template contract surface | current scaffold contract source | `transition-complete` | contract-transition target; workflow + artifact dependency | follow-up runtime/tooling and later cutover phases | Template surface was updated and merged in PR #72 as part of the bounded transition phase |
| `.github/skills/sense-env-scaffold/` | runtime/tooling surface | executable path dependency | `inventory-complete` | `confirmed-blocker` | future runtime/tooling transition phase | Explicit inventory evidence marks this as runtime/tooling blocker |
| `.github/skills/plan-step-tracker/` | runtime/tooling surface | executable gate helper path dependency | `inventory-complete` | `confirmed-blocker` | future runtime/tooling transition phase | Explicit inventory evidence marks this as runtime/tooling blocker |
| `.github/skills/python-project-init-greenfield/` | runtime/tooling surface | generated baseline layout dependency | `inventory-complete` | `confirmed-blocker` | future runtime/tooling transition phase | Explicit inventory evidence marks this as runtime/tooling blocker |
| `.github/skills/python-project-retrofit/` | runtime/tooling surface | retrofit acceptance handoff path dependency | `inventory-complete` | `confirmed-blocker` | future runtime/tooling transition phase | Explicit inventory evidence marks this as runtime/tooling blocker |
| `.github/skills/copilot-instructions-init/` | runtime/tooling surface | generator / fingerprint dependency | `inventory-complete` | `confirmed-blocker` | future runtime/tooling transition phase | Explicit inventory evidence marks this as runtime/tooling blocker |

## Frozen Boundaries

Frozen boundary status model used here:

- `frozen`
- `drift-not-found`
- `drift-detected`

| Boundary ID | Boundary statement | Status | Source artifact | Notes |
| --- | --- | --- | --- | --- |
| `FB-01` | This runway is not full migration | `frozen` | `analysis/codex-migration-runway/requirements.md` | Runway-only boundary remains active |
| `FB-02` | `.github/skills/` remains the current active authored/reviewed workflow path | `frozen` | `AGENTS.md`, `docs/repo-positioning.md`, `plan/positioning-freeze/positioning-freeze.plan.md` | Current-vs-target distinction remains explicit |
| `FB-03` | `skills/` is target architecture only, not current active path | `frozen` | `AGENTS.md`, `docs/repo-positioning.md`, `plan/positioning-freeze/positioning-freeze.plan.md` | No source artifact in this set authorizes active-path cutover |
| `FB-04` | Big Feature Branch is `feat/andrew/copilot-to-codex-migration` | `frozen` | `analysis/codex-migration-runway/technical-spec.md` | Phase branches should merge here first |
| `FB-05` | No direct phase merge to `dev` | `frozen` | `analysis/codex-migration-runway/requirements.md`, `analysis/codex-migration-runway/technical-spec.md` | `dev` stays outside runway phase routing |
| `FB-06` | inventory, contract transition, runtime/tooling transition, promotion, and installer work must not collapse into one phase | `frozen` | `analysis/codex-migration-runway/requirements.md`, `docs/migration/platform-coupling-inventory.md` | Inventory evidence reinforces this separation |
| `FB-07` | Evidence cannot replace upstream plan contract | `frozen` | this checklist, plus inventory evidence limitations | Applied because requested source-of-truth set is incomplete |

## Authority Chain Checks

Authority chain status model used here:

- `complete`
- `missing-upstream-plan`
- `missing-current-plan`
- `evidence-without-contract`
- `not-applicable`

Rules:

- evidence artifact presence does not satisfy plan-contract presence
- upstream phase contract and upstream evidence must be tracked separately
- handoff completeness cannot be marked `complete` if any required upstream plan
  is missing

| Topic / Chain node | Required plan contract | Evidence artifact | Status | Why it matters | Repair needed |
| --- | --- | --- | --- | --- | --- |
| `positioning-freeze` | `plan/positioning-freeze/positioning-freeze.plan.md` | frozen doc changes reflected in governance / positioning artifacts | `complete` | This is the only fully readable phase contract in the requested source set | none |
| `platform-coupling-inventory` | `plan/platform-coupling-inventory/platform-coupling-inventory.plan.md` | `docs/migration/platform-coupling-inventory.md` | `missing-upstream-plan` | Inventory evidence exists, but the upstream execution contract is absent, so inherited boundaries and stop conditions cannot be fully verified | add the missing upstream plan contract to the readable source set |
| `skill-authoring-path-transition` | `plan/skill-authoring-path-transition/skill-authoring-path-transition.plan.md` | merged creator / reviewer / template contract changes in the Big Feature Branch | `missing-upstream-plan` | The current phase contract is present, but the inherited upstream inventory plan contract is still missing, so full authority-chain completeness cannot be claimed | add the missing upstream inventory plan contract to the readable source set |
| `platform-coupling-inventory evidence -> downstream use` | upstream plan required separately | `docs/migration/platform-coupling-inventory.md` | `evidence-without-contract` | Evidence cannot replace the upstream phase contract when a later phase inherits dependency handling from inventory work | restore contract + evidence pair |

## Notes

- This checklist was intentionally created only from the readable source-of-truth
  artifacts present in the current worktree.
- Missing requested source-of-truth artifacts were not reconstructed from memory,
  branch history, or other worktrees.
- `skill-authoring-path-transition` is now represented by both its repo-visible
  phase plan and merged contract-surface changes.
- Until the missing upstream inventory plan contract is restored into this
  worktree, runway-wide status remains partially complete rather than fully
  authoritative.
