# C4: the exact kernel <0|exp(-tau H)|0> for H = -(1/2) Laplacian - 1/r, by two independent routes.
# Environment: Python 3.13.16, numpy 2.5.3, scipy 1.18.1, mpmath 1.3.0. Deterministic.
#
# Route (i), closed form from recalled spectral data, answer eq. (C9):
#   K0(tau) = sum_{n>=1} exp(tau/(2n^2)) / (pi n^3)  +  (1/pi) int_0^inf k exp(-tau k^2/2) / (1 - exp(-2 pi/k)) dk
#   inputs [R]/[V]: |psi_n00(0)|^2 = 1/(pi n^3), E_n = -1/(2n^2), Sommerfeld factor (2pi/k)/(1-e^{-2pi/k}),
#   completeness of {bound states, Coulomb waves}, and that only l = 0 states are nonzero at r = 0.
# Route (ii), from the Hamiltonian only: the l = 0 radial operator -(1/2) d^2/dr^2 - 1/r on (0, Rbox) with
#   u(0) = u(Rbox) = 0, discretised by second-order finite differences, diagonalised. For l = 0,
#   psi(r) = u(r)/(sqrt(4 pi) r), so psi(0) = u'(0)/sqrt(4 pi); states with l >= 1 vanish at r = 0.
#   K0_box = (1/4pi) sum_i exp(-tau E_i) u_i'(0)^2, with u'(0) from the second-order one-sided formula
#   u'(0) ~ (4 u_1 - u_2)/(2h). Eigenpairs above Ecut = 120 are dropped; the dropped part is bounded by
#   exp(-tau_min*Ecut) * 17/(16 pi h^3) < 1e-19 (completeness of the discrete eigenvectors).
# Control: the same box code with V = 0 must reproduce the free value (2 pi tau)^(-3/2).
# Declared failure (before running):
#   G1 free control: relative error > 1e-3 at the finest h;
#   G2 Coulomb box vs closed form: relative difference > 5e-3 at the finest h;
#   G3 after Richardson extrapolation with the observed order: relative difference > 5e-4;
#   G4 box bound states n = 1..3: |E_n + 1/(2n^2)| > 1e-3 or relative error of |psi(0)|^2 vs 1/(pi n^3) > 5e-3;
#   G5 box-size sensitivity (Rbox = 30 vs 40 at h = 0.01): relative change > 1e-6.
import numpy as np
from scipy.linalg import eigh_tridiagonal
import mpmath as mp

taus = [0.5, 1.0, 2.0, 4.0]
ECUT = 120.0
fails = []

# ---------------- route (i) ----------------
mp.mp.dps = 30
def closed_form(tau):
    tau = mp.mpf(tau)
    Sb = mp.nsum(lambda n: mp.exp(tau / (2 * n**2)) / (mp.pi * n**3), [1, mp.inf])
    Sc = mp.quad(lambda k: k * mp.exp(-tau * k**2 / 2) / (-mp.expm1(-2 * mp.pi / k)), [0, 0.5, 2, 6, mp.inf]) / mp.pi
    return float(Sb), float(Sc), float(Sb + Sc)

# ---------------- route (ii) ----------------
def box(h, Rbox, coulomb=True):
    M = int(round(Rbox / h)) - 1
    r = h * np.arange(1, M + 1)
    d = np.full(M, 1.0 / h**2) + (-1.0 / r if coulomb else 0.0)
    e = np.full(M - 1, -0.5 / h**2)
    w, v = eigh_tridiagonal(d, e, select='v', select_range=(-10.0, ECUT))
    du0 = (4 * v[0, :] - v[1, :]) / (2 * h**1.5)   # u'(0) with u_j = v_j / sqrt(h)
    return w, du0

def K_box(w, du0, tau):
    return float(np.sum(np.exp(-tau * w) * du0**2) / (4 * np.pi))

print("route (i): closed form")
cf = {}
for tau in taus:
    Sb, Sc, tot = closed_form(tau)
    cf[tau] = tot
    free = (2 * np.pi * tau) ** -1.5
    print(f"  tau={tau:<4} bound part={Sb:.10f}  continuum part={Sc:.10f}  total={tot:.10f}  free={free:.10f}  ratio={tot/free:.4f}")

hs = [0.02, 0.01, 0.005]
Rbox = 40.0
res, resfree = {}, {}
for h in hs:
    w, du0 = box(h, Rbox, True)
    wf, du0f = box(h, Rbox, False)
    res[h] = {tau: K_box(w, du0, tau) for tau in taus}
    resfree[h] = {tau: K_box(wf, du0f, tau) for tau in taus}
    if h == hs[-1]:
        print("\nG4: lowest box eigenstates at h = 0.005, Rbox = 40")
        for n in (1, 2, 3):
            En, p0 = w[n - 1], du0[n - 1] ** 2 / (4 * np.pi)
            dE, dp = En + 1 / (2 * n**2), p0 / (1 / (np.pi * n**3)) - 1
            print(f"  n={n}: E={En:.7f} (exact -1/(2n^2) = {-1/(2*n**2):.7f}, diff {dE:+.2e});  |psi(0)|^2={p0:.7f} (1/(pi n^3) = {1/(np.pi*n**3):.7f}, rel {dp:+.2e})")
            if abs(dE) > 1e-3 or abs(dp) > 5e-3:
                fails.append(("G4", n))

print("\nG1: free control, box (V = 0) vs (2 pi tau)^(-3/2)")
for tau in taus:
    free = (2 * np.pi * tau) ** -1.5
    row = "  ".join(f"h={h}: {resfree[h][tau]/free-1:+.2e}" for h in hs)
    print(f"  tau={tau:<4} relative error  {row}")
    if abs(resfree[hs[-1]][tau] / free - 1) > 1e-3:
        fails.append(("G1", tau))

print("\nG2/G3: Coulomb box vs closed form")
for tau in taus:
    d = [res[h][tau] / cf[tau] - 1 for h in hs]
    p = np.log2(abs(res[hs[0]][tau] - res[hs[1]][tau]) / abs(res[hs[1]][tau] - res[hs[2]][tau]))
    rich = res[hs[2]][tau] + (res[hs[2]][tau] - res[hs[1]][tau]) / (2**p - 1)
    dr = rich / cf[tau] - 1
    print(f"  tau={tau:<4} rel.diff h=0.02: {d[0]:+.2e}  h=0.01: {d[1]:+.2e}  h=0.005: {d[2]:+.2e}   observed order p={p:.2f}   Richardson: {dr:+.2e}")
    if abs(d[2]) > 5e-3:
        fails.append(("G2", tau))
    if abs(dr) > 5e-4:
        fails.append(("G3", tau))

print("\nG5: box size, h = 0.01")
w30, d30 = box(0.01, 30.0, True)
for tau in taus:
    a, b = K_box(w30, d30, tau), res[0.01][tau]
    print(f"  tau={tau:<4} Rbox=30: {a:.12f}  Rbox=40: {b:.12f}  rel.change {a/b-1:+.2e}")
    if abs(a / b - 1) > 1e-6:
        fails.append(("G5", tau))
print("\nFAILURES:", fails if fails else "none")
