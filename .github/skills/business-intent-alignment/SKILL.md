---
name: business-intent-alignment
description: Align ambiguous business intent into a measurable requirements baseline at `analysis/<topic>/requirements.md` by using Socratic questioning, contradiction surfacing, and extreme-boundary checks before technical translation starts.
---

# Purpose
Turn ambiguous business intent into a measurable, contradiction-aware baseline that can be frozen in `analysis/<topic>/requirements.md`.

# Trigger / When to use
Use this skill when:
- business goals are stated as outcomes, preferences, or urgency without measurable requirements
- stakeholders disagree, omit constraints, or mix goals with assumed solutions
- the next workflow step needs a frozen baseline before technical planning or task decomposition
- the request sounds certain but still hides untested assumptions about users, scale, timing, roles, or failure handling

Do not use this skill when:
- `analysis/<topic>/requirements.md` is already frozen and the next task is technical translation; use `business-to-technical-translation`
- the task is implementation planning, architecture design, or coding
- the user wants uncommitted brainstorming without converting it into a requirements baseline

# Inputs
- topic name and intended `analysis/<topic>/requirements.md` path
- stated business outcomes, success claims, deadlines, and stakeholder expectations
- target users, actors, permissions, and environments
- known constraints, dependencies, compliance rules, and failure consequences
- any existing notes, tickets, meeting summaries, or prior contradictions

# Process
1. Confirm the task is business-intent alignment rather than technical solutioning or implementation planning.
2. Adopt a Socratic interviewer posture. Convert every claim into something testable: who needs what outcome, by when, under which conditions, and how success will be observed.
3. Challenge assumptions directly. Ask hard follow-up questions about actor boundaries, hidden dependencies, incentives, manual work, exception handling, and business loss if the outcome fails.
4. Run extreme-boundary checks before freezing anything:
   - no network or degraded external dependency
   - wrong user role or missing approval
   - interrupted process or partial completion
   - lowest-volume and peak-volume conditions
   - time-window, audit, or regulatory edge cases
5. Surface contradictions explicitly. If one statement conflicts with another, record the conflict, force a decision, and do not smooth it over with vague wording.
6. Force measurability. Rewrite vague words such as `fast`, `simple`, `accurate`, or `better` into observable thresholds, decision rules, and acceptance signals.
7. Freeze the resolved baseline into `analysis/<topic>/requirements.md` with measurable requirements, explicit assumptions, non-goals, surfaced contradictions, and any remaining blockers that must be resolved before technical translation.

# Examples
- Positive: Turn `make partner onboarding faster` into a baseline that defines actor roles, approval deadlines, measurable completion targets, interruption handling, and explicit contradictions about compliance review timing.
- Negative: Accept `users want a simple dashboard` as sufficient, skip edge-case questioning, and move straight to technical design without measurable thresholds or contradiction tracking.

# Outputs
- `analysis/<topic>/requirements.md` as the business baseline for downstream work
- measurable requirements with named actors, conditions, thresholds, and acceptance signals
- explicit assumptions, non-goals, surfaced contradictions, and blocker notes
- a clear handoff boundary for technical translation

# Verification
- confirm every requirement is observable or measurable
- confirm contradictions are surfaced instead of hidden in soft wording
- confirm extreme-boundary checks were applied before freezing the baseline
- confirm the output names what is in scope, out of scope, and still unresolved

# Red Flags
- the draft repeats stakeholder adjectives without converting them into measurable behavior
- one stakeholder promise silently cancels another requirement
- technical implementation ideas appear before the baseline is frozen
- edge conditions are dismissed as `later` even though they change the requirement meaning

# Common Rationalizations
- `Everyone already knows what fast means.`
- `Engineering can figure out the contradictions later.`
- `Offline or wrong-role cases are edge cases, not requirement work.`
- `If we write enough tickets, the missing business logic will emerge.`

# Boundaries
- Do not design system architecture, estimate implementation, or break work into engineering tasks.
- Do not freeze a baseline by hiding contradictions behind compromise wording.
- Do not treat stakeholder preference statements as measurable requirements without challenge.
- Do not replace named actors, thresholds, and failure conditions with generic aspirational language.

# Local references
- `reference.md`: stable rules for measurability, contradiction surfacing, extreme-boundary checks, and freeze criteria
- `examples.md`: detailed Socratic interviewer scenarios, including positive and negative requirement-alignment patterns
- `checklist.md`: repeatable medium-risk misuse-prevention checks before declaring the baseline review-ready
