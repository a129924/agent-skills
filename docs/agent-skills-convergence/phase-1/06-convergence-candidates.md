# Convergence Candidates
## A. Safe to keep `skills/` as canonical

- Skill Name: `agent-skill-reviewer`
  Current Best Source: `skills/`
  Reason: identical same-name content or low-risk canonical candidate
  Risk: low
  Recommended Phase 2 Action: adopt `skills/` as canonical without content rewrite
  Recommended Phase 3 Action: optional codex projection if needed
- Skill Name: `business-intent-alignment`
  Current Best Source: `skills/`
  Reason: identical same-name content or low-risk canonical candidate
  Risk: low
  Recommended Phase 2 Action: adopt `skills/` as canonical without content rewrite
  Recommended Phase 3 Action: optional codex projection if needed
- Skill Name: `business-to-technical-translation`
  Current Best Source: `skills/`
  Reason: identical same-name content or low-risk canonical candidate
  Risk: low
  Recommended Phase 2 Action: adopt `skills/` as canonical without content rewrite
  Recommended Phase 3 Action: optional codex projection if needed
- Skill Name: `git-branch-naming`
  Current Best Source: `skills/`
  Reason: identical same-name content or low-risk canonical candidate
  Risk: low
  Recommended Phase 2 Action: adopt `skills/` as canonical without content rewrite
  Recommended Phase 3 Action: optional codex projection if needed
- Skill Name: `git-commit-convention`
  Current Best Source: `skills/`
  Reason: identical same-name content or low-risk canonical candidate
  Risk: low
  Recommended Phase 2 Action: adopt `skills/` as canonical without content rewrite
  Recommended Phase 3 Action: optional codex projection if needed
- Skill Name: `git-post-merge-workflow`
  Current Best Source: `skills/`
  Reason: identical same-name content or low-risk canonical candidate
  Risk: low
  Recommended Phase 2 Action: adopt `skills/` as canonical without content rewrite
  Recommended Phase 3 Action: optional codex projection if needed
- Skill Name: `python-project-init-greenfield`
  Current Best Source: `skills/`
  Reason: same-name content is identical across `skills/` and `.github/skills/`; only `.codex/skills/` projection is missing
  Risk: low
  Recommended Phase 2 Action: adopt `skills/` as canonical without content rewrite
  Recommended Phase 3 Action: project with path rewrite and runtime validation only if Codex consumption is needed
- Skill Name: `python-project-retrofit`
  Current Best Source: `skills/`
  Reason: same-name content is identical across `skills/` and `.github/skills/`; only `.codex/skills/` projection is missing
  Risk: low
  Recommended Phase 2 Action: adopt `skills/` as canonical without content rewrite
  Recommended Phase 3 Action: project with path rewrite and runtime validation only if Codex consumption is needed
- Skill Name: `worktree-manager`
  Current Best Source: `skills/`
  Reason: identical same-name content or low-risk canonical candidate
  Risk: low
  Recommended Phase 2 Action: adopt `skills/` as canonical without content rewrite
  Recommended Phase 3 Action: optional codex projection if needed

## B. Need merge into `skills/`

- Skill Name: `agent-skill-creator`
  Current Best Source: `skills/`
  Reason: skills/ and .github/ differ on authoring target path
  Risk: medium
  Recommended Phase 2 Action: merge newer GitHub-only or divergent material into `skills/` under review
  Recommended Phase 3 Action: project after merge and runtime review
- Skill Name: `agent-skill-template`
  Current Best Source: `skills/`
  Reason: template and folder-contract differ on active authoring path
  Risk: medium
  Recommended Phase 2 Action: merge newer GitHub-only or divergent material into `skills/` under review
  Recommended Phase 3 Action: project after merge and runtime review
- Skill Name: `python-library-architecture`
  Current Best Source: `skills/`
  Reason: github surface adds reference.md and broader validation wording
  Risk: medium
  Recommended Phase 2 Action: merge newer GitHub-only or divergent material into `skills/` under review
  Recommended Phase 3 Action: project after merge and runtime review
