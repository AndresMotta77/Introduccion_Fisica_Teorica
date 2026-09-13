#!/usr/bin/env python3
# figures.py  --  P002, figures 1-3
#
# Fig 1  fig1-slow-oscillation.png
#        (a) theta(t) from the exact equation over three slow periods, with the
#            averaged (slow) solution over it;
#        (b) a zoom of three drive periods showing the fast ripple, with the
#            predicted TH + (A/l) sin(TH) cos(w t) over it.
# Fig 2  fig2-stability.png
#        (a) where the inverted position is held, in the (A/l, omega) plane:
#            direct integration of the exact nonlinear equation (markers), the
#            exact Floquet boundary of the linearised equation (solid), and the
#            averaged prediction A^2 w^2 = 2 g l (dashed);
#        (b) theta(t) at three points across the boundary.
# Fig 3  fig3-effective-potential.png
#        the effective potential W(TH) below, at, and above threshold, with the
#        barrier angle TH_c marked.
#
# Environment (pinned): python 3.11.15, numpy 2.4.4, scipy 1.17.1,
# matplotlib 3.10.9.  Deterministic; no random numbers.

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

g, l = 9.81, 1.0
OUT = "."

plt.rcParams.update({
    "font.size": 9, "axes.titlesize": 9.5, "axes.labelsize": 9,
    "figure.dpi": 160, "savefig.dpi": 160, "savefig.bbox": "tight",
    "axes.grid": True, "grid.alpha": 0.25, "grid.linewidth": 0.5,
    "axes.spines.top": False, "axes.spines.right": False,
    "legend.frameon": False, "legend.fontsize": 8,
})

C_EXACT, C_AVG, C_PRED = "#1b3a6b", "#c8102e", "#0f8a5f"


def exact_rhs(t, s, A, w):
    th, thd = s
    return [thd, (g - A * w**2 * np.cos(w * t)) * np.sin(th) / l]


def averaged_rhs(t, s, A, w):
    TH, THd = s
    return [THd, (g / l) * np.sin(TH)
            - (A**2 * w**2 / (2 * l**2)) * np.sin(TH) * np.cos(TH)]


def Omega(A, w):
    v = A**2 * w**2 / (2 * l**2) - g / l
    return np.sqrt(v) if v > 0 else np.nan


# =========================== figure 1 ======================================
A, eps = 0.05, 0.05
w = 2.0 * np.sqrt(2 * g * l) / A            # twice the threshold frequency
Om = Omega(A, w)
Tslow, Tdrive = 2 * np.pi / Om, 2 * np.pi / w
th0 = 0.35

tmax = 3 * Tslow
ts = np.linspace(0, tmax, 200001)
ex = solve_ivp(exact_rhs, (0, tmax), [th0, 0.0], t_eval=ts, args=(A, w),
               rtol=1e-11, atol=1e-13, method='DOP853', max_step=Tdrive / 30)
# the averaged solution is started from the SLOW part of the same initial
# state: theta(0) = TH(0) + (A/l) sin TH(0) at t = 0, so TH(0) solves
# TH + (A/l) sin TH = th0.
TH0 = th0
for _ in range(60):
    TH0 -= (TH0 + (A / l) * np.sin(TH0) - th0) / (1 + (A / l) * np.cos(TH0))
av = solve_ivp(averaged_rhs, (0, tmax), [TH0, 0.0], t_eval=ts, args=(A, w),
               rtol=1e-11, atol=1e-13, method='DOP853')
assert ex.success and av.success

fig, ax = plt.subplots(3, 1, figsize=(6.6, 7.2))
ax[0].plot(ts, np.rad2deg(ex.y[0]), lw=0.6, color=C_EXACT,
           label=r"exact $\theta(t)$")
ax[0].plot(ts, np.rad2deg(av.y[0]), lw=1.6, color=C_AVG, ls="--",
           label=r"averaged $\Theta(t)$")
ax[0].axhline(0, color="k", lw=0.6, alpha=0.5)
ax[0].set_xlabel("t  [s]")
ax[0].set_ylabel(r"$\theta$  [deg]")
ax[0].set_title(
    rf"$l={l:g}$ m, $A={A:g}$ m ($A/l={eps:g}$), $\omega={w:.1f}\,$s$^{{-1}}$"
    rf"$=2\omega_{{\rm c}}$" "\n"
    rf"$\Omega={Om:.3f}\,$s$^{{-1}}$, released from "
    rf"$\theta(0)={np.rad2deg(th0):.1f}^\circ$ at rest")
ax[0].legend(loc="lower center", ncol=2)
ax[0].set_xlim(0, tmax)
ax[0].set_ylim(-34, 30)

