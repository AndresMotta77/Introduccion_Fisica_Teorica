# check_numeric.py -- P003.S02, numerical checks [N].
# Standalone. Run: python3 check_numeric.py
# Tested with: Python 3.13.18, numpy 2.5.3, scipy 1.18.1. Seed fixed below.
#
# Assumptions restated as [A] in the text: D > 0, tau > 0, kappa > 0; grids,
# windows and tolerances are stated at each check together with the output
# that would count as FAIL.
import numpy as np
import scipy
from scipy import integrate, special, linalg

print("numpy", np.__version__, "scipy", scipy.__version__)
SEED = 20261112
rng = np.random.default_rng(SEED)


# ---------------------------------------------------------------------------
# Building blocks taken from the PROBLEM STATEMENT only
def log_rho0(p, q, t, D, d=1):
    """log of the free kernel, prompt section 3a."""
    r2 = np.sum(np.atleast_1d((np.asarray(p) - np.asarray(q))**2), axis=0) if d > 1 else (p - q)**2
    return -0.5*d*np.log(4*np.pi*D*t) - r2/(4*D*t)


# Claimed closed forms (these are what is under test)
def bridge_mean_var(x, xp, u, tau, D):
    return x + (u/tau)*(xp - x), 2*D*u*(tau - u)/tau          # text eq. (5)


def avgV_closed(kind, x, xp, u, tau, D, par):
    m, s2 = bridge_mean_var(x, xp, u, tau, D)
    if kind == "quad":
        return 0.5*par*(m**2 + s2)
    if kind == "cos":
        V0, k = par
        return V0*np.cos(k*m)*np.exp(-0.5*k**2*s2)
    if kind == "quartic":
        return par*(m**4 + 6*m**2*s2 + 3*s2**2)
    raise ValueError


def Vfun(kind, y, par):
    if kind == "quad":
        return 0.5*par*y**2
    if kind == "cos":
        V0, k = par
        return V0*np.cos(k*y)
    if kind == "quartic":
        return par*y**4


def int_avgV_closed(kind, x, xp, tau, D, par, n=80):
    """int_0^tau <V>_u du by Gauss-Legendre on the closed form (smooth integrand)."""
    g, wts = np.polynomial.legendre.leggauss(n)
    tot = 0.0
    for gi, wi in zip(g, wts):
        tot = tot + wi*avgV_closed(kind, x, xp, 0.5*tau*(gi + 1), tau, D, par)
    return 0.5*tau*tot


def logK_mehler(x, xp, tau, D, kap):
    """Oscillator kernel; independently verified in check_symbolic.py (S6)."""
    om = np.sqrt(2*D*kap)
    Mw = om/(2*D)
    return 0.5*np.log(Mw/(2*np.pi*np.sinh(om*tau))) - Mw*((x**2 + xp**2)*np.cosh(om*tau) - 2*x*xp)/(2*np.sinh(om*tau))


def int_avgV_quad_closed(x, xp, tau, D, kap):
    """Closed form of int_0^tau <V>_u du for V = kap y^2/2 (eq. (12); S5 symbolic)."""
    return kap*tau/6*(x**2 + x*xp + xp**2) + kap*D*tau**2/6


# ===========================================================================
print("\n=== N1  <V>_u: quadrature from the definition vs closed form ===")
# Integrand from the definition: rho0(x,y;u) V(y) rho0(y,x';tau-u)/rho0(x,x';tau).
# Window: [min(x,x') - 14 sqrt(2 D tau) - 1, max(x,x') + same] (chosen from x,x',tau
# only, not from the claimed mean/variance). FAIL if max relative error > 1e-8
# or normalization error > 1e-10.
def avgV_quad(kind, x, xp, u, tau, D, par):
    L = 14*np.sqrt(2*D*tau) + 1
    lo, hi = min(x, xp) - L, max(x, xp) + L
    lr = log_rho0(x, xp, tau, D)
    f = lambda y: np.exp(log_rho0(x, y, u, D) + log_rho0(y, xp, tau - u, D) - lr)
    pts = [x, xp]
    num = integrate.quad(lambda y: f(y)*Vfun(kind, y, par), lo, hi, points=pts, limit=400, epsabs=0, epsrel=1e-13)[0]
    nor = integrate.quad(f, lo, hi, points=pts, limit=400, epsabs=0, epsrel=1e-13)[0]
    return num, nor


