---
name: plan-step-tracker
description: Query step status (pending/done) in plan/<topic>.step.md with minimal token cost and explicit blocking when incomplete.
---

# Purpose

Enable Main Agent and users to efficiently query whether execution steps in `plan/<topic>/<topic>.step.md` are complete (done/pending) with minimal token overhead, and to block continuation when steps remain incomplete.

# Trigger / When to use

Use this skill when:
- Main Agent is executing a multi-step plan and needs to check remaining work (`plan/<topic>/<topic>.step.md`)
- User asks "what steps are still incomplete?" for a given topic
- CI/workflow requires exit code blocking (exit 1) when steps remain pending
- Low-token-cost status query is needed (4 dedicated operations avoid full file parsing)

Do not use this skill when:
- Querying multiple topics simultaneously (non-goal per R7)
- Modifying or updating step status (read-only skill only)
- Monitoring files for real-time changes (no file watching support)
- Integrating with SQL todos table (independent mechanism)

# Inputs

- `<topic>`: Required. Topic name matching `plan/<topic>/` directory. Skill looks for `plan/<topic>/<topic>.step.md`.
- `<operation>`: One of: `read_all`, `read_not_run`, `read_success`, `check_all_succeeded`

# Process

1. **Verify `.step.md` exists** at `plan/<topic>/<topic>.step.md` (Python CLI checks existence; exits 1 if missing).
2. **Parse content lines** matching `^\- \[.\]` pattern only (skip frontmatter, headings, non-checkbox lines).
3. **Classify status**:
   - `[X]` (uppercase) → done
   - `[ ]` (space) → pending
   - `[x]` (lowercase) → pending + emit warning to stderr
4. **Apply operation**:
   - `read_all`: Return all steps (done + pending)
   - `read_not_run`: Return only pending steps
   - `read_success`: Return only done steps
   - `check_all_succeeded`: Return SUCCESS (exit 0) if all done; BLOCKED + list + exit 1 if any pending
5. **Output format**: Structured list (each line: `[X/space] step text`); blocking operations flag completion status clearly.

**Primary execution path**: Use `python .github/skills/plan-step-tracker/scripts/step_tracker.py <operation> <topic>`.  
**Fallback** (if Python CLI unavailable): Use grep patterns per `reference.md` quick-lookup table.

# Examples

**Positive: Main Agent checks remaining work before final validation**
```bash
$ python .github/skills/plan-step-tracker/scripts/step_tracker.py read_not_run my-feature-topic
[ ] Step 2: Implement core logic
[ ] Step 5: Write integration tests

# Exit code 0 (found pending steps, returned successfully)
# Agent parses output, discovers 2 items remain, continues work
```

**Negative: Agent ignores blocking signal and proceeds prematurely**
```bash
$ python .github/skills/plan-step-tracker/scripts/step_tracker.py check_all_succeeded my-feature-topic
❌ BLOCKED: 3 steps pending (exit code 1)
[ ] Step 1: Setup environment
[ ] Step 3: Documentation
[ ] Step 6: Code review

# Exit code 1 (blocking signal)
# WRONG: Agent should halt and display the pending list; MUST NOT continue past this point
```

# Outputs

**For `read_all`, `read_not_run`, `read_success`**:
- List of steps (each line: `[X] step text` or `[ ] step text`)
- Exit code 0 (success; list may be empty if all done or no pending)

**For `check_all_succeeded`**:
- **SUCCESS**: All steps done → `✅ SUCCESS: All N steps complete` + exit code 0
- **BLOCKED**: Any step pending → `❌ BLOCKED: M steps pending (exit code 1)` + list of pending steps + exit code 1

**Error cases** (all exit code 1):
- `.step.md` file not found → `Error: File not found: plan/<topic>/<topic>.step.md`
- Empty file or no checkbox lines → Return empty list (not an error)
- `[x]` (lowercase) detected → Warn on stderr: `Warning: Found lowercase [x] at line N; treating as pending`

# Boundaries

- **Single file per topic**: Assumes `plan/<topic>/` contains exactly one `<topic>.step.md` file; does not aggregate across multiple files.
- **Binary status only**: done or pending; no intermediate states (in_progress, blocked, etc.).
- **Read-only**: This skill does not modify `.step.md` files.
- **No cross-topic queries**: Each operation takes exactly one `<topic>` argument.
- **No integration tests**: Tests use `tmp_path` fixture; does not read real `plan/` directory.
- **Case-sensitive status**: Only `[X]` (uppercase) is accepted as done; `[x]` (lowercase) triggers warning.
- **Max 200 steps per file**: No pagination support; assumes reasonable file size.

# Verification (Medium-Risk Control)

Because this skill produces blocking signals (exit code 1) used in CI workflows, verify:
- ✓ Exit code 0 when all steps done (enables continuation)
- ✓ Exit code 1 when any step pending (blocks CI/workflow)
- ✓ Exit code 1 when `.step.md` not found (explicit error signal)
- ✓ Lowercase `[x]` emits warning to stderr (detects formatting issues)
- ✓ Grep fallback patterns match Python CLI output exactly (ensures consistency)

# Local references

- `reference.md`: `.step.md` format spec, grep quick-lookup patterns, `[x]` lowercase rule, CLI usage, splitting rules
- `examples.md`: 4 operation examples (CLI + grep fallback), blocking scenario, edge cases (empty file, missing `.step.md`, no checkboxes)
- `scripts/step_tracker.py`: Python CLI implementation (uv script, `>=3.11`, 4 subcommands)
- `tests/test_step_tracker.py`: pytest suite covering parse, filter, blocking, and edge cases (6 test classes)
