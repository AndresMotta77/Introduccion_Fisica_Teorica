# Coverage — pc3_oscillator_levels.py

PI check run on 2026-11-12, after the prompt0 of P003.S03 was drafted and before it was sent.
It is prior knowledge for anyone who reads it, and it must not be attached to a solver prompt
for chunk K5. Its results go to the S03 auditor in the `[FOCUS]` block
(`../chunks.md`, K5).

## What was run

Four runs. The script in this folder is the version of run 4. Comments in it mark each change.

- Run 1 (`pc3_oscillator_levels.run1.out`). Routes A and B agreed at τ = 0.5 and 0.25. At
  τ = 0.1 the script crashed: for distant grid points the free kernel underflows to 0, the
  division gave 0/0, and the eigensolver received NaNs. Change: where the free kernel
  underflows, the weight is set to 0. This changed the check, not the derivation.
- Run 2 (`pc3_oscillator_levels.run2.out`). Routes A and B agreed at all three τ. Route C
  crashed at β = 5, m = 1, because τ = 5 > √6 makes the coefficient b = 1/τ − τ/6 negative and
  acosh(a/b) complex. Change: route A extended to b < 0. The kernel is then the Mehler kernel
  with x′ → −x′, and the eigenvalues are λ₀(sgn(b) e^{−θ})ⁿ with cosh θ = a/|b|. This corrected
  the PI's closed form, which as first written held only for τ < √6. It was not a tolerance
  change.
- Run 3. Stopped by hand after ten minutes inside `sympy.series(acosh(a/b))`. Its output was
  lost to pipe buffering. Change: the series is taken through s = sinh(θ/2). That is the same
  quantity computed faster.
- Run 4 (`pc3_oscillator_levels.out`). Every comparison passed.

## Results passed to [FOCUS]

- Slice weight: w = (2πτ)^{−1/2} exp[−(x − x′)²/2τ − τ(x² + xx′ + x′²)/6 − τ²/12].
  Route B rebuilds the exponent from free kernels and agrees to 1e-13.
- Spectrum of the slice operator: λₙ = C √(2π sinh θ/Ω) e^{−θ(n+½)}, with a = 1/τ + τ/3,
  b = 1/τ − τ/6, C = (2πτ)^{−1/2} e^{−τ²/12}, cosh θ = a/b, Ω = √(a² − b²) = √(1 + τ²/12).
  Agreement with grid diagonalisation is better than 2e-13 for n ≤ 4 and τ ∈ {0.5, 0.25, 0.1}.
- E_n(τ) = −ln λₙ/τ = (n + ½)(1 + τ²/24) − τ³/144 + (3/1280)(2n + 1)τ⁴ + O(τ⁵). Every level
  lies above n + ½, as a pointwise lower bound on a positive kernel requires for the top
  eigenvalue.
- The symmetric primitive kernel e^{−τV/2} ρ₀ e^{−τV/2}: E_n(τ) = (n + ½)(1 − τ²/24)
  + (3/1280)(2n + 1)τ⁴ + O(τ⁵), with no τ³ term.
- For τ > √6 the odd-n eigenvalues are negative. At τ = √6 the kernel factorises and has rank
  one. Only the m = 1 rows of Table I at β = 5 and 10 are in that regime.
- Route C: the trace of T^m, λ₀^m/(1 − sgn(b)^m e^{−mθ}), gives an energy that agrees with
  pc1's route B formula (the DFT re-derivation of eq. (19)) to better than 1e-38 at all fifteen
  Table I points. pc1's corrected (19) is therefore confirmed by a third route that shares
  nothing with the DFT.

## A consequence for K6 (arithmetic in this note, not run as code)

The τ² terms of the two approximants cancel level by level. The τ³ term, −τ³/144, comes from
the bridge-averaged weight alone and does not depend on n. With E_n(τ) = (n + ½)(1 ± τ²/24)
+ bτ³, one has ln Ẑ_m = −βbτ³ + (the n-dependent part), so the thermal energy picks up
4bτ³ from it. The sum of the two errors at fixed β is then 4(−1/144)τ³ = −τ³/36 = −β³/(36m³),
for every β. Against `pc2_average.out` at m = 1600: β = 1 predicted −6.78e-12, pc2 −6.78e-12;
β = 5 predicted −8.48e-10, pc2 −8.45e-10; β = 10 predicted −6.78e-9, pc2 −6.75e-9. That
explains the m⁻³ residual pc2 found, for the oscillator. Whether a τ³ term of this kind
appears for a general smooth V is the open half of K6.

## Would have caught

- A wrong exponent for the oscillator slice weight: a factor in the τ²/12 constant, the
  1/6, or the cross term. Route B does not use the Gaussian form of the bridge.
- A wrong match to the Mehler kernel (a, b, θ, Ω, the prefactor), through the eigenvalue
  comparison.
- A disagreement between the spectral trace and pc1's DFT formula for Ê_m.
- Wrong series coefficients, through the comparison with route A at τ = 0.1. The residual is
  7.5e-9 at n = 0, consistent with an omitted τ⁵ term.

## Would not have caught

- An error in V or in ρ₀ shared by every route. V = x²/2 is assumed ([A]; see errata E5).
- Errors in levels above n = 4, or outside |x| ≤ 8 on the grid.
- An error in the primitive series. It comes from the closed form only, with no numerical
  route.
- Anything about the Coulomb case.
