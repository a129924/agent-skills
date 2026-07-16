# step-creator Plan

> Semantic warning: `analysis/step-creator/requirements.md` 與 `analysis/step-creator/technical-spec.md` 均不存在。本計畫只以已凍結的使用者意圖、Planner baseline 與下列 repo-visible authority 建立單一 topic contract；這兩個缺少的 analysis artifact 不是本 topic 的 execution prerequisite，Creator 不得用推測補入額外語意。

## Goal

建立單一 `step-creator` Agent Skill。Caller 必須明確選擇 `base-plan`、`agent-skill-plan` 或 `python-implementation-plan` profile；skill 讀取 `plan/<topic>/<topic>.plan.md`，一次性產生對應且可供執行與追蹤的 `plan/<topic>/<topic>.step.md`。

## Non-Goal

- 不修改任何既有 planning、workflow、git、release、Python 或 Agent Skill authority。
- 不建立第四種 profile，也不自動猜測 profile。
- 不覆寫、合併、正規化、修復或更新已存在的 `*.step.md`。
- 不執行 plan、implementation、review、commit、push、PR、merge、release、tag 或 worktree 移除。
- 不把 `.github/**`、`.codex/**` 或其他 platform projection 當 canonical source。
- 不重開已凍結的 architecture、path、workflow、profile 或 contract decision。

## In-Scope

- 新增 canonical skill `skills/step-creator/` 及三個 caller-explicit profiles。
- 新增一個非 authority 的 shared lifecycle shell，為三個 profiles 提供固定 head、固定 tail 與條件 sentinel/substitute。
- Base/Agent profiles 產生固定 frontmatter、workflow table、fixed head、由 exact source actor/action 抽取的 contextual actions、Implementation Steps、fixed tail 與 handoff fields。
- Python profile 保留 canonical Python step template 的 exact frontmatter、executor note、六階段名稱與順序；它是 adapter，於 fixed head 與 Implementation Steps 間固定產生 profile-owned collective contextual action，並不要求或新增 Base/Agent status/actor/action source-plan contract，再接入共用 fixed head/tail。
- 實作 profile eligibility preflight、evidence-based `[X]` / `[ ]`、exact one-to-one Implementation Step mapping、collective contextual-action dedup、existing-output BLOCKED 與 whole-file/rendered-section tracker semantics。
- 固定同一 managed topic worktree selector、attached topic branch selector 與 path intent，貫穿 planned fixed head 到 execution-time fixed tail cleanup；初始 generation 不要求 worktree 已存在。
- 提供 reference、examples、checklist 與 topic planning artifacts。

## Out-Of-Scope

- 上游 workflow/contract/skill 對齊寫入。
- projection 產生、同步或 migration。
- runtime agent registry、workflow-to-agent binding 或 orchestration semantics。
- 修改 README、VERSION 或進行 release。
- 自動發現 profile、自動修正 source plan 或推導未聲明的 release branch。
- 以 primary worktree 取代或冒充 managed topic worktree。
- 任何未列於 `Written` 的 repo 檔案修改。

## ReadOnly

