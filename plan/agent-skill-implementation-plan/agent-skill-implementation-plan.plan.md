# Windows-to-WSL Development Command Skill Plan

## Analysis Inputs

This plan is authored without the optional analysis layer:

- Missing: `analysis/agent-skill-implementation-plan/requirements.md`
- Missing: `analysis/agent-skill-implementation-plan/technical-spec.md`

This is a semantic soft warning, not an execution blocker. The human-provided
draft plan is the planning input for this topic. No chat-time instruction may
broaden the locked decisions below without a new approved plan revision.

## Goal / Outcome

- Create a company-notebook, user-scoped `windows-wsl-dev` Skill that keeps
  Codex and Codex Remote in the native Windows App session while running
  approved cross-platform development commands in WSL.
- The independent Implementer creates only these external, user-profile files:
  `%USERPROFILE%\.agents\skills\windows-wsl-dev\SKILL.md`,
  `%USERPROFILE%\.agents\skills\windows-wsl-dev\scripts\wsl-run.ps1`, and
  an append-only managed section in the effective user Codex instruction file.
- The result preserves command output and Linux exit codes, uses a Linux
  `.venv/bin/python` when one already exists, and produces actionable WSL
  diagnostics without weakening company security controls.

## Scope

- **In scope**:
  - inspect the active Windows user context, effective Codex home, instruction
    precedence, WSL availability, default distribution, and target project
    directory before any external write;
  - create the user-only `windows-wsl-dev` Skill and its PowerShell wrapper;
  - append concise host-specific routing guidance to the effective user Codex
    instruction file without overwriting existing content;
  - validate WSL directory mapping, output, exit-code propagation, bounded
    quoting cases, Python virtual-environment selection, and native-command
    non-routing without changing a shared repository or installing dependencies.

- **Out of scope**:
  - any write under this repository, including `skills/**`, `.github/**`,
    `.codex/**`, `README.md`, `VERSION`, project-level `AGENTS.md`, or platform
    projections, except for the topic-local planning artifacts listed below;
  - macOS changes, synchronizing host rules to another machine, or a second
    Codex session inside WSL;
  - WDAC, Device Guard, AppLocker, registry, execution-policy, WSL-installation,
    security-policy, dependency-installation, or global-Python changes;
  - automatic migration of Git or Windows-native development commands to WSL;
  - deletion, renaming, or recreation of an existing project `.venv`.

## Locked Decisions

1. **Host and storage boundary**
   - Codex remains in the native Windows App; only selected development
     toolchain commands cross the WSL boundary.
   - The only implementation targets are user-profile paths on the company
     Windows notebook. They are external runtime targets, not repository
     artifacts and must never be committed.
   - The Skill location is fixed at
     `%USERPROFILE%\.agents\skills\windows-wsl-dev\`; do not relocate it into
     this repository, `%CODEX_HOME%\skills`, or a macOS profile.
   - `SKILL.md` starts with this exact front matter:

     ```yaml
     ---
     name: windows-wsl-dev
     description: >
       Use on a native Windows Codex host when cross-platform project development
       commands must execute through WSL. This includes Python, uv, pip, pytest,
       Pyright, Ruff, and similar Linux-oriented project toolchains, especially
       when Device Guard or WDAC blocks project-local Windows executables. Do not
       use on macOS or Linux, and do not use for genuinely Windows-native builds.
     ---
     ```

2. **Instruction-file decision**
   - Resolve Codex home as `$env:CODEX_HOME` when non-empty, otherwise
     `$env:USERPROFILE\.codex`.
   - Re-check `AGENTS.override.md` immediately before writing. In the observed
     session `CODEX_HOME` is unset, `%USERPROFILE%\.codex\AGENTS.md` exists,
     and `AGENTS.override.md` does not exist, so the intended target is that
     existing `AGENTS.md`.
   - If an override exists at implementation time, stop for a human decision;
     do not silently change either instruction file. If no override exists,
     append one idempotent `## Managed Windows development environment` section
     to `AGENTS.md`, preserving all pre-existing bytes and instructions.
   - The appended section is exactly:

     ```markdown
     ## Managed Windows development environment

     When Codex is running natively on this Windows notebook:

     - Use the `windows-wsl-dev` Skill for cross-platform development commands.
     - Run Python project commands, including uv, pytest, Pyright, and Ruff,
       through WSL.
     - Never execute project-local `.venv\Scripts\*.exe` files.
     - Keep Codex itself in the native Windows session so the existing App and
       Remote session remain intact.
     - Run genuinely Windows-specific commands natively.
     - Do not apply these host-specific rules on macOS or Linux.
     ```

