# Semantic-First Design — Review Routing Log

## Current state

- Planning artifacts initialized by Plan-Creator.
- No Plan-Reviewer or implementation Reviewer verdict has been issued.
- Current workflow status: `planned`.

## Routing rule

- Plan-Reviewer records the independent planning-artifact verdict below. An
  `approved` result permits routing to Implementer; `needs-rework` returns only
  to Plan-Creator.
- Reviewer records the independent implementation verdict only after the
  Implementer reports `review-ready`. An `approved` result routes to Main Agent
  for Phase 4.5; `needs-rework` returns only to Implementer unless planning
  contract drift requires planner re-entry.
- Each verdict entry must be exactly one JSON object using the shared reviewer
  handoff contract. Do not add prose after a verdict object.

## Plan-Reviewer verdict

{
  "verdict": "approved",
  "blocking_issues": [],
  "copilot_feedback_triage": {
    "ADDRESS": [],
    "DISCUSS": [],
    "SKIP": []
  }
}

## Implementation Reviewer verdict

{
  "verdict": "approved",
  "blocking_issues": [],
  "copilot_feedback_triage": {
    "ADDRESS": [],
    "DISCUSS": [],
    "SKIP": []
  }
}
