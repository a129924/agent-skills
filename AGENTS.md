# agent-skills governance summary

For the full repository role and migration boundary, see
[docs/repo-positioning.md](docs/repo-positioning.md).

## Agent preference

- Respond in Traditional Chinese (繁體中文) by default.

## Governance source

- `AGENTS.md` is the governance canonical source.

## Skill source model

- `skills/` is the intended canonical skill source and target architecture.
- `.github/skills/` remains the current Copilot active authored and reviewed
  workflow path during transition.
- `.<platform>/skills/` is a future adapter or projection layout, not source of
  truth.

## Topic boundary

- This topic freezes repository positioning only.
- It does not implement skill-path migration, platform directory changes, or
  creator/reviewer/template path transition.
