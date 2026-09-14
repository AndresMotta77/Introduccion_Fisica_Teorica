#!/usr/bin/env python3
# check6_duffing_shift.py  --  P002, check N7   (new in round 2)
#
# Purpose: test the amplitude-frequency relation derived by Lindstedt-Poincare
# in §3.9 of the answer,
#
#     xdd + Om^2 x + alpha x^3 = 0   =>   omega(a) = Om (1 + 3 alpha a^2/(8 Om^2))
#     and hence   T(a)/T(0) - 1 = -3 alpha a^2/(8 Om^2) + O(a^4).      (claim)
#
# In round 1 this relation was recalled rather than derived, tagged [R], and
# tested only indirectly (as column (c) of check N3, which measured it inside
# the pendulum problem).  Finding F1.2 of audit 1 asked for the provenance to be
# fixed.  It is now derived in the text, and this script tests the derived
# relation directly on the bare Duffing equation, away from the pendulum, so
# that the two are independent.
#
# Design: the residual is O(a^4) relative, so a single tolerance proves little.
# The amplitude is swept down by a factor of 8 and the residual is required to
# fall like a^2 RELATIVE to the shift itself (equivalently a^4 absolute), which
# a wrong coefficient cannot fake.  Mutants with 3/8 replaced by 1/8, 3/4 and
# -3/8 are run alongside.
#
# Environment (pinned): python 3.11.15, numpy 2.4.4, scipy 1.17.1
# Deterministic; no random numbers.

import numpy as np
from scipy.integrate import solve_ivp

OM = 6.0                      # same Omega as check N3 uses, for comparability
G_OVER_L = 9.81               # only used to build the pendulum's own alpha


def duffing_rhs(t, s, Om, alpha):
    x, v = s
    return [v, -Om**2 * x - alpha * x**3]


def measured_period(a, Om, alpha, n_periods=40):
    """Period from a straight-line fit to the zero-crossing times."""
    tmax = n_periods * 2 * np.pi / Om
    ts = np.linspace(0.0, tmax, 200001)
    sol = solve_ivp(duffing_rhs, (0, tmax), [a, 0.0], t_eval=ts,
                    args=(Om, alpha), rtol=1e-12, atol=1e-14, method='DOP853')
    assert sol.success, sol.message
    x = sol.y[0]
    sg = np.sign(x)
    idx = np.where(sg[:-1] * sg[1:] < 0)[0]
    t0, t1, y0, y1 = ts[idx], ts[idx + 1], x[idx], x[idx + 1]
    tc = t0 - y0 * (t1 - t0) / (y1 - y0)
    k = np.arange(len(tc))
    slope, _ = np.polyfit(k, tc, 1)
    return 2 * slope, len(tc)


print("CHECK N7 -- amplitude-frequency relation for xdd + Om^2 x + alpha x^3 = 0.")
print("Derived in §3.9 by Lindstedt-Poincare; tested here on the bare Duffing")
print("equation, with no pendulum anywhere in the script.")
print()

# alpha chosen to be the pendulum's own: the effective well of §3.8 has
# THdd = -Om^2 TH - 4 beta TH^3 with beta = -(Om^2/6 + (g/l)/8), so alpha = 4 beta.
beta = -(OM**2 / 6 + G_OVER_L / 8)
alpha = 4 * beta
print(f"Om = {OM}, beta = {beta:.6f}, alpha = 4*beta = {alpha:.6f}")
print("T(0) is taken as 2*pi/Om, the exact a -> 0 limit of the Duffing period.")
print()

T0 = 2 * np.pi / OM
print(f"{'a':>9} {'T_meas':>12} {'meas shift':>13} {'pred shift':>13} "
      f"{'residual':>12} {'resid/a^4':>11} {'ncross':>7}")
rows = []
for a in [0.16, 0.08, 0.04, 0.02]:
    T, nc = measured_period(a, OM, alpha)
    meas = T / T0 - 1
    pred = -3 * alpha * a**2 / (8 * OM**2)
    res = meas - pred
    rows.append((a, meas, pred, res))
    print(f"{a:9.4f} {T:12.8f} {meas:+13.5e} {pred:+13.5e} {res:+12.3e} "
          f"{res/a**4:11.4f} {nc:7d}")

print()
print("Convergence order of the residual (expected 4: the next term is O(a^4)):")
for i in range(len(rows) - 1):
    a0, _, _, r0 = rows[i]
    a1, _, _, r1 = rows[i + 1]
    print(f"  a {a0:.4f} -> {a1:.4f}:  order = "
          f"{np.log(abs(r0/r1))/np.log(a0/a1):5.2f}")

print()
print("Cross-check against check N3.  At a = 0.02, the shift predicted here is")
print("the eps-independent floor that column (c) of N3 measured inside the")
print("pendulum problem.")
a = 0.02
pred = -3 * alpha * a**2 / (8 * OM**2)
print(f"  predicted period shift at a = {a}: {pred:+.5e}")
print(f"  N3 column (c), measured in the pendulum:  +1.205e-04")
print(f"  (N3's column (c) is a PERIOD shift, so it should equal this value.)")

print()
print("MUTATION TEST: same measurement against wrong coefficients.")
for name, coef in [("3/8  (claim)", 3 / 8), ("1/8", 1 / 8), ("3/4", 3 / 4),
                   ("-3/8 (sign flipped)", -3 / 8)]:
    a = 0.08
    T, _ = measured_period(a, OM, alpha)
    meas = T / T0 - 1
    pred = -coef * alpha * a**2 / OM**2
    rel = abs(meas - pred) / abs(meas)
    print(f"  coefficient {name:22s}: predicted {pred:+.5e}, measured "
          f"{meas:+.5e}, rel err {rel:8.4f} -> "
          f"{'consistent' if rel < 0.02 else 'REJECTED'}")
