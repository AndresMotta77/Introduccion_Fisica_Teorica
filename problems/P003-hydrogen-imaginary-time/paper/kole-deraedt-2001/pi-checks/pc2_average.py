"""
pc2_average.py  (PI check, not a solver artifact)

Kole and De Raedt remark below Table I that (Ehat_m + E_m)/2 is remarkably close to the
exact energy and say they have no justification. Question: is this an exact cancellation
of the leading 1/m^2 errors, and what order is the residual?

Uses route B of pc1_table1.py (re-derived (19), printed (20)), which agreed with the
independent matrix route C to <= 3.4e-8 (pc1b). hbar = M = omega = 1, V = x^2/2, mpmath at
40 digits so that differences of order 1e-12 are resolved.

What would count as "no exact cancellation": m^2 * (err_hat + err_prim) tending to a
nonzero constant as m grows. What would count as cancellation: that quantity tending to 0,
with the rate giving the order of the residual.
"""
from mpmath import mp, mpf, cos, pi, coth, log
mp.dps = 40
def Ehat(b, m):
    s = sum((2+cos(2*pi*n/m))/(1-cos(2*pi*n/m)+b**2*(2+cos(2*pi*n/m))/(6*m**2)) for n in range(m))
    return b/(6*m)*(1+s/m)
def Etr(b, m):
    s = sum(1/(1-cos(2*pi*n/m)+b**2/(2*m**2)) for n in range(m))
    return b/(2*m**2)*s
for b in (mpf(1), mpf(5), mpf(10)):
    ex = coth(b/2)/2
    prev = None
    print(f"beta = {b}")
    for m in (100, 200, 400, 800, 1600):
        eh, et = Ehat(b, m) - ex, Etr(b, m) - ex
        s2 = (eh + et) * m**2
        slope = "" if prev is None else f"  local order of (err_hat+err_prim): {float(-log(abs(eh+et)/prev[1])/log(mpf(m)/prev[0])):.3f}"
        print(f"  m={m:5d}  m^2*err_hat={float(eh*m**2):+.8f}  m^2*err_prim={float(et*m**2):+.8f}  m^2*(sum)={float(s2):+.3e}{slope}")
        prev = (m, abs(eh + et))
