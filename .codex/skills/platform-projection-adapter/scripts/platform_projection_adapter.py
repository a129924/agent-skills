#!/usr/bin/env python3
"""Project the canonical skills library into a caller-provided platform root."""

from __future__ import annotations

import argparse
import contextlib
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Callable, Sequence, TextIO


PLACEHOLDER_PREFIX = ".codex/"
IGNORED_SOURCE_DIR_NAMES = {"__pycache__"}
IGNORED_SOURCE_SUFFIXES = {".pyc", ".pyo"}


class ProjectionError(Exception):
    """Raised when projection planning or apply cannot complete safely."""

    def __init__(self, message: str, *, source_count: int = 0) -> None:
        super().__init__(message)
        self.source_count = source_count


@dataclass(frozen=True)
class PlanEntry:
    source_path: Path
    relative_path: Path
    target_path: Path
    display_path: str
    rendered_content: str
    action: str
    conflict: bool


@dataclass(frozen=True)
class ProjectionPlan:
    source_count_total: int
    entries: tuple[PlanEntry, ...]

    @property
    def source_count(self) -> int:
        return self.source_count_total

    @property
    def create_count(self) -> int:
        return sum(1 for entry in self.entries if entry.action == "create")

    @property
    def update_count(self) -> int:
        return sum(1 for entry in self.entries if entry.action == "update")

    @property
    def noop_count(self) -> int:
        return sum(1 for entry in self.entries if entry.action == "noop")

    @property
    def conflict_count(self) -> int:
        return sum(1 for entry in self.entries if entry.conflict)

    def paths_for(self, action: str) -> list[str]:
        return [entry.display_path for entry in self.entries if entry.action == action]

    def conflict_paths(self) -> list[str]:
        return [entry.display_path for entry in self.entries if entry.conflict]


