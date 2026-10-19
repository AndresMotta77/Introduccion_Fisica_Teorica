# C3: composition law of the free kernel, used in the large-r (volume) argument, eq. (B9)-(B10).
# Environment: Python 3.13.16, numpy 2.5.3, scipy 1.18.1, sympy 1.14.0. Seed fixed below.
#
# Claim (1D factor; the 3D kernel is the product of three such factors):
#   int dy rho1(x,y;s) rho1(y,z;t) = rho1(x,z;s+t),   rho1(x,y;t) = (2 pi t)^(-1/2) exp(-(x-y)^2/(2t)).
# (i) Symbolic: the completing-the-square identity of eq. (B9), written out independently on both sides.
# (ii) Numerical: quadrature of the left side vs the right side at random (x,z,s,t), including points near
#      the edges (s/t very small or very large, |x-z| several widths). Tolerance 1e-9 relative.
# Declared failure: symbolic difference not identically zero, or any relative discrepancy > 1e-9.
import numpy as np
import sympy as sp
from scipy.integrate import quad

x, y, z = sp.symbols('x y z', real=True)
s, t = sp.symbols('s t', positive=True)   # [A] s, t > 0: imaginary-time steps are positive
lhs = -(x - y)**2 / (2 * s) - (y - z)**2 / (2 * t)
rhs = -(s + t) / (2 * s * t) * (y - (t * x + s * z) / (s + t))**2 - (x - z)**2 / (2 * (s + t))
print("(i) symbolic: expand(lhs - rhs) =", sp.simplify(sp.expand(lhs - rhs)))
fails = []
if sp.simplify(sp.expand(lhs - rhs)) != 0:
    fails.append("symbolic")

rng = np.random.default_rng(7)
rho = lambda a, b, tt: np.exp(-(a - b) ** 2 / (2 * tt)) / np.sqrt(2 * np.pi * tt)
cases = [(rng.uniform(-3, 3), rng.uniform(-3, 3), rng.uniform(0.05, 3), rng.uniform(0.05, 3)) for _ in range(8)]
cases += [(0.0, 0.0, 1e-3, 5.0), (2.0, -2.0, 5.0, 1e-3), (0.0, 6.0, 0.5, 0.5), (1.0, 1.0, 0.01, 0.01)]
print("(ii) numerical composition, x z s t -> relative error")
for (xx, zz, ss, tt) in cases:
    c = (tt * xx + ss * zz) / (ss + tt); w = np.sqrt(ss * tt / (ss + tt))
    val, err = quad(lambda yy: rho(xx, yy, ss) * rho(yy, zz, tt), c - 40 * w, c + 40 * w, epsabs=0, epsrel=1e-13, limit=200)
    ref = rho(xx, zz, ss + tt)
    rel = abs(val - ref) / ref
    print(f"  {xx:+.3f} {zz:+.3f} {ss:.4f} {tt:.4f}  ->  {rel:.2e}")
    if rel > 1e-9:
        fails.append((xx, zz, ss, tt))
print("FAILURES:", fails if fails else "none")
