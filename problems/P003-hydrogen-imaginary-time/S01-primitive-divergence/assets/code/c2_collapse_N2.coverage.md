# Coverage note — c2_collapse_N2.py

Check: C2 [N]. Can the kinetic factors compensate? The $N=2$ integral with a cutoff, (B16) to (B18). Full discussion, with the verbatim code and output, in `answers/answer-2.md` §4.2.

Required by `CONVENTIONS.md` §1.1: a check with no stated blind spot has not been thought about. The text below is reproduced verbatim from the answer, so that this file can be read on its own.

Output: `c2_collapse_N2.out` in this directory. Run twice in round 1 and once in round 2, with the code unchanged; all three outputs are byte-identical (compared with `cmp`). The `.out` file is the round-2 output.

---

What it tests. In part (a), it uses Monte Carlo over independent random directions to test the angular identity (B17) independently of its derivation (seed 20261019, 400 000 pairs per $\kappa$). In part (b), it computes $R(\eta)$, the full $N=2$ bead integral with cutoff divided by the same integral with the kinetic factor replaced by its maximum, for $\Delta\tau=1$, $L=1.5$, and five values of $\eta$. The input is the $N=2$ integrand of (A3), which comes from the problem statement and the given kernel. "The kinetic factor compensates" would show up as $R\to0$.

What it would have caught. Compensation; a wrong kinetic exponent at $N=2$; a wrong angular reduction (through part (a)); a wrong small-$\eta$ expansion (B18).

What it would not have caught. Anything at $N\ge3$, which only the general bounds (B14) to (B16) cover; the large-volume divergence, since the beads are confined to $B_L$; the overall prefactor, which cancels in $R$.

Assumptions. [A] Two independent, uniformly distributed directions have $\cos\theta_{12}$ uniform on $[-1,1]$; this is what (B17) uses. The Monte Carlo samples directions directly as normalised Gaussian vectors, so it does not rely on that fact.

Outcome. All criteria pass. $R$ increases towards 1, and at $\eta=0.0125$, $(1-R)/(2\eta^2/\Delta\tau)=1.0272$, against a prediction of about $1+2\eta/\Delta\tau=1.025$. At $\eta=0.2$ and $0.1$ the region away from the origin still dominates and $R$ is small; this is expected, and no criterion was placed on those rows except $R\le1$ and the monotonic decrease of $1-R$.
