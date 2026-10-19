# C5 (run 2): the Kato-class quantity for V = -1/r in three dimensions, eq. (C3)-(C5).
# Environment: Python 3.13.16, mpmath 1.3.0. Deterministic.
# CHANGE FROM RUN 1 (c5_kato_class_run1_scipy.py): run 1 used scipy QUADPACK and failed the comparison with
# the recalled Newton formula at |x|/delta = 0.99 by 1.6e-7 (tolerance 1e-7), with QUADPACK reporting
# non-convergence for exactly that inner integral (integrable singularity at c = -1 when s ~ |x|).
# Run 2 changes ONLY the quadrature method (mpmath tanh-sinh, outer integral split at s = |x|).
# Tolerances, the formula and the bound are unchanged.
#
#   f_delta(x) = int_{|y-x|<delta} d^3y / (|y| |x-y|)
# Claim derived in the answer (AM-GM plus the bathtub comparison): f_delta(x) <= 4 pi delta for every x.
# Recalled comparison formula [R] (Newton's theorem): f = 4 pi (delta - |x|/2) for |x| <= delta,
#   2 pi delta^2/|x| for |x| >= delta.
# Computed by direct quadrature centred at x: f = 2 pi int_0^delta s ds int_{-1}^{1} dc (|x|^2+s^2+2|x|s c)^(-1/2).
# Declared failure: any value exceeding 4 pi delta (1 + 1e-8), or disagreement with the recalled
# formula by more than 1e-7 relative.
import mpmath as mp
mp.mp.dps = 30
fails = []
print(" delta   |x|/delta   f (quadrature)      4 pi delta        Newton formula [R]   rel.diff")
for delta in (mp.mpf('0.1'), mp.mpf(1)):
    for q in ('0', '0.1', '0.5', '0.99', '1', '1.5', '3'):
        X = mp.mpf(q) * delta
        def inner(s_):
            if X == 0:
                return mp.mpf(2)
            return s_ * mp.quad(lambda c: 1 / mp.sqrt(X**2 + s_**2 + 2 * X * s_ * c), [-1, 1])
        brk = [0, X, delta] if 0 < X < delta else [0, delta]
        f = 2 * mp.pi * mp.quad(inner, brk)
        newton = 4 * mp.pi * (delta - X / 2) if X <= delta else 2 * mp.pi * delta**2 / X
        rel = abs(f - newton) / newton
        print(f" {mp.nstr(delta,3):<6} {q:<10}  {mp.nstr(f,15):<18} {mp.nstr(4*mp.pi*delta,15):<17} {mp.nstr(newton,15):<20} {mp.nstr(rel,2)}")
        if f > 4 * mp.pi * delta * (1 + mp.mpf('1e-8')):
            fails.append(("bound", float(delta), q))
        if rel > mp.mpf('1e-7'):
            fails.append(("newton", float(delta), q))
print("FAILURES:", fails if fails else "none")
