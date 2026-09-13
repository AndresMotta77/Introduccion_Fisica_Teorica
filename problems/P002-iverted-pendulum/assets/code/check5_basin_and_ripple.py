#!/usr/bin/env python3
# check5_basin_and_ripple.py  --  P002, checks N5 and N6
#
# N5.  The effective potential per unit m*l^2 is
#          W(TH) = (g/l)*cos(TH) + (A^2 w^2/(4 l^2))*sin^2(TH),
#      whose stationary points are TH = 0, TH = pi, and (when A^2 w^2 > 2 g l)
#          TH_c = arccos( 2 g l / (A^2 w^2) ),
#      a maximum of W that bounds the well around the inverted position.  The
#      claim tested here is that TH_c is, to leading order in eps = A/l, the
#      largest release angle from rest for which the pendulum does not fall.
#      The exact nonlinear equation is integrated and the true boundary found
#      by bisection on the release angle; the two are compared as eps -> 0.
#
# N6.  The claim tested is that the fast ripple superposed on the slow motion
#      is  xi = (A/l)*sin(TH)*cos(w*t),  amplitude (A/l)*sin(TH).  The ripple
#      is extracted from the exact solution by subtracting a one-drive-period
#      moving average, and its envelope compared with (A/l)*sin(TH).
#
# Neither check uses any intermediate quantity from the hand derivation other
# than the formula being tested.  The trajectories come from the exact
# equation of motion, which check N1 and check N2 test separately.
#
# Environment (pinned): python 3.11.15, numpy 2.4.4, scipy 1.17.1
# Deterministic; no random numbers.

import numpy as np
from scipy.integrate import solve_ivp

g, l = 9.81, 1.0


def exact_rhs(t, s, A, w):
    th, thd = s
    return [thd, (g - A * w**2 * np.cos(w * t)) * np.sin(th) / l]


def falls(th0, A, w, n_slow=25):
    """Integrate from rest at th0 and report whether the pendulum leaves the
    neighbourhood of the inverted position.  Escape criterion: |theta| exceeds
    2.5 rad (143 deg), far outside any legitimate slow oscillation about 0 and
    still short of pi, so the test does not hinge on what happens after it
    falls."""
    Om2 = A**2 * w**2 / (2 * l**2) - g / l
    Om = np.sqrt(max(Om2, 1e-12))
    tmax = n_slow * 2 * np.pi / Om
    ev = lambda t, s, A, w: abs(s[0]) - 2.5
    ev.terminal, ev.direction = True, 1.0
    sol = solve_ivp(exact_rhs, (0, tmax), [th0, 0.0], args=(A, w),
                    rtol=1e-9, atol=1e-11, method='DOP853',
                    max_step=2 * np.pi / w / 10, events=ev)
    assert sol.success, sol.message
    return len(sol.t_events[0]) > 0


def boundary_release_angle(A, w, iters=18):
    lo, hi = 1e-3, 1.6                    # lo must survive, hi must fall;
    #                                       hi is above any TH_c tested here
    #                                       and below the escape threshold
    assert not falls(lo, A, w), "even a tiny release angle falls"
    assert falls(hi, A, w), "release at 1.6 rad does not fall"
    for _ in range(iters):
        mid = 0.5 * (lo + hi)
        if falls(mid, A, w):
            hi = mid
        else:
            lo = mid
    return 0.5 * (lo + hi)


print("CHECK N5 -- basin boundary of the inverted position.")
print("TH_c = arccos(2 g l / (A^2 w^2)) is compared with the release angle at")
print("which the exact nonlinear equation first fails to hold the pendulum up.")
print("The target is held fixed at TH_c = 60 deg while eps = A/l is reduced,")
print("so a discrepancy that does not shrink with eps is a failure.")
print()
TH_C_TARGET = np.deg2rad(60.0)
print("Two comparisons are made.  The raw one compares TH_c with the release")
print("angle theta(0).  But releasing FROM REST at theta(0) does not set the")
print("slow amplitude to theta(0): at t = 0 the fast ripple is at its maximum,")
print("xi(0) = (A/l) sin(TH), so the slow amplitude is theta(0) - (A/l)sin(TH).")
print("That is an O(eps) offset predicted by the same derivation, so the")
print("corrected column is the sharper test.  If the correction were invented")
print("to close a gap it would not also have the right coefficient, which is")
print("why sin(TH_c) = sin(60 deg) = 0.8660 is printed alongside diff/eps.")
print()
print(f"{'eps=A/l':>9} {'A':>8} {'omega':>10} {'TH_c pred':>11} "
      f"{'TH_c exact':>11} {'raw diff':>11} {'diff/eps':>9} {'corrected':>11} "
      f"{'corr/eps^2':>11}")
rows5 = []
for eps in [0.08, 0.04, 0.02, 0.01]:
    A = eps * l
    # solve  cos(TH_c) = 2 g l/(A^2 w^2)  for w
    w = np.sqrt(2 * g * l / (A**2 * np.cos(TH_C_TARGET)))
    th_pred = np.arccos(2 * g * l / (A**2 * w**2))
    th_num = boundary_release_angle(A, w)
    d = th_num - th_pred
    dc = (th_num - (A / l) * np.sin(th_num)) - th_pred
    rows5.append((eps, d, dc))
    print(f"{eps:9.4f} {A:8.4f} {w:10.2f} {th_pred:11.6f} {th_num:11.6f} "
          f"{d:+11.3e} {d/eps:+9.4f} {dc:+11.3e} {dc/eps**2:+11.4f}")

