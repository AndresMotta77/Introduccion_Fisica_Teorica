# P002 — Inverted pendulum with a vertically oscillating pivot

**Date:** 2026-09-13 → 2026-09-14
**Verdict:** ACCEPT-WITH-FIXES (round 1; both findings MINOR, both accepted)
**Rounds:** 1
**Status:** closed

Sections 1–4 and 7 are the factual record, written by `/log` from what is in
this folder. Sections 5 and 6 are yours and are left empty on purpose. Section 5
is the one thing in the method that only you can produce — `/log` is forbidden
from writing it or improving its wording, because a model grading its own
conduct in the conversation it was part of is not evidence.

## 1. The problem

From David Morin's *Problem of the Week*, Harvard Department of Physics, Week 67
(12/22/03), "Inverted pendulum". Statement verbatim in `prompts/prompt0.md` §1;
the problem sheet itself is `prob67.pdf`, resolved from the general reference in
prompt0 and cited with its locator in `sources/sources.bib`.

A mass $m$ sits at the end of a massless stick of length $l$ whose other end is
driven vertically as $y(t)=A\cos\omega t$ with $A\ll l$. If $\omega$ is large
enough and the pendulum starts nearly upside down, it does not fall. Explain
why, and find the frequency of the back-and-forth motion.

Method constraint set in prompt0 §5: Lagrangian approach for the equation of
motion. Deliverable set in §4: full derivation, domain of validity, and a plot
of the oscillation and of where it breaks.

## 2. My first attempt

`human/attempt.md` was created by `New-Problem.ps1` and left as the empty
template. No attempt was recorded before prompt0 was sent, and none is
reconstructed here. `meta.yaml` records `human_attempt.exists: false`.

No gate turns on this. It does mean that for P002 there is no prior to compare
the model's hypotheses against, which is the one thing the human branch of the
workflow is for.

## 3. First interaction with the AI

Solver: Claude Opus 5, effort high (user-reported, from prompt0 §0), with code
execution and web access. One session, 2026-09-13.

`answers/answer-1.md`. The declared prior knowledge was complete: the solver
recognised the problem as the Kapitza pendulum on sight, wrote out the standard
result before deriving anything — stability for $A^2\omega^2>2gl$, slow
frequency $\Omega=\sqrt{A^2\omega^2/2l^2-g/l}$, and the $\sin^2$ effective
potential — and then derived it. The full declaration is in
`sources/independence.md`.

It also stated, and recorded the ordering, that no source was retrieved until
the derivation and all six computational checks were finished. That ordering is
the only thing separating this run from P001, where the model retrieved a
published solution and transcribed it.

Six checks in round 1, eight by the end:

- N1: the equation of motion re-derived symbolically from the geometry.
- N2: the same equation against a Newtonian formulation with a constraint force
  and no Lagrangian. **This check failed on its first run** and the failure is
  reported in the answer before the revision, with the diagnosis — Lyapunov
  divergence in the below-threshold whirling regime, not a disagreement between
  the formulations — and a statement that what was changed was the check and not
  the derivation.
- N3: the slow period measured on the exact nonlinear equation, converging on
  the closed form at second order in $A/l$.
- N4: the stability threshold recomputed by exact Floquet theory, with no
  averaging anywhere.
- N5, N6: the barrier angle $\Theta_{\rm c}$ and the fast-ripple envelope.
- N7, N8 were added in round 2; see section 4.

Every check is also run against deliberately mutated versions of the claim — a
flipped sign, a missing factor of two, a dropped $\sin\Theta$ — and reports
whether the mutant is rejected, so that a passing check cannot be read as
vacuous.

## 4. Audit

Auditor: Gemini 3.1 Pro Avanzado with the extended-reasoning option; effort
level unknown. Both user-reported. The report carried no run header, which
audit-prompt v1.3 would have required and v1.2, the version in force, did not.

Verdict ACCEPT-WITH-FIXES. Nine passes, seven Pass, two Partial. Two findings,
both MINOR, both accepted with no rebuttal:

- **F1.1** — the size-counting table in §3.3 asserted $\omega_0^2\ll
  \varepsilon^2\omega^2$ near threshold. False: at the boundary
  $\varepsilon^2\omega^2=2\omega_0^2$ exactly. A good finding. The error was in
  the justification and not in a step — the term was kept in the averaged
  equation throughout — and if it had been true and acted on there would have
  been no threshold at all.
