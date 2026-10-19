# Coverage note — c1_radial_growth.py

Check: C1 [N]. One-bead radial integral against the growth law (B2) and (B6). Full discussion, with the verbatim code and output, in `answers/answer-2.md` §4.2.

Required by `CONVENTIONS.md` §1.1: a check with no stated blind spot has not been thought about. The text below is reproduced verbatim from the answer, so that this file can be read on its own.

Output: `c1_radial_growth.out` in this directory. Run twice in round 1 and once in round 2, with the code unchanged; all three outputs are byte-identical (compared with `cmp`). The `.out` file is the round-2 output.

---

What it tests. It computes $4\pi\int_\eta^\varepsilon r^2e^{a/r}dr$ by direct quadrature in $r$. The integrand comes straight from the potential factor $e^{-\Delta\tau V}$ with $V=-1/r$ and $a=\Delta\tau$, not from the derivation. The result is compared with the lower bound (B2), with the leading law and its first correction, and with the three-term law (B6). The failure criteria were declared in the script before it was run.

What it would have caught. A wrong power of $\eta$ or a wrong exponent in the growth law; a wrong coefficient (for example $1/a$); a violation of the logarithmic lower bound. The contrast column, the ratio to the wrong law $\eta^3e^{a/\eta}$, decays like $\eta$, which shows the check can tell neighbouring powers apart.

What it would not have caught. Errors in going from $Z_N$ to the one-bead integral; the prefactor $(2\pi\Delta\tau)^{-3N/2}$; anything about the kinetic factor or the large-volume divergence. Rows with $a/\eta\le10$ are outside the asymptotic regime: they are reported and tested only against the lower bound.

Assumptions. The quadrature breakpoints are placed at multiples of $\eta^2/a$, a scale that comes from my analysis. A wrong scale would make the quadrature less accurate and show up as failures, not as passes. The mpmath working precision is 50 digits.

Outcome. All criteria pass. At $a/\eta=160$: $I/L_1=1.0258$; $(I/L_1-1)/(\eta/a)=4.130$, against a prediction of $4+20\eta/a=4.125$; and $I/L_3-1=2.99\times10^{-5}$, against $120(\eta/a)^3=2.93\times10^{-5}$.
