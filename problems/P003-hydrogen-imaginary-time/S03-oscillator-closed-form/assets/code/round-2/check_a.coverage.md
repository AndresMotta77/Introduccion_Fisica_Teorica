#### A: `check_a.py` — $w$ against direct numerical evaluation of its definition `[N]`

What it tests. At 13 points ($8$ random with seed 20261112, plus $(0,0,1)$; widely separated endpoints at small $\tau$, $(2,-2,10^{-3})$; large $\tau=20$; $\tau=5$ with $x=-4$, $x'=3$; and $\tau=\sqrt6$), it computes $I$ by nested 30-digit tanh-sinh quadrature of the definition. The $y$-breakpoints are found numerically from the integrand, so the check does not import $\bar y$ or $\sigma^2$. It compares the result with (8). Failure: relative difference $>10^{-12}$, or mpmath error estimates above that level. It also reports the discrepancy of four wrong candidate formulas (primitive symmetric split, missing $\tau^2/12$, doubled cross term, $\tau^2/6$) against the same numerics, to show the check discriminates.

What it would catch: any error in (8) or (9) larger than $10^{-12}$ relative at these points, including wrong coefficients of $x^2$, $xx'$, $x'^2$ or of the constant, since the points vary all of these.

What it would not catch: an error that vanishes at all 13 points (implausible for a polynomial in $x,x'$ with $\tau$-dependent coefficients, but not excluded). It also would not catch a misreading of the problem's definition shared between the code and the derivation; the code transcribes the definition literally, as written in the prompt.