3. **Routing policy**
   - On a native Windows host with `wsl.exe`, route Python project command
     families through the wrapper: `python`, `python3`, `uv`, `pip`, `pip3`,
     `pytest`, `pyright`, `ruff`, `mypy`, `pre-commit`, `tox`, and `nox`,
     including `uv run ...` forms.
   - Node, Go, Rust, Make, and CMake families may use WSL only when the target
     repository clearly uses their Linux environment; the Skill must not route
     them automatically by default.
   - Keep PowerShell-specific commands, registry work, WinUI/WPF/COM/services,
     MSI/MSIX, code signing, MSBuild/MSVC/Windows SDK work, security
     administration, file inspection/editing, and Git in their established
     native environment unless a repository explicitly requires WSL Git.
   - On macOS or Linux, the Skill does not apply and leaves commands in their
     established native environment. On native Windows, a routed
     cross-platform development command requires a usable WSL path: if
     `wsl.exe` is missing or blocked, no usable distribution exists, or Bash
     cannot start, classify the requested routed command as `blocked`. Never
     fall back to a Windows project executable, global Python, or another
     native implementation of that routed command.

4. **Wrapper contract**
   - `wsl-run.ps1` exposes `-Command <string>`, optional `-Distro <string>`,
     and optional `-WorkingDirectory <string>`.
   - Distribution resolution is fixed: explicit `-Distro`, then
     `CODEX_WSL_DISTRO`, then WSL's default distribution. The wrapper does not
     assume `Ubuntu` and does not persist a distribution choice.
   - Working-directory resolution is fixed: explicit `-WorkingDirectory`, then
     the current PowerShell directory. Convert the resolved Windows directory
     with the selected distribution's `wslpath -a`; never hand-convert drive
     letters or path separators. Pass the result to `wsl.exe --cd`.
   - Build the `wsl.exe` invocation as a PowerShell argument array and invoke it
     with `&`; do not use `Invoke-Expression`, a synthesized PowerShell command
     line, execution-policy changes, or an unsafe interpolation of the requested
     shell string.
   - Encode the UTF-8 `-Command` payload as Base64, pass only the encoded value
     as a WSL argument, and decode it inside `bash -lc` before execution by a
     login shell. This centralizes the Windows-to-Bash quoting boundary while
     retaining shell constructs such as `&&` in the requested command.
   - The wrapper forwards stdout and stderr unchanged, captures the invoked WSL
     process result, and exits with its exact numeric exit code. It must not
     claim arbitrary shell-string safety beyond the tested character cases.
   - The wrapper owns only deterministic preflight classifications: unsupported
     host, missing or blocked `wsl.exe`, absent or invalid selected/default
     distribution, unavailable Bash, and Windows-directory or WSL-directory
     mapping failure. After that preflight succeeds, a nonzero payload exit is
     `command itself failed` by default; the wrapper must not infer that a
     tool, dependency, or virtual environment was missing.

5. **Virtual-environment and safety policy**
   - Never run project-local `.venv\Scripts\python.exe`, `pip.exe`,
     `pyright.exe`, or `pytest.exe`, and never use Windows global Python for
     project dependency management.
   - The Skill, not the wrapper, performs the following explicit, non-mutating
     Python/uv preflight only when the agent has deliberately selected a direct
     `uv sync` or `uv run --no-sync ...` command. Before that selected command,
     inspect the project `.venv`: capture whether the Windows marker
     `.venv\\Scripts\\python.exe` exists and, through the selected WSL
     distribution, whether `.venv/bin/python` is executable. Do not attempt to
     parse an arbitrary shell payload or classify its internals.
   - For that known preflight, a Windows marker is evidence for `existing .venv
     is a Windows environment`; an executable Linux marker is evidence for a
     usable Linux environment; neither marker is evidence for `Linux virtual
     environment has not been created`. The Skill returns `blocked` with this
     evidence before executing the selected Python/uv command. The wrapper
     never runs `uv sync` on its own. A Windows-format environment is neither
     used, removed, nor renamed.
   - Recreating or renaming a Windows `.venv`, creating a Linux environment, or
     installing dependencies needs separate explicit human authorization.
   - Validation that calls `uv` may run only against an already-existing Linux
     environment and must use `--no-sync` to avoid dependency mutation.