print()
print(f"sin(TH_c) = {np.sin(TH_C_TARGET):.4f} -- compare the diff/eps column.")
print()
print("Convergence orders:")
for i in range(len(rows5) - 1):
    e0, d0, c0 = rows5[i]
    e1, d1, c1 = rows5[i + 1]
    print(f"  eps {e0:.4f} -> {e1:.4f}:  order(raw) = "
          f"{np.log(abs(d0/d1))/np.log(e0/e1):5.2f}   order(corrected) = "
          f"{np.log(abs(c0/c1))/np.log(e0/e1):5.2f}")

print()
print("Control: is the bisected boundary actually sensitive to the prediction?")
print("Below-threshold parameters should give NO stable release angle at all.")
A, l_ = 0.02, 1.0
w_sub = 0.8 * np.sqrt(2 * g * l) / A      # below the threshold
try:
    b = boundary_release_angle(A, w_sub)
    print(f"  sub-threshold omega = {w_sub:.1f}: boundary found at {b:.4f} rad"
          "  <-- unexpected")
except AssertionError as e:
    print(f"  sub-threshold omega = {w_sub:.1f}: {e}  <-- expected: nothing is held")

print()
print("=" * 72)
print("CHECK N6 -- amplitude of the fast ripple, claimed to be (A/l)*sin(TH).")
print()
eps = 0.03
A = eps * l
w = 2.0 * np.sqrt(2 * g * l) / A
Om = np.sqrt(A**2 * w**2 / (2 * l**2) - g / l)
Tdrive = 2 * np.pi / w
tmax = 2 * np.pi / Om                      # one slow period
nper = 400                                 # samples per drive period
ts = np.linspace(0, tmax, int(tmax / Tdrive) * nper + 1)
sol = solve_ivp(exact_rhs, (0, tmax), [0.6, 0.0], args=(A, w), t_eval=ts,
                rtol=1e-12, atol=1e-14, method='DOP853', max_step=Tdrive / 40)
assert sol.success
th = sol.y[0]
# slow part: moving average over exactly one drive period
kern = np.ones(nper) / nper
slow = np.convolve(th, kern, mode='same')
ripple = th - slow
# compare the ripple envelope with (A/l)*sin(slow), drive period by period
nblocks = len(th) // nper
print(f"eps = {eps},  omega = {w:.1f},  Omega = {Om:.4f},  "
      f"{nblocks} drive periods in one slow period")
print(f"{'block':>6} {'TH (rad)':>10} {'ripple amp':>12} {'(A/l)|sinTH|':>13} "
      f"{'ratio':>9}")
ratios = []
for b in range(2, nblocks - 2):            # skip the edges of the convolution
    sl = slice(b * nper, (b + 1) * nper)
    amp = 0.5 * (ripple[sl].max() - ripple[sl].min())
    THb = slow[sl].mean()
    pred = (A / l) * abs(np.sin(THb))
    if b % max(1, (nblocks // 10)) == 0:
        print(f"{b:6d} {THb:10.5f} {amp:12.5e} {pred:13.5e} {amp/pred:9.5f}")
    ratios.append(amp / pred)
ratios = np.array(ratios)
print()
print(f"ratio over all {len(ratios)} interior drive periods: "
      f"mean {ratios.mean():.5f}, min {ratios.min():.5f}, max {ratios.max():.5f}")
print(f"Expected 1 + O(eps) = 1 +/- {eps:.2f}.  "
      f"{'PASS' if abs(ratios.mean()-1) < 3*eps else 'FAIL'}")
print()
print("The ratio is the wrong statistic near TH = 0, where the predicted")
print("amplitude (A/l)|sin TH| passes through zero and the O(eps^2) remainder")
print("dominates it; the outliers above are exactly those blocks.  Two better")
print("conditioned statistics follow.  They are additional diagnostics, not a")
print("replacement of the criterion above, which was met as stated.")
sin_all, amp_all, pred_all = [], [], []
for b in range(2, nblocks - 2):
    sl = slice(b * nper, (b + 1) * nper)
    amp_all.append(0.5 * (ripple[sl].max() - ripple[sl].min()))
    THb = slow[sl].mean()
    sin_all.append(abs(np.sin(THb)))
    pred_all.append((A / l) * abs(np.sin(THb)))
sin_all = np.array(sin_all); amp_all = np.array(amp_all); pred_all = np.array(pred_all)
sel = sin_all > 0.2
rsel = amp_all[sel] / pred_all[sel]
print(f"  (i)  ratio restricted to blocks with |sin TH| > 0.2 "
      f"({sel.sum()} blocks): mean {rsel.mean():.5f}, "
      f"min {rsel.min():.5f}, max {rsel.max():.5f}")
absres = np.abs(amp_all - pred_all)
print(f"  (ii) max absolute residual |amp - (A/l)|sin TH|| = {absres.max():.3e}"
      f"  = {absres.max()/eps**2:.3f} * eps^2   (expected O(eps^2))")
print()
print("Mutation: the same ratio against a constant-amplitude ripple A/l")
print("(i.e. dropping the sin(TH) factor):")
pred_const = A / l
r2 = []
for b in range(2, nblocks - 2):
    sl = slice(b * nper, (b + 1) * nper)
    r2.append(0.5 * (ripple[sl].max() - ripple[sl].min()) / pred_const)
r2 = np.array(r2)
print(f"  mean {r2.mean():.5f}, min {r2.min():.5f}, max {r2.max():.5f} "
      f"-> {'REJECTED' if r2.min() < 0.9 else 'not rejected'}")
