#### B: `check_b.py` — partition functions and energies `[N]`

What it tests.
- B1 prints the closed forms and compares the two forms of (21).
- B2 is the second route: for each of the 15 $(\beta,m)$ it builds the $m\times m$ Hessian of the action numerically, by polarisation of $S(x) = -\sum\ln w(x_n,x_{n+1})$, and its $\beta$-derivative by complex-step differentiation. It then evaluates the Gaussian integral and $\hat E_m = \partial_\beta S(0) + \tfrac12\operatorname{tr}(H^{-1}\partial_\beta H)$ with LAPACK. It uses no circulant algebra, no product formula and no analytic derivative. Failure: $|\Delta E|$ or $|\Delta\ln Z|>10^{-8}$.
- B3 checks the analytic derivative (20), (21) against mpmath's numerical derivative of (18), (19).
- B4 checks the two bounds.
- B5 recomputes $\hat Z_m$, $\hat E_m$ from the spectrum (23) via (29), (30).
- B6 tests (31): $m^2\times$ (residual after the $m^{-2}$ and $m^{-3}$ terms) must stay bounded as $m$ doubles.

What it would catch: errors in (12)–(21) (B2, B3), in the relation (29), (30) (B5), or in the asymptotic coefficients (31) (B6).

What it would not catch: errors in (9) (B2 starts from (9); covered by A and S1). B2's accuracy at $\beta=1$, $m=500$ ($6.3\times10^{-9}$ bridge, $8.2\times10^{-9}$ primitive) is limited by the conditioning of $H$ (eigenvalues from $\tau=0.002$ to $4/\tau$). This is adequate for six-decimal claims but would not resolve errors below $10^{-8}$. B6 is a statement about the closed form's asymptotics, not an independent computation of $\hat E_m$.
