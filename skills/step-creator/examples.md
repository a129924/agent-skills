# Examples

## Valid Base generation

Caller input:

```text
topic=cache-policy
profile=base-plan
```

The source has canonical topic sections, exactly one `planned` status, valid
`creator-in-progress` transition, one Creator action, and a top-level ordered
Implementation Steps list. Destination is missing. Render the Base wire with
pending lifecycle actions; do not require an existing managed worktree merely
to create the tracker.

## Valid Agent Skill generation

Caller selects `agent-skill-plan`. The source declares one bounded
`skills/cache-policy-helper/` skill, Creator artifacts, an independent Reviewer,
and a `review-ready` handoff. Preserve the source Creator action in Contextual
Actions. Do not place reviewer approval or fixed lifecycle actions in
Implementation Steps.

## Valid Python generation without a literal profile marker

Caller explicitly selects `python-implementation-plan`. The source is a bounded
Python change with all 13 canonical sections, an explicit async exemption, five
test categories, Validation Commands, and top-level Implementation Steps. It
does not contain the text `python-implementation-plan`, a status, a next actor,
or a stage-local action. This is eligible: retain the exact Python frontmatter,
executor note, six workflow stages, fixed adapter-owned Creator contextual
action `**Actor:** Creator — **Action:** Complete source ## Implementation Steps in order.`, one-to-one Implementation mapping, and shared shell.

## Existing output blocks

If `plan/cache-policy/cache-policy.step.md` already exists, return:

```text
BLOCKED: output already exists at plan/cache-policy/cache-policy.step.md
```

Do not patch, normalize `[x]`, merge, overwrite, or create a second output.

## Invalid profile and extraction blockers

- Profile omitted or `auto`: `BLOCKED`; request one supported caller value.
- Base/Agent source with two current statuses, missing next actor, nested-only
  Implementation Steps, or a stage action that cannot be extracted exactly:
  `BLOCKED`.
- Agent source naming two skills or only `.github/skills/...` outputs:
  `BLOCKED`.
- Python source with non-Python intent or incomplete Decisions/Test/Validation
  contract: `BLOCKED`.

## Marker and worktree evidence

A source `[x]` becomes `[ ]` in generated output and produces a warning. A
commit message or planned worktree path is not completion proof. Initial
generation with no topic worktree keeps fixed head and cleanup slots pending;
an update claiming `[X] create-worktree` must show exact managed worktree plus
attached branch evidence. A primary worktree, conflict, or ambiguity blocks.

## Conditional tail examples

- When retention policy requires a remote branch, render only
  `remote-retained`; never additionally render remote delete.
- When neither the source plan nor retention policy states whether to retain the
  remote topic branch, return `BLOCKED`; do not render `remote-retained` as a
  safe-looking default. If the two authorities conflict, also return `BLOCKED`
  and report both exact evidence sources.
- When source truth declares terminal at merged, slot 13 is exactly `[X]
  Determine release requirement — release not required`; replace slots 14–21
  with the sole `release-not-applicable` sentinel. Do not also render a pending
  release-resolution checkbox.
- When release is required and no authoritative version source exists, slot 15
  is `tag-only`; when README is not needed, slot 16 is
  `README-not-required`. Multiple disagreeing version sources block.
- Missing release applicability, tag approval, destructive removal approval, or
  selected-worktree identity is not a harmless pending branch when rendering a
  claimed completion: block rather than invent evidence.

## Tracker split

For a Python output, all six Workflow Stages may include one pending stage while
every Implementation Step is `[X]`. `check_all_succeeded` is false;
`check_impl_steps_succeeded` is true. For Base/Agent, whole-file scope includes
rendered head, contextual, Implementation, and tail checkboxes.
