# CLI Workflow Alignment Plan

## Goal / Outcome

Create a repo-visible execution plan for a new CLI workflow alignment topic that
adds one repo agent plus one human-facing guide so this repository can use
Copilot CLI with less repeated context and clearer command routing. The
completed topic should produce a review-ready agent at
`.github/agents/workflow-gate.agent.md`, a guide at
`.github/guides/COPILOT-CLI-WORKFLOW.md`, and a small README discoverability
update that points users to the new guide without broadening the repository into
a generic CLI manual.

## Scope

- **In scope**:
  - create `.github/agents/workflow-gate.agent.md`
  - create `.github/guides/COPILOT-CLI-WORKFLOW.md`
  - update `README.md` to add one guide-table row for the new workflow guide
  - define one repo agent that reduces repeated reviewer / workflow-gate context
    for this repository's common Copilot CLI flows
  - document practical usage for `/pr`, `/review`, `/fleet`, and `/tasks`
  - document prompt-compression patterns that reduce repeated pasted context
    without hiding workflow-critical scope

- **Out of scope**:
  - changing `.github/copilot-instructions.md`
  - changing `plan/agent-handoff-workflow.md` or `.github/guides/MAIN-AGENT-WORKFLOW.md`
  - creating or revising any new or existing skill under `.github/skills/`
  - turning the repository into a general-purpose Copilot CLI documentation
    library
  - covering unrelated slash commands such as `/delegate`, `/research`, or
    `/mcp` in the first draft
  - changing `VERSION`, tags, or release notes in this topic

## Locked Decisions

- This topic is a **repo-guidance topic with declared README timing**, not a new
  stable-skill promotion topic.
- First-draft output is limited to one repo agent, one guide, and one README
  discoverability change.
- The repo agent name is locked to `workflow-gate`.
- The guide file name is locked to `COPILOT-CLI-WORKFLOW.md`.
- The agent's role is **entry-point orchestration**, not implementation review
  replacement:
  - it should reduce repeated workflow framing and route work into the correct
    existing skills or CLI flows
  - it must not replace `plan-reviewer`, `agent-skill-reviewer`, or git workflow
    skills as the canonical owner of their specialized decisions
- The guide's command coverage is locked to:
  - `/pr`
  - `/review`
  - `/fleet`
  - `/tasks`
- The guide must stay **scenario-first**, centered on this repo's observed
  workflows:
  - plan / workflow gate
  - review-ready validation
  - PR comment triage
  - post-merge follow-up
- README discoverability is included in this topic:
  - update the `## Guides` table during `publish-in-progress`
  - do not add the agent to `## Current skills`
- `VERSION` remains unchanged in this topic.

## Boundaries / Exclusions

- `workflow-gate.agent.md` owns reusable CLI entry framing for this repository;
  it does not own the repository's execution contract, which remains in
  `plan/agent-handoff-workflow.md`.
- `COPILOT-CLI-WORKFLOW.md` owns human-facing operational guidance and example
  prompt patterns for the selected CLI commands; it does not redefine skill
  folder policy, plan contract rules, or release governance.
- Existing specialized skills remain the canonical owners of their domains:
  - `plan-creator` and `plan-reviewer` own topic-plan authoring and review
  - `agent-skill-reviewer` owns skill-folder review
  - `git-post-merge-workflow` and `git-release-management` own their respective
    git and release flows
- If later work needs:
  - more slash commands than the locked set
  - agent examples for multiple personas
  - repo-wide instruction changes
  - guide coverage beyond this repository's workflow patterns
  then stop and split that into a separate topic.

## Status / Allowed Transitions

- **Current**: `merged`
- **Execution model**: follow the canonical creator -> reviewer -> publish ->
  merge path; this topic ends at `merged` with no separate Phase 10 release
  action.
