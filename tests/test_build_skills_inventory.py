"""Tests for scripts/build_skills_inventory.py."""

from __future__ import annotations

import json
import os
import sys
from pathlib import Path

import pytest


sys.path.insert(0, str(Path(__file__).parent.parent / "scripts"))

from build_skills_inventory import build_records, discover_skill_roots, write_inventory


def _write(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def _create_base_repo(tmp_path: Path) -> Path:
    repo_root = tmp_path / "repo"
    repo_root.mkdir()
    _write(repo_root / "VERSION", "0.0.test\n")
    return repo_root


def _create_multi_surface_fixture(repo_root: Path) -> None:
    _write(repo_root / "skills" / "alpha" / "SKILL.md", "# alpha\n")
    _write(repo_root / "skills" / "alpha" / "notes.md", "alpha-notes\n")
    _write(repo_root / "skills" / "beta" / "SKILL.md", "# beta\n")
    _write(repo_root / "skills" / "beta" / "references" / "ref.md", "beta-ref\n")
    _write(repo_root / "skills" / "not-a-skill" / "readme.md", "ignore-me\n")
    _write(repo_root / "skills" / "nested" / "gamma" / "SKILL.md", "# gamma\n")
    _write(repo_root / "agents" / "demo" / "SKILL.md", "# agent\n")
    _write(repo_root / ".github" / "skills" / "gh-skill" / "SKILL.md", "# gh\n")
    _write(repo_root / ".codex" / "skills" / "codex-skill" / "SKILL.md", "# codex\n")
    _write(repo_root / ".claude" / "skills" / "platform-skill" / "SKILL.md", "# platform\n")


def _load_jsonl(path: Path) -> list[dict[str, str]]:
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines()]


def test_discover_skill_roots_only_accepts_top_level_skills_with_skill_md(
    tmp_path: Path,
) -> None:
    repo_root = _create_base_repo(tmp_path)
    _create_multi_surface_fixture(repo_root)

    roots = discover_skill_roots(repo_root)

    assert [root.relative_to(repo_root).as_posix() for root in roots] == [
        "skills/alpha",
        "skills/beta",
    ]


def test_discover_skill_roots_excludes_symlinked_skill_directories(
    tmp_path: Path,
) -> None:
    repo_root = _create_base_repo(tmp_path)
    _write(repo_root / "skills" / "alpha" / "SKILL.md", "# alpha\n")
    real_skill_root = repo_root / "external-skill"
    _write(real_skill_root / "SKILL.md", "# external\n")

    symlink_path = repo_root / "skills" / "linked-skill"
    try:
        os.symlink(real_skill_root, symlink_path, target_is_directory=True)
    except (NotImplementedError, OSError) as exc:
        pytest.skip(f"symlink creation unsupported in this environment: {exc}")

    roots = discover_skill_roots(repo_root)

    assert [root.relative_to(repo_root).as_posix() for root in roots] == ["skills/alpha"]


def test_write_inventory_emits_only_canonical_records_as_valid_jsonl(
    tmp_path: Path,
) -> None:
    repo_root = _create_base_repo(tmp_path)
    _create_multi_surface_fixture(repo_root)
    output_path = repo_root / "artifacts" / "skills-inventory.jsonl"

    records = write_inventory(repo_root, output_path)
    payloads = _load_jsonl(output_path)

    assert len(records) == 2
    assert len(payloads) == 2
    assert [payload["canonical_path"] for payload in payloads] == [
        "skills/alpha",
        "skills/beta",
    ]
    assert all(set(payload) == {"canonical_path", "tree_hash"} for payload in payloads)
    assert all(payload["tree_hash"] for payload in payloads)


def test_write_inventory_is_byte_stable_for_unchanged_input(tmp_path: Path) -> None:
    repo_root = _create_base_repo(tmp_path)
    _create_multi_surface_fixture(repo_root)
    output_path = repo_root / "artifacts" / "skills-inventory.jsonl"

    write_inventory(repo_root, output_path)
    first_bytes = output_path.read_bytes()

    write_inventory(repo_root, output_path)
    second_bytes = output_path.read_bytes()

    assert first_bytes == second_bytes


