# table.py -- prints the markdown table of part (b) from the closed forms (mpmath, 30 digits).
# Python 3.13.18, mpmath 1.3.0.  Run: python3 -I table.py
import mpmath as mp
mp.mp.dps = 30
def Ehat(beta, m):
    beta = mp.mpf(beta); t = beta/m
    k = mp.sqrt(1 + t**2/12); kp = t/(12*k); a, b = k + t/2, k - t/2
    return t/6 + (a**(m-1)*(kp + mp.mpf(1)/2) - b**(m-1)*(kp - mp.mpf(1)/2))/(a**m - b**m)
def Eprim(beta, m):
    t = mp.mpf(beta)/m
    return mp.coth(m*mp.asinh(t/2))/mp.sqrt(4 + t**2)
print("| beta | m | Ehat_m | E_m | exact | Ehat_m - exact | E_m - exact |")
print("|---:|---:|---:|---:|---:|---:|---:|")
for beta in (1, 5, 10):
    ex = mp.coth(mp.mpf(beta)/2)/2
    for m in (1, 10, 50, 100, 500):
        eh, ep = Ehat(beta, m), Eprim(beta, m)
        print(f"| {beta} | {m} | {float(eh):.10f} | {float(ep):.10f} | {float(ex):.10f} | "
              f"{float(eh-ex):+.4e} | {float(ep-ex):+.4e} |")