- Skill Name: `python-package-layout`
  Current Best Source: `skills/`
  Reason: github surface adds reference.md and broader routing wording
  Risk: medium
  Recommended Phase 2 Action: merge newer GitHub-only or divergent material into `skills/` under review
  Recommended Phase 3 Action: project after merge and runtime review
- Skill Name: `python-blueprint-authoring`
  Current Best Source: `skills/`
  Reason: github surface adds checklist and reference set
  Risk: medium
  Recommended Phase 2 Action: merge newer GitHub-only or divergent material into `skills/` under review
  Recommended Phase 3 Action: project after merge and runtime review
- Skill Name: `python-plan-authoring`
  Current Best Source: `skills/`
  Reason: github surface adds templates and expanded plan contract
  Risk: medium
  Recommended Phase 2 Action: merge newer GitHub-only or divergent material into `skills/` under review
  Recommended Phase 3 Action: project after merge and runtime review
- Skill Name: `python-pre-commit`
  Current Best Source: `skills/`
  Reason: github surface adds script, templates, references, and tests
  Risk: medium
  Recommended Phase 2 Action: merge newer GitHub-only or divergent material into `skills/` under review
  Recommended Phase 3 Action: project after merge and runtime review
- Skill Name: `python-pyproject-toolconfig`
  Current Best Source: `skills/`
  Reason: github surface adds script, templates, references, and tests
  Risk: medium
  Recommended Phase 2 Action: merge newer GitHub-only or divergent material into `skills/` under review
  Recommended Phase 3 Action: project after merge and runtime review
- Skill Name: `python-tdd-test-authoring`
  Current Best Source: `skills/`
  Reason: github surface adds checklist and verdict-oriented references
  Risk: medium
  Recommended Phase 2 Action: merge newer GitHub-only or divergent material into `skills/` under review
  Recommended Phase 3 Action: project after merge and runtime review
- Skill Name: `python-blueprint-review`
  Current Best Source: `.github/skills/`
  Reason: missing canonical counterpart under skills/; validates exact current library root via .github/skills path
  Risk: medium
  Recommended Phase 2 Action: merge newer GitHub-only or divergent material into `skills/` under review
  Recommended Phase 3 Action: project after merge and runtime review

## C. Keep only as Copilot legacy

- Skill Name: `copilot-instructions-init`
  Current Best Source: `.github/skills/`
  Reason: writes .github/copilot-instructions.md and consumes .github skill inventory
  Risk: high
  Recommended Phase 2 Action: do not canonicalize into generic tree yet
  Recommended Phase 3 Action: do not project generically

## D. Need split into generic core + platform adapter

- Skill Name: `plan-step-tracker`
  Current Best Source: `skills/`
  Reason: CLI path and supported operation set differ between surfaces
  Risk: medium
  Recommended Phase 2 Action: design adapter boundary before convergence
  Recommended Phase 3 Action: project after merge and runtime review
- Skill Name: `sense-env-scaffold`
  Current Best Source: `skills/`
  Reason: runtime assertion handling differs in script implementation
  Risk: medium
  Recommended Phase 2 Action: design adapter boundary before convergence
  Recommended Phase 3 Action: project after merge and runtime review

## E. Need human review

- Skill Name: `plan-creator`
  Current Best Source: `skills/`
  Reason: fallback contract source differs between surfaces
  Risk: high
  Recommended Phase 2 Action: freeze until drift authority is decided
  Recommended Phase 3 Action: human-review before any projection
- Skill Name: `plan-reviewer`
  Current Best Source: `skills/`
  Reason: review basis path and blocked behavior differ between surfaces
  Risk: high
  Recommended Phase 2 Action: freeze until drift authority is decided
  Recommended Phase 3 Action: human-review before any projection

## F. Candidate for deletion later, but do not delete in Phase 1

- none identified in Phase 1
