# Template reference

A stable skill in this repository usually has:
- one trigger family
- one responsibility
- one primary output pattern
- concise positive and negative examples in `SKILL.md`
- local example or reference material
- no hidden dependency on other skill folders
- clear roles for any optional files or folders

## Example depth rule

- simple skills may rely on concise `SKILL.md` examples when they already cover
  most routine usage
- higher-complexity skills should include `examples.md`
- reviewer may still require `examples.md` when the brief examples are not enough

## Split signals

Create a second skill when:
- the trigger list keeps growing
- the outputs differ substantially
- the process branches into unrelated jobs
- the skill starts relying on too many repo-global assumptions

## Promotion rule

Do not treat a new skill as stable until `agent-skill-reviewer` returns
`approved`.

## Ownership rule

- creator may draft or revise until the skill is `review-ready`
- reviewer may return `approved` or `needs-rework`
- creator may not self-approve
- reviewer may not author the final implementation directly
