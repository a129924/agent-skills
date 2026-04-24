# Workflow Execution Hardening Plan

## Goal / outcome
- Produce a repo-visible execution contract for hardening the workflow so it is
  harder to skip, easier to stop safely, and less likely to stage or ship the
  wrong files.
- Strengthen the canonical workflow and the Main Agent executable guide so the
  most failure-prone transitions become explicit gates instead of soft intent.
- Capture the agreed rules for:
  - Phase 2 branch preflight before any creator work
  - STOP POINT 2 hard handoff to human before manual merge
  - safe staging rules that reject broad staging by default
  - reasonable irreversibility and late-defect routing after merge / release
  - remaining edge-case handling needed to keep the workflow auditable
- Keep this topic focused on workflow execution semantics, not on authoring a new
  domain skill or changing the stable library.

## Scope
- **In scope**:
  - Update `plan/agent-handoff-workflow.md` so Phase 2 becomes a real creator
    precondition, not just descriptive text.
  - Update `.github/guides/MAIN-AGENT-WORKFLOW.md` so STOP POINT 2 becomes a
    true hard stop and the pre-commit staging flow becomes safer.
  - Define explicit safe-staging boundaries for publish work:
    - allowed file set
    - staged preview expectations
    - rejection of broad staging such as `git add -A`
  - Define workflow-level routing for late-discovered defects, including what may
    still route back before release and what must become a repair topic.
  - Add or refine only the minimum tightly coupled workflow wording needed in git
    support skills if contradictions remain after the spec / guide updates.
  - Record the remaining workflow edge cases that must be resolved explicitly
    rather than left to ad hoc agent judgment.

- **Out of scope**:
  - Creating or revising a regular domain skill under `.github/skills/python-*`
    or similar folders
  - Updating `README.md`
  - Updating `VERSION`
  - Creating a repository release or Git tag
  - Re-litigating the entire creator/reviewer architecture from scratch
  - Broad repo-wide style edits unrelated to workflow execution semantics

## Locked decisions
- This topic is a **workflow execution hardening topic**, not a new skill topic
  and not a stable-library publish topic.
- The workflow hardening for this topic must encode the following decisions:
  1. **Phase 2 preflight gate**
     - Creator work must not begin until Main Agent verifies branch readiness.
     - Branch readiness must include the current branch, branch naming policy,
       worktree state, and topic alignment.
     - The first implementation step after plan validation is therefore branch
       preparation, not creator drafting.
  2. **STOP POINT 2 hard stop**
     - Once the workflow reaches the human manual-merge stage, agent execution
       must fully stop.
     - No background waiting, no polling loop, and no automatic merge detection
       may continue after handoff to the human.
     - Phase 9-10 may resume only when a human sends a new explicit message after
       merge.
  3. **Safe staging boundary**
     - Broad staging such as `git add -A` is not an acceptable default in the
       publish path.
     - The allowed staged file set is limited to:
       1. artifact paths locked in the topic plan
       2. PR direct-apply files
       3. extra files explicitly approved by a human
     - STOP POINT 1 must preview the staged file set clearly before commit.
  4. **Reasonable irreversibility**
     - `released` remains a hard no-rollback boundary for the original topic.
     - `merged` but not yet `released` may allow limited rollback only with
       explicit routing, not as an automatic default.
     - Late-discovered defects after merge should prefer repair-note or follow-up
       topic routing over retroactively rewriting the original topic intent.
  5. **Layered responsibility**
     - Canonical workflow and Main Agent guide own phase boundaries, stop
       conditions, staging safety, and routing rules.
     - Tightly coupled git skills may reinforce those rules, but they are not the
       sole enforcement layer.
  6. **Reference usage**
     - `other-project-examples/reference-agent-skills/addyosmani/agent-skills`
       may influence lifecycle enforcement style, anti-rationalization language,
       and “required steps before implementation” phrasing.
     - It must not replace this repository's topic-plan contract or folder
       conventions.
- This topic does **not** add stable-library metadata; `README.md`, `VERSION`,
  release notes, and tags stay untouched.

## Boundaries / exclusions
- Do not widen this topic into a broad rewrite of all git-related skills unless a
  direct contradiction remains after the workflow spec and guide are updated.
- Do not change regular skill content merely to “demonstrate” the hardened
  workflow.
- Do not allow new workflow rules to depend on hidden session context, cached
  branch assumptions, or background waiting behavior.
- Do not treat `git-commit-convention` as the only place that catches mixed or
  unsafe staging; workflow-level gating must remain primary.
- Do not retroactively rewrite the meaning of historical topics or their locked
  intent in this topic.
