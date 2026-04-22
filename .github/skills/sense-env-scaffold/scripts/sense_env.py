#!/usr/bin/env python3
"""
sense_env.py — Repository environment sensing scaffold (v1).

Supported assertion kinds: path_exists, path_type, command_available.
This script uses only Python standard-library modules.

This script lives at .github/skills/sense-env-scaffold/scripts/sense_env.py.

Supported assertion kinds (v1): path_exists, path_type, command_available.
Unknown kinds in acceptance mode cause exit 30 (contract error).

Exit codes:
    0  — success
    10 — operational error (I/O failure writing manifest)
    20 — acceptance failure (one or more assertions evaluated as FAIL)
    30 — contract error (missing/unreadable file, missing fenced block,
         malformed block, or unknown assertion kind in acceptance mode)

On I/O failure, the script attempts to emit the manifest JSON to stderr
as a fallback before returning exit 10.
"""

from __future__ import annotations

import argparse
import datetime
import json
import os
import re
import shutil
import subprocess
import sys
from pathlib import Path
from typing import Any

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

SCRIPT_VERSION = "1.0.0"
SCHEMA_VERSION = "1"

EXIT_OK = 0
EXIT_IO_ERROR = 10
EXIT_ACCEPTANCE_FAIL = 20
EXIT_CONTRACT_ERROR = 30

FENCED_BLOCK_RE = re.compile(
    r"^\s*```yaml\s+\[sensing-assertions\]\s*\r?\n(.*?)```",
    re.MULTILINE | re.DOTALL,
)

KEY_PATHS = [
    "README.md",
    ".github/",
    "pyproject.toml",
    "tests/",
    "scripts/",
    ".github/copilot-instructions.md",
]

SECRET_PATTERNS = re.compile(
    r"(token|secret|password|api_key|apikey|credential|auth)",
    re.IGNORECASE,
)


class UnsupportedAssertionKindError(ValueError):
    """Raised when an assertion kind is outside the v1 supported subset."""

# ---------------------------------------------------------------------------
# Repo-root detection
# ---------------------------------------------------------------------------


def find_repo_root(start: Path) -> Path:
    """Search upward from start for a .git directory or file."""
    current = start.resolve()
    while True:
        candidate = current / ".git"
        if candidate.exists():
            return current
        parent = current.parent
        if parent == current:
            return start.resolve()
        current = parent


# ---------------------------------------------------------------------------
# Manifest construction helpers
# ---------------------------------------------------------------------------


def make_meta(mode: str) -> dict[str, str]:
    return {
        "schema_version": SCHEMA_VERSION,
        "run_mode": mode,
        "timestamp_utc": datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "script_version": SCRIPT_VERSION,
    }


def make_fingerprint(repo_root: Path) -> dict[str, Any]:
    marker = ".git"
    if not (repo_root / ".git").exists():
        marker = None  # type: ignore[assignment]
    vi = sys.version_info
    return {
        "repo_root_marker": marker,
        "python_version": f"{vi.major}.{vi.minor}.{vi.micro}",
        "platform": sys.platform,
    }


def make_facts(repo_root: Path) -> dict[str, Any]:
    repo_present = (repo_root / ".git").exists()

    git_available = False
    current_branch: str | None = None
    workspace_clean: bool | None = None

    if shutil.which("git"):
        try:
            result = subprocess.run(
                ["git", "rev-parse", "--abbrev-ref", "HEAD"],
                capture_output=True,
                text=True,
                cwd=repo_root,
                timeout=10,
            )
            if result.returncode == 0:
                git_available = True
                current_branch = result.stdout.strip() or None
        except Exception:
            pass

    if git_available:
        try:
            status_result = subprocess.run(
                ["git", "status", "--porcelain"],
                capture_output=True,
                text=True,
                cwd=repo_root,
                timeout=10,
            )
            if status_result.returncode == 0:
                workspace_clean = status_result.stdout.strip() == ""
        except Exception:
            pass

    key_paths: dict[str, bool] = {}
    for rel in KEY_PATHS:
        key_paths[rel] = (repo_root / rel).exists()

    return {
        "repo_present": repo_present,
        "git_available": git_available,
        "current_branch": current_branch,
        "workspace_clean": workspace_clean,
        "key_paths": key_paths,
    }


def make_gap(
    kind: str,
    target: str,
    detail: str,
    remediation_type: str | None,
) -> dict[str, Any]:
    """Build a gap record (without id; caller assigns id before appending)."""
    return {
        "kind": kind,
        "target": target,
        "state": "UNRESOLVED",
        "detail": detail,
        "remediation_type": remediation_type,
    }


