# /// script
# requires-python = ">=3.11"
# ///
"""Step status tracker for plan/<topic>/<topic>.step.md files.

Usage:
  python step_tracker.py read_all <topic>
  python step_tracker.py read_not_run <topic>
  python step_tracker.py read_success <topic>
  python step_tracker.py check_all_succeeded <topic>
  python step_tracker.py check_impl_steps_succeeded <topic>
"""

import sys
import re
from pathlib import Path
from dataclasses import dataclass
from typing import Literal
import argparse


@dataclass
class Step:
    """Represents a single step in the tracking file."""

    text: str
    status: Literal["done", "pending"]
    bracket: str  # Original bracket marker: [X], [x], or [ ]


def _parse_step_line(
    line: str, line_num: int, pattern: re.Pattern[str]
) -> Step | None:
    """Parse a single step line and return a Step or None."""
    match = pattern.match(line.rstrip())
    if not match:
        return None

    bracket_char = match.group(1)
    step_text = match.group(2).strip()
    bracket = f"[{bracket_char}]"

    if bracket_char == "X":
        status: Literal["done", "pending"] = "done"
    elif bracket_char == " ":
        status = "pending"
    elif bracket_char == "x":
        status = "pending"
        print(
            f"Warning: Found lowercase [x] at line {line_num}; treating as pending",
            file=sys.stderr,
        )
    else:
        status = "pending"
        print(
            f"Warning: Found unexpected bracket content [{bracket_char}] at line {line_num}; treating as pending",
            file=sys.stderr,
        )

    return Step(text=step_text, status=status, bracket=bracket)


def parse_steps(topic: str, plan_dir: Path = Path("plan")) -> list[Step]:
    """Parse steps from plan/<topic>/<topic>.step.md.

    Args:
        topic: Topic name (e.g., 'my-feature')
        plan_dir: Base plan directory (default: 'plan')

    Returns:
        List of Step objects

    Raises:
        FileNotFoundError: If .step.md file does not exist
    """
    step_file = plan_dir / topic / f"{topic}.step.md"

    if not step_file.exists():
        raise FileNotFoundError(f"File not found: {step_file}")

    steps: list[Step] = []
    pattern = re.compile(r"^\- \[(.)\](.*)")

    with open(step_file, "r", encoding="utf-8") as f:
        for line_num, line in enumerate(f, start=1):
            step = _parse_step_line(line, line_num, pattern)
            if step is not None:
                steps.append(step)

    return steps


def parse_impl_steps(topic: str, plan_dir: Path = Path("plan")) -> list[Step]:
    """Parse only the steps under the '## Implementation Steps' section.

    Reads plan/<topic>/<topic>.step.md and returns Step objects found
    exclusively inside the '## Implementation Steps' heading block,
    stopping at the next '##' heading.

    Args:
        topic: Topic name (e.g., 'my-feature')
        plan_dir: Base plan directory (default: 'plan')

    Returns:
        List of Step objects from the Implementation Steps section only.

    Raises:
        FileNotFoundError: If .step.md file does not exist
    """
    step_file = plan_dir / topic / f"{topic}.step.md"

    if not step_file.exists():
        raise FileNotFoundError(f"File not found: {step_file}")

    steps: list[Step] = []
    pattern = re.compile(r"^\- \[(.)\](.*)")
    in_impl_section = False

    with open(step_file, "r", encoding="utf-8") as f:
        for line_num, line in enumerate(f, start=1):
            stripped = line.rstrip()
            if stripped.startswith("## "):
                in_impl_section = stripped == "## Implementation Steps"
                continue
            if in_impl_section:
                step = _parse_step_line(stripped, line_num, pattern)
                if step is not None:
                    steps.append(step)

    return steps


def format_step(step: Step) -> str:
    """Format a step for display using original bracket."""
    return f"{step.bracket} {step.text}"


def read_all(topic: str, plan_dir: Path = Path("plan")) -> int:
    """Read and display all steps."""
    try:
        steps = parse_steps(topic, plan_dir)
    except FileNotFoundError as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1

    for step in steps:
        print(format_step(step))

    return 0


