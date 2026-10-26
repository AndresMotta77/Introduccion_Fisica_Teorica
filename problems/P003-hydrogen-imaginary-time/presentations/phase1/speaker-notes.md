# Speaker notes — Phase 1 presentation

Copied from the `<aside>` of each slide in `artifact/slides/`, in slide order. About 1,250
words in all, which is 9 to 9.5 minutes at a normal speaking pace.

## 1. The path integral for hydrogen, and why it fails at the nucleus

*Guide 15 · Project 04 · Phase 1* · 52 words

This is the first phase of our project on the hydrogen ground state from imaginary time. We first go through our notes page by page: Feynman's path integral, its imaginary-time version, and what happens to the Coulomb potential at the nucleus. Then we show what we found when we checked those pages.

## 2. Feynman: add up the amplitudes of all paths

*Our notes · p. 1* · 83 words

Page one of our notes follows Feynman. We divide the time into N equal parts of size epsilon, and the action becomes a Riemann sum: a kinetic term for each segment and the potential at each point, N terms in all. Each path j has an amplitude A e to the i S j over h bar, and the total amplitude adds them. Integrating over the intermediate positions, with both endpoints fixed, gives the kernel, which in the limit is Feynman's path integral.

## 3. The integrals are Gaussian

*Our notes · p. 2* · 78 words

Page two collects the Gaussian integrals we need. When the quadratic form is diagonal, each variable integrates on its own and the result is a product of square roots. When the form has cross terms, a change of basis diagonalises it: in the two-variable example the matrix has eigenvalues three and one. In general the product of the eigenvalues is the determinant of M. For the free particle the matrix is tridiagonal and its determinant is exactly N.

## 4. The free-particle propagator

*Our notes · p. 3* · 79 words

Page three applies this to the free particle. We expand the action around the classical path, with a fluctuation z that vanishes at both ends; for a free particle the expansion is exact. The classical part gives a phase, and the fluctuations give exactly the Gaussian integral of page two. Each of the N segments carries a factor one over C, which fixes A. The powers of C and the factor N combine, and we get the free propagator.

## 5. The project: E₀ from the partition function

*Our notes · p. 4* · 80 words

Page four states the project. We want the ground-state energy from the partition function in imaginary time, because imaginary time suppresses the higher energies. The Wick rotation turns the evolution operator into e to the minus beta H, so the trace is a sum of decaying exponentials. For large beta only the ground state survives, and E zero is minus log Z over beta. In position space the trace starts and ends at the same x: only closed paths contribute.

## 6. Dividing β into m segments

*Our notes · p. 5* · 89 words

Page five meets the obstacle: the kinetic and potential operators do not commute, so the exponential of their sum does not factor. Our solution is to divide beta into m segments of size delta beta. For one short segment, expanding both exponentials to first order gives the same result, so each segment is replaced by U hat, the kinetic factor times the potential factor. Z becomes the trace of m copies of U. The notes add that this only works for very small intervals; keep that phrase in mind.

## 7. Inserting the identity m times

*Our notes · p. 6* · 86 words

Page six turns the trace into ordinary integrals. Inserting the identity between the factors, for m equal to three, gives three matrix elements around a closed loop, and in general m of them, with the last position joined to the first. Each one is the potential weight at x j times the free propagator in imaginary time, a Gaussian in the jump. Multiplying them gives Z m as an integral over m positions. One correction: the potential term carries delta beta, as page seven has it.

## 8. The exponent is a Euclidean action

*Our notes · p. 7* · 82 words

Page seven recognises the structure. With delta tau equal to h bar delta beta, the exponent is a discrete action, so Z m looks like a Feynman path integral with weight e to the minus S over h bar. Our notes also take a faster route for hydrogen. Rotating t to minus i tau in the classical action flips the sign of the kinetic term, the action becomes i times the Euclidean action, and the phase becomes a real, positive statistical weight.

## 9. Monte Carlo meets the weight of the potential

*Our notes · pp. 8–9* · 86 words

Pages eight and nine are where hydrogen breaks. To sample paths by Monte Carlo we discretise the Euclidean action with m beads. The weight of the potential at each bead is dimensionless and grows without bound as r goes to zero. Integrated over a small ball, the r squared from the volume element does not compensate it, and the integral diverges. Our notes conclude that the sum diverges and that the kinetic term does not compensate either. Next: what we found when we checked these claims.

## 10. Proof that one bead diverges

*Results · item 2* · 94 words

Now the results. Being unbounded is not enough to diverge, since one over r is unbounded and still integrable, so item two needs a proof. Since e to the x is at least x cubed over six, r squared times the weight is at least a cubed over six r, and the integral diverges like the log of the cutoff. The true growth is much faster. The figure shows why a numerical check can miss it: the integral looks converged until the cutoff passes delta tau over fifteen, then gains thirty-three orders of magnitude.

## 11. The kinetic term cannot compensate

*Results · item 4* · 88 words

Item four says the kinetic term does not compensate, and it was asserted without proof. Keep every bead inside the unit ball: no spring stretches by more than two, so every spring factor is at least a fixed positive number. Integrating the other beads leaves the one-bead integral, so Z m is infinite for every m and every slice. A spring factor is largest when its two beads coincide, so collapsing onto the nucleus costs nothing. With a cutoff, the springs do not even change the leading growth.

## 12. The exact kernel is finite at the nucleus

*Results · the exact problem* · 96 words

Is the exact problem itself sick at the nucleus? It is not. Minus one over r belongs to the Kato class, and for such potentials the exact imaginary-time kernel is finite everywhere, including at r equal to zero. At the origin it is a sum over bound states plus the continuum: at tau equal to one, 0.91957, checked by a second route. The trace, however, is infinite: level n has n squared states, far from the nucleus. So the energy has to come from the matrix element our notes end with, the kernel at a point.

## 13. Time slicing needs a potential bounded below

*Results · the step of p. 5* · 92 words

Why does the slicing of page five fail when the exact problem is fine? Splitting each segment and letting m grow is the Trotter product formula. In real time it needs self-adjoint operators with a self-adjoint sum, and hydrogen satisfies both. In imaginary time it also needs both operators bounded below. The kinetic energy is; minus k over r is not. The exact kernel averages the potential along continuous paths, which spend almost no time at the nucleus, while slicing samples it at points, and one point can sit on the nucleus.

## 14. What changed in our notes

*Results* · 81 words

Putting it together for our notes. The closed paths of page four are right, but for hydrogen Z is infinite, so ground-state dominance cannot be applied to it directly. The Taylor argument of page five fails near the nucleus. Page six needs delta beta on the potential and, for hydrogen, three dimensions. The claims of pages eight and nine are all correct; we had asserted them, and they are now proved. What we missed is the second divergence, from large distances.

## 15. Summary

*In short* · 89 words

To sum up. Feynman's slicing turns the imaginary-time trace into a closed chain of beads joined by Gaussian springs. For the Coulomb potential the weight at each bead is not integrable at the nucleus, so the bead integral is infinite for every number of segments, and the springs cannot help. The exact kernel is finite, so the failure belongs to the slicing. In the next phase we replace the potential factor in each segment by its average over the free paths of that segment, following Kole and De Raedt.