def make_assertion_record(
    kind: str,
    target: str,
    state: str,
    expected: Any,
    observed: Any,
    remediation_type: str | None,
) -> dict[str, Any]:
    """Build an assertion record (without id; caller assigns id before appending)."""
    return {
        "kind": kind,
        "target": target,
        "state": state,
        "expected": expected,
        "observed": observed,
        "remediation_type": remediation_type,
    }


# ---------------------------------------------------------------------------
# Contract loading and fenced-block extraction
# ---------------------------------------------------------------------------


def resolve_contract_path(
    contract_file: str | None,
    repo_root: Path,
) -> Path | None:
    if contract_file:
        p = Path(contract_file)
        if not p.is_absolute():
            p = repo_root / p
        return p

    for candidate in ("retrofit-plan.md", "blueprint.md"):
        p = repo_root / candidate
        if p.is_file():
            return p

    return None


def extract_assertions_block(text: str) -> str | None:
    match = FENCED_BLOCK_RE.search(text)
    if match:
        return match.group(1)
    return None


# ---------------------------------------------------------------------------
# Narrow YAML-like assertion parser
# ---------------------------------------------------------------------------
# Supports only:
#   - top-level sequence of mappings
#   - scalar keys and scalar values
#   - no nested mappings, no anchors, no multiline strings,
#     no flow-style collections
# Does NOT claim general YAML compatibility.


def parse_assertions(block: str) -> list[dict[str, str]]:
    """Parse the narrow YAML-like assertion block into a list of dicts."""
    records: list[dict[str, str]] = []
    current: dict[str, str] | None = None

    for raw_line in block.splitlines():
        line = raw_line.strip()

        if not line or line.startswith("#"):
            continue

        if line.startswith("- "):
            if current is not None:
                records.append(current)
            rest = line[2:].strip()
            current = {}
            if rest:
                key, _, value = rest.partition(":")
                current[key.strip()] = value.strip().strip('"').strip("'")
            continue

        if current is not None and ":" in line:
            key, _, value = line.partition(":")
            current[key.strip()] = value.strip().strip('"').strip("'")
            continue

        raise ValueError(f"Unsupported assertion syntax: {raw_line!r}")

    if current is not None:
        records.append(current)

    return records


# ---------------------------------------------------------------------------
# Assertion evaluation
# ---------------------------------------------------------------------------


def evaluate_assertion(
    record: dict[str, str],
    repo_root: Path,
) -> tuple[dict[str, Any], dict[str, Any] | None]:
    """
    Evaluate one assertion record.

    Returns (assertion_record_without_id, gap_without_id | None).
    Raises UnsupportedAssertionKindError for any kind outside the v1 subset.
    """
    kind = record.get("kind", "")
    target = record.get("target", "")
    expected_raw = record.get("expected", "")

    if kind == "path_exists":
        expected = expected_raw.lower() in ("true", "yes", "1")
        observed = (repo_root / target).exists()
        state = "PASS" if observed == expected else "FAIL"
        gap = None
        if state == "FAIL":
            remediation = "CREATE_FILE" if expected else "REMOVE_PATH"
            gap = make_gap(
                kind,
                target,
                f"path_exists: expected {expected}, got {observed}",
                remediation,
            )
        return make_assertion_record(kind, target, state, expected, observed, None if state == "PASS" else remediation), gap

    if kind == "path_type":
        path = repo_root / target
        if path.is_dir():
            observed: Any = "directory"
        elif path.is_file():
            observed = "file"
        else:
            observed = None
        expected = expected_raw.strip()
        state = "PASS" if observed == expected else "FAIL"
        gap = None
        if state == "FAIL":
            remediation = "CREATE_PATH" if observed is None else "FIX_PATH_TYPE"
            gap = make_gap(
                kind,
                target,
                f"path_type: expected {expected!r}, got {observed!r}",
                remediation,
            )
        return make_assertion_record(kind, target, state, expected, observed, None if state == "PASS" else remediation), gap

    if kind == "command_available":
        expected = expected_raw.lower() in ("true", "yes", "1")
        observed = shutil.which(target) is not None
        state = "PASS" if observed == expected else "FAIL"
        gap = None
        if state == "FAIL":
            remediation = "INSTALL_TOOL" if expected else "REMOVE_TOOL"
            gap = make_gap(
                kind,
                target,
                f"command_available: expected {expected}, got {observed}",
                remediation,
            )
        return make_assertion_record(kind, target, state, expected, observed, None if state == "PASS" else remediation), gap

    # Unknown assertion kind — contract error in acceptance mode
    raise UnsupportedAssertionKindError(
        f"assertion kind {kind!r} is not in the v1 supported subset "
        f"(path_exists, path_type, command_available)"
    )


