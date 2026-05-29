---
name: python-pre-commit
description: Define a canonical pre-commit policy and reusable config skeleton for uv-based Python projects, including hook selection, stage choices, and merge guidance for existing configs.
complexity: medium
risk_profile:
  - ambiguity_sensitive
inputs:
  - target project context
  - whether the project uses uv
  - whether an existing `.pre-commit-config.yaml` already exists
  - whether strict type-checking hooks should be included
  - preferred ruff rev tag when version pinning matters
outputs:
  - a canonical pre-commit hook policy for the project
  - a reusable `.pre-commit-config.yaml` skeleton or merge recommendation
  - explicit install/run follow-up commands when the user wants to apply the config
use_when:
  - a uv-based Python project needs pre-commit setup or cleanup
  - an existing `.pre-commit-config.yaml` needs canonical hook guidance and merge rules
  - the task is to choose hook composition and stage policy, not just to run a script
do_not_use_when:
  - the project does not use uv
  - the task is CI/CD pipeline configuration
  - the request is about secrets scanning policy only
  - the request is specifically to manage `.git/hooks/` directly
---

# Purpose
Provide policy-level guidance and a reusable config skeleton for uv-based Python pre-commit setups without making script execution or install flow the core contract.

# Trigger / When to use
Use this skill when:
- a uv-based Python project needs pre-commit setup or cleanup
- an existing `.pre-commit-config.yaml` needs canonical hook guidance and merge rules
- the task is to choose hook composition and stage policy, not just to run a script

Do not use this skill when:
- the project does not use uv
- the task is CI/CD pipeline configuration
- the request is about secrets scanning policy only
- the request is specifically to manage `.git/hooks/` directly

# Inputs
- target project context
- whether the project uses uv
- whether an existing `.pre-commit-config.yaml` already exists
- whether strict type-checking hooks should be included
- preferred ruff rev tag when version pinning matters

# Process
1. Confirm the project is uv-based. If not, stop and ask for the correct project convention instead of forcing uv-specific guidance.
2. Use the canonical baseline hook set: formatting/lint hooks plus lightweight repo hygiene hooks. Keep slow hooks such as test or type-check runs on `manual` unless the repository explicitly wants stronger enforcement.
3. If a config already exists, preserve intentional local hooks and merge toward the canonical baseline rather than overwriting blindly.
4. Make version-pinning strategy explicit, especially for the ruff pre-commit rev.
5. When asked to produce config, provide a reusable skeleton and the exact follow-up commands needed to install or run it, while keeping those commands outside the core policy contract.

# Recommended Hook Policy
- formatting and lint hooks run on normal commit
- slow hooks such as `pytest` and `pyright` default to `manual`
- existing intentional local hooks are preserved unless they conflict directly

# Validation
Before proceeding, confirm:
- the project is uv-based
- the hook set distinguishes fast commit hooks from slow manual hooks
- merge guidance preserves deliberate existing hooks
- version pinning is explicit when a concrete rev is proposed

# Boundaries
- Do not make script execution, template substitution, or install flow the main contract.
- Do not silently overwrite an existing config.
- Do not treat CI policy or secrets scanning as this skill's primary scope.

