# P003.S01 — Failure of the primitive path integral at r = 0 for the Coulomb potential

Final document. It is derived from `answers/answer-2.md`, the last answer of the loop, by removing the parts that belong elsewhere in the folder. It is not a rewrite. Every equation, number and output below is the text of `answer-2.md`, and the section and equation numbering is unchanged, so the audit trail and the provenance ledger still point at the same places.

| | |
|---|---|
| Problem | P003.S01, failure of the primitive path integral at $r=0$ for the Coulomb potential |
| Container | P003, Guide 15, Project 04: the hydrogen ground state from imaginary time (`../PLAN.md`, chunk K1) |
| Course | Introduction to Theoretical Physics |
| Opened / closed | 2026-10-19 / 2026-10-19 |
| Rounds | 1 (verdict ACCEPT; one NIT, accepted) |
| Solver | Claude Opus 5.5 (`claude-opus-5-5`, self-reported), effort extra (user-reported, prompt0 §0) |
| Auditor | Gemini (self-reported), effort high (self-reported); no code execution, no web |
| Result | $Z_N=+\infty$ for every $N\ge1$ and $\Delta\tau>0$. The exact kernel is finite everywhere ($K_1(\mathbf 0,\mathbf 0)=0.91957$), and the exact trace is infinite for a different reason. The imaginary-time Trotter formula needs $V$ bounded below, and $-1/r$ is not |

The following parts of `answer-2.md` are not reproduced here. The section numbers below keep the gaps rather than closing them.

- The run note at its head is replaced by the table above.
- §1, the prior-knowledge declaration, and §6, the convergence check, are in `sources/independence.md`.
- §10, the response to audit 1, is in `audits/findings.yaml`, with the audit itself in `audits/audit-report-1.md`; its check C6 is in `assets/code/`.

The provenance of every tagged claim is in `sources/provenance.md`. Tag meanings are in `templates/CONVENTIONS.md` §1.

> ## Release gates: 3 of 14 failed
>
> Stamped here by `/log` per `skills/log/SKILL.md` step 2, which requires a failed gate to be recorded in `meta.yaml` and in a banner at the top of this file rather than quietly fixed. The user closed the loop with these failures on record. None of the three touches a derivation step or a number.
>
> `no_unflagged_recall`, fail. Two `[R]` tags are not in the Risk register (§7): the proton radius in §4.1 item 6, and "$R_{nl}(0)=0$ for $l\ge1$" in the coverage note of check C4. Neither is load-bearing. They are not added here, because step 3 of the log skill forbids editing the final document.
>
> `code_audited`, fail. The audit's pass 6 is one line, "Code was audited by reading; execution not performed in this session", and it reviews no check for circularity, vacuity or laundered assumptions. Check C6, added in round 2, was never seen by the auditor.
>
> `latex_clean`, fail. `final.pdf` compiles with no undefined references, no undefined citations, no missing characters and no `\emph`, but two overfull boxes exceed 10 pt: 39.1 pt and 34.8 pt. They are the display equations (A3) and (B10), which are wider than the text block. Both are typographic and are left as they are, for the same step-3 reason. Five overfull rows in the provenance table, which `/log` authors, were cleared by widening its columns.
>
> The other eleven gates pass.

---

## 2. Setup

### 2.1 Conventions

Atomic units throughout: $\hbar=m_e=e^2/4\pi\varepsilon_0=1$. Lengths are in Bohr radii $a_0$; imaginary time and inverse temperature are in $\hbar/E_h$. $B_\varepsilon(\mathbf x)$ is the open ball of radius $\varepsilon$ centred at $\mathbf x$, and $B_\varepsilon=B_\varepsilon(\mathbf 0)$. $|A|$ is the Lebesgue measure of $A\subset\mathbb R^3$. "Kernel" means the integral kernel in the position representation.

### 2.2 Symbol table