- **F1.2** — standard results invoked without provenance tags. Answered by
  deriving them instead of tagging them: Lindstedt–Poincaré in the new §3.9, and
  $\det M=1$ and the $|\operatorname{tr}M|<2$ criterion in §4.4.

Two things from this round are worth keeping.

**The audit's pass-6 number does not match the audit's pass-6 code.** The report
gives `Exact: 4.2764` from a script it quotes. Run verbatim that script prints
`Exact: 4.2867`, and five different integrators agree. The audit's conclusion
survives, but the sign of the deviation is reversed. The report is committed
verbatim with the correction appended as a note, per the log skill's rule that a
wrong number in an audit report is an accurate record of what the auditor said.

**The audit's method was better than anything in round 1 for that job, and was
adopted.** Extracting $\Omega$ from the Floquet phase involves no averaging and
no curve fitting. It became check N8, swept in $\varepsilon$, and it then
produced the strongest result in the problem: N4 places the exact stability
boundary slightly *above* $\sqrt{2gl}/A$, and N8 finds the exact frequency
slightly *above* the closed form far from threshold, and those two are only
compatible if the correction to $\Omega$ changes sign in between. It does, and
the frequency vanishes exactly at the boundary N4 located by a separate
bisection. Two independently computed quantities constraining each other.

`answers/answer-2.md` was not itself audited. The stopping rule was met at round
1, and ACCEPT-WITH-FIXES means one further pass closes the MINORs; that pass is
answer-2. Its new material — §3.9, N7, N8 — has therefore never been read by an
auditor, which is recorded rather than resolved.

## 5. How the model handled being corrected

<!-- Your own read of the exchange, written after the loop closed. Nobody but
     you can write this section: it is a judgement about how the conversation
     went, not a fact recoverable from the files.

     Worth noting when it applies:
     - Did it concede anything without an argument, or concede a point you
       later decided was right after all?
     - Did it push back, and was the rebuttal any good?
     - Did any answer look retrieved rather than derived, and what gave it
       away?
     - Did a correction of yours send it somewhere worse?
     - Anything it did that you would not have predicted.

     One honest paragraph beats a checklist. Delete the section if nothing
     about the exchange was worth recording. -->

## 6. Reflection

<!-- Yours. This section is the point of the logbook, and /log does not write
     it. What actually happened, in your own words: whether the loop earned its
     cost on this problem, whether the audit found anything you would not have,
     and whether you believe the result more than you did before. -->

## 7. What this problem changed in the method

Three things surfaced that are about the workflow rather than about the physics.
None has been acted on; they are recorded here and, where they belong there, in
`claude/workflow-feedback.md`.

**§6.3 of prompt0 can burn the ground truth.** The solver is required to
retrieve and confirm its *Used* sources. For a problem whose source is a
problem-of-the-week sheet, the solution sheet sits next to the problem sheet, so
obeying §6.3 means opening the answer key during the loop. It was opened after
the derivation and all checks were complete, and the ordering is recorded, but
it is now inside the loop: `meta.yaml` has `ground_truth.arrived: mid-loop`, and
rounds 2 and later cannot also be validated by it. The clean fix is for the
solution sheet to be retrieved by the auditor, or after the loop closes.

**The freeze and cross-references interact.** Round 2 needed to add two checks
to §4. Inserting them in check order would have renumbered §4.6 and §4.7, which
are referenced from frozen sections of §3, so they were appended as §4.8 and
§4.9 instead. Separately, a stale cross-reference inside frozen §3.8 was found
and deliberately left uncorrected, since silently editing a frozen section is
the failure the freeze exists to prevent. Both are small; both suggest the
frozen list should say whether cross-reference repair counts as a rewrite.

**`rebuttals_upheld: 0` is uninformative here.** `claude/workflow-feedback.md`
§5 tracks it as the detector for sycophantic drift. On P002 both findings were
correct and conceding them was right, so the zero says nothing about whether the
solver would have disagreed. The nearest thing to a disagreement in this problem
went the other way: the solver contested a number in the audit report, not a
finding. That may be worth its own counter.

## Where things are

| | |
|---|---|
| The result, as a document | `final/final.md`, `final.tex`, `final.pdf` |
| What the model knew going in | `sources/independence.md` |
| Per-claim tag ledger | `sources/provenance.md` |
| The audit, verbatim | `audits/audit-report-1.md` |
| Findings and their disposition | `audits/findings.yaml` |
| Every script, its output, and its blind spots | `assets/code/` |
| Machine-readable metadata | `meta.yaml` |