# zoom: three drive periods starting at t = 0, where the slow amplitude is at
# its maximum and the ripple is therefore largest
m = ts <= 3 * Tdrive
THz = np.interp(ts[m], ts, av.y[0])
pred = THz + (A / l) * np.sin(THz) * np.cos(w * ts[m])
ax[1].plot(ts[m] * 1e3, np.rad2deg(ex.y[0][m]), lw=1.4, color=C_EXACT,
           label=r"exact $\theta(t)$")
ax[1].plot(ts[m] * 1e3, np.rad2deg(THz), lw=1.4, ls="--", color=C_AVG,
           label=r"averaged $\Theta(t)$")
ax[1].plot(ts[m] * 1e3, np.rad2deg(pred), lw=1.2, ls=":", color=C_PRED,
           label=r"$\Theta+(A/l)\sin\Theta\,\cos\omega t$")
ax[1].set_xlabel("t  [ms]")
ax[1].set_ylabel(r"$\theta$  [deg]")
ax[1].set_title("three drive periods at the turning point: the fast ripple")
ax[1].legend(loc="lower left")

# residual over one slow period, against the predicted envelope
m2 = ts <= Tslow
res = ex.y[0][m2] - np.interp(ts[m2], ts, av.y[0])
env = (A / l) * np.abs(np.sin(np.interp(ts[m2], ts, av.y[0])))
ax[2].plot(ts[m2], np.rad2deg(res), lw=0.5, color=C_EXACT,
           label=r"$\theta(t)-\Theta(t)$")
ax[2].plot(ts[m2], np.rad2deg(env), lw=1.3, color=C_PRED,
           label=r"$\pm (A/l)\,|\sin\Theta(t)|$")
ax[2].plot(ts[m2], -np.rad2deg(env), lw=1.3, color=C_PRED)
ax[2].set_xlabel("t  [s]")
ax[2].set_ylabel(r"$\theta-\Theta$  [deg]")
ax[2].set_title("the ripple over one slow period, against its predicted envelope")
ax[2].legend(loc="lower center", ncol=2)
ax[2].set_xlim(0, Tslow)
fig.tight_layout()
fig.savefig(f"{OUT}/fig1-slow-oscillation.png")
plt.close(fig)
print("fig1 written;  Omega =", Om, " Tslow =", Tslow, " Tdrive =", Tdrive)

# =========================== figure 2 ======================================
TWO_PI = 2 * np.pi


def floquet_trace(G, e):
    def rhs(tau, y):
        f = G - e * np.cos(tau)
        return [y[1], f * y[0], y[3], f * y[2]]
    s = solve_ivp(rhs, (0, TWO_PI), [1.0, 0.0, 0.0, 1.0],
                  rtol=1e-12, atol=1e-14, method='DOP853')
    return s.y[0, -1] + s.y[3, -1]


def floquet_Gc(e):
    lo, hi = 0.0, max(4 * e**2, 1e-8)
    while abs(floquet_trace(hi, e)) < 2.0:
        hi *= 2
    for _ in range(60):
        mid = 0.5 * (lo + hi)
        if abs(floquet_trace(mid, e)) < 2.0:
            lo = mid
        else:
            hi = mid
    return 0.5 * (lo + hi)


def survives(A, w, th0=0.1, tmax=6.0):
    ev = lambda t, s, A, w: abs(s[0]) - 2.5
    ev.terminal, ev.direction = True, 1.0
    s = solve_ivp(exact_rhs, (0, tmax), [th0, 0.0], args=(A, w), rtol=1e-9,
                  atol=1e-11, method='DOP853', max_step=2 * np.pi / w / 10,
                  events=ev)
    return len(s.t_events[0]) == 0


eps_grid = np.linspace(0.02, 0.30, 22)
w_ratio = np.linspace(0.5, 1.6, 22)
pts_ok, pts_no = [], []
for e in eps_grid:
    Aa = e * l
    wc = np.sqrt(2 * g * l) / Aa
    for r in w_ratio:
        (pts_ok if survives(Aa, r * wc) else pts_no).append((e, r))
pts_ok, pts_no = np.array(pts_ok), np.array(pts_no)

eps_fine = np.linspace(0.02, 0.30, 40)
r_floq = np.array([np.sqrt(g / (l * floquet_Gc(e))) / (np.sqrt(2 * g * l) / (e * l))
                   for e in eps_fine])

fig, ax = plt.subplots(1, 2, figsize=(9.2, 3.6),
                       gridspec_kw=dict(width_ratios=[1.15, 1]))
ax[0].scatter(pts_ok[:, 0], pts_ok[:, 1], s=9, c=C_EXACT, marker="o",
              label="stays up (nonlinear, $\\theta_0=0.1$ rad)")
