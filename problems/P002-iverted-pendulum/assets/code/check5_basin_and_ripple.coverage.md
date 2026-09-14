# Coverage note — check5_basin_and_ripple.py

Checks: N5 and N6. Full discussion, with the verbatim output, in
`answers/answer-2.md` §4.5 — "4.5 Checks N5 and N6 — the barrier angle, and the fast ripple".

Required by `CONVENTIONS.md` §1.1: a check with no stated blind spot has not
been thought about. Both halves are reproduced here verbatim from the answer so
that this file can be read on its own.

Output: `out_check5.txt` in this directory.

---

What these would have caught: N5 would have caught a wrong barrier angle, and
does reject the below-threshold control, where no release angle at all is held.
N6 rejects the $\sin\Theta$-free mutant decisively, with the ratio ranging from
0.028 to 0.55 instead of 1. Together they test the parts of §3 that N3 and N4 do
not: the shape of the effective potential away from $\Theta=0$, and the fast
solution (24) on which the entire averaging rests.

What they would **not** have caught: N5 uses a specific escape criterion
($|\theta|>2.5$ rad) and a finite integration window of 25 slow periods; a
trajectory that escapes only after much longer would be counted as bound, so the
measured boundary is an upper bound on the true one. Near the separatrix the
slow motion is arbitrarily slow, so this is a real limitation and not a
formality. N6 is run at a single $\varepsilon$ and a single amplitude, so it
verifies the form of (24) but not its convergence order.

