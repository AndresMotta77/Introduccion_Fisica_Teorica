#### S1–S6: `check_algebra.py`

What it tests.
- S1 recomputes $I$ from the definition with sympy's own Gaussian integration, with no completion of the square supplied by hand; this is the strongest check on (8).
- S2 checks my completion of the square (algebra only).
- S3 and S4 build the $m\times m$ Hessian of the actual ring action for $m=1..7$ and compare $\det(\tau A)$ with $D_m^2$. This tests the circulant diagonalisation, the product formula and the small-ring cases.
- S5 checks the parameter identities behind (23) and (24).
- S6 produces the series (27), (28) and checks the equivalence of the two forms of (25).

What it would catch: any error in the $y$- or $u$-integrals (S1); a wrong eigenvalue, a wrong product identity or a wrong treatment of $m=1,2$ (S3, S4); algebra slips in $\kappa$, $s_\pm$, $q$ (S5); wrong series coefficients (S6).

What it would not catch. S2, S5 and S6 test my algebra, not the physics: they take my intermediate expressions as input. S3 and S4 take $w$ from (9) as input, so an error in (9) would propagate into them unnoticed (that is covered by S1 and `check_a.py`). S6 expands my closed form (25), so it cannot detect an error in (25) itself (C1, C5 do). S1 relies on sympy's integrator being right, which `check_a.py` covers independently.