ax[0].scatter(pts_no[:, 0], pts_no[:, 1], s=9, c="#b0b0b0", marker="x",
              label="falls over")
ax[0].plot(eps_fine, r_floq, color=C_PRED, lw=1.6,
           label="exact Floquet boundary")
ax[0].axhline(1.0, color=C_AVG, ls="--", lw=1.6,
              label=r"averaged: $A^2\omega^2=2gl$")
ax[0].set_xlabel(r"$\varepsilon = A/l$")
ax[0].set_ylabel(r"$\omega\,/\,\omega_{\rm c}$,   $\omega_{\rm c}=\sqrt{2gl}/A$")
ax[0].set_title("where the inverted position is held")
ax[0].legend(loc="upper center", bbox_to_anchor=(0.5, -0.22), ncol=2)
ax[0].set_ylim(w_ratio[0], w_ratio[-1])

A2 = 0.05
wc2 = np.sqrt(2 * g * l) / A2
for r, ls, lab in [(1.4, "-", r"$\omega=1.4\,\omega_{\rm c}$: held"),
                   (1.02, "-", r"$\omega=1.02\,\omega_{\rm c}$: marginal"),
                   (0.9, "-", r"$\omega=0.9\,\omega_{\rm c}$: falls")]:
    ww = r * wc2
    tm = 4.0
    tt = np.linspace(0, tm, 40001)
    s = solve_ivp(exact_rhs, (0, tm), [0.1, 0.0], t_eval=tt, args=(A2, ww),
                  rtol=1e-10, atol=1e-12, method='DOP853',
                  max_step=2 * np.pi / ww / 20)
    ax[1].plot(tt, np.rad2deg(s.y[0]), lw=0.9, ls=ls, label=lab)
ax[1].set_xlabel("t  [s]")
ax[1].set_ylabel(r"$\theta$  [deg]")
ax[1].set_title(rf"$A/l={A2:g}$, released from $\theta_0=5.7^\circ$ at rest")
ax[1].legend(loc="upper center", bbox_to_anchor=(0.5, -0.22), ncol=1)
ax[1].set_ylim(-40, 200)
fig.tight_layout()
fig.savefig(f"{OUT}/fig2-stability.png")
plt.close(fig)
print("fig2 written;  n stable =", len(pts_ok), " n fallen =", len(pts_no))

# =========================== figure 3 ======================================
TH = np.linspace(-np.pi, np.pi, 2401)
fig, axs = plt.subplots(1, 2, figsize=(8.6, 3.4),
                        gridspec_kw=dict(width_ratios=[1.5, 1]))
ax, axin = axs
A3 = 0.05
wc3 = np.sqrt(2 * g * l) / A3
for r, c in [(0.7, "#9aa3ad"), (1.0, "#6b7280"), (1.5, C_EXACT), (2.2, C_PRED)]:
    ww = r * wc3
    W = (g / l) * np.cos(TH) + (A3**2 * ww**2 / (4 * l**2)) * np.sin(TH)**2
    W0 = (g / l)                       # W at Theta = 0, exactly
    for a_, lw_ in ((ax, 1.4), (axin, 1.4)):
        a_.plot(np.rad2deg(TH), W - W0, color=c, lw=lw_,
                label=(rf"$\omega={r:g}\,\omega_{{\rm c}}$" if a_ is ax else None))
    q = 2 * g * l / (A3**2 * ww**2)
    if q < 1:
        thc = np.arccos(q)
        Wc = (g / l) * np.cos(thc) + (A3**2 * ww**2 / (4 * l**2)) * np.sin(thc)**2
        ax.plot([np.rad2deg(thc), -np.rad2deg(thc)], [Wc - W0] * 2, "o",
                ms=4.5, color=c)
for a_ in (ax, axin):
    a_.axvline(0, color="k", lw=0.6, alpha=0.4)
    a_.set_xlabel(r"$\Theta$  [deg from upward vertical]")
    a_.set_ylabel(r"$W(\Theta)-W(0)$   [s$^{-2}$]")
ax.set_title(r"effective potential per unit $ml^2$; dots mark $\Theta_{\rm c}$")
ax.legend(loc="lower center", ncol=4, bbox_to_anchor=(0.5, -0.46))
axin.set_xlim(-30, 30)
axin.set_ylim(-0.8, 1.6)
axin.axhline(0, color="k", lw=0.5, alpha=0.4)
axin.set_title(r"detail near $\Theta=0$: the well that holds it up")
fig.tight_layout()
fig.savefig(f"{OUT}/fig3-effective-potential.png")
plt.close(fig)
print("fig3 written")
