"""
pc4_coulomb_exponent.py  (PI check, not a solver artifact)

Prepared for the auditor's [FOCUS] block of P003.S04 (chunks K7, K8). Must not be attached
to a solver prompt.

Object. K = -D Laplacian in three dimensions, rho0(x, y; t) = (4 pi D t)^(-3/2)
exp(-|x - y|^2 / (4 D t)), V = -q^2/r. The bridge-averaged exponent is
    J(x, x') = int_0^tau du A_u(x, x'),
    A_u(x, x') = int d^3y rho0(x, y; u) (q^2/|y|) rho0(y, x'; tau - u) / rho0(x, x'; tau),
so that the slice weight is rho0(x, x'; tau) exp(+J).

Claims tested (from errata.md N1 and chunks.md K8, the PI's hand work, never checked):
  (i)   J(0, 0) = q^2 sqrt(pi tau / D), and J(x, x') <= q^2 sqrt(pi tau / D) everywhere;
  (ii)  for each u, A_u equals q^2 erf(|mu|/(2 s)) / |mu| with mu = ((tau - u) x + u x')/tau
        and s^2 = D u (tau - u)/tau (the Gaussian average of 1/r);
  (iii) J(x, x) -> tau q^2 / |x| as |x| -> infinity.

Routes. "direct": A_u from the free kernels by quadrature in y, using only that x, x' and
the nucleus are collinear (both on the z axis), so the y integral is two-dimensional
(spherical coordinates about the nucleus from run 2 on; cylindrical in run 1). The Gaussian form of the bridge is not used. "erf": the
formula in (ii). The u integral uses u = tau sin^2(phi), which removes the 1/sqrt(u(tau-u))
endpoint behaviour at x = x' = 0, and Gauss-Legendre in phi.

Failure: relative difference between routes above 1e-6 at any point, or a value of J above
the bound in (i). Tolerance set by the 2D quadrature, stated before running.

numpy 2.5.3, scipy 1.18.1. No random numbers.
"""
import numpy as np
from numpy.polynomial.legendre import leggauss
from scipy.special import erf

def A_spherical(z1, z2, u, tau, D, q2, nr=300, nc=600):
    # Run 1 used cylindrical coordinates about the z axis with Gauss-Legendre in (rho, z);
    # the point singularity of 1/|y| at the nucleus spoiled that quadrature (errors up to
    # 2e-4 wherever the nucleus lay inside the Gaussian, 1e-14 where it did not). Run 2
    # uses spherical coordinates (r, c = cos(angle to the z axis)) centred on the nucleus,
    # where r^2 dr cancels the 1/r. Still only free kernels; the change is to the check.
    s = np.sqrt(2 * D * u * (tau - u) / tau)
    zc = abs(((tau - u) * z1 + u * z2) / tau)
    rlo, rhi = max(0.0, zc - 12 * s), zc + 12 * s
    gr, wr = leggauss(nr)
    r = rlo + 0.5 * (rhi - rlo) * (gr + 1)
    wrr = 0.5 * (rhi - rlo) * wr
    c, wc = leggauss(nc)
    Rr, C = np.meshgrid(r, c, indexing="ij")
    d1 = Rr ** 2 + z1 ** 2 - 2 * Rr * z1 * C       # |y - x|^2
    d2 = Rr ** 2 + z2 ** 2 - 2 * Rr * z2 * C       # |y - x'|^2
    k1 = np.exp(-d1 / (4 * D * u)) / (4 * np.pi * D * u) ** 1.5
    k2 = np.exp(-d2 / (4 * D * (tau - u))) / (4 * np.pi * D * (tau - u)) ** 1.5
    k0 = np.exp(-((z1 - z2) ** 2) / (4 * D * tau)) / (4 * np.pi * D * tau) ** 1.5
    f = k1 * k2 / k0 * q2 * Rr * 2 * np.pi          # r^2 * (1/r) * 2 pi
    return np.einsum("i,j,ij->", wrr, wc, f)

