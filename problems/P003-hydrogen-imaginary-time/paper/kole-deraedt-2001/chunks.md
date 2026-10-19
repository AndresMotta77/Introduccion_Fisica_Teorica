# Kole and De Raedt (2001) — claim map and chunk ledger

PI and auditor material. Do not attach this file to a solver prompt. The part of each chunk
marked "solver sees" is a draft for prompt0 §1, and only that part is copied into a prompt.
Everything else (expectations, decisive tests, links to `errata.md`) goes to the auditor in
the INPUTS `[FOCUS]` block after the answer exists, or stays here.

Paper: arXiv:physics/0102015v1, the PDF supplied on 2026-10-18. Locators are to that
version. The procedure that produced this file is §4 of `../../PLAN.md`.

## 1. Claim map

Every numbered equation, table, and sentence that asserts something, with how the paper
supports it. "Asserted" means stated without derivation or citation; "cited" means a
reference is given in place of a derivation.

| claim | locator | content | kind | support in the paper | chunk |
|---|---|---|---|---|---|
| c1 | (1) | Trotter–Suzuki product formula | quoted | cited [5,6] | K1 |
| c2 | (2)–(3) | Z as the limit of primitive approximants Z_m | quoted | cited [6,7] | K1 |
| c3 | (4) | hydrogen Hamiltonian, reduced mass M | definition | — | K1 |
| c4 | (5) | free imaginary-time kernel | quoted | standard | K1 |
| c5 | (6) | primitive Z_m for hydrogen | derivation | substitution shown | K1 |
| c6 | p. 1–2 | sampling based on (6) drives the beads to the nucleus and fails | assertion | asserted | K1 |
| c7 | p. 2 | higher-order product formulas "only make things worse" | assertion | asserted, cites [8] | K1b |
| c8 | p. 2 | the hydrogen path integral is hard to define; formal solution in [10,11] | quoted | cited | K14 (extension) |
| c9 | (7)–(9) | Trotter for a regularised V_ε, rewritten as a ratio | derivation | shown (E1) | K2 |
| c10 | (10) | free-path weight is a probability density if the free kernel is ≥ 0 | derivation | shown | K2 |
| c11 | (11) | Jensen's inequality | quoted | standard | K2 |
| c12 | (12)–(13) | bound in terms of bead marginals | derivation | shown, with errors (E2, E3) | K2 |
| c13 | (14) | the lower bound on the propagator | derivation | shown; cites [12] | K2 |
| c14 | p. 3 | trapezium rule in (14) gives symmetrised Trotter and flips the inequality | assertion | asserted (E4) | K3 |
| c15 | (15) | an upper bound | quoted | cited [12] | K3 |
| c16 | (16) | the approximant Ẑ_m | definition | — | K4 |
| c17 | p. 3 | Ẑ1 is Feynman's variational approximation | assertion | cited [9,10] (E8) | K4 |
| c18 | p. 3 | convolution smears out singularities; (14) is finite for Coulomb | assertion | shown later for (25) | K8 |
| c19 | p. 3 | oscillator V = Mω²x² | definition | — (E5) | K5 |
| c20 | (17) | oscillator slice weight | derivation | "straightforward", footnote [15] | K5 |
| c21 | (18) | Ẑ_m in closed form | derivation | asserted result (E6) | K5 |
| c22 | (19) | Ê_m | derivation | asserted result (E6) | K5 |
| c23 | (20) | primitive E_m | quoted | cited [7] | K5 |
| c24 | Table I | fifteen rows of E_m, E, Ê_m | numerical | — (E7) | K5 |
| c25 | p. 3 | (Ê_m + E_m)/2 is remarkably close to E, unexplained | observation | none | K6 |
| c26 | footnote [15] | the Gaussian route works for every polynomial V | assertion | asserted | K5 perturbation, K6 |
| c27 | (21) | helium Hamiltonian | definition | — (E10) | K13 |
| c28 | (22) | splitting of I into one- and two-body terms | derivation | shown (E11) | K13 |
| c29 | (23)–(24) | two-body bridge average as a Gaussian convolution, D = D1 + D2 | derivation | "straightforward manipulation" | K7 |
| c30 | (25) | Coulomb case as a one-dimensional angle integral | derivation | result only (N1) | K8 |
| c31 | p. 5 | I12 is finite | assertion | "easy to check" | K8 |
| c32 | p. 5 | I1 and I2 from I12 with arguments set to zero | derivation | shown | K7 |
| c33 | (26) | helium approximant | definition | — (E12, E13) | K13 |
| c34 | (27) | hydrogen approximant | definition | — (E13) | K9 |
| c35 | p. 6 | finite integrands make (26)–(27) usable for PIQMC | assertion | asserted (E14) | K9 |
| c36 | p. 6 | E = lim_{β→∞} lim_{β/m→0} Ê_m | quoted | standard | K10 |
| c37 | Table II, p. 6 | hydrogen energies; five runs of 10⁵ steps; discretisation error hidden in the noise | numerical, assertion | — (E15) | K11 |
| c38 | Table III | helium energies | numerical | — | K13 |
| c39 | p. 6 | any H0 with positive Gaussian kernels can replace K; oscillators | assertion | asserted | K14 |
| c40 | p. 6 | with an oscillator H0 at m = 1 this is Feynman–Kleinert / Giachetti–Tognetti | assertion | cited [18–23] | K14 |
| c41 | (28) | Σ(x_k − x_{k+1})² as a sum of squares | derivation | "straightforward algebra" | K12 |
| c42 | (29)–(30) | the transformation and its inverse | derivation | result only (E16) | K12 |
| c43 | p. 7 | a global move costs O(m); y1 is the classical position | assertion | asserted | K12 |