| Exact path | Owner | Role in this topic |
| --- | --- | --- |
| `AGENTS.md` | Repository governance | Canonical source/projection boundary authority |
| `plan/agent-handoff-workflow.md` | Repo workflow contract | Workflow states, roles, STOP POINT 1/2 and post-merge boundaries |
| `plan/topic-plan-contract.md` | Topic-plan contract | Required plan sections, artifact-path and reviewer-handoff contract |
| `skills/worktree-manager/SKILL.md` | worktree-manager | Managed topic worktree lifecycle behavior authority |
| `skills/worktree-manager/checklist.md` | worktree-manager | Managed worktree identity and validation evidence rules |
| `skills/worktree-manager/reference.md` | worktree-manager | Managed worktree create/get/inventory/remove reference |
| `skills/git-branch-naming/SKILL.md` | git-branch-naming | Attached topic-branch naming and preparation contract |
| `skills/plan-step-tracker/SKILL.md` | plan-step-tracker | Whole-file and Implementation-only query behavior authority |
| `skills/plan-step-tracker/reference.md` | plan-step-tracker | Checkbox format, section scope and marker semantics authority |
| `skills/plan-step-tracker/scripts/step_tracker.py` | plan-step-tracker | Exact rendered-checkbox parser behavior |
| `skills/git-commit-convention/SKILL.md` | git-commit-convention | Commit preparation/message contract |
| `skills/git-post-merge-workflow/SKILL.md` | git-post-merge-workflow | Post-merge sync and managed cleanup contract |
| `skills/git-post-merge-workflow/references/stop-point-2-checklist.md` | git-post-merge-workflow | Exact STOP POINT 2 resume evidence |
| `skills/git-release-management/SKILL.md` | git-release-management | Release/tag gate authority |
| `skills/git-release-management/references/gate-contract.md` | git-release-management | Release gate ordering and blocking contract |
| `skills/git-release-management/references/version-sources.md` | git-release-management | Dynamic version-source inventory contract |
| `skills/git-release-management/references/version-bump-guidance.md` | git-release-management | Version update guidance |
| `skills/python-plan-authoring/SKILL.md` | python-plan-authoring | Python plan/step co-artifact, 13-section and six-stage contract |
| `skills/python-plan-authoring/templates/python-plan-template.md` | python-plan-authoring | Python plan section source contract |
| `skills/python-plan-authoring/templates/step-template.md` | python-plan-authoring | Exact Python step scaffold |
| `skills/python-plan-review/SKILL.md` | python-plan-review | Python plan-review behavior |
| `skills/python-plan-review/checklist.md` | python-plan-review | Python plan completeness checks |
| `skills/agent-skill-creator/SKILL.md` | agent-skill-creator | Single bounded Agent Skill creator behavior |
| `skills/agent-skill-creator/blueprint.md` | agent-skill-creator | Agent Skill content blueprint |
| `skills/agent-skill-creator/folder-contract.md` | agent-skill-creator | Canonical Agent Skill folder/file contract |
| `skills/agent-skill-reviewer/SKILL.md` | agent-skill-reviewer | Independent Agent Skill review behavior |
| `skills/agent-skill-reviewer/review-checklist.md` | agent-skill-reviewer | Agent Skill review-ready checklist |
| `README.md` | Stable-library documentation | Read-only evidence that this topic declares no README update |
| `VERSION` | Repository release baseline | Read-only current version-source evidence; not a cross-repo hardcode |

## Written

| Exact path | Owner | Role in this topic |
| --- | --- | --- |
| `plan/step-creator/step-creator.plan.md` | Planning actor | Current topic execution contract |
| `plan/step-creator/step-creator.step.md` | Planning actor | Topic progression artifact derived from this plan |
| `skills/step-creator/SKILL.md` | step-creator Creator | Public trigger, profile eligibility, inputs, blocking behavior, routing and generation procedure |
| `skills/step-creator/reference.md` | step-creator Creator | 只包含三個共用主題：generation/eligibility、evidence/tracker、lifecycle rendering；詳細規則由 SKILL、template、profile references 與 examples 擁有 |
| `skills/step-creator/examples.md` | step-creator Creator | Positive and blocking examples for profiles, eligibility and conditional branches |
| `skills/step-creator/checklist.md` | step-creator Creator | Preflight and output validation checklist |
| `skills/step-creator/templates/shared-lifecycle-shell.md` | step-creator Creator | Non-authoritative fixed head/tail and sentinel/substitute rendering template |
| `skills/step-creator/references/base-plan-profile.md` | step-creator Creator | Exact Base eligibility, output wire and source mapping |
| `skills/step-creator/references/agent-skill-plan-profile.md` | step-creator Creator | Exact Agent Skill eligibility, output wire and contextual mapping |
| `skills/step-creator/references/python-plan-authoring-adapter.md` | step-creator Creator | Exact Python eligibility/scaffold adapter and shared-shell insertion contract |

## Deleted

None.

## TestCase

