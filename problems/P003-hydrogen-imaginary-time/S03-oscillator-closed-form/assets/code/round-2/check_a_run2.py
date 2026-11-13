# check_a.py -- part (a): closed-form w against direct numerical evaluation of its DEFINITION.
# Python 3.13.18, mpmath 1.3.0, numpy 2.5.3 (numpy only for the seeded RNG).
# Run: python3 -I check_a.py
#
# The exponent I(x,x';tau) = int_0^tau du (1/rho0(x,x';tau)) int dy rho0(x,y;u) V(y) rho0(y,x';tau-u)
# is computed by nested tanh-sinh quadrature (mpmath.quad), working only with the integrand
# as written in the problem. The y-range is split at points found numerically from the
# integrand itself (the maximiser of the Gaussian part, located by mp.findroot on its
# numerical derivative, and its numerical curvature), so the quadrature does not import the
# bridge mean/variance derived in the text.
# Failure criterion: relative difference between I_num and I_closed above 1e-12 at any point.
# Discrimination: four wrong candidate closed forms are evaluated against the same I_num.
import numpy as np
import mpmath as mp

mp.mp.dps = 30

def rho0(a, b, t):
    return (2*mp.pi*t)**mp.mpf(-0.5)*mp.exp(-(a - b)**2/(2*t))

def V(z):
    return z**2/2

# REVISION NOTE (run 2). Run 1 (check_a_run1.py, output out_a_run1_FAILED.txt) integrated
# rho0*V*rho0 over y and divided by rho0(x,x';tau) afterwards. At the 5 points with large
# (x-x')^2/tau the integrand is ~exp(-(x-x')^2/(2 tau)) (e.g. e^-8000), mpmath's tanh-sinh
# stopping test is absolute, so it stopped at low degree (its own error estimate was 5.8e-4
# relative) and I_num came out low by 3.5e-8 relative. The fix moves the constant factor
# 1/rho0(x,x';tau) inside the y-integral (an identity), so the integrand is O(1), and records
# mpmath's own error estimates so a non-converged quadrature is visible.
MAXERR = [mp.mpf(0)]

def inner(x, xp, tau, u):
    """(1/rho0(x,xp;tau)) int dy rho0(x,y;u) V(y) rho0(y,xp;tau-u), by quadrature."""
    g = lambda yy: -(yy - x)**2/(2*u) - (yy - xp)**2/(2*(tau - u))   # log of Gaussian part
    dg = lambda yy: mp.diff(g, yy)
    # numerical maximiser: secant iteration on the numerical derivative (verify=False because
    # for tiny u the derivative is O(1/u) and the absolute residual test is meaningless)
    ystar = mp.findroot(dg, (x, xp + mp.mpf('1e-3')), solver='secant', verify=False)
    curv = -mp.diff(g, ystar, 2)                                       # numerical curvature
    s = 1/mp.sqrt(curv)
    pts = [-mp.inf] + [ystar + k*s for k in (-40, -12, -5, -2, 0, 2, 5, 12, 40)] + [mp.inf]
    r = rho0(x, xp, tau)
    f = lambda yy: rho0(x, yy, u)*V(yy)*rho0(yy, xp, tau - u)/r
    val, err = mp.quad(f, pts, error=True)
    MAXERR[0] = max(MAXERR[0], abs(err)/max(abs(val), mp.mpf('1e-300')))
    return val

def I_num(x, xp, tau):
    x, xp, tau = mp.mpf(x), mp.mpf(xp), mp.mpf(tau)
    MAXERR[0] = mp.mpf(0)
    val, err = mp.quad(lambda uu: inner(x, xp, tau, uu), [0, tau/4, tau/2, 3*tau/4, tau], error=True)
    return val, abs(err)/abs(val), MAXERR[0]

def I_closed(x, xp, tau):
    return tau*(x**2 + x*xp + xp**2)/6 + tau**2/12

wrong = {
    "prim  tau(x^2+x'^2)/4       ": lambda x, xp, t: t*(x**2 + xp**2)/4,
    "no tau^2/12 term            ": lambda x, xp, t: t*(x**2 + x*xp + xp**2)/6,
    "cross-term coeff doubled    ": lambda x, xp, t: t*(x**2 + 2*x*xp + xp**2)/6 + t**2/12,
    "tau^2/6 instead of tau^2/12 ": lambda x, xp, t: t*(x**2 + x*xp + xp**2)/6 + t**2/6,
}

rng = np.random.default_rng(20261112)
pts = []
for _ in range(8):
    x0, x1 = rng.uniform(-3, 3, size=2)
    t0 = 10**rng.uniform(-2, 1)
    pts.append((float(x0), float(x1), float(t0)))
# boundary / special points
pts += [(0.0, 0.0, 1.0), (2.0, -2.0, 1e-3), (1.5, 1.5, 20.0), (-4.0, 3.0, 5.0), (0.7, -0.7, 2.449489742783178)]

TOL = mp.mpf('1e-12')
nfail = 0
worst = {k: mp.mpf(0) for k in wrong}
print(f"{'x':>9} {'xp':>9} {'tau':>11} {'I_num':>22} {'I_closed':>22} {'relerr':>10} "
      f"{'w relerr':>10} {'quad_u':>8} {'quad_y':>8}")
for (a, b, t) in pts:
    In, eu, ey = I_num(a, b, t)
    Ic = I_closed(mp.mpf(a), mp.mpf(b), mp.mpf(t))
    rel = abs(In - Ic)/abs(Ic)
    wrel = abs(mp.exp(Ic - In) - 1)        # relative error of w = rho0*exp(-I)
    ok = (rel < TOL) and mp.isfinite(In) and eu < TOL and ey < TOL
    nfail += (not ok)
    print(f"{a:9.4f} {b:9.4f} {t:11.6g} {mp.nstr(In, 18):>22} {mp.nstr(Ic, 18):>22} "
          f"{mp.nstr(rel, 3):>10} {mp.nstr(wrel, 3):>10} {mp.nstr(eu, 2):>8} {mp.nstr(ey, 2):>8} "
          f"{'ok' if ok else 'FAIL'}")
    for k, fw in wrong.items():
        worst[k] = max(worst[k], abs(In - fw(mp.mpf(a), mp.mpf(b), mp.mpf(t)))/abs(In))
print("points tested:", len(pts), " failures:", nfail)
print("max relative discrepancy of WRONG candidates against the same numerics:")
for k in wrong:
    print("   ", k, mp.nstr(worst[k], 4))
