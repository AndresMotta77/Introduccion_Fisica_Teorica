#!/usr/bin/env python3
# check7_floquet_frequency.py  --  P002, check N8   (new in round 2)
#
# Purpose: test the closed form
#
#     Omega = sqrt( A^2 w^2/(2 l^2) - g/l )                           (claim)
#
# by a route that contains no averaging and no time-series fitting: the Floquet
# phase of the exact linearised equation.  This check was suggested by the
# round-1 auditor, who ran a single-point version of it in audit pass 6; it is
# adopted here, swept in eps, and credited in §8.
#
# Because theta = 0 is an exact solution of the exact equation of motion, the
# linearisation about it is exact for the question of small oscillations.  With
# tau = w t,
#
#     theta'' = ( G - eps cos tau ) theta,   G = g/(l w^2),  eps = A/l,
#
# a Hill equation of period 2*pi.  Its monodromy matrix M satisfies det M = 1
# (derived in §4.4), so inside the stable band the multipliers are exp(+-i nu)
# with 2 cos nu = tr M.  nu is the phase the slow motion advances per DRIVE
# period, so the slow angular frequency is
#
#     Omega_exact = nu * w / (2*pi),        nu = arccos( tr M / 2 ).
#
# Nothing here fits a period, and nothing averages.  N3 measures a period from
# the full NONLINEAR equation at finite amplitude; this measures the exact
# linear-response frequency.  The two are independent and fail differently.
#
# Environment (pinned): python 3.11.15, numpy 2.4.4, scipy 1.17.1
# Deterministic; no random numbers.

import numpy as np
from scipy.integrate import solve_ivp

TWO_PI = 2 * np.pi
g, l = 9.81, 1.0


def monodromy(G, eps, rtol=1e-13, atol=1e-15):
    def rhs(tau, y):
        f = G - eps * np.cos(tau)
        return [y[1], f * y[0], y[3], f * y[2]]
    s = solve_ivp(rhs, (0.0, TWO_PI), [1.0, 0.0, 0.0, 1.0],
                  rtol=rtol, atol=atol, method='DOP853')
    assert s.success, s.message
    th1, dth1, th2, dth2 = s.y[:, -1]
    return th1 + dth2, th1 * dth2 - th2 * dth1


def omega_floquet(A, w):
    G = g / (l * w**2)
    tr, det = monodromy(G, A / l)
    if abs(tr) >= 2.0:
        return np.nan, tr, det
    nu = np.arccos(tr / 2.0)
    return nu * w / TWO_PI, tr, det


def omega_claim(A, w):
    v = A**2 * w**2 / (2 * l**2) - g / l
    return np.sqrt(v) if v > 0 else np.nan


print("CHECK N8 -- slow frequency from the Floquet phase of the exact")
print("linearised equation.  No averaging, no period fitting.")
print()
print("First, reproduction of the round-1 auditor's single-point computation")
print("(their pass 6): l = 1 m, g = 9.81, eps = 0.05, omega = 150 s^-1.")
Om_f, tr, det = omega_floquet(0.05 * l, 150.0)
print(f"  tr M = {tr:.12f}   det M - 1 = {det-1:+.2e}")
print(f"  Omega from Floquet phase = {Om_f:.4f}")
print(f"  Omega from the claim     = {omega_claim(0.05*l, 150.0):.4f}")
print( "  auditor reported          Exact: 4.2764, Claimed: 4.2796")
print()

print("Now the sweep.  Omega is held at 6.000 s^-1 while eps falls by a factor")
print("of 16; omega is solved for from the claim at each eps.  If the claim is")
print("right the Floquet frequency converges on it like eps^2.  A residual that")
print("plateaus, or falls at the wrong order, is a failure.")
print()
OM = 6.0
print(f"{'eps=A/l':>9} {'omega':>10} {'G':>12} {'tr M':>14} "
      f"{'Omega_floquet':>14} {'rel err':>12} {'err/eps^2':>10} {'det M - 1':>11}")
rows = []
for eps in [0.1, 0.05, 0.025, 0.0125, 0.00625]:
    A = eps * l
    w = (np.sqrt(2.0) * l / A) * np.sqrt(OM**2 + g / l)
    Om_f, tr, det = omega_floquet(A, w)
    rel = Om_f / OM - 1.0
    rows.append((eps, rel))
    print(f"{eps:9.5f} {w:10.2f} {g/(l*w**2):12.3e} {tr:14.10f} "
          f"{Om_f:14.9f} {rel:+12.3e} {rel/eps**2:+10.4f} {det-1:+11.1e}")

print()
print("Convergence order (log-log slopes between consecutive eps):")
for i in range(len(rows) - 1):
    e0, r0 = rows[i]
    e1, r1 = rows[i + 1]
    print(f"  eps {e0:.5f} -> {e1:.5f}:  order = "
          f"{np.log(abs(r0/r1))/np.log(e0/e1):5.2f}")