6. **Non-stable intent**
   - This is a user-environment workaround, not a stable-library topic.
     `README.md` and `VERSION` do not change, no release/tags exist, and no
     shared skill enters `skills/`.

## Boundaries / Exclusions

- **ReadOnly**: all existing repository files; existing user Codex instructions
  and any existing project `.venv` until the Implementer has inspected them;
  Device Guard, WDAC, AppLocker, WSL configuration, global Python, and macOS.
- **Written**: only the two new user-profile Skill files and the one append-only
  user Codex instruction section described in this plan; only topic-local
  planning artifacts may be written in this repository.
- **Deleted**: none.
- **Modify**: no shared-repository implementation file. The external instruction
  file may receive only the managed section after the override check passes.
- The Implementer owns external writes and validation; the Reviewer independently
  assesses them. The Main Agent owns routing and human gates. No role may treat
  a sandbox-only WSL failure as proof of the user's actual-account condition.
- If any required external path, instruction precedence, WSL distribution, or
  project virtual-environment state differs from this contract, stop and return
  `blocked` or `human-check`; do not broaden scope or bypass policy.

## Status / Allowed Transitions

- **Current**: `review-ready`. This uncommitted plan amendment and its required
  progression artifact are ready for independent Plan-Reviewer re-review, but
  must not be represented as `planned`; in the canonical status model,
  `planned` means the topic plan and progression artifact are committed and
  ready for execution.
- **Execution model**: Plan-Reviewer re-review first. Its plan-review verdict
  is a gate on this candidate plan, not a claim that the topic status has
  reached `approved`. If the plan passes re-review, a human must separately
  and explicitly authorize a **plan-amendment-only repository commit** for the
  revised plan and the topic progression artifact before this plan may be
  marked `planned`. That approval does not authorize an external user-profile
  write. After that commit, the Main Agent verifies the progression artifact
  and creates the approved `feature/andrew/windows-wsl-dev` worktree from that
  commit. Once the artifact records a validated worktree, a second explicit
  human authorization is required before the independent Implementer may
  create or modify the external user-profile Skill or user-level instruction
  file. Independent Reviewer review follows only after that external
  implementation is `review-ready`.
- **Allowed transitions**:
  - `planned` -> `creator-in-progress`
  - `creator-in-progress` -> `review-ready`
  - `review-ready` -> `reviewer-in-progress`
  - `reviewer-in-progress` -> `approved`
  - `reviewer-in-progress` -> `needs-rework`
  - `needs-rework` -> `creator-in-progress`
  - `approved` -> `creator-in-progress`
  - `approved` -> `publish-in-progress` only after the human explicitly
    authorizes the canonical repository publication phase for reviewed
    implementation work. In that canonical phase, the Main Agent commits,
    pushes, and prepares a PR; it is not a planning-only label and it never
    itself authorizes external implementation.

Routing notes:

- The immediate gate is an independent Plan-Reviewer verdict using the JSON
  contract below. A `needs-rework` verdict routes only to Plan-Creator for a
  bounded plan repair; it does not authorize external implementation.
- After Plan-Reviewer approval, stop for the human plan-amendment-only commit
  authorization. That limited commit includes only the revised topic plan and
  its topic-local progression artifact; it does not enter
  `publish-in-progress`, push, or open a PR by inference. Once that commit
  makes the plan `planned`, the Main Agent must validate the progression
  artifact, create the approved feature worktree from that commit, and record
  the verified branch, worktree path, and base commit in the progression
  artifact. Stop again for the independent external-write authorization before
  dispatching the Implementer.
- The standard Phase 4.5 plan-alignment checkpoint applies after the external
  implementation review. Any scope, contract, or workflow drift routes back to
  the appropriate independent role; it never authorizes policy bypass.

## Artifact Paths

| Artifact | Path | Owner | Role |
| --- | --- | --- | --- |
| Topic plan | `plan/agent-skill-implementation-plan/agent-skill-implementation-plan.plan.md` | Plan-Creator | Repo-visible execution contract for this user-scoped topic |
| Topic progression artifact | `plan/agent-skill-implementation-plan/agent-skill-implementation-plan.step.md` | Plan-Creator (initial contract); Main Agent (truthful gate-state updates only) | Required current-truth progression state before the second and later role handoffs |
| Review routing log | `plan/agent-skill-implementation-plan/agent-skill-implementation-plan.review-log.md` | Plan-Reviewer / Reviewer | Required repo-visible routing record when review findings control rework or re-review |
| Topic close summary | `plan/agent-skill-implementation-plan/agent-skill-implementation-plan.summary.md` | Main Agent | Required current-truth close and handoff artifact; before close or handoff it must contain `current state`, `completed`, `not completed`, `required follow-up`, and `next handoff` with both `next actor` and `next step` |

