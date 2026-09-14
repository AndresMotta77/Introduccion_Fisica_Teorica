# Coverage note — check1_eom_symbolic.py

Checks: N1. Full discussion, with the verbatim output, in
`answers/answer-2.md` §4.1 — "4.1 Check N1 — the equation of motion, symbolically, from the geometry".

Required by `CONVENTIONS.md` §1.1: a check with no stated blind spot has not
been thought about. Both halves are reproduced here verbatim from the answer so
that this file can be read on its own.

Output: `out_check1.txt` in this directory.

---

What this would have caught: any algebra slip between (1) and (16) — a dropped
cross term in (6), a sign error in (12) or (13), a failure of the
$\dot y_p\dot\theta\cos\theta$ cancellation. The sign-flipped mutant is rejected
with a nonzero residual, so the test is not vacuous.

What it would **not** have caught: a wrong setup. If (1) itself encoded the
geometry incorrectly — the pivot moving horizontally, say, or $\theta$ measured
from the wrong axis — sympy would faithfully derive the equation of motion for
that wrong problem and report PASS. It also says nothing about §3.3 onwards.
Check N2 addresses the first gap; checks N3–N5 address the second.