for kind, par in [("quad", 1.3), ("cos", (0.8, 2.1)), ("quartic", 0.7)]:
    maxrel, maxnorm = 0.0, 0.0
    n = 150
    for i in range(n):
        D = rng.uniform(0.2, 2.0)
        tau = 10**rng.uniform(-2, np.log10(5))
        frac = [1e-4, 1 - 1e-4, 0.5][i] if i < 3 else rng.uniform(0, 1)
        u = frac*tau
        x, xp = rng.uniform(-3, 3, size=2)
        num, nor = avgV_quad(kind, x, xp, u, tau, D, par)
        cl = avgV_closed(kind, x, xp, u, tau, D, par)
        scale = max(abs(cl), 1e-3*abs(Vfun(kind, 1.0, par)))  # guard vs zeros of cos
        maxrel = max(maxrel, abs(num - cl)/scale)
        maxnorm = max(maxnorm, abs(nor - 1))
    print(f"N1 {kind:8s} draws={n}  max rel err={maxrel:.2e}  max |norm-1|={maxnorm:.2e}  ->",
          "PASS" if (maxrel < 1e-8 and maxnorm < 1e-10) else "FAIL")


# ===========================================================================
print("\n=== N2  weighted free-walk Monte Carlo (definition of the bridge) ===")
# Free walks x_0 = x, increments N(0, 2 D delta); weight = rho0(x_{n-1}, x'; delta).
# Then E_bridge[f(x_j)] = sum w f(x_j) / sum w. This uses only rho0 and the
# definition of the bridge, not eq. (5). FAIL if any |z| > 4.
D, tau, x, xp = 0.5, 1.0, 0.3, -0.4
kind, par = "cos", (1.0, 2.0)
nsteps, npaths = 16, 400_000
delta = tau/nsteps
inc = rng.normal(0.0, np.sqrt(2*D*delta), size=(npaths, nsteps - 1))
paths = x + np.cumsum(inc, axis=1)                      # x_1 .. x_{n-1}
w = np.exp(log_rho0(paths[:, -1], xp, delta, D) - log_rho0(x, xp, tau, D) + 0.0)
W = w.sum()
zs = []
for j in range(1, nsteps):
    f = Vfun(kind, paths[:, j - 1], par)
    est = np.sum(w*f)/W
    se = np.sqrt(np.sum(w**2*(f - est)**2))/W
    cl = avgV_closed(kind, x, xp, j*delta, tau, D, par)
    zs.append((est - cl)/se)
print("N2 z-scores, j=1..15:", " ".join(f"{z:+.2f}" for z in zs))
print("N2 effective sample size:", f"{W**2/np.sum(w**2):.0f}", " max|z| =", f"{max(abs(z) for z in zs):.2f}", "->",
      "PASS" if max(abs(z) for z in zs) < 4 else "FAIL")


# ===========================================================================
print("\n=== N3  finite-m Trotter inequality (T6) on a grid ===")
# K_m(x_a,x_b) = (P^m)_{ab}/h, P_ij = h rho0(x_i,x_j;eps) exp(-eps V(x_j)), eps = tau/m
# (kernel of (e^{-eps K} e^{-eps V})^m by trapezoid quadrature of the bead integrals).
# R_m = rho0(x_a,x_b;tau) exp(-eps sum_{j=1}^m <V>_{j eps}), <V>_tau := V(x_b).
# Region tested: |x_a|,|x_b| <= 3 and |x_a - x_b| <= 2.5.
# Quadrature error estimated by repeating with h/2. FAIL if min log(K_m/R_m) < -10*(h vs h/2 discrepancy).
def trotter_check(kind, par, D, tau, m, h, Lbox=10.0):
    xg = np.arange(-Lbox, Lbox + h/2, h)
    eps = tau/m
    P = h*np.exp(log_rho0(xg[:, None], xg[None, :], eps, D) - eps*Vfun(kind, xg[None, :], par))
    Pm = np.linalg.matrix_power(P, m)
    sel = np.where(np.abs(xg) <= 3 + 1e-9)[0]
    XA, XB = np.meshgrid(xg[sel], xg[sel], indexing="ij")
    Km = Pm[np.ix_(sel, sel)]/h
    S = np.zeros_like(XA)
    for j in range(1, m):
        S += avgV_closed(kind, XA, XB, j*eps, tau, D, par)
    S += Vfun(kind, XB, par)
    logR = log_rho0(XA, XB, tau, D) - eps*S
    return np.log(Km) - logR, XA, XB          # 2D arrays on the |x|<=3 sub-grid