def read_not_run(topic: str, plan_dir: Path = Path("plan")) -> int:
    """Read and display only pending steps."""
    try:
        steps = parse_steps(topic, plan_dir)
    except FileNotFoundError as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1

    pending_steps = [s for s in steps if s.status == "pending"]

    for step in pending_steps:
        print(format_step(step))

    return 0


def read_success(topic: str, plan_dir: Path = Path("plan")) -> int:
    """Read and display only completed steps."""
    try:
        steps = parse_steps(topic, plan_dir)
    except FileNotFoundError as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1

    done_steps = [s for s in steps if s.status == "done"]

    for step in done_steps:
        print(format_step(step))

    return 0


def check_all_succeeded(topic: str, plan_dir: Path = Path("plan")) -> int:
    """Check if all steps are complete. Exit 0 if yes, 1 if any pending."""
    try:
        steps = parse_steps(topic, plan_dir)
    except FileNotFoundError as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1

    pending_steps = [s for s in steps if s.status == "pending"]

    if not pending_steps:
        total = len(steps)
        print(f"✅ SUCCESS: All {total} steps complete")
        return 0

    print(f"❌ BLOCKED: {len(pending_steps)} steps pending (exit code 1)")
    for step in pending_steps:
        print(format_step(step))

    return 1


def check_impl_steps_succeeded(topic: str, plan_dir: Path = Path("plan")) -> int:
    """Check if all Implementation Steps are complete. Exit 0 if yes, 1 if any pending.

    Unlike check_all_succeeded, this only inspects the '## Implementation Steps'
    section of the step.md file, ignoring Workflow Stages entries that are
    expected to be incomplete at Phase 3 (Implementation Gate).
    """
    try:
        steps = parse_impl_steps(topic, plan_dir)
    except FileNotFoundError as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1

    if not steps:
        print("❌ BLOCKED: no Implementation Steps found")
        return 1

    pending_steps = [s for s in steps if s.status == "pending"]

    if not pending_steps:
        total = len(steps)
        print(f"✅ SUCCESS: All {total} Implementation Steps complete")
        return 0

    print(f"❌ BLOCKED: {len(pending_steps)} implementation steps pending (exit code 1)")
    for step in pending_steps:
        print(format_step(step))

    return 1


def main() -> int:
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description="Query step status in plan/<topic>/<topic>.step.md files"
    )
    subparsers = parser.add_subparsers(dest="operation", required=True)

    # read_all
    read_all_parser = subparsers.add_parser(
        "read_all", help="Read all steps (pending and done)"
    )
    read_all_parser.add_argument("topic", help="Topic name")

    # read_not_run
    read_not_run_parser = subparsers.add_parser(
        "read_not_run", help="Read only pending steps"
    )
    read_not_run_parser.add_argument("topic", help="Topic name")

    # read_success
    read_success_parser = subparsers.add_parser(
        "read_success", help="Read only completed steps"
    )
    read_success_parser.add_argument("topic", help="Topic name")

    # check_all_succeeded
    check_all_parser = subparsers.add_parser(
        "check_all_succeeded",
        help="Check if all steps complete; exit 0 if yes, 1 if any pending",
    )
    check_all_parser.add_argument("topic", help="Topic name")

    # check_impl_steps_succeeded
    check_impl_parser = subparsers.add_parser(
        "check_impl_steps_succeeded",
        help="Check if all Implementation Steps complete (ignores Workflow Stages); exit 0 if yes, 1 if any pending",
    )
    check_impl_parser.add_argument("topic", help="Topic name")

    args = parser.parse_args()

    topic = args.topic
    plan_dir = Path("plan")

    if args.operation == "read_all":
        return read_all(topic, plan_dir)
    elif args.operation == "read_not_run":
        return read_not_run(topic, plan_dir)
    elif args.operation == "read_success":
        return read_success(topic, plan_dir)
    elif args.operation == "check_all_succeeded":
        return check_all_succeeded(topic, plan_dir)
    elif args.operation == "check_impl_steps_succeeded":
        return check_impl_steps_succeeded(topic, plan_dir)

    return 1


if __name__ == "__main__":
    sys.exit(main())