The main path, from the definitions to the hydrogen result: c9–c13 → c29 → c30–c31 →
c34–c35 → c36 → c37. Chunks on it are required; the rest are optional or extensions.

## 2. Dependency order

```
K1  → K1b
K2  → K3
K2  → K4 → K14 (extension)
K2  → K7 → K8 → K9 → K10 → K11
K5  → K6
K5  → K10
K8  → K13 (extension), K10 → K13
K12   (no inputs: path moves)
```

No chunk depends on K1, but S01 (K1) must close before any sampler runs, because the guide
asks for the failure of the primitive weight to be shown first. K5 is a case of K2, but its
prompt asks for the bridge average directly, so the two can run in parallel.

## 3. Chunks

Each block: what the chunk covers; type and loop weight (defined in PLAN §4.3); the guide's
consultation form; phase; inputs and how they enter prompt0; paper access; the draft
statement the solver sees; what a complete answer contains; the decisive test; the
perturbation variant; status.

### K1 — The primitive discretisation of −1/r (c1–c6)

- Type: derivation with an assertion test. Weight: full. Human attempt recommended, by each
  team member, since the guide's defence asks every member to explain this proof. Blind
  solve recommended.
- Guide: phase 1, derivation consult. Subproblem S01.
- Inputs: none. Paper: closed-book.
- Solver sees (draft §1): Hydrogen with an infinitely heavy nucleus, H = −½∇² − 1/r in
  atomic units. (a) Write the N-slice primitive approximation to ⟨r|e^{−τH}|r′⟩, and from it
  two Euclidean quantities: the trace Z_N(β) and the projection
  A_N(τ) = ∫ Ψ_T(r_0) ⟨r_0|(e^{−Δτ K} e^{−Δτ V})^N|r_N⟩ Ψ_T(r_N) dr_0 dr_N, Δτ = τ/N, for a
  continuous trial function Ψ_T that is bounded below by a positive constant near the
  origin, each written out as an integral over bead positions. (b) Decide whether Z_N and
  A_N are finite, for every N ≥ 1 and Δτ > 0, and prove it. (c) Decide whether the exact
  kernel ⟨r|e^{−τH}|r′⟩ and the exact trace Tr e^{−βH} are finite. (d) The primitive
  approximation is justified by a product-formula theorem. State its hypotheses and say
  which, if any, fail here.
- Complete answer: the integrals written out; proofs for (b) and (c), every inequality
  justified; the theorem in (d) stated with a locator; a computation that can fail (for
  example the radial integral with a cutoff η → 0 and the predicted growth law).
