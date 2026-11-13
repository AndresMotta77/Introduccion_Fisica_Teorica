# check_b.py -- part (b): closed forms of Zhat_m, Z_m, Ehat_m, E_m; table; second route.
# Python 3.13.18, numpy 2.5.3, mpmath 1.3.0. Deterministic (no random numbers).
# Run: python3 -I check_b.py
#
# B1  table from the closed forms of the text (mpmath, 30 digits), plus exact 1/2 coth(beta/2).
# B2  SECOND ROUTE: for each (beta, m) build the m x m Hessian H of the closed-ring action
#     S(x) = -sum_n ln w(x_n, x_{n+1}) numerically by polarisation (S evaluated from the
#     closed form of (a); no circulant algebra, no product formula), the beta-derivative of H
#     by complex-step differentiation of S, then
#        ln Zhat = -S(0) + (m/2) ln 2pi - (1/2) ln det H,
#        Ehat    = dS(0)/dbeta + (1/2) tr(H^{-1} dH/dbeta),
#     and the same for the primitive product rho0(x_n,x_{n+1}) exp(-tau V(x_n)).
#     Failure: |Delta E| > 1e-8 or |Delta ln Z| > 1e-8 at any of the 15 points.
# B3  analytic beta-derivative vs mpmath numerical derivative of ln Zhat (closed form).
# B4  bounds: Zhat_m <= Z_exact (Jensen), Z_m >= Z_exact.
# B5  Ehat_m from the spectrum of (c): sum_n eps_n lam_n^m / sum_n lam_n^m, eps_n = -d ln|lam_n|/dtau.
# B6  large-m asymptotics: m^2 (Ehat_m - U) -> beta^2 (U/8 + beta U'/24) - beta^3/(36 m) + O(1/m^2),
#     m^2 (E_m - U) -> -beta^2 (U/8 + beta U'/24) + O(1/m^2).
import numpy as np
import mpmath as mp

mp.mp.dps = 30
BETAS = [1, 5, 10]
MS = [1, 10, 50, 100, 500]

# ---------------- closed forms of (b), typed from the text ----------------
def Zhat(beta, m):
    beta = mp.mpf(beta); t = beta/m
    k = mp.sqrt(1 + t**2/12)
    return mp.exp(-beta*t/12)/((k + t/2)**m - (k - t/2)**m)

def Ehat(beta, m):
    beta = mp.mpf(beta); t = beta/m
    k = mp.sqrt(1 + t**2/12); kp = t/(12*k)
    a, b = k + t/2, k - t/2
    return t/6 + (a**(m - 1)*(kp + mp.mpf(1)/2) - b**(m - 1)*(kp - mp.mpf(1)/2))/(a**m - b**m)

def Zprim(beta, m):
    beta = mp.mpf(beta); t = beta/m
    k = mp.sqrt(1 + t**2/4)
    return 1/((k + t/2)**m - (k - t/2)**m)

def Eprim(beta, m):
    beta = mp.mpf(beta); t = beta/m
    k = mp.sqrt(1 + t**2/4); kp = t/(4*k)
    a, b = k + t/2, k - t/2
    return (a**(m - 1)*(kp + mp.mpf(1)/2) - b**(m - 1)*(kp - mp.mpf(1)/2))/(a**m - b**m)

def Eprim_coth(beta, m):          # equivalent form 2 in the text
    t = mp.mpf(beta)/m
    return mp.coth(m*mp.asinh(t/2))/mp.sqrt(4 + t**2)

def U(beta):
    return mp.coth(mp.mpf(beta)/2)/2

