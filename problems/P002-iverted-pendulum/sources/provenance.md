# Provenance ledger — P002

One row per tagged claim in `answers/answer-2.md`, built from the tags in the
text rather than from the Sources section. This is the file that answers "did
the model derive this or recall it".

Tag meanings are in `templates/CONVENTIONS.md` §1. "Load-bearing" means the
final result in `final/final.md` §Result changes if the claim is wrong.

Equation numbers are those of `answers/answer-2.md`, which `final/final.md`
preserves.

## Summary

| Tag | Count | Meaning |
|:--|:------|:-------------------------------------------------|
| `[D]` | 23 | Derived in the document from premises stated in it |
| `[A]` | 9 | Assumption, convention or ansatz |
| `[N]` | 8 checks + 3 register rows | Numerical or symbolic computation |
| `[V]` | 1 | Checked against a source retrieved this session |
| `[R]` | 2 | Recalled from training, no locator confirmed |
| `[S]` | 0 | — none. Nothing is invoked as a standard result without either deriving it or marking it `[R]`. |
| `[?]` | 1 | Solver not confident |

Nothing load-bearing is `[R]`, `[?]` or `{ver: no}`. The two `[R]` entries are
attributions, not steps: removing both leaves every equation in §3 intact.

## Derived claims — `[D]`

| Eq. / § | Claim | Source | Locator | Verified | Load-bearing |
|:--|:--------------------------------|:------|:----------|:------|:----|
| §2.3 | $\theta\equiv0$ and $\theta\equiv\pi$ are exact solutions of (16) for all $A,\omega$ | this document | — | N1, N2 | yes |
| (10) | The $t$-only group in $L$ is annihilated by $\partial_\theta$ and $\partial_{\dot\theta}$ and may be dropped | this document | — | N1 | yes |
| (15) | The $\dot y_p\dot\theta\cos\theta$ terms cancel identically; only the pivot's acceleration survives | this document | — | N1 | yes |
| (16) | Equation of motion $l\ddot\theta=(g-A\omega^2\cos\omega t)\sin\theta$ | this document | — | N1, N2 | yes |
| (17) | (15) is the pendulum equation with $g\to g_{\rm eff}(t)=g+\ddot y_p$ | this document | — | N2 | no (consistency remark) |
| (17) | $A=0$ reduces to $l\ddot\theta=g\sin\theta$, growth $e^{\omega_0 t}$ | this document | — | N1 | no |
| (20a) | $\mu=2gl/(A^2\omega^2)=\cos\Theta_{\rm c}$; stability is $\mu<1$ | this document | — | N4 | yes |
| §3.3 | Two blocks separated by exactly one factor of $\varepsilon$ | this document | — | N3, N8 | yes |
| §3.3 | All three slow terms are $O(\varepsilon^2\omega^2)$; none may be dropped | this document | — | N4 | yes |
| §3.3 | Ordering inside the slow block degenerates at $\mu=1$ | this document | — | N4, §3.8 | no |
| (24) | $c_1=c_2=0$ in the fast solution | this document | — | N6 | yes |
| (24) | $\xi=(A/l)\sin\Theta\cos\omega t$ | this document | — | N6 | yes |
| (27)–(28) | $\langle\cos\omega t\,\xi\rangle=\tfrac12\varepsilon\sin\Theta$; the averaged equation | this document | — | N3, N8 | yes |
| (32) | The added term of $U_{\rm eff}$ equals the time-averaged kinetic energy of the fast motion | this document | — | algebraic identity, §3.5 | no (internal cross-check) |
| (38) | $W''(\pi)>0$ always; the hanging position is never destabilised at this order | this document | — | self-check 3 | no |
| (39) | $W''(\Theta_{\rm c})<0$: the barrier is a maximum | this document | — | N5 | yes (for $\Theta_{\rm c}$) |
| (43)–(44) | $\Omega/\omega<\varepsilon/\sqrt2$, so the timescale separation follows from $A\ll l$ | this document | — | N3, N8 | yes (non-circularity) |
| (46) | $\beta<0$ always; at threshold $W$ has a quartic maximum, so (37) is strict | this document | — | N4, fig. 3 | yes |
| (53) | Secular removal gives $c_1=\tfrac34\alpha a^2$ | this document | — | N7 | no |
| (56) | $T(a)/T(0)-1=a^2(\tfrac14+3\omega_0^2/16\Omega^2)$, always positive | this document | — | N7, N3 col. (c) | no |
| §4.3 | The analytic size of N3's column (c) is (56) | this document | — | N7 | no |
| (58) | $\det M=1$ exactly, by constancy of the Wronskian | this document | — | printed as $\det M-1\sim10^{-15}$ | yes (for N4, N8) |
| (59) | Linear stability of $\theta=0$ is exactly $|\operatorname{tr}M|<2$ | this document | — | N4 $\varepsilon=0$ block | yes (for N4, N8) |
| §4.4 | $\lambda_\pm=e^{\pm i\nu}$ with $2\cos\nu=\operatorname{tr}M$ defines the Floquet phase | this document | — | N8 | yes (for N8) |

## Verified against a retrieved source — `[V]`

| Eq. / § | Claim | Source | Locator | Verified | Load-bearing |
|:--|:--------------------------------|:------|:----------|:------|:----|
| §4.4, before (59) | Floquet's theorem: one matrix $M$ advances the state over every period | E. Folkers, *Floquet's Theorem*, 2018 | Theorem 2.8 §2.4; Lemma 3.12 §3.4; §3.4 cases 1–3 | `{ver: tool}`, retrieved 2026-09-14; retrieval note in §8 item 7 | no — §4.4 derives $\det M=1$ and the trace criterion independently |

## Recalled — `[R]`

| Eq. / § | Claim | Source | Locator | Verified | Load-bearing |
|:--|:--------------------------------|:------|:----------|:------|:----|
| §8 item 3, register R1 | That the effective-potential method for a rapidly oscillating field is Landau & Lifshitz, *Mechanics*, §30 | Landau & Lifshitz, *Mechanics*, 3rd ed. | §30 claimed, no equation number claimed | `{ver: no}` — book not retrieved | **no**. §3.3–§3.5 derives the averaging from the equation of motion and imports no formula. |
| §4.4, register R3 | Existence and uniqueness for linear ODEs with continuous coefficients | — | none | not verified | **no** for the physics; yes for the applicability of Floquet theory. The coefficient of (57) is entire in $\tau$. |

Both appear in the Risk register, so `no_unflagged_recall` holds. The `[R]` in
§3.9 and the `[S]` in §8 are references to the tags themselves in prose, not
claims: §3.9 says the relation *was* `[R]` in round 1 and is now derived, and §8
says an unconfirmable `[S]` must be downgraded.

## Assumptions — `[A]`

| Eq. / § | Assumption | What it buys | What breaks without it | Load-bearing |
|:--|:--------------------|:--------------|:--------------------|:----|
| §2.1 | $\theta$ measured from the upward vertical | reads naturally for the inverted case | nothing; relabel $\theta\to\pi-\theta$ | no |
| (18) | Two-timescale split $\theta=\Theta+\xi$, $\langle\xi\rangle=0$ | an autonomous slow equation | all of §3.3–§3.6; the threshold survives via N4 | yes |
| (20) | Truncating $\sin(\Theta+\xi)$ at first order in $\xi$ | linearity in $\xi$ | relative error $O(\varepsilon^2)$, measured by N3 | yes |
| (21) | $\Theta$ held fixed over one drive period | closed-form $\xi$ | relative error $O(\varepsilon^2)$, measured by N3 | yes |
| (49) | $\alpha a^2/\Omega^2$ small | closed-form amplitude correction | (56) only; no result in §5 | no |
| §5 item 5 | Massless rigid stick, point mass, frictionless pivot, planar motion, uniform $g$, exactly sinusoidal and exactly vertical drive | the posed problem | a massive stick replaces $l$ by $I/(ml_{\rm cm})$; damping shrinks the basin; a horizontal component breaks the $A\to-A$ symmetry | yes, but all are given in the problem statement |
| N2 code | Comparison tolerance $10^{-6}$ rad at `rtol=1e-11`; refinement study on failure | a criterion that can fail | stated in §4.2, including the failure it produced | — |
| N5 code | Escape criterion $\lvert\theta\rvert>2.5$ rad within 25 slow periods | a decidable test | stated in §4.5; can only overestimate the basin | — |
| N7 code | $T(0)$ taken as $2\pi/\Omega$, the exact $a\to0$ limit | a reference period | stated in the script header | — |

No assumption lives only inside a `simplify` call or a solver option. Every
assumption inside the code is restated as an `[A]` in the text, which is the
`code_not_circular` requirement.

## Computations — `[N]`

| Check | Tests | File | Non-circular because | Mutants rejected |
|:--|:-------------|:--------------------------|:-------------|:--------|
| N1 | (16) from the geometry, symbolically | `check1_eom_symbolic.py` | inputs are $x(t),y(t)$ and the definitions of $T,V$, not any line of §3.2 | sign-flipped drive |
| N2 | (16) against Newton + constraint force | `check2_newton_vs_lagrange.py` | no Lagrangian, no generalised coordinate | sign-flipped drive, $10^{9}$ separation |
| N3 | (41) from the exact nonlinear equation | `check3_slow_frequency.py` | integrates (16); $\Omega$ enters only at comparison time | $\times2$, $\div2$, $+g/l$ |
| N4 | (37) by exact Floquet theory | `check4_floquet_boundary.py` | no averaging anywhere; $\varepsilon=0$ block checked against a closed form | $\varepsilon^2$, $\varepsilon^2/4$, $\varepsilon/2$ |
| N5 | (34), the barrier angle | `check5_basin_and_ripple.py` | bisects on the exact equation's behaviour | sub-threshold control holds nothing |
| N6 | (24), the ripple envelope | `check5_basin_and_ripple.py` | ripple extracted from the exact solution by moving average | constant-amplitude ripple |
| N7 | (55)–(56) on the bare Duffing equation | `check6_duffing_shift.py` | no pendulum in the script at all | $1/8$, $3/4$, sign flip |
| N8 | (41) from the Floquet phase | `check7_floquet_frequency.py` | no averaging and no period fitting | $\times2$, $\div2$, $+g/l$ |

Three `[N]` rows in the Risk register are not checks but limitations of them:
integrator tolerance (N2 set 8), N5's finite window, and the shared `monodromy`
routine between N4 and N8.

## Low confidence — `[?]`

| Eq. / § | Claim | Status |
|:--|:----------------|:--------------------------------------|
| §4.4, register ?1 | $G_{\rm c}=(\varepsilon^2/2)(1+c\varepsilon^2)$ with $c\to-0.4374\approx-7/16$ | Numerical observation over a factor of 32 in $\varepsilon$. Not derived, no source retrieved. Not used in §5. Queued as open question 1. |
