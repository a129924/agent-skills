# Adopted Ideas from Other Project Examples

This changelog records external Agent Skills ideas that have been formally adopted into this repository's stable library through the reference intake workflow defined in [REFERENCE-INTAKE-PROCESS.md](./REFERENCE-INTAKE-PROCESS.md).

Each entry links to:
- The original external reference and INTAKE.md triage decision
- The follow-up topic plan and PR that implemented the adoption
- The creator/reviewer/template changes that resulted
- Affected local skills (if any)

---

## Adoption records

| Reference | Adopted ideas | Decision date | PR/Commit | Creator/reviewer changes | Pilot skills | Status |
| --- | --- | --- | --- | --- | --- | --- |
| [addyosmani/agent-skills](../../other-project-examples/reference-agent-skills/addyosmani/INTAKE.md) | Validation rigor, red-flag framing, error-pattern discovery, lifecycle clarity, example pairing | 2026-04-24 | Pending follow-up topic | Pending implementation | TBD | `PENDING` |

---

## Column guide

- **Reference**: Link to the external repository and its INTAKE.md decision document
- **Adopted ideas**: High-level summary of what ideas were taken from this reference
- **Decision date**: When the intake triage was completed
- **PR/Commit**: Links to the follow-up PR and commit(s) that implemented the adoption
- **Creator/reviewer changes**: Which files in `.github/skills/` were updated (e.g., `agent-skill-creator/SKILL.md`, `agent-skill-reviewer/checklist.md`)
- **Pilot skills**: Sample `.github/skills/` folders that were improved using the new creator/reviewer rules
- **Status**: `PENDING` (waiting for follow-up topic), `IN_PROGRESS` (follow-up topic in review), `COMPLETE` (merged and validated)

---

## Future maintenance

- **When to update**: After a follow-up adoption topic is merged and validated
- **New references**: As new external repositories are discovered and triaged, add them to the table and link to their INTAKE.md
- **Status transitions**: Update entries as follow-up topics move through the workflow
- **Deprecations**: If an adopted idea becomes deprecated, mark it with a deprecation note and link to the replacement pattern

---

## Template for new adoption records

When a follow-up topic (created per [REFERENCE-INTAKE-PROCESS.md](./REFERENCE-INTAKE-PROCESS.md)) is merged and implemented:

1. Copy this template and fill in the details:

```markdown
| [Reference name](link/to/INTAKE.md) | Idea 1, Idea 2, Idea 3 | YYYY-MM-DD | [PR #XX](link) | [file1.md](link), [file2.md](link) | [skill1](link), [skill2](link) | `COMPLETE` |
```

2. Add the row to the table above in the appropriate position
3. Update the reference's INTAKE.md with a link back to this changelog entry (use relative path: `../../guides/OTHER-PROJECT-EXAMPLES.md`)
4. Update the reference's INTAKE.md `Implementation status` field to `Complete`

---

## See also

- [REFERENCE-INTAKE-PROCESS.md](./REFERENCE-INTAKE-PROCESS.md) — the canonical 5-layer intake workflow
- [CATALOG.md](../../other-project-examples/reference-agent-skills/CATALOG.md) — registry of all external references discovered
- [plan/reference-intake-workflow/](../../plan/reference-intake-workflow/) — the topic plan that established this process