- Decisive test (PI only): (1) A_N = ∞ from non-integrability at the nucleus, for every N
  and Δτ. (2) The exact kernel is finite, and Tr e^{−βH} is infinite for a different reason
  (Rydberg series and continuum). An answer that runs these two infinities together has
  not understood the problem. (3) The failing hypothesis is the semiboundedness of V: with
  V unbounded below, e^{−ΔτV} is not a bounded operator and the product formula is not
  covered. (4) The proposal's Proposition 1 is one valid proof of (b); the solver must not
  have seen it.
- Perturbation: V = −1/r^s for s = 1/2 and s = 3/2. The primitive integral diverges for
  every s > 0, while H is bounded below for s < 2, so the failure is a property of the
  discretisation at every s. A derivation that only works for s = 1 was recalled.
- Status: not started.

### K1b — Higher-order product formulas (c7)

- Type: assertion test. Weight: standard. Optional.
- Guide: phase 1 or 3, audit consult. Subproblem: second round of S01, or its own.
- Inputs: K1 closed (§3a). Paper: open-book for the sentence on p. 2 only.
- Solver sees: Derive the symmetric fourth-order factorisation of e^{−Δτ(K+V)} in which the
  double commutator appears in the potential factor (Takahashi–Imada form). Evaluate the
  modified potential for V = −1/r and decide whether the resulting slice weight is
  integrable at the nucleus. Then assess the sentence of Kole and De Raedt quoted in §3b.
- Decisive test: sign and coefficient of the |∇V|² term (errata E9); integrability; whether
  the answer separates "integrable" from "converges at fourth order".
- Status: not started.

### K2 — The lower bound on the propagator (c9–c13)

- Type: derivation. Weight: standard (full if the method is the effective action and time
  allows).
- Guide: phase 1, derivation consult. Subproblem S02.
- Inputs: none. Paper: closed-book first; in round 2, open-book on (7)–(14) with the
  instruction to compare.
- Solver sees: Let H = K + V with K = −D∇² in three dimensions and V bounded below. Show that
  ⟨x|e^{−τH}|x′⟩ ≥ ⟨x|e^{−τK}|x′⟩ exp(−∫₀^τ du ⟨V⟩_u), where ⟨V⟩_u is the average of V over
  the position at time u of the free Brownian bridge from x to x′ of duration τ, and write
  ⟨V⟩_u with free kernels. Give two derivations, one from the product formula and one from
  the Feynman–Kac representation. State where positivity of the free kernel is used. Then
  say what is needed to apply the bound to V = −1/r, which is not bounded below.
- Complete answer: both derivations with every step; the bead marginal written with its
  times; the regularisation and its removal argued; a numerical test of the inequality on
  the oscillator against the exact Mehler kernel.
- Decisive test: the bead marginal carries times iτ/m and (m − i)τ/m, and the step from (12)
  to (13) is an equality (E2, E3; the round-2 comparison should find them); the removal of
  the regulator has an argument (monotone convergence or equivalent); the numerical
  test covers small τ (ratio → 1) and large τ (bound loose).
- Perturbation: replace K by an oscillator H0 = −D∇² + ½κx² as the reference, which §V of
  the paper proposes without derivation. The bound must change accordingly.
- Status: not started.

### K3 — The upper bound and the trapezium remark (c14, c15)

- Type: assertion test. Weight: standard. Optional; low priority.
- Inputs: K2 closed. Paper: open-book, (14)–(15) and the sentences between them.
- Solver sees: The paper states (15) and a remark about replacing the u-integral in (14) by
  a two-point trapezium rule. Establish or refute each inequality in (15) and the remark.
- Decisive test: E4; numerical test of both sides of (15) on the oscillator.
- Status: not started.

### K4 — The approximant Ẑ_m (c16–c18)

- Type: assertion test with one open question. Weight: standard. Optional; useful before
  K14.
- Inputs: K2 closed. Paper: open-book for (16) and the sentence on Ẑ1.
- Solver sees: With Ẑ_m defined by (16): (a) show Ẑ_m ≤ Z; (b) for m = 1, compare Ẑ1 with
  Feynman's variational lower bound for a free-particle trial action and decide whether
  they are the same functional of V; (c) decide whether Ẑ_{km} ≥ Ẑ_m for integers k ≥ 2.
- Decisive test: (b) end-point bridge average against centroid smearing (E8); (c) the PI
  expects refinement to tighten the bound by the tower property of conditional
  expectation, but has not proved it.
