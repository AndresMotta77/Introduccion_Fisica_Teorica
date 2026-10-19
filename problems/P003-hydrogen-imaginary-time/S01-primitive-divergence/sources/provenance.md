# Provenance ledger — P003.S01

One row per tagged claim in `answers/answer-2.md`, built from the tags in the text rather than from its Sources section. This is the file that answers "did the model derive this or recall it".

Tag meanings are in `templates/CONVENTIONS.md` §1. A claim is load-bearing if the result in `final/final.md` §5 changes when the claim is wrong. Equation numbers are those of `answers/answer-2.md`, which `final/final.md` keeps.

## Summary

| Tag | Rows | Meaning |
|:--|:--|:--|
| `[D]` | 27 | Derived in the document from premises stated in it |
| `[A]` | 5 | Assumption, definition or convention |
| `[S]` | 1 | Standard result invoked with a locator, not retrieved |
| `[V]` | 7 | Checked against a source retrieved this session |
| `[R]` | 11 | Recalled; no locator confirmed |
| `[N]` | 6 checks (C1–C6) plus the failed C5 run 1 | Numerical or symbolic computation |
| `[?]` | 0 | — |

Load-bearing items that are not `[D]` are the three below. All three are in the Risk register.

- The definition [A1].
- The Trotter-formula statement (C8)–(C9), `[V]` through secondary sources only; Reed–Simon itself is `{ver: no}`.
- The kernel theorem in C.3, `[S]` `{ver: no}`, which the retrieved Broderix–Hundertmark–Leschke abstract supports.

Two `[R]` entries are not in the Risk register: the proton radius in §4.1 item 6, and "$R_{nl}(0)=0$ for $l\ge1$" in C4's coverage note. Neither is load-bearing. Together they are why the `no_unflagged_recall` gate fails; see `meta.yaml`.

## Derived claims — `[D]`

