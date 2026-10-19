# Coverage note — c3_chapman_kolmogorov.py

Check: C3 [N]. Composition law of the free kernel, (B12). Full discussion, with the verbatim code and output, in `answers/answer-2.md` §4.2.

Required by `CONVENTIONS.md` §1.1: a check with no stated blind spot has not been thought about. The text below is reproduced verbatim from the answer, so that this file can be read on its own.

Output: `c3_chapman_kolmogorov.out` in this directory. Run twice in round 1 and once in round 2, with the code unchanged; all three outputs are byte-identical (compared with `cmp`). The `.out` file is the round-2 output.

---

What it tests. (i) The completing-the-square identity of B.4, symbolically, with the two sides written independently. (ii) The one-dimensional composition integral by quadrature, against the closed form, at twelve parameter sets, including extreme ratios $s/t$ and large separations.

What it would have caught. An error in the composition law or in its normalisation, either of which would invalidate (B13).

What it would not have caught. Anything involving $V$.

Assumptions. [A] $s,t>0$, declared in the code; imaginary-time steps are positive.

Outcome. All twelve parameter sets agree to $1.2\times10^{-15}$ or better, and the symbolic difference is identically zero.
