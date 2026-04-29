# copilot-instructions-init implementation plan

## Goal / Outcome

Produce a stable Agent Skill that generates or refreshes a target project's
`.github/copilot-instructions.md` from current project facts instead of generic
intent-only prose.

When complete, this topic should provide a repo-visible skill that:

- treats `.github/copilot-instructions.md` generation and update as one single
  responsibility
- derives target-project instructions from sensed facts, installed skills, and
  plan contracts in that priority order
- hard-blocks when facts are stale, missing, or in conflict with human intent
- forbids silent merge of materially different existing instructions
- supports both greenfield follow-up generation and retrofit follow-up refresh
  without taking ownership of those topics themselves

## Scope

- **In scope**:
  - creating `.github/skills/copilot-instructions-init/` as a new stable skill
  - documenting the target-project generation/update contract for exactly one
    file: `.github/copilot-instructions.md`
  - documenting input priority across sensed facts, installed skills, plan
    artifacts, and human intent
  - documenting hard-stop behavior for stale facts, missing facts, intent/fact
    conflicts, and unsupported referenced tools or skills
  - documenting materially-different detection using managed versus non-managed
    instruction blocks
  - documenting greenfield placeholder handoff and retrofit follow-up behavior
  - publishing the new stable skill into `README.md` and `VERSION`

- **Out of scope**:
  - modifying this repository's own `.github/copilot-instructions.md`
  - implementing or changing `sense_env.py`
  - changing `python-project-init-greenfield` or `python-project-retrofit`
    behavior in this topic
  - generating target-project business logic, CI, infrastructure, or README
    content outside `.github/copilot-instructions.md`
  - auto-merging existing target-project instructions with generated content
  - adding a downgrade path that emits a generic placeholder when required facts
    are missing

## Locked Decisions

### Topic identity and stable-library timing

- This is a **stable-library-affecting topic with declared timing**.
- The skill itself is created in the topic branch and reviewed normally.
- Stable-library promotion for `README.md`, `VERSION`, and tagging happens at
  **release**, not during creator drafting.

### Single responsibility

- `copilot-instructions-init` is the target project's "brain maintainer".
- It may both **generate** and **update** a target project's
  `.github/copilot-instructions.md`.
- Its scope stays limited to that single target-project file; it does not take
  ownership of adjacent files such as README, blueprint contracts, or retrofit
  plans.

### Input priority

- Generation/update priority is:
  1. **Sensed facts**
  2. **Installed skills**
  3. **Plan / blueprint / retrofit contract**
  4. **Human intent description**
- The skill must not write instructions that assume tools, layouts, or skills
  that are not supported by the current sensed state.

### Human double-check gate

- If human intent conflicts with current sensed facts, the skill must stop and
  ask which source should govern the next step.
- Example conflicts include:
  - human says Poetry while sensed facts show uv
  - human says no instructions file exists while the file is present
  - human requests a skill or command that is not installed or available

### Overwrite policy

- If the target project already contains a materially different
  `.github/copilot-instructions.md`, the skill must stop and ask.
- Silent merge is forbidden.
- The skill should present a concrete diff-oriented choice set:
  - full overwrite
  - keep current content
  - manual merge by the human

### Greenfield relationship

- `python-project-init-greenfield` only creates a placeholder
  `.github/copilot-instructions.md`.
- Formal instructions generation happens only after facts are available.
- The intended pipeline is: scaffold first, sense first, then generate the real
  instructions.

### Retrofit relationship

- `python-project-retrofit` does not generate instructions itself.
- After retrofit, `copilot-instructions-init` is the standard follow-up topic
  for refreshing the target project's instructions.
- Retrofit sensing delta is a valid high-priority input for the update path.

### Output contract

- The target-project output is always `.github/copilot-instructions.md`.
- Generated content must include these fixed sections:
  - `## Project Truth`
  - `## Governance`
  - `## Implementation Rules`
- The result must be usable instructions content, not a second placeholder.

### Safety and stale-fact rules

- Missing required facts is a **hard block**.
- Required fact categories include at least:
  - toolchain
  - installed skills
  - project structure / entrypoints
- Facts are stale if any fingerprint changed since the last sensing snapshot:
  1. Git `HEAD`
  2. `pyproject.toml` / `uv.lock`
  3. `.github/skills/` summary
