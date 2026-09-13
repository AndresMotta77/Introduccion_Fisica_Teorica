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
your own attempt (optional)             templates/human-attempt.md
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
| `templates/human-attempt.md` | Your own attempt, in whatever form it exists. Optional. |
| `templates/prompt0.md` | The initial prompt. Sections 0–5 per problem, 6–8 invariant. |
| `templates/audit-prompt.md` | Nine audit passes. Output splits into a report for me and a corrector prompt for the solver. |
| `templates/blind-solve-prompt.md` | Optional: the auditor solves the problem cold before seeing the answer. |
| `templates/compliance-probe.md` | One bare assertion against a claim known to be right, to measure how readily the model folds. |
| `templates/exploration-prompt.md` | Turns a closed problem into a queue of structured next problems. |
| `skills/log/SKILL.md` | The `/log` skill: collects, gates, builds `final.md/.tex/.pdf`, commits. |
| `scripts/New-Problem.ps1` | Creates the folder structure for a new problem. |
| `index.md`, `index.yaml` | The problem register, and eventually the dataset. |
| `CHANGELOG.md` | Template versions and what changed between them. |

## What the method is for

Four things carry most of the weight.

1. **Your own attempt, when you make one.** The only prior in the process that
   was not produced by a language model, and not reconstructable after reading
   the model's answer. Any format, no requirement — but record honestly whether
   it predates the answer.
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

```powershell
.\scripts\New-Problem.ps1 -Id 2 -Slug pendulum-with-moving-pivot
```

That creates `problems/P002-pendulum-with-moving-pivot/` with every directory
the layout expects, plus three seeded files: `meta.yaml` with the template
versions read from the templates themselves, a `README.md` skeleton for the
logbook entry, and `human/attempt.md`. Add `-WhatIf` to see what it would do
without doing it, `-Bare` for directories only.

It does not create `prompts/prompt0.md`, on purpose. Then:

1. Your own attempt, if you make one. Fill in `human/attempt.md`, or delete it
   and drop a scan or a photo of your handwritten pages into `human/` instead.
   Optional, and nothing fails without it. Worth doing anyway: it is the only
   prior in the process that did not come from a language model, and you cannot
   reconstruct it after reading the model's answer.
2. Fill `prompts/prompt0.md` from `templates/prompt0.md`: sections 0–5 per
   problem, 6–8 verbatim.
3. Run the loop until a round yields no BLOCKER and no MAJOR. Escalate at 4.
4. Run the compliance probe.
5. `/log P###`.
