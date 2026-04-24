# Reference Intake Process

This document defines the canonical **lightweight, repeatable 5-layer process** for evaluating, triaging, and selectively translating ideas from external Agent Skills repositories into this repository's stable library.

**Purpose**: Prevent ad-hoc import of external patterns, maintain policy consistency, ensure traceability of adoption decisions, and preserve the repository's independent skill-folder contract.

---

## Core principles

1. **Traceable decisions**: All external-reference evaluations are stored in repo-visible `INTAKE.md` files, not left in session context or hidden chat history.
2. **No direct copying**: External repositories are referenced as-is in `other-project-examples/`; adopted ideas are translated into our format via the standard creator/reviewer workflow.
3. **Gated adoption**: All external ideas flow through `creator -> reviewer -> PR -> release` gates, not imported outside the workflow.
4. **Policy-first**: Adoption decisions must align with this repository's `.github/copilot-instructions.md` contract and canonical policy.
5. **Maintenance focus**: Reference status is checked quarterly; stale references are deprecated or refreshed explicitly.

---

## The 5-Layer Process

### 1. Storage & Discovery Layer

**Goal**: Organize external references so they are findable and indexed.

**Setup**:
- External references live in `other-project-examples/reference-agent-skills/<author>/<repo-name>/`
- Each reference folder is a clone or archive of the external repo, preserved as-is
- A sibling `INTAKE.md` is added to the same folder to record triage decisions (not inside the external repo)

**Artifacts**:
- `other-project-examples/reference-agent-skills/CATALOG.md` — registry of all external references with metadata and status
- `other-project-examples/reference-agent-skills/<author>/INTAKE.md` — triage decision and translation checklist for each reference

**Who**: Reference discoverer (human or future reference-scout agent) registers the repo and adds it to CATALOG.md.

---

### 2. Review & Triage Layer

**Goal**: Evaluate the external reference against this repository's needs and contract.

**Triage template** (use as-is for each reference):

```markdown
# INTAKE: <author>/<repo-name>

## Metadata
- Author: [name]
- URL: [link]
- License: [license] ✅/❌ Compatible?
- Primary focus: [1-2 key domains]
- Number of skills: [count]

## Triage Questions

### Does this reference address gaps in our stable library?
**Answer**: YES / PARTIALLY / NO
**Rationale**: [explain]

### Are the patterns portable to our skill contract?
**Answer**: YES / PARTIALLY / NO
**Rationale**: [explain what is portable and what is not]

### Is the license compatible?
**Answer**: YES / NO
**License conflict**: [if NO, explain]

### Does it suggest improvements to creator/reviewer/template rules?
**Answer**: YES / NO
**Suggestions**: [list specific improvements]

## Decision: ADOPT / ADOPT+ADAPT / REJECT / MONITOR

### Ideas to adopt
1. [idea name and brief rationale]
2. [...]

### Ideas to reject
1. [idea name and rationale for rejection]
2. [...]

## Translation tasks (for follow-up topic)
- [ ] Task A: [implementation step 1]
- [ ] Task B: [implementation step 2]
- [ ] ...

## Rationale
[Explain why this decision is right for this repository.]

## Status
- Intake status: [ADOPT / ADOPT+ADAPT / REJECT / MONITOR]
- Implementation status: [Pending / In progress / Complete]
```

**Who**: Reference triage owner (human or future triage agent) fills the template and records the decision.

**Frequency**:
- For new references: Triage within 2 weeks of discovery
- For monitored references: Re-evaluate quarterly (see Maintenance layer below)

---

### 3. Extraction & Translation Layer

**Goal**: Convert external ideas into actionable creator/reviewer/template changes without direct copying.

**Anti-patterns** (what NOT to do):
- ❌ Direct folder copy from external repo into `.github/skills/`
- ❌ Mixing external naming rules with this repository's kebab-case conventions
- ❌ Skipping `.github/copilot-instructions.md` alignment
- ❌ Importing incompatible structure without adaptation
- ❌ Leaving translation decisions in chat history instead of documenting in INTAKE.md

