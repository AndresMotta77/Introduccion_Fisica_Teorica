# Growth-law figure for the deck. Data: direct quadrature of 4*pi*int_eta^1 r^2 exp(a/r) dr
# (the method of check C1), a = dtau = 0.1, compared with the predicted law and the log lower bound.
import mpmath as mp, numpy as np, matplotlib
matplotlib.use('Agg'); import matplotlib.pyplot as plt
mp.mp.dps = 40
a, eps = mp.mpf('0.1'), mp.mpf(1)
def I(eta):
    w = eta**2 / a
    pts = [eta] + [eta + k*w for k in (1, 3, 10, 30, 100, 300, 1000) if eta + k*w < eps] + [eps]
    return 4*mp.pi*mp.quad(lambda r: r**2*mp.exp(a/r), pts)
q = np.array([1, 2, 5, 10, 15, 20, 30, 40, 50, 60, 70, 80, 90, 100], float)   # a/eta
logI = np.array([float(mp.log10(I(a/mp.mpf(x)))) for x in q])
qq = np.linspace(15, 100, 300)
qb = np.linspace(1, 100, 300)
law = np.array([float(mp.log10(4*mp.pi*(a/mp.mpf(x))**4*mp.exp(mp.mpf(x))/a)) for x in qq])
lb = np.array([float(mp.log10(2*mp.pi*a**3/3*mp.log(eps/(a/mp.mpf(x))))) for x in qb[1:]])
for x, y in zip(q, logI): print(f"a/eta={x:5.0f}  log10 I = {y:8.3f}")
INK, MUTED, GRID, CARD, BLUE, ORANGE = '#14213D', '#5B6678', '#E2DED3', '#FFFDF8', '#1C5CAB', '#EB6834'
plt.rcParams.update({'font.family': 'DejaVu Sans', 'font.size': 15, 'text.color': INK, 'axes.labelcolor': INK,
                     'xtick.color': MUTED, 'ytick.color': MUTED, 'axes.edgecolor': GRID})
fig, ax = plt.subplots(figsize=(7.6, 5.0), dpi=200)
fig.patch.set_facecolor(CARD); ax.set_facecolor(CARD)
ax.grid(True, color=GRID, lw=1); ax.set_axisbelow(True)
for s in ('top', 'right'): ax.spines[s].set_visible(False)
ax.plot(qb[1:], lb, color=MUTED, lw=2, ls=(0, (4, 3)), label=r'lower bound  $(2\pi a^3/3)\,\ln(\varepsilon/\eta)$')
ax.plot(qq, law, color=BLUE, lw=2, label=r'growth law  $4\pi\eta^4 e^{a/\eta}/a$')
ax.plot(q, logI, 'o', ms=8, color=ORANGE, mec=CARD, mew=2, label='direct quadrature', zorder=3)
ax.set_xlabel('a / η   (cutoff closer to the nucleus →)')
ax.set_ylabel('log₁₀ of the one-bead integral')
ax.set_xlim(0, 104); ax.set_ylim(-4, 36)
ax.text(78, 29.5, 'growth law', color=BLUE, ha='right', fontsize=14)
ax.text(101, lb[-1] + 1.4, 'lower bound', color=MUTED, ha='right', fontsize=14)
leg = ax.legend(loc='upper left', frameon=False, fontsize=13)
fig.tight_layout()
fig.savefig('fig_growth.png', facecolor=CARD)
print('saved', fig.get_size_inches()*200)
