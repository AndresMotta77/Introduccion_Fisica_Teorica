# check_algebra.py -- symbolic checks for P003.S03
# Python 3.13.18, sympy 1.14.0, mpmath 1.3.0. Deterministic (no random numbers).
# Run: python3 -I check_algebra.py
#
# S1  recomputes the bridge integral from the DEFINITION with sympy's own integrator
#     (no completing-the-square supplied by hand), under the assumption 0 < u < tau.
# S2  checks the hand completion of the square (algebra only).
# S3  builds the m x m Hessian of the closed-ring action from w (eq. a) for m = 1..7,
#     symbolically, and compares det(tau*A) with the closed form D_m^2.
# S4  same for the primitive product rho0 * exp(-tau V(x_n)).
# S5  identities c = (kappa+tau/2)^2, q = (kappa-tau/2)/(kappa+tau/2) from A, B.
# S6  small-tau series of E_n(tau), n symbolic, both kernels.
import sympy as sp

x, xp, y = sp.symbols('x xp y', real=True)
u, tau = sp.symbols('u tau', positive=True)
n = sp.symbols('n', nonnegative=True, integer=True)

def rho0(a, b, t):
    return (2*sp.pi*t)**sp.Rational(-1, 2)*sp.exp(-(a - b)**2/(2*t))

V = lambda z: z**2/2

# ---------- S1: y- and u-integrals from the definition ----------
# Assumption [A1]: 0 < u < tau (encoded as v = tau - u > 0).
v = sp.symbols('v', positive=True)
integrand_y = rho0(x, y, u)*V(y)*rho0(y, xp, v)/rho0(x, xp, u + v)
Iy = sp.integrate(sp.expand(integrand_y), (y, -sp.oo, sp.oo), conds='none')
Iy = sp.simplify(Iy)
Iy_tau = sp.simplify(Iy.subs(v, tau - u))
print("S1 inner y-integral (sympy):", sp.factor(Iy_tau))
Iu = sp.integrate(sp.expand(Iy_tau), (u, 0, tau))
Iu = sp.simplify(Iu)
claimed = tau*(x**2 + x*xp + xp**2)/6 + tau**2/12
print("S1 u-integral (sympy):", sp.expand(Iu))
print("S1 claimed           :", sp.expand(claimed))
print("S1 difference simplifies to:", sp.simplify(Iu - claimed))

# ---------- S2: hand completion of the square ----------
ybar = ((tau - u)*x + u*xp)/tau
sig2 = u*(tau - u)/tau
lhs = sp.log(rho0(x, y, u)*rho0(y, xp, tau - u)/rho0(x, xp, tau))
rhs = sp.log((2*sp.pi*sig2)**sp.Rational(-1, 2)*sp.exp(-(y - ybar)**2/(2*sig2)))
print("S2 log(bridge ratio) - log(Gaussian(ybar, sig2)) =",
      sp.simplify(sp.expand_log(lhs - rhs, force=True)))

# ---------- S3/S4: Hessians of closed-ring actions ----------
kap = sp.sqrt(1 + tau**2/12)
kapP = sp.sqrt(1 + tau**2/4)

def w_closed(a, b, t):
    return rho0(a, b, t)*sp.exp(-t*(a**2 + a*b + b**2)/6 - t**2/12)

def bond_prim(a, b, t):
    return rho0(a, b, t)*sp.exp(-t*V(a))

def D_closed(k, t, m):
    return (k + t/2)**m - (k - t/2)**m

for label, bond, k in (("S3 bridge   ", w_closed, kap), ("S4 primitive", bond_prim, kapP)):
    for m in range(1, 8):
        xs = sp.symbols('x1:%d' % (m + 1), real=True)
        S = 0
        for i in range(m):
            S += -sp.expand_log(sp.log(bond(xs[i], xs[(i + 1) % m], tau)), force=True)
        H = sp.hessian(S, xs)
        det_tauA = sp.expand((tau*H).det())
        Dm2 = sp.expand(D_closed(k, tau, m)**2)
        diff = sp.simplify(det_tauA - Dm2)
        print(f"{label} m={m}: det(tau*A) - D_m^2 = {diff}")

# ---------- S5: kernel parameters -> c, q ----------
A = 1/tau + tau/3
B = 1/tau - tau/6
kk = sp.sqrt(A**2 - B**2)
print("S5 kappa^2 - (1+tau^2/12) =", sp.simplify(kk**2 - (1 + tau**2/12)))
c_expr = tau*(A + kap)
print("S5 tau(A+kappa) - (kappa+tau/2)^2 =", sp.simplify(sp.expand(c_expr - (kap + tau/2)**2)))
q_expr = B/(A + kap)
print("S5 B/(A+kappa) - (kappa-tau/2)/(kappa+tau/2) =",
      sp.simplify(q_expr - (kap - tau/2)/(kap + tau/2)))
AP = 1/tau + tau/2
BP = 1/tau
print("S5 primitive: AP^2-BP^2 - (1+tau^2/4) =", sp.simplify(AP**2 - BP**2 - (1 + tau**2/4)))
print("S5 primitive: tau(AP+kapP) - (kapP+tau/2)^2 =",
      sp.simplify(sp.expand(tau*(AP + kapP) - (kapP + tau/2)**2)))
print("S5 primitive: BP/(AP+kapP) - (kapP-tau/2)/(kapP+tau/2) =",
      sp.simplify(BP/(AP + kapP) - (kapP - tau/2)/(kapP + tau/2)))

# ---------- S6: small-tau series ----------
En_b = tau/12 + sp.log(kap + tau/2)/tau + n/tau*sp.log((kap + tau/2)/(kap - tau/2))
En_p = -(sp.log(1/(kapP + tau/2)) + n*sp.log((kapP - tau/2)/(kapP + tau/2)))/tau
sb = sp.series(En_b - (n + sp.Rational(1, 2)), tau, 0, 7).removeO()
sp_ = sp.series(En_p - (n + sp.Rational(1, 2)), tau, 0, 7).removeO()
print("S6 bridge   E_n-(n+1/2) =", sp.collect(sp.expand(sb), tau, sp.factor))
print("S6 primitive E_n-(n+1/2) =", sp.collect(sp.expand(sp_), tau, sp.factor))
# alternative closed form of the bridge levels: (n+1/2)*Omega + tau/12 + log(1-tau^2/6)/(2 tau)
Om = 2/tau*sp.atanh(tau/(2*kap))
alt = (n + sp.Rational(1, 2))*Om + tau/12 + sp.log(1 - tau**2/6)/(2*tau)
for tv in (sp.Rational(1, 10), sp.Rational(7, 5), sp.Rational(12, 5)):
    for nv in (0, 3):
        d = (En_b - alt).subs({tau: tv, n: nv}).evalf(30)
        print(f"S6 alt-form difference at tau={tv}, n={nv}: {d}")