for kind, par in [("cos", (1.0, 2.0)), ("quad", 1.0)]:
    for m in [2, 4, 8, 16]:
        lr1, XA1, XB1 = trotter_check(kind, par, 0.5, 1.0, m, 0.05)
        lr2, XA2, XB2 = trotter_check(kind, par, 0.5, 1.0, m, 0.025)
        assert np.allclose(XA2[::2, ::2], XA1) and np.allclose(XB2[::2, ::2], XB1)
        mask1 = np.abs(XA1 - XB1) <= 2.5
        mask2 = np.abs(XA2 - XB2) <= 2.5
        disc = np.max(np.abs(lr1 - lr2[::2, ::2])[mask1])
        tol = max(10*disc, 1e-12)
        lr = lr2[mask2]
        print(f"N3 {kind:4s} m={m:2d}: min log(K_m/R_m)={lr.min():+.3e}  max={lr.max():.3e}  h-vs-h/2 disc={disc:.1e}  ->",
              "PASS" if lr.min() > -tol else "FAIL")


# ===========================================================================
print("\n=== N4  oscillator: (*) against the exact (Mehler) kernel ===")
# D = 1/2, kappa = 1 (omega = 1). L = log(R/K); (*) says L <= 0.
# FAIL if max L > 1e-12 (rounding allowance) on the grid x,x' in [-3,3]^2 (121x121).
D, kap = 0.5, 1.0
om = np.sqrt(2*D*kap)
xg = np.linspace(-3, 3, 121)
XA, XB = np.meshgrid(xg, xg, indexing="ij")
print(" tau     max L        min L         at x=x'=0: L        large-tau asympt.")
for tau in [0.05, 0.1, 0.2, 0.5, 1.0, 2.0, 5.0, 10.0]:
    logR = log_rho0(XA, XB, tau, D) - int_avgV_quad_closed(XA, XB, tau, D, kap)
    L = logR - logK_mehler(XA, XB, tau, D, kap)
    L00 = (log_rho0(0.0, 0.0, tau, D) - int_avgV_quad_closed(0.0, 0.0, tau, D, kap)) - logK_mehler(0.0, 0.0, tau, D, kap)
    asym = -kap*D*tau**2/6 + om*tau/2 - 0.5*np.log(2*om*tau)
    print(f" {tau:5.2f}  {L.max():+.3e}  {L.min():+.3e}  {L00:+.6e}  {asym:+.6e}  ->", "PASS" if L.max() <= 1e-12 else "FAIL")

print("\nN4b small tau: -L compared with the leading term of part (b), Dk^2 tau^3 xbar^2/12,")
print("    and with leading + next (eq. (30)); points with |x-x'| <= 2 sqrt(2 D tau), |xbar| >= 0.5")
for tau in [0.4, 0.2, 0.1, 0.05, 0.025]:
    logR = log_rho0(XA, XB, tau, D) - int_avgV_quad_closed(XA, XB, tau, D, kap)
    mL = -(logR - logK_mehler(XA, XB, tau, D, kap))
    xb, Dl = 0.5*(XA + XB), XB - XA
    sel = (np.abs(Dl) <= 2*np.sqrt(2*D*tau)) & (np.abs(xb) >= 0.5)
    P1 = kap**2*D*tau**3*xb**2/12
    P2 = P1 + kap**2*D*tau**3*Dl**2/720 + kap**2*D**2*tau**4/90
    r1 = np.max(np.abs(mL[sel]/P1[sel] - 1))
    r2 = np.max(np.abs(mL[sel]/P2[sel] - 1))
    print(f"   tau={tau:5.3f}  npts={sel.sum():5d}  max|(-L)/P1 - 1|={r1:.3e}  max|(-L)/P2 - 1|={r2:.3e}")
print("   at xbar = 1, Delta = 0:  -L/tau^3 ->", ", ".join(
    f"{(-(log_rho0(1.,1.,t,D)-int_avgV_quad_closed(1.,1.,t,D,kap)-logK_mehler(1.,1.,t,D,kap)))/t**3:.6f}" for t in [0.2, 0.1, 0.05, 0.025, 0.0125]),
    f"   prediction D k^2/12 = {kap**2*D/12:.6f}")


