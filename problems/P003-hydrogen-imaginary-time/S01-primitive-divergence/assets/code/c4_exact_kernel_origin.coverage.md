# Coverage note — c4_exact_kernel_origin.py

Check: C4 [N]. The exact kernel at the origin, by two independent routes, (C5). Full discussion, with the verbatim code and output, in `answers/answer-2.md` §4.2.

Required by `CONVENTIONS.md` §1.1: a check with no stated blind spot has not been thought about. The text below is reproduced verbatim from the answer, so that this file can be read on its own.

Output: `c4_exact_kernel_origin.out` in this directory. Run twice in round 1 and once in round 2, with the code unchanged; all three outputs are byte-identical (compared with `cmp`). The `.out` file is the round-2 output.

---

What it tests. Route (i) evaluates the closed form (C5), whose inputs are recalled spectral data. Route (ii) uses only the problem's Hamiltonian: it discretises the $l=0$ radial operator $-\frac12u''-u/r$ on $(0,R_{\rm box})$ by second-order finite differences, diagonalises it, and assembles $\frac1{4\pi}\sum_ie^{-\tau E_i}u_i'(0)^2$. A control run with $V=0$ must reproduce $(2\pi\tau)^{-3/2}$. Three grid spacings are used, plus a box-size test, and the lowest three box eigenstates are compared with the recalled bound-state data.

What it would have caught.

- A wrong Sommerfeld factor. The repulsive form, for example, gives a continuum term orders of magnitude too small at small $k$.
- A wrong bound-state density at the origin.
- A missing factor $4\pi$ or $(2\pi)^3$.
- A wrong finite-difference normalisation (control G1).
- A kernel that diverged at the origin: route (ii) would then fail to converge in $h$.
- A box-size artifact (G5).

What it would not have caught. Finiteness at points other than the origin; off-diagonal elements; the general theorem cited in C.3. Both routes also assume that the $l=0$ sector carries all the weight at $r=0$. That holds because $R_{nl}(0)=0$ for $l\ge1$, and the same is true of the continuum partial waves [R].

Assumptions.

- [A] In route (ii), the $l=0$ sector of the self-adjoint $H$ corresponds to the boundary condition $u(0)=0$. The radial operator is limit-circle at $r=0$, and $u(0)=0$ selects the regular solution, which is the one corresponding to $H^2$ functions [R]. Agreement with route (i), whose inputs are the spectral data of the three-dimensional $H$, supports this.
- [A] $u'(0)$ is taken from the one-sided second-order formula $(4u_1-u_2)/2h$, which is valid for $u$ smooth at 0 (for example $u_{1s}\propto re^{-r}$).
- Eigenpairs above $E=120$ are dropped. The bound on the dropped part, below $10^{-19}$, is stated in the script.

Outcome. All criteria pass.

- The observed convergence order is 1.96 to 1.99.
- After Richardson extrapolation, routes (i) and (ii) agree to $5\times10^{-7}$ relative or better at all four $\tau$.
- The free control converges at second order; at the finest grid its error is between $1.6\times10^{-5}$ ($\tau=4$) and $1.3\times10^{-4}$ ($\tau=0.5$).
- The box bound states reproduce $E_n=-1/(2n^2)$ to $3\times10^{-6}$, and $1/(\pi n^3)$ to $3\times10^{-4}$, for $n=1,2,3$.
