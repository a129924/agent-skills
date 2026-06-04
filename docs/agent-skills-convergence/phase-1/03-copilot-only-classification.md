# Copilot-Only Classification

## copilot-instructions-init

### Classification

copilot_only: true

### Evidence
- The skill name and purpose are explicitly about initializing `.github/copilot-instructions.md`.
- Existing migration evidence treats it as a runtime/tooling blocker tied to `.github` inventory and Copilot instruction generation.

### Copilot-specific dependencies
- `.github/copilot-instructions.md`
- `.github/skills/` inventory assumptions
- GitHub/Copilot compatibility wording

### Recommendation
- split_generic_core_and_copilot_adapter

### Reason
The skill is materially coupled to GitHub/Copilot output shape and should not be treated as a generic portable skill without an adapter split.

## Notes

- No other skill met the Copilot-only threshold from evidence alone.
- Several skills are path-sensitive or runtime-coupled, but that alone did not justify a Copilot-only label.