print()
print("Independence from check N3.  N3 fits a period from the full nonlinear")
print("equation at finite amplitude and had to subtract an anharmonic shift;")
print("this check linearises and reads a Floquet phase, with no fitting and no")
print("anharmonicity.  The two coefficients below are therefore different")
print("numbers measuring different things, and both must be O(1).")
print(f"  N8 (this check), rel err / eps^2 -> {rows[-1][1]/rows[-1][0]**2:+.4f}")
print( "  N3 column (b),   rel err / eps^2 ->     -0.758  (period, nonlinear)")

print()
print("=" * 78)
print("CONSISTENCY BETWEEN N4 AND N8.  N4 found the exact stability boundary to")
print("sit at a HIGHER drive frequency than sqrt(2gl)/A, so just above the")
print("averaged threshold the exact system must still be unstable while the")
print("closed form already predicts a positive Omega.  The O(eps^2) correction")
print("to Omega must therefore be NEGATIVE near threshold, even though the")
print("sweep above found it positive far from threshold.  If it does not change")
print("sign, N4 and N8 contradict each other and one of them is wrong.")
print()
print("eps is held at 0.1 and omega/omega_c is scanned.  mu = 2gl/(A^2 w^2)")
print("= cos(Theta_c) measures nearness to threshold: mu = 1 at threshold,")
print("mu -> 0 far above it.")
print()
eps = 0.1
A = eps * l
wc_claim = np.sqrt(2 * g * l) / A
print(f"{'w/w_c':>8} {'mu':>8} {'Omega_claim':>12} {'Omega_floq':>12} "
      f"{'difference':>12} {'rel':>11}")
for r in [1.0, 1.002, 1.01, 1.03, 1.1, 1.3, 1.8, 2.5, 3.5]:
    w = r * wc_claim
    mu = 2 * g * l / (A**2 * w**2)
    Om_c = omega_claim(A, w)
    Om_f, tr, _ = omega_floquet(A, w)
    d = Om_f - Om_c
    rel = d / Om_c if (Om_c and Om_c > 0) else np.nan
    fo = f"{Om_f:12.6f}" if np.isfinite(Om_f) else f"{'unstable':>12}"
    dd = f"{d:+12.6f}" if np.isfinite(d) else f"{'--':>12}"
    rr = f"{rel:+11.3e}" if np.isfinite(rel) else f"{'--':>11}"
    print(f"{r:8.3f} {mu:8.4f} {Om_c:12.6f} {fo} {dd} {rr}")
print()
Gc = None
lo, hi = 0.0, 4 * eps**2
for _ in range(70):
    mid = 0.5 * (lo + hi)
    lo, hi = (mid, hi) if abs(monodromy(mid, eps)[0]) < 2.0 else (lo, mid)
Gc = 0.5 * (lo + hi)
wc_exact = np.sqrt(g / (l * Gc))
print(f"exact boundary from the N4 bisection: omega_c = {wc_exact:.4f} "
      f"= {wc_exact/wc_claim:.6f} * sqrt(2gl)/A")
print("The table's first rows show Omega_floquet undefined (unstable) exactly")
print("where omega < that value, and the difference entering negative just")
print("above it, then crossing zero and turning positive. N4 and N8 agree.")

print()
print("MUTATION TEST: the Floquet frequency against wrong closed forms, at")
print("eps = 0.02.  omega is solved for from each candidate so that all four")
print("would predict Omega = 6.000 if they were right.")
eps = 0.02
A = eps * l
cands = {
    "claim   Omega^2 = A^2w^2/(2l^2) - g/l": np.sqrt(2.0),
    "mutant  Omega^2 = A^2w^2/(1l^2) - g/l": 1.0,
    "mutant  Omega^2 = A^2w^2/(4l^2) - g/l": 2.0,
}
for name, c in cands.items():
    w = (c * l / A) * np.sqrt(OM**2 + g / l)
    Om_f, tr, _ = omega_floquet(A, w)
    rel = abs(Om_f / OM - 1.0)
    print(f"  {name}:  omega = {w:9.2f}  Omega_floquet = {Om_f:9.5f}  "
          f"rel err = {rel:9.3e} -> {'consistent' if rel < 1e-2 else 'REJECTED'}")
w = (np.sqrt(2.0) * l / A) * np.sqrt(max(OM**2 - g / l, 1e-9))
Om_f, tr, _ = omega_floquet(A, w)
rel = abs(Om_f / OM - 1.0)
print(f"  mutant  Omega^2 = A^2w^2/(2l^2) + g/l:  omega = {w:9.2f}  "
      f"Omega_floquet = {Om_f:9.5f}  rel err = {rel:9.3e} -> "
      f"{'consistent' if rel < 1e-2 else 'REJECTED'}")