Artifact path notes:

- The external implementation targets are fixed in `Locked Decisions` and are
  intentionally not repo-visible or staged artifacts.
- The Plan-Creator creates this topic-local progression artifact together with
  this plan amendment. It is not a reusable Skill, is not created through a
  `step-creator` profile, and must not write or claim any `skills/**` source or
  platform projection.
- The progression artifact has exactly these required sections: `Workflow
  Stages`, `Actionable Steps`, and `Handoff / Gate Notes`. `Workflow Stages`
  records each stage's state, entry evidence, required next gate, and next
  owner. `Actionable Steps` records the one next bounded action for each
  non-terminal stage. `Handoff / Gate Notes` records the plan amendment commit
  boundary, feature-worktree boundary, external-write authorization boundary,
  and the rule that no status update may change a locked decision.
- Plan-Creator owns initial creation and any plan-alignment amendment of the
  artifact. The Main Agent may update only current stage, verified evidence,
  and next handoff after a completed gate; it must not alter its workflow
  contract, the plan, or implementation scope. A later contradiction routes
  back to Plan-Creator.
- Creation timing is fixed: the artifact is created before this re-review and
  reviewed and committed with this plan amendment. The feature worktree may be
  created only after that commit. The Main Agent changes the feature-worktree
  stage to `feature-worktree-ready` only after it verifies the branch
  `feature/andrew/windows-wsl-dev`, its worktree path, and its base commit.
  The Implementer may be dispatched only after that state and a separate,
  explicit human authorization for external user-profile writes.
- This topic does not modify `README.md`, `VERSION`, `.github/**`, `.codex/**`,
  `skills/**`, or any project repository. Any proposed repository write beyond
  the listed planning artifacts is plan drift and must stop.

## Implementation Steps

1. The independent Implementer re-runs the Phase 1 user-context inspection:
   `$env:USERPROFILE`, `$env:CODEX_HOME`, `$env:OS`, `Get-Command wsl.exe`,
   `wsl.exe --status`, `wsl.exe --list --verbose`, the effective `AGENTS.md`,
   possible `AGENTS.override.md`, and `%USERPROFILE%\.agents\skills`.
   Record only necessary facts; do not print secrets or a full environment.
2. Stop and classify the preflight as `human-check` if an override instruction
   file exists, or `blocked` if WSL is missing, policy-blocked, lacks a usable
   distribution, its default cannot be determined, or Bash is unavailable.
   For any routed cross-platform Python/development command on native Windows,
   this is terminal for that command: do not fall back to Windows Python,
   `.venv\\Scripts\\*.exe`, or native equivalents. The earlier sandbox
   observation of `Wsl/EnumerateDistros/Service/E_ACCESSDENIED` is diagnostic
   context only and must be rechecked in the user's actual Windows account.
3. Create `%USERPROFILE%\.agents\skills\windows-wsl-dev\SKILL.md` with the
   exact requested YAML front matter, Windows-host and `wsl.exe` detection,
   the locked command-routing policy, native-command exclusions, Git caution,
   virtual-environment policy, expected wrapper invocation, and explicit
   no-op behavior outside native Windows.
4. Create `%USERPROFILE%\.agents\skills\windows-wsl-dev\scripts\wsl-run.ps1`
   with the locked parameters and resolution order. Validate only host,
   `wsl.exe`, selected/default distribution, Bash, Windows working directory,
   and its WSL mapping before dispatch. For every wrapper preflight failure
   report: Windows working directory, selected distribution when known,
   requested command, exit code when available, a non-secret suggested
   diagnostic command, and one precise deterministic classification:
   unsupported host, missing/blocked WSL, no/configured-missing distribution,
   unavailable Bash, or unmappable directory. After successful preflight, pass
   the payload unchanged and classify a nonzero payload exit only as `command
   itself failed`.
5. If no override exists, append the locked managed Windows-development section
   exactly once to the effective `AGENTS.md`. It must direct Codex to use this
   Skill for cross-platform tooling, prohibit project-local Windows `.venv`
   executables, keep Codex/Remote native, retain Windows-native commands, and
   limit the rule to this Windows host.