- **Allowed transitions**:
  - `planned` -> `creator-in-progress`
  - `creator-in-progress` -> `review-ready`
  - `review-ready` -> `reviewer-in-progress`
  - `reviewer-in-progress` -> `approved`
  - `reviewer-in-progress` -> `needs-rework`
  - `needs-rework` -> `creator-in-progress`
  - `approved` -> `creator-in-progress`
  - `approved` -> `publish-in-progress`
  - `publish-in-progress` -> `pr-open`
  - `publish-in-progress` -> `merged`
  - `pr-open` -> `needs-rework`
  - `pr-open` -> `merged`
  - `merged` -> terminal

Routing notes:

- Use the standard Phase 4.5 planner-alignment checkpoint from
  `plan/agent-handoff-workflow.md`.
- If creator or reviewer drifts into workflow-spec editing, broad CLI feature
  documentation, or skill-authoring work, route back to `creator-in-progress`
  and repair scope before publish.

## Artifact Paths

| Artifact | Path | Owner | Role |
| --- | --- | --- | --- |
| Topic plan | `plan/cli-workflow-alignment/cli-workflow-alignment.plan.md` | Planning actor | Repo-visible execution contract for this topic |
| Repo agent | `.github/agents/workflow-gate.agent.md` | Creator | Reusable repo agent that reduces repeated workflow framing and routes work into the correct review / PR / follow-up path |
| CLI workflow guide | `.github/guides/COPILOT-CLI-WORKFLOW.md` | Creator | Human-facing guide for prompt compression and practical `/pr`, `/review`, `/fleet`, and `/tasks` usage in this repository |
| Guide discoverability | `README.md` | Main Agent | Add one `## Guides` row pointing readers to the new CLI workflow guide |

Artifact path notes:

- This topic does **not** modify `VERSION`, `.github/copilot-instructions.md`,
  `plan/agent-handoff-workflow.md`, `.github/guides/MAIN-AGENT-WORKFLOW.md`, or
  any existing skill folder.
- These paths are an executable contract.
- If later work tries to add more agents, more guides, extra repo docs, or other
  surfaces outside this set, stop and repair the plan or split the work into a
  separate topic.

## Stable library metadata

### README row

- Table: `## Guides`
- Exact row:

  `| \`COPILOT-CLI-WORKFLOW.md\` | practical Copilot CLI operating guide for workflow-gated prompting, reduced repeated context, and when to use \`/pr\`, \`/review\`, \`/fleet\`, and \`/tasks\` with the repo agent |`

- Position:
  - after `MAIN-AGENT-WORKFLOW.md`
  - before `REFERENCE-INTAKE-PROCESS.md`

### VERSION bump

- No change in this topic.
- Reason: this topic adds repo-local workflow guidance and a repo agent, but it
  does not add a new stable skill or require a repository release action.

### Timing

- README timing: `publish-in-progress`
- Reason: the PR should show the new guide together with the discoverability row
- Release action: no separate release action in this topic

### Additional release metadata

- Release notes artifact: none in this topic
- Tag action: none in this topic

## Implementation Steps

### Creator Phase (after plan approval)

1. Create `.github/agents/` if it does not already exist.
2. Draft `.github/agents/workflow-gate.agent.md` as one repo agent with:
   - frontmatter naming and description
   - clear trigger / when-to-use framing for workflow-gated repo work
   - explicit boundaries that defer specialized review and git decisions to the
     existing skills and workflow docs
   - guidance that reduces repeated context without suppressing artifact paths,
     scope, or required output formats
3. Draft `.github/guides/COPILOT-CLI-WORKFLOW.md` as a practical guide that
   covers:
   - when to use `/pr`
   - when to use `/review`
   - when to use `/fleet`
   - when to use `/tasks`
   - short prompt patterns for the repository's common workflow scenarios
   - when short follow-ups such as "請繼續" are enough and when explicit scope
     restatement is still required
4. Keep the guide scenario-first and repository-specific rather than turning it
   into a generic feature catalog.