# ---------------------------------------------------------------------------
# Snapshot shaping
# ---------------------------------------------------------------------------


def _is_secret_shaped(key: str, value: Any) -> bool:
    if isinstance(value, str) and SECRET_PATTERNS.search(key):
        return True
    return False


def shape_snapshot(manifest: dict[str, Any], repo_root: Path) -> dict[str, Any]:
    """Return a copy of the manifest with machine-local data removed."""
    import copy

    snapshot = copy.deepcopy(manifest)

    # Fingerprint: remove platform-specific fields beyond the allowed set
    fp = snapshot.get("fingerprint", {})
    allowed_fp = {"repo_root_marker", "python_version", "platform"}
    for key in list(fp.keys()):
        if key not in allowed_fp:
            del fp[key]

    # Facts: normalize current_branch (keep), strip machine-specific data
    facts = snapshot.get("facts", {})
    # Remove any absolute path values inside key_paths
    key_paths = facts.get("key_paths", {})
    for k, v in list(key_paths.items()):
        if isinstance(v, str) and os.path.isabs(v):
            key_paths[k] = None

    # Remove any top-level secret-shaped fields from facts
    for k in list(facts.keys()):
        if _is_secret_shaped(k, facts[k]):
            del facts[k]

    return snapshot


# ---------------------------------------------------------------------------
# Manifest output
# ---------------------------------------------------------------------------


def write_manifest(manifest: dict[str, Any], output_path: Path) -> None:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(manifest, f, indent=2, ensure_ascii=False)
        f.write("\n")


def _try_emit(manifest: dict[str, Any], output_path: Path) -> bool:
    """
    Try to write manifest to output_path.
    On failure, annotates manifest with the error and emits to stderr.
    Returns True if written to disk, False if fell back to stderr.
    """
    try:
        write_manifest(manifest, output_path)
        return True
    except Exception as exc:
        manifest.setdefault("meta", {})["error"] = str(exc)
        try:
            print(json.dumps(manifest, indent=2, ensure_ascii=False), file=sys.stderr)
        except Exception:
            pass
        return False


# ---------------------------------------------------------------------------
# Run modes
# ---------------------------------------------------------------------------


def run_discovery(repo_root: Path, output_path: Path, snapshot: bool) -> int:
    manifest: dict[str, Any] = {
        "meta": make_meta("discovery"),
        "fingerprint": make_fingerprint(repo_root),
        "facts": make_facts(repo_root),
        "assertions": [],
        "gaps": [],
    }

    if not _try_emit(manifest, output_path):
        return EXIT_IO_ERROR

    if snapshot:
        snap = shape_snapshot(manifest, repo_root)
        snap_path = repo_root / ".github" / "env-manifest.snapshot.json"
        if not _try_emit(snap, snap_path):
            return EXIT_IO_ERROR

    return EXIT_OK


