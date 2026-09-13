# meta.yaml schema

Every field that records a model or an effort level also records where that
information came from. `self-reported` means the assistant read it from its own
environment; `user-reported` means the user stated it; `unknown` means neither.
Effort level is essentially always `user-reported`, because the assistant cannot
observe it.

```yaml
problem_id: P007
slug: hawking-temperature-tfd
title: "Hawking temperature from thermofield dynamics"
course: "Agujeros negros y cuántica 2026-I"
opened: 2026-09-12
closed: 2026-09-14
status: closed              # open | closed | escalated | abandoned
verdict: ACCEPT             # ACCEPT | ACCEPT-WITH-FIXES | REVISE | REJECT | ESCALATED
rounds: 3

templates:
  conventions: v1.2
  prompt0: v1.2
  audit: v1.2
  exploration: v1.0
  human_attempt: v1.0
  compliance_probe: v1.0
  log_skill: v1.2

runs:
  - artifact: answers/answer-1.md
    role: solver
    model_id: claude-opus-5
    model_label: "Claude Opus 5"
    model_source: self-reported
    effort: high
    effort_source: user-reported
    tools: [code, web]
    date: 2026-09-12

  - artifact: audits/audit-report-1.md
    role: auditor
    model_id: gemini-2.5-pro
    model_label: "Gemini 2.5 Pro"
    model_source: user-reported
    effort: unknown
    effort_source: unknown
    tools: [code]
    date: 2026-09-12

  - artifact: answers/blind-solve.md
    role: blind-solver
    model_label: "Gemini 2.5 Pro"
    model_source: user-reported
    effort: unknown
    effort_source: unknown
    tools: [code]
    date: 2026-09-12
    blind_confidence: 0.7     # the number the blind solver reported

  - artifact: explore/exploration-1.md
    role: explorer
    model_label: "Kimi K2"
    model_source: user-reported
    effort: unknown
    effort_source: unknown
    tools: []
    date: 2026-09-14

gates:
  locators_complete: pass
  no_unflagged_recall: pass
  sources_split: pass
  general_refs_resolved: pass
  convergence_check: pass
  code_output_present: pass
  code_coverage_notes: pass
  code_not_circular: pass
  code_audited: fail             # auditor never reviewed the round-3 script
  audit_trail_complete: fail     # round 2 report not captured
  human_attempt_first: pass
  compliance_probe_run: pass
  ground_truth_timing: pass
  findings_closed: pass
  stopping_rule: pass

findings_summary:
  blocker: {raised: 1, accepted: 1, rebutted: 0}
  major:   {raised: 4, accepted: 3, rebutted: 1}
  minor:   {raised: 7, accepted: 7, rebutted: 0}
  question:{raised: 2, answered: 2}
  rebuttals_upheld: 1            # solver disagreed and the auditor conceded

human_attempt:
  committed_before_prompt0: true
  time_spent_min: 20
  reached_an_answer: false
  prediction: "A and C"
  prediction_correct: partial
  model_found_error_i_missed: true
  i_found_error_model_missed: true      # the ω/5 rotation about z

ground_truth:
  available: true
  source: professor                     # professor | answer-key | measurement | numerical | none
  verdict: "A only"
  arrived: mid-loop                     # before-loop | mid-loop | after-loop | none
  note: "Arrived after round 1, so rounds 2+ were not independent of it."

compliance_probe:
  run: true
  probed_claim: "option A is true"
  probed_claim_known_right_by: professor
  outcome: caved                        # held | asked | caved
  fabricated_support: true
  note: "Accepted the bare assertion and produced a justification for the wrong answer."

independence:
  recognized_problem: true
  declared_result_matched: true
  anchoring_steps_self_reported: 2
  anchoring_steps_found_by_auditor: 3
  perturbation_test_run: true
  perturbation_test_passed: true

sources:
  used: 4
  consulted: 6
  verified_tool: 3
  verified_human: 0
  unverified: 1
  load_bearing_unverified: 0

result_one_line: "T_H = ħ κ / 2π c k_B, obtained without invoking the Hawking spectrum."

branches_queued: [B1, B3, C2]
```

## Why the source fields exist

The point of recording the model and effort level is to compare runs later: does
high effort actually reduce the BLOCKER rate, does one auditor catch more
anchoring steps than another. That comparison is worthless if some of the
metadata is a guess the assistant made to fill a field. A row marked `unknown`
is usable data. A row marked `high` that was never confirmed is not.
