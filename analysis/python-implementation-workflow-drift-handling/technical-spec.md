---
topic: python-implementation-workflow-drift-handling
status: READY FOR PLAN AUTHORING
baseline: analysis/python-implementation-workflow-drift-handling/requirements.md
created: 2026-05-15
updated: 2026-05-15
---

# Technical Specification: Python Implementation Workflow Drift Handling

## Baseline Summary

本 topic 要補齊 `.github/agents/python-implementation-workflow.agent.md` 與
`plan/agent-handoff-workflow.md` 對 medium / high severity drift 的處置契約，確保：

1. medium / high drift 不會被 ordinary `needs-rework` 靜默吞掉
2. correction artifact 依 severity 被正確要求
3. parent artifacts 最終回補為 current truth
4. correction artifacts 保留為 historical truth
5. human / workflow agent / planner / implementer 的權責在 correction path 中不混淆

---

## Requirement-to-Technical Mapping

| Requirement | Technical realization | Dependencies | Cost / burden | Status |
| --- | --- | --- | --- | --- |
| R1 Medium / High drift 不得 silent advance | 在 `.github/agents/python-implementation-workflow.agent.md` 新增全域 drift policy、impact-based trigger、provisional classification gate、planner confirmation gate | 現有 6-phase contract、`plan/agent-handoff-workflow.md` source-of-truth 規則 | 中：需修改 phase routing 語義，但不能破壞既有 ordinary rework 路徑 | feasible |
| R2 ordinary rework 與 correction-triggering drift 可區分 | 在 agent 與 workflow doc 中定義 impact-based decision rule；明確寫出哪些影響屬 correction-triggering drift | 已凍結 baseline 對 source-of-truth / public contract / architecture boundary / phase routing 的定義 | 低-中：主要是規則文字與 decision table | feasible |
| R3 correction artifact 依 severity 出現 | 在 agent 與 workflow doc 中定義 conditional required artifact pattern；明確保留 `*.correction-plan.md` / `*.correction-step.md` 命名 | topic-level file naming contract；後續 topic plan 必須列出 artifact paths | 中：需兼顧 artifact contract 與不把它變成 always-on workflow burden | feasible |
| R4 High severity = suspect code | 在 agent routing 中加入 high-severity branch，禁止把現有 implementation 當 ordinary patch baseline；要求 correction-plan + correction-step | Planner severity confirmation；review-triggered evidence | 低-中：主要是路由與 wording，不是執行程式邏輯 | feasible |
| R5 Parent artifacts 必須回補 current truth | 在 workflow doc 新增 parent-sync completion rule；在 agent 中加入 correction closure 前置檢查 | correction artifacts naming and sync-note rule | 中：需和 current source-of-truth contract 完整對齊 | feasible with prerequisites |
| R6 Correction artifacts 保留 historical truth | 在 workflow doc 與 agent 中定義 resolved / superseded allowed, deletion forbidden | repo-visible artifact retention policy | 低：規則明確即可 | feasible |
| R7 Role boundary 在 correction path 中保持清楚 | 在 agent 與 workflow doc 中分別標記：human signal、workflow provisional routing、planner final authority、implementer execution boundary | Roles table in `plan/agent-handoff-workflow.md` | 中：需避免與既有 reviewer / main-agent ownership 文義衝突 | feasible with prerequisites |
| R8 correction artifact 必須帶 parent sync note | 在 correction artifact policy 中規定最小 sync-note 欄位；agent / workflow doc 都需引用同一組欄位 | correction artifact pattern must be documented consistently in both files | 低-中：欄位定義與閉環規則 | feasible |

---

## Technical Tasks and Artifacts

### Workstream A — Update `.github/agents/python-implementation-workflow.agent.md`

**Scope**

- Keep the existing 6-phase structure.
- Add drift/correction semantics without turning ordinary `needs-rework` into a new human STOP POINT.

**Tasks**

1. Add a global `Implementation Drift / Human Correction Policy` section.
2. Define:
   - provisional vs final severity authority
   - impact-based correction trigger rule
   - the four routing states:
     - `IMPLEMENT_CONTINUE`
     - `IMPLEMENT_PATCH`
     - `PLANNER_CLARIFY`
     - `PLANNER_REPLAN`
3. Add a routing decision table mapping each state to:
   - trigger
   - owner
   - required artifact
   - next phase
   - acceptance condition
4. Add the Deviation / Correction Report format:
   - Markdown explanatory sections
   - fixed JSON Machine Verdict block
5. Update Phase 3 / 4 / 5 behavior so medium/high drift:
   - cannot silently advance
   - requires planner-confirmed severity
   - requires the severity-appropriate correction artifacts
6. Add closure rule:
   - planner closes correction only after required reviews pass
   - parent sync is complete

**Affected artifact**

- `.github/agents/python-implementation-workflow.agent.md`

### Workstream B — Update `plan/agent-handoff-workflow.md`

**Scope**

- Make the repo-level workflow contract explicitly compatible with the new correction semantics.

**Tasks**

1. Add canonical correction-layer semantics:
   - parent artifacts = current truth
   - correction artifacts = historical truth
2. Add severity-gated correction artifact rule:
   - low -> note only
   - medium -> correction plan, plus correction step when multi-step repair is required
   - high -> both correction artifacts, implementation treated as suspect code
3. Add parent-sync completion contract before correction closure.
4. Add retention rule:
   - resolved / superseded allowed
   - direct deletion forbidden
5. Ensure the new wording does not contradict:
   - source-of-truth rules
   - role ownership table
   - STOP POINT semantics
   - topic plan prerequisite rules

**Affected artifact**

- `plan/agent-handoff-workflow.md`

