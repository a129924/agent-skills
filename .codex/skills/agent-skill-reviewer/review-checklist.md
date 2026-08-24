# Reviewer checklist

A skill is `approved` only if all of these are true:

## Required core
- `SKILL.md` exists
- `reference.md` or `examples.md` exists

## Structure
- `SKILL.md` has `name` and `description` frontmatter
- `SKILL.md` frontmatter includes `complexity` field (for new and materially edited skills; see Legacy Skill Policy for unedited legacy skills)
- `SKILL.md` includes `Purpose`
- `SKILL.md` includes `Trigger / When to use`
- `SKILL.md` includes `Inputs`
- `SKILL.md` includes `Process`
- `SKILL.md` includes `Examples`
- `SKILL.md` includes `Outputs`
- `SKILL.md` includes `Boundaries`
- `SKILL.md` includes `Local references`
- local references name local files or folders and state what each one is for
- YAML `use_when` and `do_not_use_when` align with body `Trigger / When to use` (if present)
- YAML `inputs` aligns with body `Inputs` (if present)
- YAML `outputs` lists artifact names only and does not contradict body `Outputs` (if present)
- YAML and body sections do not contradict each other

## Optional additions
- each optional file or folder has a clear local job
- optional additions stay local to the skill
- optional additions are justified by the skill's scope
- optional additions follow the responsibility matrix
- generic catch-all names such as `docs/`, `misc/`, or `helpers/` are rejected
  unless the repository spec gives them a fixed role
- each file inside `references/` has a clear topic and role

## Quality
- the skill has one responsibility
- the trigger is explicit and narrow enough to be useful
- the folder is portable and mostly self-contained
- the skill does not depend on hidden repo-global context
- the skill includes example or reference material in the same folder
- `SKILL.md` includes at least one concise correct example
- `SKILL.md` includes at least one concise incorrect example
- **each SKILL.md example is typically 10–20 lines** (code + explanation combined)
- **Examples section in SKILL.md occupies no more than 10–15% of total SKILL.md length**

## Example depth
- `examples.md` may stay optional when the concise `SKILL.md` examples already cover about 80% of routine usage
- `examples.md` exists when the skill is high complexity
- `examples.md` exists when the concise `SKILL.md` examples are not enough
- detailed examples match the skill's main paths and anti-patterns

## Risk-based validation fit
- validation weight matches the skill's risk, branching, external-tool usage, and
  downstream impact
- lightweight skills are not burdened with heavyweight validation that does not
  improve real misuse prevention
- higher-risk or gatekeeping skills include stronger validation signals or
  equivalent local guidance
- stronger validation may appear as explicit verification guidance, red flags,
  rationalizations, a checklist, or another clearly declared local mechanism
- when ambiguity would materially change the output, the draft tells the agent to
  stop and ask instead of silently guessing

## Reference depth
- `reference.md` stays focused when one file is enough
- `references/` supplements split reference detail and does not replace the required companion-file rule
- split into `references/` when local reference detail grows beyond about 1,000 tokens
- split into `references/` when local reference detail covers more than 3 logical topics
- each split reference file is listed in `Local references` with its role

## High-complexity triggers
- code refactoring
- branching or multi-path decisions
- script or external-tool usage
- higher-risk outputs or larger downstream impact

## Ownership and lifecycle
- creator stops at `review-ready`
- reviewer returns `approved` or `needs-rework`
- reviewer does not produce the final implementation directly

## Topic plan alignment
- locked `Artifact paths` are valid and align with the actual output locations
- repo-visible artifacts are not mixed with session-only or local-only artifacts
- path drift is sent back for plan repair instead of being silently tolerated
- when a topic plan locks creator/reviewer-first rollout, downstream regular skills
  must remain untouched in that topic
- scope drift from a creator/reviewer-first topic into downstream regular-skill
  rollout returns `needs-rework`
- for path-alignment topics, every path mention is classifiable as canonical
  source / authoring-only, output-facing, or explicit bootstrap fallback
- for canonical-source or authoring-only wording in those topics, the draft
  uses `skills/<skill-name>/`
- for output-facing, runnable, or copy-pasteable wording in those topics, the
  draft defaults to `.codex/skills/<skill-name>/`
- for bootstrap fallback in those topics, the draft uses `skills/<skill-name>/`
  only when the projected entrypoint does not yet exist and the text labels the
  path as fallback
- reviewer does not assume any concrete `.codex/skills/` projection path
  unless context or prompt explicitly puts that surface in scope
- hardcoded `.codex/...`, `.github/...`, or another concrete platform root as a
  default path returns `needs-rework`
- downstream planning-spine implications are recorded as follow-up rather than
  treated as blockers unless inventory evidence explicitly classifies them as blockers

## Reviewer independence
- Reviewer is a **separate agent** (SubAgent in VS Code; `/fleet` in CLI)
  - Must not inherit creator's session context or assumptions
  - Must apply checklist objectively