- Status: not started.

### K5 — The oscillator in closed form (c19–c24)

- Type: derivation, then reproduction. Weight: standard. Required: it is the positive
  control for the phase-2 code.
- Guide: phase 1, derivation consult. Subproblem S03.
- Inputs: none. Paper: closed-book in round 1 (the solver gets the definition (16) and the
  oscillator; (17)–(20) and Table I are withheld); open-book in round 2 with (17)–(20) and Table I
  and the instruction to reproduce every row and report every discrepancy.
- Solver sees (round 1): One-dimensional oscillator, V = ½Mω²x², units ħ = M = ω = 1. For the
  approximant (16) and for the primitive approximant (3), derive the cyclic m-slice
  partition functions and the energies −∂ ln Z/∂β in closed form, with every step of the
  bridge average and of the diagonalisation. Evaluate both for β ∈ {1, 5, 10} and
  m ∈ {1, 10, 50, 100, 500}.
- Decisive test: E5, E6, E7. pc1 in `pi-checks/` has the PI's numbers; the auditor gets
  them only after round 1.
- Perturbation: V = λx⁴. The slice weight needs bridge moments up to fourth order and Ẑ_m
  is no longer Gaussian; compare with the exact energy from diagonalisation. Connects to
  Project 01 of the guide.
- Status: not started. The proposal's check 7 derived the oscillator weight independently
  and reproduced four rows; it is prior knowledge for whoever has read the proposal.

### K6 — Why the average of the two approximants works (c25, c26)

- Type: gap. Weight: full. Optional; research-level for a semester project.
- Guide: phase 3 or 4. Candidate extension.
- Inputs: K5 closed. Paper: the observation itself is given; nothing else.
- Solver sees: For the oscillator, expand the errors of the primitive E_m and the Jensen
  Ê_m at fixed β in powers of 1/m, to the first two nonvanishing orders each. Explain the
  observation that (E_m + Ê_m)/2 is much closer to the exact energy than either. Decide
  whether the explanation applies to a general smooth V, and test it on V = λx⁴.
- Decisive test (PI only): pc2 finds the leading 1/m² coefficients equal and opposite and a
  residual of order m⁻³ coming from Ê_m. An answer that finds a residual of order m⁻⁴ has
  an error somewhere, either in it or in pc2. Literature: unknown to the PI.
- Status: not started.

### K7 — The bridge average as a Gaussian convolution (c29, c32)

- Type: derivation. Weight: standard. Required.
- Guide: phase 1, derivation consult. Subproblem S04 (with K8).
- Inputs: none. Paper: closed-book.
- Solver sees: For K = −D∇² in three dimensions, write
  ∫₀^τ du ⟨x|e^{−uK} V e^{−(τ−u)K}|x′⟩ / ⟨x|e^{−τK}|x′⟩ as an integral over u of a Gaussian
  average of V, giving the mean and covariance. Repeat for a pair potential V(r1 − r2) of
  two particles with D1 and D2, reducing it to the relative coordinate.
- Decisive test: covariance 2Du(τ − u)/τ per component; D = D1 + D2 for the pair; a sampled
  bridge test that would catch a factor of 2 in the variance.
- Status: not started.

### K8 — The Coulomb slice weight and its finiteness (c18, c30, c31)

- Type: derivation. Weight: full. Required: it carries the guide's demand that the chosen
  weight be shown finite in writing.
- Guide: phase 1, derivation consult. Subproblem S04.
- Inputs: K7, through §3a once closed. Paper: closed-book in round 1; (25) given in round 2.
- Solver sees: For V = −q²/r, reduce the result of K7 to a single one-dimensional integral
  suitable for numerical work. Prove that it is finite for all x, x′, including
  x = x′ = 0. Give its behaviour as |x|, |x′| → 0 and → ∞, and a bound uniform in x, x′.
- Decisive test: agreement with (25) in round 2 (N1); a direct quadrature of the
  three-dimensional Gaussian average at random points, near the nucleus included; the
  value at x = x′ = 0, which the PI gets as q²√(πτ/D) and the solver must find on its own;
  the large-distance limit τq²/|x| when x ≈ x′.
