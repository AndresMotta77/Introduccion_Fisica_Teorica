# check_symbolic.py -- P003.S02, symbolic checks [N].
# Standalone. Run: python3 check_symbolic.py
# Tested with: Python 3.13.18, sympy 1.14.0, mpmath 1.3.0.  No randomness.
#
# Symbol assumptions used below (each is stated as [A] in the text):
#   D > 0 (given in the problem), time intervals a, b, c, u, w > 0
#   (they are the lengths u, tau-u, ... of sub-intervals of (0, tau)),
#   kappa > 0 (oscillator), x, x', y real.
# No simplify call below relies on any other assumption.
import sympy as sp

print("sympy", sp.__version__)

D, kap = sp.symbols('D kappa', positive=True)
a, b, c, u, w = sp.symbols('a b c u w', positive=True)
x, xp, y, y1, y2, X, Dl = sp.symbols('x xp y y1 y2 X Delta', real=True)


def rho0(p, q, t):
    """1D free kernel, prompt section 3a, d = 1."""
    return (4*sp.pi*D*t)**sp.Rational(-1, 2)*sp.exp(-(p - q)**2/(4*D*t))


def report(name, expr):
    e = sp.simplify(expr)
    print(f"{name}: residual = {e}   ->", "PASS" if e == 0 else "FAIL")


# ---------------------------------------------------------------- S1
# Bridge marginal at time u (tau = u + w): product of free kernels divided
# by rho0(x,x';tau), compared with the claimed Gaussian N(m_u, s2_u),
# m_u = (x w + x' u)/tau, s2_u = 2 D u w / tau   (eqs. (5)-(6) of the text).
tau = u + w
lhs = rho0(x, y, u)*rho0(y, xp, w)/rho0(x, xp, tau)
m_u = (x*w + xp*u)/tau
s2_u = 2*D*u*w/tau
gauss = (2*sp.pi*s2_u)**sp.Rational(-1, 2)*sp.exp(-(y - m_u)**2/(2*s2_u))
report("S1 log(marginal) - log(claimed Gaussian)",
       sp.expand_log(sp.log(lhs), force=True) - sp.expand_log(sp.log(gauss), force=True))

# ---------------------------------------------------------------- S2
# Chapman-Kolmogorov: int dy rho0(x,y;u) rho0(y,x';w) = rho0(x,x';u+w).
ck = sp.integrate(rho0(x, y, u)*rho0(y, xp, w), (y, -sp.oo, sp.oo))
report("S2 Chapman-Kolmogorov ratio - 1", sp.simplify(ck/rho0(x, xp, u + w)) - 1)

# ---------------------------------------------------------------- S3
# Two-time joint density of the bridge at times u1 = a, u2 = a+b, tau = a+b+c,
# from the product of three free kernels (definition). Its exponent is a
# quadratic form in (y1, y2); read off the precision matrix, invert, compare
# with the claimed covariance 2D[min(u,v) - u v/tau]   (eq. (8) of the text).
expo = -(y1 - x)**2/(4*D*a) - (y2 - y1)**2/(4*D*b) - (xp - y2)**2/(4*D*c)
P = sp.Matrix(2, 2, lambda i, j: -sp.diff(expo, [y1, y2][i], [y1, y2][j]))
Cov = sp.simplify(P.inv())
T = a + b + c
u1, u2 = a, a + b
claimed = sp.Matrix([[2*D*(u1 - u1*u1/T), 2*D*(u1 - u1*u2/T)],
                     [2*D*(u1 - u1*u2/T), 2*D*(u2 - u2*u2/T)]])
for i in range(2):
    for j in range(2):
        report(f"S3 Cov[{i}{j}] - claimed", Cov[i, j] - claimed[i, j])
# mean of the joint density: stationary point of expo
sol = sp.solve([sp.diff(expo, y1), sp.diff(expo, y2)], [y1, y2], dict=True)[0]
report("S3 mean(y1) - m(u1)", sol[y1] - (x*(T - u1) + xp*u1)/T)
report("S3 mean(y2) - m(u2)", sol[y2] - (x*(T - u2) + xp*u2)/T)

# ---------------------------------------------------------------- S4
# Covariance integrals used in part (b). C(u,v) = 2D min(u,v)(tau-max)/tau.
# Integrate over the triangle v<u and double (C symmetric).
t = sp.symbols('t', positive=True)   # t = tau
U, V_ = sp.symbols('U V', positive=True)
Clow = 2*D*V_*(t - U)/t              # C(U,V) for V < U
def dbl(f_low):
    return sp.simplify(2*sp.integrate(sp.integrate(f_low, (V_, 0, U)), (U, 0, t)))
I1 = dbl(Clow)
I2 = sp.simplify(sp.integrate(sp.integrate(Clow*(U/t - sp.Rational(1, 2)), (V_, 0, U)), (U, 0, t))
                 + sp.integrate(sp.integrate(Clow*(V_/t - sp.Rational(1, 2)), (V_, 0, U)), (U, 0, t)))
