# Creator examples

## Example 1: split a broad skill

If a draft tries to cover both "create a skill" and "review a skill", split it
into two folders:
- `agent-skill-creator`
- `agent-skill-reviewer`

## Example 2: create a focused skill

Goal:
- draft a skill that rewrites release notes into a short changelog

Result:
```text
.codex/skills/release-note-shortener/
├── SKILL.md
├── examples.md
└── checklist.md
```

Why this passes the creator bar:
- canonical source is still authored under `skills/release-note-shortener/`
- the first copy-pasteable path is the projected `.codex/...` form
- one trigger family
- one primary output
- brief positive and negative examples can live in `SKILL.md`
- local examples live in the same folder
- `checklist.md` has a declared review role
- the output is `review-ready`, not `approved`

## Example 3: high-complexity skill

Goal:
- draft a refactoring skill with multiple decision branches

Result:
```text
.codex/skills/safe-refactor/
├── SKILL.md
├── examples.md
├── checklist.md
└── run-task.sh
```

Why this needs `examples.md`:
- refactoring is high complexity
- brief examples in `SKILL.md` are not enough
- scripts and branching paths need detailed positive and negative cases

## Example 4: use heavier validation only when risk warrants it

Goal:
- draft a release-gating skill that can block or defer repository-visible actions

Result:
```text
.codex/skills/release-gate-checker/
├── SKILL.md
├── examples.md
└── checklist.md
```

Why this heavier shape passes:
- the skill is a gatekeeper with higher downstream impact
- the draft can justify explicit verification or checklist guidance
- the extra validation is proportionate to the risk

## Example 5: keep a lightweight skill lightweight

Goal:
- draft a naming-convention skill with one clear trigger family

Result:
```text
.codex/skills/simple-naming-rule/
├── SKILL.md
└── reference.md
```

Why this stays lightweight:
- the main misuse prevention is already covered by trigger, boundaries, and examples
- adding release-grade checklists or rationalization tables would be unnecessary
- the creator keeps validation proportional instead of copying a heavier pattern

## Example 6: split oversized reference material

Goal:
- draft a skill with several distinct rule clusters and edge-case notes

Result:
```text
.codex/skills/policy-auditor/
├── SKILL.md
├── reference.md
└── references/
    ├── severity-rules.md
    └── exception-cases.md
```

Why this split passes:
- the reference material covers more than 3 logical topics
- each split file has one clear role
- `Local references` can name each file and explain its job

## Example 7: bootstrap fallback is explicit, not the default

Goal:
- draft a skill before any projected entrypoint exists yet

Result:
- author the canonical source under `skills/<skill-name>/`
- show `.codex/skills/<skill-name>/` as the normal output-facing path
- if you must mention the source path operationally, label
  `skills/<skill-name>/` as a bootstrap fallback because the projected
  entrypoint does not yet exist
- do not edit any `.codex/skills/<skill-name>/` compatibility or
  projection surface in the same phase

Why this passes:
- creator keeps `skills/<skill-name>/` limited to canonical source and
  explicitly labeled fallback
- the default copy-pasteable path still points to `.codex/...`
- creator does not assume a concrete platform surface on its own