1. Explicit `base-plan` with an eligible source and missing output generates the frozen Base wire.
2. Explicit `agent-skill-plan` with an eligible single-skill source and missing output generates the frozen Agent wire.
3. Caller explicitly selects `python-implementation-plan`; a source that describes Python implementation work and satisfies the canonical Python plan contract generates the frozen Python wire even if the source contains no literal profile-name marker.
4. Missing, unknown, ambiguous or inferred caller profile returns BLOCKED without writing.
5. Missing/unreadable source plan returns BLOCKED without writing.
6. Existing output returns BLOCKED without overwrite, merge, normalization, repair or partial write.
7. Base eligibility accepts only a canonical topic plan with all required sections, no Agent/Python specialized claim, one current status, explicit allowed transitions, exact next actor/action and exact top-level Implementation Steps.
8. Base missing/ambiguous/mismatched status, transition, actor, action, Implementation Steps or specialized-profile claim returns BLOCKED.
9. Agent eligibility accepts only Base shared progression inputs plus one explicit bounded Agent Skill responsibility, canonical exact `skills/<skill-name>/...` outputs, creator/reviewer separation and review-ready-not-approved handoff.
10. Agent generic/multiple-skill intent, projection-only path, ownership ambiguity, approved-as-creator handoff or profile mismatch returns BLOCKED.
11. Python eligibility rejects non-Python intent, an incomplete or ambiguous canonical 13-section/async/test/validation contract, existing output or caller/source incompatibility; it does not require a literal `python-implementation-plan` string or Base/Agent status/actor/action fields in source.
12. Base/Agent frontmatter contains exactly `topic`, `step_profile`, `source_plan`, `created` in frozen order.
13. Base/Agent output section order exactly matches the frozen wire.
14. Base/Agent `Workflow Stages` table contains `Current status`, `Allowed next transitions`, `Next actor`, with exact source fidelity.
15. Every source Implementation Step maps one-to-one, verbatim and in order to one rendered checkbox; no extra dynamic Implementation Step is invented.
16. Base/Agent contextual actions retain `**Actor:** … — **Action:** …` form, source wording, order and evidence marker.
17. Base/Agent only: exact duplicate actions explicitly collective/shared are deduplicated; non-identical actions and all Implementation Steps remain separate.
18. Exact repo-visible one-to-one completion evidence renders `[X]`; pending or merely planned work renders `[ ]`.
19. Read-only source `[x]` never counts as completion; generated marker is `[ ]` and a warning is emitted.
20. Partial/progress evidence that cannot map one-to-one returns BLOCKED.
21. Initial generation before any topic worktree exists is valid and renders `create-worktree`, `prepare-topic-branch`, slot 22 inspection, slot 23 approval and slot 24 removal as `[ ]`, with one exact topic selector, branch selector and managed-path intent carried consistently.
22. Fixed head order is managed `create-worktree` then `prepare-topic-branch`, before contextual/dynamic middle.
23. `create-worktree` is `[X]` only when exact evidence proves the selected managed topic worktree and attached selected topic branch now exist; primary worktree evidence never satisfies it.
24. If `create-worktree` is claimed `[X]` but the selected managed worktree/attached branch is absent or conflicts with evidence, update/query/execution is BLOCKED.
25. STOP POINT 1 renders before commit, push and PR creation.
26. STOP POINT 2 renders as human-merge handoff and requires a complete stop before merge follow-up.
27. Human merge and new explicit resume are evidence/handoff actions, never creator-owned Implementation Steps.
28. Slot 12 renders exactly one of remote delete action or `remote-retained`, never both.
29. Slot 13 always renders the release-resolution checkbox; no-release exact evidence renders `[X] Determine release requirement — release not required`.
30. With that no-release resolution, slots 14–21 are replaced by the single exact `release-not-applicable` sentinel and create no omitted or pending release-resolution checkbox.
31. Unknown release applicability returns BLOCKED rather than choosing a branch.
32. Release-required rendering keeps slots 14–21 in order and requires release commit/push before tag approval/tag creation/tag push.
33. Empty authoritative version inventory in a release-required branch substitutes exact `[X] tag-only — no authoritative version source discovered` at slot 15.
34. Multiple authoritative version sources require synchronized updates; dirty/conflicting versions or an existing conflicting tag blocks tag work.
35. Slot 16 renders README update or exact `README-not-required`, supported by stable metadata or an explicit non-stable/no-README declaration.
36. Exact human tag approval is required before annotated tag creation and tag push.
37. Tail slots 22–24 remain `[ ]` until execution proves the same selected managed topic worktree/branch identity and clean/release evidence, records exact destructive approval, removes that worktree and verifies removal in order.
38. After fixed-head completion, cleanup/update execution is BLOCKED by absent selected worktree, identity ambiguity/conflict, primary-worktree target, dirty/unresolved state, missing approval or failed removal; normal pre-worktree initial generation is not BLOCKED.
39. Slot 25 local topic branch deletion occurs only after verified selected managed worktree removal.
40. `check_all_succeeded` for Base/Agent evaluates every rendered checkbox in fixed head, contextual actions, Implementation Steps and fixed tail.
41. `check_all_succeeded` for Python evaluates those same rendered regions plus all six `Workflow Stages` checkboxes.
42. `check_impl_steps_succeeded` for every profile evaluates exactly the `## Implementation Steps` checkbox entries and no other section.
43. A pending Python Workflow Stage makes `check_all_succeeded` false while all-complete Python Implementation Steps still make `check_impl_steps_succeeded` true.
44. Replaced/omitted release slots create no phantom pending checkbox.
45. `merged` or `released` never implies topic-close; final verification records close-semantics evidence separately.
46. Python output retains exact three-key frontmatter, exact executor note, all six canonical stages in order, and the fixed profile-owned contextual action before Implementation Steps.
47. Python contextual action renders exactly `**Actor:** Creator — **Action:** Complete source ## Implementation Steps in order.` with its evidence marker; it is adapter behavior, not source actor/action extraction or a new Python source-plan contract.
48. All writes stay inside the exact `Written` set; no upstream authority or platform projection is modified.
49. Validation detects section-order, path-set, owner, eligibility, caller profile, source intent, worktree selector/evidence phase, slot-order, sentinel/substitute, marker, tracker-scope or evidence-field drift.