### Workstream C — Future topic-plan and implementation implications

This workstream is not implementation for the current change; it is the technical consequence surface that later execution must honor.

**Implications**

1. Later topic plans that introduce correction artifacts must list them explicitly in `Artifact paths`.
2. Later correction-capable workflows may need topic-level patterns such as:
   - `plan/<topic>/<topic>.correction-plan.md`
   - `plan/<topic>/<topic>.correction-step.md`
3. If long-term architecture governance wants the correction rules elevated beyond this workflow topic, a later ADR / workflow-policy topic is required.

**Status**

- out of current implementation scope
- tracked so current technical spec does not silently assume these follow-up surfaces away

---

## Dependency and Integration Notes

1. **Source-of-truth dependency**
   - The new correction policy must preserve `plan/agent-handoff-workflow.md` as the repo-level authority.
   - The custom agent may add detail, but not contradict repo-level semantics.
2. **Role-boundary dependency**
   - Planner final authority must fit the existing roles table.
   - The new wording must not accidentally move final closure authority to workflow agent or human chat.
3. **Topic-plan dependency**
   - Because topic plans currently define executable artifact paths, any later use of correction artifacts in real topics must be compatible with that contract.
4. **Worktree execution dependency**
   - This topic's repo-visible authoring and later implementation happen in:
     `/Users/andrew/code/python/agent-skills.worktrees/python-implementation-workflow-drift-handling`
   - base branch: `dev`
   - feature branch: `feat/andrew/python-implementation-workflow-drift-handling`
   - PR target branch: `dev`

---

## Architecture Compliance Self-Check

| Dimension | Result | Notes |
| --- | --- | --- |
| Repo-visible source of truth | **fits existing architecture** | Parent artifacts remain authoritative current truth; correction artifacts add history, not replacement authority |
| Role ownership model | **fits with prerequisites** | Feasible if wording keeps planner as final severity/closure authority and workflow agent as provisional router only |
| STOP POINT semantics | **fits existing architecture** | Ordinary `needs-rework` stays internal; correction handling does not add a new generic human STOP POINT |
| Topic plan artifact-path contract | **fits with prerequisites** | Future plans must explicitly list correction artifacts when they apply; this topic must not imply auto-created sidecars everywhere |
| Worktree execution preflight | **fits existing architecture** | Repo already requires explicit worktree execution preflight for PR-bound work |
| Parser / automation assumptions | **fits with prerequisites** | Safe for this topic if changes remain documentation/agent-contract only; if any tool later parses correction artifacts, that becomes a separate implementation surface |

---

## Cost-of-Realization Assessment

| Workstream | Complexity | Sequencing | Notes |
| --- | --- | --- | --- |
| Workstream A: custom agent update | Medium | 1 | Most of the behavior change lives here; high wording precision required because Phase 3/4/5 routing must stay coherent |
| Workstream B: repo workflow doc update | Medium | 1 | Must be updated in the same topic to avoid contradicting the custom agent |
| Cross-document consistency check | Medium | 2 | Required because the same policy will be described in two authoritative surfaces |
| Future topic-plan integration | Low-Medium | later topic | Not for this implementation, but future plans must explicitly carry correction artifact paths when used |
| Future ADR / workflow policy promotion | Low | optional later topic | Only needed if the correction rule becomes a long-term architecture rule beyond this workflow topic |

**Operational burden**

- Ongoing burden is moderate because maintainers must preserve current-vs-historical truth distinctions.
- Reviewer burden increases slightly because medium/high drift now requires checking correction-layer completeness, not only final content.

---

## Conflicts and Blockers

No blocking contradiction remains in the frozen business baseline. The main technical sensitivities are:

| Issue | Type | Handling |
| --- | --- | --- |
| correction artifacts accidentally become replacement source of truth | architecture conflict | keep parent/current truth rule explicit in both files |
| human correction phrasing sounds like direct override | source-of-truth risk | require planner-confirmed severity and repo-visible correction artifacts |
| future topic plans omit correction artifact paths | execution-contract drift | require later topic plans to list correction artifacts explicitly when used |
| future automation expects correction artifacts by default | scope creep | keep this topic document-only unless a later topic explicitly introduces parser/tooling support |

---

## Rollback Triggers

Roll back to alignment if any of these conditions become true during planning or implementation:

1. **Failing assumption**: correction artifacts can coexist with current topic-plan semantics without changing source-of-truth authority.
   - **Contradicting technical fact**: the proposed wording makes correction artifacts act like replacement parent plans.
   - **Required renegotiation**: decide whether correction artifacts are history-only or whether the repo wants a larger plan-contract redesign.
2. **Failing assumption**: planner remains final authority.
   - **Contradicting technical fact**: the draft wording lets workflow agent or human chat close correction without planner confirmation.
   - **Required renegotiation**: restate authority boundaries before implementation continues.
3. **Failing assumption**: this topic can stay limited to agent + workflow docs.
   - **Contradicting technical fact**: a safe implementation also requires parser / script / tool changes.
   - **Required renegotiation**: either expand scope explicitly or split a follow-up topic.
4. **Failing assumption**: ordinary `needs-rework` and correction-triggering drift remain distinguishable.
   - **Contradicting technical fact**: the implementation language cannot express the impact-based boundary clearly enough for another agent to apply it consistently.
   - **Required renegotiation**: refine the boundary rule before coding.

---

## What Is Intentionally Excluded

- creating or updating a topic plan in `plan/python-implementation-workflow-drift-handling/`
- editing `.github/copilot-instructions.md`, `README.md`, or `VERSION`
- adding parser/tooling support that machine-reads correction artifacts
- changing branch/worktree governance beyond the already approved execution preflight for this topic