- When facts are stale, the skill must instruct the operator to re-run sensing
  before generation/update continues.

### Materially different detection

- Material difference uses the **Non-Managed Blocks Modification** rule.
- Agent-managed blocks are marked with Markdown comments such as:
  - `<!-- START AGENT BLOCK -->`
  - `<!-- END AGENT BLOCK -->`
- If non-managed content outside those blocks is non-empty, or core rules have
  been manually changed, the file is materially different and requires explicit
  human direction.

### Consistency-check policy

- **Greenfield / first generation**: no extra re-sensing after write; sensing is
  already the prerequisite.
- **Update / retrofit refresh**: run a post-write semantic consistency check
  against current manifest/facts.
- The current locked direction is a static consistency check, not a full
  acceptance rerun.

## Boundaries / Exclusions

- The planning actor defines the topic contract only; it does not draft the
  final skill folder here.
- Creator work must stay inside `.github/skills/copilot-instructions-init/`
  plus declared stable-library release surfaces.
- Reviewer evaluates the draft independently and must not author the final
  implementation directly.
- Main Agent owns branch prep, planner alignment, PR flow, post-merge sync, and
  release/version actions.
- This topic must not redefine this repository's own canonical
  `.github/copilot-instructions.md`; that file remains repo policy, not target
  project output.
- This topic must not absorb greenfield scaffolding, retrofit restructuring, or
  sensing-script implementation into one blended skill.

## Status / Allowed Transitions

- **Current**: `approved`
- **Execution model**: follow the canonical creator -> reviewer -> publish ->
  merge -> release path for a stable-library-affecting topic
- **Allowed transitions**:
  - `planned` -> `creator-in-progress`
  - `creator-in-progress` -> `review-ready`
  - `review-ready` -> `reviewer-in-progress`
  - `reviewer-in-progress` -> `approved`
  - `reviewer-in-progress` -> `needs-rework`
  - `needs-rework` -> `creator-in-progress`
  - `approved` -> `creator-in-progress`
  - `approved` -> `publish-in-progress`
  - `publish-in-progress` -> `pr-open`
  - `publish-in-progress` -> `merged`
  - `pr-open` -> `needs-rework`
  - `pr-open` -> `merged`
  - `merged` -> `released`
  - `released` -> terminal

Routing notes:

- This topic uses the standard Phase 4.5 planner-alignment checkpoint after
  reviewer approval.
- Because this topic declares a stable-library release action, Main Agent must
  not treat `merged` as terminal.

## Artifact Paths

| Artifact | Path | Owner | Role |
| --- | --- | --- | --- |
| Topic plan | `plan/copilot-instructions-init/copilot-instructions-init.plan.md` | Planning actor | Repo-visible execution contract for this topic |
| Skill root | `.github/skills/copilot-instructions-init/` | Creator | Root output location for the skill draft |
| Core skill contract | `.github/skills/copilot-instructions-init/SKILL.md` | Creator | Executable instructions contract for generation/update behavior |
| Detailed examples | `.github/skills/copilot-instructions-init/examples.md` | Creator | Branching scenarios for greenfield, update, retrofit, stale facts, and overwrite conflicts |
| Instruction layering reference | `.github/skills/copilot-instructions-init/references/instruction-layering.md` | Creator | Defines the target instruction sections and the boundary between facts, governance, and implementation rules |
| Merge/conflict reference | `.github/skills/copilot-instructions-init/references/merge-and-conflict-policy.md` | Creator | Defines overwrite policy, managed-block behavior, and materially-different stop rules |
| Input-priority reference | `.github/skills/copilot-instructions-init/references/input-sources-and-priority.md` | Creator | Defines fact-first input ordering, stale checks, and required-fact categories |
| Review checklist | `.github/skills/copilot-instructions-init/checklist.md` | Creator | Higher-risk validation checklist for this hard-stop / conflict-handling skill |
| Stable library summary | `README.md` | Main Agent | Add the stable-library row for `copilot-instructions-init` during release |
| Repo version baseline | `VERSION` | Main Agent | Apply the stable-skill SemVer minor bump during release |

Artifact path notes:

- This topic does **not** modify this repository's own
  `.github/copilot-instructions.md`.
- The listed paths are an executable contract; if creator or release work
  drifts outside them, route back to planning/creator alignment before
  continuing.
