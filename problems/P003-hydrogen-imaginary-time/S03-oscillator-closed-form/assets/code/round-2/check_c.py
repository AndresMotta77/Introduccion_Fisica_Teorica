# check_c.py -- part (c): eigenvalues of T_tau (bridge kernel w) and of the symmetric
# primitive kernel exp(-tau V/2) exp(-tau K) exp(-tau V/2), checked against
#   C1  Nystrom (trapezoid) diagonalisation of the kernel on a uniform grid, two grid sizes;
#   C2  reconstruction of the kernel from the claimed spectrum via Mehler's formula
#       (DLMF 18.18.28), an independent identity;
#   C3  Hilbert-Schmidt norm: grid value of int int w^2 against sum_n lambda_n^2
#       (tests that no eigenvalue is missing, without invoking completeness);
#   C4  the (b)-(c) relation: Tr (h W)^m on the grid against the closed form of Zhat_m from (b);
#   C5  small-tau coefficients of E_n - (n+1/2) extracted from GRID eigenvalues;
#   C6  variational bound E_0(tau) >= 1/2 for the bridge kernel (Jensen + Perron argument).
# Python 3.13.18, numpy 2.5.3, scipy 1.18.1, mpmath 1.3.0. Deterministic (seeded RNG).
# Run: python3 -I check_c.py
#
# The kernels are evaluated from the closed form of (a), which is checked independently
# against its definition in check_a.py. Closed forms of (c) are typed in here from the text.
import numpy as np
import mpmath as mp
from scipy.special import eval_hermite

def rho0(a, b, t):
    return np.exp(-(a - b)**2/(2*t))/np.sqrt(2*np.pi*t)

def w_bridge(a, b, t):                   # eq. (a) of the text
    return rho0(a, b, t)*np.exp(-t*(a*a + a*b + b*b)/6 - t*t/12)

def w_prim(a, b, t):                     # kernel of e^{-tV/2} e^{-tK} e^{-tV/2}
    return np.exp(-t*a*a/4)*rho0(a, b, t)*np.exp(-t*b*b/4)

# ----- closed forms of (c), as stated in the text -----
def spec_bridge(t, nmax):
    k = np.sqrt(1 + t*t/12)
    a, b = k + t/2, k - t/2
    lam = np.array([np.exp(-t*t/12)*b**n/a**(n + 1) for n in range(nmax)])
    return lam, k, b/a, np.exp(-t*t/12)/a

def spec_prim(t, nmax):
    k = np.sqrt(1 + t*t/4)
    a, b = k + t/2, k - t/2
    lam = np.array([b**n/a**(n + 1) for n in range(nmax)])
    return lam, k, b/a, 1/a

def grid_eigs(kern, t, L, h):
    xs = np.arange(-L, L + h/2, h)
    X, Y = np.meshgrid(xs, xs, indexing='ij')
    M = h*kern(X, Y, t)
    ev = np.linalg.eigvalsh(M)
    ev = ev[np.argsort(-np.abs(ev))]
    return ev, M, xs

NMAX = 8
TOL = 1e-10                    # absolute, in units of lambda_0
taus = [0.05, 0.2, 0.5, 1.0, 2.0, np.sqrt(6.0), 3.0, 5.0, 10.0]
nfail = 0
print("C1 grid diagonalisation: max_n |lam_grid - lam_closed|/lam_0 over n < 8 "
      "(h and h/2), sign pattern of grid eigenvalues")
for name, kern, spec in (("bridge", w_bridge, spec_bridge), ("prim  ", w_prim, spec_prim)):
    for t in taus:
        lam, k, q, l0 = spec(t, NMAX)
        A = 1/t + (t/3 if name == "bridge" else t/2)
        h = min(0.1, np.sqrt(t)/4, 1/(4*np.sqrt(A)))
        L = 12.0
        ev1, _, _ = grid_eigs(kern, t, L, h)
        ev2, _, _ = grid_eigs(kern, t, L, h/2)
        e1 = np.max(np.abs(ev1[:NMAX] - lam))/lam[0]
        e2 = np.max(np.abs(ev2[:NMAX] - lam))/lam[0]
        signs = ''.join('+' if s > 0 else '-' for s in ev2[:NMAX])
        ok = (e1 < TOL) and (e2 < TOL) and np.all(np.isfinite(ev2[:NMAX]))
        nfail += (not ok)
        print(f"  {name} tau={t:8.5f} q={q:+.6f} N={len(ev2):5d} err(h)={e1:.2e} err(h/2)={e2:.2e} "
              f"grid signs {signs}  {'ok' if ok else 'FAIL'}")