| Eq. / § | Claim | Source | Locator | Checked by | Load-bearing |
|:----|:--------------------|:--------|:---|:-------|:----|
| (A1) | Trace in the position representation, with the identity inserted between factors (formal for this $V$) | this document | — | — | yes |
| (A2) | One-slice matrix element $=\rho_0(\mathbf r_{j+1},\mathbf r_j;\Delta\tau)\,e^{\Delta\tau/r_j}$; potential at the right-hand point | this document; free kernel from prompt0 §3a | — | C2 (its $N=2$ integrand) | yes |
| (A3) | Primitive trace as a $3N$-dimensional bead integral with prefactor $(2\pi\Delta\tau)^{-3N/2}$ | this document | — | none; the prefactor is a declared blind spot (§6) | yes |
| (A4) | The same formula in the notes' units | this document | — | — | no |
| Part A | Cyclic invariance of the bead labels; independence from the factor order in $T$ | this document | — | — | no (used to single out bead 1) |
| (B1) | $e^x\ge x^3/6$ for $x\ge0$ | this document | — | C1 (lower-bound column) | yes |
| (B2)–(B3) | $I_a(\eta,\varepsilon)\ge(2\pi a^3/3)\ln(\varepsilon/\eta)$, so $\int_{B_\varepsilon}e^{a/r}d^3r=\infty$ | this document | — | C1 | yes |
| (B4)–(B6) | Growth law $I_a\simeq4\pi\eta^4e^{a/\eta}/a\,[1+4\eta/a+20(\eta/a)^2+\dots]$, with remainder bound | this document | — | C1 | no (quantitative; the divergence rests on (B3)) |
| (B7)–(B9) | Restricted-domain lower bound on the Gaussians, so $Z_N=+\infty$ for every $N\ge1$ and $\Delta\tau>0$ | this document | — | none directly; C2 covers the $N=2$ cut integral | yes |
| B.2 | Localised forms: $Z_N^{(L)}=\infty$ for every $L$; $\rho_N(\mathbf r,\mathbf r')=\infty$ for $N\ge2$; $\rho_1$ not locally integrable at $\mathbf r'=0$ | this document | — | — | yes (part (c) comparison) |
| (B11) | Inside a bounded region with a neighbourhood of the origin removed for every bead, the integral is finite | this document | — | — | yes (identifies the region) |
| (B12) | Composition law of free kernels, by completing the square | this document | — | C3 (symbolic and numerical) | yes (for (B13)) |
| (B13) | $Z_N\ge\int d^3r_1(2\pi\beta)^{-3/2}=\infty$: the large-volume divergence | this document | — | C3 (input only) | yes |
| B.5 | Kinetic weight is maximal when the beads coincide, and positive at $\mathbf r_j=0$ for fixed neighbours | this document | — | — | yes |
| (B14)–(B16) | With a cutoff, $Z_N^{(L)}(\eta)\simeq(2\pi\Delta\tau)^{-3N/2}(4\pi\eta^4e^{\Delta\tau/\eta}/\Delta\tau)^N$ | this document | — | C2 ($N=2$ only) | no (sharpening) |
| (B17) | Angular identity $16\pi^2e^{-(r_1^2+r_2^2)/\Delta\tau}\sinh\kappa/\kappa$ | this document | — | C2(a), Monte Carlo | no |
| (B18) | $1-R\simeq(2\eta^2/\Delta\tau)(1+2\eta/\Delta\tau)$ at $N=2$ | this document | — | C2(b) | no |
| B.6 | $D(T^N)=\{0\}$ for $N\ge2$; $T$ unbounded | this document (uses an `[R]` identity theorem) | — | none | no |
| (C1)–(C3) | $\sup_{\mathbf x}f_\delta(\mathbf x)\le4\pi\delta$ by AM–GM and the bathtub comparison, so $-1/r\in K_3$ | this document | — | C5 | yes (hypothesis of the C.3 theorem) |
| (C4)–(C5) | Explicit $K_\tau(\mathbf 0,\mathbf 0)$ from bound-state and continuum data at the origin | this document from `[V]` and `[R]` inputs | — | C4 (two routes) | yes (finiteness at the origin) |
| C.3, below (C5) | The bound-state sum is at most $e^{\tau/2}\zeta(3)/\pi$ (step added for F1.1) | this document | — | C6 | no (C4 route (ii) is independent) |
| C.3, below (C5) | The continuum integrand behaves like $k$ at 0 and like $k^2e^{-\tau k^2/2}/2\pi$ at $\infty$; free limit recovered | this document | — | C4 (control G1) | yes |
| (C6) | Jensen: $\langle\varphi,e^{-\beta H}\varphi\rangle\ge e^{-\beta\langle\varphi,H\varphi\rangle}$ | this document (uses `[R]` functional calculus) | — | none | yes (for (C7)) |
| (C7) | $\operatorname{Tr}e^{-\beta H}=+\infty$, from translated orthonormal test states | this document | — | none | yes |
| C.6 table | Hypotheses (i) and (ii) hold for $K$, $V$; (iii) fails for $V$ | this document from C.1 | — | — | yes |
| C.6 | Real-time formula (C8) holds; approximants are unbounded, and for $N\ge2$ defined only on the zero vector | this document | — | — | yes |
| Part D | Assessment of H1–H6 | this document, from the notes | notes pp. 4–9 | read against the PDF | yes (deliverable) |

## Assumptions — `[A]`

| Where | Assumption | What fails if it is wrong | Load-bearing |
|:---|:------------|:----------|:---|
| [A1], Part A | (A3), the bead integral, is the definition of $Z_N$ | If an operator trace was meant, it does not exist (B.6), and (b) only strengthens | yes |
| C2 | Two independent, uniformly distributed directions have $\cos\theta_{12}$ uniform on $[-1,1]$ | (B17) would be wrong; the Monte Carlo in C2(a) does not rely on it | no |
| C3 | $s,t>0$ | Nothing physical; imaginary-time steps are positive | no |
| C4 | The $l=0$ boundary condition $u(0)=0$ corresponds to the three-dimensional $H$ (also tagged `[R]`) | Route (ii) would compute another self-adjoint extension; agreement with route (i) argues against this | no |
| C4 | $u'(0)$ from the one-sided second-order formula, valid for $u$ smooth at 0 | Lower-order convergence; the observed order 1.96–1.99 argues against this | no |

## Standard results — `[S]`

| Where | Claim | Source | Locator | Verified | Load-bearing |
|:---|:-------------|:--------|:------|:------|:---|
| C.3 | $e^{-tH}$ has a jointly continuous integral kernel for $V_-\in K_\nu$, $V_+\in K_\nu^{\rm loc}$ | Simon, Bull. AMS 7 (1982) | Theorem B.7.1 | `{ver: no}` (Project Euclid returned a bot-check page) | yes (finiteness at general points) |

## Verified against a retrieved source — `[V]`

| Where | Claim | Source | Locator | Verified | Load-bearing |
|:---|:-------------|:--------|:------|:------|:---|
| C.1 | $V\in L^2+L^\infty(\mathbb R^3)$ is $-\Delta$-bounded with relative bound 0; Kato–Rellich gives self-adjointness on $D(K)$ | Simon, arXiv:1711.00528 (2017) | §7, Theorem 7.3 and the text after eq. (7.15) | `{ver: tool}` (search-result excerpts) | yes ((ii) in C.6) |
| C.2 | Definition of the Kato class $K_d$ | Shen, Illinois J. Math. 45 (2001) | eq. (1.1) | `{ver: tool}` (search-result excerpt) | yes |
| C.3 | Continuous kernel for Kato-class scalar potentials, extending Simon 1982 | Broderix, Hundertmark, Leschke, Rev. Math. Phys. 12 (2000) | abstract; §6 title | `{ver: tool}`; theorem number not reached | yes (supports the `[S]` row) |
| C.3 | $[\psi_n(0)]^2=4\alpha_n^3$, radial normalisation | Fäldt and Wilkin, arXiv:quant-ph/9710049 | §IV, eq. (21); normalisation eq. (3) | `{ver: tool}` | no (C4 route (ii) is independent) |
| C.3 | Sommerfeld factor $2\pi\eta/(e^{2\pi\eta}-1)$, with $\eta=-me^2/\hbar^2k$ for attraction | Fäldt and Wilkin, arXiv:quant-ph/9710049 | §IV, eq. (19); normalisation eq. (4) | `{ver: tool}` | no (same) |
| C.6 | Trotter formula: unitary form if $A+B$ is essentially self-adjoint on $D(A)\cap D(B)$; semigroup form if, in addition, $A$ and $B$ are bounded below | Encyclopedia of Mathematics, "Trotter product formula"; arXiv:2308.00290; arXiv:2501.04564 | entry after eq. (a1); Thm A1.17; Thm B.3.7 (quoting Reed–Simon I, Thm VIII.31) | `{ver: tool}` (secondary sources); Reed–Simon itself `{ver: no}` | yes |
| C.6 | Kato's 1978 product formula requires positive self-adjoint $A$, $B$ | Simon, arXiv:1711.00528 | §18, Theorem 18.2 | `{ver: tool}`, partial (number, title and hypothesis read in excerpts) | no |

## Recalled — `[R]`

| Where | Claim | In Risk register | Load-bearing |
|:---|:-------------|:-----|:-----|
| B.6 | Identity theorem for real-analytic functions | yes | no |
| C.3 | $E_n=-1/(2n^2)$ | yes | no (C4 check G4 reproduces $n=1,2,3$) |
| C.3 | Completeness of the bound states plus Coulomb waves | yes | no (route (i) only) |
| C.4 | Spectral theorem and functional calculus, for (C6) | yes | yes, low risk |
| C.4 | The bound-state sum $\sum_nn^2e^{\beta/2n^2}$ diverges (illustration) | yes (hydrogen spectrum) | no |
| C.6 | Feynman–Kac and Khas'minskii, qualitative remark (Simon 1982, `{ver: no}`) | yes | no |
| Part D, H1 | Ground-state dominance for the diagonal kernel | yes | no |
| §4.1 item 6 | Proton radius about $1.6\times10^{-5}a_0$ | no | no |
| C4 coverage | $R_{nl}(0)=0$ for $l\ge1$, and likewise for continuum partial waves | no | no |
| C4 | Limit-circle at $r=0$; $u(0)=0$ selects the regular solution | yes (as `[A]`/`[R]`) | no |
| C5 | Newton's-theorem closed form for $f_\delta$ | yes | no (used only for comparison) |

## Computations — `[N]`

| Check | Tests | Inputs from | Would not catch | Outcome |
|:---|:--------|:-------|:-------|:------|
| C1 | (B2), (B6) by direct quadrature | the potential factor of the problem | the step from $Z_N$ to one bead; the prefactor; kinetic factors | pass |
| C2 | (B17) by Monte Carlo; (B16) and (B18) at $N=2$ | the $N=2$ integrand of (A3) | $N\ge3$; the large-volume region; the prefactor | pass |
| C3 | (B12), symbolic and quadrature | the free kernel | anything involving $V$ | pass |
| C4 | (C5) against finite-difference diagonalisation; free control; box size; bound states | route (ii) uses only the radial Hamiltonian | points other than the origin; off-diagonal elements | pass |
| C5 run 1 | (C3) bound; [R] Newton formula | definition of $f_\delta$ | — | FAIL against the Newton formula (QUADPACK non-convergence); bound passed |
| C5 run 2 | same, with tanh-sinh quadrature | same | whether $K_3$ is the right hypothesis for the cited theorem | pass |
| C6 | F1.1 bound, including the $\tau\to0$ limit | the sum computed directly | the continuum term; recalled data | pass |