6. Validate non-destructively from an existing project path, including a path
   containing spaces: WSL availability; `pwd` mapping; visible stdout/stderr;
   a `17` exit result reflected by `$LASTEXITCODE`; and requested-command
   quoting containing spaces, single/double quotes, parentheses, equals signs,
   and file paths. Report any unsupported quoting case rather than masking it.
7. Before selecting either `uv sync` or `uv run --no-sync ...`, apply the
   locked Skill preflight and record the Windows and Linux `.venv` marker
   evidence described in `Locked Decisions`. If the Windows marker exists or
   neither marker proves a usable Linux environment, report the Skill-level
   `blocked` classification and do not execute the selected command. When the
   inspected project already has an executable Linux `.venv/bin/python` and no
   dependency change is required, validate
   `uv run --no-sync python -c "import sys; print(sys.executable)"` and
   `uv run --no-sync pyright` through the wrapper. Confirm the executable is a
   Linux path resolving through `.venv/bin/python` and the wrapper did not
   invoke a Windows `.venv\Scripts\*.exe`. Otherwise report the environment as
   not yet created and stop without `uv sync`.
8. Confirm one clearly Windows-native probe remains native, inspect only the
   user-profile files changed by this topic, and report that no shared project
   path contains the company-specific rule. Hand the evidence to the independent
   Reviewer without self-approving the implementation.

## Validation / Acceptance Checks

- User-context inspection identifies the effective Codex home and instruction
  precedence before any write; existing instructions remain byte-preserved
  outside the new managed section.
- `windows-wsl-dev` exists only under the company notebook user profile with the
  requested SKILL front matter and wrapper parameter contract; no repository or
  macOS file is changed.
- The wrapper selects an explicit distro, `CODEX_WSL_DISTRO`, or the actual WSL
  default in that order, does not assume Ubuntu, maps paths using `wslpath`,
  starts the requested command from the mapped directory, and preserves stdout,
  stderr, and exit code `17`.
- Bounded quotation tests cover the requested character classes. The final
  evidence names any residual shell-language limitation; it does not make an
  untested universal-safety claim.
- Wrapper preflight failures are limited to deterministic host, WSL, distro,
  Bash, and directory-mapping categories. Payload failures are reported as
  `command itself failed`; only the explicitly selected Skill-level `uv sync`
  or `uv run --no-sync` preflight may report Windows `.venv` or missing Linux
  environment, and it must retain the marker evidence.
- No project-local Windows virtual-environment executable or global Python is
  used for project dependency management. A Windows `.venv` is only reported,
  never changed. Linux Python validation is performed only against a pre-existing
  environment with `uv --no-sync`.
- Native Windows commands and ordinary Codex file work remain native; Git stays
  in its established environment unless a project explicitly requires WSL Git.
- The implementation has no WDAC/security-policy bypass, execution-policy
  mutation, WSL installation, dependency installation, repository write,
  commit, push, PR, release, or macOS synchronization.

## Reviewer Handoff

```json
{
  "verdict": "approved|needs-rework",
  "blocking_issues": [],
  "copilot_feedback_triage": {
    "ADDRESS": [],
    "DISCUSS": [],
    "SKIP": []
  }
}
```

## Post-merge / release actions

- No repository merge, release, tag, README update, VERSION bump, commit, push,
  or PR action is currently authorized by this topic. A plan-only commit may
  occur only after Plan-Reviewer approval and explicit human authorization; it
  is a Phase 1 prerequisite and does **not** redefine or enter the canonical
  `publish-in-progress` status. This repository-publication authorization
  remains independent of the later external user-profile implementation
  authorization.
- The topic cannot close after independent review alone. Before close or a
  human/agent handoff, the Main Agent must create or validate the listed topic
  summary artifact with `current state`, `completed`, `not completed`,
  `required follow-up`, and `next handoff` (`next actor` and `next step`). A
  later reusable canonical Skill requires a separately authorized topic and
  the normal human gates.

## Open Questions / Unresolved Items

- The usable WSL distribution cannot be confirmed from this sandbox because
  `wsl.exe --list --verbose` returned
  `Wsl/EnumerateDistros/Service/E_ACCESSDENIED`. The independent Implementer
  must verify this under the user's actual Windows account before external
  writes or validation; no distribution is preselected by this plan.