- Reviewer outputs: `approved` or `needs-rework` only
  - Includes explicit reasoning and blocking issues (if `needs-rework`)
- Creator may patch PR after reviewer approves (Phase 7)
  - Direct-apply fixes only (style, typo, meta, formatting)
  - Reviewer does NOT re-check these patches
  - Major changes require reviewer to re-evaluate

## Stable library metadata (if applicable)
When the skill is intended for the stable library, review-checklist.md must verify:
- Topic plan includes `Stable library metadata` section
- README row format is complete and matches repo table schema
- README row positioned correctly (alphabetical order or policy-defined position)
- VERSION bump direction is specified and justified
- VERSION direction aligns with commit semantics (MINOR for new skill, PATCH for correction)
- timing for README / VERSION actions is declared explicitly
- if timing is `release`, the topic plan also declares a release action that will
  execute Phase 10

## Reject signals
- multiple unrelated trigger families
- "do everything" language
- missing required core files
- missing concise positive or negative examples in `SKILL.md`
- missing `examples.md` for a high-complexity skill
- missing stronger validation for a higher-risk or gatekeeping skill
- scope drift into downstream regular-skill rollout when the topic plan locks a
  creator/reviewer-first phase
- `skills/...` used as the default runnable, copy-pasteable, or output-facing
  path
- hardcoded `.codex/...`, `.github/...`, or another concrete platform root used
  as the default without injected context
- fallback wording that mentions `skills/...` without explicitly stating that
  the projected entrypoint does not yet exist
- oversized multi-topic `reference.md` left unsplit
- split reference files missing role labels in `Local references`
- optional additions with no declared role
- vague boundaries
- review comments that would require inventing a different skill
- **Examples section in SKILL.md exceeds 15% of total file length or individual examples exceed 20 lines** (signals over-documentation; defer detailed scenarios to `examples.md`)
- YAML contradicts body sections
- `Validation` present for a medium or high complexity skill but defines no SOFT FAIL or BLOCKED conditions
- high complexity skill missing `Validation` entirely, or medium complexity skill missing `Validation` when ambiguity would materially change output
- `Workflow State Contract` present but missing `status` field
- hard-stop `FAIL → stop` design in Validation for a recoverable gap

## Complexity-gated sections

low:
- `Validation`, `Failure Handling`, `Workflow State Contract` are optional

medium:
- `Validation` present when ambiguity would materially change output (recommended otherwise)
- `Failure Handling` present if ambiguity would materially change output

high:
- `Validation` present and defines both Required and Quality Checks tiers
- `Failure Handling` present with all three categories (Missing Context,
  Ambiguous Requirement, Execution Limitation)
- `Workflow State Contract` present if skill participates in multi-agent handoff

## Complexity and risk profile review

- confirm `complexity` field exists in YAML frontmatter
- confirm `complexity` matches the skill's actual workflow risk, branching, and
  downstream impact
- escalate `low → medium` if the skill has multi-step outputs or downstream dependencies
- escalate `medium → high` if the skill modifies code, creates plans used by
  other agents, or participates in multi-agent handoff
- confirm `risk_profile` tags match actual skill behavior when present
- escalate `complexity` when `risk_profile` tags understate actual behavior
- do not approve a skill if required sections are missing after complexity escalation

## Severity levels

BLOCKER — must fix before approved:
- missing required core files
- missing `Validation` for a high complexity skill
- YAML contradicts body
- `Validation` present but has no SOFT FAIL or BLOCKED conditions
- hard-stop `FAIL → stop` design for a recoverable gap

WARNING — approved with notes:
- `Validation` missing Quality Checks tier for medium or high complexity skill
- `Failure Handling` missing one of the three required categories
- YAML advisory fields missing but body is complete
- `risk_profile` absent for a medium or high complexity skill

INFO — optional improvement:
- `Workflow State Contract` absent for high complexity skill that participates in handoff
- `complexity` field absent on legacy skill not currently under edit

## Verdict rules

- any BLOCKER → `needs-rework`
- WARNING only → `approved` with notes
- INFO only → `approved`

## Legacy Skill Policy

- existing skills without `complexity` are classified as `unclassified`
- do not reject a legacy skill solely for missing `complexity` or `risk_profile`
- require classification when the skill is materially edited
- require classification before the skill is used in multi-agent handoff
- treat missing governance body sections on unedited legacy skills as INFO, not BLOCKER

## Dry Review Report Format

When running a dry review against an existing skill, produce a report in this
format:

```
Target skill:
- path:
- inferred complexity:
- inferred risk_profile:

Verdict:
- approved | needs-rework

Findings:
- BLOCKER:
  - ...
- WARNING:
  - ...
- INFO:
  - ...

Legacy handling:
- Is this a legacy skill without new metadata?
- Should classification be required now or deferred?

Checklist feedback:
- Did the updated checklist create false positives?
- Did the updated checklist miss any obvious risk?
- Should any rule be softened, clarified, or escalated?
```
