# Coverage — check_numeric.py (final)

Runs: round 1, run 2 -> check_numeric.round1.out; round 2 -> check_numeric.round2.out (identical except the script path in two stderr warnings).

The text below is quoted from the solver's own coverage notes (answers/answer-2.md §4.3 unless stated). /log adds nothing to them. Where the answer gives no 'would not catch' half, that absence is recorded rather than filled in.

N1 ($\langle V\rangle_u$ closed forms against quadrature of (4), 150 random draws per potential, including $u/\tau=10^{-4}$ and $1-10^{-4}$). This is a numerical check of (5)–(6) and of the Gaussian-moment formulas, independent of S1. Would catch errors in either. Would not catch anything about $d>1$.

N2 (weighted free random walks). Tests (16), the marginal at bead time $t_j=j\tau/m$. Inputs: only $\rho_0$ (used as importance weight) and the definition of the bridge, not (5). Would catch a wrong bead time. For instance, $t_j=(j-\frac12)\varepsilon$ shifts the mean by $|\Delta|/2m\approx0.022$, which changes $\langle\cos2y\rangle$ by up to about 0.04, against standard errors of about 0.002. Would not catch anything about $d>1$ or the continuum limit.

N3 (finite-$m$ inequality (17) on a grid; quadrature converged, with h versus h/2 differences of order $3\times10^{-15}$). Would catch a violation of (17), such as from a mis-applied Jensen step or badly wrong bead marginals. Would not catch a valid but looser bound, which also passes. It does not test the $m\to\infty$ limit.

N4 ((18) against Mehler on a 121×121 grid at eight values of $\tau$ from 0.05 to 10). Would catch any violation of $(\ast)$ at grid points. Would not catch off-grid behaviour, nor a looser bound; N4b addresses the latter.

N4b (sharpness: $-\ln(R/K)$ against (26) and (30)). Would catch a wrong leading coefficient, e.g. $1/24$ would make $(-L)/P_1\to2$, and a wrong next order for the oscillator. Would not catch the $\nabla^3V$ terms.

N5 (DVR validation against $\rho_0$ and Mehler, to about $10^{-11}$). Would catch DVR errors, including a wrong kinetic matrix (the Colbert–Miller form is used from memory, `[R]`, and is validated here rather than trusted). Would not catch DVR errors specific to non-quadratic potentials. Spectral accuracy for smooth $V$ is the argument; validation on two different potentials is the evidence.

N5b (cosine, coefficients $a$ and $b$ at $\Delta=0$). Would catch errors in (26) and (29) for a non-quadratic potential, including the $V'V'''/30$ term. Would not catch the $\Delta$-dependent terms (N8).

N5c ((18) for the cosine at $\tau$ from 0.2 to 4). Would catch violations in the tested region. Would not catch anything off-grid.

N6a ((37) against a grid evaluation of (21)). Would catch algebra errors in (37). Would not catch errors in (12), which both evaluations use; (12) is checked by S5 and N1.

N6b ($\hat Z_m\le Z$; $m^2(1-\hat Z_m/Z)\to A$; three values of $\beta$; $m$ up to 2048). Would catch a wrong order in $1/m$, since $m^2(1-\hat Z/Z)$ would diverge or vanish, and a wrong coefficient in (35)–(36). Would not catch anything about non-Gaussian $V$. The `[?]` tail issue in (34) is benign for the oscillator.

N7a ((44) against Monte Carlo and two-dimensional numerical quadrature). Would catch errors in (44). Would not catch errors in the $u$-integration (N7b).

N7b ((46), including equality at the origin). Would catch errors in (45)–(46). Would not catch a failure of (47) itself: no exact Coulomb kernel was computed (open question).

N7c (monotone convergence (42) at the origin). Would catch non-monotonicity or a wrong limit. Would not catch problems in the operator convergence (41).