def test_tree_hash_changes_when_included_file_content_changes(tmp_path: Path) -> None:
    repo_root = _create_base_repo(tmp_path)
    _write(repo_root / "skills" / "alpha" / "SKILL.md", "# alpha\n")
    _write(repo_root / "skills" / "alpha" / "content.md", "v1\n")
    _write(repo_root / "skills" / "beta" / "SKILL.md", "# beta\n")
    _write(repo_root / "skills" / "beta" / "content.md", "stable\n")

    before = {record.canonical_path: record.tree_hash for record in build_records(repo_root)}

    _write(repo_root / "skills" / "alpha" / "content.md", "v2\n")
    after = {record.canonical_path: record.tree_hash for record in build_records(repo_root)}

    assert before["skills/alpha"] != after["skills/alpha"]
    assert before["skills/beta"] == after["skills/beta"]


def test_tree_hash_changes_when_included_file_is_added(tmp_path: Path) -> None:
    repo_root = _create_base_repo(tmp_path)
    _write(repo_root / "skills" / "alpha" / "SKILL.md", "# alpha\n")
    _write(repo_root / "skills" / "alpha" / "content.md", "stable\n")
    _write(repo_root / "skills" / "beta" / "SKILL.md", "# beta\n")
    _write(repo_root / "skills" / "beta" / "content.md", "stable\n")

    before = {record.canonical_path: record.tree_hash for record in build_records(repo_root)}

    _write(repo_root / "skills" / "beta" / "references" / "extra.md", "new-file\n")
    after = {record.canonical_path: record.tree_hash for record in build_records(repo_root)}

    assert before["skills/alpha"] == after["skills/alpha"]
    assert before["skills/beta"] != after["skills/beta"]


def test_tree_hash_ignores_excluded_junk_files(tmp_path: Path) -> None:
    repo_root = _create_base_repo(tmp_path)
    _write(repo_root / "skills" / "alpha" / "SKILL.md", "# alpha\n")
    _write(repo_root / "skills" / "alpha" / "content.md", "stable\n")
    _write(repo_root / "skills" / "beta" / "SKILL.md", "# beta\n")
    _write(repo_root / "skills" / "beta" / "content.md", "stable\n")

    before = {record.canonical_path: record.tree_hash for record in build_records(repo_root)}

    _write(
        repo_root / "skills" / "alpha" / "__pycache__" / "content.cpython-313.pyc",
        "junk\n",
    )
    _write(repo_root / "skills" / "alpha" / ".DS_Store", "junk\n")
    _write(repo_root / "skills" / "alpha" / ".pytest_cache" / "CACHEDIR.TAG", "junk\n")
    _write(repo_root / "skills" / "alpha" / ".mypy_cache" / "meta.json", "junk\n")
    _write(repo_root / "skills" / "alpha" / ".ruff_cache" / "index", "junk\n")
    after = {record.canonical_path: record.tree_hash for record in build_records(repo_root)}

    assert before == after


def test_tree_hash_ignores_symlinked_files(tmp_path: Path) -> None:
    repo_root = _create_base_repo(tmp_path)
    _write(repo_root / "skills" / "alpha" / "SKILL.md", "# alpha\n")
    _write(repo_root / "skills" / "alpha" / "content.md", "stable\n")
    _write(repo_root / "skills" / "beta" / "SKILL.md", "# beta\n")
    _write(repo_root / "skills" / "beta" / "content.md", "stable\n")

    before = {record.canonical_path: record.tree_hash for record in build_records(repo_root)}

    external_target = repo_root / "outside.txt"
    _write(external_target, "outside\n")
    try:
        os.symlink(external_target, repo_root / "skills" / "alpha" / "linked.txt")
    except (NotImplementedError, OSError) as exc:
        pytest.skip(f"symlink creation unsupported in this environment: {exc}")
    after = {record.canonical_path: record.tree_hash for record in build_records(repo_root)}

    assert before == after
