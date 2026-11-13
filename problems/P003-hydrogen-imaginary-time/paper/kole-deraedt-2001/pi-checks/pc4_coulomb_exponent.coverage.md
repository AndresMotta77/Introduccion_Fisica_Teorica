# Coverage — pc4_coulomb_exponent.py

PI check run on 2026-11-12, after the prompt0 of P003.S04 was drafted and before it was sent.
It is prior knowledge for anyone who reads it, and it must not be attached to a solver prompt
for chunks K7 or K8. Its results go to the S04 auditor in the `[FOCUS]` block
(`../chunks.md`, K7–K8).

## What was run

Three runs. All three compare the same erf formula against a direct quadrature built from
free kernels. Only the quadrature of the direct route changed between runs.

- Run 1 (`pc4_coulomb_exponent.run1.out`): cylindrical coordinates about the z axis, with
  Gauss–Legendre in (ρ, z). 14 of 18 points failed, with relative differences from 6e-7 to
  1.8e-4. Every failure had the nucleus inside the Gaussian. The points with the nucleus
  outside it agreed to 1e-14. Diagnosis: the 1/|y| point singularity spoils the quadrature.
- Run 2 (`pc4_coulomb_exponent.run2.out`): spherical coordinates centred on the nucleus,
  where r² dr cancels 1/r. The near-nucleus points now agreed to 1e-14 and 8 far points
  failed, by 2e-7 to 2e-4. Diagnosis: far from the nucleus and at small u, the Gaussian is
  narrow in angle and the angular grid does not resolve it.
- Run 3 (`pc4_coulomb_exponent.out`): for each u, spherical coordinates if the nucleus is
  within 12σ of the Gaussian's centre and cylindrical otherwise. All 18 points agreed to
  better than 1.2e-12.

The tolerance (1e-6) was not changed. What changed was the quadrature, chosen to suit each
regime. Each run reports every point.

## Results passed to [FOCUS]

- For each u, the bridge average of q²/|y| equals q² erf(|μ|/2s)/|μ|, with
  μ = ((τ − u)x + ux′)/τ and s² = Du(τ − u)/τ. That is, the bridge position at time u is
  Gaussian with mean μ and variance 2Du(τ − u)/τ per component.
- J(0, 0) = q²√(πτ/D) at (D, q², τ) = (0.5, 1, 0.05), (0.5, 1, 0.4) and (0.3, 2, 0.2). The
  maximum of J over the 18 points is at x = x′ = 0 in every case. In atomic units
  (D = 1/2, q = 1) the maximum is √(2πτ), 0.5605 at τ = 0.05.
- J(x, x)·|x|/(τq²) → 1 for large |x|. It is 0.999998 at |x| = 0.5 and τ = 0.05, and equal to
  1 to ten digits from |x| = 1 on.

## Would have caught

- A factor of 2 in the bridge variance: J at the origin scales as 1/s.
- A wrong bridge mean, a wrong Gaussian average of 1/r, or a wrong value at the origin.
- A violation of the bound J ≤ q²√(πτ/D) at any of the 18 points.

## Would not have caught

- Configurations where x, x′ and the nucleus are not collinear. The direct route needs that
  symmetry. The erf form covers the general case only if the derivation of (ii) is right in
  general.
- The PI's hand reduction of the u-integral with u = τ cos²φ to the printed eq. (25)
  (errata N1). Only the erf integrand it starts from is tested here. The paper's (25) itself
  is not in the repository and was not compared.
- A proof of the bound. It holds at the tested points. The general statement rests on the
  Gaussian average of a radially decreasing function being largest when the Gaussian is
  centred at the origin, which the PI recalls ([R], {ver: no}).
- Anything about the spectrum of the slice operator.
