# C5: the Kato-class quantity for V = -1/r in three dimensions, eq. (C3)-(C5).
# Environment: Python 3.13.16, numpy 2.5.3, scipy 1.18.1. Deterministic.
#
#   f_delta(x) = int_{|y-x|<delta} d^3y / (|y| |x-y|)
# Claim derived in the answer (AM-GM plus the bathtub comparison): f_delta(x) <= 4 pi delta for every x.
# Recalled comparison formula [R] (Newton's theorem for the shell average of 1/|x+s w|):
#   f_delta(x) = 4 pi (delta - |x|/2) for |x| <= delta,  2 pi delta^2/|x| for |x| >= delta.
# Computed here by direct quadrature in coordinates centred at x: y = x + s w, d^3y = s^2 ds dOmega,
#   f = 2 pi int_0^delta s ds int_{-1}^{1} dc (|x|^2 + s^2 + 2|x| s c)^(-1/2).
# Declared failure: any value exceeding 4 pi delta (1 + 1e-8), or disagreement with the recalled
# formula by more than 1e-7 relative (the latter would falsify only the [R] formula, not the bound).
import numpy as np
from scipy.integrate import quad

fails = []
print(" delta   |x|/delta   f (quadrature)     4 pi delta      Newton formula [R]   rel.diff")
for delta in (0.1, 1.0):
    for q in (0.0, 0.1, 0.5, 0.99, 1.0, 1.5, 3.0):
        X = q * delta
        def inner(s_):
            if X == 0.0:
                return 2.0 / s_ * s_  # int_{-1}^{1} dc / s = 2/s, times s
            g = lambda c: 1.0 / np.sqrt(X * X + s_ * s_ + 2 * X * s_ * c)
            pts = [-1.0, 1.0]
            val, _ = quad(g, -1.0, 1.0, epsabs=0, epsrel=1e-12, limit=200, points=None if abs(s_ - X) > 1e-12 else None)
            return s_ * val
        f, _ = quad(inner, 0.0, delta, epsabs=0, epsrel=1e-11, limit=400, points=[X] if 0 < X < delta else None)
        f *= 2 * np.pi
        newton = 4 * np.pi * (delta - X / 2) if X <= delta else 2 * np.pi * delta**2 / X
        rel = abs(f - newton) / newton
        print(f" {delta:<6} {q:<10}  {f:.12f}   {4*np.pi*delta:.12f}   {newton:.12f}    {rel:.1e}")
        if f > 4 * np.pi * delta * (1 + 1e-8):
            fails.append(("bound", delta, q))
        if rel > 1e-7:
            fails.append(("newton", delta, q))
print("FAILURES:", fails if fails else "none")
