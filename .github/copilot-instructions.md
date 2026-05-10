# agent-skills repository instructions

## Agent Preferences

- **Language**: Respond in Traditional Chinese (繁體中文) by default.

This repository is an Agent Skills workbench, not an application codebase or a
Python package.

## Repository goal
- Collect ready-to-use GitHub Agent Skills.
- Create new skills with `agent-skill-creator`.
- Review skills with `agent-skill-reviewer` before treating them as stable.

## Canonical policy owner
This file is the GitHub/Copilot-specific always-on guidance mirror for this
repository.

Governance and repository positioning authority live in `AGENTS.md` and
`docs/repo-positioning.md`.

Ownership model:
- `AGENTS.md` owns governance rules
- `docs/repo-positioning.md` owns current state, target architecture, and
  migration boundary
- `.github/copilot-instructions.md` mirrors that guidance as GitHub/Copilot
  always-on instructions
- `README.md` summarizes it for humans
- `agent-skill-template` mirrors it in reusable form
- `agent-skill-creator` applies it during drafting
- `agent-skill-reviewer` enforces it during review

## Always-on rules
- Focus on GitHub Agent Skills only.
- For governance and positioning questions, follow `AGENTS.md` and
  `docs/repo-positioning.md`.
- During the current transition workflow, store project skills under
  `.github/skills/<skill-name>/`.
- Keep every skill as self-contained and copy-friendly as possible.
- Prefer small, single-purpose skills over broad helper bundles.
- Treat `.github/copilot-instructions.md` as GitHub/Copilot always-on guidance
  and `.github/skills/*/SKILL.md` as task-specific instructions.

## Required skill shape
Each stable skill directory should contain:
- `SKILL.md`
- `examples.md` or `reference.md`
- optional `checklist.md`, scripts, `references/`, or local subfolders only when
  the skill truly needs them

Optional additions are allowed only when their role is explicit and local to the
skill.

## Skill folder responsibility matrix
| Item | Responsibility | Status |
| --- | --- | --- |
| `SKILL.md` | Executable instruction contract for the skill, including concise positive and negative examples | Required |
| `reference.md` | Stable local knowledge, constraints, edge cases, and usage notes | Required or choose `examples.md` |
| `references/` | Split topic-specific reference files when one `reference.md` would become too broad | Optional |
| `examples.md` | Detailed example inputs, outputs, anti-patterns, and usage patterns | Required for high-complexity skills or when `SKILL.md` examples are not enough |
| `checklist.md` | Repeatable verification or operational checklist | Optional |
| scripts | Local automation with one explicit operational job | Optional |
| `assets/` | Static local resources used only by this skill | Optional |
| `templates/` | Reusable local templates used only by this skill | Optional |
| `fixtures/` | Sample local data or payloads used only by this skill | Optional |

Rules for optional items:
- every optional file or folder must map to one clear responsibility
- `Local references` must name the item and say what it is for
- avoid vague catch-all names such as `docs/`, `misc/`, `helpers/`, or `stuff/`
  unless the repository spec later assigns them a fixed role

## Reference policy
- Keep `reference.md` focused when one file is enough.
- `references/` is a split-reference supplement, not by itself a replacement for
  the required companion-file rule.
- If `reference.md` grows beyond about 1,000 tokens or covers more than 3 logical
  topics, split it into topic files under `references/`.
- If `reference.md` is the chosen companion file and becomes too broad, keep it
  focused or reduce it to a short overview while moving detailed topics into
  `references/`.
- When `references/` exists, `SKILL.md` must list each split file in
  `Local references` and state the role of each file.
- Reviewer may still require a split when the file remains too broad even if the
  rough threshold is not exceeded.

Each `SKILL.md` should contain:
- YAML frontmatter with `name` and `description`
- `Purpose`
- `Trigger / When to use`
- `Inputs`
- `Process`
- `Examples`
- `Outputs`
- `Boundaries`
- `Local references`

In `Local references`, name local files or folders and state what each one is for.

## Example policy
- Every `SKILL.md` must include at least one concise correct example and one
  concise incorrect example.
- `examples.md` may stay optional when the concise `SKILL.md` examples already
  cover about 80% of routine usage.
- `examples.md` is required when the skill:
  - handles code refactoring
  - has branching or multi-path decisions
  - depends on scripts or external tools
  - produces higher-risk outputs or larger downstream impact
- Reviewer may still require `examples.md` when the `SKILL.md` examples are not
  enough.

## Risk-based validation policy
- Validation weight should match the skill's risk, branching, external-tool usage,
  and downstream impact.
- Lightweight skills may stay concise when `Trigger / When to use`,
  `Boundaries`, and brief positive / negative examples already prevent routine misuse.
- Medium-complexity skills should make their main decision path explicit and may
  add brief verification guidance when needed.
- Higher-risk or gatekeeping skills should include stronger validation signals or
  equivalent local guidance, such as explicit verification, red flags,
  rationalizations, or a checklist.
- Stronger validation is optional-by-need, not a new mandatory top-level shape for
  every skill.
- Reviewer may require stronger validation when the skill controls review,
  release, external tools, or other higher-impact flows.

## Quality bar
A skill is only complete when it is:
- single responsibility
- portable
- independent
- explicit about when it should be triggered
- backed by example or reference material in the same folder
- approved by `agent-skill-reviewer`

