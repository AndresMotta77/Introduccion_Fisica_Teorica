# Coverage note — c5_kato_class.py

Check: C5 [N]. The Kato-class quantity, (C1) to (C3). Full discussion, with the verbatim code and output, in `answers/answer-2.md` §4.2.

Required by `CONVENTIONS.md` §1.1: a check with no stated blind spot has not been thought about. The text below is reproduced verbatim from the answer, so that this file can be read on its own.

Output: `c5_kato_class.out` in this directory. Run twice in round 1 and once in round 2, with the code unchanged; all three outputs are byte-identical (compared with `cmp`). The `.out` file is the round-2 output.

This check has two runs. Run 1 is `c5_kato_class_run1_scipy.py` with `c5_kato_class_run1_scipy.out`, and it FAILED its comparison with the recalled Newton formula. Run 2 is `c5_kato_class.py`, which changes only the quadrature method. The answer reports both runs.

---

What it tests. It computes $f_\delta(\mathbf x)$ by quadrature in coordinates centred at $\mathbf x$, for $|\mathbf x|/\delta\in\{0,0.1,0.5,0.99,1,1.5,3\}$ and $\delta\in\{0.1,1\}$. It compares the result with the derived bound $4\pi\delta$, and with a closed form based on Newton's theorem [R], which is not used in the derivation.

What it would have caught. A wrong bound (C3).

What it would not have caught. Whether the Kato class is the right hypothesis for the cited kernel theorem.

Run 1 failed. It used scipy's QUADPACK and reported disagreement with the recalled Newton formula at $|\mathbf x|/\delta=0.99$ ($1.6\times10^{-7}$ against a tolerance of $10^{-7}$). QUADPACK issued non-convergence warnings during the run. Python shows each warning only once, so the run does not say which rows triggered them. The inner integrand has an integrable singularity at $c=-1$ when $s=|\mathbf x|$, which lies inside the integration range for every $0<|\mathbf x|<\delta$. The comment at the head of the run-2 script attributes the warnings to the $0.99$ row specifically; that overstates what run 1 shows. The bound check passed at every point in run 1.

What I changed. I changed the check, not the derivation: only the quadrature method (to mpmath's tanh-sinh, with the outer integral split at $s=|\mathbf x|$). The tolerance, the formula and the bound are unchanged. Run 2 passes all criteria, with the bound attained at $\mathbf x=\mathbf 0$.

Run 1 code and output:
