# Provenance ledger — P003.S02

One row per tagged claim in the final answer (`answers/answer-2.md` = `final/final.md`). The rows are built by /log from the provenance tags in the text, not from the Sources section. Tag meanings follow CONVENTIONS v1.5 §1. "given" marks material supplied in prompt0. The `[A1]`–`[A6]` labels are the answer's `[A]` assumptions. Verification status is carried over exactly as the answer recorded it. "Load-bearing" means that the stated result changes if the claim is wrong. The `[N]` column names the solver's computational checks of the claim, which are evidence, not verification.

Two conventions for the columns:
- Section references such as §3.5.4 and §4.3 are to the answer; U1–U6 and C1–C7 are the answer's Sources entries.
- Restatements of the same items in the answer's Risk register (§7) are not given separate rows.

| Location | Claim | Tag | Source | Locator | Verification | Load-bearing | `[N]` checks |
|---|---|---|---|---|---|---|---|
| (2) | free kernel $\rho_0$ | given | prompt0 §3a | — | trusted (given) | yes | S1–S3 use it as input |
| §2.3 [A1] | $H$ defined as the form sum $K\dotplus V$ | A | — | — | — | yes | — |
| §2.3 [A1] | form sum = closure of $K+V$ on $C_c^\infty$ | R | Reed–Simon II (U4) | Thm X.28 | `{ver: no}`, corroborated (Ichinose 1980; Simon arXiv:1710.06999) | no (identification only) | — |
| §2.3 [A2] | $V$ continuous, $V\ge-c$ | A | prompt0 §1(a) | — | given | yes | — |
| §2.3 [A3] | growth $V\le C_ae^{a\lvert y\rvert^2}$ for all $a>0$ | A | — | — | — | yes (route T; pointwise form of (18)) | — |
| §2.3 [A4] | $V\in C^4$, bounded below, bounded derivatives 1–4 | A | — | — | — | yes ((26)–(35)) | — |
| §2.3 [A5] | $\operatorname{Tr}e^{-\beta H}<\infty$ | A | prompt0 §1(b) | — | given | yes ((22)–(23)) | — |
| §2.3 [A6] | meaning of "free Brownian bridge" (generator $D\nabla^2$) | A | — | — | — | yes | — |
| (3)–(4) | bridge marginal, $\langle V\rangle_u$ through free kernels | D | — | — | — | yes | N1, N2 |
| (5)–(6) | Gaussian marginal: mean $m(u)$, variance $2Du(\tau-u)/\tau$ | D | — | — | — | yes | S1, N1 |
| (7) | Chapman–Kolmogorov | D | — | — | — | yes | S2 |
| (8) | bridge covariance $C(u,v)$ | D | — | — | — | yes | S3 |
| (9) | $z$-substitution form of $\langle V\rangle_u$ | D | — | — | — | yes | — |
| (10) | Lemma J (Jensen, tangent-line form), proved in text | D | (name: Rudin, U6) | Thm 3.3 | `{ver: no}` for the name; proof in text | yes (the inequality); the citation is not | — |
| (11)–(12) | Gaussian-moment examples; $\Phi_\tau$ for the oscillator | D | — | — | — | yes for (d) | S5, N1 |
| (13) | Kato's product formula for form sums | V | Simon, arXiv:1711.00528 (U2); also Reed–Simon I (U3) | Thm 18.2, eq. (18.6), Remark 1; RS I Thm S.21 | `{ver: tool}` (U2); RS I Thm S.21 `{ver: no}` | yes | — |
| (14) | kernel of $T_m$ (Tonelli) | D | — | — | — | yes | N3 |
| (15) | normalized bead density $P_m$ | D | — | — | — | yes | — |
| (16) | marginal of bead $j$ at time $t_j=j\tau/m$ | D | — | — | — | yes | N2 |
| (17) | finite-$m$ Jensen inequality | D | — | — | — | yes | N3 |
| §3.2 T6 | continuity of $u\mapsto\langle V\rangle_u$ by dominated convergence | D (with `[R]` input) | Rudin (U6) | Thm 1.34 | `{ver: no}` | yes | — |
| §3.2 T6 | joint continuity of $K_\tau$ | V | Bodmann–Leschke–Warzel, arXiv:quant-ph/9703031 (U5) | §1.4 | `{ver: tool}` | yes (pointwise form) | — |
| (18) | inequality $(\ast)$ | D | — | — | — | yes | N4, N5c |
| §3.2 remark | removing [A3] within route T by truncation and monotone convergence of forms | ? | Simon, J. Funct. Anal. 28, 377 (1978) | none (bibliography entry only) | `{ver: no}` | no | — |
| (19) | Feynman–Kac, bridge form | V | Simon, arXiv:math-ph/9907022 (U1) | Thm 1.1, eqs. (1.1)–(1.2) | `{ver: tool}` | yes | — |
| §3.3 F2 | dilation to general $D$ | D | — | — | — | yes | — |
| (20) | Tonelli: $\mathbb ES=\Phi_\tau$ | D | — | — | — | yes | — |
| §3.3 end | (18) at every point without [A3] | ? | Bodmann–Leschke–Warzel (U5) | §1.4 | `{ver: tool}` (explicit only for $-\gamma/\lvert q\rvert$) | no (super-Gaussian $V$ only) | — |
| §3.4 | positivity uses P1–P5 | D | — | — | — | yes | — |
| (21) | bead integral $\hat Z_m$ | D | — | — | — | yes | N6a |
| (22) | $\operatorname{Tr}e^{-\beta H}$ as a bead integral of exact kernels | D (with `[R]` input) | Reed–Simon I (U3) | Thm VI.23 | `{ver: no}` | yes | — |
| (23) | $\hat Z_m\le\operatorname{Tr}e^{-\beta H}$ | D | — | — | — | yes | N6b |
| (24) | trapezium rule gives the kernel of $e^{-\tau V/2}e^{-\tau K}e^{-\tau V/2}$ | D | — | — | — | yes | S5 (endpoint limits) |
| (25) | $\delta=\ln\mathbb Ee^{-Y}$ | D | — | — | — | yes | — |
| (25a) | tilted-variance representation; $\delta\ge0$ | D | — | — | — | yes | — |
| (25a) | differentiation under $\mathbb E$ (exponential moments of $Y$) | ? | — | — | — | yes (for the rigour of (25a)) | — |
| §3.5.4 | index convention and dictionary (round 2, F1.1) | D | — | — | — | no (notation) | S9 |
| §3.5.4 | decomposition $A_1,\dots,C_3$; covariances; $\kappa_3=O(\tau^5)$ | D | — | — | — | yes | S4, S9 |
| (26) | leading defect $D\tau^3\lvert\nabla V(\bar x)\rvert^2/12$ | D | — | — | — | yes | S7b/S7c, S8, N4b, N5b |
| (26) | remainder $O(D^2\tau^4)$ by power counting | ? | — | — | — | yes (order of the remainder) | N4b, N5b, N8 (numerical $\tau^4$ behaviour) |
| (27) | $\operatorname{Var}Y$ through $O(\tau^4)$, index form | D | — | — | — | no (beyond the leading term) | S9 ($d=2$, exact) |
| (28) | $\delta$ through $O(\tau^4)$, index form | D | — | — | — | no | N8, S9 |
| (29) | $d=1$, $\Delta=0$ reduction | D | — | — | — | no | N5b |
| (30) | oscillator, through $O(\tau^4)$ | D | — | — | — | no | S7b/S7c, N4b |
| (31)–(33) | $\hat Z_m/Z$ as an exact-measure average; cyclic symmetry; thermal marginal | D | — | — | — | yes | — |
| (34) | $\mathbb E_{\rm ex}\delta=\frac{D\tau^3}{12}\langle\lvert\nabla V\rvert^2\rangle_\beta+O(\tau^4)$ | D | — | — | — | yes | N6b |
| (34) | tail integrability of the remainder | ? | — | — | — | yes (the $O(m^{-3})$ correction) | — |
| (35) | relative error $\frac{D\beta^3}{12m^2}\langle\lvert\nabla V\rvert^2\rangle_\beta$, order $1/m^2$ | D | — | — | — | yes | N6b |
| (36)–(37) | oscillator coefficient $A(\beta)$; circulant $\hat Z_m$ | D | — | — | — | yes for (d) | N6a, N6b |
| (38) | Coulomb $H$ self-adjoint on $H^2$, bounded below (Kato's theorem) | R | Reed–Simon II (U4) | Thm X.15 | `{ver: no}`, corroborated (arXiv:1801.03361 Thm VII.2) | yes | — |
| (38) | $E_*=q^4/4D$ (hydrogen) | R | — | — | `{ver: no}` | no | — |
| (39)–(40) | truncation $V_N$; $(\ast)$ for $V_N$ | D | — | — | — | yes | — |
| (41) | $H^2(\mathbb R^3)\subset L^\infty$ | R | Reed–Simon II (U4) | Thm IX.28 | `{ver: no}`, corroborated (arXiv:1801.03361 Lemma VII.1) | yes | — |
| (41) | common core + pointwise convergence ⇒ strong resolvent convergence | R | Reed–Simon I (U3) | Thm VIII.25(a) | `{ver: no}`, corroborated (arXiv:1912.07325; arXiv:1509.01580) | yes | — |
| (41) | strong resolvent convergence ⇒ $f(H_N)\to f(H)$ for bounded continuous $f$ | R | Reed–Simon I (U3) | Thm VIII.20(b) | `{ver: no}`, corroborated (arXiv:2501.04564; U1) | yes | — |
| (42) | monotone convergence theorem, applied three times | D (with `[R]` input) | Rudin (U6) | Thm 1.26 | `{ver: no}`, corroborated (Irish Math. Soc. Bull. 59) | yes | N7c |
| (43)–(46) | $\langle1/\lvert y\rvert\rangle$ erf formula; bound $\sqrt{\pi\tau/D}$ | D | — | — | — | yes | N7a, N7b |
| (47) | $(\ast)$ for Coulomb, with Coulomb-kernel continuity | D + V | Bodmann–Leschke–Warzel (U5) | §1.4 | `{ver: tool}` | yes | — |
| §3.6 | alternative route: Feynman–Kac directly for $-\gamma/\lvert q\rvert$ | V | Bodmann–Leschke–Warzel (U5) | §1.4 | `{ver: tool}` | no | — |
| §3.6 | primitive approximant infinite for Coulomb | D | — | — | — | no | — |
| §3.6 | (b) estimate does not apply (three reasons) | D | — | — | — | yes (answer to (c)) | — |
| §3.6 | $\operatorname{Tr}e^{-\beta H}=\infty$ for Coulomb on $\mathbb R^3$ | R | — | — | `{ver: no}` | no | — |
| (48) | $\delta(0,0;\tau)=\frac{q^4\tau}{4D}\operatorname{Var}X+O(\tau^{3/2})$ | D | — | — | — | partly (supports "not $O(\tau^3)$") | — |
| (48) | exponential moments of $X$ (Khas'minskii) | ? / R | — | — | `{ver: no}` | partly | — |
| (49) | $m^{-3/2}$ law in a confined setting | ? (heuristic) | — | — | — | no | — |
| (50) | Mehler kernel | D/N | verified symbolically (S6) | — | PDE and initial condition checked; uniqueness `[R]` | yes for (d) | S6 |
| (51) | large-$\tau$ asymptotics at the origin | D | — | — | — | no | N4 |
| §4.2 | assumptions inside the code (positivity of symbols, windows, grids) | A | — | — | — | yes (checks) | — |
| §4.3 S6 | uniqueness of the heat-kernel solution | R | — | — | `{ver: no}` | no | — |
| §4.3 N5 | Colbert–Miller sinc-DVR kinetic matrix | R | Colbert & Miller (C6) | none | `{ver: no}`; validated numerically (N5) | no | N5 |
| §4.3 S9 | Stein's identity $\mathbb E[x_if]=\Sigma_{ij}\mathbb E[\partial_jf]$ | D | — | — | — | no (inside the check) | S9 self-test |
| §6 | comparison with the Takahashi–Imada correction | consulted | Takahashi & Imada (C1) | abstract | `{ver: tool}` | no | — |
| §9 item 3 | primitive approximant is an upper bound (Golden–Thompson/Araki–Lieb–Thirring) | R | — | none | `{ver: no}` | no | N6 (oscillator only) |

Rows that bear on a gate:
- The last row is an `[R]` that does not appear in the answer's Risk register. It is the failure of `no_unflagged_recall`.
- The §3.2-remark row cites a paper with no locator. Together with Sources entries C2, C5 and C6, it is the failure of `general_refs_resolved`. C5 is Feynman & Hibbs "ch. 11" and Feynman "ch. 3", which are also cited in the Prior-knowledge declaration, now in `sources/independence.md`.