## Goal / Outcome

This canonical outcome binds `## Goal`: one review-ready `step-creator` skill must deterministically generate exactly one eligible, caller-selected profile-specific progression artifact from one source topic plan, with fixed lifecycle gates, a consistently selected managed topic worktree lifecycle and evidence-truthful tracking. Success means the complete `Written` set satisfies this contract without changing any read-only or excluded surface.

## Scope

This canonical scope binds `## In-Scope` and `## Out-Of-Scope` exactly. Only the `Written` paths and behaviors enumerated in `## In-Scope` may be created; all `## Out-Of-Scope` behavior, every read-only dependency, every projection surface and every unlisted path remain excluded.

## Locked Decisions

### Invocation, eligibility and blocking contract

- Input source is exactly `plan/<topic>/<topic>.plan.md`; output is exactly `plan/<topic>/<topic>.step.md`.
- Caller explicitly passes exactly one profile: `base-plan`, `agent-skill-plan`, or `python-implementation-plan`. Content sniffing, fallback selection and inference are forbidden.
- Output creation is atomic and create-only. Existing output returns `BLOCKED: output already exists`; do not overwrite, merge, normalize, repair, truncate or partially write.
- Missing/unreadable source, invalid topic/path, unsupported caller profile, profile-ineligible source, unresolved release branch, unmappable progress or contradictory evidence returns BLOCKED before write.
- Absence of a managed topic worktree during normal initial generation is not a blocker; fixed head and tail worktree actions render pending with exact selectors/path intent.

Base eligibility is exact:

- Source has every canonical `plan/topic-plan-contract.md` required section.
- Source makes no specialized Agent Skill or Python implementation claim.
- Source declares exactly one unambiguous current status.
- Source declares explicit allowed transition(s) from that current status, each matching `plan/agent-handoff-workflow.md`.
- Source declares one exact next actor and one exact stage-local next action consistent with status/transition.
- Source has one exact top-level `## Implementation Steps` section with executable items.
- Extraction preserves status, transition, actor and action wording; step-creator does not repair, choose, reinterpret or synthesize them.
- Missing, multiple, ambiguous, contradictory or mismatched data; absent/duplicate/nested-only Implementation Steps; or Agent/Python specialized intent makes Base BLOCKED.

Agent eligibility is exact:

- Source satisfies Base shared progression inputs: canonical sections, one status, explicit valid transitions, exact next actor, exact stage-local action and one top-level Implementation Steps section.
- Source declares exactly one bounded Agent Skill name and single responsibility.
- Creator output paths are exact canonical repo-visible paths under `skills/<skill-name>/...`; projection-only paths are ineligible.
- Source separates Creator from independent Reviewer and hands off at `review-ready`, never creator-asserted `approved`.
- Generic/multiple skills, projection-only output, ambiguous ownership, creator/reviewer collapse, review-ready/approved mismatch or caller/source incompatibility makes Agent BLOCKED.
- Status, transition, actor, action, paths, responsibility and handoff wording are extracted faithfully.

Python eligibility is exact:

- Caller, not the source, explicitly selects `python-implementation-plan`.
- Source does not need and must not be required to contain a literal `python-implementation-plan` marker or profile-name claim.
- Source must explicitly describe bounded Python implementation work and satisfy the canonical `python-plan-authoring` 13-section contract, including its async-planning status/trigger-or-exemption requirements, triggered async subsections when applicable, one exact top-level `## Implementation Steps`, five-category Test Plan and explicit Validation Commands/config reference. It does not need Base/Agent current-status, next-actor or stage-local-action fields.
- Python generation is BLOCKED only for non-Python intent, an incomplete/ambiguous/contradictory canonical Python contract, existing output, or incompatibility between caller-selected Python profile and source intent/shape.
- `python-plan-authoring` remains authority; adapter validation does not redefine it.

The skill owns generation only. Later marker updates are actor-owner actions backed by exact evidence.

