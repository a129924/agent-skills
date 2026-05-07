# Reference — plan-step-tracker

## Canonical file and marker rules

- The tracked file path is `plan/<topic>/<topic>.step.md`.
- Only checkbox lines that match `- [.]` are relevant to this skill.
- Marker interpretation is fixed:
  - `[X]` = done
  - `[ ]` = pending
  - `[x]` = pending and warning-worthy
- This skill is read-only; it reports declared checkbox state and does not repair formatting.

## Python CLI contract

Use the local script from the repository root:

```bash
python .github/skills/plan-step-tracker/scripts/step_tracker.py <operation> <topic>
```

Supported operations:

| Operation | Result | Exit code |
| --- | --- | --- |
| `read_all` | prints all parsed checkbox lines | `0` |
| `read_not_run` | prints pending lines, including `[x]` | `0` |
| `read_success` | prints completed `[X]` lines | `0` |
| `check_all_succeeded` | prints success summary if all done; otherwise blocked summary plus pending lines | `0` when complete, `1` when pending |

Error contract:

- Missing file prints `Error: File not found: plan/<topic>/<topic>.step.md` to stderr and returns exit code `1`.
- Lowercase `[x]` prints `Warning: Found lowercase [x] at line N; treating as pending` to stderr.

## Grep fallback guidance

Use grep only when the Python CLI cannot run.

```bash
# all parsed checkbox lines
grep '^\- \[.\]' plan/<topic>/<topic>.step.md

# pending lines with a broad fallback that catches both [ ] and [x]
grep '^\- \[[ x]\]' plan/<topic>/<topic>.step.md

# completed lines
grep '^\- \[X\]' plan/<topic>/<topic>.step.md
```

Blocking fallback example:

```bash
PENDING=$(grep -c '^\- \[[ x]\]' plan/<topic>/<topic>.step.md)
if [ "$PENDING" -eq 0 ]; then
  echo 'SUCCESS: All steps complete'
  exit 0
else
  echo "BLOCKED: $PENDING steps pending"
  grep '^\- \[[ x]\]' plan/<topic>/<topic>.step.md
  exit 1
fi
```

Fallback limitation:

- grep can approximate pending detection for `[x]`, but it does not emit the Python CLI warning automatically
- when using grep fallback, call out lowercase `[x]` manually if present
