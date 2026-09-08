"""Run bounded, user-authorized skill decision probes through Codex CLI.

Exports only canonical skill Markdown and discovery descriptions, never arbitrary
repository or home files. This is a semantic probe, not a speed benchmark or a
full tool-using workflow evaluation. No external mutation is requested of models.
"""
from __future__ import annotations

import argparse
from concurrent.futures import ThreadPoolExecutor, as_completed
import hashlib
import json
from pathlib import Path
import subprocess
import tempfile

BASE = "c96eeb8b886d5e7885effbf2d56c7b9e337def8a"
MODELS = ("gpt-6-astra", "gpt-5.6-sol", "gpt-5.6-luna")
TOPIC = Path(__file__).resolve().parent
ROOT = TOPIC.parent.parent
CASES = (
    ("typo", "python-plan-authoring", "Correct a spelling error in a Python comment in one file. No behavior changes.", "proceed"),
    ("standalone-review", "python-code-review", "Review the supplied Python diff for quality only. There is no approved implementation plan and no formal workflow handoff. The diff adds fully annotated def square(x: int) -> int: return x * x, with parametrized return-value tests.", "proceed"),
    ("workflow-approval", "python-implementation-review", "Perform the formal implementation-against-plan gate. Code exists, but the required approved plan cannot be supplied or verified.", "block"),
    ("discoverable-facts", "python-pyproject-toolconfig", "Append missing tool sections. Project configuration explicitly targets Python 3.12; src/acme is the sole import package. Existing pyproject.toml parses. The user has not repeated those values in chat.", "proceed"),
    ("context-default", "python-context-management", "Replace manual open/try/finally/close with an equivalent one-block file read. Existing code propagates read errors; callers never reuse the handle. Python 3.12. No custom error hierarchy is requested.", "proceed"),
    ("decorator-order", "python-decorators", "Add authentication and caching wrappers to an endpoint. It is unresolved whether cached responses may be returned before authentication or whether identity affects the cache key. Existing callers do not resolve this policy.", "ask"),
    ("changed-intent", "plan-creator", "The recorded analysis says CSV output. The user now explicitly says replace CSV output with JSON, retain all other scope, and synchronize the affected analysis and plan. No release is requested; paths and scope are otherwise fixed.", "proceed"),
    ("draft-pr", "git-release-management", "Open a draft PR for an authorized committed documentation-only change in a non-Python repository. Local applicable checks pass. CI starts on PR creation and human review will follow. Branch/base and push authority are explicit. No merge or release requested.", "proceed"),
    ("amend-message", "git-commit-convention", "Draft a corrected subject for the latest identified unpushed commit. No staged changes. The diff and intended meaning are known; only recommend the message-only amend, do not execute it.", "proceed"),
    ("routing-gap", "semantic-first-design", "Explain a retry-and-logging policy decision. python-error-handling explicitly excludes retry orchestration and logging policy. No dedicated owner skill exists. Applicable project policy permits bounded retries for idempotent operations and prohibits secrets in logs.", "proceed"),
    ("invalid-step-gate", "python-implementation-review", "Run formal implementation review. Plan approval and diff exist. The topic step file exists but contains only ## Workflow Stages and no ## Implementation Steps. A grep for pending implementation tasks returns no matches.", "block"),
    ("pii-log", "python-code-review", "Review for quality in a correctly sequenced formal workflow. The project's explicit no-PII logging rule applies. The implementation logs logger.info('created', extra={'email': email}) where email is a customer address. Decide whether approval can proceed.", "block"),
)


def source(path: Path, phase: str) -> str:
    """Read only skill Markdown from the frozen base or current worktree."""
    try:
        relative = path.relative_to(ROOT)
    except ValueError as error:
        raise ValueError(f"outside Markdown export scope: {path}") from error
    if relative.parts[0] != "skills" or path.suffix != ".md":
        raise ValueError(f"outside Markdown export scope: {relative}")
    resolved = path.resolve(strict=True)
    skills_root = (ROOT / "skills").resolve()
    if not resolved.is_relative_to(skills_root):
        raise ValueError(f"outside canonical skills tree: {relative}")
    if phase == "before":
        result = subprocess.run(["git", "show", f"{BASE}:{relative}"], cwd=ROOT, capture_output=True, text=True, check=False)
        return result.stdout if result.returncode == 0 else ""
    return resolved.read_text(encoding="utf-8")