- Target-project `.github/copilot-instructions.md` is the subject of the skill,
  not a repo artifact created in this repository.

## Stable library metadata

- `README row`: insert this exact table row under `## Current skills`, immediately after `| \`agent-skill-template\` | provides the canonical template and reference shape |` and before `| \`git-branch-naming\` | names or repairs development branches with semantic prefixes and migration guidance |`:
  `| \`copilot-instructions-init\` | generates or refreshes target-project \`.github/copilot-instructions.md\` from sensed facts, installed skills, and plan contracts, with hard stops for stale facts, missing facts, and materially different existing instructions |`
- `VERSION bump`: `0.25.0` -> `0.26.0` (MINOR)
- `timing`: `release`
- `rationale`: this topic adds a new stable skill to the library, but the
  repository's recent stable-skill workflow performs README/VERSION/tag
  promotion in post-merge release handling rather than inside creator drafting
- `release-note expectations`: create and push tag `v0.26.0` after merge once
  post-merge release conditions are satisfied

## Implementation Steps

1. Create `.github/skills/copilot-instructions-init/SKILL.md`.
   - Define generate/update triggers
   - Define fixed input priority
   - Define the hard-stop behavior for stale facts, missing facts, and
     human-intent conflicts
   - Include concise positive and negative examples directly in `SKILL.md`

2. Create `examples.md` for the higher-risk branching paths.
   - Greenfield placeholder -> sensed-facts generation
   - Retrofit follow-up refresh after structure changes
   - Human/toolchain conflict requiring double-check
   - Stale-facts block
   - Materially different existing instructions block
   - Missing-facts hard block

3. Create `references/instruction-layering.md`.
   - Explain required instruction sections
   - Explain how facts become project truth
   - Explain how installed skills become governance rules
   - Explain what belongs in implementation rules and what does not

4. Create `references/merge-and-conflict-policy.md`.
   - Define managed versus non-managed blocks
   - Define overwrite choice set
   - Define materially-different detection
   - Define when the skill must stop and ask instead of merge

5. Create `references/input-sources-and-priority.md`.
   - Define the fact-first ordering
   - Define required-fact categories
   - Define the three-layer stale fingerprint check
   - Define update-mode consistency checking

6. Create `checklist.md`.
   - Include reviewer-facing checks for hard stops, overwrite policy,
     stale-fact detection, and target-project output shape

7. Keep implementation inside the declared skill folder only.
   - Do not revise greenfield, retrofit, or the repo's own
     `.github/copilot-instructions.md` in this topic

## Validation / Acceptance Checks

- Confirm all required topic-plan sections are present and canonical.
- Confirm artifact paths are exact and bounded.
- Confirm the skill keeps one clear responsibility: generate/update only the
  target-project `.github/copilot-instructions.md`.
- Confirm `SKILL.md` includes concise positive and negative examples.
- Confirm `examples.md` covers greenfield, retrofit, stale facts, materially
  different existing content, missing facts, and human/fact conflict.
- Confirm references explicitly declare roles in `Local references`.
- Confirm the fact-priority rule is explicit and not diluted by human-intent
  fallback.
- Confirm missing-facts behavior is a hard block, not a generic-template
  downgrade.
- Confirm stale detection uses the three declared fingerprints.
- Confirm overwrite policy forbids silent merge of materially different content.
- Confirm update mode includes a post-write consistency check while greenfield
  first generation does not require an extra re-sensing pass.
- Confirm stable-library metadata matches the declared release action for
  `README.md`, `VERSION`, and tag creation.

## Reviewer Handoff

```json
{
  "verdict": "approved|needs-rework",
  "blocking_issues": [],
  "copilot_feedback_triage": {
    "ADDRESS": [],
    "DISCUSS": [],
    "SKIP": []
  }
}
```

## Post-merge / release actions

- After merge, STOP POINT 2 applies until an explicit human resume message
  confirms merge completion and asks to continue.
- On valid post-merge resume, Main Agent performs release handling:
  - synchronize local branch state
  - update `README.md` with the stable-skill row for
    `copilot-instructions-init`
  - update `VERSION` from `0.25.0` to `0.26.0`
  - create and push tag `v0.26.0`
- When those release actions complete, transition the topic from `merged` to
  `released`.

## Open Questions / Unresolved Items

- None. The topic's blocking planning decisions are locked.
