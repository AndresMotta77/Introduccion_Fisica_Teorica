"""
pc3_oscillator_levels.py  (PI check, not a solver artifact)

Prepared for the auditor's [FOCUS] block of P003.S03 (chunk K5). Must not be attached to
a solver prompt.

Object. One-dimensional oscillator, hbar = M = omega = 1, V(x) = x^2/2, free kernel
rho0(x, x'; t) = (2 pi t)^(-1/2) exp(-(x - x')^2 / (2 t)) (D = 1/2). The bridge-averaged
slice weight is
    w(x, x'; tau) = rho0(x, x'; tau) exp(-I(x, x')),
    I(x, x') = int_0^tau du int dy rho0(x, y; u) V(y) rho0(y, x'; tau - u) / rho0(x, x'; tau).
Its integral operator T has eigenvalues lambda_n(tau); E_n(tau) = -ln(lambda_n)/tau.

Routes.
  A  closed form. By hand: I = tau (x^2 + x x' + x'^2)/6 + tau^2/12, so w is a Gaussian
     kernel C exp(-(a/2)(x^2 + x'^2) + b x x') with a = 1/tau + tau/3, b = 1/tau - tau/6,
     C = (2 pi tau)^(-1/2) exp(-tau^2/12). Matching to the Mehler kernel of frequency
     Omega at time t (theta = Omega t): cosh(theta) = a/b, Omega = sqrt(a^2 - b^2),
     lambda_n = C sqrt(2 pi sinh(theta)/Omega) exp(-theta (n + 1/2)).
  B  numerical, from the definition. I(x, x') by Gauss-Legendre in u and the trapezium
     rule in y with the free kernels themselves (the Gaussian form of the bridge is not
     used), then Nystrom diagonalisation of h * W on a uniform x grid. Shares nothing with
     A except V and rho0.
  C  the trace Zhat_m = sum_n lambda_n^m = lambda_0^m / (1 - e^(-m theta)), its energy
     -d ln Zhat_m / d beta at tau = beta/m by a numerical derivative, compared with pc1's
     route B formula for Ehat_m (the DFT re-derivation of eq. (19)).
  S  sympy series in tau of E_n(tau) for route A and for the symmetric primitive kernel
     exp(-tau V(x)/2) rho0 exp(-tau V(x')/2).

Failure would be: |lambda_A - lambda_B| / lambda_A > 1e-8 for n <= 4 (tolerance set by the
y-grid; stated before running), or |route C - pc1 route B| > 1e-10 at the Table I points.

numpy 2.5.3, scipy 1.18.1, sympy 1.14.0, mpmath 1.3.0. No random numbers.
"""
import numpy as np
from numpy.polynomial.legendre import leggauss
import sympy as sp
from mpmath import mp, mpf, cos as mcos, pi as mpi, sqrt as msqrt, sinh as msinh, acosh as macosh, exp as mexp, log as mlog, diff as mdiff

def rho0(x, y, t):
    return np.exp(-(x - y) ** 2 / (2 * t)) / np.sqrt(2 * np.pi * t)

def lam_closed(tau, n):
    a = 1 / tau + tau / 3
    b = 1 / tau - tau / 6
    C = np.exp(-tau ** 2 / 12) / np.sqrt(2 * np.pi * tau)
    th = np.arccosh(a / b)
    Om = np.sqrt(a * a - b * b)
    return C * np.sqrt(2 * np.pi * np.sinh(th) / Om) * np.exp(-th * (n + 0.5))

def lam_numeric(tau, L=8.0, N=401, hy=0.004, nu=48):
    x = np.linspace(-L, L, N)
    h = x[1] - x[0]
    y = np.arange(-L - 2, L + 2 + hy / 2, hy)
    Vy = 0.5 * y ** 2
    g, wg = leggauss(nu)
    u = 0.5 * tau * (g + 1)
    wu = 0.5 * tau * wg
    num = np.zeros((N, N))
    for uk, wk in zip(u, wu):
        R1 = rho0(x[:, None], y[None, :], uk)
        R2 = rho0(y[:, None], x[None, :], tau - uk)
        num += wk * (R1 * (Vy * hy)[None, :]) @ R2
    R0 = rho0(x[:, None], x[None, :], tau)
    # run 1 divided 0 by 0 where R0 underflows (|x - x'| large at tau = 0.1) and the
    # eigensolver received NaNs. Where R0 underflows the weight is set to 0; this changes
    # the check, not the derivation (recorded in the coverage note).
    ok = R0 > 1e-280
    I = np.where(ok, num / np.where(ok, R0, 1.0), 0.0)
    W = np.where(ok, R0 * np.exp(-I), 0.0)
    ev = np.linalg.eigvalsh(h * 0.5 * (W + W.T))[::-1]
    return ev, I, x

