# Provenance ledger — P003.S03

One row per tagged claim in `final/final.md`, which is `answers/answer-2.md` with §1 and §10 moved out. Built from the tags in the text, listed by `assets/code/log/extract_tags.py` (output in `extract_tags.out`), not from the Sources section. Equation numbers and sections are those of answer-2. "Verified" records the status the answer gave: `tool` means the locator was retrieved in session, `no` means recall, and `n/a` covers derivations, assumptions and checks. "Load-bearing" says whether a final result in §5 would fall if the claim were wrong.

| Eq. / section | Tag | Claim | Source | Locator | Verified | Load-bearing |
|---|---|---|---|---|---|---|
| (0), §2.3 | [D] | $\langle x\vert e^{-tK}\vert x'\rangle = \rho_0(x,x';t)$, by Fourier inversion and (G) | derived here | — | n/a | yes, for the primitive kernel in (c) |
| (G), §2.3 | [D] | Gaussian integral, real $p>0$ and complex $J$ | derived here | — | n/a | yes |
| §3.1 | [A1] | $y$-integral evaluated for $0<u<\tau$; endpoints have measure zero | assumption | — | n/a | yes (benign: the integrand extends to a polynomial) |
| (2)–(3) | [D] | completing the square, $R = (x-x')^2/\tau$ | derived here | — | n/a | yes |
| (4) | [D] | bridge ratio is the normalised Gaussian $p_u(y)$ | derived here | — | n/a | yes |
| (5) | [D] | $\int p_u\,y^2/2 = (\bar y^2+\sigma^2)/2$ | derived here | — | n/a | yes |
| (6)–(9) | [D] | $u$-integrals; closed form of $w$ | derived here | — | n/a | yes |
| §3.1 remark (after (10)) | [R] | Feynman–Kac plus Jensen give $w\le\rho$, hence $\hat Z_m\le Z$ and $E_0\ge\tfrac12$ | recall | — | no | no (self-checks B4, C6 only) |
| (11)–(12) | [D] | ring action as $\tfrac12x^{\rm T}\hat Ax$ with cyclic shift $P$ and identity $\mathbf 1$; cases $m=1,2$ | derived here | — | n/a | yes |
| (13) | [D] | Gaussian integral over $\mathbb R^m$ by orthogonal diagonalisation | derived here | — | n/a | yes |
| (16) | [D] | $\sqrt C = s_+$, $z = s_-/s_+$ from $\sqrt C(1\pm z)$ | derived here | — | n/a | yes |
| (17)–(18) | [D] | roots-of-unity product; closed form of $\hat Z_m$ | derived here | — | n/a | yes |
| (19a)–(19) | [D] | primitive matrix and $Z_m = [2\sinh(m\operatorname{arcsinh}(\beta/2m))]^{-1}$ | derived here | — | n/a | yes |
| (20) | [D] | $\hat E_m$ | derived here | — | n/a | yes |
| (21) | [D] | $E_m$, both forms | derived here | — | n/a | yes |
| (22), route 2 | [S] | Hermite generating function $e^{2\xi z-z^2} = \sum H_n(\xi)z^n/n!$ | DLMF | §18.12, eq. (18.12.15), read through the MaRDI mirror | tool | route 2 only; route 1 gives the spectrum without it |
| (22), route 2 | [A2] | $\partial_s^n$ under the $x'$-integral (holomorphic parameter integral) | assumption | — | n/a | route 2 only |
| §3.3, completeness | [S] | Hermite expansions converge in $L^2(\mathbb R,e^{-x^2}dx)$ | DLMF, citing Szegő (1975) Thms 3.1.5, 5.7.1 | §18.18(i), eqs. (18.18.6)–(18.18.7) and the $L^2$ paragraph | tool | route 2 only |
| §3.3, route 1 | [D] | spectrum from the power sums $\operatorname{Tr}T^m = \hat Z_m(m\tau)$ | derived here | — | n/a | alternative to route 2 |
| §3.3, route 1 | [R] | $T^m$ trace class for $m\ge2$, $\operatorname{Tr}T^m = \sum\mu_j^m$, trace as an integral of composed kernels | recall | — | no | route 1 and (29); route 2 and checks C4, B5 stand without it |
| (23)–(24) | (untagged) | eigenvalues of $T_\tau$ and $T^P_\tau$ from the lemma | — | — | — | yes (see note 1) |
| (25) | [D] | $E_n(\tau)$ for $\tau<\sqrt6$, both forms | derived here | — | n/a | yes |
| (26) | [D] | regimes $\tau=\sqrt6$ (rank one) and $\tau>\sqrt6$ (sign alternation) | derived here | — | n/a | yes |
| (27), leading terms | [D] | $E_n-(n+\tfrac12) = (2n+1)\tau^2/48 - \tau^3/144 + \dots$, by hand | derived here | — | n/a | yes |
| (27), $\tau^4$–$\tau^6$ | [N] | higher series coefficients from the sympy series (S6) | computation | `assets/code/round-2/check_algebra.py` | n/a (executed) | yes, for the $\tau^4$ and higher coefficients |
| (28) | [D] | primitive levels and series; $\tau^6$ term from S6 | derived here | — | n/a | yes |
| (29)–(30) | [D] | $\hat Z_m = \sum\lambda_n^m$; $\hat E_m$ as an average of $\varepsilon_n = d(\tau E_n)/d\tau$ | derived here | — | n/a | yes |
| (31) | [D] | large-$m$ asymptotics of $\hat E_m$, $E_m$ | derived here | — | n/a | yes |
| (31) | [A3] | small-$\tau$ expansion inside $\sum_n$ | assumption | — | n/a | yes, for (31); checked by B6 |
| §4.3 | [A] | assumptions inside the check code (positivity and reality flags in sympy, trapezoid rule, principal log at real arguments) | assumption | — | n/a | no (checks only) |
| §4.3, check A | [N] | $w$ against quadrature of its definition at 13 points | computation | `assets/code/round-2/check_a.py` | n/a (executed) | no (evidence) |
| §4.3, check C | [N] | grid spectra, Mehler reconstruction, Hilbert–Schmidt norm, traces, small-$\tau$ coefficients, $E_0\ge\tfrac12$ | computation | `assets/code/round-2/check_c.py` | n/a (executed) | no (evidence) |
| §4.3, check C2 | [R] | $\Vert H_n\Vert^2 = 2^nn!\sqrt\pi$ | recall (DLMF Table 18.3.1, not retrieved) | — | no | no |
| §4.3, check B | [N] | second route for (b); derivative, bounds, spectrum route, asymptotics | computation | `assets/code/round-2/check_b.py` | n/a (executed) | no (evidence) |
| §4.3, check P1 | [N] | `\mathbb` misuse scan and compile under the house preamble | computation | `assets/code/round-2/check_p1.py` | n/a (executed) | no (presentation) |
| §6 | [R] | repeated mention of the trace identities (same claim as route 1) | recall | — | no | as above |

Notes.

1. Eqs. (23) and (24), the eigenvalues of (c), carry no tag of their own. They are obtained in the paragraphs "Application to $T_\tau$" and "Application to $T^P_\tau$" by inserting (10) into the lemma. I record them here without inventing a tag.
2. The heading of the S1–S6 checks (`check_algebra.py`, §4.3) has no `[N]` tag, unlike the A, B, C and P1 headings. Its symbolic results are referred to as `[N]` where they are used, at (27).
3. "Executed" means the scripts were run by the solver in rounds 1 and 2. The auditor of round 1 executed no code.
