# /// script
# requires-python = ">=3.11"
# ///
"""Apply tool configuration sections to pyproject.toml.

Detects existing [tool.*] sections via tomllib and appends only missing ones
from the skill's templates directory. Outputs changes to stdout for review
before writing to disk.
"""
import argparse
import re
import tomllib
from pathlib import Path


def _apply_substitutions(content: str, python_version: str, package_name: str) -> str:
    """Replace template placeholders with actual values.

    Order matters: py${PYTHON_VERSION} must be replaced before ${PYTHON_VERSION}
    so ruff's target-version gets the no-dot form (e.g. py310) while pyright's
    pythonVersion retains the dot form (e.g. 3.10).
    """
    python_version_nodot = python_version.replace(".", "")
    content = re.sub(r"py\$\{PYTHON_VERSION\}", f"py{python_version_nodot}", content)
    content = content.replace("${PYTHON_VERSION}", python_version)
    content = content.replace("${PACKAGE_NAME}", package_name)
    return content


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Append missing [tool.*] sections to pyproject.toml"
    )
    parser.add_argument(
        "--python-version",
        required=True,
        help="Python version for target-version and pythonVersion (e.g., 3.10)",
    )
    parser.add_argument(
        "--package-name",
        required=True,
        help="Package name for pyright include path (e.g., mylib)",
    )
    args = parser.parse_args()

    pyproject_path = Path("pyproject.toml")
    if not pyproject_path.exists():
        raise FileNotFoundError(f"pyproject.toml not found in {Path.cwd()}")

    with pyproject_path.open("rb") as f:
        data = tomllib.load(f)

    existing_tools: set[str] = set(data.get("tool", {}).keys())

    skill_dir = Path(__file__).parent.parent
    templates_dir = skill_dir / "templates"

    sections_to_append: list[str] = []

    for tmpl_name, section_key in [
        ("toolconfig-ruff.toml.tmpl", "ruff"),
        ("toolconfig-pyright.toml.tmpl", "pyright"),
        ("toolconfig-pytest.toml.tmpl", "pytest"),
    ]:
        if section_key in existing_tools:
            print(f"ℹ️  [tool.{section_key}] already exists — skipping")
            continue

        tmpl_path = templates_dir / tmpl_name
        content = _apply_substitutions(
            tmpl_path.read_text(), args.python_version, args.package_name
        )
        sections_to_append.append(content)
        print(f"✅ Will append [tool.{section_key}]")

    if not sections_to_append:
        print("ℹ️  All tool sections already exist — nothing to append")
        return

    with pyproject_path.open("a") as f:
        f.write("\n" + "\n\n".join(sections_to_append) + "\n")

    print(f"\n✅ Appended {len(sections_to_append)} section(s) to {pyproject_path}")


if __name__ == "__main__":
    main()
