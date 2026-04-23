# Creator/Reviewer Gate Hardening Plan

## Goal / outcome
- Produce a repo-visible execution contract for the **first rollout phase** of the
  validation upgrade work.
- Strengthen `agent-skill-creator` and `agent-skill-reviewer` first so they become
  the gatekeepers for later downstream skill updates.
- Translate the most valuable ideas from the external reference library into this
  repository's format **without** importing its folder structure directly.
- Keep this topic focused on the creator/reviewer gate plus the minimum shared
  policy/template updates needed to keep those two skills consistent.

## Scope
- **In scope**:
  - Update `.github/skills/agent-skill-creator/` to express clearer
    risk-based validation expectations.
  - Update `.github/skills/agent-skill-reviewer/` so the same expectations are
    enforced consistently during review.
  - Update the minimum tightly coupled shared files needed to keep creator and
    reviewer aligned:
    - `.github/copilot-instructions.md`
    - `.github/skills/agent-skill-template/`
  - Keep explicit deferral notes for downstream regular skills so later topics do
    not need to infer ordering from chat history.

- **Out of scope**:
  - Bulk-editing the rest of `.github/skills/`
  - Creating a new regular domain skill
  - Adding or removing stable-library entries in `README.md`
  - Updating `VERSION`
  - Running a repository release or tag action
  - Rewriting `plan/agent-handoff-workflow.md` or `.github/guides/MAIN-AGENT-WORKFLOW.md`

## Locked decisions
- This topic is a **meta-skill gate refinement topic**, not a downstream skill
  rollout and not a release topic.
- Execution order is fixed:
  1. harden `agent-skill-creator`
  2. harden `agent-skill-reviewer`
  3. make only the minimum supporting shared-file edits required for consistency
  4. defer downstream skill cases to a later topic
- The external reference repository may influence:
  - process-first wording
  - verification / evidence expectations
  - red-flag style risk signaling
  - anti-rationalization guidance

  It must **not** replace this repository's skill-folder contract.
- Validation remains **risk-based**, not universal-by-default:
  - lightweight rules stay lightweight
  - medium-complexity skills keep bounded structure
  - heavy validation is concentrated in high-risk / gatekeeper skills
- This topic may refine how creator and reviewer talk about:
  - `Do not use` / boundaries
  - stop-and-ask behavior on ambiguity
  - when `Verification`, `Red Flags`, or `Common Rationalizations` should appear

  It must **not** force every existing skill to adopt all of those sections in the
  same topic.
- `agent-skill-reviewer` remains the approval gate and must not author the final
  implementation directly.
- `README.md` and `VERSION` remain untouched in this topic; any later human-summary
  sync or versioning decision belongs to a follow-up rollout topic if needed.
- Because this topic does not add a new stable skill entry and does not declare a
  release action, `Stable library metadata` is intentionally absent.

## Boundaries / exclusions
- Do not update regular domain skills such as `python-*`, `git-*`, or
  `sense-env-scaffold` in this topic.
- Do not broaden this work into repo-wide mandatory section inflation for every
  skill folder.
- Do not invent new optional folder roles unless the canonical policy truly needs
  them.
- Do not change the stable-library table rows in `README.md`.
- Do not change `VERSION` or introduce a tag / release workflow step.
- Do not rewrite creator/reviewer so aggressively that existing repository policy
  ownership becomes unclear; `.github/copilot-instructions.md` must remain the
  canonical policy owner.

## Status / allowed transitions
- **Current status**: `publish-in-progress`
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