## Ownership boundaries
- `agent-skill-creator` may draft or revise a skill until it is `review-ready`.
- `agent-skill-reviewer` may return `approved` or `needs-rework`.
- Creator may not approve its own output.
- Reviewer may not author the final implementation directly.
- A human or external workflow owns the handoff between creator and reviewer.

## Naming
- Directory name: lowercase kebab-case
- Skill name in frontmatter: match the directory when possible
- Avoid vague names such as `general-helper` or `do-everything`

## Working style
- Put reusable detail next to the skill that uses it, not in repo-global
  helper files.
- If a new skill overlaps an existing one, narrow or split scope instead of
  broadening the old skill.
- Do not accept a skill into the stable library until the reviewer flow passes.

## Implementation handoff contracts
- When preparing a prompt for another implementation agent, do not rely on chat
  memory alone. Name the repo-visible source-of-truth artifacts explicitly
  (for example `analysis/<topic>/requirements.md`,
  `analysis/<topic>/technical-spec.md`, and `plan/<topic>/<topic>.plan.md`).
- When work is expected to happen in a worktree, include the exact worktree path,
  current branch, intended feature branch, PR target branch, and the allowed file
  paths to modify. Do not let an implementer infer these from context.
- Re-state locked decisions, artifact paths, and stop conditions in the
  implementation prompt so planner intent and implementer execution do not drift.
- If implementer output conflicts with the frozen plan or analysis artifacts,
  stop and surface the drift explicitly instead of silently reconciling it.

## Subagent Role Enforcement
When working through the skill lifecycle (creator → reviewer → stable library),
use independent `/fleet` subagents instead of self-performing these roles:
- **Never self-perform creator work** — always use `/fleet @.github/skills/agent-skill-creator/`
  to draft new skills or modifications, even if you're technically capable
- **Never self-perform reviewer work** — always use `/fleet @.github/skills/agent-skill-reviewer/`
  for independent verdicts; the main agent cannot grade its own output
- **Why this matters** — role separation prevents blind spots, ensures honest
  feedback, and maintains the integrity of the approval workflow
- When launching subagents, verify they appear in `/tasks` before continuing; if
  not visible, you have not correctly delegated
- Loading a skill, paraphrasing what reviewer or creator would do, or claiming a
  role was delegated is not enough. The creator and reviewer must each exist as
  visible `/fleet` subagents before work continues.

## STOP POINT 2 Resume Routing
After manual merge handoff (STOP POINT 2), route post-merge cleanup and local
sync through `git-post-merge-workflow`.

Use `.github/skills/git-post-merge-workflow/references/stop-point-2-checklist.md`
as the portable resume checklist for merge confirmation, local sync entry
conditions, and branch cleanup checks.

## Topic Planning with Analysis Layer
The repository now supports an optional **analysis layer** before plan creation,
enabling stronger requirement discipline through two pre-plan artifacts:

### When to use the analysis layer
- You have fuzzy or conflicting requirements that need clarification before
  planning begins
- The topic involves multiple stakeholders or complex business logic that would
  benefit from a frozen baseline
- You want `plan-creator` to operate in strict-mode validation (100% mapping
  between technical-spec and final plan)
- The topic is a new workflow, agent, or skill that has not been implemented yet
  and another agent may be asked to execute it later
- You intend to switch the main agent into an observer / orchestrator role after
  planning and need repo-visible artifacts for downstream handoff

### The analysis layer structure
Create these optional files **before** running `plan-creator`:
- `analysis/<topic>/requirements.md` — frozen requirement baseline from
  `business-intent-alignment` (or manually authored and locked)
- `analysis/<topic>/technical-spec.md` — technical translation and feasibility
  assessment from `business-to-technical-translation`

### How plan-creator consumes the analysis layer
- **Strict mode** (both files present): `plan-creator` validates that all scope,
  artifact paths, and implementation steps in the final plan map 100% to the
  technical-spec; no self-healing or gap-filling allowed
- **Soft mode** (one or both files missing): `plan-creator` can proceed but must
  emit an explicit semantic warning before output, e.g., "偵測到前置分析缺失，
  計畫可能存在語意漂移風險"
- **Authority rule**: analysis-layer content always outranks conversation-time
  instructions unless you explicitly say `override <file>`; when conflict
  detected and no override given, `plan-creator` must flag the conflict and
  halt rather than silently merging inputs

### Skills that support this layer
- `business-intent-alignment` — Socratic interviewer perspective; produces
  measurable, contradiction-free requirement baseline
- `business-to-technical-translation` — pessimist implementer perspective;
  produces feasibility checks, cost-of-realization warnings, and rollback triggers

## Step-tracking gate semantics
- If a workflow gate is deciding whether implementation work is complete, it must
  evaluate only `## Implementation Steps` in `plan/<topic>/<topic>.step.md`.
- Do not treat `## Workflow Stages` markers as implementation-completion signals
  for review gates; those stages include future phases and can create false
  blocking states.
- When changing step-gate semantics, update the parser / script contract and the
  corresponding tests together. Do not change only agent prose or plan wording.

## Worktree execution preflight
- Before implementation starts in a worktree, ensure the worktree is attached to
  a PR-capable feature branch. Do not begin implementation on `dev`, on a base
  branch, or on detached HEAD when the task is expected to end in a PR.
- State the base branch, feature branch, and PR target branch explicitly in the
  prompt or handoff contract. If branch setup is missing, stop and create or
  switch to the correct feature branch before continuing.
