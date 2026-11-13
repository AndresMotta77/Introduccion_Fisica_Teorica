# check_extra.py -- P003.S02, check N8 [N], added after runs of check_numeric.py.
# Standalone. Python 3.13.18, numpy 2.5.3, scipy 1.18.1. No randomness.
# Tests the Delta-dependent tau^4 terms of eq. (28) for a non-quadratic potential:
#   delta = D tau^3 V'^2/12 + D tau^3 V''^2 Delta^2/720 + D tau^3 V' V''' Delta^2/240
#           + D^2 tau^4 (V''^2/90 + V' V'''/30) + O(tau^5)      (1D, derivatives at xbar)
# With D = 1/2 and Delta = 2 sqrt(tau):  delta/tau^3 = a + b tau + ..., a = D V'^2/12,
#   b = V''^2/180 + V' V'''/60.
# Exact kernel: sinc-DVR exactly as in check_numeric.py N5 (validated there against
# rho0 and Mehler to ~1e-11). tau values chosen so x = xbar - sqrt(tau), x' = xbar + sqrt(tau)
# are grid points (h = 0.04). FAIL if |a_fit/a_pred - 1| > 1e-3 or |b_fit - b_pred| > 0.05 |b_pred|.
import numpy as np
from scipy import linalg

print("numpy", np.__version__)
h, Lb, D = 0.04, 12.0, 0.5
xg = np.arange(-Lb, Lb + h/2, h); N = len(xg)
idx = np.arange(N); dif = idx[:, None] - idx[None, :]
T = np.where(dif == 0, D*np.pi**2/(3*h**2), 2*D*(-1.0)**dif/(h**2*np.where(dif == 0, 1, dif)**2))
V0, k = 1.0, 1.0
E, U = linalg.eigh(T + np.diag(V0*np.cos(k*xg)))


def log_rho0(p, q, t):
    return -0.5*np.log(4*np.pi*D*t) - (p - q)**2/(4*D*t)


def int_avgV_cos(x, xp, tau, n=80):
    g, w = np.polynomial.legendre.leggauss(n)
    u = 0.5*tau*(g + 1)
    m = x + (u/tau)*(xp - x); s2 = 2*D*u*(tau - u)/tau
    return 0.5*tau*np.sum(w*V0*np.cos(k*m)*np.exp(-0.5*k**2*s2))


taus = [0.0256, 0.04, 0.0576, 0.1024, 0.16]
for xb in [0.4, 0.8, 1.2, 2.0, 2.8]:
    ys = []
    for t in taus:
        r = np.sqrt(t)
        i, j = int(round((xb - r + Lb)/h)), int(round((xb + r + Lb)/h))
        assert abs(xg[i] - (xb - r)) < 1e-9 and abs(xg[j] - (xb + r)) < 1e-9
        Kij = (U[i, :]*np.exp(-t*E))@U[j, :]/h
        logR = log_rho0(xg[i], xg[j], t) - int_avgV_cos(xg[i], xg[j], t)
        ys.append((np.log(Kij) - logR)/t**3)
    c = np.polyfit(taus, ys, 2)
    V1, V2, V3 = -V0*k*np.sin(k*xb), -V0*k**2*np.cos(k*xb), V0*k**3*np.sin(k*xb)
    a_pred = D*V1**2/12
    b_pred = V2**2/180 + V1*V3/60
    b_noDelta = D**2*(V2**2/90 + V1*V3/30)   # what b would be if the Delta terms were absent
    ok = abs(c[2]/a_pred - 1) < 1e-3 and abs(c[1] - b_pred) < 0.05*abs(b_pred)
    print(f"N8 xbar={xb}: a_fit={c[2]:+.6e} a_pred={a_pred:+.6e} | b_fit={c[1]:+.5e} b_pred={b_pred:+.5e}"
          f" (b without Delta terms: {b_noDelta:+.5e}) ->", "PASS" if ok else "FAIL")