print("Route A vs route B: eigenvalues of the slice operator")
fails = 0
for tau in (0.5, 0.25, 0.1):
    evB, I, x = lam_numeric(tau)
    # spot check of I against the hand formula at a few grid points (diagnostic only)
    idx = [(200, 200), (150, 260), (100, 300)]
    for i, j in idx:
        hand = tau * (x[i] ** 2 + x[i] * x[j] + x[j] ** 2) / 6 + tau ** 2 / 12
        print(f"  tau={tau:<5} I({x[i]:+.2f},{x[j]:+.2f}) numeric={I[i, j]:.12f} hand={hand:.12f} diff={I[i, j] - hand:+.2e}")
    for n in range(5):
        la = lam_closed(tau, n)
        rel = abs(la - evB[n]) / la
        ok = rel < 1e-8
        fails += (not ok)
        print(f"  tau={tau:<5} n={n}  lambda_A={la:.12f}  lambda_B={evB[n]:.12f}  rel={rel:.2e}  {'ok' if ok else 'FAIL'}"
              f"  E_n(tau)={-np.log(la) / tau:.10f}  exact={n + 0.5}")
print(f"route A vs B failures: {fails}")

print()
print("Route C: Zhat_m from the spectrum vs pc1 route B (re-derived eq. (19))")
mp.dps = 40
def lnZ_spec(beta, m):
    tau = beta / m
    a = 1 / tau + tau / 3
    b = 1 / tau - tau / 6
    C = mexp(-tau ** 2 / 12) / msqrt(2 * mpi * tau)
    # run 2 crashed at beta = 5, m = 1: for tau > sqrt(6), b < 0 and acosh(a/b) is
    # complex. With b < 0 the kernel is the Mehler kernel with x' -> -x', so the
    # eigenvalues are lambda_0 (sgn(b) e^(-theta))^n with cosh(theta) = a/|b|. This extends
    # route A to b < 0; it does not alter the b > 0 case.
    sg = 1 if b > 0 else -1
    th = macosh(a / abs(b))
    Om = msqrt(a * a - b * b)
    lam0 = C * msqrt(2 * mpi * msinh(th) / Om) * mexp(-th / 2)
    return m * mlog(lam0) - mlog(1 - sg ** m * mexp(-m * th))
def Ehat_pc1(b, m):
    s = sum((2 + mcos(2 * mpi * n / m)) / (1 - mcos(2 * mpi * n / m) + b ** 2 * (2 + mcos(2 * mpi * n / m)) / (6 * m ** 2)) for n in range(m))
    return b / (6 * m) * (1 + s / m)
failsC = 0
for b in (mpf(1), mpf(5), mpf(10)):
    for m in (1, 10, 50, 100, 500):
        eC = -mdiff(lambda bb: lnZ_spec(bb, m), b)
        eB = Ehat_pc1(b, m)
        d = abs(eC - eB)
        failsC += d > mpf("1e-10")
        print(f"  beta={float(b):<4} m={m:<4} E_spec={float(eC):.10f}  E_pc1B={float(eB):.10f}  |diff|={float(d):.1e}")
print(f"route C failures: {failsC}")

print()
print("tau = sqrt(6): b = 0, the kernel factorises and T has rank one; for tau > sqrt(6) the odd-n eigenvalues are negative.")
print("Series in tau (sympy), n symbolic")
t, n = sp.symbols("tau n", positive=True)
# Run 3 was stopped by hand after 10 minutes inside sp.series(acosh(a/b)); its output was
# lost to pipe buffering. The series is now taken through s = sinh(theta/2), using
# cosh(theta) = 1 + 2 s^2 and sinh(theta) = 2 s sqrt(1 + s^2); same quantity, faster.
def series_E(a, b, C, order=6):
    c = sp.series(a / b, t, 0, order + 2).removeO()
    s2 = sp.expand((c - 1) / 2)                      # = sinh^2(theta/2)
    f = sp.series(sp.expand(s2 * 4 / t ** 2), t, 0, order).removeO()   # s = (tau/2) sqrt(f)
    s = sp.series((t / 2) * sp.sqrt(f), t, 0, order + 1).removeO()
    th = sp.series(2 * sp.asinh(s), t, 0, order + 1).removeO()
    sh = sp.series(2 * s * sp.sqrt(1 + s ** 2), t, 0, order + 1).removeO()
    Om = sp.series(sp.sqrt(sp.expand(a ** 2 - b ** 2)), t, 0, order + 1).removeO()
    lnlam = sp.log(C) + sp.Rational(1, 2) * sp.log(2 * sp.pi) \
        + sp.Rational(1, 2) * sp.series(sp.log(sh / Om), t, 0, order + 1).removeO() \
        - th * (n + sp.Rational(1, 2))
    return sp.expand(sp.series(sp.expand(-lnlam / t), t, 0, 5).removeO())
Ej = series_E(1 / t + t / 3, 1 / t - t / 6, sp.exp(-t ** 2 / 12) / sp.sqrt(2 * sp.pi * t))
Ep = series_E(1 / t + t / 2, 1 / t, 1 / sp.sqrt(2 * sp.pi * t))
print("  bridge-averaged:  E_n(tau) =", sp.collect(Ej, t))
print("  primitive (sym):  E_n(tau) =", sp.collect(Ep, t))
# numerical cross-check of the series against route A at tau = 0.1 (n = 0, 3)
for nn in (0, 3):
    ser = float(Ej.subs({n: nn, t: sp.Rational(1, 10)}))
    print(f"  series vs route A at tau = 0.1, n = {nn}: {ser:.10f} vs {-np.log(lam_closed(0.1, nn)) / 0.1:.10f}")
