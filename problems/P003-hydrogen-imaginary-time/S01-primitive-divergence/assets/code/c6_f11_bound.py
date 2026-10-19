# C6 (round 2, for finding F1.1): the bound on the bound-state sum in (C5).
# Environment: Python 3.13.16, mpmath 1.3.0. Deterministic.
#
# Claim (answer section C.3, as amended for F1.1):
#   S(tau) = sum_{n>=1} exp(tau/(2 n^2)) / (pi n^3)  <=  exp(tau/2) * zeta(3) / pi    for every tau > 0,
# because 1/n^2 <= 1 for n >= 1 and exp is increasing, so exp(tau/(2n^2)) <= exp(tau/2) term by term.
# Also: as tau -> 0 both sides tend to zeta(3)/pi, so the ratio S/bound -> 1 (the bound is sharp there),
# and the n = 1 term alone already exceeds a fraction 1/zeta(3) ~ 0.83 of the bound.
# Declared failure (before running): any tau with S > bound (relative excess > 1e-25 at 30 digits),
# or a ratio S/bound that does not approach 1 as tau -> 0 (|ratio - 1| > 1e-5 at tau = 1e-6).
import mpmath as mp
mp.mp.dps = 30
fails = []
print(" tau        S(tau)                       e^{tau/2} zeta(3)/pi          S/bound")
for tau in ('1e-6', '0.01', '0.5', '1', '2', '4', '10', '40'):
    t = mp.mpf(tau)
    S = mp.nsum(lambda n: mp.exp(t / (2 * n**2)) / (mp.pi * n**3), [1, mp.inf])
    B = mp.exp(t / 2) * mp.zeta(3) / mp.pi
    r = S / B
    print(f" {tau:<10} {mp.nstr(S, 20):<28} {mp.nstr(B, 20):<28} {mp.nstr(r, 12)}")
    if S > B * (1 + mp.mpf('1e-25')):
        fails.append(("bound", tau))
    if tau == '1e-6' and abs(r - 1) > mp.mpf('1e-5'):
        fails.append(("limit", tau))
print("FAILURES:", fails if fails else "none")
