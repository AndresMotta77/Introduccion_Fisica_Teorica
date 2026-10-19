# Coverage — pc1_table1.py and pc1b_fd_step.py

PI checks run while planning P003, before any solver run. They are prior knowledge for
anyone who reads them, and must not be attached to a solver prompt for chunk K5.

## What was run

`pc1_table1.py`, once, output in `pc1_table1.out`. `pc1b_fd_step.py`, once, output in
`pc1b_fd_step.out`. Neither script was edited after it ran.

The pre-stated agreement criterion between the PI's two routes (|B − C| < 1e-7) failed:
the largest gap was 3.35e-7, at m = 500. `pc1b` shows that the gap depends on the
finite-difference step of route C, with a minimum at an intermediate step (3.4e-8 at worst
over the rows tested), which is the signature of truncation against round-off. The two
routes therefore agree to the precision the finite difference allows. The 1e-7 criterion
was too tight for a centred difference of a 500 × 500 log-determinant at h = 1e-5. That was
a mistake in setting the tolerance, and it says nothing about the paper.

## Would have caught

- Eq. (19) as printed being usable: route A grows with m (4.84 at β = 1, m = 100, against
  the exact 1.08198), so the printed formula cannot have produced Table I.
- A wrong re-derivation of (19) by the PI (route B), since route C does not use (18)–(20)
  at all: it builds the quadratic forms term by term from (17) and from the primitive (3).
- Misreading Table I: the exact column is asserted against (1/2) coth(β/2) for all rows.
- Discrepancies in Table I larger than rounding. Five of fifteen rows are flagged. Two are
  at the level of the last printed digit: (β = 1, m = 1), Ê = 7/6 printed as 1.16668; and
  (β = 5, m = 10), off by 0.7 and 2.3 units of the fifth decimal. Three are not:
  (β = 5, m = 50) Ê off by 4.4e-4; (β = 5, m = 100) E_m off by −1.5e-4 and Ê by +1.5e-4;
  (β = 10, m = 10) E_m printed 0.44273 where both routes give 0.447273, which looks like a
  dropped digit.

## Would not have caught

- An error shared by (17) and the PI's reading of it. Route C takes (17) as given, with
  V = x²/2. If (17) itself were wrong in a way that still reproduces the other twelve rows,
  this check would not see it. Check 7 of the proposal derived the bridge average
  independently and agrees with (17) read this way.
- Whether the three discrepant rows are typesetting errors or rows computed at a different
  m. The β = 5, m = 100 published values are close to the m = 500 values, which suggests
  the latter, but this check cannot tell.
- Anything about the Coulomb case.

## Inputs and assumptions

- [A] V = x²/2 (the paper prints V = Mω²x²; see errata E5). Under V = Mω²x² the exact
  column would be (1/√2) coth(β/√2) and would not match the table.
- [A] Cyclic paths x_{m+1} = x_1, as in (3) and (16).
- Table I values were read by the PI from a 110 dpi rendering of page 4 of the arXiv v1
  PDF. The published Phys. Rev. E version has not been compared.
