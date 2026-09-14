# Coverage note — check7_floquet_frequency.py

Checks: N8. Full discussion, with the verbatim output, in
`answers/answer-2.md` §4.9 — "4.9 Check N8 — the slow frequency from the Floquet phase".

Required by `CONVENTIONS.md` §1.1: a check with no stated blind spot has not
been thought about. Both halves are reproduced here verbatim from the answer so
that this file can be read on its own.

Output: `out_check7.txt` in this directory.

---

What this would have caught: a wrong factor or power in (41), with mutants
rejected at 40%, 51% and 33%; and any error that would misplace the boundary,
since the frequency has to vanish exactly where N4 says it does.

What it would **not** have caught: anything nonlinear — this is the $a\to0$
limit and says nothing about $\Theta_{\rm c}$, the basin, or finite-amplitude
periods. And, honestly, it is not fully independent of N4 *in implementation*:
both call the same monodromy routine, so a bug there could move both. They
extract different functions of the same matrix — N4 uses $|\operatorname{tr}M|$
against 2, N8 uses $\arccos(\operatorname{tr}M/2)$ — and the shared routine is
itself witnessed from outside by $\det M-1\sim10^{-15}$ and by N4's
$\varepsilon=0$ block reproducing $2\cosh(2\pi\sqrt G)$ to ten digits, but a
reader should know the two share a code path.
