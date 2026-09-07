---
name: git-release-management
description: "Assess draft-PR, merge, or release readiness using endpoint-specific gates; tagging needs release authorization."
complexity: high
risk_profile:
  - destructive_action
  - ambiguity_sensitive
  - external_tooling
inputs:
  - target branch, PR, tag, or release version
  - current workspace state including whether uncommitted changes exist
  - project version sources such as pyproject.toml, __version__.py, or package.json
  - pass/fail signals from testing, strict typing, lint, CI, reviewer approval, and documentation updates
  - whether the change includes API or contract changes that require synced documentation
  - whether an emergency marker and human confirmation exist
outputs:
  - release decision — blocked, ready for PR, ready to tag, or emergency-path pending human confirmation
  - normal-path or emergency-path gate result with explicit failed-gate diagnostics
  - repair guidance for each failed gate condition
  - safe PR or tagging commands when all gates are satisfied
  - version-bump guidance based on commit semantics
use_when:
  - preparing a PR gate, release, tag, or hotfix
  - the agent detects gh pr create, release-tag intent, or a milestone that should trigger release checks
  - the user asks whether the branch is safe to merge or tag
  - a release process needs repair guidance after a failed gate
do_not_use_when:
  - the main task is drafting a commit message or naming a normal development branch
  - the request is only to browse tags without judging release readiness
  - the user wants to bypass core quality gates without human approval or without recording the exception
---

# Purpose
Decide whether a change is safe to release, and provide the exact blocking reasons or safe tagging guidance.

# Trigger / When to use
Use this skill when:
- the user is preparing a PR gate, release, tag, or hotfix
- the agent detects `gh pr create`, release-tag intent, or a milestone that should trigger release checks
- the user asks whether the branch is safe to merge or tag
- a release process needs repair guidance after a failed gate

Do not use this skill when:
- the main task is drafting a commit message or naming a normal development branch
- the request is only to browse tags without judging release readiness
- the user wants to bypass core quality gates without human approval or without recording the exception

# Inputs
- the target branch, PR, tag, or release version
- the current workspace state, including whether uncommitted changes exist
- the project's current version sources such as `pyproject.toml`, `__version__.py`, or `package.json`
- the pass/fail signals from testing, strict typing, lint, CI, reviewer approval, and documentation updates
- whether the change includes API or contract changes that require synced documentation
- whether an emergency marker and human confirmation exist

# Process
1. Select the requested endpoint before applying gates:
   - Draft PR: verify authorized branch/base, intended committed diff, relevant local checks, and honest disclosure of pending checks/review. CI or human approval that the PR will request is not a creation prerequisite. Stop at human review; never infer merge or tag permission.
   - Merge readiness: require the repository's applicable review, CI, test, lint and typing gates; report absent evidence as unconfirmed. Tag uniqueness and version-to-tag agreement apply only when this is also a release.
   - Release/tag: follow the normal or explicit emergency path in `references/detailed-guidance.md`. That release-specific procedure, validation and failure handling apply to this endpoint, not ordinary draft creation.
2. For draft PR or merge assessment, use the endpoint checks above and report the remaining gates.
3. For release/tag, read `references/detailed-guidance.md` for version synchronization, normal/emergency gates, tagging safety, and failure recovery before proceeding.

# Examples

- **Positive**: Block a release until `pyproject.toml`, `__version__.py`, CI, type checks, docs, and the intended tag all align, then output the exact safe tagging commands.
- **Negative**: Allow `[emergency]` to skip failing tests, ignore an existing tag, or release from a dirty workspace because the change "looks small."

# Outputs
- a release decision: blocked, ready for PR, ready to tag, or emergency-path pending human confirmation
- a clear normal-path or emergency-path gate result
- explicit failed-gate diagnostics and repair guidance
- safe commands only for the requested endpoint after its applicable gate is satisfied
- version-bump guidance based on commit semantics

# Validation
- Draft PR is complete when the intended committed diff is published to the correct base as a draft and pending checks/review are disclosed. An existing draft is reused, not duplicated.
- Merge readiness requires actual applicable repository gate evidence; this skill does not authorize merging.
- For release/tag validation and repair, read `references/detailed-guidance.md` before any tagging decision.

# Failure Handling
- Missing target or publishing authority: inspect existing context first; ask if still ambiguous. Do not publish to a guessed branch or repository.
- Unavailable CI or review evidence: disclose as pending for a draft; do not claim merge/release readiness.
- Failed local or external action: report the exact failure, retry safe in-scope repairs under existing authorization, and stop for new authority or materially changed risk.

# Boundaries
- Do not invent missing reviewer approval, passing test signals, or version alignment.
- For release/tag, do not bypass required gates except pre-release reviewer approval on the explicit emergency path.
- Draft PR creation may request pending CI and review; this is not a release-gate bypass. Never represent a draft as merge-ready or release-ready. Version-to-tag and tag-uniqueness checks apply only to a release/tag endpoint.
- Do not manage ordinary feature-branch naming or commit-body wording.
- For release/tag, do not assume a fixed project layout when no version files exist; use the documented tag-only mode.

# Local references
- `examples.md`: strict release scenarios, emergency examples, blocked-gate diagnostics, and repair commands
- `references/gate-contract.md`: endpoint-specific gating and required evidence for release/tag
- `references/version-sources.md`: current-state-first version-source detection and synchronization rules
- `references/version-bump-guidance.md`: bump-priority rules derived from commit semantics
- `references/emergency-path.md`: emergency marker, human-confirmation, and post-release follow-up rules

- `references/detailed-guidance.md`: release/tag-only procedure, validation and repair; not required for draft-PR intake.