nfail = 0
# ---------------- B1: table ----------------
print("B1 closed-form table")
print(f"{'beta':>4} {'m':>4} {'Ehat_m':>16} {'E_m':>16} {'exact':>16} {'Ehat_m-exact':>14} {'E_m-exact':>14}")
table = {}
for beta in BETAS:
    for m in MS:
        eh, ep, ex = Ehat(beta, m), Eprim(beta, m), U(beta)
        table[(beta, m)] = (eh, ep)
        print(f"{beta:4d} {m:4d} {mp.nstr(eh, 12, min_fixed=-1, max_fixed=3):>16} "
              f"{mp.nstr(ep, 12, min_fixed=-1, max_fixed=3):>16} {mp.nstr(ex, 12, min_fixed=-1, max_fixed=3):>16} "
              f"{mp.nstr(eh - ex, 6):>14} {mp.nstr(ep - ex, 6):>14}")
print("    max |E_m(product form) - E_m(coth form)| over table:",
      mp.nstr(max(abs(Eprim(b, m) - Eprim_coth(b, m)) for b in BETAS for m in MS), 3))

# ---------------- B2: second route, numerically assembled m x m matrices ----------------
def bond_bridge(a, b, t):          # -ln w(a,b;t), w from eq. (a); works for complex t
    w = np.exp(-(a - b)**2/(2*t))/np.sqrt(2*np.pi*t)*np.exp(-t*(a*a + a*b + b*b)/6 - t*t/12)
    return -np.log(w)

def bond_prim(a, b, t):            # -ln[rho0(a,b;t) exp(-t V(a))]
    w = np.exp(-(a - b)**2/(2*t))/np.sqrt(2*np.pi*t)*np.exp(-t*a*a/2)
    return -np.log(w)

def action(X, beta, m, bond):      # X: (..., m) array of configurations; closed ring
    t = beta/m
    return np.sum(bond(X, np.roll(X, -1, axis=-1), t), axis=-1)

def route2(beta, m, bond):
    hcs = 1e-30                    # complex-step size
    def S_and_dS(X):
        Sc = action(X.astype(complex), beta + 1j*hcs, m, bond)
        return Sc.real, Sc.imag/hcs
    S0, dS0 = S_and_dS(np.zeros((1, m)))
    S0, dS0 = S0[0], dS0[0]
    E = np.eye(m)
    Se, dSe = S_and_dS(E)                         # S(e_i)
    H = np.zeros((m, m)); dH = np.zeros((m, m))
    for i in range(m):
        Sij, dSij = S_and_dS(E + E[i])            # rows: e_j + e_i
        H[i, :] = Sij - Se[i] - Se + S0
        dH[i, :] = dSij - dSe[i] - dSe + dS0
        H[i, i] = 2*(Se[i] - S0)
        dH[i, i] = 2*(dSe[i] - dS0)
    sign, logdet = np.linalg.slogdet(H)
    lnZ = -S0 + 0.5*m*np.log(2*np.pi) - 0.5*logdet
    En = dS0 + 0.5*np.trace(np.linalg.solve(H, dH))
    asym = np.max(np.abs(H - H.T))
    return lnZ, En, sign, asym

print("B2 second route (numerically assembled m x m Hessians) vs closed forms")
print(f"{'beta':>4} {'m':>4} {'dlnZhat':>10} {'dEhat':>10} {'dlnZ':>10} {'dE':>10} {'sgn':>4}")
for beta in BETAS:
    for m in MS:
        lzb, eb, sb, ab = route2(beta, m, bond_bridge)
        lzp, ep, sp_, ap = route2(beta, m, bond_prim)
        d1 = lzb - float(mp.log(Zhat(beta, m))); d2 = eb - float(table[(beta, m)][0])
        d3 = lzp - float(mp.log(Zprim(beta, m))); d4 = ep - float(table[(beta, m)][1])
        ok = max(abs(d1), abs(d2), abs(d3), abs(d4)) < 1e-8 and sb > 0 and sp_ > 0 \
            and np.all(np.isfinite([d1, d2, d3, d4]))
        nfail += (not ok)
        print(f"{beta:4d} {m:4d} {d1:10.1e} {d2:10.1e} {d3:10.1e} {d4:10.1e} {int(sb*sp_):4d} "
              f"{'ok' if ok else 'FAIL'}")

