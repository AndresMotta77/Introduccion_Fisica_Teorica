#!/usr/bin/env python3
# check1_eom_symbolic.py  --  P002, check N1
#
# Purpose: derive the equation of motion from the GEOMETRY of the problem
# (the Cartesian position of the bob) rather than from any expression that
# appears in the hand derivation, and compare the result with the claimed
# equation of motion
#
#     l*thetadd = (g - A*w**2*cos(w*t)) * sin(theta).                 (claim)
#
# Nothing below reuses an intermediate result of the hand derivation: the only
# inputs are x(t), y(t), the kinetic and potential energy definitions, and the
# Euler-Lagrange operator.
#
# Environment (pinned):
#   python 3.11.15, sympy 1.14.0
# No randomness is used in this script, so no seed is needed.

import sympy as sp

t = sp.symbols('t', real=True)
m, l, g, A, w = sp.symbols('m l g A omega', positive=True)
th = sp.Function('theta', real=True)(t)

# --- geometry, straight from the problem statement -------------------------
# theta is measured from the UPWARD vertical; the pivot sits at (0, y_p(t)).
y_p = A * sp.cos(w * t)
x = l * sp.sin(th)
y = y_p + l * sp.cos(th)

xd = sp.diff(x, t)
yd = sp.diff(y, t)

T = sp.Rational(1, 2) * m * (xd**2 + yd**2)
V = m * g * y
L = sp.simplify(T - V)
print("L =", sp.simplify(sp.expand_trig(L)))

# --- Euler-Lagrange --------------------------------------------------------
EL = sp.diff(sp.diff(L, sp.diff(th, t)), t) - sp.diff(L, th)
EL = sp.simplify(sp.expand(EL))
print("Euler-Lagrange expression (should equal 0):")
print(sp.simplify(EL))

# Solve for theta''
thdd = sp.solve(sp.Eq(EL, 0), sp.diff(th, t, 2))
print("theta'' solved from Euler-Lagrange:")
for s in thdd:
    print("   ", sp.simplify(s))

claim = (g - A * w**2 * sp.cos(w * t)) * sp.sin(th) / l
print("claimed theta'' =", claim)

assert len(thdd) == 1, "unexpected number of solutions"
resid = sp.simplify(sp.expand_trig(sp.simplify(thdd[0] - claim)))
print("residual (solved - claimed) =", resid)
print("CHECK N1:", "PASS" if resid == 0 else "FAIL")

# --- a deliberately wrong claim, to show the check can fail -----------------
# If the check cannot reject a wrong equation it is worth nothing, so run it
# against one.  The mutant has the driving term with the wrong sign.
mutant = (g + A * w**2 * sp.cos(w * t)) * sp.sin(th) / l
resid_mutant = sp.simplify(sp.expand_trig(sp.simplify(thdd[0] - mutant)))
print("residual against sign-flipped mutant =", resid_mutant)
print("MUTANT REJECTED:", "yes" if resid_mutant != 0 else "no -- the check is vacuous")

# --- the A -> 0 limit ------------------------------------------------------
print("A -> 0 limit of theta'':", sp.simplify(thdd[0].subs(A, 0)))
