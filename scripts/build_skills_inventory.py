# /// script
# requires-python = ">=3.11"
# ///
"""Build a deterministic inventory for canonical skills only.

This script is intentionally bounded to canonical `skills/` roots at the
repository top level. Each first-level directory that contains `SKILL.md`
becomes exactly one inventory record in `artifacts/skills-inventory.jsonl`.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import tempfile
from dataclasses import dataclass
from pathlib import Path


JUNK_DIR_NAMES = {
    "__pycache__",
    ".pytest_cache",
    ".mypy_cache",
    ".ruff_cache",
}
JUNK_FILE_NAMES = {".DS_Store"}
JUNK_FILE_SUFFIXES = {".pyc"}


@dataclass(frozen=True)
class SkillRecord:
    canonical_path: str
    tree_hash: str

    def to_json_line(self) -> str:
        return json.dumps(
            {
                "canonical_path": self.canonical_path,
                "tree_hash": self.tree_hash,
            },
            ensure_ascii=True,
            sort_keys=True,
            separators=(",", ":"),
        )


def discover_skill_roots(repo_root: Path) -> list[Path]:
    """Return canonical skill roots under top-level `skills/` only."""
    skills_root = repo_root / "skills"
    if not skills_root.is_dir():
        raise FileNotFoundError(f"Canonical skills directory not found: {skills_root}")

    roots: list[Path] = []
    for candidate in sorted(skills_root.iterdir(), key=lambda path: path.name):
        if not candidate.is_dir():
            continue
        if (candidate / "SKILL.md").is_file():
            roots.append(candidate)

    return roots


def is_included_file(path: Path, skill_root: Path) -> bool:
    """Return True when a path participates in the tree hash contract."""
    if path.is_symlink():
        return False

    if not path.is_file():
        return False

    if path.name in JUNK_FILE_NAMES:
        return False

    if path.suffix in JUNK_FILE_SUFFIXES:
        return False

    relative_parts = path.relative_to(skill_root).parts
    if any(part in JUNK_DIR_NAMES for part in relative_parts[:-1]):
        return False

    return True


def iter_skill_files(skill_root: Path) -> list[Path]:
    """Return all in-scope regular files for one skill root in stable order."""
    included: list[Path] = []

    for current_root, dir_names, file_names in os.walk(skill_root, topdown=True):
        dir_names[:] = sorted(name for name in dir_names if name not in JUNK_DIR_NAMES)
        current_path = Path(current_root)

        for file_name in sorted(file_names):
            candidate = current_path / file_name
            if is_included_file(candidate, skill_root):
                included.append(candidate)

    included.sort(key=lambda path: path.relative_to(skill_root).as_posix())
    return included


def compute_tree_hash(skill_root: Path) -> str:
    """Compute the frozen skill-root-relative SHA-256 stream hash."""
    digest = hashlib.sha256()

    for file_path in iter_skill_files(skill_root):
        relative_path = file_path.relative_to(skill_root).as_posix().encode("utf-8")
        digest.update(relative_path)
        digest.update(b"\0")
        digest.update(file_path.read_bytes())
        digest.update(b"\0")

    return digest.hexdigest()


def build_records(repo_root: Path) -> list[SkillRecord]:
    """Create deterministic inventory records for canonical skill roots."""
    records: list[SkillRecord] = []

    for skill_root in discover_skill_roots(repo_root):
        canonical_path = skill_root.relative_to(repo_root).as_posix()
        records.append(
            SkillRecord(
                canonical_path=canonical_path,
                tree_hash=compute_tree_hash(skill_root),
            )
        )

    records.sort(key=lambda record: record.canonical_path)
    return records


def serialize_records(records: list[SkillRecord]) -> str:
    """Serialize records as UTF-8 JSONL with trailing newline."""
    if not records:
        return ""

    return "".join(f"{record.to_json_line()}\n" for record in records)


def validate_inventory_text(inventory_text: str, expected_count: int) -> None:
    """Validate JSONL parseability, required fields, and record cardinality."""
    if expected_count == 0:
        if inventory_text != "":
            raise ValueError("Expected empty artifact text for zero records")
        return

    lines = inventory_text.splitlines()
    if len(lines) != expected_count:
        raise ValueError(
            f"Inventory line count mismatch: expected {expected_count}, got {len(lines)}"
        )

    seen_paths: set[str] = set()
    for index, line in enumerate(lines, start=1):
        payload = json.loads(line)
        if not isinstance(payload, dict):
            raise ValueError(f"Inventory line {index} is not a JSON object")

        canonical_path = payload.get("canonical_path")
        tree_hash = payload.get("tree_hash")

        if not isinstance(canonical_path, str) or not canonical_path:
            raise ValueError(f"Inventory line {index} has empty canonical_path")
        if not canonical_path.startswith("skills/"):
            raise ValueError(
                f"Inventory line {index} is outside canonical skills/: {canonical_path}"
            )
        if canonical_path in seen_paths:
            raise ValueError(f"Duplicate canonical_path detected: {canonical_path}")
        seen_paths.add(canonical_path)

        if not isinstance(tree_hash, str) or not tree_hash:
            raise ValueError(f"Inventory line {index} has empty tree_hash")


def write_inventory(repo_root: Path, output_path: Path) -> list[SkillRecord]:
    """Build, validate, and safely publish the inventory artifact."""
    records = build_records(repo_root)
    inventory_text = serialize_records(records)
    validate_inventory_text(inventory_text, expected_count=len(records))

    output_path.parent.mkdir(parents=True, exist_ok=True)
    fd, temp_path_str = tempfile.mkstemp(
        prefix=f".{output_path.name}.",
        suffix=".tmp",
        dir=output_path.parent,
        text=True,
    )
    temp_path = Path(temp_path_str)

    try:
        with os.fdopen(fd, "w", encoding="utf-8", newline="\n") as handle:
            handle.write(inventory_text)

        temp_text = temp_path.read_text(encoding="utf-8")
        validate_inventory_text(temp_text, expected_count=len(records))
        os.replace(temp_path, output_path)
    except Exception:
        temp_path.unlink(missing_ok=True)
        raise

    return records


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Build artifacts/skills-inventory.jsonl from canonical skills/"
    )
    parser.add_argument(
        "--repo-root",
        type=Path,
        default=Path(__file__).resolve().parents[1],
        help="Repository root to scan. Defaults to the parent of scripts/.",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=None,
        help="Output path for the JSONL artifact. Defaults to <repo-root>/artifacts/skills-inventory.jsonl.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    repo_root = args.repo_root.resolve()
    output_path = (
        args.output.resolve()
        if args.output is not None
        else repo_root / "artifacts" / "skills-inventory.jsonl"
    )

    try:
        records = write_inventory(repo_root, output_path)
    except Exception as exc:
        print(f"ERROR: {exc}")
        return 1

    print(f"Wrote {len(records)} records to {output_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