**Approved patterns** (what TO do):
- ✅ Translate the idea into this repository's format (split model, modular references, etc.)
- ✅ Update `.github/skills/agent-skill-creator/` and `.github/skills/agent-skill-reviewer/` rules to enforce the pattern
- ✅ Update `.github/skills/agent-skill-template/` to guide future skills toward the new pattern
- ✅ Document the adoption in `.github/guides/OTHER-PROJECT-EXAMPLES.md` with links to the INTAKE.md and follow-up PR

**Process**:
1. Review the INTAKE.md triage decision (ADOPT or ADOPT+ADAPT)
2. For each adopted idea:
   - Identify which creator/reviewer/template files need changes
   - Write the change as part of a **new topic** (`plan/<topic>/<topic>.plan.md`)
   - Follow the standard `creator -> reviewer -> PR -> release` workflow for that topic
   - Link the topic plan and final PR back to the INTAKE.md as "Translation tasks" completed

**Workflow diagram**:
```
External reference (INTAKE.md)
          ↓
   Adoption decision (ADOPT / ADOPT+ADAPT)
          ↓
Create follow-up topic plan
  (e.g., plan/enhance-creator-validation/)
          ↓
   [Standard creator → reviewer → PR → release]
          ↓
Update creator/reviewer rules
          ↓
Apply to pilot skills & validate
          ↓
Record in OTHER-PROJECT-EXAMPLES.md
          ↓
Final status: COMPLETE
```

**Who**: Creator agent (per the standard creator/reviewer workflow) implements the changes in a follow-up topic.

---

### 4. Rollout & Enforcement Layer

**Goal**: Ensure adoption decisions are enforced and become part of the standard workflow.

**Enforcement rules**:
- No external idea is considered "adopted" until the creator/reviewer rules are updated and reviewed
- Pilot application to local skills happens only after creator/reviewer rules are approved
- Final adoption is recorded in `OTHER-PROJECT-EXAMPLES.md` with full traceability

**Status tracking**:
- **Pending**: Triage complete, awaiting follow-up topic creation
- **In progress**: Follow-up topic is in creator/reviewer workflow
- **Complete**: Creator/reviewer rules merged, pilot application done, changelog updated

**Who**: Main Agent (publisher/release actor) coordinates the follow-up topic and ensures enforcement rules are met.

---

### 5. Maintenance & Refresh Layer

**Goal**: Keep external references current and deprecate stale ideas.

**Quarterly review**:
- Scheduled: Every 3 months (or when a monitored reference releases significant new work)
- For each reference marked `MONITOR`:
  - Check the external repository for material changes
  - Update INTAKE.md with new findings
  - Re-evaluate status: Upgrade from `MONITOR` to `ADOPT` or `ADOPT+ADAPT`? Stay `MONITOR`? Change to `REJECT`?
  - If status changes, create a follow-up topic

**Deprecation process**:
- If an adopted idea becomes stale or conflicts with new policy:
  - Mark it as deprecated in a comment in the relevant creator/reviewer/template section
  - Document the replacement pattern
  - Create a follow-up topic to migrate existing skills to the new pattern
  - Update the changelog in `OTHER-PROJECT-EXAMPLES.md`

**Who**: Reference maintenance owner (human or future maintenance agent) performs quarterly reviews.

---

## Artifacts and their roles

| Artifact | Path | Responsibility | Role |
| --- | --- | --- | --- |
| External reference | `other-project-examples/reference-agent-skills/<author>/<repo>/` | Reference discoverer | Store external repo as-is |
| Intake decision | `other-project-examples/reference-agent-skills/<author>/INTAKE.md` | Triage owner | Record triage, translation tasks, rationale |
| Catalog | `other-project-examples/reference-agent-skills/CATALOG.md` | Reference discoverer + triage owner | Registry of all external references and their status |
| Adoption changelog | `.github/guides/OTHER-PROJECT-EXAMPLES.md` | Main Agent + follow-up creator | Record of implemented adoptions, linked to PRs and commits |
| Follow-up topic plan | `plan/<topic>/<topic>.plan.md` | Follow-up creator | Implement creator/reviewer/template changes per INTAKE.md |

