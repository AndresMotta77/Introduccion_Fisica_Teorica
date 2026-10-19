# Kole and De Raedt (2001) — discrepancy ledger

PI and auditor material. Do not attach this file to a solver prompt. A solver that has read
it is anchored on every entry below, and the chunks that are meant to find these things
independently lose their value. If it was attached, say so in that subproblem's
`sources/independence.md`.

Source read: J. S. Kole and H. De Raedt, "Quantum Monte Carlo method for attractive Coulomb
potentials", arXiv:physics/0102015v1 (6 Feb 2001), 7 pages, the PDF supplied by the user on
2026-10-18 (its header reads "DRAFT: August 8, 2021", the date on which arXiv regenerated
the PDF; the content is v1). Equation and page numbers below refer to that file. The published
version, Phys. Rev. E 64, 016704 (2001), has not been read; some of these may be corrected
there. Every entry should be checked against it before it is cited outside this repository.

Status values: `candidate` (found by the PI, not yet settled by a subproblem), `confirmed`
(settled by the subproblem named, with its audit), `rejected` (the paper was right).
Confidence is the PI's, before any subproblem has run.

| id | where | kind | confidence | settled by | status |
|---|---|---|---|---|---|
| E1 | eqs. (8)–(9) | notation | high | K2 | candidate |
| E2 | eq. (12) | sign | high | K2 | candidate |
| E3 | eq. (13) | wrong kernel times, inequality where equality holds | medium | K2 | candidate |
| E4 | text after (14) | "l.h.s." for "r.h.s." | high | K3 | candidate |
| E5 | §III, definition of V | factor 1/2 missing | high | K5 | candidate |
| E6 | eqs. (18), (19) | powers of m | high | K5 | candidate |
| E7 | Table I | three rows do not reproduce | high | K5 | candidate |
| E8 | text after (16) | identification of Ẑ1 with Feynman's variational bound | low | K4 | candidate |
| E9 | §I, p. 2 | assertion about higher-order product formulas | low | K1b | candidate |
| E10 | eq. (21), and (22), (26) | helium charges | high | K13 | candidate |
| E11 | eq. (22) | β for τ, stray parenthesis | high | K13 | candidate |
| E12 | eq. (26) | argument order and use of primes | medium | K13 | candidate |
| E13 | eqs. (26), (27) | extra factor τ in the exponent | high | K9 | candidate |
| E14 | eq. (27) and §IV text | finite integrand taken as a usable measure | high | K9 | candidate |
| E15 | §IV | estimator and error-bar method not stated | high (it is an omission) | K10, K11 | candidate |
| E16 | Appendix | {u_i} for {y_i}; indices in (29)–(30) | medium | K12 | candidate |
| E17 | ref. [11] | page number | high | done | confirmed in the proposal |
| N1 | eq. (25) | no discrepancy found | — | K8 | PI derivation only |

## Entries

**E1. Eqs. (8)–(9).** The integration variables are written dx1 ··· dxn while the products
run to m, and the end points x and x′ of (7) never appear in (8): the product runs over
⟨x_i|e^{−τK/m}|x_{i+1}⟩ for i = 1, …, m with all x_i integrated. Presumably x_1 = x and
x_{m+1} = x′ with x_2, …, x_m integrated. Notation only, but the solver of K2 has to fix a
reading before the Jensen step means anything.

**E2. Eq. (12).** Inside the integral the kernel is printed ⟨x_n|e^{+τK/m}|x_{n+1}⟩. It
should be e^{−τK/m}, as in (10).

**E3. Eq. (13).** The bead marginal is printed ⟨x|e^{τK/m}|x_i⟩V_ε(x_i)⟨x_i|e^{τK/m}|x′⟩ /
⟨x|e^{−τK}|x′⟩ and joined to (12) by ≥. Integrating (12) over all beads except x_i is a
marginalisation, which gives an equality, and the marginal of bead i in a free bridge of
total time τ is ⟨x|e^{−(i/m)τK}|x_i⟩⟨x_i|e^{−(1−i/m)τK}|x′⟩ / ⟨x|e^{−τK}|x′⟩: the two
kernels carry the times iτ/m and (m − i)τ/m where the print has τ/m for each, and the sign
of the exponent is negative. With
those times the sum over i becomes the integral over u in (14), which is how the paper
proceeds, so the intended content is clear.

