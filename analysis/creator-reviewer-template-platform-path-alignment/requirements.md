# Requirements: creator-reviewer-template-platform-path-alignment

## Status

- **Status**: `FROZEN`
- **Topic**: `creator-reviewer-template-platform-path-alignment`
- **Date**: 2026-06-17
- **Scope**: analysis baseline for creator / reviewer / template path-language alignment only

## Problem Statement

`skills/agent-skill-creator/**`, `skills/agent-skill-reviewer/**`, and
`skills/agent-skill-template/**` still contain transition-era wording that
defaults many copy-pasteable or runnable path examples to `skills/...`.

This now conflicts with the frozen repository intent for this topic:

1. canonical source remains `skills/`
2. projection / compatibility surfaces remain `.<platform>/**`
3. output-facing, runnable, and copy-pasteable paths should default to
   `.<platform>/...`
4. `skills/...` is allowed only for source-model or authoring-only context
5. bootstrap fallback is allowed only when the projected entrypoint does not
   yet exist, and the fallback must be labeled explicitly

The missing outcome is a bounded baseline that lets these three skills describe
path semantics consistently without reopening downstream regular-skill rollout,
platform rematerialization, or broader runtime/install/sync behavior.

## Evidence Read

The baseline uses the following repo-visible evidence:

- `AGENTS.md`
- `.github/prompts/create-analysis.prompt.md`
- `analysis/platform-projection-adapter/requirements.md`
- `analysis/platform-projection-adapter/technical-spec.md`
- `analysis/skills-canonical-positioning/requirements.md`
- `analysis/skills-canonical-positioning/technical-spec.md`
- `skills/agent-skill-creator/SKILL.md`
- `skills/agent-skill-creator/blueprint.md`
- `skills/agent-skill-creator/folder-contract.md`
- `skills/agent-skill-creator/examples.md`
- `skills/agent-skill-reviewer/SKILL.md`
- `skills/agent-skill-reviewer/review-checklist.md`
- `skills/agent-skill-reviewer/examples.md`
- `skills/agent-skill-template/SKILL.md`
- `skills/agent-skill-template/template.md`
- `skills/agent-skill-template/folder-contract.md`
- `skills/agent-skill-template/reference.md`

## Actors

| Actor | Role | What must be true after this topic |
| --- | --- | --- |
| Skill author | Uses creator/template guidance to draft a new skill | Can distinguish source-of-truth wording from the path they should copy, run, or hand to a platform consumer |
| Skill reviewer | Uses reviewer guidance to evaluate a draft or projected artifact | Can reject source/output/fallback conflation without inventing new path semantics |
| Platform consumer | Reads a path example or command from these skills | Sees `.<platform>/...` as the default output-facing path unless an explicit fallback condition is stated |
| Planning actor | Prepares later implementation scope | Can keep changes inside the three skill families and their necessary local reference files |

## Frozen Requirements

| ID | Requirement | Acceptance signal |
| --- | --- | --- |
| R1 | When these three skill families describe canonical source ownership or authoring-only location, they must use `skills/...` wording and keep it clearly limited to source-model or authoring-only context. | A reader can point to every `skills/...` path in scope and classify it as source-model, authoring-only, or explicit fallback rather than as the default runnable/copy-pasteable path. |
| R2 | When these three skill families provide output-facing, runnable, or copy-pasteable paths, commands, folder shapes, or handoff examples, they must default to the placeholder projection form `.<platform>/...` rather than bare `skills/...`. | Another reader can scan all in-scope copy-pasteable examples and find `.<platform>/...` as the default path surface instead of `skills/...`. |
| R3 | The topic must not silently choose a concrete platform root such as `.codex/...` or `.github/...` as the new default. If a consumer requires a concrete platform path to keep the contract usable, that must trigger rollback to alignment rather than a hardcoded default. | No in-scope guidance promotes a concrete platform root as the default. Any discovered requirement for `.codex/...` or another concrete platform root is recorded as a rollback trigger or blocker. |
| R4 | Bootstrap use of `skills/...` is allowed only when the projected entrypoint does not yet exist, and the text must label that path as a fallback rather than as the normal path. | Every allowed `skills/...` bootstrap instruction names the missing projected entrypoint condition and includes explicit fallback language. |
| R5 | Reviewer-facing rules must enforce the distinction between source-model wording, output-facing projection wording, and explicit bootstrap fallback wording. | Reviewer process/checklist/examples give a reviewer a repeatable way to mark misaligned path language as `needs-rework` without treating downstream projection surfaces as canonical. |
| R6 | This topic's editable scope is limited to `skills/agent-skill-creator/**`, `skills/agent-skill-reviewer/**`, `skills/agent-skill-template/**`, and only the local reference files in those folders that carry affected path semantics. | Future implementation artifacts name only those scoped files as editable and treat downstream regular skills, `.codex/**`, `.github/**`, and rematerialization work as forbidden scope. |
| R7 | The aligned wording must remain compatible with the `platform-projection-adapter` contract: `skills/` stays canonical source, platform-facing surfaces stay projection-only, placeholder projection paths stay generic, and fallback wording must not imply platform rematerialization. | Technical translation can map every requirement without changing `analysis/platform-projection-adapter/*` assumptions. If a proposed wording would contradict that contract, the topic rolls back to alignment instead of forcing implementation. |

