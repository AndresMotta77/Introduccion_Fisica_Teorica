# Logbook — Introduction to Theoretical Physics

A logbook for the Introduction to Theoretical Physics course. Its purpose is to
record the process of solving problems, and in particular the process of working
with AI tools.

The logbook is not a record of final answers. What it tries to capture is:

- The hypotheses used to solve each problem.
- My own reasoning, before consulting any AI.
- The prompts used, and which model and effort level produced each response.
- The hypotheses the AI proposed.
- The errors found.
- How those errors were identified.
- The changes made to the hypotheses.
- How the solution evolved.
- Personal reflections on the process.

The working method in `templates/` grew out of the first problem in this
repository, where two things happened that are worth naming. The model did not
derive the result; it found the solution on the web and transcribed it. And when
it was told, without any argument, that a correct option was wrong, it agreed.
The same behaviour produced a useful correction once and a wrong answer once,
which is why both are now measured rather than judged case by case.

## Method

```
human attempt, committed first          templates/human-attempt.md
  ↓
prompt0                                 templates/prompt0.md
  ↓
[optional] blind solve by the auditor   templates/blind-solve-prompt.md
  ↓
solver → answer-k                       declaration, tagged steps, code, sources
  ↓
auditor + audit prompt → report k       templates/audit-prompt.md
  ↓                          ↘
corrector-prompt-k ← Part B   Part A, pasted back so it enters the record
  ↓
solver → answer-(k+1), with rebuttals
  ↓
stop at no BLOCKER and no MAJOR; escalate at round 4
  ↓
compliance probe                        templates/compliance-probe.md
  ↓
/log P###                               skills/log/SKILL.md
  ↓
exploration → next problems queued      templates/exploration-prompt.md
```

| Path | What it is |
|---|---|
| `templates/CONVENTIONS.md` | Provenance tags, citation locator format, severity levels, verdicts, loop control. Given to every model in the loop. |
| `templates/human-attempt.md` | The timed attempt, written and committed before any model sees the problem. |
| `templates/prompt0.md` | The initial prompt. Sections 0–5 per problem, 6–8 invariant. |
| `templates/audit-prompt.md` | Nine audit passes. Output splits into a report for me and a corrector prompt for the solver. |
| `templates/blind-solve-prompt.md` | Optional: the auditor solves the problem cold before seeing the answer. |
| `templates/compliance-probe.md` | One bare assertion against a claim known to be right, to measure how readily the model folds. |
| `templates/exploration-prompt.md` | Turns a closed problem into a queue of structured next problems. |
| `skills/log/SKILL.md` | The `/log` skill: collects, gates, builds `final.md/.tex/.pdf`, commits. |
| `index.md`, `index.yaml` | The problem register, and eventually the dataset. |
| `CHANGELOG.md` | Template versions and what changed between them. |

## What the method is for

Four things carry most of the weight.

1. **The human attempt comes first.** It is the only prior in the process that
   was not produced by a language model, and it cannot be reconstructed after
   reading the model's answer.
2. **An executable check, treated as evidence rather than proof.** sympy or
   numerics, recomputing from the problem statement rather than from the
   derivation's own intermediate results, written so it can fail, and carrying a
   note on what it would not have caught. The model wrote the code, so the code
   is audited too.
3. **Citation verification status.** Every locator carries `{ver: tool | human |
   no}`. An `[S]` that cannot be confirmed becomes an honest `[R]`. A general
   reference is not a citation: the chapter, section and equation actually used
   are recorded.
4. **The compliance probe and a mechanical stopping rule.** No BLOCKER and no
   MAJOR in one full round, escalate at round 4, and one probe at the end to see
   whether the agreement along the way meant anything.

## Problems

| ID | Title | Verdict | Rounds | Probe |
|----|-------|---------|--------|-------|
| [P001](problems/P001-rolling-discs/) | Two discs rolling without slipping | A only (professor) | 2 | caved |

## Starting a problem

1. Create `problems/P###-slug/` following `skills/log/reference/layout.md`.
2. Write `human/attempt.md` and commit it on its own.
3. Fill `prompts/prompt0.md` sections 0–5; paste 6–8 verbatim.
4. Run the loop.
5. Run the compliance probe.
6. `/log P###`.
