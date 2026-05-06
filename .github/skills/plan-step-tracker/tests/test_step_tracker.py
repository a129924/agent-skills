"""Tests for step_tracker.py"""

import pytest
from pathlib import Path
import sys

# Import the step_tracker module
sys.path.insert(0, str(Path(__file__).parent.parent / "scripts"))
from step_tracker import (
    parse_steps,
    read_all,
    read_not_run,
    read_success,
    check_all_succeeded,
)


@pytest.fixture
def temp_plan_dir(tmp_path):
    """Create a temporary plan directory structure."""
    plan_dir = tmp_path / "plan"
    plan_dir.mkdir()
    return plan_dir


@pytest.fixture
def sample_step_file(temp_plan_dir):
    """Create a sample .step.md file with mixed statuses."""
    topic = "test-topic"
    topic_dir = temp_plan_dir / topic
    topic_dir.mkdir()

    content = """---
topic: test-topic
phase: implementation
created: 2025-01-15
---

# test-topic — Step Tracking

## Implementation Steps

### Phase 1: Core
- [X] 1. Setup environment
- [ ] 2. Implement main logic
- [X] 3. Add basic tests

### Phase 2: Polish
- [ ] 4. Write documentation
- [x] 5. Code review (lowercase)
- [ ] 6. Integration tests
"""

    step_file = topic_dir / f"{topic}.step.md"
    step_file.write_text(content)

    return temp_plan_dir, topic


class TestParseStatus:
    """Test status parsing: [X] → done, [ ] → pending, [x] → pending+warning."""

    def test_parse_uppercase_X_as_done(self, temp_plan_dir, capsys):
        """Parse [X] as done status."""
        topic = "test-uppercase"
        topic_dir = temp_plan_dir / topic
        topic_dir.mkdir()

        content = """---
topic: test-uppercase
---
- [X] Completed task
"""
        (topic_dir / f"{topic}.step.md").write_text(content)

        steps = parse_steps(topic, temp_plan_dir)
        assert len(steps) == 1
        assert steps[0].status == "done"
        assert steps[0].text == "Completed task"

    def test_parse_space_as_pending(self, temp_plan_dir):
        """Parse [ ] as pending status."""
        topic = "test-pending"
        topic_dir = temp_plan_dir / topic
        topic_dir.mkdir()

        content = """---
topic: test-pending
---
- [ ] Pending task
"""
        (topic_dir / f"{topic}.step.md").write_text(content)

        steps = parse_steps(topic, temp_plan_dir)
        assert len(steps) == 1
        assert steps[0].status == "pending"
        assert steps[0].text == "Pending task"

    def test_parse_lowercase_x_as_pending_with_warning(self, temp_plan_dir, capsys):
        """Parse [x] as pending with stderr warning."""
        topic = "test-lowercase"
        topic_dir = temp_plan_dir / topic
        topic_dir.mkdir()

        content = """---
topic: test-lowercase
---
- [x] Incorrectly lowercase task
"""
        (topic_dir / f"{topic}.step.md").write_text(content)

        steps = parse_steps(topic, temp_plan_dir)
        captured = capsys.readouterr()

        assert len(steps) == 1
        assert steps[0].status == "pending"
        assert "[x]" in captured.err or "lowercase" in captured.err

    def test_ignore_non_checkbox_lines(self, temp_plan_dir):
        """Ignore lines that don't start with checkbox pattern."""
        topic = "test-mixed"
        topic_dir = temp_plan_dir / topic
        topic_dir.mkdir()

        content = """---
topic: test-mixed
---

# Header line
Some plain text
- [X] Task 1
Another line without checkbox
- [ ] Task 2
## Subheader
"""
        (topic_dir / f"{topic}.step.md").write_text(content)

        steps = parse_steps(topic, temp_plan_dir)
        assert len(steps) == 2
        assert steps[0].status == "done"
        assert steps[1].status == "pending"


