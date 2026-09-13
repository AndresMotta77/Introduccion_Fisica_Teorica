#!/usr/bin/env python3
# diag_set8.py -- diagnosis of the FAILING set 8 in check2.
# Question: is the disagreement a disagreement between the two FORMULATIONS,
# or is it the Cartesian integration losing the constraint |u| = l?
# Test: tighten rtol/atol and see whether max|dtheta| and the constraint drift
# fall together.  If they do, it is integrator error, not physics.

import numpy as np
from scipy.integrate import solve_ivp

SEED = 20260913
rng = np.random.default_rng(SEED)
g = 9.81
sets = []
for i in range(8):
    l = float(rng.uniform(0.2, 1.5))
    A = float(rng.uniform(0.005, 0.05) * l)
    wc = np.sqrt(2 * g * l) / A
    factor = float(rng.uniform(1.2, 2.5)) if i < 6 else float(rng.uniform(0.4, 0.8))
    w = factor * wc
    th0 = float(rng.uniform(-0.3, 0.3))
    sets.append((l, A, w, th0, min(40 * 2 * np.pi / w * 5, 6.0), factor))

for i, s in enumerate(sets, 1):
    print(i, [f"{v:.5g}" for v in s])
print()

l, A, w, th0, tmax, factor = sets[7]


def rhs_theta(t, s):
    th, thd = s
    return [thd, (g - A * w**2 * np.cos(w * t)) * np.sin(th) / l]


def rhs_cart(t, s):
    ux, uy, vx, vy = s
    pdd_y = -A * w**2 * np.cos(w * t)
    k = ((g + pdd_y) * uy - (vx * vx + vy * vy)) / l**2
    return [vx, vy, k * ux, -(g + pdd_y) + k * uy]


ts = np.linspace(0, tmax, 4001)
for tol in [1e-9, 1e-11, 1e-13, 1e-14]:
    a = solve_ivp(rhs_theta, (0, tmax), [th0, 0.0], t_eval=ts, rtol=tol,
                  atol=tol / 10, method='DOP853', max_step=0.2 * 2 * np.pi / w)
    u0 = [l * np.sin(th0), l * np.cos(th0), 0.0, 0.0]
    b = solve_ivp(rhs_cart, (0, tmax), u0, t_eval=ts, rtol=tol, atol=tol / 10,
                  method='DOP853', max_step=0.2 * 2 * np.pi / w)
    th_b = np.arctan2(b.y[0], b.y[1])
    d = np.abs(np.unwrap(a.y[0]) - np.unwrap(th_b))
    drift = np.abs(np.hypot(b.y[0], b.y[1]) - l) / l
    # first time the two curves separate by more than 1e-6
    idx = np.argmax(d > 1e-6) if np.any(d > 1e-6) else -1
    tsep = ts[idx] if idx >= 0 else np.inf
    print(f"rtol={tol:.0e}  max|dth|={d.max():.3e}  max drift={drift.max():.3e}  "
          f"separation time={tsep:.3f} s  (tmax={tmax:.2f})")

print()
print("Number of drive periods in the window:", tmax * w / (2 * np.pi))
print("factor omega/omega_crit =", factor, " -> below threshold, pendulum falls")
