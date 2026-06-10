# Creator blueprint

Use this as the default folder shape for a `review-ready` skill.

```text
skills/<skill-name>/
├── SKILL.md
├── reference.md            # required unless examples.md already covers local detail
├── references/             # optional, for split topic-specific reference files
├── examples.md            # required for high-complexity or clearly higher-risk skills
├── checklist.md           # optional, useful for repeatable higher-risk validation
├── run-task.sh            # optional
└── assets/                # optional
```

- Use `reference.md` or `examples.md` as the required companion file.
- Use `references/` only as a split-reference supplement, not as a replacement
  for the required companion file.
- Add `references/` when one `reference.md` would exceed about 1,000 tokens or
  more than 3 logical topics.
- Add `examples.md` when the skill is high complexity or the `SKILL.md`
  examples are not enough.
- Add stronger validation guidance only when the skill's risk warrants it.

## YAML Usage Policy

```markdown
# Only name and description are treated as portable runtime discovery fields.
# All remaining fields are repository governance metadata.
name: <skill-name>
description: <what the skill does and when to use it>

# Repository governance metadata — not guaranteed runtime routing fields.
complexity: low | medium | high

risk_profile:
  - ambiguity_sensitive       # missing/ambiguous input may change output meaningfully
  - multi_agent_handoff       # output consumed by another agent or workflow step
  - destructive_action        # may delete, overwrite, migrate, or irreversibly change
  - external_tooling          # calls CLI tools, APIs, networked services, package managers
  - code_modification         # directly edits source code, tests, configuration, or artifacts

inputs:
  - <input-1>

outputs:
  - <artifact-1>

use_when:
  - <trigger scenario>

do_not_use_when:
  - <exclusion scenario>
```

- `name` and `description` drive skill discovery; keep them precise.
- `complexity`, `risk_profile`, `inputs`, `outputs`, `use_when`, and
  `do_not_use_when` are governance metadata — must align with the body but are
  not enforced at the platform level.
- YAML and body must not contradict each other; contradiction is a reject signal.
- List only the applicable `risk_profile` tags; omit the others.

## Minimum `SKILL.md` shape

```md
---
name: <skill-name>
description: <what the skill does and when to use it>
complexity: low | medium | high
---

# Purpose
<one clear job>

# Trigger / When to use
Use this skill when:
- ...

Do not use this skill when:
- ...

# Inputs
- ...

# Process
1. ...
2. ...
3. ...

# Examples
- Positive: ...
- Negative: ...

# Outputs
- ...

# Validation
<!-- Required for complexity: high. Recommended for complexity: medium. -->

## Required Checks
- <hard condition that must be true>

## Quality Checks (best effort)
- <soft condition — improves output but not blocking>

## On Soft Fail
- mark status as INCOMPLETE
- continue with best-effort output
- list missing information explicitly

# Failure Handling
<!-- Required for complexity: high. Required for complexity: medium when ambiguity
     would materially change output. -->

## Missing Context
- mark output as INCOMPLETE
- list required additional inputs explicitly

## Ambiguous Requirement
- if blocking: stop and ask the user before proceeding
- if non-blocking: proceed with stated assumptions, list them explicitly

## Execution Limitation
- state the limitation explicitly in output
- do not fabricate data to fill gaps

# Workflow State Contract (Optional)
<!-- Recommended for complexity: high when participating in multi-agent handoff. -->

When participating in multi-agent workflows, include:
- current_step: <step name from Process>
- next_step: <next step or DONE>
- status: IN_PROGRESS | COMPLETE | INCOMPLETE | BLOCKED

Omit this section if the skill is not part of a multi-agent handoff workflow.

# Verification
- ...                       <!-- optional for higher-risk or easier-to-misuse skills -->

# Red Flags
- ...                       <!-- optional for higher-risk skills -->

# Common Rationalizations
- ...                       <!-- optional for higher-risk skills -->

# Boundaries
- ...

# Local references
- `reference.md`: stable constraints, notes, or edge cases
- `references/decision-rules.md`: topic-specific reference file when reference content is split
- `examples.md`: detailed patterns and anti-patterns for complex tasks
- `checklist.md`: repeatable verification steps (optional)
- `assets/`: local-only material used by this skill (optional)
```

## Creation rules
- Use lowercase kebab-case for `<skill-name>`.
- Treat `skills/<skill-name>/` as the canonical authoring target for transition
  work; do not treat any `.<platform>/skills/` compatibility/projection surface
  or promotion as part of this blueprint.
- If responsibility, trigger, or boundaries are ambiguous, ask before drafting.
- Classify validation weight before drafting: lightweight, medium-complexity, or higher-risk.
- Propose `complexity` in YAML frontmatter for every new skill.
- Propose `risk_profile` tags for medium and high complexity skills.
- Keep the skill single-purpose.
- Apply YAML Usage Policy: `name` and `description` are runtime discovery fields;
  remaining fields are governance metadata that must align with the body.
- Keep supporting material in the same folder.
- Split oversized reference material into `references/` by topic.
- If `reference.md` is the chosen companion file and becomes too broad, keep it
  focused or reduce it to a short overview while moving detailed topics into
  `references/`.
- Put concise positive and negative examples in `SKILL.md`.
- Add `examples.md` when the skill is high complexity or the brief examples are not enough for about 80% of routine usage.
- Add `Validation` for medium complexity skills when ambiguity would materially change output (recommended otherwise); require it for high complexity skills.
- Add `Failure Handling` when ambiguity would materially change output.
- Add `Workflow State Contract` only when the skill joins multi-agent handoff.
- Do not write hard `FAIL → stop` conditions; use SOFT FAIL or BLOCKED instead.
- Add stronger validation signals only when risk, branching, tooling, or downstream impact justify them.
- Add optional files or folders only when each one has a clear role.
- Stop at `review-ready`.
- Tell the user when the draft is `review-ready`, then let a human or external workflow send it to `agent-skill-reviewer`.