### Marker, evidence and tracker contract

- `[M]` is a template metavariable only. Every generated checkbox substitutes uppercase `[X]` or `[ ]`; literal `[M]` never appears.
- `[X]` requires exact repo-visible one-to-one completion evidence. Planned, pending or unproved work is `[ ]`.
- Lowercase source `[x]` is pending input, not completion; output marker is `[ ]` plus warning. Source is never modified.
- Partial/unmappable evidence returns BLOCKED.
- Initial generation may legitimately have no worktree evidence: all head/tail worktree lifecycle items remain `[ ]`; absence alone does not block.
- Base/Agent `check_all_succeeded` covers every rendered checkbox in fixed head, contextual actions, Implementation Steps and fixed tail.
- Python `check_all_succeeded` covers those regions plus all six Workflow Stages.
- All profiles' `check_impl_steps_succeeded` covers exactly entries inside `## Implementation Steps`.
- Release replacement contributes only the checkbox rendered; omitted/replaced slots create no pending work.

### Exact Base/Agent output wire

Both `base-plan` and `agent-skill-plan` use this literal order/shape:

```markdown
---
topic: <topic>
step_profile: <base-plan|agent-skill-plan>
source_plan: plan/<topic>/<topic>.plan.md
created: YYYY-MM-DD
---

# <topic> — Step Tracking

## Workflow Stages

| Current status | Allowed next transitions | Next actor |
| --- | --- | --- |
| <exact source-plan status> | <exact canonical allowed transition(s)> | <exact source-plan next actor> |

## Actionable Steps

### Main Agent — Fixed Head

- [M] **Actor:** Main Agent — **Action:** create-worktree — **Selector:** topic=<topic>; branch=<exact topic-branch selector>; managed-path-intent=<worktree-manager path intent>
- [M] **Actor:** Main Agent — **Action:** prepare-topic-branch — **Selector:** same topic, branch and managed-path intent

### Contextual Actions

- [M] **Actor:** <source actor> — **Action:** <preserved contextual/stage-local action>

## Implementation Steps

- [M] 1. <source Implementation Step 1, verbatim>
- [M] 2. <source Implementation Step 2, verbatim>

## Main Agent Actionable Steps — Fixed Tail

<rendered fixed-tail actions and conditional sentinel/substitute in locked order; slots 22–24 repeat the same selector/path intent>

## Handoff / Gate Notes

- Selected profile: <base-plan|agent-skill-plan>
- Source plan: plan/<topic>/<topic>.plan.md
- Shared lifecycle shell: skills/step-creator/templates/shared-lifecycle-shell.md
- Managed worktree intent: topic=<topic>; branch=<exact topic-branch selector>; managed-path-intent=<worktree-manager path intent>; primary-worktree=false
- Progression truth inputs: <exact repo-visible source plan and any source-declared progression/review/summary paths used>
- Completion evidence inputs: <exact repo-visible artifact paths and/or exact command, PR, merge, release, tag or worktree evidence used for markers>
- Marker semantics: `[X]` exact one-to-one evidence; `[ ]` pending/planned/unproved; lowercase source `[x]` is pending and warns.
- Tracker semantics: `check_all_succeeded` covers rendered head/contextual/Implementation/tail checkboxes; `check_impl_steps_succeeded` covers only Implementation Steps.
- Owner-only updates: only action owner may update after exact evidence; step-creator never updates existing output.
```

- Topic selector is exact `<topic>`. Branch selector and managed-path intent are exact governed selector inputs carried from an explicit source value when present, otherwise from fixed `git-branch-naming`/`worktree-manager` shell contract; they are planned selectors, not a false existence claim.
- Same selector tuple repeats at head, tail 22–24 and Handoff; competing tuples BLOCK generation.
- Mirror every top-level Implementation Step exactly once, verbatim and ordered. Context/reviewer/Main Agent/release/human actions stay outside.
- Contextual actions preserve source order and exact Actor/Action wording.
- Collective dedup only for explicitly collective/shared exact Actor+Action duplicates; preserve first and all source headings in progression note. No near-duplicate normalization or Implementation dedup.
- Progression/completion inputs contain exact paths/identifiers, never hidden memory/chat/vague process.

### Exact Python output wire

Python preserves canonical scaffold and adds a fixed adapter-owned collective contextual action:

