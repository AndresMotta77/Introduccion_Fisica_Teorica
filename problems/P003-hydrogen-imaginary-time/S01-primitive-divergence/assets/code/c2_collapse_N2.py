# C2: do the kinetic factors compensate? N = 2 primitive bead integral with an inner cutoff eta on both
# beads and both beads confined to |r| < L.
# Environment: Python 3.13.16, numpy 2.5.3, mpmath 1.3.0. Seed fixed below.
#
# From the bead integral (answer eq. (A3)) at N = 2, the two links give |r2-r1|^2/(2 dtau) twice, so
#   Z2(eta) = (2 pi dtau)^(-3) * int_{eta<|r1|,|r2|<L} d^3r1 d^3r2 exp(-|r1-r2|^2/dtau + dtau/r1 + dtau/r2).
# Angular integration (answer eq. (B12)), valid for independent uniform directions:
#   int dOmega1 dOmega2 exp(-|r1-r2|^2/dtau) = 16 pi^2 exp(-(r1^2+r2^2)/dtau) sinh(k)/k,  k = 2 r1 r2/dtau.
# Part (a) tests that angular identity by Monte Carlo over random directions (independent of the closed form).
# Part (b) computes R(eta) = Z2(eta) / [ (2 pi dtau)^(-3) I(eta)^2 ],  I(eta) = 4 pi int_eta^L r^2 e^{dtau/r} dr,
#   i.e. the full N = 2 integral divided by what it would be if the kinetic factor were replaced by its maximum.
# Predictions (answer eqs. (B13)-(B15)):  R <= 1 for every eta;  R -> 1 as eta -> 0;
#   (1 - R)/(2 eta^2/dtau) -> 1, with a first correction of about +2 eta/dtau.
# Declared failure (before running):
#   Fa  any Monte Carlo deviation larger than 5 standard errors;
#   Fb1 R > 1 + 1e-12 for any eta;
#   Fb2 1 - R not decreasing as eta decreases;
#   Fb3 (1 - R)/(2 eta^2/dtau) outside [0.95, 1.10] at the smallest eta (prediction ~1.025).
# What would count as "the kinetic factor compensates": R -> 0 as eta -> 0.
import numpy as np
import mpmath as mp

rng = np.random.default_rng(20261019)
fails = []

# ---------- (a) Monte Carlo test of the angular identity ----------
def unit_vectors(n):
    v = rng.normal(size=(n, 3))
    return v / np.linalg.norm(v, axis=1, keepdims=True)

n = 400_000
print("(a) angular average <exp(k cos theta)> over independent uniform directions vs sinh(k)/k")
for k in (0.01, 0.5, 2.0, 5.0):
    u, w = unit_vectors(n), unit_vectors(n)
    vals = np.exp(k * np.sum(u * w, axis=1))
    est, se = vals.mean(), vals.std(ddof=1) / np.sqrt(n)
    exact = np.sinh(k) / k
    z = (est - exact) / se
    print(f"  k={k:<5} MC={est:.6f} +- {se:.2e}   sinh(k)/k={exact:.6f}   z={z:+.2f}")
    if abs(z) > 5:
        fails.append(("Fa", k))

# ---------- (b) the N = 2 integral ----------
mp.mp.dps = 30
dtau, L = mp.mpf(1), mp.mpf('1.5')

def pts(eta):
    w = eta**2 / dtau
    return [eta] + [eta + k * w for k in (1, 3, 10, 30, 100, 300, 1000) if eta + k * w < L] + [L]

def g(r1, r2):  # angular average of the kinetic factor, divided by 16 pi^2
    k = 2 * r1 * r2 / dtau
    return mp.exp(-(r1**2 + r2**2) / dtau) * mp.sinh(k) / k

print("\n(b) R(eta) = Z2 / [(2 pi dtau)^-3 I^2],  dtau = 1, L = 1.5")
print("  eta        R                    1-R                 (1-R)/(2 eta^2/dtau)   predicted ~1+2eta/dtau")
prev = None
for eta in (mp.mpf('0.2'), mp.mpf('0.1'), mp.mpf('0.05'), mp.mpf('0.025'), mp.mpf('0.0125')):
    P = pts(eta)
    wgt = lambda r: r**2 * mp.exp(dtau / r - dtau / eta)          # scaled radial weight
    Iw = mp.quad(wgt, P)                                            # I(eta) / (4 pi e^{dtau/eta})
    J = mp.quad(lambda a, b: wgt(a) * wgt(b) * g(a, b), P, P)       # Z2 / [(2 pi dtau)^-3 16 pi^2 e^{2 dtau/eta}]
    one_minus = mp.quad(lambda a, b: wgt(a) * wgt(b) * (1 - g(a, b)), P, P) / Iw**2
    R = J / Iw**2
    ratio = one_minus / (2 * eta**2 / dtau)
    print(f"  {mp.nstr(eta,5):<10} {mp.nstr(R,16):<20} {mp.nstr(one_minus,10):<19} {mp.nstr(ratio,8):<22} {mp.nstr(1+2*eta/dtau,6)}")
    print(f"             consistency |R + (1-R) - 1| = {mp.nstr(abs(R + one_minus - 1), 3)}")
    if R > 1 + mp.mpf('1e-12'):
        fails.append(("Fb1", float(eta)))
    if prev is not None and not (one_minus < prev):
        fails.append(("Fb2", float(eta)))
    prev = one_minus
    last_ratio = ratio
if not (0.95 <= last_ratio <= 1.10):
    fails.append(("Fb3", float(last_ratio)))
print("FAILURES:", fails if fails else "none")
