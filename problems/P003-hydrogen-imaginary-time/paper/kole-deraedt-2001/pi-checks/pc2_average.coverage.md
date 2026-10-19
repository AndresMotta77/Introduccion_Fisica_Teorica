# Coverage — pc2_average.py

PI check run while planning P003. Prior knowledge; must not be attached to a solver prompt
for chunk K6.

## Result

For the oscillator, the leading errors of E_m (primitive) and Ê_m (Jensen) are of order
1/m² with equal magnitude and opposite sign: m² times their sum goes to zero, at a local
order that approaches 3 for β = 1, 5 and 10. The average (E_m + Ê_m)/2 therefore converges
as m⁻³, one order faster than either approximant. The residual comes from Ê_m, whose m² × error still drifts as 1/m
at m = 1600, while that of E_m has settled. This answers the remark below Table I
numerically for one potential. It does not explain it.

## Would have caught

- A nonzero sum of the leading coefficients: m² × (sum) would have tended to a constant.
- A residual of order m⁻⁴ or m⁻²: the local order would have gone to 4 or 2.

## Would not have caught

- Anything beyond the harmonic oscillator. Whether the cancellation holds for other
  potentials is the open question of chunk K6; the oscillator is the case where both
  approximants are Gaussian, so it may be special.
- An error in route B that route C did not detect. Route C (pc1) confirms route B only to
  about 3e-8, the limit of its finite difference. At β = 1 that is comparable to the
  1/m² errors at m = 1600 (3.9e-8) and far above the summed residual there (m² × sum =
  −1.7e-5, so the sum itself is about −7e-12). The cancellation and the order 3 rest on
  route B alone, evaluated at 40 digits.

## Inputs

Route B formulas from pc1_table1.py, re-typed into this script (same expressions).
mpmath 1.4.1, Python 3.13.16. Deterministic.
