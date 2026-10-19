# Coverage note — c6_f11_bound.py

Check: Check C6 [N]. The bound on the bound-state sum (finding F1.1). Full discussion, with the verbatim code and output, in `answers/answer-2.md` §10.

Required by `CONVENTIONS.md` §1.1: a check with no stated blind spot has not been thought about. The text below is reproduced verbatim from the answer, so that this file can be read on its own.

Output: `c6_f11_bound.out` in this directory. Run once, in round 2.

---

What it tests. The inequality $\sum_{n\ge1}e^{\tau/2n^2}/(\pi n^3)\le e^{\tau/2}\zeta(3)/\pi$ at eight values of $\tau$ from $10^{-6}$ to 40, with the sum evaluated by mpmath's `nsum` at 30 digits. It also tests that the ratio of the two sides tends to 1 as $\tau\to0$. The failure criteria were declared in the script before it was run.

What it would have caught. A bound that is too small, which would show up as a violation; for example $e^{\tau/2}/\pi$ without the factor $\zeta(3)$. Also a constant that is too large by a fixed factor, which would fail the $\tau\to0$ test; for example $\zeta(2)$ in place of $\zeta(3)$, where the ratio would tend to $\zeta(3)/\zeta(2)\approx0.73$.

What it would not have caught. A bound that is valid but looser in its $\tau$ dependence, such as $e^{\tau}\zeta(3)/\pi$; that would not be an error. Anything else in (C5), in particular the continuum term and the recalled spectral data, which route (ii) of C4 covers.

Assumptions. None beyond $\tau>0$.

Outcome. No failures. The sums agree with the bound-state parts printed by C4 at $\tau=0.5,1,2,4$. That agreement is only consistency, since both use the same formula. As $\tau$ grows, the ratio tends to $1/\zeta(3)\approx0.832$, because the $n=1$ term dominates; this was stated in the script header before the run. The script was run once.
