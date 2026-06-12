from __future__ import annotations

import importlib.util
import io
import sys
from pathlib import Path

import pytest


SCRIPT_PATH = (
    Path(__file__).resolve().parents[1]
    / "scripts"
    / "platform_projection_adapter.py"
)


def load_adapter_module(script_path: Path, module_name: str):
    spec = importlib.util.spec_from_file_location(module_name, script_path)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


@pytest.fixture
def adapter_module():
    return load_adapter_module(SCRIPT_PATH, "platform_projection_adapter")


def run_adapter(adapter_module, repo_root: Path | None, *args: str, write_file=None):
    stdout = io.StringIO()
    stderr = io.StringIO()
    kwargs = {"stdout": stdout, "stderr": stderr}
    if repo_root is not None:
        kwargs["repo_root"] = repo_root
    if write_file is not None:
        kwargs["write_file"] = write_file
    exit_code = adapter_module.run(list(args), **kwargs)
    return exit_code, stdout.getvalue(), stderr.getvalue()


def write_text(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def make_repo(tmp_path: Path) -> Path:
    repo_root = tmp_path / "repo"
    skills_root = repo_root / "skills"
    write_text(repo_root / "AGENTS.md", "# test repo\n")
    write_text(
        skills_root / "alpha" / "SKILL.md",
        "Alpha uses .codex/skills/alpha/SKILL.md and skills/alpha/SKILL.md.\n",
    )
    write_text(
        skills_root / "alpha" / "reference.md",
        "Provenance lives at .codex/skills-provenance.json.\n",
    )
    write_text(
        skills_root / "nested" / "guides" / "note.md",
        "Nested file.\n",
    )
    return repo_root


def test_platform_root_is_required(adapter_module, tmp_path: Path):
    repo_root = make_repo(tmp_path)
    exit_code, stdout, stderr = run_adapter(adapter_module, repo_root)

    assert exit_code == 2
    assert stdout == ""
    assert "--platform-root" in stderr


def test_dry_run_reports_summary_without_writing(adapter_module, tmp_path: Path):
    repo_root = make_repo(tmp_path)
    target_root = tmp_path / ".codex"

    exit_code, stdout, stderr = run_adapter(
        adapter_module,
        repo_root,
        "--platform-root",
        str(target_root),
    )

    assert exit_code == 0
    assert stderr == ""
    assert "mode: dry-run" in stdout
    assert f"platform_root: {target_root.as_posix()}" in stdout
    assert "source_count: 3" in stdout
    assert "create: 3" in stdout
    assert "update: 0" in stdout
    assert "noop: 0" in stdout
    assert "conflicts: 0" in stdout
    assert "result: SAFE_TO_APPLY" in stdout
    assert not (target_root / "skills").exists()


def test_dry_run_ignores_runtime_cache_junk(adapter_module, tmp_path: Path):
    repo_root = make_repo(tmp_path)
    pycache_root = repo_root / "skills" / "alpha" / "__pycache__"
    pycache_root.mkdir(parents=True, exist_ok=True)
    (pycache_root / "ignored.cpython-311.pyc").write_bytes(b"\xff\xfe\xfd")
    (repo_root / "skills" / "alpha" / "ignored.pyo").write_bytes(b"\xff\xfe\xfd")
    target_root = tmp_path / ".codex"

    exit_code, stdout, stderr = run_adapter(
        adapter_module,
        repo_root,
        "--platform-root",
        str(target_root),
    )

    assert exit_code == 0
    assert stderr == ""
    assert "source_count: 3" in stdout
    assert "__pycache__" not in stdout
    assert "ignored.pyo" not in stdout
    assert "result: SAFE_TO_APPLY" in stdout


@pytest.mark.parametrize(
    ("platform_root", "expected_fragment"),
    [
        pytest.param("repo-root", "source=", id="equal-to-canonical"),
        pytest.param("nested-under-skills", "target=", id="target-inside-canonical"),
    ],
)
def test_platform_root_overlap_fails_fast(
    adapter_module,
    tmp_path: Path,
    platform_root: str,
    expected_fragment: str,
):
    repo_root = make_repo(tmp_path)
    if platform_root == "repo-root":
        overlap_root = repo_root
    else:
        overlap_root = repo_root / "skills" / "projection-root"

    exit_code, stdout, stderr = run_adapter(
        adapter_module,
        repo_root,
        "--platform-root",
        str(overlap_root),
    )

    assert exit_code == 1
    assert "Platform root would overlap canonical skills/" in stderr
    assert "result: BLOCKED" in stdout
    assert "Platform root would overlap canonical skills/" in stdout
    assert expected_fragment in stdout


def test_apply_creates_targets_and_rewrites_placeholders(adapter_module, tmp_path: Path):
    repo_root = make_repo(tmp_path)
    target_root = tmp_path / ".codex"

    exit_code, stdout, stderr = run_adapter(
        adapter_module,
        repo_root,
        "--platform-root",
        str(target_root),
        "--apply",
    )

    assert exit_code == 0
    assert stderr == ""
    assert "mode: apply" in stdout
    assert "result: APPLIED" in stdout

    projected_skill = target_root / "skills" / "alpha" / "SKILL.md"
    assert projected_skill.exists()
    assert (
        projected_skill.read_text(encoding="utf-8")
        == f"Alpha uses {target_root.as_posix()}/skills/alpha/SKILL.md and skills/alpha/SKILL.md.\n"
    )
    assert (
        (target_root / "skills" / "alpha" / "reference.md").read_text(encoding="utf-8")
        == f"Provenance lives at {target_root.as_posix()}/skills-provenance.json.\n"
    )
    assert (target_root / "skills" / "nested" / "guides" / "note.md").exists()


def test_root_platform_projection_preserves_single_slash(adapter_module, tmp_path: Path):
    repo_root = make_repo(tmp_path)
    source_path = repo_root / "skills" / "alpha" / "SKILL.md"

    assert adapter_module.normalize_platform_root("/") == "/"
    assert (
        adapter_module.render_source(source_path, "/")
        == "Alpha uses /skills/alpha/SKILL.md and skills/alpha/SKILL.md.\n"
    )


def test_projected_codex_copy_runs_as_standalone_entrypoint(tmp_path: Path):
    repo_root = make_repo(tmp_path)
    projected_script = (
        repo_root
        / ".codex"
        / "skills"
        / "platform-projection-adapter"
        / "scripts"
        / "platform_projection_adapter.py"
    )
    write_text(projected_script, SCRIPT_PATH.read_text(encoding="utf-8"))
    projected_module = load_adapter_module(
        projected_script,
        "platform_projection_adapter_projected",
    )
    target_root = tmp_path / ".codex-target"

    exit_code, stdout, stderr = run_adapter(
        projected_module,
        None,
        "--platform-root",
        str(target_root),
    )

    assert exit_code == 0
    assert stderr == ""
    assert "mode: dry-run" in stdout
    assert "source_count: 3" in stdout
    assert "result: SAFE_TO_APPLY" in stdout
    assert not (target_root / "skills").exists()

def test_repo_root_autodiscovery_failure_blocks_when_markers_are_missing(tmp_path: Path):
    detached_root = tmp_path / "detached"
    detached_script = (
        detached_root / "scripts" / "platform_projection_adapter.py"
    )
    write_text(detached_script, SCRIPT_PATH.read_text(encoding="utf-8"))
    detached_module = load_adapter_module(
        detached_script,
        "platform_projection_adapter_detached",
    )
    target_root = tmp_path / ".codex-target"

    exit_code, stdout, stderr = run_adapter(
        detached_module,
        None,
        "--platform-root",
        str(target_root),
    )

    assert exit_code == 1
    assert "Failed to locate repository root from script path" in stderr
    assert "result: BLOCKED" in stdout
    assert "Failed to locate repository root from script path" in stdout
    assert not (target_root / "skills").exists()


def test_apply_blocks_on_differing_target_without_force(adapter_module, tmp_path: Path):
    repo_root = make_repo(tmp_path)
    target_root = tmp_path / ".codex"
    target_file = target_root / "skills" / "alpha" / "SKILL.md"
    write_text(target_file, "manual change\n")

    exit_code, stdout, stderr = run_adapter(
        adapter_module,
        repo_root,
        "--platform-root",
        str(target_root),
        "--apply",
    )

    assert exit_code == 1
    assert stderr == ""
    assert "update: 1" in stdout
    assert "conflicts: 1" in stdout
    assert "result: BLOCKED" in stdout
    assert "--force" in stdout
    assert target_file.read_text(encoding="utf-8") == "manual change\n"


def test_apply_force_overwrites_differing_targets(adapter_module, tmp_path: Path):
    repo_root = make_repo(tmp_path)
    target_root = tmp_path / ".codex"
    target_file = target_root / "skills" / "alpha" / "SKILL.md"
    write_text(target_file, "manual change\n")

    exit_code, stdout, stderr = run_adapter(
        adapter_module,
        repo_root,
        "--platform-root",
        str(target_root),
        "--apply",
        "--force",
    )

    assert exit_code == 0
    assert stderr == ""
    assert "update: 1" in stdout
    assert "conflicts: 1" in stdout
    assert "result: APPLIED" in stdout
    assert (
        target_file.read_text(encoding="utf-8")
        == f"Alpha uses {target_root.as_posix()}/skills/alpha/SKILL.md and skills/alpha/SKILL.md.\n"
    )


def test_rerun_after_success_becomes_noop(adapter_module, tmp_path: Path):
    repo_root = make_repo(tmp_path)
    target_root = tmp_path / ".codex"

    apply_code, _, _ = run_adapter(
        adapter_module,
        repo_root,
        "--platform-root",
        str(target_root),
        "--apply",
    )
    dry_run_code, stdout, stderr = run_adapter(
        adapter_module,
        repo_root,
        "--platform-root",
        str(target_root),
    )

    assert apply_code == 0
    assert dry_run_code == 0
    assert stderr == ""
    assert "create: 0" in stdout
    assert "update: 0" in stdout
    assert "noop: 3" in stdout
    assert "conflicts: 0" in stdout
    assert "result: SAFE_TO_APPLY" in stdout


def test_invalid_utf8_source_fails_fast(adapter_module, tmp_path: Path):
    repo_root = tmp_path / "repo"
    source_root = repo_root / "skills"
    (source_root / "broken").mkdir(parents=True, exist_ok=True)
    (source_root / "broken" / "SKILL.md").write_bytes(b"\xff\xfe\xfd")
    target_root = tmp_path / ".codex"

    exit_code, stdout, stderr = run_adapter(
        adapter_module,
        repo_root,
        "--platform-root",
        str(target_root),
    )

    assert exit_code == 1
    assert "Failed to decode UTF-8 source file" in stderr
    assert "result: BLOCKED" in stdout
    assert "Failed to decode UTF-8 source file" in stdout
    assert not target_root.exists()


def test_unreadable_source_fails_fast(adapter_module, tmp_path: Path, monkeypatch):
    repo_root = make_repo(tmp_path)
    target_root = tmp_path / ".codex"
    broken_source = repo_root / "skills" / "alpha" / "reference.md"
    original_read_text = adapter_module.Path.read_text

    def fake_read_text(path_self, *args, **kwargs):
        if path_self == broken_source:
            raise PermissionError("permission denied")
        return original_read_text(path_self, *args, **kwargs)

    monkeypatch.setattr(adapter_module.Path, "read_text", fake_read_text)

    exit_code, stdout, stderr = run_adapter(
        adapter_module,
        repo_root,
        "--platform-root",
        str(target_root),
    )

    assert exit_code == 1
    assert "Failed to read source file" in stderr
    assert "source_count: 3" in stdout
    assert "result: BLOCKED" in stdout
    assert "Failed to read source file" in stdout
    assert not target_root.exists()


@pytest.mark.parametrize(
    ("symlink_target_kind", "force_apply"),
    [
        pytest.param("skills-root", False, id="symlinked-skills-root"),
        pytest.param("leaf-file", True, id="symlinked-leaf-file"),
    ],
)
def test_apply_refuses_symlinked_target_paths(
    adapter_module,
    tmp_path: Path,
    symlink_target_kind: str,
    force_apply: bool,
):
    repo_root = make_repo(tmp_path)
    target_root = tmp_path / ".codex"
    outside_root = tmp_path / "outside"
    outside_root.mkdir(parents=True, exist_ok=True)

    if symlink_target_kind == "skills-root":
        target_root.mkdir(parents=True, exist_ok=True)
        (target_root / "skills").symlink_to(outside_root, target_is_directory=True)
        args = [
            "--platform-root",
            str(target_root),
            "--apply",
        ]
    else:
        target_file = target_root / "skills" / "alpha" / "SKILL.md"
        target_file.parent.mkdir(parents=True, exist_ok=True)
        outside_file = outside_root / "SKILL.md"
        outside_file.write_text("manual change\n", encoding="utf-8")
        target_file.symlink_to(outside_file)
        args = [
            "--platform-root",
            str(target_root),
            "--apply",
            "--force",
        ]

    exit_code, stdout, stderr = run_adapter(
        adapter_module,
        repo_root,
        *args,
    )

    assert exit_code == 1
    assert "Refusing to write through symlinked target path" in stderr
    assert "result: BLOCKED" in stdout
    assert "Refusing to write through symlinked target path" in stdout


def test_partial_apply_reports_failure_and_rerun_recomputes(adapter_module, tmp_path: Path):
    repo_root = make_repo(tmp_path)
    target_root = tmp_path / ".codex"
    original_write = adapter_module.write_rendered_file
    call_count = {"value": 0}

    def flaky_write(target_path: Path, rendered_content: str) -> None:
        call_count["value"] += 1
        if call_count["value"] == 2:
            raise OSError("simulated write failure")
        original_write(target_path, rendered_content)

    exit_code, stdout, stderr = run_adapter(
        adapter_module,
        repo_root,
        "--platform-root",
        str(target_root),
        "--apply",
        write_file=flaky_write,
    )

    assert exit_code == 1
    assert "result: BLOCKED" in stdout
    assert "Failed to write target file" in stdout
    assert "simulated write failure" in stderr

    dry_run_code, dry_run_stdout, dry_run_stderr = run_adapter(
        adapter_module,
        repo_root,
        "--platform-root",
        str(target_root),
    )

    assert dry_run_code == 0
    assert dry_run_stderr == ""
    assert "create: 2" in dry_run_stdout
    assert "update: 0" in dry_run_stdout
    assert "noop: 1" in dry_run_stdout
    assert "conflicts: 0" in dry_run_stdout
    assert "result: SAFE_TO_APPLY" in dry_run_stdout