**E4. Text after (14).** "Note that l.h.s of (14) reduces to the standard, symmetrized
Trotter-Suzuki formula approximation if we replace the integral over u by a two-point
trapezium-rule approximation." The right-hand side is meant.

**E5. §III.** The oscillator potential is defined as V = Mω²x². Both (17) and the exact
energy (ħω/2)coth(βħω/2) correspond to V = Mω²x²/2. The PI's derivation: the free bridge
from x_n to x_{n+1} over time τ has mean x̄(u) = x_n + (x_{n+1} − x_n)u/τ and variance
ħ²u(τ − u)/(Mτ), so ∫₀^τ du ⟨x(u)²⟩ = τ(x_n² + x_n x_{n+1} + x_{n+1}²)/3 + ħ²τ²/(6M), and
multiplying by Mω²/2 gives (βMω²/6m)(x_n² + x_{n+1}² + x_n x_{n+1} + βħ²/(2mM)) with
τ = β/m, which is (17). With V = Mω²x² every term would be twice as large and the exact
energy would be (ħω/√2)coth(βħω/√2). Check 7 of the proposal used V = x²/2 and reproduced
four rows of Table I.

**E6. Eqs. (18) and (19).** Diagonalising the quadratic form of (17) with a discrete
Fourier transform gives, for each mode θ_n = 2πn/m, the factor
1 − cos θ_n + (β²ħ²ω²/6m²)(2 + cos θ_n) = 1 + β²ħ²ω²/(3m²) − (1 − β²ħ²ω²/(6m²)) cos θ_n.
The paper prints 3m and 6m where the PI gets 3m² and 6m². Then
Ê_m = (βħ²ω²/6m)[1 + (1/m) Σ_n (2 + cos θ_n)/(1 − cos θ_n + β²ħ²ω²(2 + cos θ_n)/(6m²))],
while (19) as printed has no 1/m in front of the sum and 6m in the denominator. The printed
(19) grows with m (pc1 route A: 4.84 at β = 1, m = 100, against the exact 1.08198); the
corrected one reproduces Table I except for the rows in E7, and agrees to 3e-8 with a route
that builds the m × m matrices directly from (17) (pc1 route C, pc1b). The m = 1 rows cannot
tell the two versions apart. Eq. (20) as printed is consistent with the primitive form.

**E7. Table I.** Against both of the PI's routes, three rows disagree by more than rounding:
(β = 5, m = 50) Ê printed 0.50694, computed 0.507376; (β = 5, m = 100) E_m printed 0.50678,
computed 0.506629, and Ê printed 0.50679, computed 0.506935; (β = 10, m = 10) E_m printed
0.44273, computed 0.447273, which looks like a dropped digit. Two more differ in the last
printed digit only: (β = 1, m = 1) Ê = 7/6 printed 1.16668, and (β = 5, m = 10). The
β = 5, m = 100 printed values are close to the computed m = 500 values. Evidence:
`pi-checks/pc1_table1.out`. The proposal's check 7 compared only four rows, none of these.

**E8. Text after (16).** "The simplest approximant Ẑ1 corresponds to the Feynman's
variational approximation to the full Feynman path integral." Ẑ1 averages V over the free
bridge between fixed end points (x = x′ for a trace). Feynman's variational bound, in the
form the PI recalls it (Feynman and Hibbs ch. 11; Feynman and Kleinert 1986), smears V
around the path centroid with a Gaussian of variance βħ²/(12M). Both are Jensen bounds,
conditioned on different things, and the PI expects them to differ. [R], {ver: no}; the
reference texts have not been retrieved. The discussion in §V makes the same
identification for an oscillator reference at m = 1.

**E9. §I, p. 2.** "Using instead of the simplest Trotter-Suzuki formula (1) a more
sophisticated one [8] only makes things worse because these hybrid product formulae contain
derivatives of the potential." No derivation is given. The PI recalls [R] that the
symmetric fourth-order factorisation of Takahashi and Imada adds to V a term proportional to
+τ²ħ²|∇V|²/M, which for V = −q²/r is a positive 1/r⁴ term near the nucleus, so the weight
would be bounded there. Whether that factorisation then converges for Coulomb is a separate
question. Low confidence; the sign and coefficient must be derived in K1b before this entry
means anything.