def A_cylindrical(z1, z2, u, tau, D, q2, nr=400, nz=801):
    # The run-1 quadrature, kept for the regime where the nucleus is outside the Gaussian.
    s = np.sqrt(2 * D * u * (tau - u) / tau)
    zc = ((tau - u) * z1 + u * z2) / tau
    g, w = leggauss(nz)
    z = zc + 12 * s * g
    wz = 12 * s * w
    gr, wr = leggauss(nr)
    rho = 6 * s * (gr + 1)
    wrho = 6 * s * wr
    Z, R = np.meshgrid(z, rho, indexing="ij")
    k1 = np.exp(-(R ** 2 + (Z - z1) ** 2) / (4 * D * u)) / (4 * np.pi * D * u) ** 1.5
    k2 = np.exp(-(R ** 2 + (Z - z2) ** 2) / (4 * D * (tau - u))) / (4 * np.pi * D * (tau - u)) ** 1.5
    k0 = np.exp(-((z1 - z2) ** 2) / (4 * D * tau)) / (4 * np.pi * D * tau) ** 1.5
    f = k1 * (q2 / np.sqrt(R ** 2 + Z ** 2)) * k2 / k0 * 2 * np.pi * R
    return np.einsum("i,j,ij->", wz, wrho, f)

def A_direct(z1, z2, u, tau, D, q2):
    # Run 2 showed the spherical grid accurate (1e-14) near the nucleus and inaccurate far
    # from it, where the Gaussian is narrow in angle; run 1 showed the reverse for the
    # cylindrical grid. Run 3 picks per u: spherical if the nucleus is within 12 sigma of
    # the Gaussian's centre, cylindrical otherwise. Both use only free kernels.
    s = np.sqrt(2 * D * u * (tau - u) / tau)
    zc = abs(((tau - u) * z1 + u * z2) / tau)
    if zc < 12 * s:
        return A_spherical(z1, z2, u, tau, D, q2)
    return A_cylindrical(z1, z2, u, tau, D, q2)

def A_erf(z1, z2, u, tau, D, q2):
    mu = abs(((tau - u) * z1 + u * z2) / tau)
    s = np.sqrt(D * u * (tau - u) / tau)
    if mu < 1e-14:
        return q2 / (s * np.sqrt(np.pi))              # limit of erf(mu/2s)/mu
    return q2 * erf(mu / (2 * s)) / mu

def J(z1, z2, tau, D, q2, route, nphi=40):
    g, w = leggauss(nphi)
    phi = 0.25 * np.pi * (g + 1)                     # phi in (0, pi/2)
    wphi = 0.25 * np.pi * w
    tot = 0.0
    for p, wp in zip(phi, wphi):
        u = tau * np.sin(p) ** 2
        du = 2 * tau * np.sin(p) * np.cos(p)
        a = A_direct(z1, z2, u, tau, D, q2) if route == "direct" else A_erf(z1, z2, u, tau, D, q2)
        tot += wp * du * a
    return tot

fails = 0
print("(i)-(ii): J at points on the z axis, both routes, and the bound q^2 sqrt(pi tau/D)")
cases = [(0.5, 1.0, 0.05), (0.5, 1.0, 0.4), (0.3, 2.0, 0.2)]
points = [(0.0, 0.0), (0.05, 0.0), (0.05, -0.05), (0.3, 0.1), (1.0, 1.2), (-0.5, 0.5)]
for D, q2, tau in cases:
    bound = q2 * np.sqrt(np.pi * tau / D)
    for z1, z2 in points:
        jd = J(z1, z2, tau, D, q2, "direct")
        je = J(z1, z2, tau, D, q2, "erf")
        rel = abs(jd - je) / abs(je)
        bad = rel > 1e-6 or jd > bound * (1 + 1e-9)
        fails += bad
        print(f"  D={D} q2={q2} tau={tau:<4} x=({z1:+.2f}) x'=({z2:+.2f})  J_direct={jd:.10f}  J_erf={je:.10f}"
              f"  rel={rel:.1e}  bound={bound:.10f}  {'FAIL' if bad else 'ok'}")
print(f"failures: {fails}")
print()
print("(iii): J(x, x) * |x| / (tau q^2) as |x| grows (erf route; D = 0.5, q2 = 1, tau = 0.05)")
for R in (0.5, 1, 2, 5, 10, 50):
    print(f"  |x|={R:<5} ratio={J(R, R, 0.05, 0.5, 1.0, 'erf') * R / 0.05:.10f}")