## Resolved Contradictions

### C1 - Canonical source versus output default

- Conflict: repository governance keeps `skills/` as canonical source, but this
  topic requires output-facing paths to default to `.<platform>/...`.
- Resolution: freeze a three-way distinction:
  - `skills/...` for source-model or authoring-only context
  - `.<platform>/...` for output-facing / runnable / copy-pasteable context
  - `skills/...` again only for explicitly labeled bootstrap fallback

### C2 - Generic platform placeholder versus concrete platform convenience

- Conflict: a concrete example such as `.codex/...` may feel more convenient,
  but the frozen input forbids silently choosing one platform default.
- Resolution: keep the default generic as `.<platform>/...`; if a real consumer
  cannot proceed without a concrete platform root, route back to alignment.

### C3 - Fallback allowance versus source-path re-promotion

- Conflict: allowing bootstrap fallback could accidentally re-promote
  `skills/...` as the ordinary operational path.
- Resolution: fallback is legal only when the projected entrypoint is missing
  and only when the text labels it as fallback.

## Explicit Assumptions

- A1: This topic is analysis-only and does not itself edit any source skill.
- A2: The three scoped skill families are the only in-scope authority surfaces
  for this topic; downstream regular skills remain follow-up work.
- A3: Platform consumers can understand or later substitute the generic
  `.<platform>/...` placeholder without this topic naming a concrete root.
- A4: `analysis/platform-projection-adapter/*` remains the controlling contract
  for projection semantics and is not reopened here.

## Extreme-Boundary Checks

| Boundary | Requirement result |
| --- | --- |
| The projected entrypoint does not yet exist | The skill may mention `skills/...` only as an explicitly labeled bootstrap fallback; it must not become the new default path |
| A reviewer sees a draft that uses `.codex/...` without context injecting that concrete root | The reviewer must treat that as a rollback-to-alignment signal or `needs-rework`, not as an acceptable default |
| A reader opens only one of the scoped files and copies the first visible path | The first copy-pasteable path must point to `.<platform>/...` unless it is explicitly labeled fallback |
| Only a subset of creator/reviewer/template files get aligned in implementation | Remaining out-of-scope or unchanged files must not be used to justify widening this topic into downstream regular-skill rollout |
| A future consumer asks for rematerializing `.codex/**` or `.github/**` to make the wording true | That request is out of scope for this topic and must roll back to alignment instead of broadening implementation |

## Success Signals

This topic is frozen successfully when:

1. source-model, output-facing, and fallback path semantics are distinct and
   testable,
2. `skills/...` is no longer the default copy-pasteable or runnable path in the
   three scoped skill families,
3. no concrete platform root becomes the default by convenience, and
4. future implementation can stay inside the three scoped skill families and
   their necessary local reference files without reopening projection tooling or
   downstream skill rollout.

## Blocker Status

No blocker from the current evidence set. The frozen inputs are specific enough
to proceed to technical translation.
