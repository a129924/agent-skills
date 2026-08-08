# Semantic-First Design — Progression

## Workflow Stages

| Stage | Status | Owner | Entry condition | Exit / next gate |
| --- | --- | --- | --- | --- |
| Original plan authoring | done (historical) | Plan-Creator | Locked human decisions and readable shared contracts | Original plan became review-ready |
| Original planning-artifact review | approved (historical) | Plan-Reviewer | Original planning artifacts existed | Original approval permitted implementation |
| Original feature implementation | done (historical) | Implementer | Original planning approval | PR feedback now requires a separately reviewed six-file repair |
| Original implementation review | approved (historical) | Reviewer | Original implementation was review-ready | Original approval permitted publish preparation |
| Original publish and PR opening | done (historical) | Main Agent | Approved implementation and authorized publish path | Existing PR is open |
| Human review | needs-rework (historical) | Human | Existing PR is open | PR feedback entered `pr-open` -> `needs-rework` |
| First planning-artifact repair | done (historical) | Plan-Creator | Historical PR `needs-rework` required planning repair | Completed handoff at `review-ready` |
| First renewed planning-artifact review | approved (historical) | Plan-Reviewer | First repair was `review-ready` | Prior approval permitted implementation work |
| Implementation repair content | done (historical) | Implementer | Prior renewed planning approval | Six document/inventory content passed renewed implementation review |
| Renewed implementation review | needs-rework (received trigger) | Reviewer | Implementation content was review-ready | Planning lifecycle/log contradiction requires Planning-state repair; no skill/inventory repair is requested |
| Planning-state repair | done (historical) | Plan-Creator | Received planning-only `needs-rework` | Post-repair Plan-Reviewer approved the completed `review-ready` handoff |
| Post-repair planning-artifact review | approved (historical) | Plan-Reviewer | Planning-state repair was `review-ready` | Approval routes existing seven fixes to final independent implementation review |
| New Implementer content repair | not required | Implementer | Post-repair Plan-Reviewer `approved` | No new content change before final review |
| Final implementation review of existing seven fixes | approved (historical) | Reviewer | Five prior verdicts and existing seven fixes | Sixth recorded `approved` completes all review gates |
| Patch commit and push | publish-in-progress (current) | Main Agent (publication); Implementer (validation support) | All six review gates approved; passing validation and explicit prior user authorization | Existing PR receives bounded patch commit(s) and returns to human review |
| Human review after patch | pending | Human | Existing PR contains pushed repair | Human merge decision; no automatic continuation |
| Post-merge release assessment | blocked by human gate | Human then Main Agent | Explicit human resume after merge | No automatic tag or release |

## Actionable Steps

1. Six review gates are complete, including final independent implementation
   approval of the existing seven fixes. No further Implementer content repair
   is required.
2. Main Agent runs publication validation with Implementer support. Commit and
   push require passing validation plus the explicit prior user authorization.
3. On successful publication, the existing PR returns to human review.
4. Stop for human review. Do not merge, release, tag, or perform post-merge
   work without a later explicit human action.

## Handoff / Gate Notes

- `pr-open` -> `needs-rework`, the prior renewed Plan-Reviewer `approved`, and
  the received renewed Implementation Reviewer `needs-rework` are historical
  evidence. The last result triggers Planning-state repair only.
- All six review gates are complete, including Final Implementation Reviewer
  `approved`. Current status is `publish-in-progress`; next actor is the
  Main Agent publication flow with Implementer validation support. No content
  repair remains.
- Commit/push are still gated by passing validation and explicit prior user
  authorization. No commit, push, PR mutation, merge, release, or tag occurs
  from this planning-artifact update.
- The exact implementation document set is `SKILL.md`, short `reference.md`,
  `examples.md`, and the three named files in `references/`; any extra tracked
  path needs plan repair.
- Generated inventory is canonical-skill completeness/hash evidence. It is
  never hand-edited and is regenerated exactly once after all six canonical
  documents are final.
- Human review remains the terminal automatic boundary after the patch push.