```markdown
---
topic: <topic>
phase: plan-authoring
created: YYYY-MM-DD
---

# <topic> — Step Tracking

> **Executor**: Mark each step `[X]` when complete.
> All Implementation Steps must be `[X]` before submitting for `python-implementation-review`.
> Update this file at: `plan/<topic>/<topic>.step.md`

## Workflow Stages

- [M] plan-authoring
- [M] plan-review
- [M] tdd-test-authoring
- [M] implementation
- [M] implementation-review
- [M] code-review

## Actionable Steps

### Main Agent — Fixed Head

- [M] **Actor:** Main Agent — **Action:** create-worktree — **Selector:** topic=<topic>; branch=<exact topic-branch selector>; managed-path-intent=<worktree-manager path intent>
- [M] **Actor:** Main Agent — **Action:** prepare-topic-branch — **Selector:** same topic, branch and managed-path intent

### Contextual Actions

- [M] **Actor:** Creator — **Action:** Complete source ## Implementation Steps in order.

## Implementation Steps

- [M] 1. <source Implementation Step 1, verbatim>
- [M] 2. <source Implementation Step 2, verbatim>

## Main Agent Actionable Steps — Fixed Tail

<rendered fixed-tail actions and conditional sentinel/substitute in locked order; slots 22–24 repeat the same selector/path intent>

## Handoff / Gate Notes

- Selected profile: python-implementation-plan
- Source plan: plan/<topic>/<topic>.plan.md
- Shared lifecycle shell: skills/step-creator/templates/shared-lifecycle-shell.md
- Managed worktree intent: topic=<topic>; branch=<exact topic-branch selector>; managed-path-intent=<worktree-manager path intent>; primary-worktree=false
- Progression truth inputs: <exact repo-visible source plan and any source-declared progression/review/summary paths used>
- Completion evidence inputs: <exact repo-visible artifact paths and/or exact command, PR, merge, release, tag or worktree evidence used for markers>
- Marker semantics: `[X]` exact one-to-one evidence; `[ ]` pending/planned/unproved; lowercase source `[x]` is pending and warns.
- Tracker semantics: `check_all_succeeded` covers six stages plus rendered head/contextual/Implementation/tail; `check_impl_steps_succeeded` covers only Implementation Steps.
- Owner-only updates: only action owner may update after exact evidence; step-creator never updates existing output.
```

- Six stages remain exactly `plan-authoring`, `plan-review`, `tdd-test-authoring`, `implementation`, `implementation-review`, `code-review` in order.
- Stage `[X]` requires exact completion evidence, otherwise `[ ]`.
- Contextual Actions is fixed profile-owned adapter behavior: it renders exactly `**Actor:** Creator — **Action:** Complete source ## Implementation Steps in order.` with its evidence marker. It does not extract or validate source status, actor or action, and does not add a Python source-plan contract.
- Python Implementation Steps mirror one-to-one, verbatim and ordered; existing output remains BLOCKED.
- Pending stage blocks all-gate even when all Implementation Steps are `[X]`, but not implementation-only gate.
- Same planned selector tuple/fidelity rules apply; initial lack of resolved worktree evidence is valid and renders lifecycle actions `[ ]`.
- Source profile-name text is neither required nor used as eligibility evidence; caller selection plus source Python intent/canonical contract are authoritative for routing.

### Shared lifecycle shell, planned selector and exact tail

- `skills/step-creator/templates/shared-lifecycle-shell.md` is the only shared shell for all profiles and is not authority.
- At generation time it freezes one exact selector tuple: topic, governed topic-branch selector and managed worktree path intent. This does not assert an existing worktree.
- Fixed head renders create/reuse selected managed topic worktree, then prepare/attach selected branch. Without current evidence both are `[ ]`; generation continues.
- `create-worktree` becomes `[X]` only when exact inventory proves selected managed worktree and selected attached branch. Claimed-X conflict or selector ambiguity during update/execution BLOCKS.
- Base/Agent dynamic middle remains source/Creator/Implementer owned and source-extracted; Python uses the fixed profile-owned collective contextual action. Fixed head/tail remain Main Agent-owned; human merge/resume remain handoff/evidence only.
- Tail logical slots:

1. validation and bounded staging
2. STOP POINT 1
3. commit
4. push
5. open PR
6. review/observe PR
7. STOP POINT 2 human-merge handoff and complete stop
8. record exact human merge evidence
9. require new explicit human resume
10. verify merged
11. fast-forward-only target/default sync
12. remote branch delete/retain resolution
13. release/no-release resolution
14. dynamic version-source inventory
15. required version updates, or tag-only substitution
16. README update/not-required resolution
17. release commit
18. release push
19. exact human approval for exact tag create and push
20. annotated tag creation
21. tag push
22. inspect selected managed topic worktree and prove clean/release evidence
23. obtain exact destructive approval to remove selected managed topic worktree
24. remove selected managed topic worktree and verify removal
25. delete local topic branch after verified removal
26. final verification and close-semantics evidence

