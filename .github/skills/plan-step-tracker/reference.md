# Reference — plan-step-tracker

## `.step.md` Format Specification

Each topic's step file lives at `plan/<topic>/<topic>.step.md`.

### File structure

```yaml
---
topic: <topic>
phase: implementation
created: YYYY-MM-DD
---

# <topic> — Step Tracking

## Workflow Stages
- [X] stage-1-name
- [ ] stage-2-name

## Implementation Steps

### Group A: <Feature Name>
- [X] 1. Completed step
- [ ] 2. Pending step
- [X] 3. Another done step

### Group B: <Another Feature>
- [ ] 4. Not started yet
```

### Rules

1. **YAML Frontmatter** (`--- ... ---` block): metadata only; informational only, not parsed by script
2. **Content lines**: Only lines matching `^\- \[.\]` pattern are parsed:
   - `- [X]` → done
   - `- [ ]` → pending (space inside brackets)
   - `- [x]` → **pending + warning** (lowercase not accepted; treated as formatting error)
3. **Non-checkbox content**: Titles (`#`, `##`), plain text, other formatting → ignored
4. **Grouping**: Groups (`### Group A`, `### Group B`) copied directly from `plan.md` structure; do not invent new groupings
5. **Single file per topic**: Plan is not split → Steps are not split. If a plan breaks into multiple `.plan.md` files, then and only then create corresponding `.step.md` files.

## Grep Quick-Reference Patterns

| Operation | Grep Command | Expected Output |
| --- | --- | --- |
| `read_all` | `grep '^\- \[.\]' plan/<topic>/<topic>.step.md` | All checkbox lines |
| `read_not_run` | `grep '^\- \[ \]' plan/<topic>/<topic>.step.md` | Pending lines only |
| `read_success` | `grep '^\- \[X\]' plan/<topic>/<topic>.step.md` | Done lines only |
| `check_all_succeeded` | `grep -c '^\- \[ \]' plan/<topic>/<topic>.step.md` | Count: 0 = SUCCESS, >0 = BLOCKED |

### Fallback usage

If Python CLI is unavailable:

```bash
# Query pending steps
grep '^\- \[ \]' plan/<topic>/<topic>.step.md

# Verify all done (count pending steps; 0 = success)
test $(grep -c '^\- \[ \]' plan/<topic>/<topic>.step.md) -eq 0 && echo "SUCCESS" || echo "BLOCKED"
```

## Lowercase `[x]` Rule

**Status**: `[x]` (lowercase) is **not** a valid done marker.

**Behavior**:
- Treat `[x]` as pending (same as `[ ]`)
- Emit warning to stderr: `Warning: Found lowercase [x] at line N; treating as pending`
- Do not silently accept; surface the formatting issue to user

**Rationale**: Detect copy-paste errors or inconsistencies; lowercase often indicates user forgot uppercase.

**Example**:
```
- [X] Correctly done
- [x] Wrongly lowercase → treated as pending, warning issued
- [ ] Pending
```

## Splitting Rules

**When to split into multiple `.step.md` files**:
- Only when `plan/<topic>/` itself contains multiple `<topic>_*.plan.md` files (topic is formally split)
- Then create corresponding `<topic>_*.step.md` tracking files

**When NOT to split**:
- Single `plan/<topic>/<topic>.plan.md` → single `plan/<topic>/<topic>.step.md`
- Do not invent new groupings or subdivisions

**Rationale**: Avoid administrative overhead; keep step structure aligned with plan structure.

## Python CLI Usage

### Installation

No installation required; `step_tracker.py` is a uv script.

```bash
# Direct execution
python .github/skills/plan-step-tracker/scripts/step_tracker.py <operation> <topic>
```

### Operations

```bash
# Read all steps (pending + done)
python .github/skills/plan-step-tracker/scripts/step_tracker.py read_all my-feature

# Read pending steps only
python .github/skills/plan-step-tracker/scripts/step_tracker.py read_not_run my-feature

# Read done steps only
python .github/skills/plan-step-tracker/scripts/step_tracker.py read_success my-feature

# Check if all done (exit 0 if yes, 1 if any pending)
python .github/skills/plan-step-tracker/scripts/step_tracker.py check_all_succeeded my-feature
if [ $? -eq 0 ]; then
  echo "All steps complete; proceeding..."
else
  echo "Some steps pending; cannot proceed."
fi
```

### Exit Codes

| Code | Meaning |
| --- | --- |
| 0 | Operation succeeded (valid for all operations; check output for content) |
| 1 | Blocking condition (check_all_succeeded has pending, or `.step.md` not found) |

## Common Implementation Notes

- **Token efficiency** (R6): Python reads one file end-to-end, line by line; avoids full file parsing overhead
- **Semantic equivalence**: Grep patterns and Python CLI produce semantically equivalent output; format may differ (Python strips `- ` prefix from output)
- **No side effects**: All operations are read-only; no modification of `.step.md` files
- **Portability**: Python ≥ 3.11 (matches existing `apply_toolconfig.py` standard); uv script format (`# /// script` header)
