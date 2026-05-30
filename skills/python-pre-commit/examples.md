# Examples

- Positive: Recommend ruff and repo-hygiene hooks on normal commit, keep `pytest` and `pyright` on `manual`, and preserve deliberate existing local hooks during merge.
- Positive: Provide a reusable `.pre-commit-config.yaml` skeleton plus follow-up install/run commands when the user wants to apply the policy.
- Negative: Make a wrapper script or install flow the core contract, silently overwrite an existing config, or widen the skill into CI policy design.