I3 = dbl(Clow*(U/t - sp.Rational(1, 2))*(V_/t - sp.Rational(1, 2)))
I4 = dbl(Clow**2)
# int int C(u,v) C(v,v) du dv  (not symmetric: do it directly)
Cfull = lambda p, q: 2*D*sp.Min(p, q)*(t - sp.Max(p, q))/t
I5 = sp.simplify(sp.integrate(sp.integrate(2*D*U*(t - V_)/t*2*D*V_*(t - V_)/t, (U, 0, V_))
                              + sp.integrate(2*D*V_*(t - U)/t*2*D*V_*(t - V_)/t, (U, V_, t)), (V_, 0, t)))
report("S4 I1 - D t^3/6", I1 - D*t**3/6)
report("S4 I2 (odd moment) - 0", I2)
report("S4 I3 - D t^3/360", I3 - D*t**3/360)
report("S4 I4 - 2 D^2 t^4/45", I4 - 2*D**2*t**4/45)
report("S4 I5 - D^2 t^4/15", I5 - D**2*t**4/15)

# ---------------------------------------------------------------- S5
# <V>_u for V = kappa y^2/2 from the DEFINITION (integral over y of the kernel
# product), then integrated over u in (0, tau). Compared with the claim
# int_0^tau <V>_u du = (kappa tau/6)(x^2 + x x' + x'^2) + kappa D tau^2/6.
avgV = sp.integrate(rho0(x, y, u)*kap*y**2/2*rho0(y, xp, w), (y, -sp.oo, sp.oo))/rho0(x, xp, u + w)
avgV = sp.simplify(avgV)
uu = sp.symbols('uu', positive=True)
avgV_u = sp.simplify(avgV.subs(w, t - u).subs(u, uu))
intV = sp.simplify(sp.integrate(avgV_u, (uu, 0, t)))
report("S5 int <V>_u du - claimed", intV - (kap*t/6*(x**2 + x*xp + xp**2) + kap*D*t**2/6))
# endpoint limits (trapezium identity, part (b))
report("S5 lim u->0 <V>_u - V(x)", sp.limit(avgV_u, uu, 0) - kap*x**2/2)
report("S5 lim u->tau <V>_u - V(x')", sp.limit(avgV_u, uu, t) - kap*xp**2/2)

# ---------------------------------------------------------------- S6
# Mehler kernel (oscillator H = -D d^2/dx^2 + kappa x^2/2, omega = sqrt(2 D kappa),
# M = 1/(2D)). Not taken on trust: check that it solves the imaginary-time
# equation  d_tau K = D K_xx - (kappa x^2/2) K  and that ln K - ln rho0 -> 0 as tau->0.
om = sp.sqrt(2*D*kap)
Mw = om/(2*D)
def K_mehler(p, q, s):
    return sp.sqrt(Mw/(2*sp.pi*sp.sinh(om*s)))*sp.exp(-Mw*((p**2 + q**2)*sp.cosh(om*s) - 2*p*q)/(2*sp.sinh(om*s)))
s = sp.symbols('s', positive=True)
Km = K_mehler(x, xp, s)
pde = sp.diff(Km, s) - (D*sp.diff(Km, x, 2) - kap*x**2/2*Km)
report("S6 Mehler PDE residual / K", sp.simplify((pde/Km).rewrite(sp.exp)))
lead = sp.series(sp.log(Km/rho0(x, xp, s)).rewrite(sp.exp), s, 0, 1).removeO()
report("S6 ln K - ln rho0 at O(s^0)", sp.simplify(lead))

# ---------------------------------------------------------------- S7
# ln K_exact - ln RHS(*) for the oscillator, x = X - Delta/2, x' = X + Delta/2,
# Delta = d sqrt(tau) (the scaling of part (b)). tau = e^2, expand in e.
# Prediction (from the general variance computation, text eq. (26), plus the
# quadratic-V extras, eq. (30)):
#   kappa^2 D tau^3 X^2/12 + kappa^2 D tau^3 Delta^2/720 + kappa^2 D^2 tau^4/90 + O(tau^5)
e, dd = sp.symbols('e d', positive=True)
taue = e**2
xs, xps = X - dd*e/2, X + dd*e/2
RHS = rho0(xs, xps, taue)*sp.exp(-(kap*taue/6*(xs**2 + xs*xps + xps**2) + kap*D*taue**2/6))
diff_log = sp.log(K_mehler(xs, xps, taue)) - sp.log(RHS)
ser = sp.series(diff_log.rewrite(sp.exp), e, 0, 11).removeO()
ser = sp.expand(sp.simplify(ser))
pred = kap**2*D*taue**3*X**2/12 + kap**2*D*taue**3*(dd*e)**2/720 + kap**2*D**2*taue**4/90
print("S7 series of ln(K/RHS) through e^10 (tau^5):")
print("   ", sp.collect(ser, e))
resid = sp.expand(ser - pred)
low = sum(resid.coeff(e, k)*e**k for k in range(0, 10))
report("S7 residual through tau^4 (e^0..e^9)", low)
print("S7 first term beyond prediction (e^10 = tau^5):", sp.factor(resid.coeff(e, 10)))
