# Coverage note — check3_slow_frequency.py

Checks: N3. Full discussion, with the verbatim output, in
`answers/answer-2.md` §4.3 — "4.3 Check N3 — the slow frequency, measured from the exact equation".

Required by `CONVENTIONS.md` §1.1: a check with no stated blind spot has not
been thought about. Both halves are reproduced here verbatim from the answer so
that this file can be read on its own.

Output: `out_check3.txt` in this directory.

---

What this would have caught: any wrong numerical factor or wrong power in (41).
The three mutants — $\Omega^2=A^2\omega^2/l^2-g/l$,
$\Omega^2=A^2\omega^2/(4l^2)-g/l$, and $\Omega^2=A^2\omega^2/(2l^2)+g/l$ — are
rejected with relative errors of 66%, 34% and 48% against
$1.7\times10^{-4}$ for the claim. It would also have caught a wrong averaged
equation (28), since column (b) compares directly against it.

What it would **not** have caught: an error shared between (16) and the
integrator — but (16) is what N1 and N2 test, so the chain is closed. It does
not probe large slow amplitudes: $\theta(0)=0.02$ rad was used deliberately to
keep the anharmonic term small, so the check says nothing about the accuracy of
$\Omega$ as a description of motion with $|\Theta|$ approaching
$\Theta_{\rm c}$. It also does not test the stability threshold, only the
frequency above it, and it cannot distinguish (41) from any formula agreeing
with it to $O(\varepsilon^2)$.