- Perturbation: Yukawa, V = −q² e^{−κr}/r, for which the Gaussian average has a closed form
  in terms of erfc. Connects to Project 05 of the guide.
- Status: not started.

### K9 — Is the hydrogen weight a probability measure? (c34, c35)

- Type: derivation with an assertion test. Weight: full. Required: this is the guide's
  "real, positive and normalisable" statement.
- Guide: phase 1, derivation and audit consults. Subproblem S05.
- Inputs: K8 through §3a. Paper: closed-book in round 1; (27) and the sentence after it in
  round 2.
- Solver sees: Using the slice weight of K8: (a) write the m-slice approximant to
  Tr e^{−βH} for hydrogen on all of R³ and decide whether it is finite; (b) write the
  projection A_N(τ) with trial-function ends, for Ψ_T = e^{−ζr} and for a Gaussian Ψ_T, and
  decide whether its normalised integrand is a probability density on R^{3(N+1)};
  (c) describe what a Metropolis walk does when given a weight whose integral is infinite,
  and how one would notice in a finite run.
- Decisive test: (a) infinite through the volume (E14); (b) normalisable; round 2 should
  produce E13 (dimension of τΣI) and E14 from the paper's text.
- Status: not started.

### K10 — The estimators (c36)

- Type: derivation. Weight: standard. Required: the guide's "fix the energy estimator".
- Guide: phase 1, derivation consult. Subproblem S06.
- Inputs: K9 and K5 through §3a. Paper: closed-book.
- Solver sees: For the projection of K9(b) with the slice weight of K8, derive estimators
  of E_1s, ⟨r⟩ and the radial density P(r) whose expectations tend to the exact values as
  NΔτ → ∞ and Δτ → 0. For each, say whether it is a mixed or a pure estimator, the sign of
  its bias at finite Δτ if it can be determined, and its variance near the nucleus. Apply
  the energy estimator to the oscillator weight of K5 and compare with the closed form.
- Decisive test: a thermodynamic estimator must contain the τ-derivative of the effective
  potential (E15); the end-bead local energy is a mixed estimator; ⟨r⟩ and P(r) from the
  middle bead are pure; P(r) carries 4πr².
- Status: not started.

### K11 — Table II and the claim about discretisation error (c37)

- Type: reproduction. Weight: standard. Required in phase 3: the second presentation
  compares with the central reading.
- Inputs: the phase-2 code, K10. Paper: open-book.
- Solver sees: this subproblem inverts the usual roles. The team runs the code at the
  paper's (β, m), with the projection setup of K9(b), and writes the comparison; that
  write-up is answer-1 and goes through the audit loop.
- Decisive test: whether the paper's claim that discretisation error is hidden in the noise
  survives a sweep in τ at fixed β; how their five-run error bars compare with a blocking
  analysis of comparable statistics (E15).
- Status: not started.

### K12 — Staging coordinates (c41–c43)

- Type: implementation. Weight: light. Required if the path moves of the appendix are used.
- Guide: phase 2, implementation consult. One of the units S08–S11.
- Inputs: none. Paper: open-book, since this is an algorithm and no result in it is under
  test.
- Solver sees: One function that maps independent Gaussian variables to a free path of m
  beads with fixed or cyclic ends, with its inverse, plus one test: the sampled bead
  covariance matches the free-bridge covariance to within its statistical error.
- Decisive test: E16; the Jacobian; the covariance test at m = 3 and m = 100.
- Status: not started.

### K13 — Helium (c27, c28, c33, c38)

- Type: extension. Weight: full. Option for phase 4.
- Inputs: K8, K10. Paper: open-book.
- Decisive test: E10, E11, E12.
- Status: not started.

### K14 — An oscillator reference in place of the free particle (c39, c40)

- Type: extension. Weight: full. Option for phase 4; research-level.
- Inputs: K2 (and its perturbation variant), K4. Paper: open-book for §V.
- Solver sees: Generalise the bound of K2 to the reference H0 = −D∇² + ½κx² with κ free.
  Derive the slice weight for V = −1/r. Decide how κ should be chosen for each slice and
  whether a variational choice improves the τ-dependence of the hydrogen energy. Compare
  the m = 1 case with the Feynman–Kleinert effective classical potential.
- Status: not started.