---

## Example: Full lifecycle

**Scenario**: You discover a new external Agent Skills repo from author "Jane Doe".

1. **Storage** (Discovery Layer):
   - Clone/archive `jane-doe/agent-skills` to `other-project-examples/reference-agent-skills/jane-doe/agent-skills/`
   - Create `other-project-examples/reference-agent-skills/jane-doe/INTAKE.md`
   - Update `CATALOG.md` with new entry (`PENDING`)

2. **Triage** (Review Layer):
   - Fill INTAKE.md with metadata and triage questions
   - Answer: "Does it address gaps? YES. Portable? PARTIALLY. License OK? YES. Improves creator/reviewer? YES."
   - Decision: `ADOPT+ADAPT`
   - List specific ideas: validation rigor, error-pattern framing, lifecycle clarity
   - Store translation tasks in INTAKE.md

3. **Extraction** (Translation Layer):
   - Create follow-up topic: `plan/enhance-creator-validation/enhance-creator-validation.plan.md`
   - Identify changes needed in `.github/skills/agent-skill-creator/` and `.github/skills/agent-skill-reviewer/`
   - Walk through creator → reviewer → PR → release workflow

4. **Rollout** (Enforcement Layer):
   - After follow-up topic merges, update CATALOG.md status from `PENDING` to `ADOPT+ADAPT`
   - Apply refined creator/reviewer expectations to 2 pilot skills
   - Verify improvements

5. **Maintenance** (Refresh Layer):
   - Update `OTHER-PROJECT-EXAMPLES.md` with adoption record:
     ```
     | jane-doe/agent-skills | Validation rigor + error-pattern framing | 2026-04 | PR #42 | `ADOPT+ADAPT` |
     ```
   - Schedule next review: 2026-10

6. **Future** (Maintenance):
   - Quarterly: Re-check jane-doe/agent-skills repo
   - If new patterns emerge, update INTAKE.md
   - If status should change, create a new follow-up topic

---

## Common questions

### Q: Can we adopt an external idea without updating creator/reviewer rules?

**A**: No. External ideas must flow through the standard creator/reviewer workflow. If adoption doesn't change the rules, it's not a repository-level adoption — it's a one-off reference. Keep it in the INTAKE.md as a note, not as an adopted pattern.

### Q: What if the external repo's license conflicts with ours?

**A**: Record the conflict in INTAKE.md, set status to `REJECT`, and explain why. Do not pursue further without license resolution.

### Q: Can I skip the INTAKE.md and just reference an external repo?

**A**: No. INTAKE.md is the traceable decision artifact. Without it, future maintainers won't know why a reference was added or whether it was deliberately rejected. Always populate INTAKE.md.

### Q: How do I deprecate an adopted idea?

**A**: 
1. Mark the relevant section in creator/reviewer/template with a deprecation comment
2. Create a follow-up topic to migrate existing skills
3. Update INTAKE.md and OTHER-PROJECT-EXAMPLES.md with the deprecation note
4. Execute the follow-up topic through the standard workflow

### Q: What if a reference is mostly irrelevant?

**A**: Set status to `REJECT` in INTAKE.md, explain why, and leave it there for posterity. Future reviewers will know the decision was deliberate.

---

## Next steps

- For the initial addyosmani/agent-skills reference, see `other-project-examples/reference-agent-skills/addyosmani/INTAKE.md`
- To track adopted ideas, see `.github/guides/OTHER-PROJECT-EXAMPLES.md`
- To create a follow-up topic for implementation, use `plan-creator` to generate `plan/<topic>/<topic>.plan.md` per `plan/agent-handoff-workflow.md`