def parse_args(argv: Sequence[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Project canonical skills/ content into a platform root.",
    )
    parser.add_argument(
        "--platform-root",
        required=True,
        help="Target platform root. Projection writes land under <platform-root>/skills/.",
    )
    parser.add_argument(
        "--apply",
        action="store_true",
        help="Write the projection into the target root. Default is dry-run.",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Allow overwriting managed target files whose content differs.",
    )
    args = parser.parse_args(argv)
    if args.force and not args.apply:
        parser.error("--force requires --apply")
    return args


def repo_root_from_script(script_path: Path | None = None) -> Path:
    resolved_script_path = resolve_for_overlap_check(script_path or Path(__file__))
    for candidate in resolved_script_path.parents:
        if (candidate / "AGENTS.md").is_file() and (candidate / "skills").is_dir():
            return candidate
    raise ProjectionError(
        "Failed to locate repository root from script path: "
        f"{resolved_script_path}"
    )


def normalize_platform_root(raw_platform_root: str) -> str:
    normalized = Path(raw_platform_root).as_posix()
    if normalized == "/":
        return normalized
    normalized = normalized.rstrip("/")
    return normalized or "."


def resolve_for_overlap_check(path: Path) -> Path:
    try:
        return path.resolve(strict=False)
    except OSError as exc:
        raise ProjectionError(f"Failed to resolve path: {path}") from exc


def validate_non_overlapping_roots(source_root: Path, platform_root: Path) -> None:
    resolved_source_root = resolve_for_overlap_check(source_root)
    resolved_target_skills_root = resolve_for_overlap_check(platform_root / "skills")
    if (
        resolved_target_skills_root == resolved_source_root
        or resolved_target_skills_root.is_relative_to(resolved_source_root)
        or resolved_source_root.is_relative_to(resolved_target_skills_root)
    ):
        raise ProjectionError(
            "Platform root would overlap canonical skills/: "
            f"source={resolved_source_root} target={resolved_target_skills_root}"
        )


def discover_source_files(source_root: Path) -> list[Path]:
    if not source_root.is_dir():
        raise ProjectionError(f"Canonical source root does not exist: {source_root}")
    return sorted(
        path
        for path in source_root.rglob("*")
        if path.is_file()
        and not any(part in IGNORED_SOURCE_DIR_NAMES for part in path.parts)
        and path.suffix not in IGNORED_SOURCE_SUFFIXES
    )


def render_source(source_path: Path, platform_root_text: str) -> str:
    try:
        content = source_path.read_text(encoding="utf-8")
    except UnicodeDecodeError as exc:
        raise ProjectionError(
            f"Failed to decode UTF-8 source file: {source_path}"
        ) from exc
    except OSError as exc:
        raise ProjectionError(f"Failed to read source file: {source_path}") from exc
    platform_prefix = "/" if platform_root_text == "/" else f"{platform_root_text}/"
    return content.replace(PLACEHOLDER_PREFIX, platform_prefix)


def build_plan(source_root: Path, platform_root: Path, platform_root_text: str) -> ProjectionPlan:
    entries: list[PlanEntry] = []
    target_skills_root = platform_root / "skills"
    source_files = discover_source_files(source_root)
    source_count = len(source_files)
    for source_path in source_files:
        relative_path = source_path.relative_to(source_root)
        target_path = target_skills_root / relative_path
        try:
            rendered_content = render_source(source_path, platform_root_text)
        except ProjectionError as exc:
            raise ProjectionError(str(exc), source_count=source_count) from exc
        rendered_bytes = rendered_content.encode("utf-8")

        if not target_path.exists():
            action = "create"
            conflict = False
        else:
            try:
                existing_bytes = target_path.read_bytes()
            except OSError as exc:
                raise ProjectionError(
                    f"Failed to read target file during planning: {target_path}",
                    source_count=source_count,
                ) from exc
            if existing_bytes == rendered_bytes:
                action = "noop"
                conflict = False
            else:
                action = "update"
                conflict = True

        entries.append(
            PlanEntry(
                source_path=source_path,
                relative_path=relative_path,
                target_path=target_path,
                display_path=(Path("skills") / relative_path).as_posix(),
                rendered_content=rendered_content,
                action=action,
                conflict=conflict,
            )
        )
    return ProjectionPlan(source_count_total=source_count, entries=tuple(entries))


def write_rendered_file(target_path: Path, rendered_content: str) -> None:
    target_path.parent.mkdir(parents=True, exist_ok=True)
    target_path.write_text(rendered_content, encoding="utf-8")


def validate_target_path_for_write(
    target_skills_root: Path,
    target_path: Path,
) -> None:
    current_path = target_skills_root
    relative_path = target_path.relative_to(target_skills_root)

    for part in relative_path.parts[:-1]:
        if current_path.is_symlink():
            raise ProjectionError(
                f"Refusing to write through symlinked target path: {current_path}"
            )
        current_path = current_path / part

    if current_path.is_symlink():
        raise ProjectionError(
            f"Refusing to write through symlinked target path: {current_path}"
        )
    if target_path.is_symlink():
        raise ProjectionError(
            f"Refusing to write through symlinked target path: {target_path}"
        )


def render_summary(
    *,
    mode: str,
    platform_root_text: str,
    plan: ProjectionPlan,
    result: str,
    error: str | None = None,
) -> str:
    lines = [
        f"mode: {mode}",
        f"platform_root: {platform_root_text}",
        f"source_count: {plan.source_count}",
        f"create: {plan.create_count}",
        f"update: {plan.update_count}",
        f"noop: {plan.noop_count}",
        f"conflicts: {plan.conflict_count}",
    ]
    create_paths = plan.paths_for("create")
    update_paths = plan.paths_for("update")
    conflict_paths = plan.conflict_paths()
    if create_paths:
        lines.append("create_paths:")
        lines.extend(f"  - {path}" for path in create_paths)
    if update_paths:
        lines.append("update_paths:")
        lines.extend(f"  - {path}" for path in update_paths)
    if conflict_paths:
        lines.append("conflict_paths:")
        lines.extend(f"  - {path}" for path in conflict_paths)
    lines.append(f"result: {result}")
    if error:
        lines.append(f"error: {error}")
    return "\n".join(lines) + "\n"


def execute_projection(
    args: argparse.Namespace,
    *,
    repo_root: Path,
    stdout: TextIO,
    stderr: TextIO,
    write_file: Callable[[Path, str], None] = write_rendered_file,
) -> int:
    mode = "apply" if args.apply else "dry-run"
    platform_root = Path(args.platform_root)
    platform_root_text = normalize_platform_root(args.platform_root)
    source_root = repo_root / "skills"
    target_skills_root = platform_root / "skills"

    try:
        validate_non_overlapping_roots(source_root, platform_root)
        plan = build_plan(source_root, platform_root, platform_root_text)
    except ProjectionError as exc:
        stderr.write(str(exc) + "\n")
        empty_plan = ProjectionPlan(
            source_count_total=exc.source_count,
            entries=tuple(),
        )
        stdout.write(
            render_summary(
                mode=mode,
                platform_root_text=platform_root_text,
                plan=empty_plan,
                result="BLOCKED",
                error=str(exc),
            )
        )
        return 1

    if not args.apply:
        result = "SAFE_TO_APPLY" if plan.conflict_count == 0 else "BLOCKED"
        stdout.write(
            render_summary(
                mode=mode,
                platform_root_text=platform_root_text,
                plan=plan,
                result=result,
                error=(
                    "Differing managed target files require --apply --force"
                    if plan.conflict_count
                    else None
                ),
            )
        )
        return 0 if plan.conflict_count == 0 else 1

    if plan.conflict_count and not args.force:
        stdout.write(
            render_summary(
                mode=mode,
                platform_root_text=platform_root_text,
                plan=plan,
                result="BLOCKED",
                error="Differing managed target files require --force",
            )
        )
        return 1

    for entry in plan.entries:
        if entry.action == "noop":
            continue
        try:
            validate_target_path_for_write(target_skills_root, entry.target_path)
            write_file(entry.target_path, entry.rendered_content)
        except ProjectionError as exc:
            message = str(exc)
            stderr.write(f"{message}\n")
            stdout.write(
                render_summary(
                    mode=mode,
                    platform_root_text=platform_root_text,
                    plan=plan,
                    result="BLOCKED",
                    error=message,
                )
            )
            return 1
        except OSError as exc:
            message = f"Failed to write target file: {entry.target_path}"
            stderr.write(f"{message}: {exc}\n")
            stdout.write(
                render_summary(
                    mode=mode,
                    platform_root_text=platform_root_text,
                    plan=plan,
                    result="BLOCKED",
                    error=message,
                )
            )
            return 1

    stdout.write(
        render_summary(
            mode=mode,
            platform_root_text=platform_root_text,
            plan=plan,
            result="APPLIED",
        )
    )
    return 0


def run(
    argv: Sequence[str] | None = None,
    *,
    repo_root: Path | None = None,
    stdout: TextIO | None = None,
    stderr: TextIO | None = None,
    write_file: Callable[[Path, str], None] = write_rendered_file,
) -> int:
    stdout = stdout or sys.stdout
    stderr = stderr or sys.stderr
    try:
        with contextlib.redirect_stderr(stderr):
            args = parse_args(argv)
    except SystemExit as exc:
        return int(exc.code)

    if repo_root is None:
        try:
            resolved_repo_root = repo_root_from_script()
        except ProjectionError as exc:
            mode = "apply" if args.apply else "dry-run"
            platform_root_text = normalize_platform_root(args.platform_root)
            stderr.write(str(exc) + "\n")
            stdout.write(
                render_summary(
                    mode=mode,
                    platform_root_text=platform_root_text,
                    plan=ProjectionPlan(source_count_total=0, entries=tuple()),
                    result="BLOCKED",
                    error=str(exc),
                )
            )
            return 1
    else:
        resolved_repo_root = repo_root
    return execute_projection(
        args,
        repo_root=resolved_repo_root,
        stdout=stdout,
        stderr=stderr,
        write_file=write_file,
    )


def main(argv: Sequence[str] | None = None) -> int:
    return run(argv)


if __name__ == "__main__":
    raise SystemExit(main())