- Normal actions use `- [M] **Actor:** Main Agent — **Action:** <action>` and worktree entries carry selector; completed conditional lines retain frozen form.
- STOP1 precedes commit/push/PR; STOP2 precedes merge follow-up and stops; release commit/push precede tag approval; approval precedes tag create/push; slots22/23 precede removal; verified removal precedes local deletion; merged/released is not closed.
- Initial slots22–24 are planned `[ ]` even without worktree. After head completion, cleanup requires same identity/evidence; absence, conflict/ambiguity, primary target, dirty state, missing approval or failed removal BLOCKS. Tail stays pending until own evidence.

### Conditional substitution and tracker contract

- Slot12 renders remote delete action or exactly:
  `- [X] remote-retained — source plan or retention policy requires keeping the remote branch`
- Slot13 always renders release resolution. Exact no-release evidence renders:
  `- [X] Determine release requirement — release not required`
  and replaces slots14–21 with:
  `- [X] release-not-applicable — source plan declares terminal at merged`
  Replaced slots are absent; no pending release-resolution checkbox remains. Unknown/contradictory applicability BLOCKS.
- Release slot14 inventories version sources dynamically; VERSION is current evidence only. Empty inventory substitutes slot15:
  `- [X] tag-only — no authoritative version source discovered`
  One source updates; multiple synchronize. Tag/version/dirty conflict blocks progression.
- Release slot16 renders README update or:
  `- [X] README-not-required — stable-library metadata or explicit non-stable/no-README declaration requires no README change`
  Unknown/contradictory applicability BLOCKS.
- Conditional sentinels are remote-retained, release-not-applicable, README-not-required; tag-only is slot15 substitute. No worktree sentinel.
- Base/Agent all-gate counts head/context/Implementation/tail; Python also stages. Release substitute counts once; replaced slots absent. Impl gate only Implementation.
- No conditional `[X]` without evidence.

### Topic status and stable-surface decision

- Topic becomes planned after repo-visible plan/progression artifacts. It is non-stable-library work.
- README/VERSION read-only. No release/tag; merged terminal but not automatically closed.

## Boundaries / Exclusions

- Canonical implementation only `skills/step-creator/`; platform projections unwritten.
- No unlisted path changes; repair/re-review if needed.
- ReadOnly unmodified; no invented `skills/python-plan-authoring/checklist.md`.
- Shared shell cannot override authorities.
- Primary worktree preserved and never selected/removal target.
- Planned selector does not mean existence/completion.
- No upstream alignment, projection, migration, registry, binding, orchestration, release or architecture reopening.
- Creator Implementation excludes reviewer/Main Agent/human/publishing/release/worktree cleanup.

## Status / Allowed Transitions

| Current status | Entry condition | Allowed next | Owner / stop rule |
| --- | --- | --- | --- |
| `planned` | Valid plan/progression exist; worktree may be pending | `creator-in-progress` | Planning handoff |
| `creator-in-progress` | Locked plan and governed worktree/branch setup satisfied for execution | `review-ready` | Exact Written implementation |
| `review-ready` | Creator validation/handoff complete | `reviewer-in-progress` | Independent reviewer |
| `reviewer-in-progress` | Latest draft available | `approved`, `needs-rework` | One JSON object |
| `needs-rework` | Blockers listed | `creator-in-progress` | Independent repair |
| `approved` | Draft accepted | `creator-in-progress`, `publish-in-progress` | Main Agent alignment |
| `publish-in-progress` | Approval/alignment/STOP1 | `pr-open`, `merged` | Main Agent publishing |
| `pr-open` | PR exists | `needs-rework`, `merged` | Review/human merge |
| `merged` | Merge evidence and explicit post-STOP2 resume | terminal | No release; not closed automatically |

STOP1 blocks commit/push/PR. STOP2 requires stop and new explicit resume.

## Artifact Paths

Exact executable paths are union of ReadOnly, Written, Deleted with listed owner/role. No wildcard, hidden artifact or implicit extra.

## Implementation Steps