5. Keep the new agent and guide aligned:
   - the guide should tell users when to invoke the repo agent
   - the agent should defer to the specialized skills and workflow docs named in
     the guide

### Reviewer Phase (after creator delivers review-ready)

1. Verify the topic stays within one repo-agent-plus-guide scope.
2. Verify `.github/agents/workflow-gate.agent.md` and
   `.github/guides/COPILOT-CLI-WORKFLOW.md` both exist at the locked paths.
3. Verify the guide explicitly and correctly covers `/pr`, `/review`, `/fleet`,
   and `/tasks`.
4. Verify the agent acts as an entry-point orchestrator and does not replace
   `plan-reviewer`, `agent-skill-reviewer`, or git workflow skills.
5. Verify the guide stays repository-specific and does not drift into broad
   Copilot CLI reference material.
6. Verify README / VERSION are still untouched before approval.

### Main Agent Publish Phase (after approval + planner alignment)

1. Update `README.md` with the exact locked `COPILOT-CLI-WORKFLOW.md` row at the
   locked position in `## Guides`.
2. Stage only the locked artifact set for this topic; do not stage unrelated
   files.
3. Open the PR with the agent file, guide file, and README discoverability
   change visible together.

## Validation / Acceptance Checks

- [ ] The topic plan remains valid at
  `plan/cli-workflow-alignment/cli-workflow-alignment.plan.md`.
- [ ] `Status / Allowed Transitions` uses canonical workflow transitions only.
- [ ] `Artifact Paths` remain exact and bounded to the listed repo-visible files.
- [ ] README intent is explicit and executable:
  - [ ] `README.md` row text is locked
  - [ ] timing is declared as `publish-in-progress`
  - [ ] `VERSION` is explicitly locked to no change
- [ ] Creator output is limited to:
  - [ ] `.github/agents/workflow-gate.agent.md`
  - [ ] `.github/guides/COPILOT-CLI-WORKFLOW.md`
- [ ] Main Agent publish output is limited to:
  - [ ] `README.md`
- [ ] The guide explicitly covers:
  - [ ] `/pr`
  - [ ] `/review`
  - [ ] `/fleet`
  - [ ] `/tasks`
- [ ] Agent / guide boundary integrity holds:
  - [ ] the agent reduces repeated context but does not hide workflow-critical
    scope
  - [ ] the agent does not replace specialized reviewer or git workflow skills
  - [ ] the guide stays scenario-first and repo-specific
  - [ ] no drift into workflow-spec editing or broad CLI feature reference
- [ ] Reviewer handoff remains a single machine-consumable JSON object.

## Reviewer Handoff

```json
{
  "verdict": "approved|needs-rework",
  "blocking_issues": [
    {
      "issue": "example",
      "file": "relative/path",
      "fix": "specific required correction"
    }
  ],
  "copilot_feedback_triage": {
    "ADDRESS": [
      {
        "comment": "required copilot feedback to apply",
        "location": "relative/path:line",
        "why": "why this feedback is required"
      }
    ],
    "DISCUSS": [
      {
        "comment": "optional or ambiguous feedback",
        "optional": true,
        "why": "why this is discussion-level only"
      }
    ],
    "SKIP": [
      {
        "comment": "feedback to skip",
        "why": "why this is not applicable"
      }
    ]
  }
}
```

## Post-merge / release actions

- At manual merge handoff, Main Agent must stop completely and wait for a new
  explicit human resume message; it must not keep polling or waiting in the
  background for merge completion.
- After a human explicitly resumes and merge is confirmed on GitHub, Main Agent
  performs normal post-merge local sync and marks the topic `merged`.
- No separate Phase 10 release action is required in this topic.
- Do not create a tag, release notes artifact, or version bump from this topic.

## Open Questions / Unresolved Items

- None. Current scope, artifact paths, README timing, and no-version decision are
  locked for first-draft execution.