- Do not introduce a release action in this topic.

## Status / allowed transitions
- **Current status**: `pr-open`
- **Open PR**: `#21` — `https://github.com/a129924/agent-skills/pull/21`
- **PR feedback reroute**: `pr-open` → `needs-rework` → `creator-in-progress`
  because PR #21 comments require reviewer re-check before merge handoff resumes.
- **Execution model**: follow the canonical creator → reviewer → publish → merge
  path, but stop at `merged`; no release action is declared for this topic.
- **Allowed transitions**:
  - `planned` → `creator-in-progress`
  - `creator-in-progress` → `review-ready`
  - `review-ready` → `reviewer-in-progress`
  - `reviewer-in-progress` → `approved`
  - `reviewer-in-progress` → `needs-rework`
  - `needs-rework` → `creator-in-progress`
  - `approved` → `creator-in-progress`
  - `approved` → `publish-in-progress`
  - `publish-in-progress` → `pr-open`
  - `publish-in-progress` → `merged`
  - `pr-open` → `needs-rework`
  - `pr-open` → `merged`
  - `merged` → terminal

Routing notes:
- This topic hardens the workflow contract itself, so planner alignment is
  especially important before publish work begins.
- If the implementation proposes workflow behavior that contradicts any locked
  decision above, route the topic back before publish.
- Because no release action is declared, `merged` is terminal for this topic.

## Artifact paths
| Artifact | Path | Owner | Role |
| --- | --- | --- | --- |
| Topic plan | `plan/workflow-execution-hardening/workflow-execution-hardening.plan.md` | Planning actor | Repo-visible execution contract for this topic |
| Canonical workflow spec | `plan/agent-handoff-workflow.md` | Creator | Primary workflow semantics to harden |
| Main Agent executable guide | `.github/guides/MAIN-AGENT-WORKFLOW.md` | Creator | Executable sequencing, stop points, and recovery wording that must match the canonical spec |
| Branch naming skill contract (conditional) | `.github/skills/git-branch-naming/SKILL.md` | Creator | Only update if branch-preflight hardening requires explicit contradiction repair |
| Commit convention skill contract (conditional) | `.github/skills/git-commit-convention/SKILL.md` | Creator | Only update if safe-staging hardening requires explicit staged-set guidance alignment |
| Post-merge workflow skill contract (conditional) | `.github/skills/git-post-merge-workflow/SKILL.md` | Creator | Only update if manual-resume or post-merge routing semantics require direct contradiction repair |
| Release management skill contract (conditional) | `.github/skills/git-release-management/SKILL.md` | Creator | Only update if late-defect / release routing semantics require direct contradiction repair |
| External lifecycle reference (read-only) | `other-project-examples/reference-agent-skills/addyosmani/agent-skills/AGENTS.md` | Planning actor / Creator | Source of lifecycle enforcement and anti-rationalization ideas |
| External planning command reference (read-only) | `other-project-examples/reference-agent-skills/addyosmani/agent-skills/.claude/commands/plan.md` | Planning actor / Creator | Source of read-only planning / required-steps phrasing |

Artifact path notes:
- `README.md` and `VERSION` are intentionally outside the editable artifact set.
- The git skill files listed above are **conditional artifacts**. Edit them only
  if the workflow-spec and guide changes leave a direct contradiction that would
  confuse future execution.
- Any repo-visible edit outside the listed artifact set is plan drift and must be
  routed before publish work continues.

## Implementation steps
1. Read the current canonical workflow, Main Agent guide, and tightly coupled git
   skills before making edits so the hardening remains coherent across phases.
2. Update `plan/agent-handoff-workflow.md` to make Phase 2 an explicit gate by
   stating:
   - creator work must not start before verified branch readiness
   - required branch-preflight inputs
   - stop behavior when branch readiness fails
3. Update the same canonical workflow file to harden STOP POINT 2:
   - no background waiting after handoff to human merge
   - no merge detection loop after the handoff
   - explicit human-resume requirement for Phase 9-10
4. Update the same canonical workflow file to define safe-staging boundaries:
   - forbid broad staging as a default publish pattern
   - define the allowed staged file set
   - require staged preview before commit
5. Update the same canonical workflow file to express reasonable
   irreversibility / late-defect routing:
   - what may still route back before release
   - what should become a repair topic or repair note after merge / release
6. Update `.github/guides/MAIN-AGENT-WORKFLOW.md` so the executable sequence
   matches the hardened canonical rules, including:
   - branch-preflight checklist before creator invocation
   - STOP 2 hard stop wording
   - safe-staging preview and allowed-file-set language
   - resume trigger expectations after manual merge
   - late-defect routing notes around Phase 9-10