class TestReadNotRun:
    """Test read_not_run: return only pending steps."""

    def test_read_not_run_mixed_status(self, sample_step_file, capsys):
        """Return only pending steps from mixed content."""
        temp_plan_dir, topic = sample_step_file

        result = read_not_run(topic, temp_plan_dir)
        captured = capsys.readouterr()

        assert result == 0
        lines = captured.out.strip().split("\n")
        # Should have 4 pending steps (includes lowercase [x])
        assert len(lines) == 4
        assert all("[ ]" in line or "[x]" in line for line in lines)

    def test_read_not_run_all_done(self, temp_plan_dir):
        """Return empty list when all steps are done."""
        topic = "all-done"
        topic_dir = temp_plan_dir / topic
        topic_dir.mkdir()

        content = """---
topic: all-done
---
- [X] Task 1
- [X] Task 2
"""
        (topic_dir / f"{topic}.step.md").write_text(content)

        result = read_not_run(topic, temp_plan_dir)
        assert result == 0

    def test_read_not_run_file_not_found(self, temp_plan_dir, capsys):
        """Return exit code 1 when file not found."""
        result = read_not_run("nonexistent", temp_plan_dir)
        captured = capsys.readouterr()

        assert result == 1
        assert "not found" in captured.err.lower()


class TestReadSuccess:
    """Test read_success: return only done steps."""

    def test_read_success_mixed_status(self, sample_step_file, capsys):
        """Return only done steps from mixed content."""
        temp_plan_dir, topic = sample_step_file

        result = read_success(topic, temp_plan_dir)
        captured = capsys.readouterr()

        assert result == 0
        lines = captured.out.strip().split("\n")
        # Should have 2 done steps ([X] only)
        assert len(lines) == 2
        assert all("[X]" in line for line in lines)

    def test_read_success_all_pending(self, temp_plan_dir):
        """Return empty list when all steps are pending."""
        topic = "all-pending"
        topic_dir = temp_plan_dir / topic
        topic_dir.mkdir()

        content = """---
topic: all-pending
---
- [ ] Task 1
- [ ] Task 2
"""
        (topic_dir / f"{topic}.step.md").write_text(content)

        result = read_success(topic, temp_plan_dir)
        assert result == 0

    def test_read_success_file_not_found(self, temp_plan_dir, capsys):
        """Return exit code 1 when file not found."""
        result = read_success("nonexistent", temp_plan_dir)
        captured = capsys.readouterr()

        assert result == 1
        assert "not found" in captured.err.lower()


class TestReadAll:
    """Test read_all: return all steps (pending + done)."""

    def test_read_all_mixed_status(self, sample_step_file, capsys):
        """Return all steps from mixed content."""
        temp_plan_dir, topic = sample_step_file

        result = read_all(topic, temp_plan_dir)
        captured = capsys.readouterr()

        assert result == 0
        lines = captured.out.strip().split("\n")
        # Should have 6 checkbox lines
        assert len(lines) == 6
        # Verify mix of [X] and [ ]
        done_count = sum(1 for line in lines if "[X]" in line)
        pending_count = sum(1 for line in lines if "[ ]" in line or "[x]" in line)
        assert done_count == 2
        assert pending_count == 4

    def test_read_all_file_not_found(self, temp_plan_dir, capsys):
        """Return exit code 1 when file not found."""
        result = read_all("nonexistent", temp_plan_dir)
        captured = capsys.readouterr()

        assert result == 1
        assert "not found" in captured.err.lower()


