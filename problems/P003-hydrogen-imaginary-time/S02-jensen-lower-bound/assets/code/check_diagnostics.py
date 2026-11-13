# check_diagnostics.py -- P003.S02, follow-up diagnostics to run 1 of check_numeric.py [N].
# Standalone. Python 3.13.18, numpy 2.5.3, scipy 1.18.1. Seeds fixed below.
import numpy as np
from scipy import linalg

print("numpy", np.__version__)


def log_rho0(p, q, t, D):
    return -0.5*np.log(4*np.pi*D*t) - (p - q)**2/(4*D*t)


# D1: size of the run-1 roundoff in N7b at x = x' = 0 (where I = sqrt(pi tau/D) exactly).
D, tau = 0.5, 1.0
gq, wq = np.polynomial.legendre.leggauss(200)
th = 0.25*np.pi*(gq + 1); wth = 0.25*np.pi*wq
I1 = I2 = 0.0
for t_, wt in zip(th, wth):
    u = tau*np.sin(t_)**2
    s1 = np.sqrt(2*D*u*(tau - u)/tau)                       # run-1 formula
    s2 = np.sqrt(2*D*tau*np.sin(t_)**2*np.cos(t_)**2)       # run-2 formula
    I1 += wt*2*tau*np.sin(t_)*np.cos(t_)*np.sqrt(2/np.pi)/s1
    I2 += wt*2*tau*np.sin(t_)*np.cos(t_)*np.sqrt(2/np.pi)/s2
b = np.sqrt(np.pi*tau/D)
print(f"D1 x=x'=0: run-1 I - bound = {I1 - b:+.2e}   run-2 I - bound = {I2 - b:+.2e}")

# D2: where do the NaNs of log(K_dvr) in N5c come from? (negative/zero DVR entries)
h, Lb, D = 0.04, 12.0, 0.5
xg = np.arange(-Lb, Lb + h/2, h); N = len(xg)
idx = np.arange(N); dif = idx[:, None] - idx[None, :]
T = np.where(dif == 0, D*np.pi**2/(3*h**2), 2*D*(-1.0)**dif/(h**2*np.where(dif == 0, 1, dif)**2))
E, U = linalg.eigh(T + np.diag(np.cos(xg)))
cen = np.where(np.abs(xg) <= 4 + 1e-9)[0]
XA, XB = np.meshgrid(xg[cen], xg[cen], indexing="ij")
for t in [0.2, 0.4, 1.0, 2.0, 4.0]:
    K = ((U*np.exp(-t*E))@U.T/h)[np.ix_(cen, cen)]
    near = np.abs(XA - XB) <= 3*np.sqrt(2*D*t)
    bad = K <= 0
    print(f"D2 tau={t}: nonpositive DVR entries inside tested region: {np.sum(bad & near)}, outside: {np.sum(bad & ~near)};"
          f" min |x-x'| among them: {np.min(np.abs(XA-XB)[bad]) if bad.any() else float('nan'):.2f};"
          f" largest |K| among them: {np.max(np.abs(K[bad])) if bad.any() else 0:.1e}")

# D3: N2 repeated with independent seeds and 5x more paths (all runs reported).
def V(y): return np.cos(2.0*y)
def avg_closed(x, xp, u, tau, D):
    m = x + (u/tau)*(xp - x); s2 = 2*D*u*(tau - u)/tau
    return np.cos(2.0*m)*np.exp(-0.5*4.0*s2)
D, tau, x, xp = 0.5, 1.0, 0.3, -0.4
nsteps, npaths = 16, 2_000_000
delta = tau/nsteps
for seed in [20261113, 20261114]:
    rng = np.random.default_rng(seed)
    paths = x + np.cumsum(rng.normal(0.0, np.sqrt(2*D*delta), size=(npaths, nsteps - 1)), axis=1)
    w = np.exp(log_rho0(paths[:, -1], xp, delta, D) - log_rho0(x, xp, tau, D))
    W = w.sum(); zs = []
    for j in range(1, nsteps):
        f = V(paths[:, j - 1]); est = np.sum(w*f)/W
        se = np.sqrt(np.sum(w**2*(f - est)**2))/W
        zs.append((est - avg_closed(x, xp, j*delta, tau, D))/se)
    print(f"D3 seed={seed} paths={npaths}: z =", " ".join(f"{z:+.2f}" for z in zs), f" max|z|={max(map(abs, zs)):.2f}",
          "-> PASS" if max(map(abs, zs)) < 4 else "-> FAIL")
