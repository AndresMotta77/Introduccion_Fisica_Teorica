#!/usr/bin/env python3
# check2_newton_vs_lagrange.py  --  P002, check N2   (second version; see the
# note at the bottom of this header for what changed after the first version
# failed, and why)
#
# Purpose: test the equation of motion
#
#     l*thetadd = (g - A*w**2*cos(w*t)) * sin(theta)                  (claim)
#
# against a SECOND, independently formulated dynamics: Newton's second law in
# Cartesian coordinates for the bob, with the rigid stick represented by a
# constraint force along the stick whose magnitude is fixed by differentiating
# the constraint |r - p(t)| = l twice.  No Lagrangian, no generalised
# coordinate, and no expression lifted from the hand derivation.
#
# Let u = r - p(t) be the bob position relative to the pivot, |u| = l.
#   m*rdd = -m*g*jhat + (lambda/l) * u          (force along the stick)
#   udd   = rdd - pdd
#   u.u = l^2  =>  u.ud = 0  =>  u.udd + |ud|^2 = 0
# which gives   k := lambda/(m*l) = ((g + pdd_y)*u_y - |ud|^2) / l^2
# and           udd = ( k*u_x , -(g + pdd_y) + k*u_y ).
#
# Environment (pinned):
#   python 3.11.15, numpy 2.4.4, scipy 1.17.1
# Parameter sets are drawn with numpy PCG64 seeded at 20260913.  Every set
# drawn is reported.
#
# WHAT CHANGED AFTER THE FIRST RUN (reported in full in the answer): the first
# version applied a single fixed criterion, max|dtheta| < 1e-6 over a 6 s
# window, to all eight sets.  Set 8 failed it.  Set 8 sits BELOW the stability
# threshold, so the pendulum falls and then whirls, and in that regime the
# motion has a positive Lyapunov exponent: two numerically exact but distinct
# integrations of the same equations separate exponentially.  The criterion was
# therefore wrong for that regime, not the physics.  The change made was to the
# CHECK, not to the derivation: the fixed-tolerance criterion is kept, and any
# set that fails it is then subjected to a tolerance-refinement study.  A
# discrepancy that falls when rtol is tightened -- in step with the independent
# witness |u| - l, which the theta-equation cannot drift in by construction --
# is integrator error.  A discrepancy that does not fall is a real
# disagreement.  The cost of this is stated in the coverage note.

import numpy as np
from scipy.integrate import solve_ivp

SEED = 20260913
rng = np.random.default_rng(SEED)
G = 9.81


def rhs_theta(t, s, g, l, A, w, sign=-1.0):
    """Scalar equation of motion in theta (the claim).
    sign=-1 is the claim; sign=+1 is a deliberately wrong mutant."""
    th, thd = s
    return [thd, (g + sign * A * w**2 * np.cos(w * t)) * np.sin(th) / l]


def rhs_cartesian(t, s, g, l, A, w):
    """Newton + constraint force, in Cartesian components of u = r - p(t)."""
    ux, uy, vx, vy = s
    pdd_y = -A * w**2 * np.cos(w * t)
    k = ((g + pdd_y) * uy - (vx * vx + vy * vy)) / l**2
    return [vx, vy, k * ux, -(g + pdd_y) + k * uy]


def run_pair(g, l, A, w, th0, thd0, tmax, rtol=1e-11, n=2001, sign=-1.0):
    ts = np.linspace(0.0, tmax, n)
    kw = dict(t_eval=ts, rtol=rtol, atol=rtol / 10, method='DOP853',
              max_step=0.2 * 2 * np.pi / w)
    a = solve_ivp(rhs_theta, (0, tmax), [th0, thd0], args=(g, l, A, w, sign), **kw)
    u0 = [l * np.sin(th0), l * np.cos(th0),
          l * thd0 * np.cos(th0), -l * thd0 * np.sin(th0)]
    b = solve_ivp(rhs_cartesian, (0, tmax), u0, args=(g, l, A, w), **kw)
    assert a.success and b.success, (a.message, b.message)
    th_b = np.arctan2(b.y[0], b.y[1])
    d = np.abs(np.unwrap(a.y[0]) - np.unwrap(th_b))   # unwrap: a 2pi wrap is
    drift = np.abs(np.hypot(b.y[0], b.y[1]) - l) / l  # not a disagreement
    return d.max(), drift.max()


