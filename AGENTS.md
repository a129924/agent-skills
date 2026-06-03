# agent-skills governance summary

For the full repository role and migration boundary, see
[docs/repo-positioning.md](docs/repo-positioning.md).

## Agent preference

- Respond in Traditional Chinese (繁體中文) by default.

## Governance source

- `AGENTS.md` is the governance canonical source.

## Skill source model

- `skills/` is the current canonical skill source and repository truth.
- `.github/skills/` is a GitHub/Copilot compatibility surface, not a
  repo-wide authority owner or source of truth.
- `.<platform>/skills/` is a compatibility or projection layout for
  platform-specific consumption, not source of truth.

## Topic boundary

- This topic freezes repository positioning only.
- It does not implement skill-path migration, platform directory changes, or
  creator/reviewer/template path transition.