## Artifact paths
| Artifact | Path | Owner | Role |
| --- | --- | --- | --- |
| Topic plan | `plan/creator-reviewer-gate-hardening/creator-reviewer-gate-hardening.plan.md` | Planning actor | Repo-visible execution contract for this topic |
| Workflow spec | `plan/agent-handoff-workflow.md` | Planning actor / Main Agent | Canonical execution workflow consumed by later phases |
| Canonical repo policy | `.github/copilot-instructions.md` | Creator | Shared policy wording that creator/reviewer must mirror |
| Creator skill contract | `.github/skills/agent-skill-creator/SKILL.md` | Creator | Primary drafting behavior for new skill creation |
| Creator examples | `.github/skills/agent-skill-creator/examples.md` | Creator | Concrete creation scenarios and anti-patterns |
| Creator local contract | `.github/skills/agent-skill-creator/folder-contract.md` | Creator | Shared folder-shape rules referenced during drafting |
| Creator blueprint | `.github/skills/agent-skill-creator/blueprint.md` | Creator | Starter drafting skeleton that must stay aligned with the new gate |
| Reviewer skill contract | `.github/skills/agent-skill-reviewer/SKILL.md` | Creator | Primary review behavior for the independent reviewer |
| Reviewer examples | `.github/skills/agent-skill-reviewer/examples.md` | Creator | Approval / needs-rework examples aligned to the refined gate |
| Reviewer checklist | `.github/skills/agent-skill-reviewer/review-checklist.md` | Creator | Enforcement checklist for the refined creator/reviewer contract |
| Template skill contract | `.github/skills/agent-skill-template/SKILL.md` | Creator | Copyable skeleton that must not contradict the refined gate |
| Template reference | `.github/skills/agent-skill-template/reference.md` | Creator | Shared guidance for example depth, split signals, and promotion rules |
| Template structure file | `.github/skills/agent-skill-template/template.md` | Creator | Copyable section / folder skeleton used by future drafts |
| Template local contract | `.github/skills/agent-skill-template/folder-contract.md` | Creator | Template-side mirror of required core and optional-role rules |
| External reference guide (read-only) | `other-project-examples/reference-agent-skills/addyosmani/agent-skills/README.md` | Planning actor / Creator | Source of reusable workflow ideas, not folder-structure authority |
| External review reference (read-only) | `other-project-examples/reference-agent-skills/addyosmani/agent-skills/skills/code-review-and-quality/SKILL.md` | Planning actor / Creator | Reference for review-axis, evidence, and finding-classification patterns |
| External source-policy reference (read-only) | `other-project-examples/reference-agent-skills/addyosmani/agent-skills/skills/source-driven-development/SKILL.md` | Planning actor / Creator | Reference for explicit source / verification discipline |
| External routing reference (read-only) | `other-project-examples/reference-agent-skills/addyosmani/agent-skills/skills/using-agent-skills/SKILL.md` | Planning actor / Creator | Reference for meta-skill / routing phrasing and stop-on-confusion behavior |

Artifact path notes:
- This topic intentionally leaves `README.md` and `VERSION` outside the editable
  artifact set.
- If execution reveals that creator/reviewer changes cannot stay internally
  consistent without a human-summary update, stop and create a follow-up topic
  rather than silently broadening this one.
- Any repo-visible edits outside the listed editable artifacts are plan drift and
  must route the topic back before publish work continues.

## Implementation steps
1. Read the workflow and the current creator/reviewer/template files before making
   any edits so the rollout stays aligned with the locked phase order.
2. Update `agent-skill-creator/SKILL.md` so the creator contract states, in clear
   executable language:
   - creator-first rollout for this phase
   - risk-based validation thinking
   - when ambiguity must stop drafting and trigger clarification
   - when higher-risk skills should include stronger verification / red-flag style guidance
3. Update the tightly coupled creator-side support files:
   - `blueprint.md`
   - `examples.md`
   - `folder-contract.md`

   so creator examples, skeleton wording, and local folder rules do not contradict
   the refined creator contract.
4. Update `agent-skill-reviewer/SKILL.md` and `review-checklist.md` so reviewer
   enforcement matches the new creator-side expectations, including:
   - review of risk-based validation sufficiency
   - rejection of missing higher-risk validation where the topic warrants it
   - rejection of scope drift into downstream case rollout
5. Update `agent-skill-reviewer/examples.md` so approval / rework examples reflect
   the refined review gate, not the older lighter contract.
6. Update the minimum shared policy/template files only where creator and reviewer
   need common wording:
   - `.github/copilot-instructions.md`
   - `.github/skills/agent-skill-template/SKILL.md`
   - `.github/skills/agent-skill-template/reference.md`
   - `.github/skills/agent-skill-template/template.md`
   - `.github/skills/agent-skill-template/folder-contract.md`