# ---------------- B3: analytic derivative vs numerical derivative ----------------
worst = mp.mpf(0)
for beta in BETAS:
    for m in MS:
        nd_h = -mp.diff(lambda bb: mp.log(Zhat(bb, m)), beta)
        nd_p = -mp.diff(lambda bb: mp.log(Zprim(bb, m)), beta)
        worst = max(worst, abs(nd_h - Ehat(beta, m)), abs(nd_p - Eprim(beta, m)))
print("B3 max |(-d/dbeta ln Z, mpmath numerical) - (analytic E)| over 30 values:", mp.nstr(worst, 3))
nfail += not (worst < mp.mpf('1e-20'))

# ---------------- B4: bounds ----------------
Zex = lambda beta: 1/(2*mp.sinh(mp.mpf(beta)/2))
v1 = [(b, m) for b in BETAS for m in MS if not (Zhat(b, m) <= Zex(b))]
v2 = [(b, m) for b in BETAS for m in MS if not (Zprim(b, m) >= Zex(b))]
print("B4 violations of Zhat_m <= Z_exact:", v1, "  violations of Z_m >= Z_exact:", v2)
print("    min Z_exact/Zhat_m =", mp.nstr(min(Zex(b)/Zhat(b, m) for b in BETAS for m in MS), 8),
      "  min Z_m/Z_exact =", mp.nstr(min(Zprim(b, m)/Zex(b) for b in BETAS for m in MS), 8))
nfail += len(v1) + len(v2)

# ---------------- B5: Ehat from the spectrum of (c) ----------------
def Ehat_from_spectrum(beta, m):
    t = mp.mpf(beta)/m
    k = mp.sqrt(1 + t**2/12); kp = t/(12*k)
    a, b = k + t/2, k - t/2
    q = b/a
    N = int(mp.ceil(45*mp.log(10)/(-m*mp.log(abs(q))))) + 10 if q != 0 else 1
    num = den = mp.mpf(0)
    for n in range(N):
        lam = mp.exp(-t**2/12)*b**n/a**(n + 1)
        eps = t/6 + (n + 1)*(kp + mp.mpf(1)/2)/a - (n*(kp - mp.mpf(1)/2)/b if n > 0 else 0)
        num += eps*lam**m; den += lam**m
    return num/den, den, N

worstE = worstZ = mp.mpf(0)
for beta in BETAS:
    for m in MS:
        e5, z5, N = Ehat_from_spectrum(beta, m)
        worstE = max(worstE, abs(e5 - Ehat(beta, m)))
        worstZ = max(worstZ, abs(z5/Zhat(beta, m) - 1))
print("B5 spectrum of (c) vs closed forms of (b): max |dE| =", mp.nstr(worstE, 3),
      " max |sum lam^m / Zhat - 1| =", mp.nstr(worstZ, 3))
nfail += not (worstE < mp.mpf('1e-25') and worstZ < mp.mpf('1e-25'))

# ---------------- B6: large-m asymptotics ----------------
print("B6 large-m: D_hat = m^2(Ehat-U) - [beta^2(U/8+beta U'/24) - beta^3/(36m)],  "
      "D_prim = m^2(E-U) + beta^2(U/8+beta U'/24); both should be O(1/m^2)")
for beta in BETAS:
    b = mp.mpf(beta)
    Ub = U(b); Up = -1/(4*mp.sinh(b/2)**2)
    c2 = b**2*(Ub/8 + b*Up/24)
    row = []
    for m in (500, 1000, 2000, 4000, 8000):
        Dh = m**2*(Ehat(b, m) - Ub) - (c2 - b**3/(36*m))
        Dp = m**2*(Eprim(b, m) - Ub) + c2
        row.append(f"m={m}: m^2*Dh={mp.nstr(m**2*Dh, 6)}, m^2*Dp={mp.nstr(m**2*Dp, 6)}")
    print(f"  beta={beta:2d} coeff beta^2(U/8+beta U'/24)={mp.nstr(c2, 10)}")
    for r in row:
        print("     ", r)
print("TOTAL FAILURES (B2-B5):", nfail)