| Symbol | Meaning |
|---|---|
| $\mathbf r\in\mathbb R^3$, $r=\lvert\mathbf r\rvert$ | position; distance from the nucleus |
| $K=-\tfrac12\nabla^2$ | kinetic energy operator on $L^2(\mathbb R^3)$ |
| $V(\mathbf r)=-1/r$ | attractive Coulomb potential |
| $H=K+V$ | hydrogen Hamiltonian, infinitely heavy nucleus |
| $\beta>0$ | total imaginary time |
| $N\ge1$ | number of time slices (beads) |
| $\Delta\tau=\beta/N$ | slice width |
| $\rho_0(\mathbf r,\mathbf r';t)$ | free kernel $(2\pi t)^{-3/2}\exp(-\lvert\mathbf r-\mathbf r'\rvert^2/2t)$, given in prompt 3a |
| $T=e^{-\Delta\tau K}e^{-\Delta\tau V}$ | one-slice primitive operator |
| $w(\mathbf r)=e^{-\Delta\tau V(\mathbf r)}=e^{\Delta\tau/r}$ | potential weight of one bead |
| $\mathbf r_1,\dots,\mathbf r_N$ | bead positions, with $\mathbf r_{N+1}\equiv\mathbf r_1$ |
| $Z_N(\beta)$, $P_N$ | primitive trace defined by (A3), and its integrand |
| $Z_N^{(L)}$, $Z_N^{(L)}(\eta)$ | (A3) with all beads in $B_L$; and additionally with $\lvert\mathbf r_j\rvert>\eta$ |
| $\rho_N(\mathbf r,\mathbf r')$ | primitive kernel $\langle\mathbf r\rvert T^N\lvert\mathbf r'\rangle$ written as a bead integral, (B10) |
| $I_a(\eta,\varepsilon)$ | $4\pi\int_\eta^\varepsilon r^2e^{a/r}\,dr$, with $a>0$ |
| $K_\tau(\mathbf r,\mathbf r')$ | exact kernel $\langle\mathbf r\rvert e^{-\tau H}\lvert\mathbf r'\rangle$ |
| $f_\delta(\mathbf x)$ | Kato-class quantity $\int_{B_\delta(\mathbf x)}d^3y/(\lvert\mathbf y\rvert\lvert\mathbf x-\mathbf y\rvert)$ |
| $\mu,\hbar,k,\Delta\beta,m$ | the notes' mass, Planck constant, $k=e^2/4\pi\varepsilon_0$, slice width and number of slices |

### 2.3 The problem restated

(a) Write $Z_N(\beta)=\operatorname{Tr}\big(e^{-\Delta\tau K}e^{-\Delta\tau V}\big)^N$, with $\Delta\tau=\beta/N$, as an integral over $N$ bead positions in $\mathbb R^3$, keeping every prefactor.

(b) Decide whether $Z_N$ is finite for all $N\ge1$ and $\Delta\tau>0$, and prove the answer. If it is not, identify the configurations responsible and decide whether the kinetic factors can compensate.

(c) Decide whether $K_\tau(\mathbf r,\mathbf r')$ and $\operatorname{Tr}e^{-\beta H}$ are finite. State the theorem that justifies time slicing, and identify which of its hypotheses $-1/r$ violates.

The free kernel $\rho_0$ is given and trusted (prompt 3a). Everything in the notes is treated as a hypothesis, H1 to H6, and assessed in Part D.

### 2.4 Dictionary to the notes

The notes keep $\hbar$, $\mu$ and $k$. They write $\beta=\tau/\hbar$ (p. 4), $\Delta\beta=\beta/m$, and $\Delta\tau_{\rm notes}=\hbar\Delta\beta$ (p. 7). The correspondence is:

- the prompt's $\Delta\tau$, an inverse energy, is the notes' $\Delta\beta$;
- the prompt's $N$ is the notes' $m$;
- $\mu\to1$, $\hbar\to1$, $k\to1$.

With $\hbar=1$ the notes' $\Delta\tau$ and $\Delta\beta$ coincide numerically, as the notes say on p. 9. The notes' potential weight $w_{\rm pot}=e^{\Delta\tau_{\rm notes}k/(\hbar r)}=e^{\Delta\beta k/r}$ becomes $e^{\Delta\tau/r}$.

## 3. Derivation

### Part A. The primitive trace as a bead integral

[D] Write $Z_N=\operatorname{Tr}T^N$ with $T=e^{-\Delta\tau K}e^{-\Delta\tau V}$. Take the trace in the position representation and insert the resolution of the identity $1=\int d^3r\,|\mathbf r\rangle\langle\mathbf r|$ between consecutive factors of $T$:

$$Z_N=\int d^3r_1\,\langle\mathbf r_1|T\,T\cdots T|\mathbf r_1\rangle=\int d^3r_1\cdots d^3r_N\,\langle\mathbf r_1|T|\mathbf r_N\rangle\langle\mathbf r_N|T|\mathbf r_{N-1}\rangle\cdots\langle\mathbf r_2|T|\mathbf r_1\rangle .\tag{A1}$$

With the label $\mathbf r_{N+1}\equiv\mathbf r_1$, the product is $\prod_{j=1}^N\langle\mathbf r_{j+1}|T|\mathbf r_j\rangle$.

[D] Since $V$ is a multiplication operator, $e^{-\Delta\tau V}|\mathbf r_j\rangle=e^{-\Delta\tau V(\mathbf r_j)}|\mathbf r_j\rangle$. Combining this with the given free kernel,

$$\langle\mathbf r_{j+1}|e^{-\Delta\tau K}e^{-\Delta\tau V}|\mathbf r_j\rangle=e^{-\Delta\tau V(\mathbf r_j)}\rho_0(\mathbf r_{j+1},\mathbf r_j;\Delta\tau)=(2\pi\Delta\tau)^{-3/2}\exp\Big(-\frac{|\mathbf r_{j+1}-\mathbf r_j|^2}{2\Delta\tau}\Big)\,e^{\Delta\tau/r_j}.\tag{A2}$$

The potential is evaluated at the right-hand point of each link because $V$ stands to the right of $K$ in $T$.

[D] Multiply the $N$ factors (A2). The prefactors give $(2\pi\Delta\tau)^{-3N/2}$, and the product of exponentials is the exponential of the sum:

$$Z_N(\beta)=(2\pi\Delta\tau)^{-3N/2}\int_{\mathbb R^{3N}}d^3r_1\cdots d^3r_N\,\exp\Big\{-\sum_{j=1}^{N}\Big[\frac{|\mathbf r_{j+1}-\mathbf r_j|^2}{2\Delta\tau}-\frac{\Delta\tau}{r_j}\Big]\Big\},\qquad \mathbf r_{N+1}\equiv\mathbf r_1,\quad\Delta\tau=\beta/N.\tag{A3}$$

Call the integrand $P_N$. The first term in the bracket is the discretised kinetic action, and the second is $\Delta\tau\,V(\mathbf r_j)$ with $V=-1/r$.

[A1] I take (A3) as the definition of $Z_N$.

- Why this is legitimate. $P_N$ is a nonnegative measurable function on $\mathbb R^{3N}$. Its Lebesgue integral therefore exists in $[0,+\infty]$, and by Tonelli's theorem it equals every iterated integral, taken in any order. No exchange of limits is involved.
- Why a definition is needed. For this $V$, steps (A1) and (A2) are formal. Remark B.6 shows that $T$ is unbounded and that $T^N$ with $N\ge2$ is defined only on the zero vector, so $\operatorname{Tr}T^N$ has no operator meaning here.
- What changes if it is wrong. If one insists on an operator trace, the answer to (b) becomes stronger: the object does not exist at all.
- For a bounded $V$, the same steps compose integral operators with nonnegative kernels and give the same formula.

[D] In the notes' units (dictionary 2.4), the same formula reads

$$Z_m=\Big(\frac{\mu}{2\pi\hbar^2\Delta\beta}\Big)^{3m/2}\int\prod_{j=1}^m d^3r_j\,\exp\Big\{-\sum_{j=1}^m\Big[\frac{\mu|\mathbf r_{j+1}-\mathbf r_j|^2}{2\hbar^2\Delta\beta}+\Delta\beta\,V(\mathbf r_j)\Big]\Big\},\qquad V=-k/r.\tag{A4}$$

Two properties of (A3) are used later.

- The bead labels are cyclic: $P_N$ is unchanged when every $\mathbf r_j$ is replaced by $\mathbf r_{j+1}$ at once. So anything proved for bead 1 holds for every bead.
- Reversing the order of the factors in $T$ (writing $e^{-\Delta\tau V}e^{-\Delta\tau K}$) moves the potential to the left-hand point of each link. After relabelling $j\to j+1$ the bead integral is the same, so (A3) does not depend on that choice.

Confidence for Part A: high. The only thing that would lower it is a different intended ordering or a symmetric splitting, and either leaves (A3) unchanged.

### Part B. $Z_N$ is infinite for every $N\ge1$ and every $\Delta\tau>0$

The claim is $Z_N(\beta)=+\infty$ for all $N\ge1$ and $\Delta\tau>0$. Two separate mechanisms produce it.

- Configurations with a bead near the origin. This one is specific to time slicing.
- The chain as a whole moving off to infinity. The exact trace shares this one.

Both are proved below, and then separated.

#### B.1 The one-bead radial integral

[D] For $x\ge0$, every term of $e^x=\sum_n x^n/n!$ is nonnegative. Keeping only the cubic term,

$$e^x\ge\frac{x^3}{6}\qquad(x\ge0).\tag{B1}$$

[D] Take $a>0$ and $0<\eta<\varepsilon$. Apply (B1) with $x=a/r>0$, multiply by $r^2$, and integrate:

$$I_a(\eta,\varepsilon)=4\pi\int_\eta^\varepsilon r^2e^{a/r}\,dr\ \ge\ 4\pi\int_\eta^\varepsilon r^2\,\frac{a^3}{6r^3}\,dr=\frac{2\pi a^3}{3}\int_\eta^\varepsilon\frac{dr}{r}=\frac{2\pi a^3}{3}\ln\frac{\varepsilon}{\eta}.\tag{B2}$$

The right side tends to $+\infty$ as $\eta\to0^+$, and $I_a(\eta,\varepsilon)$ increases as $\eta$ decreases. By monotone convergence,

$$\int_{B_\varepsilon}e^{a/r}\,d^3r=I_a(0,\varepsilon)=+\infty\qquad\text{for every }a>0,\ \varepsilon>0.\tag{B3}$$

The power 3 in (B1) is the smallest that works. The measure $r^2\,dr$ needs a factor $r^{-3}$ to produce a logarithm, so any power $n\ge3$ gives a divergence, while $n\le2$ would leave the bound inconclusive.

[D] Now the growth law with an inner cutoff. Substitute $u=a/r$, so $r=a/u$, $dr=-a\,u^{-2}\,du$ and $r^2\,dr=-a^3u^{-4}\,du$. The limits $r=\eta$ and $r=\varepsilon$ become $U=a/\eta$ and $U_0=a/\varepsilon$:

$$I_a(\eta,\varepsilon)=4\pi a^3\int_{U_0}^{U}u^{-4}e^{u}\,du.\tag{B4}$$

From $\frac{d}{du}\big(e^uu^{-n}\big)=e^uu^{-n}-n\,e^uu^{-n-1}$,

$$\int_{U_0}^{U}e^uu^{-n}\,du=\Big[e^uu^{-n}\Big]_{U_0}^{U}+n\int_{U_0}^{U}e^uu^{-n-1}\,du.\tag{B5}$$

Applying (B5) with $n=4$, then $n=5$, then $n=6$:

$$\int_{U_0}^{U}e^uu^{-4}\,du=\Big[e^u\big(u^{-4}+4u^{-5}+20u^{-6}\big)\Big]_{U_0}^{U}+120\int_{U_0}^{U}e^uu^{-7}\,du .$$

For $U>2U_0$, split the last integral at $U/2$.

- On $[U_0,U/2]$, $e^u\le e^{U/2}$, so this piece is at most $e^{U/2}\int_{U_0}^{\infty}u^{-7}du=e^{U/2}U_0^{-6}/6$.
- On $[U/2,U]$, $u^{-7}\le(U/2)^{-7}$, so this piece is at most $2^7U^{-7}\int_{U/2}^{U}e^u\,du\le2^7U^{-7}e^U$.

Both pieces are $O(e^UU^{-7})$ as $U\to\infty$; the first because $e^{U/2}$ grows more slowly than $e^UU^{-7}$. The boundary terms at $U_0$ do not depend on $\eta$. So, as $\eta\to0$ with $a$ and $\varepsilon$ fixed,

$$I_a(\eta,\varepsilon)=4\pi a^3e^{a/\eta}\Big[\Big(\frac{\eta}{a}\Big)^4+4\Big(\frac{\eta}{a}\Big)^5+20\Big(\frac{\eta}{a}\Big)^6+O\Big(\Big(\frac{\eta}{a}\Big)^7\Big)\Big],\qquad I_a(\eta,\varepsilon)\simeq\frac{4\pi\eta^4e^{a/\eta}}{a}.\tag{B6}$$

One more application of (B5) gives 120 as the coefficient of $(\eta/a)^7$. The integrand $e^{a/r}$ drops by a factor $e$ between $r=\eta$ and $r\approx\eta+\eta^2/a$, so the integral is dominated by a shell of thickness $\eta^2/a$ at the cutoff. Check C1 tests (B2) and (B6) against direct quadrature.

#### B.2 Configurations with one bead near the origin

[D] Fix $N\ge1$, $\Delta\tau>0$ and $0<\varepsilon\le1$, and define

$$D_\varepsilon=\{\mathbf r_1\in B_\varepsilon\}\times\{\mathbf r_k\in B_1,\ k=2,\dots,N\}\subset\mathbb R^{3N}$$

(for $N=1$, $D_\varepsilon=B_\varepsilon$). On $D_\varepsilon$ every bead lies in $B_1$. By the triangle inequality, every link then satisfies $|\mathbf r_{k+1}-\mathbf r_k|\le|\mathbf r_{k+1}|+|\mathbf r_k|<2$, including the closing link from $\mathbf r_N$ to $\mathbf r_{N+1}=\mathbf r_1$. Hence each kinetic factor obeys

$$\exp\Big(-\frac{|\mathbf r_{k+1}-\mathbf r_k|^2}{2\Delta\tau}\Big)\ \ge\ e^{-4/(2\Delta\tau)}=e^{-2/\Delta\tau}\qquad\text{on }D_\varepsilon.\tag{B7}$$

For $N=1$ the only link has length $|\mathbf r_1-\mathbf r_1|=0$, so its factor equals 1, which also satisfies (B7). Since $V<0$ everywhere, $w(\mathbf r_k)=e^{\Delta\tau/r_k}\ge1$ for $k=2,\dots,N$. Putting these together, on $D_\varepsilon$:

$$P_N\ \ge\ (2\pi\Delta\tau)^{-3N/2}\,e^{-2N/\Delta\tau}\,e^{\Delta\tau/r_1}.\tag{B8}$$

$P_N\ge0$ everywhere, so the integral over $\mathbb R^{3N}$ is at least the integral over $D_\varepsilon$. Integrate the right side of (B8) over $D_\varepsilon$. The $N-1$ beads confined to $B_1$ contribute $|B_1|^{N-1}=(4\pi/3)^{N-1}$, so

$$Z_N\ \ge\ (2\pi\Delta\tau)^{-3N/2}\,e^{-2N/\Delta\tau}\Big(\frac{4\pi}{3}\Big)^{N-1}\int_{B_\varepsilon}e^{\Delta\tau/r_1}\,d^3r_1=+\infty\tag{B9}$$

by (B3) with $a=\Delta\tau$. This proves $Z_N=+\infty$ for every $N\ge1$ and $\Delta\tau>0$. By cyclic symmetry, any bead can play the role of bead 1.

[D] The same argument works in localised forms.

- Confining every bead to $B_\ell$ with $\ell=\min(L,1)$ gives $Z_N^{(L)}=+\infty$ for every $L>0$. What matters is only where the beads are relative to the origin. Any region of configuration space that contains a neighbourhood of the origin for one bead, with the other beads in a bounded set, carries infinite weight.
- For the primitive kernel with $N\ge2$, define

$$\rho_N(\mathbf r,\mathbf r')=\langle\mathbf r|T^N|\mathbf r'\rangle:=(2\pi\Delta\tau)^{-3N/2}\int\prod_{j=2}^{N}d^3r_j\,\prod_{j=1}^{N}\exp\Big(-\frac{|\mathbf r_{j+1}-\mathbf r_j|^2}{2\Delta\tau}\Big)e^{\Delta\tau/r_j},\qquad\mathbf r_1=\mathbf r',\ \mathbf r_{N+1}=\mathbf r .\tag{B10}$$

  Restrict the intermediate bead $\mathbf r_2$ to $B_\varepsilon$ and $\mathbf r_3,\dots,\mathbf r_N$ to $B_1$. Every link then has length at most $|\mathbf r|+|\mathbf r'|+2$, so every kinetic factor is bounded below by a positive constant that depends on $|\mathbf r|$ and $|\mathbf r'|$. Hence $\rho_N(\mathbf r,\mathbf r')=+\infty$ for every pair of points when $N\ge2$.
- For $N=1$, $\rho_1(\mathbf r,\mathbf r')=\rho_0(\mathbf r,\mathbf r';\Delta\tau)\,e^{\Delta\tau/r'}$ is finite for $\mathbf r'\ne\mathbf 0$, but by (B3) it is not locally integrable in $\mathbf r'$ at $\mathbf r'=\mathbf 0$.

#### B.3 Inside a bounded region, the origin is the only source

[D] Take $0<\delta<L$ and confine every bead to the shell $\delta<|\mathbf r_j|<L$. There each kinetic factor is at most 1 and each potential factor is at most $e^{\Delta\tau/\delta}$, so

$$Z_N^{(L)}(\delta)\ \le\ (2\pi\Delta\tau)^{-3N/2}\,e^{N\Delta\tau/\delta}\Big(\frac{4\pi L^3}{3}\Big)^N<\infty .\tag{B11}$$

So within any bounded region, the divergence comes entirely from configurations in which at least one bead approaches the origin, and B.2 shows that one such bead is enough.

#### B.4 The chain moving off to infinity

[D] First, how free kernels compose. For one Cartesian component, with $s,t>0$, complete the square in $y$:

$$-\frac{(x-y)^2}{2s}-\frac{(y-z)^2}{2t}=-\frac{s+t}{2st}\Big(y-\frac{tx+sz}{s+t}\Big)^2-\frac{(x-z)^2}{2(s+t)} .$$

Integrate over $y\in\mathbb R$, using $\int\exp\!\big(-(s+t)(y-c)^2/2st\big)\,dy=\big(2\pi st/(s+t)\big)^{1/2}$:

$$\int_{\mathbb R}\frac{e^{-(x-y)^2/2s}}{\sqrt{2\pi s}}\,\frac{e^{-(y-z)^2/2t}}{\sqrt{2\pi t}}\,dy=\frac{1}{\sqrt{2\pi s}\sqrt{2\pi t}}\sqrt{\frac{2\pi st}{s+t}}\,e^{-(x-z)^2/2(s+t)}=\frac{e^{-(x-z)^2/2(s+t)}}{\sqrt{2\pi(s+t)}} .$$

The three-dimensional kernel is a product of three such factors, so

$$\int_{\mathbb R^3}\rho_0(\mathbf x,\mathbf y;s)\,\rho_0(\mathbf y,\mathbf z;t)\,d^3y=\rho_0(\mathbf x,\mathbf z;s+t).\tag{B12}$$

Check C3 tests (B12).

[D] Next, a lower bound by the free chain. Since $e^{\Delta\tau/r_j}\ge1$,

$$P_N\ge(2\pi\Delta\tau)^{-3N/2}\exp\Big(-\sum_j\frac{|\mathbf r_{j+1}-\mathbf r_j|^2}{2\Delta\tau}\Big)=\prod_j\rho_0(\mathbf r_{j+1},\mathbf r_j;\Delta\tau).$$

Integrate out the beads one at a time with (B12), using the symmetry $\rho_0(\mathbf x,\mathbf y)=\rho_0(\mathbf y,\mathbf x)$:

- over $\mathbf r_2$: $\int\rho_0(\mathbf r_3,\mathbf r_2;\Delta\tau)\rho_0(\mathbf r_2,\mathbf r_1;\Delta\tau)\,d^3r_2=\rho_0(\mathbf r_3,\mathbf r_1;2\Delta\tau)$;
- over $\mathbf r_3$: $\int\rho_0(\mathbf r_4,\mathbf r_3;\Delta\tau)\rho_0(\mathbf r_3,\mathbf r_1;2\Delta\tau)\,d^3r_3=\rho_0(\mathbf r_4,\mathbf r_1;3\Delta\tau)$;
- and so on. After $N-1$ steps what remains is $\rho_0(\mathbf r_{N+1},\mathbf r_1;N\Delta\tau)=\rho_0(\mathbf r_1,\mathbf r_1;\beta)=(2\pi\beta)^{-3/2}$. For $N=1$ no integration is needed.

Hence

$$Z_N\ \ge\ \int_{\mathbb R^3}(2\pi\beta)^{-3/2}\,d^3r_1=+\infty .\tag{B13}$$

This divergence has nothing to do with $r=0$. It is present for $V\equiv0$, where $Z_N=\operatorname{Tr}e^{-\beta K}=\infty$, and it comes from the region where all beads are far from the origin: translating a compact chain to infinity costs nothing. Part C shows the exact trace diverges for the same reason.

The problem asks for "the region responsible". There are two.

- The neighbourhoods $\{\mathbf r_j\in B_\varepsilon\}$ of the origin cause the failure specific to time slicing (B.2), and they are the only source inside bounded regions (B.3).
- The region at infinity produces a second divergence, which the continuum shares (B.4 and C.4).

#### B.5 The kinetic factors cannot compensate

Three statements, from weakest to strongest.

[D] First, the kinetic weight satisfies $\prod_j\rho_0(\mathbf r_{j+1},\mathbf r_j;\Delta\tau)\le(2\pi\Delta\tau)^{-3N/2}$, with equality exactly when all beads coincide. In particular it is maximal on the fully collapsed configuration $\mathbf r_1=\dots=\mathbf r_N=\mathbf 0$, which is where the potential weight is most singular. The kinetic factor penalises the separation between neighbouring beads. It does not penalise a bead's distance from the origin.

[D] Second, for one bead's integral to converge at the origin, the kinetic factor would have to vanish as $\mathbf r_j\to\mathbf 0$ fast enough to make $r_j^2e^{\Delta\tau/r_j}\times(\text{kinetic factor})$ integrable. But the kinetic factor depends on $\mathbf r_j$ only through $\mathbf r_j-\mathbf r_{j\pm1}$, is continuous, and is strictly positive at $\mathbf r_j=\mathbf 0$ for fixed neighbours. That is what (B7) to (B9) express.

[D] Third, the kinetic factors do not even change the leading growth. Impose the inner cutoff $\eta$ on every bead and confine all beads to $B_L$, with $0<\eta<L$. Every kinetic factor is at most 1, so

$$Z_N^{(L)}(\eta)\ \le\ (2\pi\Delta\tau)^{-3N/2}\,I_{\Delta\tau}(\eta,L)^N .\tag{B14}$$

For a lower bound, fix $\theta>0$ with $\eta(1+\theta)<L$, and keep only configurations with every bead in the thin shell $\eta<|\mathbf r_j|<\eta(1+\theta)$. There each link has length at most $2\eta(1+\theta)$, so the kinetic exponent is at least $-N\big(2\eta(1+\theta)\big)^2/(2\Delta\tau)=-2N\eta^2(1+\theta)^2/\Delta\tau$. The potential factors then integrate bead by bead:

$$Z_N^{(L)}(\eta)\ \ge\ (2\pi\Delta\tau)^{-3N/2}\,e^{-2N\eta^2(1+\theta)^2/\Delta\tau}\,I_{\Delta\tau}\big(\eta,\eta(1+\theta)\big)^N .\tag{B15}$$

To compare the two bounds, write $I(\eta,\eta(1+\theta))=I(\eta,L)-I(\eta(1+\theta),L)$ and bound each piece.

- $I(\eta(1+\theta),L)\le(4\pi/3)L^3e^{\Delta\tau/(\eta(1+\theta))}$: the integrand is at most its value at the inner end, and the volume is at most $|B_L|$.
- $I(\eta,L)\ge4\pi\int_\eta^{\eta(1+\theta/2)}r^2e^{\Delta\tau/r}\,dr\ge4\pi\eta^2(\eta\theta/2)\,e^{\Delta\tau/(\eta(1+\theta/2))}$.

So

$$\frac{I(\eta(1+\theta),L)}{I(\eta,L)}\ \le\ \frac{2L^3}{3\theta\eta^3}\exp\Big[-\frac{\Delta\tau}{\eta}\Big(\frac{1}{1+\theta/2}-\frac{1}{1+\theta}\Big)\Big]\ \longrightarrow\ 0\quad(\eta\to0),$$

because the bracket is positive and the exponential beats any power of $\eta$. Combining (B14), (B15) and $e^{-2N\eta^2(1+\theta)^2/\Delta\tau}\to1$,

$$\lim_{\eta\to0}\frac{Z_N^{(L)}(\eta)}{(2\pi\Delta\tau)^{-3N/2}I_{\Delta\tau}(\eta,L)^N}=1,\qquad Z_N^{(L)}(\eta)\simeq(2\pi\Delta\tau)^{-3N/2}\Big(\frac{4\pi\eta^4e^{\Delta\tau/\eta}}{\Delta\tau}\Big)^N .\tag{B16}$$

The divergence is the $N$-th power of the one-bead divergence, exactly as if every kinetic factor were replaced by its maximum.

[D] For $N=2$ there is a sharper prediction, which check C2 tests.

- The geometry. At $N=2$ the two links put $|\mathbf r_2-\mathbf r_1|^2/\Delta\tau$ in the exponent. With radii $r_1,r_2$ and relative angle $\theta_{12}$, $|\mathbf r_1-\mathbf r_2|^2=r_1^2+r_2^2-2r_1r_2\cos\theta_{12}$. Integrating $\hat{\mathbf r}_2$ over the sphere with polar axis $\hat{\mathbf r}_1$ gives $2\pi\int_{-1}^1dc$; integrating $\hat{\mathbf r}_1$ then gives $4\pi$; and $\int_{-1}^1e^{\kappa c}dc=2\sinh\kappa/\kappa$ with $\kappa=2r_1r_2/\Delta\tau$. So

$$\int d\Omega_1\,d\Omega_2\,e^{-|\mathbf r_1-\mathbf r_2|^2/\Delta\tau}=16\pi^2\,e^{-(r_1^2+r_2^2)/\Delta\tau}\,\frac{\sinh\kappa}{\kappa}.\tag{B17}$$

- The ratio. Let $g(r_1,r_2)$ be (B17) divided by $16\pi^2$, the angular average of the kinetic factor, and let $R(\eta)=Z_2^{(L)}(\eta)/\big[(2\pi\Delta\tau)^{-3}I(\eta,L)^2\big]$. Then $R=\iint\tilde w(r_1)\tilde w(r_2)\,g\,/\big(\int\tilde w\big)^2$ with $\tilde w(r)=r^2e^{\Delta\tau/r}$ on $[\eta,L]$, and since $g\le1$, $R\le1$.
- The deviation. With both radii in the shell, $e^{-s}=1-s+O(s^2)$ and $\sinh\kappa/\kappa=1+\kappa^2/6+O(\kappa^4)$ give $1-g=(r_1^2+r_2^2)/\Delta\tau+O(\eta^4/\Delta\tau^2)$. In the shell the radial weight is approximately $e^{\Delta\tau/\eta}e^{-\Delta\tau(r-\eta)/\eta^2}$, an exponential with mean width $\eta^2/\Delta\tau$, so $\langle r^2\rangle\approx\eta^2+2\eta\cdot\eta^2/\Delta\tau=\eta^2(1+2\eta/\Delta\tau)$. Pairs with a bead outside the shell are suppressed by the vanishing ratio shown above.

Hence

$$1-R(\eta)\ \simeq\ \frac{2\eta^2}{\Delta\tau}\Big(1+\frac{2\eta}{\Delta\tau}+\dots\Big),\qquad R(\eta)\to1^- .\tag{B18}$$

If the kinetic factor compensated the divergence, $R$ would go to 0 instead.

#### B.6 Remark: the divergence is not an artifact of the bead representation

[D] Let $M$ be multiplication by $w(r)=e^{\Delta\tau/r}$ on its maximal domain $D(M)=\{\psi\in L^2:\ w\psi\in L^2\}$, and let $T=e^{-\Delta\tau K}M$ with $D(T)=D(M)$. The claim is that $D(T^N)=\{0\}$ for $N\ge2$, and that $T$ is unbounded.

Proof that $D(T^2)=\{0\}$.

1. Let $\psi\in D(T^2)$. Then $g:=w\psi\in L^2$, and $\varphi:=T\psi=e^{-\Delta\tau K}g$ must lie in $D(M)$.
2. $\varphi$ is real-analytic. It is the convolution of $g$ with the Gaussian $\rho_0(\cdot;\Delta\tau)$, and it extends to an entire function on $\mathbb C^3$. For $\mathbf z=\mathbf x+i\boldsymbol\xi$,
$$\Big|\exp\Big(-\sum_i(z_i-y_i)^2/2\Delta\tau\Big)\Big|=\exp\Big(-\big(|\mathbf x-\mathbf y|^2-|\boldsymbol\xi|^2\big)/2\Delta\tau\Big).$$
Multiplied by $|g(\mathbf y)|$, this is integrable in $\mathbf y$ (by Cauchy–Schwarz, the Gaussian being in $L^2$), locally uniformly in $\mathbf z$. Differentiating under the integral sign then shows holomorphy in each variable.
3. Suppose $\varphi\not\equiv0$. A real-analytic function on a connected open set that vanishes to infinite order at one point vanishes identically [R]. So the Taylor series of $\varphi$ at $\mathbf 0$ has a lowest nonzero homogeneous part $P_k$, of some degree $k\ge0$.
4. $P_k$ cannot vanish on the whole unit sphere, since by homogeneity it would then vanish everywhere. So there is a spherical cap $S_0$ of positive area $\sigma_0$ on which $|P_k|\ge c>0$.
5. Taylor's theorem gives $|\varphi(\mathbf x)-P_k(\mathbf x)|\le C|\mathbf x|^{k+1}$ for $|\mathbf x|\le r_0$. For $\mathbf x=s\boldsymbol\omega$ with $\boldsymbol\omega\in S_0$ and $s\le s_1:=\min(r_0,c/2C)$, this gives $|\varphi(\mathbf x)|\ge cs^k-Cs^{k+1}\ge cs^k/2$.
6. Using $e^x\ge x^{2k+3}/(2k+3)!$ with $x=2\Delta\tau/s$,
$$\int_{B_1}w^2|\varphi|^2\,d^3x\ \ge\ \sigma_0\int_0^{s_1}s^2e^{2\Delta\tau/s}\,\frac{c^2s^{2k}}{4}\,ds\ \ge\ \frac{\sigma_0c^2}{4}\,\frac{(2\Delta\tau)^{2k+3}}{(2k+3)!}\int_0^{s_1}\frac{ds}{s}=+\infty .$$
This contradicts $\varphi\in D(M)$, so $\varphi\equiv0$.
7. In Fourier space $e^{-\Delta\tau K}$ is multiplication by $e^{-\Delta\tau|\mathbf k|^2/2}>0$, so it is injective, and $g=0$. Since $w>0$, $\psi=0$ almost everywhere.
8. Finally, $D(T^N)\subset D(T^2)$ for every $N\ge2$.

Proof that $T$ is unbounded. Take $\psi\ge0$ supported in $B_1$. Since $|\mathbf x-\mathbf y|\le|\mathbf x|+1$ on the support,

$$(T\psi)(\mathbf x)\ge(2\pi\Delta\tau)^{-3/2}e^{-(|\mathbf x|+1)^2/2\Delta\tau}\int w\psi\,d^3y,$$

so $\|T\psi\|_2\ge c_{\Delta\tau}\int w\psi$ with $c_{\Delta\tau}>0$. Now let $\psi_n$ be the normalised indicator of the shell $A_n=\{1/(2n)<|\mathbf y|<1/n\}$. It lies in $D(T)$, and $\int w\psi_n\ge e^{\Delta\tau n}|A_n|^{1/2}$ with $|A_n|=\tfrac78\cdot\tfrac{4\pi}{3}n^{-3}$, which tends to $\infty$. So $T$ is unbounded, and in particular not trace class.

Confidence for Part B:

- high for B.1 to B.5, which are elementary, with every inequality written out, and agree with checks C1 to C3;
- medium-high for B.6, which uses the identity theorem for real-analytic functions [R] and is not checked numerically.

### Part C. The continuum

#### C.1 $H$ is self-adjoint

[V] Split $V=V_1+V_2$ with $V_1=-\chi_{r<1}/r$ and $V_2=-\chi_{r\ge1}/r$.

- $\|V_1\|_2^2=\int_{r<1}r^{-2}\,d^3r=4\pi\int_0^1dr=4\pi<\infty$.
- $|V_2|\le1$.

So $V\in L^2(\mathbb R^3)+L^\infty(\mathbb R^3)$. Such a $V$ is $-\Delta$-bounded with relative bound zero (Simon 2017, §7, the discussion after eq. (7.15)). The Kato–Rellich theorem (same source, Theorem 7.3) then makes $H=K+V$ self-adjoint on $D(K)=H^2(\mathbb R^3)$ and bounded below. In particular $D(K)\subset D(V)$.

#### C.2 $-1/r$ is in the Kato class

[V] In three dimensions the Kato class $K_3$ consists of the $V$ with $\lim_{\delta\to0}\sup_{\mathbf x}\int_{|\mathbf x-\mathbf y|\le\delta}|V(\mathbf y)|\,|\mathbf x-\mathbf y|^{-1}\,d^3y=0$ (Shen 2001, eq. (1.1)).

[D] For $|V(\mathbf y)|=1/|\mathbf y|$ the quantity to control is $f_\delta(\mathbf x)=\int_{B_\delta(\mathbf x)}d^3y/(|\mathbf y||\mathbf x-\mathbf y|)$. For $a,b>0$, $(1/a-1/b)^2\ge0$ gives $1/(ab)\le(1/a^2+1/b^2)/2$, so

$$f_\delta(\mathbf x)\le\frac12\int_{B_\delta(\mathbf x)}\frac{d^3y}{|\mathbf y|^2}+\frac12\int_{B_\delta(\mathbf x)}\frac{d^3y}{|\mathbf x-\mathbf y|^2}.\tag{C1}$$

The second integral equals $\int_{B_\delta}|\mathbf z|^{-2}d^3z=4\pi\int_0^\delta dr=4\pi\delta$. For the first, let $A=B_\delta(\mathbf x)$, $B=B_\delta(\mathbf 0)$ and $\phi(\mathbf y)=|\mathbf y|^{-2}$.

- Since $|A|=|B|$, also $|A\setminus B|=|B\setminus A|$.
- On $A\setminus B$, $|\mathbf y|\ge\delta$, so $\phi\le\delta^{-2}$.
- On $B\setminus A$, $|\mathbf y|<\delta$, so $\phi>\delta^{-2}$.

Hence

$$\int_A\phi-\int_B\phi=\int_{A\setminus B}\phi-\int_{B\setminus A}\phi\ \le\ \delta^{-2}|A\setminus B|-\delta^{-2}|B\setminus A|=0,\tag{C2}$$

so the first integral is at most $\int_B\phi=4\pi\delta$. Together,

$$\sup_{\mathbf x}f_\delta(\mathbf x)\ \le\ 4\pi\delta\ \longrightarrow\ 0\quad(\delta\to0),\tag{C3}$$

so $-1/r\in K_3$, and its positive part is zero. Check C5 computes $f_\delta$ by quadrature; the bound is attained at $\mathbf x=\mathbf 0$, where $f_\delta(\mathbf 0)=4\pi\delta$.

#### C.3 The exact kernel is finite, including at the origin

[S] If $V_-\in K_\nu$ and $V_+\in K_\nu^{\rm loc}$, then $e^{-tH}$ has a jointly continuous integral kernel for every $t>0$. This is Simon 1982, Theorem B.7.1, {ver: no}. Broderix, Hundertmark and Leschke (2000) prove the same for Kato-class scalar potentials with magnetic fields; vector potential $A=0$ on $\Omega=\mathbb R^3$ is the case Simon treated (abstract and §6, {ver: tool}). By C.2 the theorem applies, so $K_\tau(\mathbf r,\mathbf r')$ is finite and continuous on $\mathbb R^3\times\mathbb R^3$ for every $\tau>0$, including at $\mathbf r=\mathbf r'=\mathbf 0$.

[D, from recalled inputs] I also evaluate the kernel explicitly at the origin, which is where the primitive kernel fails. Only $l=0$ states are nonzero at $r=0$.

- Bound states. The $l=0$ bound states have $E_n=-1/(2n^2)$ [R] and $|\psi_{n00}(0)|^2=1/(\pi n^3)$. [V] Fäldt and Wilkin give $[\psi_n(0)]^2=4\alpha_n^3$ in the radial normalisation $\psi=u/r$, $\int u^2dr=1$ (their eq. (21)). In atomic units $\alpha_n=1/n$, so $u_n'(0)^2=4/n^3$, and the full wavefunction $\psi_{n00}=u_n/(\sqrt{4\pi}\,r)$ gives $4/(4\pi n^3)=1/(\pi n^3)$.
- Continuum. Normalise the scattering states to $(2\pi)^{-3/2}e^{i\mathbf k\cdot\mathbf r}$ at infinity. Their value at the origin is the free value $(2\pi)^{-3/2}$ times the Sommerfeld factor. [V] Fäldt and Wilkin give $[\psi(k,0)]^2=2\pi\eta/(e^{2\pi\eta}-1)$, with $\eta=-me^2/(\hbar^2k)$ in the attractive case, normalised so that the free value is 1 (their eq. (19)). In atomic units $\eta=-1/k$, so

$$C^2(k)=\frac{2\pi(-1/k)}{e^{-2\pi/k}-1}=\frac{2\pi/k}{1-e^{-2\pi/k}} .\tag{C4}$$

Assuming completeness of the bound states together with the Coulomb waves [R],

$$K_\tau(\mathbf 0,\mathbf 0)=\sum_{n\ge1}\frac{e^{\tau/2n^2}}{\pi n^3}+\int\frac{d^3k}{(2\pi)^3}\,C^2(k)\,e^{-\tau k^2/2}=\sum_{n\ge1}\frac{e^{\tau/2n^2}}{\pi n^3}+\frac1\pi\int_0^\infty\frac{k\,e^{-\tau k^2/2}}{1-e^{-2\pi/k}}\,dk .\tag{C5}$$

The second form uses $d^3k=4\pi k^2dk$ and $k^2C^2/(2\pi^2)=k/\big(\pi(1-e^{-2\pi/k})\big)$.

Both terms are finite for every $\tau>0$.

- [D] The sum is bounded term by term (step added in round 2 for finding F1.1). For $n\ge1$, $1/n^2\le1$; since $\tau>0$, this gives $\tau/(2n^2)\le\tau/2$, and because the exponential is increasing, $e^{\tau/2n^2}\le e^{\tau/2}$. Hence
$$\sum_{n\ge1}\frac{e^{\tau/2n^2}}{\pi n^3}\ \le\ \frac{e^{\tau/2}}{\pi}\sum_{n\ge1}\frac{1}{n^3}=\frac{e^{\tau/2}\,\zeta(3)}{\pi}.$$
  Here $\zeta(3)=\sum_{n\ge1}n^{-3}\approx1.2021$ is finite, being a $p$-series with $p=3>1$. The bound is sharp as $\tau\to0$, where both sides tend to $\zeta(3)/\pi$. Check C6 in §10 tests it.
- The integrand behaves like $k$ as $k\to0$, and like $k^2e^{-\tau k^2/2}/(2\pi)$ as $k\to\infty$.
- Consistency: replacing $C^2$ by 1 and dropping the bound states gives $(1/2\pi^2)\int_0^\infty k^2e^{-\tau k^2/2}dk=(2\pi\tau)^{-3/2}$, the free value.

[N] Check C4 evaluates (C5) and compares it with an independent finite-difference diagonalisation of the $l=0$ radial Hamiltonian, which uses none of the recalled data. After extrapolation in the grid spacing the two agree to better than $5\times10^{-7}$ relative, for $\tau=0.5,1,2,4$. At $\tau=1$, $K_1(\mathbf 0,\mathbf 0)=0.9195694112$, which is 14.48 times the free value 0.0634936359.

#### C.4 The exact trace is infinite

[D] Step 1, a Jensen inequality from the spectral theorem. For a unit vector $\varphi\in D(H)$, the spectral measure $\mu_\varphi$ of $H$ is a probability measure with $\langle\varphi,f(H)\varphi\rangle=\int f\,d\mu_\varphi$ and $m:=\langle\varphi,H\varphi\rangle=\int\lambda\,d\mu_\varphi$ [R, functional calculus]. By convexity of $\lambda\mapsto e^{-\beta\lambda}$, $e^{-\beta\lambda}\ge e^{-\beta m}\big(1-\beta(\lambda-m)\big)$ for every real $\lambda$. Integrating against $\mu_\varphi$:

$$\langle\varphi,e^{-\beta H}\varphi\rangle\ \ge\ e^{-\beta m}\Big(1-\beta\Big(\int\lambda\,d\mu_\varphi-m\Big)\Big)=e^{-\beta\langle\varphi,H\varphi\rangle}.\tag{C6}$$

Both integrals exist: $e^{-\beta\lambda}$ is bounded on the spectrum because $H$ is bounded below, and $\lambda$ is $\mu_\varphi$-integrable because $\varphi\in D(H)$.

[D] Step 2, infinitely many orthogonal test states. Take $\varphi\in C_c^\infty(\mathbb R^3)$ with $\|\varphi\|=1$ and support in $B_1$, and set $\varphi_k(\mathbf r)=\varphi(\mathbf r-3k\hat{\mathbf e}_z)$ for $k=0,1,2,\dots$.

- The supports are disjoint, so the $\varphi_k$ are orthonormal.
- $K$ commutes with translations and $V\le0$, so $\langle\varphi_k,H\varphi_k\rangle\le\langle\varphi,K\varphi\rangle=:c<\infty$.
- For a positive operator, the trace is at least the sum of the diagonal elements over any orthonormal set: extend the set to a basis, and every added term is nonnegative.

So, by (C6),

$$\operatorname{Tr}e^{-\beta H}\ \ge\ \sum_{k\ge0}\langle\varphi_k,e^{-\beta H}\varphi_k\rangle\ \ge\ \sum_{k\ge0}e^{-\beta c}=+\infty\qquad\text{for every }\beta>0.\tag{C7}$$

The bound states alone give the same conclusion [R]: they contribute $\sum_nn^2e^{\beta/2n^2}\ge\sum_nn^2=\infty$. The argument through (C7) shows that the divergence is a large-volume effect: infinitely many disjoint regions of space each contribute at least $e^{-\beta c}$. Over a bounded region the exact diagonal kernel integrates to a finite number, $\int_{B_L}K_\beta(\mathbf r,\mathbf r)\,d^3r<\infty$, because $K_\beta$ is continuous (C.3).

#### C.5 Comparison

| Quantity | Primitive, any $N\ge1$, $\Delta\tau>0$ | Exact |
|---|---|---|
| Full trace over $\mathbb R^3$ | $+\infty$, from two sources: a bead near the origin (B9) and the chain at infinity (B13) | $+\infty$, from the large-volume source only (C7) |
| Diagonal kernel integrated over $B_L$: $\int_{B_L}\rho_N(\mathbf r,\mathbf r)d^3r$ vs $\int_{B_L}K_\beta(\mathbf r,\mathbf r)d^3r$ | $+\infty$ for every $L>0$ (B.2) | finite (C.3) |
| Kernel at fixed points $(\mathbf r,\mathbf r')$ | $+\infty$ at every pair when $N\ge2$ (B10); for $N=1$, finite if $\mathbf r'\ne\mathbf 0$ but not locally integrable at $\mathbf r'=\mathbf 0$ | finite and continuous everywhere, e.g. $K_1(\mathbf 0,\mathbf 0)=0.91957$ (check C4) |

The large-volume divergence is common to both sides and has nothing to do with $r=0$. The divergence at the origin occurs in every primitive approximant and has no counterpart in the continuum. Since $Z_N^{(L)}=\infty$ for every $N$, the localised primitive trace cannot converge to the finite localised exact quantity as $N\to\infty$. The failure happens at every finite $N$, not only in the limit.

#### C.6 The theorem that justifies time slicing, and the hypothesis $-1/r$ violates

[V] The Trotter product formula, in the form given by Reed and Simon. Let $A$ and $B$ be self-adjoint on a Hilbert space, with $A+B$ essentially self-adjoint on $D(A)\cap D(B)$. Then for real $t$,

$$e^{-it\overline{(A+B)}}=\mathop{\text{s-lim}}_{n\to\infty}\big(e^{-itA/n}e^{-itB/n}\big)^n .\tag{C8}$$

If, in addition, $A$ and $B$ are bounded below, then for $t\ge0$,

$$e^{-t\overline{(A+B)}}=\mathop{\text{s-lim}}_{n\to\infty}\big(e^{-tA/n}e^{-tB/n}\big)^n .\tag{C9}$$

What was retrieved:

- the unitary form, with the essential-self-adjointness hypothesis, as Reed–Simon I, Theorem VIII.31 (quoted in arXiv:2501.04564, Theorem B.3.7);
- the semigroup form, with "A and B bounded from below" (Encyclopedia of Mathematics, "Trotter product formula"; arXiv:2308.00290, Theorem A1.17, which attributes it to Teschl).

I have not read the semigroup clause in Reed–Simon itself: {ver: no}.

The hypotheses for $A=K$ and $B=V$, applied to $Z_N$ with $t=\beta$ and $n=N$:

| Hypothesis | Status for $K$, $V$ | Why |
|---|---|---|
| (i) $A$ and $B$ self-adjoint | holds | $K$ on $H^2(\mathbb R^3)$; $V$ as a real multiplication operator on its maximal domain |
| (ii) $A+B$ essentially self-adjoint on $D(A)\cap D(B)$ | holds | by C.1, $D(K)\subset D(V)$, so $D(K)\cap D(V)=D(K)$, and $H$ is self-adjoint there |
| (iii) $A$ and $B$ bounded below | fails for $V$ | $K\ge0$, but $\inf_r(-1/r)=-\infty$ |

So the real-time formula (C8) holds for hydrogen, $e^{-itH}=\text{s-lim}\,\big(e^{-itK/N}e^{-itV/N}\big)^N$, because $e^{-itV/N}$ is unitary whatever the sign of $V$. The imaginary-time formula (C9), which is what (A3) relies on, is not available.

This is more than a missing step in a proof. With $V$ unbounded below:

- $e^{-\Delta\tau V}$ is an unbounded operator (its norm would be $\sup_re^{\Delta\tau/r}=\infty$);
- the approximants $\big(e^{-\Delta\tau K}e^{-\Delta\tau V}\big)^N$ are not bounded operators, and for $N\ge2$ they are defined only on the zero vector (Remark B.6);
- so the strong limit in (C9) cannot even be formulated.

The hypothesis is about the summand $V$, not the sum: $H$ itself is bounded below. Kato's 1978 extension of the product formula removes the domain condition (ii) by working with form sums. It still requires $A$ and $B$ to be positive self-adjoint operators, that is, generators of self-adjoint contraction semigroups (Simon 2017, §18, Theorem 18.2). $-1/r$ violates that requirement too, and no other.

[R] Why the continuum survives when slicing fails, qualitatively. In the Feynman–Kac representation, the potential enters through the time integral $\int_0^\tau V(\mathbf b(s))\,ds$ along Brownian paths. For $V\in K_3$ this integral has finite exponential moments (Simon 1982, Khas'minskii's lemma, {ver: no}). The primitive weight replaces it by the Riemann sum $\Delta\tau\sum_jV(\mathbf r_j)$, which samples $V$ at isolated instants, and the weight $e^{\Delta\tau/r_j}$ of a single sample is not locally integrable. This is offered as diagnosis only and is not used anywhere above.

Confidence for Part C:

- high for C.1, C.2 and C.4, and for the kernel at the origin, where two independent routes agree;
- medium-high for the kernel at general points, which rests on a theorem whose locator I could not open (Simon 1982, B.7.1), supported by the retrieved abstract of Broderix, Hundertmark and Leschke;
- medium-high for the exact wording of the hypotheses in C.6, which I verified only through secondary sources. The identification of the violated hypothesis does not depend on whether the clause reads "bounded below" or "positive", because $V$ is neither.

### Part D. Assessment of the notes' hypotheses H1 to H6

H1 (p. 4) has two parts.

- Correct: the trace closes the paths, $x(\beta)=x(0)$. This is the $\mathbf r_{N+1}=\mathbf r_1$ of (A3).
- Wrong for this Hamiltonian: the ground-state dominance $Z(\beta)=\sum_ne^{-\beta E_n}\simeq e^{-\beta E_0}$ and the formula $E_0\approx-\ln Z(\beta)/\beta$. Both presuppose that $e^{-\beta H}$ is trace class with a discrete spectrum. For hydrogen in $\mathbb R^3$, $\operatorname{Tr}e^{-\beta H}=+\infty$ for every $\beta$ (C7). The bound-state sum alone diverges, and the continuum $[0,\infty)$ adds an infinite contribution. Read literally, the formula gives $E_0\approx-\infty$.

Ground-state dominance does hold for the diagonal kernel $\langle\mathbf r|e^{-\beta H}|\mathbf r\rangle$ at fixed $\mathbf r$, which is finite (C.3) [R, not proved here]. That is a statement about a kernel, not about $Z$.

H2 (p. 5) is wrong for this $V$. As a justification of time slicing it would be incomplete even for matrices.

- For bounded operators, the per-slice agreement $e^{\Delta A}e^{\Delta B}=e^{\Delta(A+B)}+O(\Delta^2)$ is true. But the global statement needs the telescoping bound $\|X^N-Y^N\|\le N\max(\|X\|,\|Y\|)^{N-1}\|X-Y\|$, which turns $N$ errors of order $\Delta^2$ into $O(1/N)$ and requires uniform bounds on $\|e^{\Delta A}\|$ and $\|e^{\Delta B}\|$. The notes stop at the per-slice expansion.
- For $V=-1/r$, the expansion $e^{-\Delta\beta V}\approx1-\Delta\beta V$ fails at every $r\lesssim\Delta\beta$ (in atomic units), however small $\Delta\beta$ is, because $\Delta\beta V$ is not uniformly small in $r$. The left side $e^{-\Delta\beta(K+V)}$ is a bounded operator ($H$ is bounded below). The right side $e^{-\Delta\beta K}e^{-\Delta\beta V}$ is unbounded (Remark B.6). So the two are not close in any operator sense, for any $\Delta\beta>0$.

The notes' phrase "valid only for very small intervals" is exactly what fails: near the nucleus, no interval is small enough. The justification that does exist is the Trotter theorem, and its semiboundedness hypothesis is the one $V$ violates (C.6).

H3 (p. 6) is wrong as written, in two substantive places and two minor ones.

- Wrong potential weight. The potential term reads $\beta V(x_j)$ where it should read $\Delta\beta V(x_j)$. The first line of p. 6 has $e^{-\Delta\beta V(x_j)}$, which is correct; the $\Delta$ is lost in the second line and stays lost through the final formula. Page 7 then writes $S_m$ with $\Delta\tau\,V(x_j)$ and $\Delta\tau=\hbar\Delta\beta$, which is the correct per-slice weight, so the error is confined to p. 6. With $\beta V$ the potential is overweighted by a factor $m$. The qualitative answer to (b) survives, since $e^{\beta/r}$ is no more integrable than $e^{\Delta\beta/r}$, but the growth law (B6) would have $a=\beta$ instead of $\Delta\beta$.
- One-dimensional formula. The prefactor $(\mu/2\pi\hbar^2\Delta\beta)^{m/2}$ and the scalar $x_j$ describe a particle on a line. For hydrogen in $\mathbb R^3$ the prefactor is $(\mu/2\pi\hbar^2\Delta\beta)^{3m/2}$, the measures are $d^3r_j$, and the kinetic term is $|\mathbf r_{j+1}-\mathbf r_j|^2$ for vectors (A4). Page 8 then writes the kinetic term with radial coordinates, $(r_{j+1}-r_j)^2$. The difference of radii is not the distance between beads: $|\mathbf r_{j+1}-\mathbf r_j|\ge\big||\mathbf r_{j+1}|-|\mathbf r_j|\big|$, with equality only when the two beads lie on the same ray from the origin. So that expression is not the three-dimensional primitive action. Meanwhile H5 integrates with the three-dimensional measure $4\pi r^2dr$, so the notes combine a one-dimensional kinetic term with a three-dimensional potential integral.
- Minor: in the first line of p. 6 the free propagator is written $\langle x_{j+1}|e^{-\beta\hat K}|x_j\rangle$, missing the $\Delta$; the next line uses $\Delta\beta$ correctly.
- Minor: the identity written as "$\prod_je^{j}=\sum_je^{j}$" should read $\prod_je^{a_j}=e^{\sum_ja_j}$. The next line uses the correct identity.

What H3 gets right: the ordering, with $V$ evaluated at the right-hand point $x_j$, matches $T$; and the per-slice prefactor $(\mu/2\pi\hbar^2\Delta\beta)^{1/2}$ is the correct one-dimensional free kernel.

H4 (p. 8) is correct. With $V=-k/r$, $-\Delta\beta V=\Delta\beta k/r>0$, and the weight tends to $+\infty$ as $r\to0^+$; the notes correctly note that it is dimensionless. On its own, though, it does not imply divergence: unbounded functions such as $1/r$ are integrable in three dimensions. It needs H5.

H5 (p. 8) is correct but unproven.

- "$r^2$ does not compensate $e^{a/r}$" is an assertion. The proof is (B1) to (B3): $e^x\ge x^3/6$ gives $r^2e^{a/r}\ge a^3/(6r)$, whose integral diverges logarithmically. The true growth with a cutoff is much faster than logarithmic: $I\simeq4\pi\eta^4e^{a/\eta}/a$ (B6).
- H5 concerns one bead with the kinetic factor ignored, so by itself it is not yet a statement about $Z_m$.
- On p. 9, item 1 reads "$e^{a/r}\to0$". Taken literally this is false: the limit as $r\to0^+$ is $+\infty$. I read it as shorthand for "$e^{a/r}$ as $r\to0$", but I flag the reading as uncertain.

H6 (p. 9) has a correct conclusion and no proof. The kinetic factors indeed do not compensate, but the notes give no argument.

- The missing step is a lower bound on the kinetic factors on a set of positive measure that contains the singular configurations: (B7) to (B9). The obvious bound on a Gaussian is an upper bound, and that points the wrong way for proving a divergence.
- B.5 sharpens the conclusion: the kinetic factors do not change the leading growth at all (B16).
- "The sum diverges" does not distinguish the two divergences of $Z_N$. The notes do not mention the large-volume one (B13), which is present even for $V=0$ and is the same mechanism that makes H1 fail.

My hypotheses against the notes'. I use none of H1 to H6 as a premise. My (A3) is the corrected three-dimensional form of H3; the lemma (B1) to (B3) proves H4 and H5; and (B7) to (B9) prove H6's conclusion.

Hypotheses of the notes I consider unnecessary for (a) to (c):

- H1, the ground-state extraction;
- H2, the Taylor-series justification, which the Trotter theorem replaces;
- the Wick-rotation route of p. 7, since (A3) follows directly from the operator expression.

Hypotheses I need that the notes do not state:

- three dimensions, with the measure $d^3r$;
- positivity of the integrand and Tonelli's theorem [A1];
- $V\le0$, so that every potential factor is at least 1;
- a lower bound on the kinetic factors on bounded sets;
- the large-volume divergence and its separation from the origin (B.3, B.4);
- the fact that $T^N$ is not an operator whose trace can be taken (B.6);
- for Part C: Kato's theorem, the Kato-class kernel theorem, the Coulomb data at the origin, and the semiboundedness hypothesis of the Trotter formula.

## 4. Verification

### 4.1 Self-check battery

1. Dimensions. In atomic units every displayed quantity is a pure number or a power of $a_0$. Restoring units:
   - the exponent $\Delta\beta k/r$ is dimensionless ($k$ in J·m, $\Delta\beta$ in J⁻¹, $r$ in m), so $a=\Delta\beta k$ is a length, $\eta^4/a$ in (B6) is a volume, and $I$ is a volume, as it must be;
   - each slice prefactor $(\mu/2\pi\hbar^2\Delta\beta)^{3/2}$ has units m⁻³ and is paired with $d^3r$, so $Z_N$ is dimensionless, as a trace must be;
   - $K_\tau(\mathbf 0,\mathbf 0)$, $(2\pi\tau)^{-3/2}$, $1/(\pi n^3)$ and the continuum term of (C5) all have units $a_0^{-3}$.
2. Limiting cases.
   - $\Delta\tau\to0$ at fixed $N$: the coefficient $2\pi\Delta\tau^3/3$ in (B2) tends to 0, yet $I=\infty$ for every $\Delta\tau>0$; the singular shell has thickness $\eta^2/\Delta\tau$.
   - $N\to\infty$ at fixed $\beta$: $Z_N=Z_N^{(L)}=\infty$ for every $N$, so there is no limit to take.
   - $\Delta\tau\to\infty$ or $\beta\to\infty$: still infinite.
   - Coupling: with $V=-Z/r$, every $Z>0$ gives the same divergence; $Z=0$ leaves only the large-volume divergence.
   - $\eta\to0$: (B6) and (B16). $L\to\infty$: (B13).
3. Reduction to simpler cases.
   - $V=0$: (A3) becomes $\operatorname{Tr}e^{-\beta K}=\infty$, by volume alone, and its localised version is finite, consistent with (B11) as $\delta\to0$.
   - $N=1$: $Z_1=(2\pi\beta)^{-3/2}\int d^3r\,e^{\beta/r}$ is infinite at both ends, consistent with (B9) and (B13).
   - Repulsive $V=+1/r$: the integrand is bounded by its kinetic part and the localised trace is finite. The proof of (B9) breaks exactly at the step $w\ge1$, where it should.
4. Symmetries. Rotations: $Z_N$ depends only on the radii and relative angles (used in (B17)). Cyclic relabelling of the beads (used to single out bead 1). Reversing the bead order, or reversing the factor order in $T$, leaves (A3) unchanged (Part A).
5. Signs. The divergence comes from $-\Delta\tau V=+\Delta\tau/r>0$ for the attractive potential, as in the problem statement ($V=-1/r$). The Euclidean kinetic exponent is negative.
6. Order of magnitude.
   - For $\Delta\tau=0.1$ (for instance $\beta=10$, $N=100$) and $\eta=10^{-3}a_0$, (B6) gives $I\approx4\pi\cdot10^{-12}e^{100}/0.1\times1.05\approx3.5\times10^{33}\,a_0^3$, against $|B_1|\approx4.2\,a_0^3$.
   - Even a finite proton, of radius about $1.6\times10^{-5}a_0$ [R], would leave a weight of order $e^{\Delta\tau/R_p}\approx e^{6250}$ at its centre. The primitive weight is unusable long before the mathematical divergence.
   - For the exact kernel, $K_1(\mathbf 0,\mathbf 0)/(2\pi)^{-3/2}\approx14.5$ [N, C4].
7. Boundary conditions. The trace imposes $\mathbf r_{N+1}=\mathbf r_1$ (A3); for $N=1$ the single link has zero length. In C4, route (ii) imposes $u(0)=0$ (the regular $l=0$ solution) and $u(R_{\rm box})=0$; changing the box size has no effect at the $10^{-13}$ level (G5).
8. Degenerate cases. Only nonnegative integrands are integrated, so the only exchanges of limit and integral are Tonelli and monotone convergence (B3). $\kappa$ in (B17) never vanishes, because $r\ge\eta>0$. $\Delta\tau>0$ and $N\ge1$ throughout. The orthogonality in (C7) comes from disjoint supports.

### 4.2 Computational checks

All scripts are standalone and run from a clean interpreter with `python3 -I`. Environment: Python 3.13.16, numpy 2.5.3, scipy 1.18.1, mpmath 1.3.0, sympy 1.14.0, Linux sandbox. In round 2 every script was re-run once, with code byte-identical to round 1, and the outputs reproduced below are from that round-2 run. Each round-2 output is byte-identical to its round-1 counterpart (compared with `cmp`). In round 1 each script had been run twice, also with identical results. Check C6, added in round 2 for finding F1.1, is in §10. C5 was run with two different quadrature methods, and both runs are reported. The only edit to any output is in C5 run 1: the absolute sandbox path in front of the script name in scipy's warning lines has been removed.

The equation numbers cited in the code comments come from an earlier draft of this document. The code is reproduced as it was run, so those comments are left unchanged. They map to the final numbering as follows:

| Check | Number in the code comment | Final number |
|---|---|---|
| C1 | (B4)–(B6) | (B2) and (B6) |
| C2 | (B12) | (B17) |
| C2 | (B13)–(B15) | (B16)–(B18) |
| C3 | (B9)–(B10) | (B12)–(B13) |
| C4 | (C9) | (C5) |
| C5 | (C3)–(C5) | (C1)–(C3) |

#### C1 [N]. One-bead radial integral against the growth law (B2) and (B6)

What it tests. It computes $4\pi\int_\eta^\varepsilon r^2e^{a/r}dr$ by direct quadrature in $r$. The integrand comes straight from the potential factor $e^{-\Delta\tau V}$ with $V=-1/r$ and $a=\Delta\tau$, not from the derivation. The result is compared with the lower bound (B2), with the leading law and its first correction, and with the three-term law (B6). The failure criteria were declared in the script before it was run.

What it would have caught. A wrong power of $\eta$ or a wrong exponent in the growth law; a wrong coefficient (for example $1/a$); a violation of the logarithmic lower bound. The contrast column, the ratio to the wrong law $\eta^3e^{a/\eta}$, decays like $\eta$, which shows the check can tell neighbouring powers apart.

What it would not have caught. Errors in going from $Z_N$ to the one-bead integral; the prefactor $(2\pi\Delta\tau)^{-3N/2}$; anything about the kinetic factor or the large-volume divergence. Rows with $a/\eta\le10$ are outside the asymptotic regime: they are reported and tested only against the lower bound.

Assumptions. The quadrature breakpoints are placed at multiples of $\eta^2/a$, a scale that comes from my analysis. A wrong scale would make the quadrature less accurate and show up as failures, not as passes. The mpmath working precision is 50 digits.

Outcome. All criteria pass. At $a/\eta=160$: $I/L_1=1.0258$; $(I/L_1-1)/(\eta/a)=4.130$, against a prediction of $4+20\eta/a=4.125$; and $I/L_3-1=2.99\times10^{-5}$, against $120(\eta/a)^3=2.93\times10^{-5}$.

```python
# C1: single-bead radial integral with an inner cutoff, against the predicted growth law.
# Environment: Python 3.13.16, mpmath 1.3.0. Deterministic (no random numbers).
#
# Quantity (from the bead integral, potential factor exp(-dtau*V) with V = -1/r, a = dtau):
#     I(eta) = 4*pi * int_eta^eps r^2 exp(a/r) dr          (integrated in r, directly)
# Predictions under test (derived in the answer, eqs. (B4)-(B6)):
#     lower bound      I(eta) >= (2*pi*a^3/3) * ln(eps/eta)          for all 0 < eta < eps
#     leading law      I(eta) ~ 4*pi*eta^4*exp(a/eta)/a              as eta -> 0
#     first correction (I/L1 - 1)/(eta/a) -> 4
#     three-term law   I/L3 - 1 = O((eta/a)^3), L3 = 4*pi*a^3*e^{a/eta}[(eta/a)^4 + 4(eta/a)^5 + 20(eta/a)^6]
# Declared failure (before running):
#     F1 any lower-bound violation;
#     F2 |I/L1 - 1| > 0.05 at the largest a/eta (=160) for any a;
#     F3 (I/L1 - 1)/(eta/a) outside [3.6, 4.4] at a/eta = 160;
#     F4 |I/L3 - 1| > 200*(eta/a)^3 at a/eta >= 40 (the next term predicts ~120*(eta/a)^3).
# Contrast: the ratio to a wrong law eta^3*exp(a/eta) is printed to show the check can tell powers apart.
import mpmath as mp

mp.mp.dps = 50
eps = mp.mpf(1)
fails = []

def I_direct(a, eta):
    a = mp.mpf(a); eta = mp.mpf(eta)
    w = eta**2 / a  # width of the region where exp(a/r) is within a factor e of its maximum
    pts = [eta] + [eta + k * w for k in (1, 3, 10, 30, 100, 300, 1000) if eta + k * w < eps] + [eps]
    return 4 * mp.pi * mp.quad(lambda r: r**2 * mp.exp(a / r), pts)

print("a     a/eta   eta            I(eta)            I/L1          (I/L1-1)/(eta/a)   I/L3-1          bound_ok  I/(eta^3 e^{a/eta})")
for a in (mp.mpf('0.5'), mp.mpf(1), mp.mpf(2)):
    for q in (2, 5, 10, 20, 40, 80, 160):
        eta = a / q
        if eta >= eps:
            continue
        I = I_direct(a, eta)
        x = eta / a
        L1 = 4 * mp.pi * eta**4 * mp.exp(a / eta) / a
        L3 = 4 * mp.pi * a**3 * mp.exp(a / eta) * (x**4 + 4 * x**5 + 20 * x**6)
        lb = (2 * mp.pi * a**3 / 3) * mp.log(eps / eta)
        ok = I >= lb
        if not ok:
            fails.append(("F1", float(a), q))
        r1 = I / L1
        c1 = (r1 - 1) / x
        r3 = I / L3 - 1
        wrong = I / (eta**3 * mp.exp(a / eta))
        print(f"{float(a):<5} {q:<7} {mp.nstr(eta,8):<14} {mp.nstr(I,10):<17} {mp.nstr(r1,10):<13} {mp.nstr(c1,8):<18} {mp.nstr(r3,6):<15} {str(ok):<9} {mp.nstr(wrong,6)}")
        if q == 160:
            if abs(r1 - 1) > 0.05:
                fails.append(("F2", float(a), q))
            if not (3.6 <= c1 <= 4.4):
                fails.append(("F3", float(a), q))
        if q >= 40 and abs(r3) > 200 * x**3:
            fails.append(("F4", float(a), q))

print("FAILURES:", fails if fails else "none")
```

```
a     a/eta   eta            I(eta)            I/L1          (I/L1-1)/(eta/a)   I/L3-1          bound_ok  I/(eta^3 e^{a/eta})
0.5   2       0.25           8.73960349        12.04766468   22.095329          0.505958        True      75.6977
0.5   5       0.1            9.950773425       26.67746559   128.38733          9.26056         True      67.0478
0.5   10      0.05           15.9913494        4.621898632   36.218986          1.88869         True      5.80805
0.5   20      0.025          6080.139943       1.276509475   5.5301895          0.0212076       True      0.802055
0.5   40      0.0125         1.610095881e+11   1.114788683   4.5915473          0.00205724      True      0.350221
0.5   80      0.00625        2.238228677e+27   1.053382198   4.2705758          0.000244223     True      0.165465
0.5   160     0.003125       7.547876444e+60   1.025811897   4.1299034          2.98763e-5      True      0.0805671
1.0   2       0.5            13.70402039       2.361397781   2.7227956          -0.704825       True      14.8371
1.0   5       0.2            23.39337986       7.839542463   34.197712          2.01521         True      19.7029
1.0   10      0.1            71.71798763       2.59103579    15.910358          0.619397        True      3.25599
1.0   20      0.05           48584.90674       1.275034259   5.5006852          0.0200274       True      0.801128
1.0   40      0.025          1.288076705e+12   1.114788683   4.5915473          0.00205724      True      0.350221
1.0   80      0.0125         1.790582942e+28   1.053382198   4.2705758          0.000244223     True      0.165465
1.0   160     0.00625        6.038301155e+61   1.025811897   4.1299034          2.98763e-5      True      0.0805671
2.0   5       0.4            77.51487582       3.247078682   11.235393          0.248876        True      8.1608
2.0   10      0.2            464.111738        2.095935349   10.959353          0.30996         True      2.63383
2.0   20      0.1            388569.6217       1.274674618   5.4934924          0.0197397       True      0.800902
2.0   40      0.05           1.030461364e+13   1.114788683   4.5915473          0.00205724      True      0.350221
2.0   80      0.025          1.432466353e+29   1.053382198   4.2705758          0.000244223     True      0.165465
2.0   160     0.0125         4.830640924e+62   1.025811897   4.1299034          2.98763e-5      True      0.0805671
FAILURES: none
```

#### C2 [N]. Can the kinetic factors compensate? The $N=2$ integral with a cutoff, (B16) to (B18)

What it tests. In part (a), it uses Monte Carlo over independent random directions to test the angular identity (B17) independently of its derivation (seed 20261019, 400 000 pairs per $\kappa$). In part (b), it computes $R(\eta)$, the full $N=2$ bead integral with cutoff divided by the same integral with the kinetic factor replaced by its maximum, for $\Delta\tau=1$, $L=1.5$, and five values of $\eta$. The input is the $N=2$ integrand of (A3), which comes from the problem statement and the given kernel. "The kinetic factor compensates" would show up as $R\to0$.

What it would have caught. Compensation; a wrong kinetic exponent at $N=2$; a wrong angular reduction (through part (a)); a wrong small-$\eta$ expansion (B18).

What it would not have caught. Anything at $N\ge3$, which only the general bounds (B14) to (B16) cover; the large-volume divergence, since the beads are confined to $B_L$; the overall prefactor, which cancels in $R$.

Assumptions. [A] Two independent, uniformly distributed directions have $\cos\theta_{12}$ uniform on $[-1,1]$; this is what (B17) uses. The Monte Carlo samples directions directly as normalised Gaussian vectors, so it does not rely on that fact.

Outcome. All criteria pass. $R$ increases towards 1, and at $\eta=0.0125$, $(1-R)/(2\eta^2/\Delta\tau)=1.0272$, against a prediction of about $1+2\eta/\Delta\tau=1.025$. At $\eta=0.2$ and $0.1$ the region away from the origin still dominates and $R$ is small; this is expected, and no criterion was placed on those rows except $R\le1$ and the monotonic decrease of $1-R$.

```python
# C2: do the kinetic factors compensate? N = 2 primitive bead integral with an inner cutoff eta on both
# beads and both beads confined to |r| < L.
# Environment: Python 3.13.16, numpy 2.5.3, mpmath 1.3.0. Seed fixed below.
#
# From the bead integral (answer eq. (A3)) at N = 2, the two links give |r2-r1|^2/(2 dtau) twice, so
#   Z2(eta) = (2 pi dtau)^(-3) * int_{eta<|r1|,|r2|<L} d^3r1 d^3r2 exp(-|r1-r2|^2/dtau + dtau/r1 + dtau/r2).
# Angular integration (answer eq. (B12)), valid for independent uniform directions:
#   int dOmega1 dOmega2 exp(-|r1-r2|^2/dtau) = 16 pi^2 exp(-(r1^2+r2^2)/dtau) sinh(k)/k,  k = 2 r1 r2/dtau.
# Part (a) tests that angular identity by Monte Carlo over random directions (independent of the closed form).
# Part (b) computes R(eta) = Z2(eta) / [ (2 pi dtau)^(-3) I(eta)^2 ],  I(eta) = 4 pi int_eta^L r^2 e^{dtau/r} dr,
#   i.e. the full N = 2 integral divided by what it would be if the kinetic factor were replaced by its maximum.
# Predictions (answer eqs. (B13)-(B15)):  R <= 1 for every eta;  R -> 1 as eta -> 0;
#   (1 - R)/(2 eta^2/dtau) -> 1, with a first correction of about +2 eta/dtau.
# Declared failure (before running):
#   Fa  any Monte Carlo deviation larger than 5 standard errors;
#   Fb1 R > 1 + 1e-12 for any eta;
#   Fb2 1 - R not decreasing as eta decreases;
#   Fb3 (1 - R)/(2 eta^2/dtau) outside [0.95, 1.10] at the smallest eta (prediction ~1.025).
# What would count as "the kinetic factor compensates": R -> 0 as eta -> 0.
import numpy as np
import mpmath as mp

rng = np.random.default_rng(20261019)
fails = []

# ---------- (a) Monte Carlo test of the angular identity ----------
def unit_vectors(n):
    v = rng.normal(size=(n, 3))
    return v / np.linalg.norm(v, axis=1, keepdims=True)

n = 400_000
print("(a) angular average <exp(k cos theta)> over independent uniform directions vs sinh(k)/k")
for k in (0.01, 0.5, 2.0, 5.0):
    u, w = unit_vectors(n), unit_vectors(n)
    vals = np.exp(k * np.sum(u * w, axis=1))
    est, se = vals.mean(), vals.std(ddof=1) / np.sqrt(n)
    exact = np.sinh(k) / k
    z = (est - exact) / se
    print(f"  k={k:<5} MC={est:.6f} +- {se:.2e}   sinh(k)/k={exact:.6f}   z={z:+.2f}")
    if abs(z) > 5:
        fails.append(("Fa", k))

# ---------- (b) the N = 2 integral ----------
mp.mp.dps = 30
dtau, L = mp.mpf(1), mp.mpf('1.5')

def pts(eta):
    w = eta**2 / dtau
    return [eta] + [eta + k * w for k in (1, 3, 10, 30, 100, 300, 1000) if eta + k * w < L] + [L]

def g(r1, r2):  # angular average of the kinetic factor, divided by 16 pi^2
    k = 2 * r1 * r2 / dtau
    return mp.exp(-(r1**2 + r2**2) / dtau) * mp.sinh(k) / k

print("\n(b) R(eta) = Z2 / [(2 pi dtau)^-3 I^2],  dtau = 1, L = 1.5")
print("  eta        R                    1-R                 (1-R)/(2 eta^2/dtau)   predicted ~1+2eta/dtau")
prev = None
for eta in (mp.mpf('0.2'), mp.mpf('0.1'), mp.mpf('0.05'), mp.mpf('0.025'), mp.mpf('0.0125')):
    P = pts(eta)
    wgt = lambda r: r**2 * mp.exp(dtau / r - dtau / eta)          # scaled radial weight
    Iw = mp.quad(wgt, P)                                            # I(eta) / (4 pi e^{dtau/eta})
    J = mp.quad(lambda a, b: wgt(a) * wgt(b) * g(a, b), P, P)       # Z2 / [(2 pi dtau)^-3 16 pi^2 e^{2 dtau/eta}]
    one_minus = mp.quad(lambda a, b: wgt(a) * wgt(b) * (1 - g(a, b)), P, P) / Iw**2
    R = J / Iw**2
    ratio = one_minus / (2 * eta**2 / dtau)
    print(f"  {mp.nstr(eta,5):<10} {mp.nstr(R,16):<20} {mp.nstr(one_minus,10):<19} {mp.nstr(ratio,8):<22} {mp.nstr(1+2*eta/dtau,6)}")
    print(f"             consistency |R + (1-R) - 1| = {mp.nstr(abs(R + one_minus - 1), 3)}")
    if R > 1 + mp.mpf('1e-12'):
        fails.append(("Fb1", float(eta)))
    if prev is not None and not (one_minus < prev):
        fails.append(("Fb2", float(eta)))
    prev = one_minus
    last_ratio = ratio
if not (0.95 <= last_ratio <= 1.10):
    fails.append(("Fb3", float(last_ratio)))
print("FAILURES:", fails if fails else "none")
```

```
(a) angular average <exp(k cos theta)> over independent uniform directions vs sinh(k)/k
  k=0.01  MC=1.000015 +- 9.13e-06   sinh(k)/k=1.000017   z=-0.19
  k=0.5   MC=1.042037 +- 4.71e-04   sinh(k)/k=1.042191   z=-0.33
  k=2.0   MC=1.811437 +- 2.97e-03   sinh(k)/k=1.813430   z=-0.67
  k=5.0   MC=14.880139 +- 4.71e-02   sinh(k)/k=14.840642   z=+0.84

(b) R(eta) = Z2 / [(2 pi dtau)^-3 I^2],  dtau = 1, L = 1.5
  eta        R                    1-R                 (1-R)/(2 eta^2/dtau)   predicted ~1+2eta/dtau
  0.2        0.2747484332427588   0.7252515668        9.0656446              1.4
             consistency |R + (1-R) - 1| = 1.97e-31
  0.1        0.549999669688688    0.4500003303        22.500017              1.2
             consistency |R + (1-R) - 1| = 3.71e-29
  0.05       0.9931740416191257   0.006825958381      1.3651917              1.1
             consistency |R + (1-R) - 1| = 6.9e-25
  0.025      0.998674583540708    0.001325416459      1.0603332              1.05
             consistency |R + (1-R) - 1| = 3.43e-23
  0.0125     0.9996789889021237   0.0003210110979     1.0272355              1.025
             consistency |R + (1-R) - 1| = 6.5e-22
FAILURES: none
```

#### C3 [N]. Composition law of the free kernel, (B12)

What it tests. (i) The completing-the-square identity of B.4, symbolically, with the two sides written independently. (ii) The one-dimensional composition integral by quadrature, against the closed form, at twelve parameter sets, including extreme ratios $s/t$ and large separations.

What it would have caught. An error in the composition law or in its normalisation, either of which would invalidate (B13).

What it would not have caught. Anything involving $V$.

Assumptions. [A] $s,t>0$, declared in the code; imaginary-time steps are positive.

Outcome. All twelve parameter sets agree to $1.2\times10^{-15}$ or better, and the symbolic difference is identically zero.

```python
# C3: composition law of the free kernel, used in the large-r (volume) argument, eq. (B9)-(B10).
# Environment: Python 3.13.16, numpy 2.5.3, scipy 1.18.1, sympy 1.14.0. Seed fixed below.
#
# Claim (1D factor; the 3D kernel is the product of three such factors):
#   int dy rho1(x,y;s) rho1(y,z;t) = rho1(x,z;s+t),   rho1(x,y;t) = (2 pi t)^(-1/2) exp(-(x-y)^2/(2t)).
# (i) Symbolic: the completing-the-square identity of eq. (B9), written out independently on both sides.
# (ii) Numerical: quadrature of the left side vs the right side at random (x,z,s,t), including points near
#      the edges (s/t very small or very large, |x-z| several widths). Tolerance 1e-9 relative.
# Declared failure: symbolic difference not identically zero, or any relative discrepancy > 1e-9.
import numpy as np
import sympy as sp
from scipy.integrate import quad

x, y, z = sp.symbols('x y z', real=True)
s, t = sp.symbols('s t', positive=True)   # [A] s, t > 0: imaginary-time steps are positive
lhs = -(x - y)**2 / (2 * s) - (y - z)**2 / (2 * t)
rhs = -(s + t) / (2 * s * t) * (y - (t * x + s * z) / (s + t))**2 - (x - z)**2 / (2 * (s + t))
print("(i) symbolic: expand(lhs - rhs) =", sp.simplify(sp.expand(lhs - rhs)))
fails = []
if sp.simplify(sp.expand(lhs - rhs)) != 0:
    fails.append("symbolic")

rng = np.random.default_rng(7)
rho = lambda a, b, tt: np.exp(-(a - b) ** 2 / (2 * tt)) / np.sqrt(2 * np.pi * tt)
cases = [(rng.uniform(-3, 3), rng.uniform(-3, 3), rng.uniform(0.05, 3), rng.uniform(0.05, 3)) for _ in range(8)]
cases += [(0.0, 0.0, 1e-3, 5.0), (2.0, -2.0, 5.0, 1e-3), (0.0, 6.0, 0.5, 0.5), (1.0, 1.0, 0.01, 0.01)]
print("(ii) numerical composition, x z s t -> relative error")
for (xx, zz, ss, tt) in cases:
    c = (tt * xx + ss * zz) / (ss + tt); w = np.sqrt(ss * tt / (ss + tt))
    val, err = quad(lambda yy: rho(xx, yy, ss) * rho(yy, zz, tt), c - 40 * w, c + 40 * w, epsabs=0, epsrel=1e-13, limit=200)
    ref = rho(xx, zz, ss + tt)
    rel = abs(val - ref) / ref
    print(f"  {xx:+.3f} {zz:+.3f} {ss:.4f} {tt:.4f}  ->  {rel:.2e}")
    if rel > 1e-9:
        fails.append((xx, zz, ss, tt))
print("FAILURES:", fails if fails else "none")
```

```
(i) symbolic: expand(lhs - rhs) = 0
(ii) numerical composition, x z s t -> relative error
  +0.751 +2.383 2.3383 0.7144  ->  0.00e+00
  -1.199 +2.241 0.0655 2.4726  ->  1.43e-16
  +1.782 -0.192 0.9439 0.8714  ->  0.00e+00
  -1.471 -0.330 1.5384 1.6828  ->  0.00e+00
  +2.973 +1.756 1.8854 2.9674  ->  1.79e-16
  -1.708 -2.039 1.8570 0.1796  ->  2.04e-16
  -2.786 +0.089 1.4253 2.7556  ->  1.91e-16
  +0.775 +0.085 1.5158 0.7802  ->  0.00e+00
  +0.000 +0.000 0.0010 5.0000  ->  1.56e-16
  +2.000 -2.000 5.0000 0.0010  ->  1.16e-15
  +0.000 +6.000 0.5000 0.5000  ->  4.08e-16
  +1.000 +1.000 0.0100 0.0100  ->  1.57e-16
FAILURES: none
```

#### C4 [N]. The exact kernel at the origin, by two independent routes, (C5)

What it tests. Route (i) evaluates the closed form (C5), whose inputs are recalled spectral data. Route (ii) uses only the problem's Hamiltonian: it discretises the $l=0$ radial operator $-\frac12u''-u/r$ on $(0,R_{\rm box})$ by second-order finite differences, diagonalises it, and assembles $\frac1{4\pi}\sum_ie^{-\tau E_i}u_i'(0)^2$. A control run with $V=0$ must reproduce $(2\pi\tau)^{-3/2}$. Three grid spacings are used, plus a box-size test, and the lowest three box eigenstates are compared with the recalled bound-state data.

What it would have caught.

- A wrong Sommerfeld factor. The repulsive form, for example, gives a continuum term orders of magnitude too small at small $k$.
- A wrong bound-state density at the origin.
- A missing factor $4\pi$ or $(2\pi)^3$.
- A wrong finite-difference normalisation (control G1).
- A kernel that diverged at the origin: route (ii) would then fail to converge in $h$.
- A box-size artifact (G5).

What it would not have caught. Finiteness at points other than the origin; off-diagonal elements; the general theorem cited in C.3. Both routes also assume that the $l=0$ sector carries all the weight at $r=0$. That holds because $R_{nl}(0)=0$ for $l\ge1$, and the same is true of the continuum partial waves [R].

Assumptions.

- [A] In route (ii), the $l=0$ sector of the self-adjoint $H$ corresponds to the boundary condition $u(0)=0$. The radial operator is limit-circle at $r=0$, and $u(0)=0$ selects the regular solution, which is the one corresponding to $H^2$ functions [R]. Agreement with route (i), whose inputs are the spectral data of the three-dimensional $H$, supports this.
- [A] $u'(0)$ is taken from the one-sided second-order formula $(4u_1-u_2)/2h$, which is valid for $u$ smooth at 0 (for example $u_{1s}\propto re^{-r}$).
- Eigenpairs above $E=120$ are dropped. The bound on the dropped part, below $10^{-19}$, is stated in the script.

Outcome. All criteria pass.

- The observed convergence order is 1.96 to 1.99.
- After Richardson extrapolation, routes (i) and (ii) agree to $5\times10^{-7}$ relative or better at all four $\tau$.
- The free control converges at second order; at the finest grid its error is between $1.6\times10^{-5}$ ($\tau=4$) and $1.3\times10^{-4}$ ($\tau=0.5$).
- The box bound states reproduce $E_n=-1/(2n^2)$ to $3\times10^{-6}$, and $1/(\pi n^3)$ to $3\times10^{-4}$, for $n=1,2,3$.

```python
# C4: the exact kernel <0|exp(-tau H)|0> for H = -(1/2) Laplacian - 1/r, by two independent routes.
# Environment: Python 3.13.16, numpy 2.5.3, scipy 1.18.1, mpmath 1.3.0. Deterministic.
#
# Route (i), closed form from recalled spectral data, answer eq. (C9):
#   K0(tau) = sum_{n>=1} exp(tau/(2n^2)) / (pi n^3)  +  (1/pi) int_0^inf k exp(-tau k^2/2) / (1 - exp(-2 pi/k)) dk
#   inputs [R]/[V]: |psi_n00(0)|^2 = 1/(pi n^3), E_n = -1/(2n^2), Sommerfeld factor (2pi/k)/(1-e^{-2pi/k}),
#   completeness of {bound states, Coulomb waves}, and that only l = 0 states are nonzero at r = 0.
# Route (ii), from the Hamiltonian only: the l = 0 radial operator -(1/2) d^2/dr^2 - 1/r on (0, Rbox) with
#   u(0) = u(Rbox) = 0, discretised by second-order finite differences, diagonalised. For l = 0,
#   psi(r) = u(r)/(sqrt(4 pi) r), so psi(0) = u'(0)/sqrt(4 pi); states with l >= 1 vanish at r = 0.
#   K0_box = (1/4pi) sum_i exp(-tau E_i) u_i'(0)^2, with u'(0) from the second-order one-sided formula
#   u'(0) ~ (4 u_1 - u_2)/(2h). Eigenpairs above Ecut = 120 are dropped; the dropped part is bounded by
#   exp(-tau_min*Ecut) * 17/(16 pi h^3) < 1e-19 (completeness of the discrete eigenvectors).
# Control: the same box code with V = 0 must reproduce the free value (2 pi tau)^(-3/2).
# Declared failure (before running):
#   G1 free control: relative error > 1e-3 at the finest h;
#   G2 Coulomb box vs closed form: relative difference > 5e-3 at the finest h;
#   G3 after Richardson extrapolation with the observed order: relative difference > 5e-4;
#   G4 box bound states n = 1..3: |E_n + 1/(2n^2)| > 1e-3 or relative error of |psi(0)|^2 vs 1/(pi n^3) > 5e-3;
#   G5 box-size sensitivity (Rbox = 30 vs 40 at h = 0.01): relative change > 1e-6.
import numpy as np
from scipy.linalg import eigh_tridiagonal
import mpmath as mp

taus = [0.5, 1.0, 2.0, 4.0]
ECUT = 120.0
fails = []

# ---------------- route (i) ----------------
mp.mp.dps = 30
def closed_form(tau):
    tau = mp.mpf(tau)
    Sb = mp.nsum(lambda n: mp.exp(tau / (2 * n**2)) / (mp.pi * n**3), [1, mp.inf])
    Sc = mp.quad(lambda k: k * mp.exp(-tau * k**2 / 2) / (-mp.expm1(-2 * mp.pi / k)), [0, 0.5, 2, 6, mp.inf]) / mp.pi
    return float(Sb), float(Sc), float(Sb + Sc)

# ---------------- route (ii) ----------------
def box(h, Rbox, coulomb=True):
    M = int(round(Rbox / h)) - 1
    r = h * np.arange(1, M + 1)
    d = np.full(M, 1.0 / h**2) + (-1.0 / r if coulomb else 0.0)
    e = np.full(M - 1, -0.5 / h**2)
    w, v = eigh_tridiagonal(d, e, select='v', select_range=(-10.0, ECUT))
    du0 = (4 * v[0, :] - v[1, :]) / (2 * h**1.5)   # u'(0) with u_j = v_j / sqrt(h)
    return w, du0

def K_box(w, du0, tau):
    return float(np.sum(np.exp(-tau * w) * du0**2) / (4 * np.pi))

print("route (i): closed form")
cf = {}
for tau in taus:
    Sb, Sc, tot = closed_form(tau)
    cf[tau] = tot
    free = (2 * np.pi * tau) ** -1.5
    print(f"  tau={tau:<4} bound part={Sb:.10f}  continuum part={Sc:.10f}  total={tot:.10f}  free={free:.10f}  ratio={tot/free:.4f}")

hs = [0.02, 0.01, 0.005]
Rbox = 40.0
res, resfree = {}, {}
for h in hs:
    w, du0 = box(h, Rbox, True)
    wf, du0f = box(h, Rbox, False)
    res[h] = {tau: K_box(w, du0, tau) for tau in taus}
    resfree[h] = {tau: K_box(wf, du0f, tau) for tau in taus}
    if h == hs[-1]:
        print("\nG4: lowest box eigenstates at h = 0.005, Rbox = 40")
        for n in (1, 2, 3):
            En, p0 = w[n - 1], du0[n - 1] ** 2 / (4 * np.pi)
            dE, dp = En + 1 / (2 * n**2), p0 / (1 / (np.pi * n**3)) - 1
            print(f"  n={n}: E={En:.7f} (exact -1/(2n^2) = {-1/(2*n**2):.7f}, diff {dE:+.2e});  |psi(0)|^2={p0:.7f} (1/(pi n^3) = {1/(np.pi*n**3):.7f}, rel {dp:+.2e})")
            if abs(dE) > 1e-3 or abs(dp) > 5e-3:
                fails.append(("G4", n))

print("\nG1: free control, box (V = 0) vs (2 pi tau)^(-3/2)")
for tau in taus:
    free = (2 * np.pi * tau) ** -1.5
    row = "  ".join(f"h={h}: {resfree[h][tau]/free-1:+.2e}" for h in hs)
    print(f"  tau={tau:<4} relative error  {row}")
    if abs(resfree[hs[-1]][tau] / free - 1) > 1e-3:
        fails.append(("G1", tau))

print("\nG2/G3: Coulomb box vs closed form")
for tau in taus:
    d = [res[h][tau] / cf[tau] - 1 for h in hs]
    p = np.log2(abs(res[hs[0]][tau] - res[hs[1]][tau]) / abs(res[hs[1]][tau] - res[hs[2]][tau]))
    rich = res[hs[2]][tau] + (res[hs[2]][tau] - res[hs[1]][tau]) / (2**p - 1)
    dr = rich / cf[tau] - 1
    print(f"  tau={tau:<4} rel.diff h=0.02: {d[0]:+.2e}  h=0.01: {d[1]:+.2e}  h=0.005: {d[2]:+.2e}   observed order p={p:.2f}   Richardson: {dr:+.2e}")
    if abs(d[2]) > 5e-3:
        fails.append(("G2", tau))
    if abs(dr) > 5e-4:
        fails.append(("G3", tau))

print("\nG5: box size, h = 0.01")
w30, d30 = box(0.01, 30.0, True)
for tau in taus:
    a, b = K_box(w30, d30, tau), res[0.01][tau]
    print(f"  tau={tau:<4} Rbox=30: {a:.12f}  Rbox=40: {b:.12f}  rel.change {a/b-1:+.2e}")
    if abs(a / b - 1) > 1e-6:
        fails.append(("G5", tau))
print("\nFAILURES:", fails if fails else "none")
```

```
route (i): closed form
  tau=0.5  bound part=0.4760580540  continuum part=0.6693036422  total=1.1453616962  free=0.1795871221  ratio=6.3777
  tau=1.0  bound part=0.5953441704  continuum part=0.3242252408  total=0.9195694112  free=0.0634936359  ratio=14.4829
  tau=2.0  bound part=0.9427694300  continuum part=0.1599918269  total=1.1027612570  free=0.0224483903  ratio=49.1243
  tau=4.0  bound part=2.4461191758  continuum part=0.0796630394  total=2.5257822153  free=0.0079367045  ratio=318.2407

G4: lowest box eigenstates at h = 0.005, Rbox = 40
  n=1: E=-0.4999969 (exact -1/(2n^2) = -0.5000000, diff +3.12e-06);  |psi(0)|^2=0.3182901 (1/(pi n^3) = 0.3183099, rel -6.22e-05)
  n=2: E=-0.1249998 (exact -1/(2n^2) = -0.1250000, diff +1.95e-07);  |psi(0)|^2=0.0397874 (1/(pi n^3) = 0.0397887, rel -3.42e-05)
  n=3: E=-0.0555542 (exact -1/(2n^2) = -0.0555556, diff +1.36e-06);  |psi(0)|^2=0.0117929 (1/(pi n^3) = 0.0117893, rel +3.06e-04)

G1: free control, box (V = 0) vs (2 pi tau)^(-3/2)
  tau=0.5  relative error  h=0.02: +2.10e-03  h=0.01: +5.25e-04  h=0.005: +1.31e-04
  tau=1.0  relative error  h=0.02: +1.05e-03  h=0.01: +2.63e-04  h=0.005: +6.56e-05
  tau=2.0  relative error  h=0.02: +5.25e-04  h=0.01: +1.31e-04  h=0.005: +3.28e-05
  tau=4.0  relative error  h=0.02: +2.63e-04  h=0.01: +6.56e-05  h=0.005: +1.64e-05

G2/G3: Coulomb box vs closed form
  tau=0.5  rel.diff h=0.02: +3.19e-04  h=0.01: +8.16e-05  h=0.005: +2.07e-05   observed order p=1.96   Richardson: -4.64e-07
  tau=1.0  rel.diff h=0.02: -4.90e-04  h=0.01: -1.23e-04  h=0.005: -3.08e-05   observed order p=1.99   Richardson: +1.27e-07
  tau=2.0  rel.diff h=0.02: -8.87e-04  h=0.01: -2.23e-04  h=0.005: -5.60e-05   observed order p=1.99   Richardson: +3.69e-07
  tau=4.0  rel.diff h=0.02: -1.13e-03  h=0.01: -2.84e-04  h=0.005: -7.12e-05   observed order p=1.99   Richardson: +4.62e-07

G5: box size, h = 0.01
  tau=0.5  Rbox=30: 1.145455211031  Rbox=40: 1.145455211031  rel.change +5.48e-14
  tau=1.0  Rbox=30: 0.919456275654  Rbox=40: 0.919456275654  rel.change +1.21e-13
  tau=2.0  Rbox=30: 1.102515033371  Rbox=40: 1.102515033371  rel.change +1.55e-13
  tau=4.0  Rbox=30: 2.525065089752  Rbox=40: 2.525065089752  rel.change +2.23e-13

FAILURES: none
```

#### C5 [N]. The Kato-class quantity, (C1) to (C3)

What it tests. It computes $f_\delta(\mathbf x)$ by quadrature in coordinates centred at $\mathbf x$, for $|\mathbf x|/\delta\in\{0,0.1,0.5,0.99,1,1.5,3\}$ and $\delta\in\{0.1,1\}$. It compares the result with the derived bound $4\pi\delta$, and with a closed form based on Newton's theorem [R], which is not used in the derivation.

What it would have caught. A wrong bound (C3).

What it would not have caught. Whether the Kato class is the right hypothesis for the cited kernel theorem.

Run 1 failed. It used scipy's QUADPACK and reported disagreement with the recalled Newton formula at $|\mathbf x|/\delta=0.99$ ($1.6\times10^{-7}$ against a tolerance of $10^{-7}$). QUADPACK issued non-convergence warnings during the run. Python shows each warning only once, so the run does not say which rows triggered them. The inner integrand has an integrable singularity at $c=-1$ when $s=|\mathbf x|$, which lies inside the integration range for every $0<|\mathbf x|<\delta$. The comment at the head of the run-2 script attributes the warnings to the $0.99$ row specifically; that overstates what run 1 shows. The bound check passed at every point in run 1.

What I changed. I changed the check, not the derivation: only the quadrature method (to mpmath's tanh-sinh, with the outer integral split at $s=|\mathbf x|$). The tolerance, the formula and the bound are unchanged. Run 2 passes all criteria, with the bound attained at $\mathbf x=\mathbf 0$.

Run 1 code and output:

```python
# C5: the Kato-class quantity for V = -1/r in three dimensions, eq. (C3)-(C5).
# Environment: Python 3.13.16, numpy 2.5.3, scipy 1.18.1. Deterministic.
#
#   f_delta(x) = int_{|y-x|<delta} d^3y / (|y| |x-y|)
# Claim derived in the answer (AM-GM plus the bathtub comparison): f_delta(x) <= 4 pi delta for every x.
# Recalled comparison formula [R] (Newton's theorem for the shell average of 1/|x+s w|):
#   f_delta(x) = 4 pi (delta - |x|/2) for |x| <= delta,  2 pi delta^2/|x| for |x| >= delta.
# Computed here by direct quadrature in coordinates centred at x: y = x + s w, d^3y = s^2 ds dOmega,
#   f = 2 pi int_0^delta s ds int_{-1}^{1} dc (|x|^2 + s^2 + 2|x| s c)^(-1/2).
# Declared failure: any value exceeding 4 pi delta (1 + 1e-8), or disagreement with the recalled
# formula by more than 1e-7 relative (the latter would falsify only the [R] formula, not the bound).
import numpy as np
from scipy.integrate import quad

fails = []
print(" delta   |x|/delta   f (quadrature)     4 pi delta      Newton formula [R]   rel.diff")
for delta in (0.1, 1.0):
    for q in (0.0, 0.1, 0.5, 0.99, 1.0, 1.5, 3.0):
        X = q * delta
        def inner(s_):
            if X == 0.0:
                return 2.0 / s_ * s_  # int_{-1}^{1} dc / s = 2/s, times s
            g = lambda c: 1.0 / np.sqrt(X * X + s_ * s_ + 2 * X * s_ * c)
            pts = [-1.0, 1.0]
            val, _ = quad(g, -1.0, 1.0, epsabs=0, epsrel=1e-12, limit=200, points=None if abs(s_ - X) > 1e-12 else None)
            return s_ * val
        f, _ = quad(inner, 0.0, delta, epsabs=0, epsrel=1e-11, limit=400, points=[X] if 0 < X < delta else None)
        f *= 2 * np.pi
        newton = 4 * np.pi * (delta - X / 2) if X <= delta else 2 * np.pi * delta**2 / X
        rel = abs(f - newton) / newton
        print(f" {delta:<6} {q:<10}  {f:.12f}   {4*np.pi*delta:.12f}   {newton:.12f}    {rel:.1e}")
        if f > 4 * np.pi * delta * (1 + 1e-8):
            fails.append(("bound", delta, q))
        if rel > 1e-7:
            fails.append(("newton", delta, q))
print("FAILURES:", fails if fails else "none")
```

```
c5_kato_class_run1_scipy.py:25: IntegrationWarning: The algorithm does not converge.  Roundoff error is detected
  in the extrapolation table.  It is assumed that the requested tolerance
  cannot be achieved, and that the returned result (if full_output = 1) is 
  the best which can be obtained.
  val, _ = quad(g, -1.0, 1.0, epsabs=0, epsrel=1e-12, limit=200, points=None if abs(s_ - X) > 1e-12 else None)
c5_kato_class_run1_scipy.py:27: IntegrationWarning: The maximum number of subdivisions (400) has been achieved.
  If increasing the limit yields no improvement it is advised to analyze 
  the integrand in order to determine the difficulties.  If the position of a 
  local difficulty can be determined (singularity, discontinuity) one will 
  probably gain from splitting up the interval and calling the integrator 
  on the subranges.  Perhaps a special-purpose integrator should be used.
  f, _ = quad(inner, 0.0, delta, epsabs=0, epsrel=1e-11, limit=400, points=[X] if 0 < X < delta else None)
 delta   |x|/delta   f (quadrature)     4 pi delta      Newton formula [R]   rel.diff
 0.1    0.0         1.256637061436   1.256637061436   1.256637061436    0.0e+00
 0.1    0.1         1.193805208364   1.256637061436   1.193805208364    0.0e+00
 0.1    0.5         0.942477796077   1.256637061436   0.942477796077    3.5e-16
 0.1    0.99        0.634601818606   1.256637061436   0.634601716025    1.6e-07
 0.1    1.0         0.628318530718   1.256637061436   0.628318530718    5.3e-16
 0.1    1.5         0.418879020479   1.256637061436   0.418879020479    0.0e+00
 0.1    3.0         0.209439510239   1.256637061436   0.209439510239    1.3e-16
 1.0    0.0         12.566370614359   12.566370614359   12.566370614359    0.0e+00
 1.0    0.1         11.938052083641   12.566370614359   11.938052083641    1.5e-16
 1.0    0.5         9.424777960769   12.566370614359   9.424777960769    0.0e+00
 1.0    0.99        6.346018199967   12.566370614359   6.346017160251    1.6e-07
 1.0    1.0         6.283185307180   12.566370614359   6.283185307180    0.0e+00
 1.0    1.5         4.188790204786   12.566370614359   4.188790204786    2.1e-16
 1.0    3.0         2.094395102393   12.566370614359   2.094395102393    2.1e-16
FAILURES: [('newton', 0.1, 0.99), ('newton', 1.0, 0.99)]
```

Run 2 code and output:

```python
# C5 (run 2): the Kato-class quantity for V = -1/r in three dimensions, eq. (C3)-(C5).
# Environment: Python 3.13.16, mpmath 1.3.0. Deterministic.
# CHANGE FROM RUN 1 (c5_kato_class_run1_scipy.py): run 1 used scipy QUADPACK and failed the comparison with
# the recalled Newton formula at |x|/delta = 0.99 by 1.6e-7 (tolerance 1e-7), with QUADPACK reporting
# non-convergence for exactly that inner integral (integrable singularity at c = -1 when s ~ |x|).
# Run 2 changes ONLY the quadrature method (mpmath tanh-sinh, outer integral split at s = |x|).
# Tolerances, the formula and the bound are unchanged.
#
#   f_delta(x) = int_{|y-x|<delta} d^3y / (|y| |x-y|)
# Claim derived in the answer (AM-GM plus the bathtub comparison): f_delta(x) <= 4 pi delta for every x.
# Recalled comparison formula [R] (Newton's theorem): f = 4 pi (delta - |x|/2) for |x| <= delta,
#   2 pi delta^2/|x| for |x| >= delta.
# Computed by direct quadrature centred at x: f = 2 pi int_0^delta s ds int_{-1}^{1} dc (|x|^2+s^2+2|x|s c)^(-1/2).
# Declared failure: any value exceeding 4 pi delta (1 + 1e-8), or disagreement with the recalled
# formula by more than 1e-7 relative.
import mpmath as mp
mp.mp.dps = 30
fails = []
print(" delta   |x|/delta   f (quadrature)      4 pi delta        Newton formula [R]   rel.diff")
for delta in (mp.mpf('0.1'), mp.mpf(1)):
    for q in ('0', '0.1', '0.5', '0.99', '1', '1.5', '3'):
        X = mp.mpf(q) * delta
        def inner(s_):
            if X == 0:
                return mp.mpf(2)
            return s_ * mp.quad(lambda c: 1 / mp.sqrt(X**2 + s_**2 + 2 * X * s_ * c), [-1, 1])
        brk = [0, X, delta] if 0 < X < delta else [0, delta]
        f = 2 * mp.pi * mp.quad(inner, brk)
        newton = 4 * mp.pi * (delta - X / 2) if X <= delta else 2 * mp.pi * delta**2 / X
        rel = abs(f - newton) / newton
        print(f" {mp.nstr(delta,3):<6} {q:<10}  {mp.nstr(f,15):<18} {mp.nstr(4*mp.pi*delta,15):<17} {mp.nstr(newton,15):<20} {mp.nstr(rel,2)}")
        if f > 4 * mp.pi * delta * (1 + mp.mpf('1e-8')):
            fails.append(("bound", float(delta), q))
        if rel > mp.mpf('1e-7'):
            fails.append(("newton", float(delta), q))
print("FAILURES:", fails if fails else "none")
```

```
 delta   |x|/delta   f (quadrature)      4 pi delta        Newton formula [R]   rel.diff
 0.1    0           1.25663706143592   1.25663706143592  1.25663706143592     0.0
 0.1    0.1         1.19380520836412   1.25663706143592  1.19380520836412     0.0
 0.1    0.5         0.942477796076938  1.25663706143592  0.942477796076938    0.0
 0.1    0.99        0.634601716025138  1.25663706143592  0.634601716025138    0.0
 0.1    1           0.628318530717959  1.25663706143592  0.628318530717959    0.0
 0.1    1.5         0.418879020478639  1.25663706143592  0.418879020478639    0.0
 0.1    3           0.20943951023932   1.25663706143592  0.20943951023932     0.0
 1.0    0           12.5663706143592   12.5663706143592  12.5663706143592     0.0
 1.0    0.1         11.9380520836412   12.5663706143592  11.9380520836412     0.0
 1.0    0.5         9.42477796076938   12.5663706143592  9.42477796076938     0.0
 1.0    0.99        6.34601716025138   12.5663706143592  6.34601716025138     0.0
 1.0    1           6.28318530717959   12.5663706143592  6.28318530717959     0.0
 1.0    1.5         4.18879020478639   12.5663706143592  4.18879020478639     0.0
 1.0    3           2.0943951023932    12.5663706143592  2.0943951023932      0.0
FAILURES: none
```

## 5. Result

(a) For every $N\ge1$ and $\beta>0$, with $\Delta\tau=\beta/N$ and $\mathbf r_{N+1}\equiv\mathbf r_1$, the primitive trace is the bead integral

$$Z_N(\beta)=(2\pi\Delta\tau)^{-3N/2}\int_{\mathbb R^{3N}}d^3r_1\cdots d^3r_N\,\exp\Big\{-\sum_{j=1}^N\Big[\frac{|\mathbf r_{j+1}-\mathbf r_j|^2}{2\Delta\tau}-\frac{\Delta\tau}{r_j}\Big]\Big\}.$$

This is (A3), taken as the definition [A1]; the same formula in the notes' units is (A4).

(b) $Z_N(\beta)=+\infty$ for every $N\ge1$ and every $\Delta\tau>0$. Two regions of configuration space are responsible.

- Configurations in which any single bead approaches the origin. These carry infinite weight on their own (B9). Inside any bounded region they are the only source (B11), and they have no counterpart in the continuum.
- Configurations in which the whole chain moves off to infinity (B13). This divergence is already present for $V=0$ and is shared by the exact trace.

The kinetic factors cannot compensate. They are bounded below near any configuration with a bead at the origin, and maximal on the fully collapsed configuration. With an inner cutoff $\eta$ on every bead and the beads confined to $B_L$, the integral grows like $(2\pi\Delta\tau)^{-3N/2}\big(4\pi\eta^4e^{\Delta\tau/\eta}/\Delta\tau\big)^N$ as $\eta\to0$: the $N$-th power of the one-bead divergence, with no suppression from the kinetic factors at leading order (B16), confirmed for $N=2$ by C2. The divergence is not an artifact of the bead representation: the operator $T^N$, $N\ge2$, is defined only on the zero vector, and $T$ is unbounded (B.6).

(c) The exact kernel $K_\tau(\mathbf r,\mathbf r')$ is finite and jointly continuous on $\mathbb R^3\times\mathbb R^3$ for every $\tau>0$, because $-1/r$ is in the Kato class (C3) and Simon's kernel theorem applies. At the origin it is given by (C5); for instance $K_1(\mathbf 0,\mathbf 0)=0.91957$, confirmed by two independent routes in C4. The exact trace $\operatorname{Tr}e^{-\beta H}$ is $+\infty$ for every $\beta>0$, from the large-volume region only (C7); over a bounded region the exact diagonal kernel integrates to a finite number, whereas its primitive counterpart is infinite for every $N$.

The theorem that justifies time slicing is the Trotter product formula (C8) and (C9). Its imaginary-time clause requires both summands to be bounded below (in Kato's 1978 version, positive). $V=-1/r$ violates exactly that hypothesis and no other: the pieces are self-adjoint, and $K+V$ is self-adjoint on $D(K)=D(K)\cap D(V)$ by Kato's theorem. Consequently the real-time product formula holds for hydrogen and the imaginary-time one is not available.

Assessment of H1 to H6:

| Hypothesis | Verdict | Where |
|---|---|---|
| H1 | closed paths: correct. Ground-state dominance and $E_0\approx-\ln Z/\beta$: wrong for hydrogen in $\mathbb R^3$, since $Z=\infty$ | p. 4; Part D, (C7) |
| H2 | wrong for $V=-1/r$: $e^{-\Delta\beta V}$ is unbounded and the per-slice expansion fails near $r=0$ for every $\Delta\beta$. Incomplete even for matrices (no error accumulation) | p. 5; Part D, C.6 |
| H3 | wrong as written: $\beta V$ for $\Delta\beta V$ (p. 6, fixed implicitly on p. 7); a one-dimensional prefactor $m/2$ and scalar coordinates for a three-dimensional problem; minor typos | p. 6, also p. 8; Part D, (A4) |
| H4 | correct, but not sufficient on its own | p. 8 |
| H5 | correct, unproven; proof (B1) to (B3), growth law (B6); p. 9 item 1 reads "→ 0", probably shorthand | p. 8, p. 9 |
| H6 | correct conclusion, unproven; proof (B7) to (B9), sharpened in (B16). The large-volume divergence is not mentioned | p. 9 |

Domain of validity: hydrogen with an infinitely heavy point nucleus, in $\mathbb R^3$, atomic units, any $N\ge1$, any $\Delta\tau>0$. The statements about $Z_N$ hold for the bead integral as defined by [A1].

## 7. Risk register

| Item | Type | What happens if it is wrong |
|---|---|---|
| (A3) taken as the definition of $Z_N$ | [A1], load-bearing | If an operator trace were intended: B.6 shows it does not exist, so the conclusion of (b) only strengthens |
| Trotter theorem statement, semigroup clause "A and B bounded below" (Reed–Simon I, Thm VIII.31) | [V] through secondary sources; Reed–Simon itself {ver: no} | If the clause reads "positive" or "non-negative", the identification of the violated hypothesis is unchanged, since $V$ is neither. If the theorem number is wrong, the locator is wrong but the content stands |
| Kato's 1978 formula, positive self-adjoint $A$, $B$ (Simon 2017, Thm 18.2) | [V], partial: excerpts confirmed the number, the title and the "positive self-adjoint" hypothesis; full statement not displayed | The remark on Kato's version would need rewording; the main identification rests on (C9) |
| $H$ self-adjoint on $D(K)$ (Kato's theorem) | [V] (Simon 2017, §7, from excerpts) | Hypothesis (ii) in C.6 would be unverified; this is low risk, being a classical theorem |
| Continuous kernel for Kato-class $V$ (Simon 1982, Thm B.7.1) | [S] {ver: no}; supported by the Broderix–Hundertmark–Leschke abstract {ver: tool} | Finiteness at general points would rest only on the BHL abstract; finiteness at the origin is independently established by C4 |
| Coulomb data at the origin: $1/(\pi n^3)$, the Sommerfeld factor, $E_n$, completeness | [V] (Fäldt and Wilkin, eqs. (19), (21)); $E_n$ and completeness [R] | Route (i) of C4 would be wrong; route (ii) does not use these data, and the two agree to $5\times10^{-7}$ |
| $l=0$ boundary condition $u(0)=0$ in C4 route (ii) | [A]/[R] | Route (ii) would compute a different self-adjoint extension; the agreement with route (i) argues against this |
| Identity theorem for real-analytic functions | [R] | Remark B.6 would be unproven; (b) does not depend on it |
| Spectral theorem and functional calculus used in (C6) | [R] | Very low risk; the bound-state argument gives (C7) independently, through [R] spectral data |
| Hydrogen spectrum $E_n=-1/(2n^2)$ with multiplicity $n^2$ | [R]; $E_{1,2,3}$ confirmed by C4 | Used only as an illustration in C.4 |
| Newton's theorem closed form | [R] | Used only as a comparison inside C5 |
| Feynman–Kac and Khas'minskii remark in C.6 | [R] {ver: no} | Qualitative and not used |
| Ground-state dominance for the kernel (H1 assessment) | [R] | Qualitative and not used |
| Reading of the handwritten notes (βV on p. 6; p. 9 item 1) | reading risk | An assessment of H3 or H5 could be misattributed; see Open questions |
| Prior-knowledge contamination from the project document | declared | The auditor should weigh the derivation against the declared result |

## 8. Sources

### Used

1. Encyclopedia of Mathematics, "Trotter product formula", the statement following eq. (a1): the unitary form holds when $A+B$ is essentially self-adjoint on $D(A)\cap D(B)$; the semigroup form holds for positive $t$ when $A$ and $B$ are bounded from below. https://encyclopediaofmath.org/wiki/Trotter_product_formula (the redirect page shows oldid 51065). {ver: tool}. Retrieval note: page text returned by web search; both statements read.
2. "An Introduction to Lieb's Simplified approach to the Bose gas", arXiv:2308.00290, Theorem A1.17: "Given two operators A and B on a Hilbert space such that A, B and A + B are self-adjoint, and bounded from below, then for t ≥ 0, e^{−t(A+B)} = lim (e^{−tA/N} e^{−tB/N})^N", attributed there to Teschl (2014), Theorem 5.12. {ver: tool}. Retrieval note: theorem text read in a search-result excerpt; Teschl not retrieved.
3. "Monotonicity of the Relative Entropy and the Two-sided Bogoliubov Inequality in von Neumann Algebras", arXiv:2501.04564, Theorem B.3.7, which quotes Reed–Simon I, Thm VIII.31, for the unitary product formula under "A+B essentially self-adjoint on dom(A) ∩ dom(B)". {ver: tool}. Retrieval note: search-result excerpt.
4. M. Reed and B. Simon, Methods of Modern Mathematical Physics I: Functional Analysis, revised ed. (1980), Theorem VIII.31. {ver: no}. Not retrieved; the semigroup clause is recalled and confirmed only through items 1 and 2.
5. B. Simon, "Tosio Kato's work on non-relativistic quantum mechanics", arXiv:1711.00528 (2017), §7, Theorem 7.3 (Kato–Rellich), and the sentence after eq. (7.15): "any V ∈ L²(ℝ³)+L^∞(ℝ³) is −Δ-bounded with relative bound zero". {ver: tool}. Retrieval note: the PDF fetched in this session was truncated after §5; §7 was read in search-result excerpts that reproduce the statement of Theorem 7.3 and that sentence. Also §18, Theorem 18.2 (Kato's product formula). {ver: tool}, partial: excerpts confirmed the number, the title, and that the result concerns positive self-adjoint $A$, $B$ (self-adjoint contraction semigroups); the full statement was not displayed.
6. G. Fäldt and C. Wilkin, "Bound and unbound wave functions at short distances", arXiv:quant-ph/9710049, §IV: eq. (19), $[\psi(k,0)]^2=2\pi\eta/(e^{2\pi\eta}-1)$ with $\eta=-me^2/\hbar^2k$ for attraction; eq. (21), $[\psi_n(0)]^2=4\alpha_n^3$; normalisations from eqs. (3) and (4). {ver: tool}. Retrieval note: the arXiv PDF was fetched and the equations and normalisations read. The arXiv page lists no journal reference.
7. K. Broderix, D. Hundertmark and H. Leschke, "Continuity properties of Schrödinger semigroups with magnetic fields", Rev. Math. Phys. 12, 181–225 (2000), arXiv:math-ph/9808004: abstract (continuous integral kernel for Kato-class scalar potentials, extending Simon 1982) and §6, "Continuity of the integral kernel of the semigroup". {ver: tool}. Retrieval note: abstract, introduction and table of contents read; the theorem number in §6 was not reached, because the fetched text ended in §2.
8. B. Simon, "Schrödinger semigroups", Bull. Amer. Math. Soc. (N.S.) 7, 447–526 (1982), Theorem B.7.1. {ver: no}. Retrieval note: the Project Euclid PDF returned a bot-check page; the AMS issue page confirmed only the title and pages.
9. Z. Shen, "Absolute continuity of periodic Schrödinger operators with potentials in the Kato class", Illinois J. Math. 45, 873–893 (2001), eq. (1.1), the definition of $K_d$. {ver: tool}. Retrieval note: search-result excerpt reproduces the definition.
10. The team's notes, `Integrales_de_Camino_de_Feynman_261017_174852_2.pdf`, pp. 4–9, the object of Part D. Read in full from the attachment.

### Consulted

- arXiv:1801.03361, which quotes Reed–Simon II, Theorem X.15 (self-adjointness of $-\Delta+v$ for $v\in L^2+L^\infty$, $n\le3$). {ver: tool}, search excerpt.
- arXiv:math-ph/9808011 ("Twist positivity"), which states the Lie–Trotter formula for self-adjoint, bounded-below $H_0$ and $V$ with essentially self-adjoint sum, citing "Theorem A.5.1 of [2]". {ver: tool}, search excerpt.
- J. Chung and Y.-J. Kim, SIAM J. Math. Anal. 45, 728–731 (2013), on Lieb–Loss, Analysis, Theorem 9.7 (Newton's theorem), which is used only for the comparison formula in C5. {ver: tool}, abstract.
- Other papers quoting the Gamow/Sommerfeld factor $2\pi\eta/(e^{2\pi\eta}-1)$ (e.g. arXiv:1710.04103 §2.2, arXiv:1406.6908 App. A). {ver: tool}, search excerpts; consistent with item 6.
- The project document `claude/start-here.md`, read because the project instructions require it. It did not affect the derivation and is declared in §1.

Not consulted: the GitHub repository named in prompt0 §5.

## 9. Open questions

1. Confirm in Reed–Simon I (revised edition, 1980) that Theorem VIII.31 contains the semigroup clause with "A and B bounded below". This needs library access, and a `{ver: human}` entry would settle it.
2. Confirm the statement of Simon 1982, Theorem B.7.1 (a jointly continuous kernel for $V_-\in K_\nu$, $V_+\in K_\nu^{\rm loc}$), through AMS or library access.
3. The notes' authors should confirm my reading of the handwriting: that the $\beta V$ in the second line of p. 6 is a slip of the pen, and what p. 9 item 1 is meant to say.
4. An auditor should check the real-analyticity step in B.6. A numerical illustration of its mechanism: for a positive $\psi$ supported away from the origin, $e^{-\Delta\tau K}(w\psi)$ evaluated at the origin is strictly positive.
5. A third route to $K_\tau(\mathbf 0,\mathbf 0)$: a Feynman–Kac Monte Carlo over Brownian bridges. It would also test finiteness away from the origin, which C4 does not.
6. A Monte Carlo estimate of $Z_N^{(L)}(\eta)$ for $N=3$ or 4, to test the $N$-th power law (B16) beyond $N=2$.
7. A question about the problem's intent, not a proposal. Since the exact $\operatorname{Tr}e^{-\beta H}$ is itself infinite in $\mathbb R^3$, H1's use of $Z$ needs a finite quantity. Which one does the larger project mean by $Z$?