# ===========================================================================
print("\n=== N5  cosine potential, exact kernel by sinc-DVR diagonalization ===")
# V = V0 cos(k x), V0 = 1, k = 1, D = 1/2. Grid h = 0.04 on [-12, 12].
# DVR kinetic for -D d^2/dx^2: T_ii = D pi^2/(3h^2), T_ij = 2D(-1)^(i-j)/(h^2 (i-j)^2).
# The DVR is NOT trusted: it is validated first on V = 0 (against rho0) and on the
# oscillator (against Mehler). FAIL criteria: validation errors > 1e-10.
h, Lb, D = 0.04, 12.0, 0.5
xg = np.arange(-Lb, Lb + h/2, h)
N = len(xg)
idx = np.arange(N)
dif = idx[:, None] - idx[None, :]
with np.errstate(divide="ignore"):
    T = np.where(dif == 0, D*np.pi**2/(3*h**2), 2*D*(-1.0)**dif/(h**2*np.where(dif == 0, 1, dif)**2))


def dvr_kernel(Vdiag, taus):
    E, U = linalg.eigh(T + np.diag(Vdiag))
    return {t: (U*np.exp(-t*E))@U.T/h for t in taus}


taus = [0.025, 0.05, 0.1, 0.2, 0.4, 1.0, 2.0, 4.0]
cen = np.where(np.abs(xg) <= 4 + 1e-9)[0]
Kfree = dvr_kernel(np.zeros(N), taus)
Kosc = dvr_kernel(0.5*xg**2, taus)
for t in taus[:6]:
    XA, XB = np.meshgrid(xg[cen], xg[cen], indexing="ij")
    near = np.abs(XA - XB) <= 3*np.sqrt(2*D*t)
    e_free = np.max(np.abs(np.log(Kfree[t][np.ix_(cen, cen)][near]) - log_rho0(XA, XB, t, D)[near]))
    e_osc = np.max(np.abs(np.log(Kosc[t][np.ix_(cen, cen)][near]) - logK_mehler(XA, XB, t, D, 1.0)[near]))
    print(f"N5 validation tau={t:5.3f}: max|log K_dvr - log rho0|={e_free:.1e}   max|log K_dvr - log K_Mehler|={e_osc:.1e}  ->",
          "PASS" if max(e_free, e_osc) < 1e-10 else "FAIL")

V0, k = 1.0, 1.0
Kcos = dvr_kernel(V0*np.cos(k*xg), taus)
print("\nN5b small-tau coefficient at Delta = 0: y(tau) = log(K/R)/tau^3, fit y = a + b tau + c tau^2")
print("    predictions: a = D V'(xbar)^2/12, b = D^2 (V''^2/90 + V' V'''/30)   [eqs. (26), (29)]")
for xb in [0.4, 0.8, 1.2, 1.6, 2.0, 2.8]:
    i = int(round((xb + Lb)/h))
    assert abs(xg[i] - xb) < 1e-9
    ys = []
    small = [0.025, 0.05, 0.1, 0.2, 0.4]
    for t in small:
        logR = log_rho0(xb, xb, t, D) - int_avgV_closed("cos", xb, xb, t, D, (V0, k))
        ys.append((np.log(Kcos[t][i, i]) - logR)/t**3)
    cfit = np.polyfit(small, ys, 2)
    a_pred = D*(V0*k*np.sin(k*xb))**2/12
    b_pred = D**2*((V0*k**2*np.cos(k*xb))**2/90 + (-V0*k*np.sin(k*xb))*(V0*k**3*np.sin(k*xb))/30)
    print(f"   xbar={xb:3.1f}: a_fit={cfit[2]:+.6e} a_pred={a_pred:+.6e} | b_fit={cfit[1]:+.5e} b_pred={b_pred:+.5e} | y(0.025)={ys[0]:+.6e}")