# tau = sqrt(6): rank one
ev, _, _ = grid_eigs(w_bridge, np.sqrt(6.0), 12.0, 0.05)
print(f"  bridge tau=sqrt6: |lam_1/lam_0| on grid = {abs(ev[1]/ev[0]):.2e} (closed form: 0)")
nfail += not (abs(ev[1]/ev[0]) < TOL)

# ----- C2: Mehler reconstruction -----
# DLMF 18.18.28: sum_n H_n(X)H_n(Y) z^n/(2^n n!) = (1-z^2)^{-1/2} exp((2XYz-(X^2+Y^2)z^2)/(1-z^2)), |z|<1.
# Claimed: kernel = sum_n lam_0 q^n phi_n(x)phi_n(x')/||phi_n||^2, phi_n = H_n(sqrt(k) x) e^{-k x^2/2},
# ||phi_n||^2 = 2^n n! sqrt(pi)/sqrt(k).  Then kernel = lam_0 sqrt(k/pi) e^{-k(x^2+x'^2)/2} * Mehler(X,Y,q).
print("C2 Mehler reconstruction of the kernel from the claimed spectrum (max relative error)")
rng = np.random.default_rng(7)
for name, kern, spec in (("bridge", w_bridge, spec_bridge), ("prim  ", w_prim, spec_prim)):
    for t in taus:
        lam, k, q, l0 = spec(t, 1)
        xs = rng.uniform(-3, 3, size=(20, 2))
        worst = 0.0
        for (a, b) in xs:
            X, Y = np.sqrt(k)*a, np.sqrt(k)*b
            mehler = (1 - q*q)**-0.5*np.exp((2*X*Y*q - (X*X + Y*Y)*q*q)/(1 - q*q))
            rec = l0*np.sqrt(k/np.pi)*np.exp(-k*(a*a + b*b)/2)*mehler
            worst = max(worst, abs(rec/kern(a, b, t) - 1))
        ok = worst < 1e-12
        nfail += (not ok)
        print(f"  {name} tau={t:8.5f}: {worst:.2e} {'ok' if ok else 'FAIL'}")
# and a truncated-series version (explicit Hermite functions), one case with q<0
t = 5.0
lam, k, q, l0 = spec_bridge(t, 60)
a, b = 0.37, -1.21
s = sum(lam[n]*eval_hermite(n, np.sqrt(k)*a)*eval_hermite(n, np.sqrt(k)*b)
        *np.exp(-k*(a*a + b*b)/2)/(2.0**n*mp.factorial(n)*np.sqrt(np.pi)/np.sqrt(k)) for n in range(60))
print(f"  explicit 60-term spectral sum, bridge tau=5 (q<0): rel. err = {abs(float(s)/w_bridge(a, b, t) - 1):.2e}")

# ----- C3: Hilbert-Schmidt norm -----
print("C3 Hilbert-Schmidt norm: grid int int kernel^2 vs sum_n lam_n^2 = lam_0^2/(1-q^2)")
for name, kern, spec in (("bridge", w_bridge, spec_bridge), ("prim  ", w_prim, spec_prim)):
    for t in (0.2, 1.0, 3.0, 10.0):
        lam, k, q, l0 = spec(t, 1)
        A = 1/t + (t/3 if name == "bridge" else t/2)
        h = min(0.05, np.sqrt(t)/6, 1/(6*np.sqrt(A)))
        xs = np.arange(-12, 12 + h/2, h)
        X, Y = np.meshgrid(xs, xs, indexing='ij')
        hs_grid = h*h*np.sum(kern(X, Y, t)**2)
        hs_closed = l0**2/(1 - q*q)
        rel = abs(hs_grid/hs_closed - 1)
        ok = rel < 1e-10
        nfail += (not ok)
        print(f"  {name} tau={t:5.2f}: grid {hs_grid:.15e} closed {hs_closed:.15e} rel {rel:.1e} "
              f"{'ok' if ok else 'FAIL'}")

# ----- C4: (b)-(c) relation via grid traces -----
def Zhat_closed(beta, m):                 # closed form of (b), typed from the text
    t = beta/m
    k = np.sqrt(1 + t*t/12)
    return np.exp(-beta*t/12)/((k + t/2)**m - (k - t/2)**m)

def Z_closed(beta, m):
    t = beta/m
    return 1/(2*np.sinh(m*np.arcsinh(t/2)))