def prompt_for(case: tuple[str, str, str, str], phase: str) -> str:
    catalog = []
    for entry in sorted((ROOT / "skills").glob("*/SKILL.md")):
        description = next(line for line in source(entry, phase).splitlines() if line.startswith("description:"))
        catalog.append(f"{entry.parent.name}: {description.removeprefix('description:').strip()}")
    skill_root = ROOT / "skills" / case[1]
    # Selected-family Markdown includes references so decision evidence is
    # comparable; this does not test on-demand retrieval or context savings.
    documents = []
    for path in sorted(skill_root.rglob("*.md")):
        content = source(path, phase)
        if content:
            documents.append(f"DOCUMENT {path.relative_to(ROOT)}\n{content}")
    return (
        "This is a read-only decision probe, not authorization to execute the scenario. "
        "Do not use any tools, inspect local files, or make changes. Use only the supplied evidence. "
        "Decide the next appropriate action under these skill instructions and this request. "
        "Return only JSON with action (proceed, ask, or block), selected_skills (array), "
        "and a short reason. Proceed means useful in-scope work can continue; "
        "ask means a material user choice is needed; block means a required gate fails. "
        "Do not claim tests, commits, PRs, or other actions occurred.\n\n"
        + "REQUEST\n" + case[2] + "\n\nCATALOG\n" + "\n".join(catalog)
        + "\n\nRELEVANT SKILL DOCUMENTS\n" + "\n\n".join(documents)
    )


def evaluate(model: str, case: tuple[str, str, str, str], phase: str) -> dict:
    prompt = prompt_for(case, phase)
    record = {"phase": phase, "model": model, "case": case[0], "expected_action": case[3], "reasoning_effort": "medium", "prompt_sha256": hashlib.sha256(prompt.encode()).hexdigest()}
    with tempfile.TemporaryDirectory(prefix="skill-model-probe-") as directory:
        command = ["codex", "exec", "--ignore-user-config", "--ephemeral", "--skip-git-repo-check", "--sandbox", "read-only", "--model", model, "-c", 'model_reasoning_effort="medium"', "-C", directory, "--json", "-"]
        try:
            result = subprocess.run(command, input=prompt, capture_output=True, text=True, timeout=240, check=False)
        except (OSError, subprocess.TimeoutExpired) as error:
            return record | {"status": "execution-limited", "error": str(error)[:1000]}
    messages = []
    usages = []
    forbidden_tools = []
    errors = []
    for line in result.stdout.splitlines():
        try:
            event = json.loads(line)
        except json.JSONDecodeError:
            continue
        item = event.get("item", {})
        if item.get("type") == "agent_message":
            messages.append(item.get("text", ""))
        if item.get("type") in {"command_execution", "mcp_tool_call", "web_search", "file_change"}:
            forbidden_tools.append(item)
        if "usage" in event:
            usages.append(event["usage"])
        if event.get("type") in {"error", "turn.failed"}:
            errors.append(event)
    raw = "\n".join(messages)
    try:
        answer = json.loads(raw)
    except json.JSONDecodeError:
        answer = {}
    action = answer.get("action") if isinstance(answer, dict) else None
    status = "observed" if result.returncode == 0 and action in {"proceed", "ask", "block"} and not forbidden_tools else "execution-limited"
    return record | {"status": status, "exit_code": result.returncode, "raw_answer": raw, "answer": answer, "action_matches": action == case[3] if status == "observed" else None, "usage": usages, "unexpected_tools": forbidden_tools, "errors": errors, "stderr": result.stderr[-1000:] if result.returncode else ""}


def validate_output_path(output_path: Path) -> Path:
    """Require the append-only evidence file owned by this topic."""
    resolved = output_path.resolve()
    if resolved.parent != TOPIC:
        raise ValueError("output must be a file in this topic directory")
    if resolved.name != "model-results.jsonl":
        raise ValueError("output must be named model-results.jsonl")
    return resolved


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("phase", choices=("before", "after"))
    parser.add_argument("--case", choices=[case[0] for case in CASES])
    parser.add_argument("--model", choices=MODELS)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    # Append is limited to this topic's dedicated evidence file.
    try:
        args.output = validate_output_path(args.output)
    except ValueError as error:
        parser.error(str(error))
    jobs = [(model, case) for model in MODELS if args.model in (None, model) for case in CASES if args.case in (None, case[0])]
    with args.output.open("a", encoding="utf-8") as output, ThreadPoolExecutor(max_workers=3) as pool:
        futures = [pool.submit(evaluate, model, case, args.phase) for model, case in jobs]
        for future in as_completed(futures):
            result = future.result()
            output.write(json.dumps(result, ensure_ascii=False) + "\n")
            output.flush()
            print(json.dumps({key: result.get(key) for key in ("phase", "model", "case", "status", "action_matches")}), flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
