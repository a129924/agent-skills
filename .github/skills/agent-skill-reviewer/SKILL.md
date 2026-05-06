---
name: agent-skill-reviewer
description: Review a review-ready Agent Skill folder for required core files, complexity-gated sections, YAML-body alignment, risk-appropriate validation, concise positive and negative examples, declared local file roles, single responsibility, portability, independence, and explicit trigger clarity. Use this when a skill draft is ready to be approved or sent back for rework.

complexity: high

risk_profile:
  - ambiguity_sensitive
  - multi_agent_handoff

use_when:
  - a new skill has been drafted and marked review-ready
  - an existing skill has changed materially
  - someone wants an approved or needs-rework verdict

do_not_use_when:
  - the request is to author a new skill from scratch
  - the task is only to browse the library without judging quality
---

# Purpose
Review a `review-ready` skill before it becomes part of the stable library.

# Trigger / When to use
Use this skill when:
- a new skill has been drafted
- an existing skill has changed materially
- someone wants an `approved` or `needs-rework` review against repository rules

Do not use this skill when:
- the request is to author a new skill from scratch
- the task is only to browse the library without judging quality

# Inputs
- the target skill folder
- the repository rules for stable skills
- the topic plan, if the review is running under a repo-visible topic workflow
- any risk signals, such as gatekeeping responsibility, external-tool usage, branching, or larger downstream impact

# Process
1. Read `review-checklist.md`.
2. Confirm the required core exists.
3. Inspect frontmatter and required sections in `SKILL.md`, including concise positive and negative examples.
4. Confirm each optional file or folder has a clear declared role, including each file inside `references/` when that folder exists.
5. Confirm the skill has one clear responsibility.
6. Confirm the skill is portable, independent, and self-contained.
7. Assess whether the skill's validation weight matches its risk, branching, external-tool usage, and downstream impact.
8. Treat `references/` as a split-reference supplement, not by itself as a replacement for the required companion-file rule.
9. If `reference.md` is too broad, require it to be split into `references/`.
10. If the skill is high complexity or the concise examples are not enough for about 80% of routine usage, require `examples.md`.
11. If the skill is higher-risk or acts as a gatekeeper, require stronger validation signals or equivalent local guidance that makes misuse harder.
12. Confirm `complexity` field exists in YAML and matches the skill's actual workflow risk, branching, and downstream impact; escalate if risk tags understate behavior.
13. Confirm YAML governance metadata (`use_when`, `do_not_use_when`, `inputs`, `outputs`) aligns with body sections and does not contradict them.
14. Confirm `Validation` section exists with Required Checks and Quality Checks tiers for medium and high complexity skills; confirm it defines SOFT FAIL or BLOCKED conditions, not only hard stops.
15. Confirm `Failure Handling` covers Missing Context, Ambiguous Requirement, and Execution Limitation for high complexity skills.
16. Confirm no hard-stop `FAIL → stop` design exists for a recoverable gap.
17. Label each finding as BLOCKER, WARNING, or INFO before returning verdict.
18. Confirm it has an explicit `Trigger / When to use` section.
19. Return `approved` or `needs-rework` with concrete fixes.

# Examples
- Positive: Review a refactoring or release-gating skill whose `SKILL.md` has brief positive and negative examples, whose local files justify stronger validation, and whose `examples.md` covers the complex branches.
- Negative: Approve a draft that has no negative example in `SKILL.md`, no `examples.md` for a branching refactor skill, or no stronger misuse-prevention guidance for a higher-risk gatekeeping skill.

# Outputs
- `approved` or `needs-rework`
- blocking issues, if any
- concise follow-up fixes when the skill fails
- findings labeled as BLOCKER, WARNING, or INFO

# Validation

## Required Checks
- `review-checklist.md` has been read before any verdict is issued
- verdict is either `approved` or `needs-rework`, not a partial or conditional answer
- every BLOCKER finding is accompanied by a concrete fix description

## Quality Checks (best effort)
- WARNING and INFO findings each include a brief rationale
- legacy skill status (unclassified) is noted when applicable
- checklist coverage gaps are surfaced in a dry review report

## On Soft Fail
- mark status as INCOMPLETE
- list which checklist sections could not be evaluated
- issue a partial verdict only if the evaluated sections conclusively resolve the outcome

# Failure Handling

## Missing Context
- mark output as INCOMPLETE
- list the missing inputs required to complete the review

## Ambiguous Requirement
- if blocking: stop and ask before issuing a verdict
- if non-blocking: proceed with stated assumptions, list them in the output

## Execution Limitation
- state the limitation explicitly in the verdict output
- do not fabricate a verdict when the target skill cannot be evaluated

# Workflow State Contract

When participating in a multi-agent review or creator-reviewer handoff, include:
- current_step: <step name from Process>
- next_step: <next step or DONE>
- status: APPROVED | NEEDS_REWORK | INCOMPLETE | BLOCKED

Omit this section when the review is performed as a standalone action.
- Do not rewrite the skill's purpose to force a pass.
- Do not approve a skill that lacks required core files, required examples, or clear local roles.
- Do not ignore vague triggers or bundled responsibilities.
- Do not require heavyweight validation on a lightweight skill unless the risk clearly warrants it.
- Do not author the final implementation directly.

# Local references
- `review-checklist.md`: approval criteria, lifecycle rules, and reject signals
- `examples.md`: approved and needs-rework examples
