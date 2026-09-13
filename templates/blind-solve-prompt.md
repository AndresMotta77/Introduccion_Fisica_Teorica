# Blind-solve prompt — v1.0 (optional stage 0)

Use this when the problem matters enough to want a real independence test, or
when you suspect the answer is a well-known textbook result the solver may be
reciting.

The auditor currently sees the solver's answer before forming an opinion, which
means it is reviewing, not checking. This stage fixes that: the auditor solves
the problem cold, from prompt0 alone, before it is shown anything. The
comparison is then between two independent attempts rather than between an
answer and a reader of that answer.

Send to the auditor model in a fresh context, before the audit prompt.

---

You are given a physics problem. Solve it independently. You will later be shown
another model's solution, but not yet, and your answer here is recorded before
you see it.

Attached: `[PROMPT0]` and `CONVENTIONS.md`.

Follow prompt0 §6 in full: the prior-knowledge declaration first, tagged steps,
sources with locators and verification status, code verification, the self-check
battery, the convergence check, the risk register.

Two additions specific to this stage:

- Work from the problem statement in §1 and the conventions in §2. Sections 3b
  and 3c of prompt0 (the user's partial work and expected results) have been
  removed from your copy on purpose. If you find yourself needing them, say
  what you needed.
- Record your total confidence in the final result as a single number between
  0 and 1, before you see anything else.

Return the answer in prompt0 §7 format.

---

## How the comparison is read

When both solutions are in hand, the useful cases are:

| Blind auditor | Solver | Reading |
|---|---|---|
| Same result, different route | — | Strongest evidence available in this workflow. |
| Same result, same route, same citations | — | Weak. Both models may be reciting the same source. Run the perturbation test in audit pass 8 before believing it. |
| Different results | — | At least one is wrong. This is the case worth the whole exercise; do not average them. |
| Auditor could not solve it | Solver did | Either the solver is good or the solver is reciting. Perturbation test, mandatory. |

Log the blind solution as `answers/blind-solve.md` and its model and effort in
`meta.yaml` like any other run. It counts as a source of evidence, not as an
answer to the problem.