print("C4 Tr (hW)^m on the grid vs closed forms of (b)")
for (beta, m) in [(1, 1), (1, 2), (1, 5), (5, 10), (10, 10), (10, 1), (10, 3), (10, 4), (5, 2)]:
    t = beta/m
    for name, kern, Zc in (("bridge", w_bridge, Zhat_closed), ("prim  ", w_prim, Z_closed)):
        A = 1/t + (t/3 if name == "bridge" else t/2)
        h = min(0.05, np.sqrt(t)/6, 1/(6*np.sqrt(A)))
        ev, M, xs = grid_eigs(kern, t, 12.0, h)
        tr = np.trace(np.linalg.matrix_power(M, m))
        rel = abs(tr/Zc(beta, m) - 1)
        ok = rel < 1e-9
        nfail += (not ok)
        print(f"  {name} beta={beta:2d} m={m:2d} tau={t:6.3f}: Tr={tr:.12e} closed={Zc(beta, m):.12e} "
              f"rel={rel:.1e} {'ok' if ok else 'FAIL'}")

# ----- C5: small-tau coefficients from GRID eigenvalues -----
# REVISION NOTE (run 2): in run 1 (out_c_run1_C5FAILED.txt) the predictions stopped at
# O(tau^3) in R_n and O(tau^2) in P_n, and the primitive case failed the 5e-6 tolerance at
# tau=0.4, n=2,3 (d = 7.4e-6, 1.0e-5), the omitted remainder scaling as tau^4 (1.0e-5 -> 6.6e-7
# -> 4.3e-8). I changed the CHECK, not the derivation: the next two analytic series terms of
# the closed form (sympy, see check_algebra-style series) were added to the predictions; the
# tolerance was kept at 5e-6. The leading coefficients under test are unchanged.
print("C5 from grid eigenvalues: R_n = [E_n-(n+1/2) - (2n+1)tau^2/48]/tau^3 (bridge, predicted "
      "-1/144 + 3(2n+1)tau/1280 - tau^2/1296 + 103(2n+1)tau^3/387072 - tau^4/10368 + 187(2n+1)tau^5/5308416 + O(tau^6));")
print("   P_n = [E_n-(n+1/2) + (2n+1)tau^2/48]/tau^4 (primitive, predicted 3(2n+1)/1280 - 5(2n+1)tau^2/14336 + 35(2n+1)tau^4/589824 + O(tau^6))")
print("   failure if |R_n - pred| or |P_n - pred| > 5e-6 at any tau <= 0.4, n <= 3")
for t in (0.4, 0.2, 0.1, 0.05):
    h = min(0.05, np.sqrt(t)/5)
    evb, _, _ = grid_eigs(w_bridge, t, 10.0, h)
    evp, _, _ = grid_eigs(w_prim, t, 10.0, h)
    rowb, rowp = [], []
    for nn in range(4):
        En = -np.log(evb[nn])/t
        R = (En - (nn + 0.5) - (2*nn + 1)*t*t/48)/t**3
        pred = (-1/144 + 3*(2*nn + 1)*t/1280 - t*t/1296 + 103*(2*nn + 1)*t**3/387072
                - t**4/10368 + 187*(2*nn + 1)*t**5/5308416)
        rowb.append(f"n={nn}: R={R:+.7f} d={R - pred:+.1e}")
        EnP = -np.log(evp[nn])/t
        P = (EnP - (nn + 0.5) + (2*nn + 1)*t*t/48)/t**4
        predP = 3*(2*nn + 1)/1280 - 5*(2*nn + 1)*t*t/14336 + 35*(2*nn + 1)*t**4/589824
        rowp.append(f"n={nn}: P={P:.7f} d={P - predP:+.1e}")
        bad = (abs(R - pred) > 5e-6) or (abs(P - predP) > 5e-6) or not np.isfinite(R + P)
        nfail += bad
    print(f"  tau={t:4.2f} bridge  " + "  ".join(rowb))
    print(f"  tau={t:4.2f} prim    " + "  ".join(rowp))

# ----- C6: E_0(tau) >= 1/2 -----
tt = np.concatenate([np.logspace(-3, 1.5, 400)])
k = np.sqrt(1 + tt*tt/12)
E0 = tt/12 + np.log(k + tt/2)/tt
viol = np.sum(E0 < 0.5 - 1e-15)
print(f"C6 E_0^bridge(tau) >= 1/2 on 400 log-spaced tau in [1e-3, 31.6]: violations = {viol}; "
      f"min(E_0 - 1/2) = {np.min(E0 - 0.5):.3e} at tau = {tt[np.argmin(E0 - 0.5)]:.3e}")
nfail += viol > 0
print("TOTAL FAILURES:", nfail)