7. Review the tightly coupled git skills only for direct contradictions. Update
   them only when necessary to keep future execution consistent with the hardened
   workflow.
8. Hand the resulting workflow topic to the reviewer flow once the spec, guide,
   and any directly coupled skill wording are internally consistent.

## Validation / acceptance checks
### Creator readiness (before handoff to reviewer)
- [ ] `plan/agent-handoff-workflow.md` now treats Phase 2 as a real creator
      precondition rather than descriptive advice
- [ ] the canonical workflow clearly forbids background waiting after STOP POINT 2
- [ ] the canonical workflow clearly forbids broad staging as a default publish
      pattern
- [ ] the allowed staged file set is explicit and aligned with the locked
      decisions in this topic plan
- [ ] the workflow expresses reasonable irreversibility without making every late
      issue an automatic rollback
- [ ] `.github/guides/MAIN-AGENT-WORKFLOW.md` no longer contradicts the canonical
      workflow on STOP 2, staging behavior, or branch preflight
- [ ] any git skill edits remain narrowly scoped to contradiction repair and do
      not broaden into unrelated git-policy rewrites
- [ ] no repo-visible edits exist outside the listed artifact paths
- [ ] `README.md` and `VERSION` remain untouched

### Reviewer approval criteria
- [ ] reviewer can trace each hardened workflow rule back to a locked decision in
      this topic plan
- [ ] role separation among planning actor, creator, reviewer, and Main Agent is
      preserved
- [ ] STOP 2 is now an actual human handoff boundary, not an implicit polling loop
- [ ] safe-staging guidance prevents broad accidental commits without forcing one
      fixed git command for every situation
- [ ] irreversibility rules preserve auditability while still allowing limited
      human-routed correction where explicitly intended
- [ ] edge-case handling is clearer after the update, even where some cases remain
      deferred for a later topic
- [ ] no stable-library publish or release semantics were introduced into this
      workflow-hardening topic

## Reviewer handoff
- Reviewer inputs:
  - Topic plan: `plan/workflow-execution-hardening/workflow-execution-hardening.plan.md`
  - Canonical workflow spec: `plan/agent-handoff-workflow.md`
  - Main Agent guide: `.github/guides/MAIN-AGENT-WORKFLOW.md`
  - Any conditionally edited git skill files listed in `Artifact paths`
- Latest independent reviewer verdict:
  - prior pre-PR verdict: `approved`
  - prior PR-loop verdict: `needs-rework`
  - latest PR-loop re-review verdict: `approved`
  - blocking issues: none
- Review focus:
  - whether the hardened workflow now prevents the known Phase 2 skip
  - whether STOP 2 is a true hard handoff to human
  - whether safe staging is enforced at workflow level instead of only at commit-message level
  - whether irreversibility / late-defect routing stays auditable and non-chaotic
  - whether any remaining edge cases are deferred explicitly instead of being left
    as hidden assumptions
- Reviewer output must follow the workflow JSON contract:

```json
{
  "verdict": "approved|needs-rework",
  "blocking_issues": [
    {
      "issue": "Description of unmet workflow-hardening requirement",
      "file": "path/to/file.md",
      "fix": "Concrete change required before re-review"
    }
  ],
  "copilot_feedback_triage": {
    "ADDRESS": [],
    "DISCUSS": [],
    "SKIP": []
  }
}
```

## Post-merge / release actions
1. After merge, run the normal post-merge local sync flow for the workflow branch.
2. Do **not** update `README.md`, `VERSION`, release notes, or tags in this topic.
3. No repository release action is required; this topic is terminal at `merged`.
4. A later follow-up topic may:
   - refine any deferred edge case that proves too large for this hardening topic
   - update human-facing summary docs if they become directly inconsistent
   - define a workflow-repair or release-repair pattern in more detail if the
     limited irreversibility rules need a dedicated follow-up

## Open questions / unresolved items
- Whether default-branch / merge-strategy mismatch needs explicit normative text
  in this same topic or can remain a documented follow-up edge case depends on
  how much wording is needed to keep Phase 9 safe.
- Whether dirty-workspace rules should be fully centralized in the canonical
  workflow or partly delegated to existing git skills may need a narrow follow-up
  clarification after draft review.
- Whether old topic plans may accept factual repair notes in-place, versus always
  using a follow-up repair topic, may need one more explicit policy pass if the
  reviewer finds ambiguity.
- Whether resume-trigger minimum evidence (for example PR number, target branch,
  or merge method) should be fully locked in this topic or left as a subsequent
  refinement is still open.
