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
.github/skills/release-note-shortener/
├── SKILL.md
├── examples.md
└── checklist.md
```

Why this passes the creator bar:
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
.github/skills/safe-refactor/
├── SKILL.md
├── examples.md
├── checklist.md
└── run-task.sh
```

Why this needs `examples.md`:
- refactoring is high complexity
- brief examples in `SKILL.md` are not enough
- scripts and branching paths need detailed positive and negative cases