class TestCheckAllSucceeded:
    """Test check_all_succeeded: SUCCESS if all done, BLOCKED if any pending."""

    def test_check_all_succeeded_all_done(self, temp_plan_dir, capsys):
        """Return exit 0 when all steps complete."""
        topic = "all-complete"
        topic_dir = temp_plan_dir / topic
        topic_dir.mkdir()

        content = """---
topic: all-complete
---
- [X] Task 1
- [X] Task 2
- [X] Task 3
"""
        (topic_dir / f"{topic}.step.md").write_text(content)

        result = check_all_succeeded(topic, temp_plan_dir)
        captured = capsys.readouterr()

        assert result == 0
        assert "SUCCESS" in captured.out
        assert "3" in captured.out

    def test_check_all_succeeded_has_pending(self, sample_step_file, capsys):
        """Return exit 1 when any steps pending."""
        temp_plan_dir, topic = sample_step_file

        result = check_all_succeeded(topic, temp_plan_dir)
        captured = capsys.readouterr()

        assert result == 1
        assert "BLOCKED" in captured.out
        # Should list BLOCKED header + pending steps (all on stdout)
        lines = captured.out.strip().split("\n")
        assert len(lines) == 5  # BLOCKED header + 4 pending steps

    def test_check_all_succeeded_file_not_found(self, temp_plan_dir, capsys):
        """Return exit code 1 when file not found."""
        result = check_all_succeeded("nonexistent", temp_plan_dir)
        captured = capsys.readouterr()

        assert result == 1
        assert "not found" in captured.err.lower()

    def test_check_all_succeeded_no_steps(self, temp_plan_dir, capsys):
        """Return SUCCESS when no steps (empty list is complete)."""
        topic = "no-steps"
        topic_dir = temp_plan_dir / topic
        topic_dir.mkdir()

        content = """---
topic: no-steps
---

# Just a header, no checkboxes
"""
        (topic_dir / f"{topic}.step.md").write_text(content)

        result = check_all_succeeded(topic, temp_plan_dir)
        captured = capsys.readouterr()

        assert result == 0
        assert "SUCCESS" in captured.out
        assert "0" in captured.out


class TestEdgeCases:
    """Test edge cases: empty file, missing file, no checkbox lines."""

    def test_empty_file(self, temp_plan_dir):
        """Handle empty file gracefully."""
        topic = "empty"
        topic_dir = temp_plan_dir / topic
        topic_dir.mkdir()

        (topic_dir / f"{topic}.step.md").write_text("")

        steps = parse_steps(topic, temp_plan_dir)
        assert steps == []

    def test_file_with_only_frontmatter(self, temp_plan_dir):
        """Handle file with only frontmatter."""
        topic = "frontmatter-only"
        topic_dir = temp_plan_dir / topic
        topic_dir.mkdir()

        content = """---
topic: frontmatter-only
phase: planning
created: 2025-01-15
---
"""
        (topic_dir / f"{topic}.step.md").write_text(content)

        steps = parse_steps(topic, temp_plan_dir)
        assert steps == []

    def test_file_not_found(self, temp_plan_dir):
        """Raise FileNotFoundError when file not found."""
        with pytest.raises(FileNotFoundError) as exc_info:
            parse_steps("missing-topic", temp_plan_dir)

        assert "not found" in str(exc_info.value).lower()

    def test_no_checkbox_lines(self, temp_plan_dir):
        """Handle file with no checkbox lines."""
        topic = "no-checkboxes"
        topic_dir = temp_plan_dir / topic
        topic_dir.mkdir()

        content = """---
topic: no-checkboxes
---

# This is a header

Just some plain text.

- Normal bullet point without checkbox

More text.
"""
        (topic_dir / f"{topic}.step.md").write_text(content)

        steps = parse_steps(topic, temp_plan_dir)
        assert steps == []

    def test_mixed_checkbox_formats(self, temp_plan_dir):
        """Handle file with various checkbox formats."""
        topic = "mixed"
        topic_dir = temp_plan_dir / topic
        topic_dir.mkdir()

        content = """---
topic: mixed
---
- [X] Done
- [ ] Pending
- [x] Lowercase
- [] No space (should not match)
-[X] No space before dash (should not match)
- [ Not a checkbox
"""
        (topic_dir / f"{topic}.step.md").write_text(content)

        steps = parse_steps(topic, temp_plan_dir)
        # Should parse exactly 3 steps: [X], [ ], [x]
        assert len(steps) == 3
        assert steps[0].status == "done"
        assert steps[1].status == "pending"
        assert steps[2].status == "pending"
