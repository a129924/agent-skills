# Copilot Instructions Init Examples

Use these examples when the concise `SKILL.md` examples are not enough.

## Scenario 1: Greenfield placeholder becomes formal instructions

**Starting point**
- the target repository already has a placeholder `.github/copilot-instructions.md`
- sensing now confirms uv, installed skills, package layout, and entrypoints
- no materially different manual instruction content exists

**Expected behavior**
1. verify the sensed facts are fresh against Git `HEAD`, `pyproject.toml` / `uv.lock`, and `.github/skills/` summary
2. derive the instructions in this order: facts -> installed skills -> plan contract -> human intent
3. replace the placeholder with formal content containing:
   - `## Project Truth`
   - `## Governance`
   - `## Implementation Rules`
4. finish without extra re-sensing because this is first-generation greenfield output

**Anti-pattern**
- keep the placeholder because it is "good enough"
- write generic rules before required facts exist

## Scenario 2: Retrofit follow-up refresh after structure changes

**Starting point**
- `python-project-retrofit` already changed layout or entrypoints
- a sensing delta or refreshed fact snapshot exists
- the target project already has `.github/copilot-instructions.md`

**Expected behavior**
1. treat the refreshed facts as the highest-priority input
2. update `## Project Truth` and any dependent governance or implementation rules that changed semantically
3. preserve only safe agent-managed content
4. run the post-write semantic consistency check against current manifests and facts

**Anti-pattern**
- skip the semantic consistency check because the refresh already completed
- reuse old structure claims that no longer match the repository

## Scenario 3: Human intent conflicts with facts or installed capabilities

**Starting point**
- the human asks for Poetry commands
- sensed facts show uv and no Poetry support

**Expected behavior**
1. stop before writing
2. explain the conflict clearly
3. ask the human which source should govern the next step
4. resume only after explicit direction

**Anti-pattern**
- treat the human request as an override and emit Poetry rules anyway
- partially mention both toolchains to avoid asking

## Scenario 4: Stale-facts hard block

**Starting point**
- the last sensing snapshot was taken on one Git `HEAD`
- current `HEAD` or `pyproject.toml` / `uv.lock` or `.github/skills/` summary has changed since then

**Expected behavior**
1. stop immediately
2. report which fingerprint changed
3. require re-sensing before generation or refresh continues

**Anti-pattern**
- continue because only one fingerprint moved
- attempt a best-effort refresh from stale facts

## Scenario 5: Materially different existing instructions

**Starting point**
- `.github/copilot-instructions.md` already exists
- content outside agent-managed block markers is non-empty, or core rules were manually changed

**Expected behavior**
1. classify the file as materially different
2. present exactly these choices:
   - full overwrite
   - keep current content
   - manual merge by the human
3. stop until the human chooses one path

**Anti-pattern**
- silently mix generated rules into the manual content
- delete non-managed content because the new draft seems better

## Scenario 6: Missing-facts hard block

**Starting point**
- installed skills were sensed, but toolchain or entrypoint facts are missing

**Expected behavior**
1. stop before generating any final instructions
2. name the missing fact category or categories
3. require a new sensing pass or fact collection step
4. do not emit a downgrade placeholder template

**Anti-pattern**
- generate a generic `.github/copilot-instructions.md` with vague guidance
- guess project structure from folder names alone

## Scenario 7: Over-specification anti-patterns (bloated output prevention)

**Starting point**
- all required facts exist and are fresh
- the project has 19 installed skills, a detailed dependency list in `pyproject.toml`, a `blueprint.md`, and a `CONTRIBUTING.md`
- human intent asks for complete coverage of "everything the project uses"

**Expected behavior**
1. apply the AI-control-plane test to every candidate rule: "will this rule influence a code-generation decision at the moment the agent writes code?"
2. exclude any content that already has a repo-visible authoritative source (`pyproject.toml`, `blueprint.md`, installed skill files)
3. exclude operational content that only humans need (CLI commands, git workflow steps, install instructions)
4. keep the generated file under 200 lines by retaining only actionable coding constraints
5. reference authoritative sources with a short pointer instead of duplicating their content

**Anti-pattern output (what to avoid)**

The following patterns each inflate the file without improving AI decision quality:

```md
# ❌ CLI commands — agents do not need run-time invocations to write code
## Commands
- uv sync
- uv run pytest tests/
- uv run pyright src/

# ❌ Full dependency list — already authoritative in pyproject.toml
## Dependencies
Runtime: httpx>=0.25.0, pydantic>=2.0
Dev: pytest, pytest-asyncio, ruff, pyright, pytest-cov, sasctl, pre-commit

# ❌ Skill enumeration — skills are already installed at .github/skills/
## Installed Skills (19)
python-async-await, python-api-signature, python-error-handling,
python-type-hints-strict, python-library-architecture, python-testing-pytest,
python-module-boundaries, sense-env-scaffold, copilot-instructions-init,
git-commit-convention, git-branch-naming, python-package-layout,
python-docstrings, python-class-design, python-data-model-methods,
python-model-selection, python-context-management,
git-post-merge-workflow, git-release-management

# ❌ Git workflow steps — belong in CONTRIBUTING.md, not AI control plane
## Git Workflow
1. Create branch: git checkout -b feat/<username>/<description>
2. Commit: follow Conventional Commits
3. Push and open PR

# ❌ Directory tree dump — already visible in the repo; not a coding rule
## Project Layout
mlops-async/
├── src/
│   └── mlops_async/
│       ├── __init__.py
│       ├── auth/
│       ├── models/
│       └── ...
```

**Corrected output (canonical sections, AI control plane only)**

```md
## Project Truth
- Package: `mlops_async` (`src/` layout; library mode)
- Toolchain: uv, Python 3.10
- Runtime deps: `httpx>=0.25.0`, `pydantic>=2.0`
- Entrypoints: none — library imported by downstream projects

## Governance
- Installed skills govern detailed rules; see `.github/skills/`
- Acceptance criteria: `blueprint.md`
- Dependencies: `pyproject.toml`

## Implementation Rules
- Async-first: use `httpx.AsyncClient` only; never `asyncio.to_thread`
- Strict typing: pyright --strict; no `Any`; no `cast` without inline comment
- No side effects at import time
- All I/O functions must be `async def`
- Use Pydantic v2 models for response parsing
- Translate HTTP errors at the client boundary; never propagate raw `httpx` exceptions
- Internal symbols use `_` prefix; public API exported from `__init__.py`
- Unit tests: mock at `httpx.AsyncClient` level; no external I/O
- Coverage target: ≥ 90%
- Ruff enforced; no `# noqa` without an inline reason
```

**Signal-to-noise check**
- target file length: ≤ 200 lines
- each rule must pass: "would an agent make a different code decision if this rule were absent?"
- if the answer is no, remove the rule and point to the authoritative source instead
