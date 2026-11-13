#### C: `check_c.py` — spectra `[N]`

What it tests.
- C1 diagonalises the kernels (9) and $e^{-\tau x^2/4}\rho_0e^{-\tau x'^2/4}$ on uniform grids at nine $\tau$ values, including $\tau>\sqrt6$ and $\tau=\sqrt6$. It compares the eight largest-magnitude eigenvalues, with signs, against (23) and (24), at grid spacing $h$ and $h/2$. Failure: error $>10^{-10}\lambda_0$.
- C2 rebuilds the kernel from the claimed $\lambda_0$, $q$, $\kappa$ via Mehler's formula (DLMF 18.18.28). This is an analytic identity independent of the grid and of the generating-function argument. It also does an explicit 60-term spectral sum at $\tau=5$, where $q<0$.
- C3 compares $\iint w^2$ on a grid with $\sum\lambda_n^2$; agreement means no eigenvalue is missing.
- C4 tests relation (29): $\operatorname{Tr}(hW)^m$ on the grid against the closed forms (18), (19), at nine $(\beta,m)$ pairs, including odd $m$ with $\tau>\sqrt6$.
- C5 extracts the small-$\tau$ coefficients of (27), (28) from grid eigenvalues alone.
- C6 checks $E_0\ge\tfrac12$.

What it would catch: any wrong eigenvalue, sign or degeneracy among the first eight levels; a missing part of the spectrum (C3); a wrong relation between (b) and (c) (C4); wrong leading series coefficients, including their $n$-dependence (C5).

What it would not catch: errors in (9) itself, since the grid uses the closed form of (a) (covered by `check_a.py` and S1). Nor eigenvalues beyond the first eight in C1; the higher ones are covered collectively by C2 and C3. C2 uses the norm $\|H_n\|^2 = 2^nn!\sqrt\pi$ only in the explicit 60-term sum, and that norm is `[R]` (not retrieved); a wrong norm would make that line fail rather than pass.
