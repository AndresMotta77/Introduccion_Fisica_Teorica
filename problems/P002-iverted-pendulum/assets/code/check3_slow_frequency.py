#!/usr/bin/env python3
# check3_slow_frequency.py  --  P002, check N3
#
# Purpose: test the headline result
#
#     Omega = sqrt( A^2*w^2/(2*l^2) - g/l )                           (claim)
#
# by integrating the EXACT equation of motion -- the one that comes out of the
# problem statement, with no averaging anywhere in the integrator -- and
# measuring the period of the slow back-and-forth motion from its zero
# crossings.  The claimed Omega is used only at the end, to be compared
# against; it never enters the integration.
#
# Design of the sweep.  The averaging is an expansion in eps = A/l, so a single
# pass/fail at one tolerance says little.  Instead eps is swept downwards with
# Omega HELD FIXED (w is solved for at each eps), and the residual is required
# to fall like eps^2, which is the order of the first neglected term.  A wrong
# numerical factor inside Omega produces an O(1) residual that does not fall at
# all, which is what the mutation test at the bottom demonstrates.
#
# Two comparisons are reported per eps:
#   (a) measured period vs 2*pi/Omega        -- the headline claim, harmonic;
#   (b) measured period vs the period of the averaged equation integrated at
#       the SAME initial amplitude -- this removes the anharmonicity of the
#       effective potential, which is a real effect and not an error, and so
#       isolates the error of the averaging step itself.
#
# Environment (pinned): python 3.11.15, numpy 2.4.4, scipy 1.17.1
# No random numbers are used; the sweep is deterministic.

import numpy as np
from scipy.integrate import solve_ivp

g, l = 9.81, 1.0
TH0 = 0.02          # small, so that the anharmonic shift is itself small
N_SLOW = 12         # slow periods integrated


def exact_rhs(t, s, A, w):
    th, thd = s
    return [thd, (g - A * w**2 * np.cos(w * t)) * np.sin(th) / l]


def averaged_rhs(t, s, A, w):
    TH, THd = s
    return [THd, (g / l) * np.sin(TH)
            - (A**2 * w**2 / (2 * l**2)) * np.sin(TH) * np.cos(TH)]


def zero_crossing_period(ts, th):
    """Half-period from a straight-line fit to the zero-crossing times.
    Returns (period, n_crossings, rms residual of the fit in seconds)."""
    s = np.sign(th)
    idx = np.where(s[:-1] * s[1:] < 0)[0]
    if len(idx) < 4:
        return np.nan, len(idx), np.nan
    t0, t1 = ts[idx], ts[idx + 1]
    y0, y1 = th[idx], th[idx + 1]
    tc = t0 - y0 * (t1 - t0) / (y1 - y0)      # linear interpolation
    k = np.arange(len(tc))
    slope, inter = np.polyfit(k, tc, 1)
    resid = np.sqrt(np.mean((tc - (slope * k + inter))**2))
    return 2 * slope, len(tc), resid


def measure(A, w, rhs, tmax):
    ts = np.linspace(0, tmax, 400001)
    sol = solve_ivp(rhs, (0, tmax), [TH0, 0.0], t_eval=ts, args=(A, w),
                    rtol=1e-11, atol=1e-13, method='DOP853',
                    max_step=2 * np.pi / w / 20)
    assert sol.success, sol.message
    return zero_crossing_period(ts, sol.y[0])


def omega_claim(A, w):
    val = A**2 * w**2 / (2 * l**2) - g / l
    return np.sqrt(val) if val > 0 else np.nan


print("CHECK N3 -- slow frequency measured from the exact equation of motion.")
print(f"g = {g}, l = {l}, theta(0) = {TH0} rad, thetadot(0) = 0.")
print("Omega is held at 6.000 rad/s while eps = A/l is swept; omega is solved")
print("for from the claim at each eps.  If the claim is right the measured")
print("period converges on 2*pi/Omega like eps^2.  A residual that plateaus,")
print("or that falls at the wrong order, is a failure.")
print()

OM = 6.0
T_harm = 2 * np.pi / OM

