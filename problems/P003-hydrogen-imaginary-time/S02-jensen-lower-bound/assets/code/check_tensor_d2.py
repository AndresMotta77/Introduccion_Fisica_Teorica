# check_tensor_d2.py -- P003.S02, check S9 [N], added in round 2 (response to audit finding F1.1).
# Standalone. Run: PYTHONHASHSEED=0 python3 -P -s check_tensor_d2.py
# Tested with: Python 3.13.18, sympy 1.14.0. Parameters drawn with random.Random(20261113).
#
# Purpose: test the INDEX CONTRACTIONS of eq. (27) in d = 2, where they are not
# reducible to 1D products. For a polynomial potential the bridge action
# S = int_0^tau V(omega(u)) du has an exactly computable variance:
#     Var S = 2 int_0^tau du int_0^u dv Cov( V(h(u)), V(h(v)) ),
#     h(u) = omega(u) - xbar = s(u) Delta + xi(u),  s(u) = u/tau - 1/2,
# with xi the centred bridge, Cov(xi_i(u), xi_j(v)) = delta_ij C(u,v), eq. (8).
# Gaussian moments are computed by Stein's identity E[x_i f(X)] = sum_j Sigma_ij E[d_j f(X)]
# (derived in the text, section 4.3), self-tested below. The potential is taken as its
# Taylor polynomial at xbar, cubic + quartic, with random rational coefficients:
#     V(xbar + h) = V_i h_i + (1/2) V_ij h_i h_j + (1/6) V_ijk h_i h_j h_k + (1/24) V_ijkl h_i h_j h_k h_l
# (the constant V(xbar) does not enter Var S). tau = e^2, Delta = e*dvec (the regime |Delta| ~ sqrt(tau)).
# Eq. (27) predicts, with summation over repeated indices,
#   [e^6]  D V_i V_i / 6
#   [e^8]  D V_ij d_j V_ik d_k / 360 + D V_i V_ijk d_j d_k / 120 + D^2 ( V_ij V_ij / 45 + V_i V_ijj / 15 )
# and no e^0..e^5 or e^7 terms; no fourth-derivative terms through e^8.
# Alternative readings of the contractions are evaluated too, to show the test discriminates.
# FAIL if any predicted coefficient differs from the exact one, or a forbidden coefficient is nonzero.
# Assumptions ([A] in text): D > 0, 0 < v < u < tau; the potential is not bounded below, which is
# irrelevant here: Var S is a Gaussian-moment identity, not a statement about e^{-tau H}.
import itertools
import random
from functools import lru_cache
import sympy as sp

print("sympy", sp.__version__)
rng = random.Random(20261113)
e = sp.symbols('e', positive=True)
u, v = sp.symbols('u v', positive=True)


def make_moment(Sigma, n):
    """Moments of a centred Gaussian vector of length n with covariance Sigma (sympy Matrix)."""
    @lru_cache(maxsize=None)
    def mom(m):
        k = sum(m)
        if k == 0:
            return sp.Integer(1)
        if k % 2:
            return sp.Integer(0)
        i = next(a for a in range(n) if m[a] > 0)
        m1 = list(m); m1[i] -= 1                      # x^m = x_i * x^{m1}
        res = sp.Integer(0)
        for j in range(n):                            # Stein: E[x_i f] = sum_j Sigma_ij E[d_j f]
            if m1[j] > 0 and Sigma[i, j] != 0:
                m2 = list(m1); c = m2[j]; m2[j] -= 1
                res += Sigma[i, j]*c*mom(tuple(m2))
        return sp.expand(res)
    return mom


def expect(poly, X, mom):
    P = sp.Poly(sp.expand(poly), *X)
    return sp.expand(sum(coef*mom(tuple(mon)) for mon, coef in P.terms()))


# ---- self-test of the moment routine against textbook Gaussian moments
s11, s12, s22 = sp.symbols('s11 s12 s22')
Sig = sp.Matrix([[s11, s12], [s12, s22]])
x1, x2 = sp.symbols('x1 x2')
mt = make_moment(Sig, 2)
tests = [(x1**4, 3*s11**2), (x1**6, 15*s11**3), (x1**2*x2**2, s11*s22 + 2*s12**2),
         (x1**3*x2, 3*s11*s12), (x1**4*x2**2, 3*s11**2*s22 + 12*s11*s12**2), (x1**3, 0)]
ok_self = all(sp.expand(expect(p, (x1, x2), mt) - r) == 0 for p, r in tests)
print("S9 self-test of Gaussian moment routine:", "PASS" if ok_self else "FAIL")


def rat(lo=-9, hi=9, dmax=5):
    q = sp.Rational(rng.randint(lo, hi), rng.randint(1, dmax))
    return q


def sym_tensor(order, d=2):
    """Random fully symmetric tensor of given order in d dims (dict index-tuple -> Rational)."""
    T = {}
    for idx in itertools.combinations_with_replacement(range(d), order):
        val = rat()
        for perm in set(itertools.permutations(idx)):
            T[perm] = val
    return T


