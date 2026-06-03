# agent-skills governance summary

For the full repository role and migration boundary, see
[docs/repo-positioning.md](docs/repo-positioning.md).

## Agent preference

- Respond in Traditional Chinese (繁體中文) by default.

## Governance source

- `AGENTS.md` is the governance canonical source.

## Workflow agent source model

- `agents/` is the canonical source for repo-defined workflow agent artifacts.
- `agents/observer-dispatcher.agent.md` is a bounded routing-only workflow
  agent artifact. It does not authorize broader agent taxonomy, registry
  behavior, workflow-to-agent binding, or runtime orchestration semantics.

## Skill source model

- `skills/` is the primary canonical skill source and repository truth for
  reusable skill behavior.
- `.github/skills/` is a GitHub/Copilot compatibility surface, not a
  repo-wide authority owner or source of truth.
- `.codex/skills/` is a repository-policy projection / compatibility surface,
  not source of truth.
- `.<platform>/skills/` is a compatibility or projection layout for
  platform-specific consumption, not source of truth.

## Platform surface model

- `.github/**`, `.codex/**`, and other `.<platform>/**` paths are projection or
  compatibility surfaces only.
- Those paths do not become canonical just because a specific tool or workflow
  consumes them.

## Topic boundary

- This topic freezes repository positioning and the bounded Observer /
  Dispatcher baseline only.
- It does not implement skill-path migration, platform directory changes,
  creator/reviewer/template path transition, workflow-to-agent binding, or
  runtime orchestration semantics.