# Analytic size of the anharmonic shift, for comparison.  Expanding the
# effective potential per unit m*l^2,  W(TH) = (g/l) cos TH + (A^2 w^2/(4 l^2))
# sin^2 TH, about TH = 0 gives  THdd = -Omega^2 TH - 4*beta*TH^3  with
# beta = g/(24 l) - A^2 w^2/(12 l^2) = -(Omega^2/6 + g/(8 l)).  For
# xdd + Om^2 x + alpha x^3 = 0 with alpha = 4 beta, the amplitude-dependent
# frequency is Om(1 + 3 alpha a^2/(8 Om^2)), so the RELATIVE PERIOD shift is
# -3*alpha*a^2/(8*Om^2) = -3*beta*a^2/(2*Om^2).  This is a property of the
# averaged system, not an error of the averaging.
beta = -(OM**2 / 6 + g / (8 * l))
anh_pred = -3 * beta * TH0**2 / (2 * OM**2)
print(f"Predicted anharmonic period shift at theta(0) = {TH0}: "
      f"{anh_pred:+.4e} (relative).  This is an eps-independent floor under")
print("comparison (a) and must NOT be read as an error of the averaging.")
print()

print(f"{'eps=A/l':>9} {'A':>9} {'omega':>10} {'w/Om':>7} {'T_meas':>10} "
      f"{'(a)=T/Th-1':>12} {'(b)=T/Tav-1':>13} {'(c)=Tav/Th-1':>13} "
      f"{'(b)/eps^2':>10} {'ncross':>6} {'fitres':>9}")

rows = []
for eps in [0.1, 0.05, 0.025, 0.0125, 0.00625]:
    A = eps * l
    w = (np.sqrt(2.0) * l / A) * np.sqrt(OM**2 + g / l)   # inverts the claim
    tmax = N_SLOW * 2 * np.pi / OM
    T_ex, nc, res = measure(A, w, exact_rhs, tmax)
    T_av, _, _ = measure(A, w, averaged_rhs, tmax)
    ra = T_ex / T_harm - 1          # signed
    rb = T_ex / T_av - 1            # signed: the averaging error
    rc = T_av / T_harm - 1          # signed: the anharmonic shift, measured
    rows.append((eps, ra, rb, rc))
    print(f"{eps:9.5f} {A:9.5f} {w:10.2f} {w/OM:7.1f} {T_ex:10.6f} "
          f"{ra:+12.3e} {rb:+13.3e} {rc:+13.3e} "
          f"{abs(rb)/eps**2:10.3f} {nc:6d} {res:9.2e}")

print()
print("Decomposition check: (a) should equal (b) + (c) + O(second order).")
for eps, ra, rb, rc in rows:
    print(f"  eps={eps:8.5f}:  (a)={ra:+.4e}   (b)+(c)={rb+rc:+.4e}   "
          f"residual={ra-rb-rc:+.2e}")

print()
print("Observed convergence orders (log-log slopes between consecutive eps).")
print("Column (b) is the one that tests the averaging; (c) is eps-independent")
print("by construction and is shown to confirm that.")
for i in range(len(rows) - 1):
    e0, a0, b0, c0 = rows[i]
    e1, a1, b1, c1 = rows[i + 1]
    pb = np.log(abs(b0 / b1)) / np.log(e0 / e1)
    print(f"  eps {e0:.5f} -> {e1:.5f}:  order(b) = {pb:5.2f}   "
          f"(c) = {c0:+.3e} -> {c1:+.3e}")

print()
print("MUTATION TEST.  The same measurement, but the period is compared with")
print("mutant formulas.  Each mutant is used to solve for omega at eps = 0.02,")
print("then the exact equation is integrated and the period measured.  A")
print("mutant that survives would mean the check cannot tell formulas apart.")
eps = 0.02
A = eps * l
mutants = {
    "claim   Omega^2 = A^2w^2/(2l^2) - g/l": lambda: (np.sqrt(2.0) * l / A) * np.sqrt(OM**2 + g / l),
    "mutant  Omega^2 = A^2w^2/(1l^2) - g/l": lambda: (1.0 * l / A) * np.sqrt(OM**2 + g / l),
    "mutant  Omega^2 = A^2w^2/(4l^2) - g/l": lambda: (2.0 * l / A) * np.sqrt(OM**2 + g / l),
    "mutant  Omega^2 = A^2w^2/(2l^2) + g/l": lambda: (np.sqrt(2.0) * l / A) * np.sqrt(max(OM**2 - g / l, 1e-9)),
}
for name, wfun in mutants.items():
    w = wfun()
    T_ex, nc, _ = measure(A, w, exact_rhs, N_SLOW * 2 * np.pi / OM)
    rel = abs(T_ex / (2 * np.pi / OM) - 1)
    print(f"  {name}:  omega = {w:9.2f}  T_meas = {T_ex:9.6f}  "
          f"rel err = {rel:9.3e}  -> {'consistent' if rel < 1e-2 else 'REJECTED'}")