print("\nN5c inequality (*) for the cosine at moderate/large tau; region |x|,|x'|<=4, |x-x'|<=3 sqrt(2 D tau)")
for t in [0.2, 0.4, 1.0, 2.0, 4.0]:
    XA, XB = np.meshgrid(xg[cen], xg[cen], indexing="ij")
    near = np.abs(XA - XB) <= 3*np.sqrt(2*D*t)
    logR = log_rho0(XA, XB, t, D) - int_avgV_closed("cos", XA, XB, t, D, (V0, k))
    L = (logR - np.log(Kcos[t][np.ix_(cen, cen)]))[near]
    print(f"   tau={t:3.1f}: max L = {L.max():+.3e}   min L = {L.min():+.3e}  ->", "PASS" if L.max() <= 1e-10 else "FAIL")


# ===========================================================================
print("\n=== N6  oscillator partition-function approximant Zhat_m ===")
# Circulant evaluation (eq. (37)): Zhat_m = prod_k [2(1-cos th_k) + (2 kap D tau^2/3)(2+cos th_k)]^(-1/2) e^{-m kap D tau^2/6}
# Cross-checked against a grid evaluation Tr(M^m), M_ij = h rho0(x_i,x_j;tau) exp(-int<V>_u du).
# Z = 1/(2 sinh(beta om/2)). Prediction (eq. (35)): m^2 (1 - Zhat_m/Z) -> A = D beta^3 kap^2 <x^2>/12,
# <x^2> = (D/om) coth(beta om/2). FAIL if any Zhat_m > Z, or if the Richardson-extrapolated
# m^2(1 - Zhat/Z) at the largest m differs from A by more than 1e-3 relative.
D, kap = 0.5, 1.0
om = np.sqrt(2*D*kap)


def logZhat_circ(beta, m):
    tau = beta/m
    th = 2*np.pi*np.arange(m)/m
    return -0.5*np.sum(np.log(4*np.sin(th/2)**2 + (2*kap*D*tau**2/3)*(2 + np.cos(th)))) - m*kap*D*tau**2/6


def logZprim_circ(beta, m):
    tau = beta/m
    th = 2*np.pi*np.arange(m)/m
    return -0.5*np.sum(np.log(4*np.sin(th/2)**2 + 2*kap*D*tau**2))


def logZhat_grid(beta, m, h=0.02, Lbox=10.0):
    tau = beta/m
    x_ = np.arange(-Lbox, Lbox + h/2, h)
    XA, XB = np.meshgrid(x_, x_, indexing="ij")
    M = h*np.exp(log_rho0(XA, XB, tau, D) - int_avgV_quad_closed(XA, XB, tau, D, kap))
    mu = np.linalg.eigvalsh(M)
    return np.log(np.sum(mu**m))


for m in [1, 2, 4, 8, 16]:
    a_, b_ = logZhat_circ(4.0, m), logZhat_grid(4.0, m)
    print(f"N6a beta=4 m={m:2d}: log Zhat circulant={a_:+.12f}  grid={b_:+.12f}  diff={a_-b_:+.1e}")

for beta in [1.0, 4.0, 10.0]:
    logZ = -np.log(2*np.sinh(beta*om/2))
    A = D*beta**3*kap**2*(D/om)/np.tanh(beta*om/2)/12
    print(f"\nN6b beta={beta}: Z={np.exp(logZ):.10e}, predicted A = {A:.8f}")
    ms = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048]
    f = {}
    allbelow, primabove = True, True
    for m in ms:
        lz = logZhat_circ(beta, m)
        lp = logZprim_circ(beta, m)
        r = np.exp(lz - logZ)
        f[m] = m**2*(-np.expm1(lz - logZ))
        allbelow &= (lz <= logZ)
        primabove &= (lp >= logZ)
        if m in (1, 2, 4, 8, 64, 512, 2048):
            print(f"   m={m:5d}  Zhat/Z={r:.12f}  m^2(1-Zhat/Z)={f[m]:.8f}  Zprim/Z={np.exp(lp-logZ):.12f}")
    rich = 2*f[2048] - f[1024]
    print(f"   Richardson 2f(2048)-f(1024) = {rich:.8f}   rel. dev. from A = {abs(rich/A-1):.2e}")
    print("   all Zhat_m <= Z:", allbelow, "  all Zprim_m >= Z:", primabove, " ->",
          "PASS" if (allbelow and abs(rich/A - 1) < 1e-3) else "FAIL")