print("CHECK N2 -- scalar theta-equation vs Newton-with-constraint-force.")
print("Both integrations start from the same physical state.")
print("Primary criterion: max|dtheta| < 1e-6 rad over the window at rtol=1e-11.")
print("A real disagreement would show as a discrepancy that does NOT fall when")
print("rtol is tightened.  Both integrators are DOP853, so a shared")
print("discretisation bias is not credible at these tolerances.")
print()
hdr = (f"{'set':>3} {'l':>6} {'A':>8} {'omega':>8} {'w/w_c':>6} {'th0':>8} "
       f"{'tmax':>6} {'max|dth|':>11} {'|u|drift':>10}  verdict")
print(hdr)

sets, failed = [], []
for i in range(8):
    l = float(rng.uniform(0.2, 1.5))
    A = float(rng.uniform(0.005, 0.05) * l)          # A << l
    wc = np.sqrt(2 * G * l) / A                      # averaged threshold
    factor = float(rng.uniform(1.2, 2.5)) if i < 6 else float(rng.uniform(0.4, 0.8))
    w = factor * wc
    th0 = float(rng.uniform(-0.3, 0.3))
    tmax = min(40 * 2 * np.pi / w * 5, 6.0)
    d, drift = run_pair(G, l, A, w, th0, 0.0, tmax)
    ok = d < 1e-6
    if not ok:
        failed.append((i + 1, l, A, w, th0, tmax))
    sets.append((l, A, w, factor, th0, tmax))
    print(f"{i+1:>3} {l:6.3f} {A:8.5f} {w:8.1f} {factor:6.2f} {th0:8.4f} "
          f"{tmax:6.2f} {d:11.3e} {drift:10.2e}  {'PASS' if ok else 'FAIL'}")

print()
print(f"Primary criterion: {8-len(failed)}/8 sets passed.")

if failed:
    print()
    print("Tolerance-refinement study on the set(s) that failed.")
    print("If the discrepancy is integrator error it falls with rtol, and the")
    print("constraint residual |u|-l falls with it.  If the two formulations")
    print("actually disagree, neither falls.")
    for (idx, l, A, w, th0, tmax) in failed:
        print(f"  set {idx}:  l={l:.4f}  A={A:.5f}  omega={w:.1f}  th0={th0:.4f}")
        prev = None
        for rtol in [1e-8, 1e-10, 1e-12, 1e-13]:
            d, drift = run_pair(G, l, A, w, th0, 0.0, tmax, rtol=rtol, n=4001)
            trend = "" if prev is None else f"  (x{d/prev:.2e})"
            prev = d
            print(f"     rtol={rtol:.0e}   max|dth|={d:.3e}   "
                  f"max||u|-l|/l={drift:.3e}{trend}")
        # and the same comparison restricted to the first 20 drive periods,
        # before exponential separation has had time to act
        tshort = 20 * 2 * np.pi / w
        d_s, drift_s = run_pair(G, l, A, w, th0, 0.0, tshort, rtol=1e-11)
        print(f"     first 20 drive periods (t < {tshort:.4f} s): "
              f"max|dth|={d_s:.3e}  -> {'PASS' if d_s < 1e-6 else 'FAIL'}")

# --- mutation test: can this check reject a wrong equation of motion? -------
print()
print("Mutation test (super-threshold set, where the primary criterion holds):")
l, A = 1.0, 0.02
w = 1.6 * np.sqrt(2 * G * l) / A
d_ok, _ = run_pair(G, l, A, w, 0.2, 0.0, 2.0, sign=-1.0)
d_mut, _ = run_pair(G, l, A, w, 0.2, 0.0, 2.0, sign=+1.0)
print(f"  claim as derived          : max|dtheta| = {d_ok:.3e}")
print(f"  driving term sign flipped : max|dtheta| = {d_mut:.3e}")
print("  MUTANT REJECTED:", "yes" if d_mut > 1e-6 else "NO -- the check is vacuous")
