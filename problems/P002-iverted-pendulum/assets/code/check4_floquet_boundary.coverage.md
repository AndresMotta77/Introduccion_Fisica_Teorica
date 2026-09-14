# Coverage note — check4_floquet_boundary.py

Checks: N4. Full discussion, with the verbatim output, in
`answers/answer-2.md` §4.4 — "4.4 Check N4 — the stability threshold, by exact Floquet theory".

Required by `CONVENTIONS.md` §1.1: a check with no stated blind spot has not
been thought about. Both halves are reproduced here verbatim from the answer so
that this file can be read on its own.

Output: `out_check4.txt` in this directory.

---

What this would have caught: a wrong numerical factor in (37), decisively. The
mutation block shows the exact computation selecting $\varepsilon^2/2$ to six
digits while returning $0.4999$ against $\varepsilon^2$, $1.9999$ against
$\varepsilon^2/4$ and $0.0125$ against $\varepsilon/2$. A wrong power of
$\varepsilon$ is rejected by the last of these at a glance. The $\varepsilon=0$
sanity block reproduces $\operatorname{tr}M=2\cosh(2\pi\sqrt G)$ to ten digits,
so the monodromy integration itself is verified against a closed form.

What it would **not** have caught: anything about the nonlinear dynamics — this
is a linear stability statement about $\Theta=0$ only, and says nothing about
$\Theta_{\rm c}$, about the slow frequency, or about what happens after the
pendulum falls. It also examines only the lowest boundary; at larger
$\varepsilon$ there are further instability tongues, which are outside the
$\varepsilon$ range scanned. And it assumes (16), so it inherits whatever N1 and
N2 do not exclude.