# ===========================================================================
print("\n=== N7  Coulomb: Gaussian average of 1/|y| in d = 3 ===")
# Claim (eq. (44)): for y ~ N(mu, s^2 I_3), <1/|y|> = erf(|mu|/(sqrt2 s))/|mu|, -> sqrt(2/pi)/s at mu = 0.
# Checked against (i) Monte Carlo, (ii) 2D quadrature in (r, cos theta) done numerically.
# FAIL if |z_MC| > 4 or quadrature rel. err > 1e-8.
def inv_r_closed(mu, s):
    return np.sqrt(2/np.pi)/s if mu == 0 else special.erf(mu/(np.sqrt(2)*s))/mu


for mu, s in [(0.0, 0.2), (0.0, 1.0), (0.3, 0.2), (0.3, 1.0), (1.0, 0.5), (3.0, 1.0)]:
    y = rng.normal(0, s, size=(1_000_000, 3)); y[:, 2] += mu
    g = 1/np.linalg.norm(y, axis=1)
    z = (g.mean() - inv_r_closed(mu, s))/(g.std()/np.sqrt(len(g)))
    dens = lambda c, r: 2*np.pi*r*(2*np.pi*s**2)**-1.5*np.exp(-(r**2 + mu**2 - 2*r*mu*c)/(2*s**2))
    q = integrate.dblquad(dens, 0, mu + 15*s, -1, 1, epsabs=0, epsrel=1e-12)[0]
    rel = abs(q/inv_r_closed(mu, s) - 1)
    print(f"N7a mu={mu:3.1f} s={s:3.1f}: closed={inv_r_closed(mu, s):.10f}  quad rel err={rel:.1e}  MC z={z:+.2f}  ->",
          "PASS" if (abs(z) < 4 and rel < 1e-8) else "FAIL")

print("\nN7b  I(x,x') = int_0^tau <1/r>_u du vs bound sqrt(pi tau/D) (eq. (46)); D = 0.5, tau = 1")
D, tau = 0.5, 1.0
gq, wq = np.polynomial.legendre.leggauss(200)
th = 0.25*np.pi*(gq + 1); wth = 0.25*np.pi*wq          # u = tau sin^2(theta), theta in (0, pi/2)
for xv, xpv in [((0, 0, 0), (0, 0, 0)), ((0.3, 0, 0), (0, 0, 0)), ((0.5, 0, 0), (-0.5, 0, 0)), ((1, 1, 0), (1, 0, 1)), ((3, 0, 0), (3, 0, 0))]:
    xv, xpv = np.array(xv, float), np.array(xpv, float)
    tot = 0.0
    for t_, wt in zip(th, wth):
        u = tau*np.sin(t_)**2
        mu = np.linalg.norm(xv + (u/tau)*(xpv - xv))
        s = np.sqrt(2*D*tau*np.sin(t_)**2*np.cos(t_)**2)   # run 2: tau-u written as tau cos^2
        tot += wt*2*tau*np.sin(t_)*np.cos(t_)*inv_r_closed(mu, s)
    print(f"   x={xv}, x'={xpv}:  I={tot:.10f}   bound={np.sqrt(np.pi*tau/D):.10f}   I-bound={tot-np.sqrt(np.pi*tau/D):+.1e}  I<=bound(+1e-12): {tot <= np.sqrt(np.pi*tau/D)+1e-12}")

print("\nN7c  monotone convergence of the truncation, x = x' = 0, D = 0.5, tau = 1:")
print("     int_0^tau <min(1/r, N)>_u du  (radial quadrature) should increase to sqrt(2 pi) =", f"{np.sqrt(2*np.pi):.10f}")
for Ntr in [1, 3, 10, 30, 100, 1000, 10000]:
    tot = 0.0
    for t_, wt in zip(th, wth):
        u = tau*np.sin(t_)**2
        s = np.sqrt(2*D*tau*np.sin(t_)**2*np.cos(t_)**2)   # run 2: tau-u written as tau cos^2
        p = lambda r: 4*np.pi*r**2*(2*np.pi*s**2)**-1.5*np.exp(-r**2/(2*s**2))
        val = integrate.quad(lambda r: min(1/r, Ntr)*p(r) if r > 0 else 0.0, 0, 15*s, points=[min(1/Ntr, 15*s)], limit=200)[0]
        tot += wt*2*tau*np.sin(t_)*np.cos(t_)*val
    print(f"     N={Ntr:6d}: {tot:.10f}")
