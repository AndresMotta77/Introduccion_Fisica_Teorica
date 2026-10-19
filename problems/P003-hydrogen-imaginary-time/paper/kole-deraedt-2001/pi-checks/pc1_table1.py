"""
pc1_table1.py  (PI check, not a solver artifact)

Question: do the printed eqs. (18)-(20) of Kole and De Raedt, arXiv:physics/0102015v1,
and their Table I agree with the slice weights they are derived from?

Units hbar = M = omega = 1. The exact energy is (1/2) coth(beta/2), i.e. V = x^2/2.

Route A  eq. (19) exactly as printed.
Route B  eq. (19) re-derived by the PI from (17): a factor 1/m in front of the sum and
         m^2 (not m) in the denominator. Eq. (20) as printed.
Route C  independent of (18)-(20): build the m x m quadratic forms of eq. (17) (read with
         V = x^2/2) and of the primitive eq. (3) with V = x^2/2, take ln Z from slogdet,
         and E = -d ln Z / d beta by a centred finite difference.
Routes B and C share only the input equations (17) and (3).

What counts as failure, stated before running: a Table I entry that differs from route C
by more than 6e-6 (published values have 5 decimals) is flagged; B and C differing by more
than 1e-7 anywhere means one of the PI's two routes is wrong.

Python 3.13.16, numpy 2.5.3, mpmath 1.4.1. Deterministic, no random numbers.
"""
import numpy as np
from mpmath import mp, mpf, cos, pi, coth

mp.dps = 30

# ---- Route A: printed (19)
def Ehat_printed(b, m):
    s = sum((2 + cos(2*pi*n/m)) / (1 - cos(2*pi*n/m) + b**2*(2 + cos(2*pi*n/m))/(6*m)) for n in range(m))
    return b/(6*m) * (1 + s)

# ---- Route B: re-derived (19), printed (20)
def Ehat_B(b, m):
    s = sum((2 + cos(2*pi*n/m)) / (1 - cos(2*pi*n/m) + b**2*(2 + cos(2*pi*n/m))/(6*m**2)) for n in range(m))
    return b/(6*m) * (1 + s/m)

def Em_B(b, m):
    s = sum(1 / (1 - cos(2*pi*n/m) + b**2/(2*m**2)) for n in range(m))
    return b/(2*m**2) * s

# ---- Route C: quadratic forms built term by term from (17) and (3)
def lnZ_C(beta, m, kind):
    a = m / (2*beta)                    # kinetic coefficient M/(2 tau hbar^2), tau = beta/m
    A = np.zeros((m, m))
    const = 0.0
    for n in range(m):
        p, q = n, (n + 1) % m           # cyclic path, x_{m+1} = x_1
        d = np.zeros(m); d[p] += 1; d[q] -= 1
        A += a * np.outer(d, d)
        if kind == "jensen":            # (beta M w^2 / 6m)(x_n^2 + x_{n+1}^2 + x_n x_{n+1} + beta hbar^2/(2 m M)), V = x^2/2
            c = beta / (6*m)
            ep, eq = np.eye(m)[p], np.eye(m)[q]
            A += c * (np.outer(ep, ep) + np.outer(eq, eq) + 0.5*(np.outer(ep, eq) + np.outer(eq, ep)))
            const -= c * beta / (2*m)
        else:                           # primitive: exp(-beta V(x_{n+1})/m), V = x^2/2
            A[q, q] += beta / (2*m)
    sign, logdet = np.linalg.slogdet(A)
    assert sign > 0, "quadratic form not positive definite"
    return 0.5*m*np.log(m/(2*np.pi*beta)) + 0.5*m*np.log(np.pi) - 0.5*logdet + const

def E_C(beta, m, kind):
    h = 1e-5
    return -(lnZ_C(beta + h, m, kind) - lnZ_C(beta - h, m, kind)) / (2*h)

# Table I as printed (read from the page image of arXiv v1, p. 4): (beta, m): (E_m, E, Ehat_m)
pub = {(1, 1): (1.00000, 1.08198, 1.16668), (1, 10): (1.08101, 1.08198, 1.08292),
       (1, 50): (1.08194, 1.08198, 1.08202), (1, 100): (1.08197, 1.08198, 1.08199),
       (1, 500): (1.08198, 1.08198, 1.08198),
       (5, 1): (0.20000, 0.50678, 1.03333), (5, 10): (0.49199, 0.50678, 0.51938),
       (5, 50): (0.50617, 0.50678, 0.50694), (5, 100): (0.50678, 0.50678, 0.50679),
       (5, 500): (0.50678, 0.50678, 0.50679),
       (10, 1): (0.10000, 0.50005, 1.76667), (10, 10): (0.44273, 0.50005, 0.54316),
       (10, 50): (0.49757, 0.50005, 0.50234), (10, 100): (0.49942, 0.50005, 0.50064),
       (10, 500): (0.50002, 0.50005, 0.50007)}

print("Route A, printed eq. (19), against the exact energy:")
for b in (1, 5, 10):
    vals = ", ".join(f"m={m}: {float(Ehat_printed(mpf(b), m)):.5f}" for m in (1, 10, 50, 100))
    print(f"  beta={b:2d}  exact={float(coth(mpf(b)/2)/2):.5f}   {vals}")

print("\nRoutes B and C against Table I (flag: |C - published| > 6e-6):")
print(" beta    m |  E_m: B        C        pub    C-pub   |  Ehat_m: B        C        pub    C-pub   | max|B-C|")
worst_BC = 0.0
flags = []
for (b, m), (Ep, Xp, Hp) in pub.items():
    eB, hB = float(Em_B(mpf(b), m)), float(Ehat_B(mpf(b), m))
    eC, hC = E_C(float(b), m, "prim"), E_C(float(b), m, "jensen")
    x = float(coth(mpf(b)/2)/2)
    assert abs(x - Xp) < 6e-6, "exact column misread"
    dBC = max(abs(eB - eC), abs(hB - hC)); worst_BC = max(worst_BC, dBC)
    f = []
    if abs(eC - Ep) > 6e-6: f.append(f"E_m off by {eC-Ep:+.1e}")
    if abs(hC - Hp) > 6e-6: f.append(f"Ehat_m off by {hC-Hp:+.1e}")
    if f: flags.append(((b, m), f))
    print(f" {b:4d} {m:4d} | {eB:.6f} {eC:.6f} {Ep:.5f} {eC-Ep:+.1e} | {hB:.6f} {hC:.6f} {Hp:.5f} {hC-Hp:+.1e} | {dBC:.1e}"
          + ("   <-- " + "; ".join(f) if f else ""))
print(f"\nlargest |B - C| over all rows: {worst_BC:.2e}  (routes agree: {worst_BC < 1e-7})")
print(f"rows flagged: {len(flags)} of {len(pub)}")
for k, f in flags:
    print("  ", k, "; ".join(f))