**E10. Eq. (21).** The Hamiltonian of "a neutral system consisting of two electrons with
opposite spin and a nucleus" is printed with −q²/|r1| − q²/|r2| + 2q²/|r1 − r2|. Helium has
nuclear charge 2q, so the electron–nucleus terms are −2q²/|r_i| and the electron–electron
term is +q²/|r1 − r2|. Eq. (22) (V1 + V2 − 2V12) and eq. (26) (I1 + I2 − 2I12) follow the
printed form. The values in Table III, near −2.9 q²/a0, suggest the code used the correct
Hamiltonian. Only relevant if helium is taken as the extension.

**E11. Eq. (22).** The first denominator is ⟨r1 r2|e^{−β(K1+K2)}|r1′ r2′⟩; everywhere else
the slice time is τ. The second line has a stray parenthesis in e^{−τK1)}.

**E12. Eq. (26).** In (22)–(25) a prime marks the other end of the time slice; in (26) it
marks electron 2. With the argument order of (23), I12(r1, r2, r1′, r2′), the last term of
(26) should read I12(r_n, r′_n, r_{n+1}, r′_{n+1}, 2D1), where it is printed
I12(r_n, r_{n+1}, r′_n, r′_{n+1}, 2D1).

**E13. Eqs. (26) and (27).** The exponent is printed τ Σ_n I(…). As defined in (22)–(24),
I already contains the integral over u from 0 to τ, and (25) carries the resulting prefactor
2τq². With q²/length an energy and τ an inverse energy (the slice operator is e^{−τK}), I is
dimensionless, so τ Σ I has the dimension of an inverse energy. Comparison with (16), whose
exponent is −∫₀^τ du ⟨V⟩, gives Σ I without the τ. With τ = 0.05, an extra τ would weaken
the effective attraction twentyfold, and Table II would not be near −0.5, so the code
probably did not have it.

**E14. Eq. (27) as a sampling measure.** The paper says that because the integrands of (26)
and (27) are always finite, they "can be used [to] perform PIQMC simulations". A finite
integrand does not make a normalisable measure. Far from the nucleus the slice weight tends
to the free one, and the integral of a closed free path over the position of the path grows
with the volume, so Ẑ^H_m over R^{3m} is infinite. The exact Tr e^{−βH} for hydrogen is also
infinite, from the Rydberg series and the continuum. The paper does not say whether a box
was used or whether the runs were short enough that the path never left the nucleus. This
is the guide's distinction between an executable calculation and a valid probability
measure, in the central reading itself, and it is why K9 reformulates the problem as
ground-state projection with trial-function ends.

**E15. §IV.** The energy estimator is not stated. With the effective potential depending on
τ = β/m, −∂ ln Ẑ_m/∂β contains derivatives of I1 with respect to τ as well as the kinetic
term, and a virial form would differ again. The error bars come from "five statistically
independent simulations of 100000 Monte Carlo steps per degree of freedom", without saying
how the five were combined or how autocorrelation was handled. The claim that "the
systematic errors due to the discretization of the path integral are hidden in the
statistical noise" is not supported by a sweep in τ; Table II has two values of τ (0.05 and
0.025) at different β.

**E16. Appendix.** "The expression for x_k in terms of the {u_i} reads" should say {y_i}.
The index ranges in (28)–(30) (the sum on the right of (28) starting at k = 2, the role of
y_1 and of x_{m+1} in (29)) need checking against a direct numerical test.

**E17. Reference [11].** Duru and Kleinert is cited as Phys. Lett. B84, 30 (1979); the
publisher's record gives 84, 185–188. Found and confirmed while writing the proposal
(`proposals/guide15-P04-hydrogen-imaginary-time/README.md`, Provenance).

**N1. Eq. (25), no discrepancy.** The PI re-derived (25) from (24) by hand: the Gaussian in
(24) has mean μ(u) = ((τ − u)a + u b)/τ, with a = r1 − r2 and b = r1′ − r2′, and variance
2u(τ − u)D/τ per component; the average of q²/|r| over it is q² erf(|μ|/(2s))/|μ| with
s² = u(τ − u)D/τ; the substitution u = τ cos²φ gives μ = sin φ cos φ (a tan φ + b cot φ) and
du = 2τ sin φ cos φ dφ, which produces (25) including the prefactor 2τq². This is a hand
derivation and has not been checked numerically. K8 checks it against a direct quadrature of (24).