7. Keep downstream regular skills untouched in this topic. If any implementation
   choice requires editing a regular skill to “prove the rule,” stop and defer that
   proof to the later pilot topic instead.
8. When the edit set is internally consistent and still matches the locked artifact
   paths, hand the topic to the independent reviewer.

## Validation / acceptance checks
### Creator readiness (before handoff to reviewer)
- [x] `agent-skill-creator` explicitly states the first-phase focus on creator /
      reviewer gate hardening before downstream rollout
- [x] `agent-skill-creator` makes ambiguity handling explicit instead of silently
      proceeding on guesswork
- [x] creator-side support files do not contradict the updated creator contract
- [x] `agent-skill-reviewer` and `review-checklist.md` clearly enforce the same
      refined creator expectations
- [x] reviewer language distinguishes lightweight / medium / heavier validation
      expectations by risk, or an equivalent explicit rule set
- [x] no new repo-global folder roles were invented without canonical-policy need
- [x] no regular domain skill folder outside creator/reviewer/template was edited
- [x] no repo-visible path drift exists outside the listed editable artifacts
- [x] `README.md` and `VERSION` remain untouched

### Reviewer approval criteria
- [x] reviewer can trace every new creator/reviewer requirement back to either:
      canonical policy, template alignment, or an explicitly locked plan decision
- [x] creator and reviewer remain separate roles with no ownership confusion
- [x] refined validation guidance is stronger for high-risk/meta skills without
      accidentally forcing the same weight onto all skills
- [x] reviewer checklist can reject missing stronger validation where the topic
      clearly requires it
- [x] reviewer examples still distinguish `approved` vs `needs-rework` with
      concrete, non-vague reasons
- [x] template files stay copy-friendly and do not become a second hidden policy owner
- [x] no stable-library publish or release semantics were smuggled into this topic
- [x] the topic remains executable under the locked artifact paths and status model

## Reviewer handoff
- Reviewer inputs:
  - Topic plan: `plan/creator-reviewer-gate-hardening/creator-reviewer-gate-hardening.plan.md`
  - Creator skill folder: `.github/skills/agent-skill-creator/`
  - Reviewer skill folder: `.github/skills/agent-skill-reviewer/`
  - Template skill folder: `.github/skills/agent-skill-template/`
  - Canonical policy file: `.github/copilot-instructions.md`
- Latest independent reviewer verdict:
  - `approved`
  - blocking issues: none
- Review focus:
  - whether creator/reviewer now form a clearer first-phase gate
  - whether validation guidance is risk-based instead of indiscriminately heavy
  - whether creator / reviewer / template / canonical policy stay aligned
  - whether the topic stayed out of downstream regular-skill rollout
  - whether any unstated requirement was introduced through examples or checklist wording
- Reviewer output must follow the workflow JSON contract:

```json
{
  "verdict": "approved|needs-rework",
  "blocking_issues": [
    {
      "issue": "Description of unmet plan-aligned requirement",
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
1. After merge, run the normal post-merge local sync flow for the working branch.
2. Do **not** update `README.md`, `VERSION`, release notes, or tags in this topic.
3. No repository release action is required; this topic is terminal at `merged`.
4. A later follow-up topic may:
   - choose one downstream pilot skill
   - perform any needed README human-summary sync
   - decide whether a later version bump is warranted

## Open questions / unresolved items
1. Should `Validation / acceptance checks` become a universally required top-level
   `SKILL.md` section later, or remain a heavier-skill pattern only?
2. Should `Red Flags` and `Common Rationalizations` become:
   - required for high-risk skills only
   - recommended but optional for medium-complexity skills
   - absent from lightweight skills by default
3. Which downstream pilot skill should follow this topic first:
   `git-release-management`, `sense-env-scaffold`, or another case?
4. Should a later follow-up topic synchronize `README.md` immediately after this
   gate-hardening work, or bundle that summary sync with the first downstream pilot?