allpass = ok_self
for run in range(3):
    d = 2
    Dv = sp.Rational(rng.randint(1, 9), rng.randint(1, 4))
    g = [rat() for _ in range(d)]
    H = sym_tensor(2); T3 = sym_tensor(3); T4 = sym_tensor(4)
    dvec = [rat(-5, 5, 3) for _ in range(d)]
    if all(x == 0 for x in dvec):
        dvec[0] = sp.Integer(1)
    tau = e**2
    Delta = [e*dv for dv in dvec]
    s_u, s_v = u/tau - sp.Rational(1, 2), v/tau - sp.Rational(1, 2)
    # covariance on the triangle 0 < v < u < tau, eq. (8)
    Cuu = 2*Dv*u*(tau - u)/tau
    Cvv = 2*Dv*v*(tau - v)/tau
    Cuv = 2*Dv*v*(tau - u)/tau
    X = sp.symbols('a1 a2 b1 b2')                    # xi(u) = (a1,a2), xi(v) = (b1,b2)
    Sigma = sp.Matrix([[Cuu, 0, Cuv, 0], [0, Cuu, 0, Cuv], [Cuv, 0, Cvv, 0], [0, Cuv, 0, Cvv]])
    mom = make_moment(Sigma, 4)

    def Vpoly(h):
        out = sum(g[i]*h[i] for i in range(d))
        out += sp.Rational(1, 2)*sum(H[(i, j)]*h[i]*h[j] for i in range(d) for j in range(d))
        out += sp.Rational(1, 6)*sum(T3[(i, j, k)]*h[i]*h[j]*h[k] for i in range(d) for j in range(d) for k in range(d))
        out += sp.Rational(1, 24)*sum(T4[(i, j, k, l)]*h[i]*h[j]*h[k]*h[l]
                                      for i in range(d) for j in range(d) for k in range(d) for l in range(d))
        return out

    hu = [s_u*Delta[i] + X[i] for i in range(d)]
    hv = [s_v*Delta[i] + X[2 + i] for i in range(d)]
    Vu, Vv = Vpoly(hu), Vpoly(hv)
    cov = expect(Vu*Vv, X, mom) - expect(Vu, X, mom)*expect(Vv, X, mom)
    cov = sp.expand(cov)
    varS = sp.expand(2*sp.integrate(sp.integrate(cov, (v, 0, u)), (u, 0, tau)))
    co = {n: sp.nsimplify(varS.coeff(e, n)) for n in range(0, 13)}

    # predictions of eq. (27), explicit index sums
    R = range(d)
    ViVi = sum(g[i]**2 for i in R)
    HdHd = sum(sum(H[(i, j)]*dvec[j] for j in R)**2 for i in R)
    gTdd = sum(g[i]*T3[(i, j, k)]*dvec[j]*dvec[k] for i in R for j in R for k in R)
    trH2 = sum(H[(i, j)]**2 for i in R for j in R)
    gLap = sum(g[i]*T3[(i, j, j)] for i in R for j in R)
    p6 = Dv*ViVi/6
    p8 = Dv*HdHd/360 + Dv*gTdd/120 + Dv**2*(trH2/45 + gLap/15)
    # alternative readings (should NOT match)
    gd = sum(g[i]*dvec[i] for i in R)
    alt_gT = gd*sum(T3[(i, j, j)]*dvec[i] for i in R for j in R)            # (V_i d_i)(V_ijj d_j)
    trH = sum(H[(i, i)] for i in R)
    alt8_a = Dv*HdHd/360 + Dv*alt_gT/120 + Dv**2*(trH2/45 + gLap/15)
    alt8_b = Dv*HdHd/360 + Dv*gTdd/120 + Dv**2*(trH**2/45 + gLap/15)        # (tr H)^2 instead of tr H^2
    forbidden = [n for n in (0, 1, 2, 3, 4, 5, 7) if co[n] != 0]
    r6, r8 = sp.simplify(co[6] - p6), sp.simplify(co[8] - p8)
    passed = (r6 == 0 and r8 == 0 and not forbidden)
    allpass &= passed
    print(f"\nS9 run {run}: D={Dv}, grad={g}, dvec={dvec}")
    print(f"   H={[[H[(i, j)] for j in R] for i in R]}, V_111,V_112,V_122,V_222={[T3[(0,0,0)],T3[(0,0,1)],T3[(0,1,1)],T3[(1,1,1)]]}")
    print(f"   exact [e^6]={co[6]}  pred={p6}  resid={r6}")
    print(f"   exact [e^8]={co[8]}  pred={p8}  resid={r8}")
    print(f"   alternative (V_i d_i)(V_ijj d_j) in place of V_i V_ijk d_j d_k: resid={sp.simplify(co[8]-alt8_a)}")
    print(f"   alternative (tr H)^2 in place of tr(H^2):                      resid={sp.simplify(co[8]-alt8_b)}")
    print(f"   nonzero coefficients among e^0..e^5, e^7: {forbidden}   [e^10] (tau^5, not predicted) = {co[10]}")
    print("   ->", "PASS" if passed else "FAIL")

print("\nS9 overall:", "PASS" if allpass else "FAIL")