1. Create `skills/step-creator/SKILL.md` with explicit caller profiles, per-profile eligibility/fidelity preflight, create-only behavior, evidence phases, marker/tracker rules, shared-shell routing and blockers.
2. Create `skills/step-creator/templates/shared-lifecycle-shell.md` with selector/path intent, pending initial worktree lifecycle, evidence updates, 26-slot tail, three sentinels/tag-only, release ranges and tracker scope.
3. Create `skills/step-creator/references/base-plan-profile.md` with Base eligibility, wire, extraction fidelity, contextual dedup and mapping.
4. Create `skills/step-creator/references/agent-skill-plan-profile.md` with single-skill eligibility, canonical paths/ownership/handoff and wire/context mapping.
5. Create `skills/step-creator/references/python-plan-authoring-adapter.md` with caller-selected routing, Python-intent plus canonical-contract eligibility without source profile marker, exact scaffold/six stages, Contextual Actions, tracker distinction and shell insertion.
6. Create `skills/step-creator/reference.md` with exactly three coherent shared topics: generation/eligibility, evidence/tracker, and lifecycle rendering. Keep detailed rules in `SKILL.md`, the shared template, the profile references and examples.
7. Create `skills/step-creator/examples.md` with valid profiles including Python source without literal profile marker; blockers for non-Python/incomplete/ambiguous Python source, invalid caller profile, existing output, extraction mismatch, lowercase x, unmappable progress, unknown release, claimed-X conflict, cleanup ambiguity; valid pending generation, release substitutions and Python tracker split.
8. Create `skills/step-creator/checklist.md` covering paths, eligibility, create-only, wires, Python source-intent/canonical-contract test, contextual mapping, worktree phases, tail, release substitution, trackers, projections and handoff.

## Validation / Acceptance Checks

- Verify exact Written only; ReadOnly unchanged; no projection write.
- Validate all 49 TestCases with checklist and bounded fixtures/examples.
- Base fixtures cover eligibility and status/transition/actor/action/section blockers.
- Agent fixtures cover one responsibility, canonical outputs, separation, review-ready and mismatch blockers.
- Python fixtures: caller explicitly selects Python; source clearly describes Python implementation and satisfies exact 13-section, async decision/subsections as applicable, five test categories and validation contract; one valid source contains no literal profile-name, current-status, next-actor or stage-local-action field and must pass. Non-Python, incomplete/ambiguous contract, existing output and true caller/source incompatibility must block.
- Assert exact Python frontmatter/executor/six stages/order, the fixed profile-owned contextual action before Implementation, and tracker split.
- Assert Base/Agent contextual preservation/dedup; assert Python does not extract contextual status/actor/action from source.
- Initial no-worktree fixture succeeds with consistent selector and pending head/tail; evidence fixture permits X; conflict fixture blocks.
- Cleanup execution fixtures block absent/ambiguous/wrong/primary/dirty/missing-approval/failure after head completion; tail pending until evidence; deletion waits.
- Assert tail release: slot12 exclusive; no-release renders completed slot13 `Determine release requirement — release not required` plus the sentinel replacing14–21; release renders the required range, tag-only15, README16, and no no-worktree sentinel.
- Assert `reference.md` contains only the three shared topics; detailed profile/template/example rules remain in their owning artifacts.
- Run tracker interface: Base/Agent all counts head/context/Implementation/tail; Python adds stages; impl only Implementation. Pending Python stage + complete Implementation => all false, impl true.
- Assert no phantom pending, lowercase input warning, unmappable block and evidence-only X.
- Assert existing destination unchanged/no temp on BLOCKED.
- Independent Agent Skill review and Plan-Reviewer approval required; no self-approval.

## Reviewer Handoff

Independent Plan-Reviewer returns exactly one object, no prose:

```json
{
  "verdict": "approved|needs-rework",
  "blocking_issues": [],
  "copilot_feedback_triage": {
    "ADDRESS": [],
    "DISCUSS": [],
    "SKIP": []
  }
}
```

Scope/contract/workflow drift, unlisted path, hidden-context dependency, caller/source incompatibility, extraction mismatch, false evidence, worktree phase confusion, wrong tracker scope, unresolved release execution branch or ownership mixing is blocking. Absence of a literal Python profile marker is explicitly not blocking.

## Post-merge / release actions

- Topic non-stable/no-README/no-VERSION.
- Initial generation may precede worktree. Before Creator execution, fixed head establishes selected managed worktree/branch with evidence.
- After merge/new resume, Main Agent verifies, FF-syncs, resolves remote, then same selected worktree for clean evidence, approval, removal, local branch deletion and final close evidence.
- Primary preserved. Cleanup-time absent/ambiguous/conflicting identity, dirty state, missing approval or failure blocks, without invalidating initial generation.
- No release/tag. release-not-applicable needs terminal-at-merged evidence.
- Merged terminal for release, not proof of close.

## Open Questions / Unresolved Items

None.
