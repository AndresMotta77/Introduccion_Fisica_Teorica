# Coverage note — check2_newton_vs_lagrange.py

Checks: N2. Full discussion, with the verbatim output, in
`answers/answer-2.md` §4.2 — "4.2 Check N2 — the equation of motion against Newton with a constraint force".

Required by `CONVENTIONS.md` §1.1: a check with no stated blind spot has not
been thought about. Both halves are reproduced here verbatim from the answer so
that this file can be read on its own.

Output: `out_check2.txt` in this directory.

---

What this would have caught: a wrong equation of motion, including the class of
error N1 cannot see, because the Newtonian route rebuilds the dynamics from
force balance and a geometric constraint rather than from $T-V$. The
sign-flipped mutant separates by $1.6\times10^{-2}$ rad against
$6.5\times10^{-12}$ for the claim, a ratio of $10^{9}$, so the check is not
vacuous. It would also have caught a wrong pivot acceleration, since $\ddot y_p$
enters both formulations independently.

What it would **not** have caught: a shared error in the geometry, which both
formulations inherit from (1) — if the pivot were supposed to move horizontally,
both would agree on the wrong answer. It would not catch anything about §3.3
onwards. And, as the failure showed, it certifies agreement only over times
short compared with the Lyapunov time in the whirling regime; in that regime the
check verifies the equations agree for the first tens of drive periods
($1.3\times10^{-10}$ rad over 20 drive periods for set 8) and nothing beyond.
For the regime the problem is actually about — near-inverted, above threshold —
agreement holds over the whole window at the $10^{-11}$ level.

