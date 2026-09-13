#!/usr/bin/env python3
# check4_floquet_boundary.py  --  P002, check N4
#
# Purpose: test the stability condition
#
#     A^2 * w^2 > 2 * g * l                                           (claim)
#
# against exact Floquet theory for the linearised equation of motion, which
# involves no averaging at all.
#
# Linearising the exact equation about theta = 0 and putting tau = w*t,
#
#     theta'' = ( G - eps*cos(tau) ) * theta ,
#       G   = g/(l*w^2),      eps = A/l ,     ' = d/dtau .
#
# This is a Hill equation with period 2*pi in tau.  Its monodromy matrix M is
# built by integrating from the two initial conditions (1,0) and (0,1) over one
# period.  The equation has no damping, so det M = 1 exactly, and the origin is
# linearly stable iff |tr M| < 2.  The claim, rewritten in these variables, is
#
#     stable  <=>  eps^2/2 > G ,   i.e. the boundary is  G_c = eps^2/2 .
#
# The test is not "does one point agree" but "does the exactly computed
# boundary G_c(eps) approach eps^2/2 as eps -> 0, and at what rate".
#
# Environment (pinned): python 3.11.15, numpy 2.4.4, scipy 1.17.1
# Deterministic; no random numbers.

import numpy as np
from scipy.integrate import solve_ivp

TWO_PI = 2 * np.pi


def monodromy_trace(G, eps):
    def rhs(tau, y):
        # y = [th1, th1', th2, th2']
        f = G - eps * np.cos(tau)
        return [y[1], f * y[0], y[3], f * y[2]]
    sol = solve_ivp(rhs, (0.0, TWO_PI), [1.0, 0.0, 0.0, 1.0],
                    rtol=1e-13, atol=1e-15, method='DOP853', dense_output=False)
    assert sol.success, sol.message
    th1, dth1, th2, dth2 = sol.y[:, -1]
    det = th1 * dth2 - th2 * dth1       # must be 1: an independent witness
    return th1 + dth2, det


def boundary_G(eps, lo=0.0, hi=None, iters=80):
    """Bisect on G for |tr M| = 2 at fixed eps.  Stable (|tr|<2) for small G,
    unstable for large G."""
    if hi is None:
        hi = max(4 * eps**2, 1e-6)
    # make sure the bracket really brackets
    while abs(monodromy_trace(hi, eps)[0]) < 2.0:
        hi *= 2
        if hi > 10:
            raise RuntimeError("no unstable side found")
    if abs(monodromy_trace(lo, eps)[0]) >= 2.0:
        raise RuntimeError("G=0 is already unstable at eps=%g" % eps)
    for _ in range(iters):
        mid = 0.5 * (lo + hi)
        if abs(monodromy_trace(mid, eps)[0]) < 2.0:
            lo = mid
        else:
            hi = mid
    return 0.5 * (lo + hi)


print("CHECK N4 -- exact Floquet stability boundary of the linearised exact")
print("equation, compared with the averaged prediction G_c = eps^2/2.")
print("No averaging enters the computation; the only approximation is the")
print("linearisation in theta, which is exact for the stability of theta = 0.")
print()
print("Sanity: at eps = 0 the equation is theta'' = G*theta, so")
print("tr M = 2*cosh(2*pi*sqrt(G)) > 2 for every G > 0 -- always unstable.")
for Gtest in [1e-4, 1e-2, 1.0]:
    tr, det = monodromy_trace(Gtest, 0.0)
    print(f"   G = {Gtest:.0e}:  tr M = {tr:.10f}   "
          f"2*cosh(2*pi*sqrt(G)) = {2*np.cosh(TWO_PI*np.sqrt(Gtest)):.10f}   "
          f"det M - 1 = {det-1:+.1e}")
print()

print(f"{'eps=A/l':>9} {'G_c exact':>14} {'eps^2/2':>14} {'ratio':>10} "
      f"{'(ratio-1)/eps^2':>16} {'det M - 1':>11}")
rows = []
for eps in [0.4, 0.2, 0.1, 0.05, 0.025, 0.0125]:
    Gc = boundary_G(eps)
    _, det = monodromy_trace(Gc, eps)
    ratio = Gc / (eps**2 / 2)
    rows.append((eps, Gc, ratio))
    print(f"{eps:9.5f} {Gc:14.9f} {eps**2/2:14.9f} {ratio:10.6f} "
          f"{(ratio-1)/eps**2:16.4f} {det-1:+11.1e}")

print()
print("The ratio approaches 1 and (ratio - 1)/eps^2 approaches a constant, so")
print("the exact boundary is G_c = (eps^2/2)*(1 + c*eps^2 + ...): the averaged")
print("condition is the leading term, with a relative error of order eps^2.")
print()

# --- the same statement in physical variables ------------------------------
print("Same boundary in physical variables, at g = 9.81 m/s^2, l = 1 m:")
g, l = 9.81, 1.0
print(f"{'A (m)':>9} {'w_c exact':>13} {'sqrt(2gl)/A':>13} {'ratio':>10}")
for eps in [0.4, 0.2, 0.1, 0.05, 0.025, 0.0125]:
    A = eps * l
    Gc = boundary_G(eps)
    wc_exact = np.sqrt(g / (l * Gc))          # G = g/(l w^2)
    wc_claim = np.sqrt(2 * g * l) / A
    print(f"{A:9.5f} {wc_exact:13.4f} {wc_claim:13.4f} {wc_exact/wc_claim:10.6f}")

print()
print("MUTATION TEST: which of these candidate boundaries does the exact")
print("Floquet computation actually select, as eps -> 0?")
for name, factor in [("G_c = eps^2/2  (claim)", 0.5),
                     ("G_c = eps^2", 1.0),
                     ("G_c = eps^2/4", 0.25),
                     ("G_c = eps/2", None)]:
    print(f"  {name}:")
    for eps in [0.1, 0.025, 0.0125]:
        Gc = boundary_G(eps)
        pred = factor * eps**2 if factor is not None else eps / 2
        print(f"     eps={eps:7.4f}:  G_c(exact)/pred = {Gc/pred:.6f}")