def run_acceptance(
    repo_root: Path,
    output_path: Path,
    contract_file: str | None,
    snapshot: bool,
) -> int:
    contract_path = resolve_contract_path(contract_file, repo_root)

    if contract_path is None or not contract_path.is_file():
        manifest: dict[str, Any] = {
            "meta": make_meta("acceptance"),
            "fingerprint": make_fingerprint(repo_root),
            "facts": make_facts(repo_root),
            "assertions": [],
            "gaps": [
                {
                    "id": "g0",
                    **make_gap(
                        "CONTRACT_MISSING",
                        str(contract_path) if contract_path else "<none>",
                        "no readable contract file found",
                        "LOCATE_CONTRACT_FILE",
                    ),
                }
            ],
        }
        _try_emit(manifest, output_path)
        return EXIT_CONTRACT_ERROR

    try:
        contract_text = contract_path.read_text(encoding="utf-8")
    except Exception:
        manifest = {
            "meta": make_meta("acceptance"),
            "fingerprint": make_fingerprint(repo_root),
            "facts": make_facts(repo_root),
            "assertions": [],
            "gaps": [
                {
                    "id": "g0",
                    **make_gap(
                        "CONTRACT_MISSING",
                        str(contract_path),
                        "contract file not readable",
                        "LOCATE_CONTRACT_FILE",
                    ),
                }
            ],
        }
        _try_emit(manifest, output_path)
        return EXIT_CONTRACT_ERROR

    block = extract_assertions_block(contract_text)
    if block is None:
        manifest = {
            "meta": make_meta("acceptance"),
            "fingerprint": make_fingerprint(repo_root),
            "facts": make_facts(repo_root),
            "assertions": [],
            "gaps": [
                {
                    "id": "g0",
                    **make_gap(
                        "CONTRACT_MALFORMED",
                        str(contract_path),
                        "no ```yaml [sensing-assertions] block found in contract",
                        "REVISE_CONTRACT",
                    ),
                }
            ],
        }
        _try_emit(manifest, output_path)
        return EXIT_CONTRACT_ERROR

    try:
        raw_records = parse_assertions(block)
    except ValueError as exc:
        manifest = {
            "meta": make_meta("acceptance"),
            "fingerprint": make_fingerprint(repo_root),
            "facts": make_facts(repo_root),
            "assertions": [],
            "gaps": [
                {
                    "id": "g0",
                    **make_gap(
                        "CONTRACT_MALFORMED",
                        str(contract_path),
                        f"malformed assertion block: {exc}",
                        "REVISE_CONTRACT",
                    ),
                }
            ],
        }
        _try_emit(manifest, output_path)
        return EXIT_CONTRACT_ERROR

    assertion_results: list[dict[str, Any]] = []
    gaps: list[dict[str, Any]] = []
    any_fail = False
    gap_idx = 0

    try:
        for idx, record in enumerate(raw_records):
            a_dict, g_dict = evaluate_assertion(record, repo_root)
            a_dict["id"] = f"a{idx}"
            assertion_results.append(a_dict)
            if g_dict is not None:
                g_dict["id"] = f"g{gap_idx}"
                gap_idx += 1
                gaps.append(g_dict)
            if a_dict["state"] == "FAIL":
                any_fail = True
    except UnsupportedAssertionKindError as exc:
        manifest = {
            "meta": make_meta("acceptance"),
            "fingerprint": make_fingerprint(repo_root),
            "facts": make_facts(repo_root),
            "assertions": assertion_results,
            "gaps": [
                {
                    "id": f"g{gap_idx}",
                    **make_gap(
                        "CONTRACT_ERROR",
                        "<assertion>",
                        str(exc),
                        "REVISE_CONTRACT",
                    ),
                }
            ],
        }
        _try_emit(manifest, output_path)
        return EXIT_CONTRACT_ERROR

    manifest = {
        "meta": make_meta("acceptance"),
        "fingerprint": make_fingerprint(repo_root),
        "facts": make_facts(repo_root),
        "assertions": assertion_results,
        "gaps": gaps,
    }

    if not _try_emit(manifest, output_path):
        return EXIT_IO_ERROR

    if any_fail:
        return EXIT_ACCEPTANCE_FAIL

    if snapshot:
        snap = shape_snapshot(manifest, repo_root)
        snap_path = repo_root / ".github" / "env-manifest.snapshot.json"
        if not _try_emit(snap, snap_path):
            return EXIT_IO_ERROR

    return EXIT_OK


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------


def main() -> int:
    parser = argparse.ArgumentParser(
        description=(
            "Repository environment sensing scaffold (v1). "
            "Supports assertion kinds: path_exists, path_type, command_available. "
            "Does not claim general YAML support."
        )
    )
    parser.add_argument(
        "--mode",
        required=True,
        choices=["discovery", "acceptance"],
        help="Run mode: 'discovery' collects facts; 'acceptance' evaluates contract assertions.",
    )
    parser.add_argument(
        "--contract-file",
        default=None,
        help=(
            "Path to contract document containing a ```yaml [sensing-assertions] block. "
            "Acceptance mode only. Falls back to retrofit-plan.md then blueprint.md."
        ),
    )
    parser.add_argument(
        "--output",
        default=None,
        help=(
            "Output path for the live manifest JSON. "
            "Defaults to <repo_root>/.github/env-manifest.json."
        ),
    )
    parser.add_argument(
        "--snapshot",
        action="store_true",
        default=False,
        help=(
            "Also write a filtered snapshot to "
            "<repo_root>/.github/env-manifest.snapshot.json "
            "(only when the run exits 0)."
        ),
    )

    args = parser.parse_args()

    repo_root = find_repo_root(Path.cwd())

    if args.output:
        output_path = Path(args.output)
        if not output_path.is_absolute():
            output_path = repo_root / output_path
    else:
        output_path = repo_root / ".github" / "env-manifest.json"

    if args.mode == "discovery":
        return run_discovery(repo_root, output_path, args.snapshot)
    else:
        return run_acceptance(repo_root, output_path, args.contract_file, args.snapshot)


if __name__ == "__main__":
    sys.exit(main())
