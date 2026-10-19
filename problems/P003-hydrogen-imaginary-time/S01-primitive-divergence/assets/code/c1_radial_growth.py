# C1: single-bead radial integral with an inner cutoff, against the predicted growth law.
# Environment: Python 3.13.16, mpmath 1.3.0. Deterministic (no random numbers).
#
# Quantity (from the bead integral, potential factor exp(-dtau*V) with V = -1/r, a = dtau):
#     I(eta) = 4*pi * int_eta^eps r^2 exp(a/r) dr          (integrated in r, directly)
# Predictions under test (derived in the answer, eqs. (B4)-(B6)):
#     lower bound      I(eta) >= (2*pi*a^3/3) * ln(eps/eta)          for all 0 < eta < eps
#     leading law      I(eta) ~ 4*pi*eta^4*exp(a/eta)/a              as eta -> 0
#     first correction (I/L1 - 1)/(eta/a) -> 4
#     three-term law   I/L3 - 1 = O((eta/a)^3), L3 = 4*pi*a^3*e^{a/eta}[(eta/a)^4 + 4(eta/a)^5 + 20(eta/a)^6]
# Declared failure (before running):
#     F1 any lower-bound violation;
#     F2 |I/L1 - 1| > 0.05 at the largest a/eta (=160) for any a;
#     F3 (I/L1 - 1)/(eta/a) outside [3.6, 4.4] at a/eta = 160;
#     F4 |I/L3 - 1| > 200*(eta/a)^3 at a/eta >= 40 (the next term predicts ~120*(eta/a)^3).
# Contrast: the ratio to a wrong law eta^3*exp(a/eta) is printed to show the check can tell powers apart.
import mpmath as mp

mp.mp.dps = 50
eps = mp.mpf(1)
fails = []

def I_direct(a, eta):
    a = mp.mpf(a); eta = mp.mpf(eta)
    w = eta**2 / a  # width of the region where exp(a/r) is within a factor e of its maximum
    pts = [eta] + [eta + k * w for k in (1, 3, 10, 30, 100, 300, 1000) if eta + k * w < eps] + [eps]
    return 4 * mp.pi * mp.quad(lambda r: r**2 * mp.exp(a / r), pts)

print("a     a/eta   eta            I(eta)            I/L1          (I/L1-1)/(eta/a)   I/L3-1          bound_ok  I/(eta^3 e^{a/eta})")
for a in (mp.mpf('0.5'), mp.mpf(1), mp.mpf(2)):
    for q in (2, 5, 10, 20, 40, 80, 160):
        eta = a / q
        if eta >= eps:
            continue
        I = I_direct(a, eta)
        x = eta / a
        L1 = 4 * mp.pi * eta**4 * mp.exp(a / eta) / a
        L3 = 4 * mp.pi * a**3 * mp.exp(a / eta) * (x**4 + 4 * x**5 + 20 * x**6)
        lb = (2 * mp.pi * a**3 / 3) * mp.log(eps / eta)
        ok = I >= lb
        if not ok:
            fails.append(("F1", float(a), q))
        r1 = I / L1
        c1 = (r1 - 1) / x
        r3 = I / L3 - 1
        wrong = I / (eta**3 * mp.exp(a / eta))
        print(f"{float(a):<5} {q:<7} {mp.nstr(eta,8):<14} {mp.nstr(I,10):<17} {mp.nstr(r1,10):<13} {mp.nstr(c1,8):<18} {mp.nstr(r3,6):<15} {str(ok):<9} {mp.nstr(wrong,6)}")
        if q == 160:
            if abs(r1 - 1) > 0.05:
                fails.append(("F2", float(a), q))
            if not (3.6 <= c1 <= 4.4):
                fails.append(("F3", float(a), q))
        if q >= 40 and abs(r3) > 200 * x**3:
            fails.append(("F4", float(a), q))

print("FAILURES:", fails if fails else "none")
