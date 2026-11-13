# P003.S02 — answer-2

Problem `P003.S02`, "A lower bound on the imaginary-time propagator from Jensen's inequality". Round 2, written in response to `audit-report-1` (verdict ACCEPT, one QUESTION, F1.1). Solver: Claude Opus 5.5 (`claude-opus-5-5`); tools: code, web; context: clean; date 2026-11-13. Conventions v1.5. The sections frozen by audit 1 (3.1, 3.2, 3.3, 3.5.2, 3.5.3, 3.6, 3.7) are reproduced byte-for-byte from answer-1; §4.2 records the check. The Prior-knowledge declaration is also reproduced unchanged, because it records what I knew before the first derivation. Every computation cited as `[N]` was rerun for this round; §4.5 has the code and the fresh output.

## Response to audit 1

| id | Disposition | What changed | Where |
|---|---|---|---|
| F1.1 (QUESTION: notation $\nabla V\cdot\nabla^3V[\Delta,\Delta,\cdot\,]$ ambiguous without indices) | accepted | The intended contraction is exactly the auditor's $\sum_{i,j,k}\partial_iV\,\partial_i\partial_j\partial_kV\,\Delta_j\Delta_k$. §3.5.4 now uses component notation with summation over repeated indices throughout: the decomposition $A_1,\dots,C_3$, the Isserlis moments written in components, every covariance, and (27)–(28). A dictionary maps each vector expression of answer-1 to its index form; it also makes explicit that $\operatorname{tr}\mathsf H^2=V_{ij}V_{ij}$ (not $(\nabla^2V)^2$) and that $\nabla V\cdot\nabla(\nabla^2V)=V_iV_{ijj}$. The symmetrization shorthand $3\delta_{a(b}\delta_{cd)}$ is replaced by the explicit three-term sum. Beyond notation, I added a check that makes the contractions testable rather than only legible: S9 computes $\operatorname{Var}S$ exactly in $d=2$ for cubic-plus-quartic potentials with random rational coefficients and matches every term of (27) through $O(\tau^4)$. It also rejects two wrong readings: $(V_i\Delta_i)(V_{jkk}\Delta_j)$ in place of $V_iV_{ijk}\Delta_j\Delta_k$, and $(\operatorname{tr}\mathsf H)^2$ in place of $\operatorname{tr}\mathsf H^2$. No coefficient, sign or power changed. | §2.2 (two new rows); §3.5.4; §4.1 items 1, 3, 4; §4.2; §4.3 (S9); §4.4 (R8–R11); §4.5.5; §5; §6; §7 items 23–25; §9 items 8–9 |

Remarks on audit 1. These are not rebuttals of F1.1; they are points the next reader of this loop should have.

1. Verdict versus CONVENTIONS §5. ACCEPT is defined as "no BLOCKER, no MAJOR, no open QUESTION", so with F1.1 open the conventions did not permit ACCEPT. None of the other verdicts fits either: ACCEPT-WITH-FIXES covers only MINOR and NIT, and REVISE needs a MAJOR. I read this as a gap in the conventions, which define no verdict for "open QUESTION only", rather than as an error of the auditor. If the next audit closes F1.1, ACCEPT applies cleanly.

2. What audit 1 did not cover. Its metadata reports no code execution and no web access, and its Pass 6 (code audit) is marked not performed. The verification code and the `{ver: no}` locators (Reed–Simon I Thms S.21, VI.23, VIII.20(b), VIII.25(a); Reed–Simon II Thms IX.28, X.15, X.28; Rudin Thms 1.26, 1.34, 3.3) have therefore been examined only by me. The ACCEPT should be read with that scope. I have added this to the Risk register (item 25) and to Open questions (item 9).

3. Frozen sections carry open `[?]` flags. Three of them, all now frozen and reproduced unchanged, contain flagged items: §3.2 (the remark on removing [A3] within the product-formula route); §3.3 (the pointwise form of (18) without [A3]); and §3.6 ((48) needs exponential moments of $X$, and (49) is a heuristic). Freezing a section does not discharge its flags, so they remain in the Risk register as items 9, 10, 14 and 15.

4. Audit 1 reports recomputing $\iint C\,du\,dv$ and the circulant eigenvalues. Both agree with S4 ($I_1=D\tau^3/6$) and with (37) in this document.

## 1. Prior-knowledge declaration

1. Do I recognize the problem? In outline, yes. Bounding a Feynman–Kac expectation from below by Jensen's inequality, $\langle e^{-S}\rangle \ge e^{-\langle S\rangle}$, with a Gaussian reference measure is Feynman's variational idea (Feynman & Hibbs, *Quantum Mechanics and Path Integrals*, ch. 11; Feynman, *Statistical Mechanics*, ch. 3; both from memory, locators not verified). As far as I recall, applying it slice by slice with the free Brownian bridge as the reference measure is the construction of the Kole–De Raedt paper excluded in §5 of the prompt. I have not consulted that paper (or the excluded repository) in this session, and I do not remember its specific claims: neither the convergence order it states nor the details of its Coulomb treatment. I know the Gaussian-smeared Coulomb potential $\operatorname{erf}(r/\sqrt2\sigma)/r$ from Ewald sums and Gaussian-basis electronic structure.

2. The result I believed to be standard before deriving anything: inequality $(\ast)$ with $\langle V\rangle_u(\mathbf x,\mathbf x') = \int d^dy\,\rho_0(\mathbf x,\mathbf y;u)V(\mathbf y)\rho_0(\mathbf y,\mathbf x';\tau-u)/\rho_0(\mathbf x,\mathbf x';\tau)$. Equivalently, a Gaussian average of $V$ whose mean lies on the straight line from $\mathbf x$ to $\mathbf x'$ and whose variance is $2Du(\tau-u)/\tau$ per coordinate. Then $\hat Z_m\le \operatorname{Tr}e^{-\beta H}$ by multiplying slice bounds, and the trapezium rule gives the symmetric (primitive) Trotter kernel. On the error, I expected a local defect of order $\tau^3$ and a global error of order $1/m^2$, by analogy with the symmetric Trotter splitting; I had no coefficient in mind. For Coulomb, I expected the smeared potential to be bounded at the origin, so that the averaged action stays finite where the primitive factor $e^{\tau q^2/2r}$ is not integrable. I also expected the smooth-potential error estimate to fail there.

3. The standard route: the Trotter product formula plus Jensen applied to the bead measure, or the Feynman–Kac bridge representation plus Jensen plus Fubini. The bridge form of Feynman–Kac is Simon, *Functional Integration and Quantum Physics*, Thm 6.6. I know that locator only through Simon, arXiv:math-ph/9907022, which I retrieved and which cites it; the book itself was not retrieved.

4. What I am anchored on. Section 3c of the prompt is empty, so nothing comes from the prompt. My own anchors are the expectations listed in item 2, and the most consequential is the $1/m^2$ expectation. Only after deriving the leading local defect $D\tau^3|\nabla V|^2/12$ (§3.5.4) did I notice that it coincides with the Takahashi–Imada correction term. That comparison was made after the computation; it is reported in the Convergence check and was not used in the derivation.

## 2. Setup

### 2.1 Conventions

$\hbar=1$. Imaginary times $\tau,\beta,u$ have dimension 1/energy, and $D$ has dimension energy × length². Points of $\mathbb R^d$ are written $x,x',y$ (vectors, not bold, in what follows). $d$ is general in (a) and (b), $d=3$ in (c), and $d=1$ with $D=\tfrac12$ in (d). $e^{-\infty}:=0$. "Kernel" always means the jointly continuous integral kernel. Its existence for the potentials used here is a cited fact (§3.2, step T6).

### 2.2 Symbol table

| Symbol | Meaning |
|---|---|
| $K=-D\nabla^2$, $V$, $H$ | kinetic operator, potential, Hamiltonian ($H=K\dotplus V$, see [A1]) |
| $\rho_0(x,x';t)$ | free kernel, eq. (2) |
| $K_\tau(x,x')$ | kernel of $e^{-\tau H}$, i.e. $\langle x|e^{-\tau H}|x'\rangle$ |
| $p_u(y\,|\,x,x';\tau)$ | one-time marginal of the free bridge at time $u$, eq. (3) |
| $m(u)$, $\sigma_u^2$ | mean and per-component variance of $p_u$, eqs. (5), (6) |
| $C(u,v)$ | bridge covariance (per component), eq. (8) |
| $\langle V\rangle_u(x,x')$ | bridge average of $V$ at time $u$, eq. (4) |
| $\Phi_\tau(x,x')$ | $\int_0^\tau du\,\langle V\rangle_u(x,x')$ (averaged action) |
| $R_\tau(x,x')$ | $\rho_0(x,x';\tau)e^{-\Phi_\tau(x,x')}$, the right side of $(\ast)$ |
| $\omega(u)$, $\xi(u)$ | bridge path; its centred part $\omega-m$ |
| $S[\omega]$ | $\int_0^\tau V(\omega(u))du$ |
| $\delta(x,x';\tau)$ | $\ln K_\tau-\ln R_\tau$ (local defect) |
| $\bar x$, $\Delta$ | $(x+x')/2$, $x'-x$ |
| $s(u)$ | $u/\tau-\tfrac12$ |
| $i,j,k,l$ | Cartesian indices $1,\dots,d$; a repeated index is summed (in §3.5.4 and §4 only) |
| $V_i,\ V_{ij},\ V_{ijk}$ | $\partial_iV,\ \partial_i\partial_jV,\ \partial_i\partial_j\partial_kV$ at $\bar x$; $\mathsf H$ is the matrix $(V_{ij})$ |
| $m$, $\varepsilon$ | number of slices; $\varepsilon=\tau/m$ in (a), $\tau=\beta/m$ in (b) |
| $T_m$ | $(e^{-\varepsilon K}e^{-\varepsilon V})^m$, eq. (13) |
| $P_m$ | normalized bead density, eq. (15) |
| $Z$, $\hat Z_m$, $\langle\cdot\rangle_\beta$ | $\operatorname{Tr}e^{-\beta H}$, the Jensen approximant (21), the thermal average |
| $c$ | constant with $V\ge -c$ |
| $q^2$, $V_N$, $H_N$ | Coulomb strength, truncated potential (39), its Hamiltonian |
| $\kappa$, $\omega_0$ | oscillator constant; $\omega_0=\sqrt{2D\kappa}$ (written $\omega$ in code) |

### 2.3 Problem restated, and standing assumptions

We are given $H=K+V$ on $L^2(\mathbb R^d)$ with $K=-D\nabla^2$, $D>0$, $V$ real, and
$$H = K + V,\qquad K=-D\nabla^2, \tag{1}$$
$$\rho_0(x,x';t)=(4\pi Dt)^{-d/2}\exp\!\big(-|x-x'|^2/4Dt\big)\quad\text{(prompt §3a, trusted).}\tag{2}$$
(a) asks for $K_\tau\ge R_\tau$ by two routes; (b) for $\hat Z_m$, $\hat Z_m\le Z$, the trapezium identity, the leading small-$\tau$ defect and the resulting order in $1/m$; (c) for the Coulomb case; and (d) for numerical tests on the oscillator.

[A1] Definition of $H$. For $V$ continuous and bounded below, $H$ is the self-adjoint operator associated with the closed form $\phi\mapsto D\int|\nabla\phi|^2+\int V|\phi|^2$ on $H^1\cap\{\int|V||\phi|^2<\infty\}$, written $K\dotplus V$. What it buys: Kato's product formula (step T1) applies without any essential-self-adjointness argument. For such $V$ the form sum coincides with the closure of $K+V$ on $C_c^\infty$ (Kato's theorem that $-\Delta+V$, $V\in L^2_{\rm loc}$, $V\ge0$, is essentially self-adjoint on $C_c^\infty$; Reed–Simon II, Thm X.28, `[R]`), so nothing depends on the choice. What breaks without it: for unbounded $V$, "$e^{-\tau H}$" is otherwise not defined.

[A2] (a) as given: $V$ continuous, $V\ge -c$ for some $c\ge0$.

[A3] Growth condition, used only in step T6 of the product-formula route and for the pointwise form of the conclusion: for every $a>0$ there is a $C_a$ with $V(y)\le C_a e^{a|y|^2}$. What it buys: $u\mapsto\langle V\rangle_u$ is finite and continuous on $[0,\tau]$, and $\Phi_\tau$ is continuous in $(x,x')$. Every polynomially bounded potential satisfies it. What breaks without it: the Riemann-sum step of route T, and the passage from "almost every $(x,x')$" to "every $(x,x')$" (see the end of §3.3). The Feynman–Kac route gives the integrated (bilinear) form of $(\ast)$ without it.

[A4] (b), error analysis: $V\in C^4$, bounded below as in [A2], with bounded derivatives of orders 1 to 4; e.g. $V=\sqrt{1+|x|^2}$, which is also confining. Bounded derivatives alone do not give a lower bound (consider $F\cdot x$), and without one the hypotheses of (a) fail. The oscillator has an unbounded gradient; for it the local result is used pointwise in $\bar x$, and its global coefficient is finite because $\langle|\nabla V|^2\rangle_\beta<\infty$.

[A5] (b), trace statements: $\operatorname{Tr}e^{-\beta H}<\infty$, as the prompt specifies.

[A6] The "free Brownian bridge" of the prompt is the process whose finite-dimensional distributions are products of $\rho_0$ normalized by $\rho_0(x,x';\tau)$, i.e. Brownian motion with generator $D\nabla^2$ conditioned to go from $x$ at time $0$ to $x'$ at time $\tau$. This is the only reading consistent with $\rho_0$ being the transition density. If a bridge with another diffusion constant were meant, the variance (6) would change and neither derivation would produce $(\ast)$.

## 3. Derivation

### 3.1 The free bridge, and $\langle V\rangle_u$ in terms of free kernels

By [A6] the one-time marginal of the bridge at time $u\in(0,\tau)$ is
$$p_u(y\,|\,x,x';\tau)=\frac{\rho_0(x,y;u)\,\rho_0(y,x';\tau-u)}{\rho_0(x,x';\tau)},\tag{3}$$
and therefore
$$\langle V\rangle_u(x,x')=\int d^dy\;\frac{\rho_0(x,y;u)\,V(y)\,\rho_0(y,x';\tau-u)}{\rho_0(x,x';\tau)}.\tag{4}$$
Equation (4) is the requested expression of $\langle V\rangle_u$ through free kernels.

`[D]` Gaussian form. Write $a=u$ and $b=\tau-u$, so that $a,b>0$ and $a+b=\tau$. The exponent of the numerator of (3) is
$$-\frac{|y-x|^2}{4Da}-\frac{|x'-y|^2}{4Db}=-\frac1{4D}\Big[\Big(\frac1a+\frac1b\Big)|y|^2-2y\cdot\Big(\frac xa+\frac{x'}b\Big)+\frac{|x|^2}a+\frac{|x'|^2}b\Big].$$
Since $\frac1a+\frac1b=\frac{\tau}{ab}$, define $\sigma^2:=2Dab/\tau$; then $\frac1{4D}\frac\tau{ab}=\frac1{2\sigma^2}$. The linear coefficient is $\frac1{4D}\cdot2\big(\frac xa+\frac{x'}b\big)=\frac{bx+ax'}{2Dab}=\frac{1}{\sigma^2}\,\frac{bx+ax'}{\tau}$. With $m:=(bx+ax')/\tau$ the exponent becomes
$$-\frac{|y-m|^2}{2\sigma^2}+\frac{|m|^2}{2\sigma^2}-\frac1{4D}\Big(\frac{|x|^2}a+\frac{|x'|^2}b\Big).$$
The $y$-independent part is
$$\frac{|bx+ax'|^2}{4Dab\tau}-\frac{\tau\,(b|x|^2+a|x'|^2)}{4Dab\tau}=\frac{b^2|x|^2+2ab\,x\cdot x'+a^2|x'|^2-(a+b)b|x|^2-(a+b)a|x'|^2}{4Dab\tau}=\frac{-ab\,|x-x'|^2}{4Dab\tau}=-\frac{|x-x'|^2}{4D\tau}.$$
The prefactor of the numerator is $(4\pi Da)^{-d/2}(4\pi Db)^{-d/2}$. Dividing by $\rho_0(x,x';\tau)=(4\pi D\tau)^{-d/2}e^{-|x-x'|^2/4D\tau}$ cancels the exponential just found and leaves the prefactor $(4\pi Dab/\tau)^{-d/2}=(2\pi\sigma^2)^{-d/2}$. Hence
$$p_u(y\,|\,x,x';\tau)=(2\pi\sigma_u^2)^{-d/2}\exp\!\Big(-\frac{|y-m(u)|^2}{2\sigma_u^2}\Big),\qquad m(u)=x+\frac u\tau(x'-x),\tag{5}$$
$$\sigma_u^2=\frac{2Du(\tau-u)}{\tau}.\tag{6}$$
`[N]` S1 checks (5)–(6) symbolically against the definition (3).

`[D]` Chapman–Kolmogorov. Integrating (5) over $y$ gives 1. Multiplying back by $\rho_0(x,x';\tau)$:
$$\int d^dy\;\rho_0(x,y;a)\,\rho_0(y,x';b)=\rho_0(x,x';a+b)\qquad(a,b>0).\tag{7}$$
`[N]` S2.

`[D]` Two-time law and covariance. For $0<u<v<\tau$ the joint density of $(\omega(u),\omega(v))$ is, by [A6], $\rho_0(x,y_1;u)\rho_0(y_1,y_2;v-u)\rho_0(y_2,x';\tau-v)/\rho_0(x,x';\tau)$; applying (7) twice shows it is normalized. It factorizes over Cartesian components. Per component the exponent is $-\tfrac12(y-\mu)^{\mathsf T}P(y-\mu)+{\rm const}$ with
$$2D\,P=\begin{pmatrix}\frac1u+\frac1{v-u}&-\frac1{v-u}\\[2pt]-\frac1{v-u}&\frac1{v-u}+\frac1{\tau-v}\end{pmatrix}=\begin{pmatrix}\frac{v}{u(v-u)}&-\frac1{v-u}\\[2pt]-\frac1{v-u}&\frac{\tau-u}{(v-u)(\tau-v)}\end{pmatrix}.$$
Its determinant is $\frac{v(\tau-u)}{u(v-u)^2(\tau-v)}-\frac1{(v-u)^2}=\frac{v(\tau-u)-u(\tau-v)}{u(v-u)^2(\tau-v)}=\frac{\tau}{u(v-u)(\tau-v)}$. Inverting,
$$P^{-1}_{11}=2D\,\frac{u(v-u)(\tau-v)}{\tau}\cdot\frac{\tau-u}{(v-u)(\tau-v)}=\frac{2Du(\tau-u)}\tau,\quad P^{-1}_{12}=2D\,\frac{u(v-u)(\tau-v)}{\tau}\cdot\frac1{v-u}=\frac{2Du(\tau-v)}\tau,\quad P^{-1}_{22}=\frac{2Dv(\tau-v)}\tau.$$
So the centred bridge $\xi=\omega-m$ has
$$\mathbb E\,\xi_a(u)\xi_b(v)=\delta_{ab}\,C(u,v),\qquad C(u,v)=\frac{2D\,\min(u,v)\,\big(\tau-\max(u,v)\big)}{\tau}.\tag{8}$$
`[N]` S3 (precision matrix read off from the kernel product, inverted, and compared with (8); means compared with (5)).

`[D]` A form used repeatedly: substituting $y=m(u)+\sigma_u z$ in (4)–(5),
$$\langle V\rangle_u(x,x')=(2\pi)^{-d/2}\int d^dz\;e^{-|z|^2/2}\,V\big(m(u)+\sigma_u z\big).\tag{9}$$
The right side also makes sense at $u=0$ and $u=\tau$, where $\sigma=0$, and there it equals $V(x)$ and $V(x')$.

`[D]` Lemma J (Jensen's inequality in the form used). Let $\mu$ be a probability measure and $X$ a measurable function with values in $(-\infty,\infty]$ and $X\ge-c$. Then $\mathbb E_\mu X\in[-c,\infty]$ is defined, and
$$\mathbb E_\mu\, e^{-X}\ \ge\ e^{-\mathbb E_\mu X},\tag{10}$$
with equality iff $X$ is $\mu$-a.e. constant. Proof. If $\mathbb E X=\infty$ the right side is $0$ and the left side is $\ge0$. Otherwise $X\in L^1(\mu)$; put $a=\mathbb E X$. The function $f(s)=e^{-s}-1+s$ has $f(0)=0$ and $f'(s)=1-e^{-s}$, which is $\le0$ for $s\le0$ and $\ge0$ for $s\ge0$, so $f\ge0$, i.e. $e^{-s}\ge1-s$. With $s=t-a$ and multiplying by $e^{-a}$: $e^{-t}\ge e^{-a}\big(1-(t-a)\big)$ for every real $t$; for $t=+\infty$ this holds trivially. Put $t=X$ and integrate, which is allowed because $\mu$ is a nonnegative measure and the right side is integrable. This gives $\mathbb E e^{-X}\ge e^{-a}(1-\mathbb E X+a)=e^{-a}$. Equality forces $f(X-a)=0$ a.e., i.e. $X=a$ a.e. This is the measure-theoretic Jensen inequality for the convex function $e^{-t}$ (Rudin, *Real and Complex Analysis*, 3rd ed., Thm 3.3, `[R]`); the proof above makes the citation non-load-bearing.

`[D]` Examples, from the Gaussian moments of (5): for $V=\tfrac\kappa2|y|^2$, $\langle V\rangle_u=\tfrac\kappa2(|m(u)|^2+d\,\sigma_u^2)$; for $V=V_0\cos(k\cdot y)$, $\langle V\rangle_u=V_0\cos(k\cdot m(u))\,e^{-|k|^2\sigma_u^2/2}$; for $d=1$ and $V=\lambda y^4$, $\langle V\rangle_u=\lambda(m^4+6m^2\sigma_u^2+3\sigma_u^4)$. `[N]` N1 checks all three by quadrature from (4). For the one-dimensional oscillator, using $\int_0^\tau(x+u\Delta/\tau)^2du=\tau(x^2+x\Delta+\Delta^2/3)=\tfrac\tau3(x^2+xx'+x'^2)$ (with $\Delta=x'-x$) and $\int_0^\tau\sigma_u^2du=2D(\tfrac{\tau^2}2-\tfrac{\tau^2}3)=\tfrac{D\tau^2}{3}$:
$$\langle V\rangle_u=\tfrac\kappa2\big(m(u)^2+\sigma_u^2\big),\tag{11}$$
$$\Phi_\tau(x,x')=\int_0^\tau du\,\langle V\rangle_u=\frac{\kappa\tau}{6}\,(x^2+xx'+x'^2)+\frac{\kappa D\tau^2}{6}.\tag{12}$$
`[N]` S5 computes (12) symbolically from the definition (4).

### 3.2 Part (a), first derivation: Trotter product formula

Step T1 `[V]`, product formula. Kato's product formula for form sums: for closed quadratic forms $q_1,q_2$ with associated semigroups $e^{-tA},e^{-tB}$, $\text{s-lim}_{m\to\infty}(e^{-tA/m}e^{-tB/m})^m=e^{-tC}P$. Here $C$ is the operator of the form sum on $Q(q_1)\cap Q(q_2)$ and $P$ is the projection onto the closure of that set (Simon, arXiv:1711.00528, Thm 18.2 with eq. (18.6); its Remark 1 refers to Reed–Simon I, Thm S.21). Take $q_1(\phi)=D\int|\nabla\phi|^2$ (operator $K$) and $q_2(\phi)=\int(V+c)|\phi|^2$ (multiplication by $V+c\ge0$). Because $V$ is continuous, hence locally bounded, $C_c^\infty\subset Q(q_1)\cap Q(q_2)$, which is therefore dense, so $P=1$. By [A1] the form-sum operator is $H+c$. With $\varepsilon=\tau/m$, and since the scalar $e^{-\varepsilon c}$ commutes with everything, $(e^{-\varepsilon K}e^{-\varepsilon(V+c)})^m=e^{-\tau c}(e^{-\varepsilon K}e^{-\varepsilon V})^m$. Multiplying by $e^{\tau c}$:
$$e^{-\tau H}=\text{s-}\lim_{m\to\infty}T_m,\qquad T_m:=\big(e^{-\varepsilon K}e^{-\varepsilon V}\big)^m.\tag{13}$$

Step T2 `[D]`, the kernel of $T_m$. The operator $e^{-\varepsilon K}$ has kernel $\rho_0(\cdot,\cdot;\varepsilon)$ (prompt §3a), and $e^{-\varepsilon V}$ is multiplication by $e^{-\varepsilon V(y)}\in(0,e^{\varepsilon c}]$. So $(e^{-\varepsilon K}e^{-\varepsilon V}f)(x_0)=\int d^dx_1\,\rho_0(x_0,x_1;\varepsilon)e^{-\varepsilon V(x_1)}f(x_1)$. Applying this $m$ times and writing the iterated integral as one integral,
$$T_m(x,x')=\int d^dx_1\cdots d^dx_{m-1}\ \prod_{j=1}^m\rho_0(x_{j-1},x_j;\varepsilon)\,e^{-\varepsilon V(x_j)},\qquad x_0=x,\ x_m=x'.\tag{14}$$
Combining the iterated integrals in arbitrary order is Tonelli's theorem when $f\ge0$, because every factor is nonnegative; for general $f$, split $f$ into four nonnegative parts. (Positivity use P1, §3.4.)

Step T3 `[D]`, bead measure. For fixed $x,x'$ define
$$P_m(x_1,\dots,x_{m-1}):=\frac{\prod_{j=1}^m\rho_0(x_{j-1},x_j;\varepsilon)}{\rho_0(x,x';\tau)},\qquad\text{so that}\qquad T_m(x,x')=\rho_0(x,x';\tau)\;\mathbb E_{P_m}\!\big[e^{-X_m}\big],\quad X_m:=\varepsilon\sum_{j=1}^m V(x_j).\tag{15}$$
$P_m\ge0$ (P2), and the denominator is strictly positive for all $x,x'$ (P3). Normalization follows from (7): integrating over $x_1$ with $a=b=\varepsilon$ gives $\rho_0(x,x_2;2\varepsilon)$; then over $x_2$ with $a=2\varepsilon$, $b=\varepsilon$, giving $\rho_0(x,x_3;3\varepsilon)$; and so on until $x_{m-1}$, which leaves $\rho_0(x,x';m\varepsilon)=\rho_0(x,x';\tau)$. Hence $\int P_m=1$.

Step T4 `[D]`, marginal of bead $j$ and its time. Fix $1\le j\le m-1$. Integrating out $x_1,\dots,x_{j-1}$ by applying (7) $j-1$ times gives $\rho_0(x,x_j;j\varepsilon)$. Integrating out $x_{j+1},\dots,x_{m-1}$ by applying (7) $m-j-1$ times gives $\rho_0(x_j,x';(m-j)\varepsilon)$. Hence the marginal density of $x_j$ under $P_m$ is
$$P_m^{(j)}(y)=\frac{\rho_0(x,y;t_j)\,\rho_0(y,x';\tau-t_j)}{\rho_0(x,x';\tau)}=p_{t_j}(y\,|\,x,x';\tau),\qquad t_j=j\varepsilon=\frac{j\tau}m.\tag{16}$$
This is the bridge marginal (3) at time $t_j$: a Gaussian with mean $x+\tfrac jm(x'-x)$ and per-component variance $2D\,t_j(\tau-t_j)/\tau=2D\tau\,j(m-j)/m^2$. Therefore $\mathbb E_{P_m}V(x_j)=\langle V\rangle_{t_j}\in(-\infty,\infty]$. For $j=m$ the endpoint is fixed, $x_m=x'$, and $\mathbb E V(x_m)=V(x')=:\langle V\rangle_\tau$, consistent with (9) at $u=\tau$. `[N]` N2 tests (16) by weighted free random walks.

Step T5 `[D]`, Jensen at finite $m$. Since $X_m\ge-m\varepsilon c=-c\tau$, Lemma J with $\mu=P_m$ and linearity of the expectation for random variables bounded below give
$$T_m(x,x')\ \ge\ \rho_0(x,x';\tau)\,\exp\Big(-\varepsilon\sum_{j=1}^m\langle V\rangle_{t_j}(x,x')\Big).\tag{17}$$
(17) uses only [A2]. `[N]` N3 tests (17) directly on a grid, for $m=2,\dots,16$, for a cosine potential and for the oscillator.

Step T6 `[D]`, the limit $m\to\infty$, under [A3]. First, $u\mapsto\langle V\rangle_u$ is continuous on $[0,\tau]$. In (9) the integrand is continuous in $u$ for each $z$, because $V$, $m(u)$ and $\sigma_u$ are continuous and $\sigma_0=\sigma_\tau=0$. For domination: $|m(u)|\le R:=\max(|x|,|x'|)$ and $\sigma_u^2\le D\tau/2$. With $a=1/(4D\tau)$ in [A3], $V(m+\sigma z)\le C_a e^{a|m+\sigma z|^2}\le C_ae^{2aR^2}e^{2a\sigma^2|z|^2}\le C_ae^{2aR^2}e^{|z|^2/4}$, and $V\ge-c$. So the integrand is bounded by $(2\pi)^{-d/2}\big(c+C_ae^{2aR^2}e^{|z|^2/4}\big)e^{-|z|^2/2}$, which is integrable and independent of $u$. Dominated convergence (Rudin, 3rd ed., Thm 1.34, `[R]`) then gives continuity on $[0,\tau]$, with $\langle V\rangle_0=V(x)$ and $\langle V\rangle_\tau=V(x')$. The same bound holds uniformly for $(x,x')$ in compact sets, so $\Phi_\tau$ is continuous in $(x,x')$. The sum $\varepsilon\sum_{j=1}^m\langle V\rangle_{j\varepsilon}$ is a right-endpoint Riemann sum of a continuous function on $[0,\tau]$, so it converges to $\Phi_\tau(x,x')$.

Strong convergence (13) does not by itself give pointwise convergence of kernels, so I pass to the limit in integrated form. For $f,g\in C_c(\mathbb R^d)$ with $f,g\ge0$, (17) gives
$$\langle f,T_mg\rangle=\iint f(x)\,T_m(x,x')\,g(x')\ \ge\ \iint f(x)g(x')\,\rho_0(x,x';\tau)\,e^{-\varepsilon\sum_j\langle V\rangle_{t_j}(x,x')}.$$
As $m\to\infty$ the left side tends to $\langle f,e^{-\tau H}g\rangle=\iint f\,K_\tau\,g$, since strong convergence implies weak convergence. The right side tends to $\iint fg\,R_\tau$ by dominated convergence: the integrand converges pointwise and is bounded by $f(x)g(x')(4\pi D\tau)^{-d/2}e^{c\tau}$. Hence $\iint f(x)g(x')\,[K_\tau-R_\tau](x,x')\ge0$ for all such $f,g$.

`[V]` $K_\tau$ is jointly continuous whenever $V_-$ is in the Kato class and $V_+$ in the local Kato class (Bodmann, Leschke & Warzel, arXiv:quant-ph/9703031, §1.4). A bounded $V_-$ and a locally bounded $V_+$ qualify. `[D]` $R_\tau$ is continuous by the paragraph above. If $K_\tau-R_\tau$ were negative at some point $(x_0,x_0')$, continuity would make it smaller than some $-\eta<0$ on a product of balls around $(x_0,x_0')$; nonnegative $f,g$ supported in those balls would then contradict the integrated inequality. Therefore
$$K_\tau(x,x')\ \ge\ \rho_0(x,x';\tau)\,\exp\Big(-\int_0^\tau du\,\langle V\rangle_u(x,x')\Big)\qquad\text{for all }x,x',\ \tau>0.\tag{18}$$
This is $(\ast)$.

Remark `[?]`. The finite-$m$ inequality (17) needs no growth condition; only T6 uses [A3]. Within this route [A3] could plausibly be removed by truncating $V_N=\min(V,N)$ and invoking the monotone convergence theorem for increasing forms (Simon, J. Funct. Anal. 28, 377 (1978); seen only as a bibliography entry in a retrieved paper, content not retrieved). I have not carried this out.

### 3.3 Part (a), second derivation: Feynman–Kac

Step F1 `[V]`. Simon, arXiv:math-ph/9907022, Thm 1.1 with eqs. (1.1)–(1.2): let $V$ be continuous on $\mathbb R^\nu$ and bounded below, and $H=H_0+V$ with $H_0=-\tfrac12\Delta$. Then for $t>0$ and $\varphi,\psi\in L^2$,
$\langle\varphi,e^{-tH}\psi\rangle=\iint\overline{\varphi(x)}\psi(y)\,e^{-tH_0}(x,y)\,Q(x,y;V,t)$, where
$Q=\mathbb E\exp\!\big(-\int_0^tV((1-\tfrac st)x+\tfrac sty+\sqrt t\,\alpha(\tfrac st))ds\big)$,
$\alpha$ is the standard bridge with $\mathbb E\alpha_i(t)\alpha_j(s)=\delta_{ij}\min(t,s)[1-\max(t,s)]$, and $e^{-tH_0}(x,y)=(2\pi t)^{-\nu/2}e^{-|x-y|^2/2t}$.

Step F2 `[D]`, general $D$ by dilation. Define the unitary $(Uf)(z):=(2D)^{d/4}f(\sqrt{2D}\,z)$. For $f(x)=(2D)^{-d/4}g(x/\sqrt{2D})$ one has $-D\nabla_x^2f(x)=-D\,(2D)^{-1}(2D)^{-d/4}(\Delta g)(x/\sqrt{2D})=-\tfrac12(2D)^{-d/4}(\Delta g)(x/\sqrt{2D})$. Hence $UKU^{-1}=-\tfrac12\Delta$, while $UVU^{-1}$ is multiplication by $\tilde V(z)=V(\sqrt{2D}z)$, which is continuous and bounded below. Kernels transform as $K_\tau(x,x')=(2D)^{-d/2}\tilde K_\tau(x/\sqrt{2D},x'/\sqrt{2D})$. In F1 the free factor becomes $(2D)^{-d/2}(2\pi\tau)^{-d/2}e^{-|x-x'|^2/(2\cdot 2D\tau)}=\rho_0(x,x';\tau)$, and $Q$ becomes $\mathbb E\,e^{-S[\omega]}$ with
$$\omega(s)=(1-\tfrac s\tau)x+\tfrac s\tau x'+\sqrt{2D\tau}\,\alpha(s/\tau).$$
The process $\omega$ is Gaussian with mean $m(s)$ from (5) and covariance $2D\tau\cdot\frac s\tau(1-\frac{s'}\tau)=2Ds(\tau-s')/\tau$ for $s\le s'$, which is (8). So $\omega$ is the bridge of §3.1 and its one-time law is $p_s$ of (5). Thus
$$\langle f,e^{-\tau H}g\rangle=\iint\overline{f(x)}\,g(x')\;\rho_0(x,x';\tau)\;\mathbb E^{x,x';\tau}\big[e^{-S[\omega]}\big],\qquad S[\omega]=\int_0^\tau V(\omega(s))\,ds.\tag{19}$$

Step F3 `[D]`, Jensen and Tonelli. For every continuous path, $s\mapsto V(\omega(s))$ is continuous on $[0,\tau]$, so $S$ is finite and $S\ge-c\tau$. Lemma J gives $\mathbb E e^{-S}\ge e^{-\mathbb E S}$. The map $(s,\omega)\mapsto V(\omega(s))+c$ is nonnegative and jointly measurable (continuous in $s$, measurable in $\omega$), so Tonelli gives
$$\mathbb E[S]+c\tau=\mathbb E\int_0^\tau\big(V(\omega(s))+c\big)ds=\int_0^\tau\big(\mathbb E V(\omega(s))+c\big)ds=\int_0^\tau\big(\langle V\rangle_s+c\big)ds,\tag{20}$$
using that $\omega(s)$ has law $p_s$. Subtracting the finite constant $c\tau$ gives $\mathbb E S=\Phi_\tau(x,x')\in(-\infty,\infty]$. Inserting $\mathbb E e^{-S}\ge e^{-\Phi_\tau}$ into (19) with $f,g\ge0$ gives the integrated form of $(\ast)$, $\iint fg\,(K_\tau-R_\tau)\ge0$. No growth condition was used. Under [A3], $R_\tau$ is continuous (T6), and the argument at the end of T6 gives (18) at every point.

Without [A3] this route gives (18) for almost every $(x,x')$ (Lebesgue differentiation), and at every point where $\Phi_\tau$ is upper semicontinuous. Getting every point in full generality needs the pointwise Feynman–Kac representation of the kernel. Bodmann–Leschke–Warzel §1.4 state continuity of the kernel for Kato-class potentials, but the text I retrieved states pointwise validity of the bridge formula explicitly only for $-\gamma/|q|$. I mark this residual `[?]`. It concerns only potentials growing faster than every $e^{a|y|^2}$.

### 3.4 Where the positivity of $\rho_0$ is used

P1 (T2): Tonelli's theorem is used to assemble the kernel (14) of the $m$-fold product. This is a technical convenience.

P2 (T3–T5): this is the essential use. Because $\rho_0>0$, the normalized product $P_m$ of (15) is a probability density, and Lemma J applies to it. The proof of Lemma J integrates the pointwise inequality $e^{-X}\ge e^{-a}(1-(X-a))$ against $P_m$, and integration preserves a pointwise inequality only for a nonnegative measure. With a complex weight, such as the real-time kernel $(4\pi iDt)^{-d/2}e^{i|x-x'|^2/4Dt}$, or a sign-indefinite one, such as an antisymmetrized fermionic product, this step fails and no bound of the form $(\ast)$ follows.

P3 (T3): $\rho_0(x,x';\tau)>0$ strictly, so the normalization in (15) exists for every pair $(x,x')$, including widely separated ones.

P4 (F1–F3): the Feynman–Kac representation is an integral against a probability measure on paths. That measure exists because its finite-dimensional distributions, the normalized products (3) and (8), are nonnegative and consistent. This is the same positivity, hidden inside the construction.

P5 (§3.5.2): multiplying the slice inequalities requires $R_\tau\ge0$, again because $\rho_0>0$. The reality of $V$ enters alongside, through $e^{-\varepsilon V}>0$.

### 3.5 Part (b)

#### 3.5.1 The approximant

`[D]` Applying (18) to each of $m$ slices of length $\tau=\beta/m$ and closing the chain ($x_m\equiv x_0$) gives
$$\hat Z_m(\beta):=\int\prod_{j=0}^{m-1}d^dx_j\ \prod_{j=0}^{m-1}\rho_0(x_j,x_{j+1};\tau)\,\exp\!\Big(-\!\int_0^\tau\!du\ (2\pi\sigma_u^2)^{-d/2}\!\int d^dy\,e^{-|y-x_j-\frac u\tau(x_{j+1}-x_j)|^2/2\sigma_u^2}\,V(y)\Big),\quad \tau=\frac\beta m.\tag{21}$$

#### 3.5.2 The inequality $\hat Z_m\le\operatorname{Tr}e^{-\beta H}$

`[D]` with `[R]` inputs. Assume [A5]. Then $e^{-\beta H/2}$ is self-adjoint and Hilbert–Schmidt, with $\|e^{-\beta H/2}\|_{\rm HS}^2=\operatorname{Tr}e^{-\beta H}$. A Hilbert–Schmidt operator on $L^2$ has an $L^2$ kernel, with HS norm equal to the $L^2$ norm of the kernel (Reed–Simon I, Thm VI.23, `[R]`). So $\operatorname{Tr}e^{-\beta H}=\iint K_{\beta/2}(x,y)^2\,dx\,dy$. The kernel is real and symmetric ($H$ is self-adjoint and $V$ is real) and nonnegative (by (18)). Composing kernels by Tonelli then gives $\iint K_{\beta/2}(x,y)K_{\beta/2}(y,x)\,dy\,dx=\int K_\beta(x,x)\,dx$. Writing $e^{-\beta H}=(e^{-\tau H})^m$ and composing $m-1$ times (Tonelli again, since all factors are $\ge0$):
$$\operatorname{Tr}e^{-\beta H}=\int\prod_{j=0}^{m-1}d^dx_j\ \prod_{j=0}^{m-1}K_\tau(x_j,x_{j+1}),\qquad x_m\equiv x_0.\tag{22}$$
By (18), $K_\tau\ge R_\tau\ge0$ pointwise. For nonnegative numbers, $a_j\ge b_j\ge0$ implies $\prod a_j\ge\prod b_j$ (P5). Integrating,
$$\hat Z_m(\beta)\ \le\ \operatorname{Tr}e^{-\beta H}.\tag{23}$$
`[N]` N6 checks (23) for the oscillator at all tested $m$ and $\beta$.

#### 3.5.3 The trapezium rule

`[D]` By T6, $u\mapsto\langle V\rangle_u$ is continuous on $[0,\tau]$ with endpoint values $V(x)$ and $V(x')$. `[N]` S5 checks these limits symbolically for the oscillator. The two-point trapezium rule replaces $\Phi_\tau$ by $\frac\tau2[V(x)+V(x')]$. Since $(M_aTM_b)(x,x')=a(x)T(x,x')b(x')$ for multiplication operators $M_a,M_b$,
$$\rho_0(x,x';\tau)\,e^{-\frac\tau2V(x)}e^{-\frac\tau2V(x')}=\big\langle x\big|e^{-\tau V/2}e^{-\tau K}e^{-\tau V/2}\big|x'\big\rangle.\tag{24}$$
Hence the trapezium version of $\hat Z_m$ is $\operatorname{Tr}(e^{-\tau V/2}e^{-\tau K}e^{-\tau V/2})^m$, the primitive approximation. Jensen gives no inequality for it.

#### 3.5.4 Leading small-$\tau$ defect

Assume [A4]. Then $V$ is continuous, bounded below, and grows at most linearly, so [A3] holds. Both sides of (19) are continuous in $(x,x')$: the left by U5, the right by dominated convergence with the bound $e^{c\tau}$. Hence $K_\tau(x,x')=\rho_0\,\mathbb E^{x,x';\tau}e^{-S}$ pointwise. Define
$$\delta(x,x';\tau):=\ln K_\tau-\ln R_\tau=\ln\mathbb E\,e^{-S}+\mathbb E S=\ln\mathbb E\,e^{-Y},\qquad Y:=S-\mathbb E S.\tag{25}$$

`[D]` An exact representation. Put $F(\lambda)=\ln\mathbb E e^{-\lambda Y}$. Then $F(0)=0$, $F'(0)=-\mathbb E Y=0$, and $F''(\lambda)=\operatorname{Var}_\lambda Y\ge0$, the variance under the tilted measure $e^{-\lambda Y}d\mathbb P/\mathbb E e^{-\lambda Y}$. Taylor's formula with integral remainder gives
$$\delta=F(1)=\int_0^1(1-\lambda)\operatorname{Var}_\lambda(Y)\,d\lambda\ \ge0,\tag{25a}$$
which incidentally reproves $(\ast)$. `[?]` Differentiating under the expectation needs $\mathbb E e^{\theta|Y|}<\infty$ for some $\theta>1$. This is plausible under [A4], since $Y$ is then a Lipschitz functional of a Gaussian process, but I have not written out the tail bound. Expanding $\operatorname{Var}_\lambda$ in $\lambda$ gives the cumulant series $\delta=\tfrac12\kappa_2-\tfrac16\kappa_3+\tfrac1{24}\kappa_4-\dots$, which I use as an asymptotic expansion with the power counting below; its convergence is not claimed.

`[D]` Index convention (added in round 2, finding F1.1). In this subsection and in §4, the indices $i,j,k,l$ run over $1,\dots,d$, and a repeated index is summed. Write $V_i:=\partial_iV(\bar x)$, $V_{ij}:=\partial_i\partial_jV(\bar x)$, $V_{ijk}:=\partial_i\partial_j\partial_kV(\bar x)$, and similarly $V_{ijkl}$. Each of these is symmetric in its indices. The vector expressions of answer-1 translate as follows:
- $|\nabla V|^2=V_iV_i$;
- $|\mathsf H\Delta|^2=V_{ij}\Delta_j\,V_{ik}\Delta_k$;
- $\operatorname{tr}\mathsf H^2=V_{ij}V_{ij}$, the squared Frobenius norm of the Hessian, not $(\operatorname{tr}\mathsf H)^2=(\nabla^2V)^2$;
- $\nabla V\cdot\nabla(\nabla^2V)=V_iV_{ijj}$;
- the term queried in F1.1, $\nabla V\cdot\nabla^3V[\Delta,\Delta,\cdot\,]=V_iV_{ijk}\Delta_j\Delta_k=\sum_{i,j,k}\partial_iV\,\partial_i\partial_j\partial_kV\,\Delta_j\Delta_k$.

Because $V_{ijk}$ is fully symmetric, it does not matter which slot carries the gradient. The only real freedom is in pairing the free indices: the gradient is contracted with one slot and $\Delta$ with the other two. S9 (§4) tests these contractions in $d=2$, including two wrong readings, which fail.

`[D]` Decomposition. Write $\omega(u)=m(u)+\xi(u)$, where $\xi$ is the centred Gaussian of (8), $\bar x=(x+x')/2$, $\Delta=x'-x$, and $m(u)-\bar x=s(u)\Delta$ with $s(u)=u/\tau-\tfrac12$. Taylor's theorem at $\bar x$ with $h=s\Delta+\xi$ gives
$$V(\bar x+h)=V(\bar x)+V_ih_i+\tfrac12V_{ij}h_ih_j+\tfrac16V_{ijk}h_ih_jh_k+R_4,\qquad|R_4|\le\tfrac1{24}\,\sup_y\|\nabla^4V(y)\|\,|h|^4,$$
where $\|\nabla^4V\|$ is the norm of the fourth-derivative tensor as a multilinear form. Collecting terms by degree in $\xi$ and subtracting means:
$$Y=A_1+A_2+B+C_1+C_3+(\text{terms listed below}),$$
with
- $A_1=\int_0^\tau V_i\,\xi_i(u)\,du$,
- $A_2=\int_0^\tau s(u)\,V_{ij}\Delta_j\,\xi_i(u)\,du$,
- $B=\tfrac12\int_0^\tau\big(V_{ij}\,\xi_i(u)\xi_j(u)-\mathbb E[V_{ij}\xi_i\xi_j]\big)\,du$,
- $C_1=\tfrac12\int_0^\tau s(u)^2\,V_{ijk}\Delta_i\Delta_j\,\xi_k(u)\,du$,
- $C_3=\tfrac16\int_0^\tau V_{ijk}\,\xi_i\xi_j\xi_k(u)\,du$, which has mean zero by parity.

The remaining terms are $\tfrac12\int_0^\tau s(u)\big(V_{ijk}\Delta_i\xi_j\xi_k-\mathbb E[\cdot]\big)du$ and the quartic remainder.

Power counting: $\xi=O((D\tau)^{1/2})$, each $\int du=O(\tau)$, and $\Delta=O((D\tau)^{1/2})$, which is the regime asked for. Hence $A_1=O(\tau^{3/2})$, $A_2,B=O(\tau^2)$ and $C_1,C_3=O(\tau^{5/2})$; powers of $D$ are suppressed here and restored in the results. The Gaussian moments needed (Isserlis' theorem, written in components) are:
- $\mathbb E\,\xi_i(u)\xi_j(v)=\delta_{ij}C(u,v)$;
- $\operatorname{Cov}\big(\xi_i\xi_j(u),\xi_k\xi_l(v)\big)=(\delta_{ik}\delta_{jl}+\delta_{il}\delta_{jk})\,C(u,v)^2$;
- $\mathbb E\,\xi_l(u)\xi_i(v)\xi_j(v)\xi_k(v)=(\delta_{li}\delta_{jk}+\delta_{lj}\delta_{ik}+\delta_{lk}\delta_{ij})\,C(u,v)\,C(v,v)$.

The integrals needed are $I_1=\iint C=D\tau^3/6$, $I_2=\iint s(v)C(u,v)=0$, $I_3=\iint s(u)s(v)C=D\tau^3/360$, $I_4=\iint C^2=2D^2\tau^4/45$ and $I_5=\iint C(u,v)C(v,v)=D^2\tau^4/15$; all are `[N]` S4. With these:

$\operatorname{Var}A_1=V_iV_j\iint\delta_{ij}C(u,v)=V_iV_i\,I_1=V_iV_i\,D\tau^3/6$.

$\operatorname{Cov}(A_1,A_2)=V_i\,V_{kj}\Delta_j\iint s(v)\,\delta_{ik}C(u,v)=V_iV_{ij}\Delta_j\,I_2=0$. This is the would-be $O(\tau^{7/2})$ contribution. It vanishes because $s$ is odd about $\tau/2$, while $\int_0^\tau C(u,v)du=Dv(\tau-v)$ is even. That integral is computed as $\frac{2D}\tau[(\tau-v)\frac{v^2}2+v\frac{(\tau-v)^2}2]=Dv(\tau-v)$.

$\operatorname{Var}A_2=V_{ij}\Delta_j\,V_{kl}\Delta_l\iint s(u)s(v)\,\delta_{ik}C(u,v)=V_{ij}\Delta_j\,V_{ik}\Delta_k\,I_3=V_{ij}\Delta_j\,V_{ik}\Delta_k\,D\tau^3/360$.

$\operatorname{Var}B=\tfrac14V_{ij}V_{kl}\iint(\delta_{ik}\delta_{jl}+\delta_{il}\delta_{jk})C(u,v)^2=\tfrac14\cdot2\,V_{ij}V_{ij}\,I_4=V_{ij}V_{ij}\,D^2\tau^4/45$. The two terms are equal by the symmetry of $V_{kl}$.

$2\operatorname{Cov}(A_1,C_3)=2\cdot\tfrac16\,V_l\,V_{ijk}\iint(\delta_{li}\delta_{jk}+\delta_{lj}\delta_{ik}+\delta_{lk}\delta_{ij})\,C(u,v)C(v,v)=\tfrac13\cdot3\,V_lV_{ljj}\,I_5=V_iV_{ijj}\,D^2\tau^4/15$. The three terms are equal by the symmetry of $V_{ijk}$.

$2\operatorname{Cov}(A_1,C_1)=2\cdot\tfrac12\,V_l\,V_{ijk}\Delta_i\Delta_j\iint s(v)^2\,\delta_{lk}C(u,v)=V_kV_{ijk}\Delta_i\Delta_j\iint s(v)^2C(u,v)=V_iV_{ijk}\Delta_j\Delta_k\,D\tau^3/120$. The last step relabels $k\to i$, $i\to j$, $j\to k$, using symmetry. Here $\iint s(v)^2C=\int_0^\tau s(v)^2Dv(\tau-v)dv=D\tau^3\int_0^1(t-\tfrac12)^2t(1-t)dt$. With $w=t-\tfrac12$, $t(1-t)=\tfrac14-w^2$, and $2\int_0^{1/2}w^2(\tfrac14-w^2)dw=2(\tfrac1{96}-\tfrac1{160})=\tfrac1{120}$. This integral is not in S4; N8 and S9 test the resulting term.

$\operatorname{Cov}(A_1,B)=\operatorname{Cov}(A_2,B)=0$ by parity (odd Gaussian moments). Every remaining covariance is $O(\tau^{9/2})$ or smaller, or odd in $\Delta$. In particular, no fourth derivative enters through $O(\tau^4)$. The part of the quartic term linear in $\xi$ carries $\Delta^3$, giving $O(\tau^{9/2})$. Its part cubic in $\xi$ carries one $\Delta$ and $\iint s(v)C(u,v)C(v,v)=0$. Its part quartic in $\xi$ has zero covariance with $A_1$ by parity, and covariance $O(\tau^5)$ with $B$. S9 includes a random quartic term and confirms this.

The third cumulant starts at $\kappa_3=3\,\mathbb E[A_1^2B]+\dots$. By Isserlis and $\operatorname{Cov}(A_1,\xi_j(v))=V_j\,Dv(\tau-v)$, $\mathbb E[A_1^2B]=V_iV_{ij}V_j\int_0^\tau D^2v^2(\tau-v)^2dv=V_iV_{ij}V_j\,D^2\tau^5/30$, so $\kappa_3=O(\tau^5)$.

Putting these together, the leading behaviour asked for in (b) is
$$\delta(x,x';\tau)=\ln K_\tau(x,x')-\ln R_\tau(x,x')=\frac{D\tau^3}{12}\,\big|\nabla V(\bar x)\big|^2+O(D^2\tau^4),\qquad|x-x'|=O(\sqrt{D\tau}).\tag{26}$$
Its sign is that of $(\ast)$. For a linear potential, $Y=A_1$ is exactly Gaussian, so (26) holds with no remainder. `[N]` S8 confirms this exactly against the imaginary-time PDE. A linear potential is not bounded below, so it lies outside [A2]; there S8 is only a check of the local coefficient, applied to the explicit PDE solution (which is the kernel in the sense of Simon's Feynman–Kac formula for potentials with $V\ge-\epsilon|x|^2-C_\epsilon$, U1). More precisely, the variance through $O(\tau^4)$ is, with all derivatives at $\bar x$ and repeated indices summed,
$$\operatorname{Var}Y=\frac{D\tau^3}6V_iV_i+\frac{D\tau^3}{360}V_{ij}\Delta_j\,V_{ik}\Delta_k+\frac{D\tau^3}{120}V_iV_{ijk}\Delta_j\Delta_k+D^2\tau^4\Big[\frac{V_{ij}V_{ij}}{45}+\frac{V_iV_{ijj}}{15}\Big]+O(\tau^5),\tag{27}$$
and therefore
$$\delta=\frac{D\tau^3}{12}V_iV_i+\frac{D\tau^3}{720}V_{ij}\Delta_j\,V_{ik}\Delta_k+\frac{D\tau^3}{240}V_iV_{ijk}\Delta_j\Delta_k+D^2\tau^4\Big[\frac{V_{ij}V_{ij}}{90}+\frac{V_iV_{ijj}}{30}\Big]+O(\tau^5).\tag{28}$$
In $d=1$ at $\Delta=0$:
$$\delta(\bar x,\bar x;\tau)=\frac{D\tau^3}{12}V'^2+D^2\tau^4\Big(\frac{V''^2}{90}+\frac{V'V'''}{30}\Big)+O(\tau^5).\tag{29}$$
For the one-dimensional oscillator ($V_{ijk}=0$, $\mathsf H=\kappa$), (27) gives the variance exactly, and
$$\delta=\frac{\kappa^2D\tau^3\bar x^2}{12}+\frac{\kappa^2D\tau^3\Delta^2}{720}+\frac{\kappa^2D^2\tau^4}{90}+O(\tau^5).\tag{30}$$
`[N]` checks of these results:
- S7b/S7c confirm (30) against the exact (Mehler) kernel.
- N4b confirms the approach of $-\ln(R/K)$ to (26) and (30) on a grid.
- N5b confirms (26) and (29) for $V=\cos x$ against an independent DVR kernel.
- N8 confirms the $\Delta$-dependent terms of (28) for $V=\cos x$.
- S9 (round 2) confirms every index contraction of (27) in $d=2$. It computes $\operatorname{Var}S$ exactly for cubic-plus-quartic potentials with random rational coefficients and matches the $\tau^3$ and $\tau^4$ coefficients. The readings $(V_i\Delta_i)(V_{jkk}\Delta_j)$ in place of $V_iV_{ijk}\Delta_j\Delta_k$, and $(\operatorname{tr}\mathsf H)^2$ in place of $\operatorname{tr}\mathsf H^2$, are both rejected.

`[?]` The remainder in (26) is controlled by formal power counting, not by a proven uniform bound.

#### 3.5.5 Order of the error of $\hat Z_m$

`[D]` Using $K_\tau=R_\tau e^{\delta}$ in (22) and comparing with (21),
$$\hat Z_m=Z\;\mathbb E_{\rm ex}\Big[e^{-\sum_{j=0}^{m-1}\delta(x_j,x_{j+1};\tau)}\Big],\qquad \mathbb E_{\rm ex}:\ \text{density }\prod_jK_\tau(x_j,x_{j+1})/Z,\tag{31}$$
which is a probability density by (22) and the positivity of $K_\tau$. Since $\delta\ge0$ and $1-t\le e^{-t}\le1-t+t^2/2$ for $t\ge0$,
$$1-\frac{\hat Z_m}{Z}=\mathbb E_{\rm ex}\Big[\sum_j\delta_j\Big]-r,\qquad0\le r\le\tfrac12\mathbb E_{\rm ex}\Big[\big(\textstyle\sum_j\delta_j\big)^2\Big].\tag{32}$$
The exact bead measure is invariant under cyclic shifts, so every $j$ contributes equally. Integrating out $x_2,\dots,x_{m-1}$ by the semigroup property, the pair $(x_0,x_1)$ has density $K_\tau(x_0,x_1)K_{\beta-\tau}(x_1,x_0)/Z$, and $x_0$ alone has density $K_\beta(x_0,x_0)/Z$, the thermal density:
$$\mathbb E_{\rm ex}\Big[\sum_j\delta_j\Big]=m\,\mathbb E_{\rm ex}\,\delta(x_0,x_1;\tau),\qquad \mathbb E_{\rm ex}\,g(x_0)=\frac{\operatorname{Tr}(e^{-\beta H}g)}{Z}=\langle g\rangle_\beta.\tag{33}$$
Insert (26). Replacing $\bar x_{01}=x_0+\Delta/2$ by $x_0$ changes $|\nabla V|^2$ by $O(|\Delta|)$, whose mean under the exact pair measure is $O(\tau)$ because $\mathbb E[\Delta\,|\,x_0]=O(\tau)$. This gives
$$\mathbb E_{\rm ex}\,\delta(x_0,x_1;\tau)=\frac{D\tau^3}{12}\langle|\nabla V|^2\rangle_\beta+O(\tau^4).\tag{34}$$
`[?]` Here the $O(\tau^4)$ remainder of (26) must be integrable against the exact pair measure, including the exponentially rare pairs with $|\Delta|\gg\sqrt{D\tau}$; this is not proven. With $m\tau^3=\beta^3/m^2$, $m\tau^4=\beta^4/m^3$ and $r=O((m\tau^3)^2)$,
$$\frac{Z-\hat Z_m}{Z}=\frac{D\beta^3}{12\,m^2}\,\langle|\nabla V|^2\rangle_\beta+O(m^{-3}).\tag{35}$$
So the error of $\hat Z_m(\beta)$ at fixed $\beta$ is of order $1/m^2$, approached from below.

`[D]` Oscillator ($d=1$, $\omega_0=\sqrt{2D\kappa}$). From the diagonal of the Mehler kernel (50) below, $K_\beta(x,x)\propto\exp(-\frac{\omega_0}{2D}x^2\tanh\frac{\beta\omega_0}2)$, so $\langle x^2\rangle_\beta=\frac{D}{\omega_0}\coth\frac{\beta\omega_0}2$. Using $D^2\kappa^2=\omega_0^4/4$,
$$\frac{D\beta^3}{12}\langle|\nabla V|^2\rangle_\beta=\frac{D\beta^3\kappa^2}{12}\frac D{\omega_0}\coth\frac{\beta\omega_0}2=\frac{(\beta\omega_0)^3}{48}\coth\frac{\beta\omega_0}2=:A(\beta).\tag{36}$$
Since $\Phi_\tau$ is quadratic (12), $\hat Z_m$ is a Gaussian integral. The exponent is $\tfrac12x^{\mathsf T}\mathcal A x+m\kappa D\tau^2/6$, where $\mathcal A$ is circulant with diagonal $a=\frac1{D\tau}+\frac{2\kappa\tau}3$ and nearest-neighbour entry $b=-\frac1{2D\tau}+\frac{\kappa\tau}6$ (for $m=1,2$ the neighbour bonds coincide, and the eigenvalue formula below still holds). Its eigenvalues are $\lambda_k=a+2b\cos\theta_k=\frac{1-\cos\theta_k}{D\tau}+\frac{\kappa\tau}3(2+\cos\theta_k)$, with $\theta_k=2\pi k/m$. The Gaussian integral and the prefactor $(4\pi D\tau)^{-m/2}$ give
$$\hat Z_m=\prod_{k=0}^{m-1}\Big[4\sin^2\tfrac{\theta_k}2+\tfrac{2\kappa D\tau^2}3(2+\cos\theta_k)\Big]^{-1/2}e^{-m\kappa D\tau^2/6},\qquad Z=\frac1{2\sinh(\beta\omega_0/2)}.\tag{37}$$
`[N]` N6a cross-checks (37) against a direct grid evaluation of (21). N6b checks (23), and checks $m^2(1-\hat Z_m/Z)\to A(\beta)$.

### 3.6 Part (c): $V=-q^2/r$ in $d=3$

What is needed. The proof of (a) used $V\ge-c$ in four places: in Kato's product formula, which needs $V+c\ge0$; in Lemma J, which needs $X$ bounded below for $\mathbb EX$ to exist; in the domination bound $e^{c\tau}$ of T6; and in Simon's Feynman–Kac theorem (F1). So one needs: (i) a self-adjoint, bounded-below $H$ to which "$e^{-\tau H}$" refers; (ii) a regularized potential that satisfies the hypotheses of (a); (iii) convergence of the left side of $(\ast)$ when the regulator is removed; (iv) convergence of the right side, together with its finiteness, so that the limiting inequality is not vacuous; (v) continuity of both sides, for a pointwise statement.

(i) `[R]`. $1/r=r^{-1}\mathbf 1_{r<1}+r^{-1}\mathbf 1_{r\ge1}\in L^2(\mathbb R^3)+L^\infty(\mathbb R^3)$, because $\int_{r<1}r^{-2}d^3x=4\pi$. By Kato's theorem (Reed–Simon II, Thm X.15, `[R]`; corroborated by a retrieved paper quoting it), $H=K-q^2/r$ is self-adjoint on $D(K)=H^2(\mathbb R^3)$, and since the relative bound is $0$ it is bounded below, $H\ge-E_*$. The hydrogen value $E_*=q^4/4D$, i.e. $-Mq^4/2$ with $M=1/2D$, is `[R]` and not needed.
$$H=-D\nabla^2-q^2/r\ \ \text{self-adjoint on }H^2(\mathbb R^3),\quad H\ge-E_*.\tag{38}$$
(ii) `[D]`. Regularize by truncation:
$$V_N:=\max(-q^2/r,\,-N)=-\min(q^2/r,N),\qquad N=1,2,\dots\tag{39}$$
$V_N$ is continuous, $-N\le V_N\le0$, and $V_N\downarrow V$ pointwise on $r>0$ as $N\uparrow\infty$. By (18) with $c=N$, and [A3] holding trivially,
$$K^{(N)}_\tau(x,x')\ \ge\ \rho_0(x,x';\tau)\,e^{-\Phi^{(N)}_\tau(x,x')},\qquad\Phi^{(N)}_\tau=\int_0^\tau du\,\langle V_N\rangle_u.\tag{40}$$
(iii) `[D]` with `[R]` inputs, the left side. Put $H_N=K+V_N$, which is self-adjoint on $H^2$ (a bounded perturbation). For $\phi\in H^2$, $(H_N-H)\phi=(V_N-V)\phi=(q^2/r-N)_+\phi$, so
$$\|(H_N-H)\phi\|^2=\int\Big(\frac{q^2}r-N\Big)_+^2|\phi|^2\le\int_{r<q^2/N}\frac{q^4}{r^2}|\phi|^2\le q^4\|\phi\|_\infty^2\,4\pi\frac{q^2}N\to0.$$
This uses $\|\phi\|_\infty<\infty$ for $\phi\in H^2(\mathbb R^3)$ (Sobolev; Reed–Simon II, Thm IX.28, `[R]`, corroborated). $H^2$ is a common core, so $H_N\to H$ in the strong resolvent sense (Reed–Simon I, Thm VIII.25(a), `[R]`, corroborated). Because $V_N\ge V$, $H_N\ge H\ge-E_*$ in the form sense, so every spectrum lies in $[-E_*,\infty)$. The function $f(\lambda)=\exp(-\tau\max(\lambda,-E_*-1))$ is bounded and continuous on $\mathbb R$, with $f(H_N)=e^{-\tau H_N}$ and $f(H)=e^{-\tau H}$. Strong resolvent convergence gives $f(H_N)\to f(H)$ strongly (Reed–Simon I, Thm VIII.20(b), `[R]`, corroborated). Hence, for $f,g\in C_c$,
$$\langle f,e^{-\tau H_N}g\rangle\ \longrightarrow\ \langle f,e^{-\tau H}g\rangle.\tag{41}$$
(iv) `[D]`, the right side; the convergence theorem is the monotone convergence theorem (Rudin, 3rd ed., Thm 1.26, `[R]`, corroborated), applied three times. Its hypotheses are a sequence of nonnegative measurable functions, pointwise nondecreasing, with pointwise limit $f$; the conclusion is that the integrals converge to $\int f$ (possibly $+\infty$).
First application: on the probability space $(\mathbb R^3,p_u(y)d^3y)$ for fixed $u\in(0,\tau)$, the functions $-V_N=\min(q^2/r,N)$ are nonnegative, continuous, nondecreasing in $N$, and converge to $q^2/r$ off the null set $\{0\}$. So $\langle-V_N\rangle_u\uparrow q^2\langle1/r\rangle_u$.
Second application: on $((0,\tau),du)$, the functions $u\mapsto\langle-V_N\rangle_u$ are nonnegative, measurable and nondecreasing. So $-\Phi^{(N)}_\tau\uparrow q^2I(x,x';\tau)$, where $I:=\int_0^\tau\langle1/r\rangle_u\,du$.
Third application: on $\mathbb R^3\times\mathbb R^3$ with weight $f(x)g(x')\rho_0\ge0$, the functions $e^{-\Phi^{(N)}_\tau}$ are nonnegative and nondecreasing. So
$$\iint fg\,\rho_0\,e^{-\Phi^{(N)}_\tau}\ \uparrow\ \iint fg\,\rho_0\,e^{q^2I}.\tag{42}$$
Finiteness. `[D]` For $y\sim\mathcal N(\mu,\sigma^2\mathbf 1_3)$, use spherical coordinates with polar axis along $\mu$ ($\mu:=|\mu|$, $c=\cos\theta$):
$$\Big\langle\frac1{|y|}\Big\rangle=\frac{2\pi}{(2\pi\sigma^2)^{3/2}}\int_0^\infty r\,dr\int_{-1}^1dc\,e^{-(r^2+\mu^2-2r\mu c)/2\sigma^2}=\frac{2\pi}{(2\pi\sigma^2)^{3/2}}\frac{\sigma^2}{\mu}\int_0^\infty dr\Big[e^{-(r-\mu)^2/2\sigma^2}-e^{-(r+\mu)^2/2\sigma^2}\Big].\tag{43}$$
The bracket integrates to $\int_{-\mu}^{\mu}e^{-t^2/2\sigma^2}dt$. Hence
$$\Big\langle\frac1{|y|}\Big\rangle=\frac{1}{\mu\sqrt{2\pi\sigma^2}}\int_{-\mu}^{\mu}e^{-t^2/2\sigma^2}dt=\frac{\operatorname{erf}\big(\mu/\sqrt2\sigma\big)}{\mu},\qquad\xrightarrow{\ \mu\to0\ }\ \sqrt{\frac2\pi}\,\frac1\sigma.\tag{44}$$
Since $\operatorname{erf}(a)=\frac2{\sqrt\pi}\int_0^ae^{-t^2}dt\le\frac{2a}{\sqrt\pi}$,
$$\Big\langle\frac1{|y|}\Big\rangle\le\sqrt{\frac2\pi}\,\frac1\sigma,\qquad\text{with equality iff }\mu=0.\tag{45}$$
With $\sigma_u$ from (6), and $\int_0^\tau\frac{du}{\sqrt{u(\tau-u)}}=\pi$ (substitute $u=\tau\sin^2\vartheta$, $du=2\tau\sin\vartheta\cos\vartheta\,d\vartheta$):
$$I(x,x';\tau)=\int_0^\tau\frac{\operatorname{erf}\!\big(|m(u)|/\sqrt2\sigma_u\big)}{|m(u)|}\,du\ \le\ \sqrt{\frac2\pi}\sqrt{\frac\tau{2D}}\;\pi=\sqrt{\frac{\pi\tau}{D}},\qquad\text{equality iff }x=x'=0.\tag{46}$$
`[N]` N7a checks (44) by Monte Carlo and by two-dimensional quadrature; N7b checks (46); N7c checks the monotone convergence in (42) numerically.
(v) Continuity. `[V]` The Coulomb kernel is jointly continuous (Bodmann–Leschke–Warzel §1.4 state this for $-\gamma/|q|$, $d\ge2$). `[D]` $I(x,x';\tau)$ is continuous in $(x,x')$ by dominated convergence: the integrand of (46) is continuous in $(x,x')$ for each $u\in(0,\tau)$, since $\operatorname{erf}(a\mu)/\mu$ is continuous including $\mu=0$, and it is dominated by $\sqrt{2/\pi}/\sigma_u$, which is integrable in $u$. Combining (40), (41) and (42), and noting that (42) is finite with bound $e^{q^2\sqrt{\pi\tau/D}}\iint fg\rho_0$, we get $\iint fg\,(K_\tau-\rho_0e^{q^2I})\ge0$. The continuity argument of T6 then gives, for all $x,x'\in\mathbb R^3$ and $\tau>0$,
$$K_\tau(x,x')\ \ge\ \rho_0(x,x';\tau)\,\exp\Big(q^2\int_0^\tau du\,\frac{\operatorname{erf}\big(|m(u)|/\sqrt2\sigma_u\big)}{|m(u)|}\Big),\qquad K_\tau(0,0)\ge(4\pi D\tau)^{-3/2}e^{q^2\sqrt{\pi\tau/D}}.\tag{47}$$
An alternative route without the regulator applies Lemma J directly to the pointwise Feynman–Kac representation for $-\gamma/|q|$ (Bodmann–Leschke–Warzel §1.4), with $\mathbb E|S|=q^2I<\infty$. I prefer the regulator route because it uses only (a) plus standard operator convergence.

Contrast with the trapezium (primitive) version: there the slice factor is $e^{\frac\tau2q^2(1/|x|+1/|x'|)}$, and on the diagonal $\int_{|x|<1}d^3x\,e^{\tau q^2/|x|}=4\pi\int_0^1r^2e^{\tau q^2/r}dr=\infty$. The primitive approximant is therefore infinite for every $m$, whereas the averaged action (46) is bounded.

Does the error estimate of (b) apply? No, for three reasons.

1. Hypothesis [A4] fails at $r=0$. $V$ is not smooth there and $\nabla V$ is unbounded.
2. The coefficient in (35) is $q^4\langle r^{-4}\rangle_\beta=q^4\int\rho_\beta(x)|x|^{-4}d^3x$. It diverges whenever the density at the origin is positive, because $\int_0r^2\cdot r^{-4}dr=\infty$. Since $K_\beta(0,0)>0$, the density at the origin is positive for the Coulomb problem.
3. The expansion parameter of §3.5.4 is $\sqrt{D\tau}/|\bar x|$, which is not small for $|\bar x|\lesssim\sqrt{D\tau}$. There the defect scales differently: at $x=x'=0$, $m\equiv0$ and $\omega(s)=\sqrt{2D\tau}\,\alpha(s/\tau)$, so the substitution $s=\tau t$ gives $S=-q^2\sqrt{\tau/2D}\,X$ with $X:=\int_0^1dt/|\alpha(t)|$. As a consistency check, $\mathbb EX=\int_0^1\sqrt{2/\pi}\,\big(t(1-t)\big)^{-1/2}dt=\sqrt{2\pi}$, which reproduces the equality case of (46). Hence $\delta(0,0;\tau)$ is a function of $g=q^2\sqrt{\tau/2D}$ alone, and
$$\delta(0,0;\tau)=\ln\mathbb E\,e^{g(X-\mathbb EX)}=\frac{g^2}2\operatorname{Var}X+O(g^3)=\frac{q^4\tau}{4D}\operatorname{Var}X+O(\tau^{3/2}).\tag{48}$$
`[?]` This needs exponential moments of $X$; Khas'minskii's lemma for Kato-class potentials would supply them, `[R]`, not checked. So near the origin the defect is of order $\tau$, not $\tau^3$.

Moreover $\operatorname{Tr}e^{-\beta H}=\infty$ on $L^2(\mathbb R^3)$, because of the continuum and the infinitely many bound states (`[R]`). The trace-level statement (23) is therefore vacuous here, and the question is meaningful only for the local defect, or in a confined or many-body setting where the trace is finite.

Heuristic `[?]`, not derived. Use (26) for $|\bar x|\gg\sqrt{D\tau}$, i.e. $\delta\approx D\tau^3q^4/(12|\bar x|^4)$, which matches (48) in magnitude at $|\bar x|\sim\sqrt{D\tau}$. Integrate against a thermal density with $\rho_\beta(0)>0$: the outer region gives $\rho_\beta(0)\,\frac{D\tau^3q^4}{12}\,4\pi\int_{\sqrt{D\tau}}^\infty r^{-2}dr\sim\rho_\beta(0)q^4D^{1/2}\tau^{5/2}$, and the inner ball gives the same order, $\rho_\beta(0)(D\tau)^{3/2}\cdot q^4\tau/D$. Multiplying by $m=\beta/\tau$:
$$\frac{Z-\hat Z_m}{Z}\ \sim\ \rho_\beta(0)\,q^4D^{1/2}\beta^{5/2}\,m^{-3/2}\qquad\text{(heuristic, confined setting).}\tag{49}$$

### 3.7 Part (d): formulas used in the numerical test

`[D]`/`[N]` In $d=1$, with $\omega_0=\sqrt{2D\kappa}$, the exact oscillator kernel (Mehler) is
$$K^{\rm osc}_\tau(x,x')=\Big(\frac{\omega_0}{4\pi D\sinh\omega_0\tau}\Big)^{1/2}\exp\Big(-\frac{\omega_0\,[(x^2+x'^2)\cosh\omega_0\tau-2xx']}{4D\sinh\omega_0\tau}\Big).\tag{50}$$
It is not taken on trust: S6 verifies that it solves $\partial_\tau K=D\partial_x^2K-\tfrac\kappa2x^2K$ and that $\ln K-\ln\rho_0\to0$ as $\tau\to0$. The right side of $(\ast)$ is $R_\tau=\rho_0e^{-\Phi_\tau}$ with $\Phi_\tau$ from (12). For large $\tau$ at $x=x'=0$: $\ln R_\tau(0,0)=-\tfrac12\ln(4\pi D\tau)-\kappa D\tau^2/6$, and from (50), using $\sinh\omega_0\tau=\tfrac12e^{\omega_0\tau}(1-e^{-2\omega_0\tau})$, $\ln K_\tau(0,0)=\tfrac12\ln\frac{\omega_0}{2\pi D}-\frac{\omega_0\tau}2+O(e^{-2\omega_0\tau})$. Hence
$$\ln\frac{R_\tau(0,0)}{K_\tau(0,0)}=-\frac{\kappa D\tau^2}{6}+\frac{\omega_0\tau}{2}-\frac12\ln(2\omega_0\tau)+O(e^{-2\omega_0\tau}).\tag{51}$$
At large $\tau$ the bound therefore stays valid but becomes useless, with the ratio decaying like $e^{-\kappa D\tau^2/6}$. The reference bridge is free: its spread $\sigma_u^2\sim D\tau$ is not confined by $V$, so $\langle V\rangle_u$ grows linearly in $\tau$ and $\Phi_\tau$ quadratically, while $\ln K_\tau$ falls only linearly, at rate $\omega_0/2$.

## 4. Verification

### 4.1 Self-check battery

1. Dimensions. $[\rho_0]=L^{-d}$; $[\sigma_u^2]=[D\tau]=EL^2\cdot E^{-1}=L^2$; $\langle V\rangle_u$ is an energy, so $\Phi_\tau$ is dimensionless, and $R_\tau$ has the dimension of $\rho_0$. In (26), $[D\tau^3|\nabla V|^2]=EL^2\cdot E^{-3}\cdot E^2L^{-2}=1$. In (28)–(30), $[D\tau^3|\mathsf H\Delta|^2]=EL^2E^{-3}(EL^{-2})^2L^2=1$ $[D^2\tau^4\,V_{ij}V_{ij}]=E^2L^4E^{-4}E^2L^{-4}=1$, $[D\tau^3\,V_iV_{ijk}\Delta_j\Delta_k]=EL^2E^{-3}(EL^{-1})(EL^{-3})L^2=1$, and $[D^2\tau^4\,V_iV_{ijj}]=E^2L^4E^{-4}(EL^{-1})(EL^{-3})=1$. In (35), $[D\beta^3\langle|\nabla V|^2\rangle]=1$. In (12), $[\kappa\tau x^2]=EL^{-2}E^{-1}L^2=1$ and $[\kappa D\tau^2]=1$. In (46), $q^2$ has dimension $E\cdot L$ and $\sqrt{\tau/D}$ has dimension $(E\cdot L)^{-1}$, so $q^2\sqrt{\pi\tau/D}$ is dimensionless. In (48), $q^4\tau/D$ is dimensionless. In (49), $[\rho_\beta(0)q^4D^{1/2}\beta^{5/2}]=L^{-3}E^2L^2E^{1/2}LE^{-5/2}=1$. In (50)–(51), $\omega_0^2=2D\kappa$ is an energy squared. All pass.

2. Limiting cases. As $\tau\to0$: $R_\tau\to\rho_0\to\delta(x-x')$, and $\delta=O(\tau^3)$. As $\tau\to\infty$ (oscillator): $R/K\to0$ like $e^{-\kappa D\tau^2/6}$ (51), so the bound is valid and useless; N4 confirms (51) to 2e-5 at $\tau=5$ and to all printed digits at $\tau=10$. As $D\to0$ at fixed $\tau$, $\sigma_u\to0$, the bridge collapses onto the straight line, and $\delta\propto D\to0$: the bound becomes sharp in the classical limit. As $D\to\infty$, the expansion parameter $D\tau^3|\nabla V|^2$ grows and the bound degrades. As $V\to0$ or $V\to$ const: Lemma J holds with equality because $S$ is constant, so $(\ast)$ is an equality. As $q\to0$ in (47), the right side tends to $\rho_0$. As $N\to\infty$ in (39), the regulator removal is (41)–(42). As $m\to\infty$, $\hat Z_m\to Z$ as $1/m^2$ (35).

3. Reduction to known simpler cases. Constant $V$: equality. Linear $V=F\cdot x$: (26) is exact, and S8 verifies it against the PDE, with coefficient $1/24$ shown to fail. Oscillator: the Mehler kernel, S7b/S7c and N4. Cubic-plus-quartic polynomial potentials in $d=2$: $\operatorname{Var}S$ is exactly computable, and S9 matches (27) through $\tau^4$.

4. Symmetries. The interchange $x\leftrightarrow x'$ is respected: $\langle V\rangle_u(x,x')=\langle V\rangle_{\tau-u}(x',x)$ by (3), so $\Phi_\tau$ and $R_\tau$ are symmetric, and $\delta$ is even in $\Delta$, which (28) respects. Translation and rotation covariance: shifting or rotating $V$ transforms $\langle V\rangle_u$ the same way, because $p_u$ depends only on $y-m(u)$ and is isotropic. The cyclic symmetry of the bead chain is used in (33). For the oscillator, parity $x\to-x$ is respected by (12) and (30). Written in index form, every term of (27)–(28) is a full contraction of $V_i,V_{ij},V_{ijk},\Delta_i$, so it is invariant under rotations, as it must be; S9 tests this with non-diagonal Hessians and generic third-derivative tensors in $d=2$.

5. Signs. $\delta\ge0$ by (25a)/Lemma J, and the leading term of (26) is $\ge0$. $\hat Z_m\le Z$ (N6: all $m$, all $\beta$). For attractive Coulomb, the exponent in (47) is $+q^2I>0$ and enhances the kernel, as it must. The large-$\tau$ ratio is $<1$.

6. Order of magnitude. Take the H$_2$ vibration, $\hbar\omega_0\approx0.546$ eV (4401 cm$^{-1}$), at $T=300$ K ($k_BT=0.02585$ eV), so $\beta\omega_0\approx21.1$, treated as an oscillator. Then (36) gives $A\approx21.1^3/48\approx196$, and the relative error of $\hat Z_m$ is $\approx196/m^2$: 2% at $m=100$, 0.02% at $m=1000$. This is the familiar scale of bead numbers for stiff vibrations in path-integral work, so it is plausible.

7. Boundary and initial conditions. As $\tau\to0$, $R_\tau\to\delta(x-x')$. The bridge marginal tends to $\delta_x$ as $u\to0$ and to $\delta_{x'}$ as $u\to\tau$ (S5 limits; (9) at $\sigma=0$). The exact kernel used, Mehler, satisfies the PDE and the initial condition (S6).

8. Degenerate cases. At $u=0,\tau$ the variance vanishes, which is handled by the $z$-substitution (9). The division by $\rho_0(x,x';\tau)$ is by a strictly positive number for every pair. Limit–integral exchanges: T6 uses dominated convergence with an explicit dominating function; (14) and (22) use Tonelli on nonnegative integrands; (20) uses Tonelli after shifting by $c$; (42) uses monotone convergence with its hypotheses checked; the m→∞ limit of kernels goes through test functions, because strong operator convergence does not give pointwise kernel convergence. For Coulomb at $\mu=0$, $\operatorname{erf}(a)/a\to2/\sqrt\pi$ is continuous. The set $r=0$ is a null set. $\operatorname{Tr}e^{-\beta H}=\infty$ for Coulomb on $\mathbb R^3$, which makes (23) vacuous; this is stated. At points with $\nabla V(\bar x)=0$ the leading term (26) vanishes and $D^2\tau^4$ takes over; this is why N4b restricts relative comparisons to $|\bar x|\ge0.5$, and why the N5b points avoid zeros of $\sin\bar x$.

### 4.2 How the checks were run

The scripts are `check_symbolic.py` (sympy), `check_numeric.py` (numpy/scipy), `check_diagnostics.py` (follow-ups to run 1 of `check_numeric.py` in round 1), `check_extra.py` (N8) and, new in round 2, `check_tensor_d2.py` (S9, sympy). Versions: Python 3.13.18, sympy 1.14.0, numpy 2.5.3, scipy 1.18.1, mpmath 1.3.0. Seeds: numpy `default_rng(20261112)` in `check_numeric.py`; 20261113 and 20261114 in the diagnostics; `random.Random(20261113)` for the S9 parameters. Sympy's internal term ordering depends on Python's hash randomization (round-1 revision R5). The two sympy scripts were therefore run as `PYTHONHASHSEED=s python3 -P -s <script>` for $s=0,1,2,3$, and for each script the four outputs are byte-identical (verified with `cmp`). The numerical scripts were run as `python3 -I <script>`.

Round 2 reran all five scripts from a fresh directory. The four round-1 scripts are byte-identical to the versions delivered with answer-1 (verified with `cmp`); the only new code is `check_tensor_d2.py`. SHA-256 of the scripts as run:
```text
221339968e5f55f6912ddcf6e066ba431c3370edb72221dbad9432391730bc70  check_diagnostics.py
e6706eb40c87daf6572e49cbcd0bdb532e3fcfe6a96ec37b4ac397889d313c2e  check_extra.py
d0612c76a7e86b766cffbaa9a9e9e798053838872744b6a145ddd869bdf6f020  check_numeric.py
164f2cc57a9ca0fb538766d90110c18c701429d60b25fa1294ae7230984a16ba  check_symbolic.py
8bb6475abe4321f4da211c224fd4cecf88cb7662e6e16eb2a3d7c22b974a1f99  check_tensor_d2.py
```
Comparison with round 1, for the record only (the outputs pasted in §4.5 are the round-2 outputs). The round-2 outputs of `check_symbolic.py`, `check_diagnostics.py` and `check_extra.py` are byte-identical to the round-1 outputs. The round-2 output of `check_numeric.py` differs only in the script path printed in the two stderr warning lines (`/home/claude/checks/round2/...` instead of `/home/claude/checks/...`).

Frozen sections. Sections 3.1, 3.2, 3.3, 3.5.2, 3.5.3, 3.6 and 3.7 of this document were extracted programmatically and compared byte-for-byte with the same sections of answer-1. All seven are identical (§4.4, R9).

`[A]` Assumptions inside the code. These are all restated here, and none goes beyond the text. The sympy symbols declared positive are $D$ (given), $\kappa$ (the oscillator), the interval lengths $a,b,c,u,w,s,t$ (which are lengths of sub-intervals of $(0,\tau)$ or times $>0$), $e=\sqrt\tau$, and $d=\Delta/\sqrt\tau$. Declaring $d>0$ means $\Delta>0$; this loses no generality because $\delta$ is even in $\Delta$ (§4.1 item 4), and the S7 output contains only $d^2$. $x,x',y,X,F$ are declared real. In the numerics: a quadrature window of $\pm(14\sqrt{2D\tau}+1)$ around $[\min(x,x'),\max(x,x')]$ (N1); grid spacings and boxes as stated in the comments; a DVR grid with $h=0.04$ on $[-12,12]$. Each tolerance and each FAIL criterion is written in a comment before the corresponding check.

### 4.3 What each check tests, what it would catch, what it would not

S1 (marginal). Tests (5)–(6) against the definition (3), in one dimension, symbolically. Inputs: $\rho_0$ from the prompt, and the claimed formula. Would catch a wrong mean or variance, for example $Du(\tau-u)/\tau$ in place of $2Du(\tau-u)/\tau$. Would not catch anything about $d>1$ (factorization is argued in the text), nor whether (3) is the intended bridge ([A6]).

S2 (Chapman–Kolmogorov (7)). Would catch normalization errors in the bead measure. Would not catch anything beyond a Gaussian integral.

S3 (covariance (8), two-time means). Inputs: the kernel product (definition) and the claimed covariance. Would catch a missing $1/\tau$ or the wrong $\min/\max$ structure. Would not catch errors in laws at three or more times; those are Gaussian and fixed by (8).

S4 (covariance integrals $I_1$–$I_5$). Inputs: the claimed $C(u,v)$, checked in S3. Would catch arithmetic errors in $1/6$, $1/360$, $2/45$, $1/15$ and in the vanishing odd moment. Would not catch an error in which integrals are the right ones, i.e. in the Isserlis bookkeeping of §3.5.4; S7, S8, N4b, N5b, N8 and S9 address that independently. The integral $\int_0^1(t-\frac12)^2t(1-t)dt=1/120$ is not in S4; N8 and S9 test the term it produces.

S5 ((12) and the endpoint limits). Computes $\langle V\rangle_u$ for the oscillator from the definition (4) by symbolic integration, then integrates over $u$. Would catch errors in (12) and in the trapezium endpoint values. Would not catch anything about non-quadratic $V$ (see N1).

S6 (Mehler). Would catch a misremembered oscillator kernel. Would not catch failures of uniqueness: I take PDE plus initial condition plus positivity as determining the kernel (`[R]`, standard).

S7a/S7b/S7c ((30) against exact). Inputs: Mehler (S6) and (12) (S5); both are independent of the variance computation that produced (30). Would catch a wrong leading coefficient, or wrong $\Delta^2$ or $\tau^4$ coefficients for quadratic $V$. Would not catch the $\nabla^3V$ terms, which vanish for the oscillator, nor anything about non-quadratic $V$. S7a is the method that failed (R1); S7c is the 40-digit arbiter that decides between S7a and S7b.

S8 (linear potential). Would catch a wrong coefficient in (26); the $1/24$ alternative is shown to leave a residual. Would not catch Hessian or third-derivative terms (absent for linear $V$).

N1 ($\langle V\rangle_u$ closed forms against quadrature of (4), 150 random draws per potential, including $u/\tau=10^{-4}$ and $1-10^{-4}$). This is a numerical check of (5)–(6) and of the Gaussian-moment formulas, independent of S1. Would catch errors in either. Would not catch anything about $d>1$.

N2 (weighted free random walks). Tests (16), the marginal at bead time $t_j=j\tau/m$. Inputs: only $\rho_0$ (used as importance weight) and the definition of the bridge, not (5). Would catch a wrong bead time. For instance, $t_j=(j-\frac12)\varepsilon$ shifts the mean by $|\Delta|/2m\approx0.022$, which changes $\langle\cos2y\rangle$ by up to about 0.04, against standard errors of about 0.002. Would not catch anything about $d>1$ or the continuum limit.

N3 (finite-$m$ inequality (17) on a grid; quadrature converged, with h versus h/2 differences of order $3\times10^{-15}$). Would catch a violation of (17), such as from a mis-applied Jensen step or badly wrong bead marginals. Would not catch a valid but looser bound, which also passes. It does not test the $m\to\infty$ limit.

N4 ((18) against Mehler on a 121×121 grid at eight values of $\tau$ from 0.05 to 10). Would catch any violation of $(\ast)$ at grid points. Would not catch off-grid behaviour, nor a looser bound; N4b addresses the latter.

N4b (sharpness: $-\ln(R/K)$ against (26) and (30)). Would catch a wrong leading coefficient, e.g. $1/24$ would make $(-L)/P_1\to2$, and a wrong next order for the oscillator. Would not catch the $\nabla^3V$ terms.

N5 (DVR validation against $\rho_0$ and Mehler, to about $10^{-11}$). Would catch DVR errors, including a wrong kinetic matrix (the Colbert–Miller form is used from memory, `[R]`, and is validated here rather than trusted). Would not catch DVR errors specific to non-quadratic potentials. Spectral accuracy for smooth $V$ is the argument; validation on two different potentials is the evidence.

N5b (cosine, coefficients $a$ and $b$ at $\Delta=0$). Would catch errors in (26) and (29) for a non-quadratic potential, including the $V'V'''/30$ term. Would not catch the $\Delta$-dependent terms (N8).

N5c ((18) for the cosine at $\tau$ from 0.2 to 4). Would catch violations in the tested region. Would not catch anything off-grid.

N6a ((37) against a grid evaluation of (21)). Would catch algebra errors in (37). Would not catch errors in (12), which both evaluations use; (12) is checked by S5 and N1.

N6b ($\hat Z_m\le Z$; $m^2(1-\hat Z_m/Z)\to A$; three values of $\beta$; $m$ up to 2048). Would catch a wrong order in $1/m$, since $m^2(1-\hat Z/Z)$ would diverge or vanish, and a wrong coefficient in (35)–(36). Would not catch anything about non-Gaussian $V$. The `[?]` tail issue in (34) is benign for the oscillator.

N7a ((44) against Monte Carlo and two-dimensional numerical quadrature). Would catch errors in (44). Would not catch errors in the $u$-integration (N7b).

N7b ((46), including equality at the origin). Would catch errors in (45)–(46). Would not catch a failure of (47) itself: no exact Coulomb kernel was computed (open question).

N7c (monotone convergence (42) at the origin). Would catch non-monotonicity or a wrong limit. Would not catch problems in the operator convergence (41).

N8 ($\Delta$-dependent $\tau^4$ terms of (28), cosine, $\Delta=2\sqrt\tau$). Would catch errors in the coefficients $1/720$ and $1/240$. It discriminates: without the $\Delta$ terms the predicted $b$ is half the fitted one. Would not catch the $d>1$ tensor structure of (28); S9 covers that for (27).

S9 (round 2; index contractions of (27) in $d=2$; `check_tensor_d2.py`). For a polynomial potential, $\operatorname{Var}S=2\int_0^\tau du\int_0^u dv\,\operatorname{Cov}(V(h(u)),V(h(v)))$, with $h=s\Delta+\xi$, is a finite sum of Gaussian moments, and the script computes it exactly. The potential is its own Taylor polynomial at $\bar x$, with random rational $V_i$, $V_{ij}$, $V_{ijk}$ and $V_{ijkl}$; three parameter sets are used, with $\tau=e^2$ and $\Delta=e\,\mathbf d$. Gaussian moments are computed by Stein's identity, `[D]`: the centred Gaussian density satisfies $\partial_j\varphi_\Sigma(x)=-(\Sigma^{-1}x)_j\varphi_\Sigma(x)$, so $x_i\varphi_\Sigma=-\Sigma_{ij}\partial_j\varphi_\Sigma$, and integrating by parts against a polynomial $f$ gives $\mathbb E[x_if(X)]=\Sigma_{ij}\mathbb E[\partial_jf(X)]$. The routine is self-tested against six textbook moments.
- Inputs: the covariance (8) (checked in S3), $m(u)$ from (5), the definition of $\operatorname{Var}S$, and Stein's identity. It uses none of $I_1$–$I_5$ and none of the hand contractions of §3.5.4. This makes it independent of the bookkeeping it tests.
- Would catch: any wrong index contraction or coefficient in (27) through $O(\tau^4)$; a spurious fourth-derivative term (the potential includes a random quartic part); nonzero odd or lower-order coefficients. It discriminates: in all three runs, the two alternative readings named in §3.5.4 leave nonzero residuals.
- Would not catch: the step from $\operatorname{Var}Y$ to $\delta$ (the factor $\tfrac12$ and $\kappa_3=O(\tau^5)$), which S7, S8, N4b, N5b and N8 test. It also would not catch anything specific to $d\ge3$. The contractions in (27) are dimension-independent expressions, but only $d=2$ is computed. Nor would it catch non-polynomial behaviour, or the `[?]` remainder bound.
- Limitation of the parameter draws: in runs 1 and 2 the random $\mathbf d$ happened to lie along a coordinate axis; run 0 has a generic direction. Off-diagonal Hessian and mixed third derivatives are nonzero in all three runs.

D1–D3 (diagnostics). These quantify the run-1 roundoff in N7b, locate the NaN warning of N5c, and repeat N2 with independent seeds and five times more paths.

### 4.4 Revision log: every failure and every change

Round 1. The full record, including the verbatim code and output of every round-1 run and the crash fragments, is in answer-1 §4.4–4.5. The corrector prompt asks for fresh output only, so here I summarize it in one line per item and do not paste it again.

R1. S7 failed in run 1 because sympy expanded `series(log(K/RHS).rewrite(exp))` wrongly. A 40-digit direct evaluation decided between the methods. The check was changed (S7a kept, S7b and S7c added); the derivation was not. S7a is still in the script and still prints FAIL in §4.5.1. That line is the retained record of the faulty method, not a failure of the derivation.

R2. Two roundoff defects in `check_numeric.py` were fixed: cancellation in $\tau-u$ (N7b) and in $1-\cos\theta$ (N6). The check was changed; the derivation was not.

R3. In run 1, N2 had $\max|z|=3.19$. D3 repeats it with two independent seeds and five times more paths, giving $\max|z|=2.23$ and $1.31$. No change.

R4. The N5c `RuntimeWarning` comes from DVR entries outside the tested region (D2). No change.

R5. Sympy's output depended on the hash seed. The S6 limit was changed to split logs, S7a was wrapped in `try`, and the seed was pinned. The derivation was not changed.

R6. N8 was added after I derived (28).

R7. S7b's $\tau^5$ coefficient matches $-\kappa_3/6$. This was observed post hoc, so it is consistency, not prediction.

Round 2.

R8, a new check, in response to F1.1. I wrote S9 (`check_tensor_d2.py`) to test the index contractions of (27) in $d=2$, where they are not reducible to one-dimensional products. It passed on its first run. That run was made before the round-2 rerun and its output is byte-identical to the rerun output in §4.5.5.

R9, the frozen sections. I extracted sections 3.1, 3.2, 3.3, 3.5.2, 3.5.3, 3.6 and 3.7 of answer-2 and answer-1 programmatically and compared them byte-for-byte. All seven are identical.

R10, what changed in the text. Changes in non-frozen sections:
- the header;
- two new rows in the symbol table (§2.2);
- §3.5.4: the decomposition, the covariance computations, (27) and (28) are rewritten in index notation, with an explicit dictionary to the vector notation of answer-1;
- §3.5.4: the symmetrization shorthand $3\,\delta_{a(b}\delta_{cd)}$ is replaced by the explicit three-term Isserlis sum;
- §3.5.4: one paragraph now argues explicitly that no fourth derivative enters through $O(\tau^4)$; in answer-1 this was folded into "every remaining covariance is $O(\tau^{9/2})$";
- §3.5.4: references to S9 are added;
- §4, §6, §7, §8 and §9 are updated, and "Response to audit 1" is added.

No coefficient, sign, power or equation number changed. No check was modified in round 2.

R11, the reruns. All five scripts were rerun from a fresh directory (§4.2). Every check passes except S7a, the retained faulty method (R1), which fails exactly as in round 1.

### 4.5 Code and output, verbatim (round 2)

#### 4.5.1 `check_symbolic.py`

```python
# check_symbolic.py -- P003.S02, symbolic checks [N].
# Standalone. Run: python3 check_symbolic.py
# Tested with: Python 3.13.18, sympy 1.14.0, mpmath 1.3.0.  No randomness, but sympy's
# internal term ordering depends on Python hash randomization: run as
#   PYTHONHASHSEED=0 python3 -P -s check_symbolic.py   (also run with seeds 1,2,3; see text)
#
# Symbol assumptions used below (each is stated as [A] in the text):
#   D > 0 (given in the problem), time intervals a, b, c, u, w > 0
#   (they are the lengths u, tau-u, ... of sub-intervals of (0, tau)),
#   kappa > 0 (oscillator), x, x', y real.
# No simplify call below relies on any other assumption.
import sympy as sp

print("sympy", sp.__version__)

D, kap = sp.symbols('D kappa', positive=True)
a, b, c, u, w = sp.symbols('a b c u w', positive=True)
x, xp, y, y1, y2, X, Dl = sp.symbols('x xp y y1 y2 X Delta', real=True)


def rho0(p, q, t):
    """1D free kernel, prompt section 3a, d = 1."""
    return (4*sp.pi*D*t)**sp.Rational(-1, 2)*sp.exp(-(p - q)**2/(4*D*t))


def report(name, expr):
    e = sp.simplify(expr)
    print(f"{name}: residual = {e}   ->", "PASS" if e == 0 else "FAIL")


# ---------------------------------------------------------------- S1
# Bridge marginal at time u (tau = u + w): product of free kernels divided
# by rho0(x,x';tau), compared with the claimed Gaussian N(m_u, s2_u),
# m_u = (x w + x' u)/tau, s2_u = 2 D u w / tau   (eqs. (5)-(6) of the text).
tau = u + w
lhs = rho0(x, y, u)*rho0(y, xp, w)/rho0(x, xp, tau)
m_u = (x*w + xp*u)/tau
s2_u = 2*D*u*w/tau
gauss = (2*sp.pi*s2_u)**sp.Rational(-1, 2)*sp.exp(-(y - m_u)**2/(2*s2_u))
report("S1 log(marginal) - log(claimed Gaussian)",
       sp.expand_log(sp.log(lhs), force=True) - sp.expand_log(sp.log(gauss), force=True))

# ---------------------------------------------------------------- S2
# Chapman-Kolmogorov: int dy rho0(x,y;u) rho0(y,x';w) = rho0(x,x';u+w).
ck = sp.integrate(rho0(x, y, u)*rho0(y, xp, w), (y, -sp.oo, sp.oo))
report("S2 Chapman-Kolmogorov ratio - 1", sp.simplify(ck/rho0(x, xp, u + w)) - 1)

# ---------------------------------------------------------------- S3
# Two-time joint density of the bridge at times u1 = a, u2 = a+b, tau = a+b+c,
# from the product of three free kernels (definition). Its exponent is a
# quadratic form in (y1, y2); read off the precision matrix, invert, compare
# with the claimed covariance 2D[min(u,v) - u v/tau]   (eq. (8) of the text).
expo = -(y1 - x)**2/(4*D*a) - (y2 - y1)**2/(4*D*b) - (xp - y2)**2/(4*D*c)
P = sp.Matrix(2, 2, lambda i, j: -sp.diff(expo, [y1, y2][i], [y1, y2][j]))
Cov = sp.simplify(P.inv())
T = a + b + c
u1, u2 = a, a + b
claimed = sp.Matrix([[2*D*(u1 - u1*u1/T), 2*D*(u1 - u1*u2/T)],
                     [2*D*(u1 - u1*u2/T), 2*D*(u2 - u2*u2/T)]])
for i in range(2):
    for j in range(2):
        report(f"S3 Cov[{i}{j}] - claimed", Cov[i, j] - claimed[i, j])
# mean of the joint density: stationary point of expo
sol = sp.solve([sp.diff(expo, y1), sp.diff(expo, y2)], [y1, y2], dict=True)[0]
report("S3 mean(y1) - m(u1)", sol[y1] - (x*(T - u1) + xp*u1)/T)
report("S3 mean(y2) - m(u2)", sol[y2] - (x*(T - u2) + xp*u2)/T)

# ---------------------------------------------------------------- S4
# Covariance integrals used in part (b). C(u,v) = 2D min(u,v)(tau-max)/tau.
# Integrate over the triangle v<u and double (C symmetric).
t = sp.symbols('t', positive=True)   # t = tau
U, V_ = sp.symbols('U V', positive=True)
Clow = 2*D*V_*(t - U)/t              # C(U,V) for V < U
def dbl(f_low):
    return sp.simplify(2*sp.integrate(sp.integrate(f_low, (V_, 0, U)), (U, 0, t)))
I1 = dbl(Clow)
I2 = sp.simplify(sp.integrate(sp.integrate(Clow*(U/t - sp.Rational(1, 2)), (V_, 0, U)), (U, 0, t))
                 + sp.integrate(sp.integrate(Clow*(V_/t - sp.Rational(1, 2)), (V_, 0, U)), (U, 0, t)))
I3 = dbl(Clow*(U/t - sp.Rational(1, 2))*(V_/t - sp.Rational(1, 2)))
I4 = dbl(Clow**2)
# int int C(u,v) C(v,v) du dv  (not symmetric: do it directly)
Cfull = lambda p, q: 2*D*sp.Min(p, q)*(t - sp.Max(p, q))/t
I5 = sp.simplify(sp.integrate(sp.integrate(2*D*U*(t - V_)/t*2*D*V_*(t - V_)/t, (U, 0, V_))
                              + sp.integrate(2*D*V_*(t - U)/t*2*D*V_*(t - V_)/t, (U, V_, t)), (V_, 0, t)))
report("S4 I1 - D t^3/6", I1 - D*t**3/6)
report("S4 I2 (odd moment) - 0", I2)
report("S4 I3 - D t^3/360", I3 - D*t**3/360)
report("S4 I4 - 2 D^2 t^4/45", I4 - 2*D**2*t**4/45)
report("S4 I5 - D^2 t^4/15", I5 - D**2*t**4/15)

# ---------------------------------------------------------------- S5
# <V>_u for V = kappa y^2/2 from the DEFINITION (integral over y of the kernel
# product), then integrated over u in (0, tau). Compared with the claim
# int_0^tau <V>_u du = (kappa tau/6)(x^2 + x x' + x'^2) + kappa D tau^2/6.
avgV = sp.integrate(rho0(x, y, u)*kap*y**2/2*rho0(y, xp, w), (y, -sp.oo, sp.oo))/rho0(x, xp, u + w)
avgV = sp.simplify(avgV)
uu = sp.symbols('uu', positive=True)
avgV_u = sp.simplify(avgV.subs(w, t - u).subs(u, uu))
intV = sp.simplify(sp.integrate(avgV_u, (uu, 0, t)))
report("S5 int <V>_u du - claimed", intV - (kap*t/6*(x**2 + x*xp + xp**2) + kap*D*t**2/6))
# endpoint limits (trapezium identity, part (b))
report("S5 lim u->0 <V>_u - V(x)", sp.limit(avgV_u, uu, 0) - kap*x**2/2)
report("S5 lim u->tau <V>_u - V(x')", sp.limit(avgV_u, uu, t) - kap*xp**2/2)

# ---------------------------------------------------------------- S6
# Mehler kernel (oscillator H = -D d^2/dx^2 + kappa x^2/2, omega = sqrt(2 D kappa),
# M = 1/(2D)). Not taken on trust: check that it solves the imaginary-time
# equation  d_tau K = D K_xx - (kappa x^2/2) K  and that ln K - ln rho0 -> 0 as tau->0.
om = sp.sqrt(2*D*kap)
Mw = om/(2*D)
def K_mehler(p, q, s):
    return sp.sqrt(Mw/(2*sp.pi*sp.sinh(om*s)))*sp.exp(-Mw*((p**2 + q**2)*sp.cosh(om*s) - 2*p*q)/(2*sp.sinh(om*s)))
s = sp.symbols('s', positive=True)
Km = K_mehler(x, xp, s)
pde = sp.diff(Km, s) - (D*sp.diff(Km, x, 2) - kap*x**2/2*Km)
report("S6 Mehler PDE residual / K", sp.simplify((pde/Km).rewrite(sp.exp)))
# (run 3: the log is written as a sum of logs by hand -- the pattern
#  series(log(ratio).rewrite(exp)) is unreliable in sympy, see S7a)
logKm = sp.Rational(1, 2)*sp.log(Mw/(2*sp.pi)) - sp.Rational(1, 2)*sp.log(sp.sinh(om*s)) \
    - Mw*((x**2 + xp**2)*sp.cosh(om*s) - 2*x*xp)/(2*sp.sinh(om*s))
logr0 = -sp.Rational(1, 2)*sp.log(4*sp.pi*D*s) - (x - xp)**2/(4*D*s)
lead = sp.series(sp.expand(logKm - logr0), s, 0, 1).removeO()
report("S6 ln K - ln rho0 at O(s^0)", sp.simplify(lead))

# ---------------------------------------------------------------- S7
# ln K_exact - ln RHS(*) for the oscillator, x = X - Delta/2, x' = X + Delta/2,
# Delta = d sqrt(tau) (the scaling of part (b)). tau = e^2, expand in e.
# Prediction (from the general variance computation, text eq. (26), plus the
# quadratic-V extras, eq. (30)):
#   kappa^2 D tau^3 X^2/12 + kappa^2 D tau^3 Delta^2/720 + kappa^2 D^2 tau^4/90 + O(tau^5)
#
# REVISION NOTE (reported in the text): the first version of this check, kept
# below as S7a, applied sp.series to log(K/RHS).rewrite(exp) and FAILED. S7c
# shows by 40-digit direct evaluation that S7a's series is itself wrong (a sympy
# expansion problem), while S7b's series (log written as a sum of logs by hand)
# agrees with the unexpanded expression. The derivation was not changed.
e, dd = sp.symbols('e d', positive=True)
taue = e**2
xs, xps = X - dd*e/2, X + dd*e/2
pred = kap**2*D*taue**3*X**2/12 + kap**2*D*taue**3*(dd*e)**2/720 + kap**2*D**2*taue**4/90

# S7a: original version
RHS = rho0(xs, xps, taue)*sp.exp(-(kap*taue/6*(xs**2 + xs*xps + xps**2) + kap*D*taue**2/6))
diff_log = sp.log(K_mehler(xs, xps, taue)) - sp.log(RHS)
# (run 3 note: under some hash seeds sp.series below raises instead of returning a
#  wrong result, so it is wrapped; its outcome is reported either way)
try:
    serA = sp.expand(sp.simplify(sp.series(diff_log.rewrite(sp.exp), e, 0, 11).removeO()))
    residA = sp.expand(serA - pred)
    lowA = sum(residA.coeff(e, k)*e**k for k in range(0, 10))
    print("S7a series (original method):", sp.collect(serA, e))
    report("S7a residual through tau^4", lowA)
except Exception as exc:
    serA = None
    print("S7a original method raised:", type(exc).__name__, str(exc)[:80], " -> FAIL (method unusable)")

# S7b: logs split by hand: log K = (1/2)log(Mw/(2 pi)) - (1/2)log sinh - exponent
logK = sp.Rational(1, 2)*sp.log(Mw/(2*sp.pi)) - sp.Rational(1, 2)*sp.log(sp.sinh(om*taue)) \
    - Mw*((xs**2 + xps**2)*sp.cosh(om*taue) - 2*xs*xps)/(2*sp.sinh(om*taue))
logR = -sp.Rational(1, 2)*sp.log(4*sp.pi*D*taue) - (xs - xps)**2/(4*D*taue) \
    - (kap*taue/6*(xs**2 + xs*xps + xps**2) + kap*D*taue**2/6)
serB = sp.expand(sp.simplify(sp.series(sp.expand(logK - logR), e, 0, 11).removeO()))
residB = sp.expand(serB - pred)
lowB = sum(residB.coeff(e, k)*e**k for k in range(0, 10))
print("S7b series (split logs):", sp.collect(serB, e))
report("S7b residual through tau^4", lowB)
print("S7b first term beyond prediction (e^10 = tau^5):", sp.factor(residB.coeff(e, 10)))

# S7c: arbiter -- evaluate the UNEXPANDED difference ln K - ln R at 40 digits and
# compare with both truncated series. Parameter values are arbitrary rationals.
vals = {D: sp.Rational(1, 2), kap: 1, X: sp.Rational(7, 10), dd: sp.Rational(13, 10)}
print("S7c   tau      direct(40 digits)            seriesA                  seriesB")
for ee in [sp.Rational(1, 5), sp.Rational(1, 10), sp.Rational(1, 20)]:
    direct = sp.N((sp.log(K_mehler(xs, xps, taue)) - sp.log(RHS)).subs(vals).subs(e, ee), 40)
    a_ = sp.N(serA.subs(vals).subs(e, ee), 20) if serA is not None else sp.nan
    b_ = sp.N(serB.subs(vals).subs(e, ee), 20)
    relB = abs((b_ - direct)/direct)
    print(f"S7c  {float(ee**2):.4f}  {float(direct):.15e}  {float(a_):.6e}  {float(b_):.15e}  relerr(B)={float(relB):.2e}")

# ---------------------------------------------------------------- S8
# Added after run 2 (new check, nothing above changed). Reduction to a simpler
# known case: for V = F x (1D) the bridge action S - ES = F int xi du is exactly
# Gaussian, so the text predicts ln K - ln R = (1/2) Var S = D F^2 tau^3/12 EXACTLY
# (eq. (26) with no remainder). Test: build K := R * exp(D F^2 tau^3/12) with R from
# (*) (int <V>_u du computed here from the definition) and check that K solves
# d_tau K = D K_xx - F x K. A wrong coefficient (e.g. 1/24) leaves a residual.
F = sp.symbols('F', real=True)
avgL = sp.simplify(sp.integrate(rho0(x, y, u)*F*y*rho0(y, xp, w), (y, -sp.oo, sp.oo))/rho0(x, xp, u + w))
intL = sp.simplify(sp.integrate(avgL.subs(w, s - u).subs(u, uu), (uu, 0, s)))
print("S8 int <Fy>_u du from definition:", sp.factor(intL))
for coef in [sp.Rational(1, 12), sp.Rational(1, 24)]:
    Klin = rho0(x, xp, s)*sp.exp(-intL + coef*D*F**2*s**3)
    res = sp.simplify((sp.diff(Klin, s) - D*sp.diff(Klin, x, 2) + F*x*Klin)/Klin)
    print(f"S8 coefficient {coef}: PDE residual / K = {res}   ->", "PASS" if res == 0 else "nonzero")
```

Round-2 output with `PYTHONHASHSEED=0`. The outputs for seeds 1, 2 and 3 are byte-identical (`cmp`). The single FAIL line is S7a, the faulty series method kept on purpose (R1); S7c shows by direct 40-digit evaluation that S7a's series is wrong and S7b's is right.

```text
sympy 1.14.0
S1 log(marginal) - log(claimed Gaussian): residual = 0   -> PASS
S2 Chapman-Kolmogorov ratio - 1: residual = 0   -> PASS
S3 Cov[00] - claimed: residual = 0   -> PASS
S3 Cov[01] - claimed: residual = 0   -> PASS
S3 Cov[10] - claimed: residual = 0   -> PASS
S3 Cov[11] - claimed: residual = 0   -> PASS
S3 mean(y1) - m(u1): residual = 0   -> PASS
S3 mean(y2) - m(u2): residual = 0   -> PASS
S4 I1 - D t^3/6: residual = 0   -> PASS
S4 I2 (odd moment) - 0: residual = 0   -> PASS
S4 I3 - D t^3/360: residual = 0   -> PASS
S4 I4 - 2 D^2 t^4/45: residual = 0   -> PASS
S4 I5 - D^2 t^4/15: residual = 0   -> PASS
S5 int <V>_u du - claimed: residual = 0   -> PASS
S5 lim u->0 <V>_u - V(x): residual = 0   -> PASS
S5 lim u->tau <V>_u - V(x'): residual = 0   -> PASS
S6 Mehler PDE residual / K: residual = 0   -> PASS
S6 ln K - ln rho0 at O(s^0): residual = 0   -> PASS
S7a series (original method): X**2*e**2*kappa/2 + e**8*(D**2*kappa**2/90 + D*d**2*kappa**2/720)
S7a residual through tau^4: residual = X**2*e**2*kappa*(-D*e**4*kappa + 6)/12   -> FAIL
S7b series (split logs): -D**2*X**2*e**10*kappa**3/60 + D*X**2*e**6*kappa**2/12 + e**8*(D**2*kappa**2/90 + D*d**2*kappa**2/720)
S7b residual through tau^4: residual = 0   -> PASS
S7b first term beyond prediction (e^10 = tau^5): -D**2*X**2*kappa**3/60
S7c   tau      direct(40 digits)            seriesA                  seriesB
S7c  0.0400  1.316572352636598e-06  9.800010e-03  1.316573155555556e-06  relerr(B)=6.10e-07
S7c  0.0100  2.045597618664627e-08  2.450000e-03  2.045597638888889e-08  relerr(B)=9.89e-09
S7c  0.0025  3.191645683638742e-10  6.125000e-04  3.191645684136285e-10  relerr(B)=1.56e-10
S8 int <Fy>_u du from definition: F*s*(x + xp)/2
S8 coefficient 1/12: PDE residual / K = 0   -> PASS
S8 coefficient 1/24: PDE residual / K = -D*F**2*s**2/8   -> nonzero
```

#### 4.5.2 `check_numeric.py`

```python
# check_numeric.py -- P003.S02, numerical checks [N].
# Standalone. Run: python3 check_numeric.py
# Tested with: Python 3.13.18, numpy 2.5.3, scipy 1.18.1. Seed fixed below.
#
# Assumptions restated as [A] in the text: D > 0, tau > 0, kappa > 0; grids,
# windows and tolerances are stated at each check together with the output
# that would count as FAIL.
import numpy as np
import scipy
from scipy import integrate, special, linalg

print("numpy", np.__version__, "scipy", scipy.__version__)
SEED = 20261112
rng = np.random.default_rng(SEED)


# ---------------------------------------------------------------------------
# Building blocks taken from the PROBLEM STATEMENT only
def log_rho0(p, q, t, D, d=1):
    """log of the free kernel, prompt section 3a."""
    r2 = np.sum(np.atleast_1d((np.asarray(p) - np.asarray(q))**2), axis=0) if d > 1 else (p - q)**2
    return -0.5*d*np.log(4*np.pi*D*t) - r2/(4*D*t)


# Claimed closed forms (these are what is under test)
def bridge_mean_var(x, xp, u, tau, D):
    return x + (u/tau)*(xp - x), 2*D*u*(tau - u)/tau          # text eq. (5)


def avgV_closed(kind, x, xp, u, tau, D, par):
    m, s2 = bridge_mean_var(x, xp, u, tau, D)
    if kind == "quad":
        return 0.5*par*(m**2 + s2)
    if kind == "cos":
        V0, k = par
        return V0*np.cos(k*m)*np.exp(-0.5*k**2*s2)
    if kind == "quartic":
        return par*(m**4 + 6*m**2*s2 + 3*s2**2)
    raise ValueError


def Vfun(kind, y, par):
    if kind == "quad":
        return 0.5*par*y**2
    if kind == "cos":
        V0, k = par
        return V0*np.cos(k*y)
    if kind == "quartic":
        return par*y**4


def int_avgV_closed(kind, x, xp, tau, D, par, n=80):
    """int_0^tau <V>_u du by Gauss-Legendre on the closed form (smooth integrand)."""
    g, wts = np.polynomial.legendre.leggauss(n)
    tot = 0.0
    for gi, wi in zip(g, wts):
        tot = tot + wi*avgV_closed(kind, x, xp, 0.5*tau*(gi + 1), tau, D, par)
    return 0.5*tau*tot


def logK_mehler(x, xp, tau, D, kap):
    """Oscillator kernel; independently verified in check_symbolic.py (S6)."""
    om = np.sqrt(2*D*kap)
    Mw = om/(2*D)
    return 0.5*np.log(Mw/(2*np.pi*np.sinh(om*tau))) - Mw*((x**2 + xp**2)*np.cosh(om*tau) - 2*x*xp)/(2*np.sinh(om*tau))


def int_avgV_quad_closed(x, xp, tau, D, kap):
    """Closed form of int_0^tau <V>_u du for V = kap y^2/2 (eq. (12); S5 symbolic)."""
    return kap*tau/6*(x**2 + x*xp + xp**2) + kap*D*tau**2/6


# ===========================================================================
print("\n=== N1  <V>_u: quadrature from the definition vs closed form ===")
# Integrand from the definition: rho0(x,y;u) V(y) rho0(y,x';tau-u)/rho0(x,x';tau).
# Window: [min(x,x') - 14 sqrt(2 D tau) - 1, max(x,x') + same] (chosen from x,x',tau
# only, not from the claimed mean/variance). FAIL if max relative error > 1e-8
# or normalization error > 1e-10.
def avgV_quad(kind, x, xp, u, tau, D, par):
    L = 14*np.sqrt(2*D*tau) + 1
    lo, hi = min(x, xp) - L, max(x, xp) + L
    lr = log_rho0(x, xp, tau, D)
    f = lambda y: np.exp(log_rho0(x, y, u, D) + log_rho0(y, xp, tau - u, D) - lr)
    pts = [x, xp]
    num = integrate.quad(lambda y: f(y)*Vfun(kind, y, par), lo, hi, points=pts, limit=400, epsabs=0, epsrel=1e-13)[0]
    nor = integrate.quad(f, lo, hi, points=pts, limit=400, epsabs=0, epsrel=1e-13)[0]
    return num, nor


for kind, par in [("quad", 1.3), ("cos", (0.8, 2.1)), ("quartic", 0.7)]:
    maxrel, maxnorm = 0.0, 0.0
    n = 150
    for i in range(n):
        D = rng.uniform(0.2, 2.0)
        tau = 10**rng.uniform(-2, np.log10(5))
        frac = [1e-4, 1 - 1e-4, 0.5][i] if i < 3 else rng.uniform(0, 1)
        u = frac*tau
        x, xp = rng.uniform(-3, 3, size=2)
        num, nor = avgV_quad(kind, x, xp, u, tau, D, par)
        cl = avgV_closed(kind, x, xp, u, tau, D, par)
        scale = max(abs(cl), 1e-3*abs(Vfun(kind, 1.0, par)))  # guard vs zeros of cos
        maxrel = max(maxrel, abs(num - cl)/scale)
        maxnorm = max(maxnorm, abs(nor - 1))
    print(f"N1 {kind:8s} draws={n}  max rel err={maxrel:.2e}  max |norm-1|={maxnorm:.2e}  ->",
          "PASS" if (maxrel < 1e-8 and maxnorm < 1e-10) else "FAIL")


# ===========================================================================
print("\n=== N2  weighted free-walk Monte Carlo (definition of the bridge) ===")
# Free walks x_0 = x, increments N(0, 2 D delta); weight = rho0(x_{n-1}, x'; delta).
# Then E_bridge[f(x_j)] = sum w f(x_j) / sum w. This uses only rho0 and the
# definition of the bridge, not eq. (5). FAIL if any |z| > 4.
D, tau, x, xp = 0.5, 1.0, 0.3, -0.4
kind, par = "cos", (1.0, 2.0)
nsteps, npaths = 16, 400_000
delta = tau/nsteps
inc = rng.normal(0.0, np.sqrt(2*D*delta), size=(npaths, nsteps - 1))
paths = x + np.cumsum(inc, axis=1)                      # x_1 .. x_{n-1}
w = np.exp(log_rho0(paths[:, -1], xp, delta, D) - log_rho0(x, xp, tau, D) + 0.0)
W = w.sum()
zs = []
for j in range(1, nsteps):
    f = Vfun(kind, paths[:, j - 1], par)
    est = np.sum(w*f)/W
    se = np.sqrt(np.sum(w**2*(f - est)**2))/W
    cl = avgV_closed(kind, x, xp, j*delta, tau, D, par)
    zs.append((est - cl)/se)
print("N2 z-scores, j=1..15:", " ".join(f"{z:+.2f}" for z in zs))
print("N2 effective sample size:", f"{W**2/np.sum(w**2):.0f}", " max|z| =", f"{max(abs(z) for z in zs):.2f}", "->",
      "PASS" if max(abs(z) for z in zs) < 4 else "FAIL")


# ===========================================================================
print("\n=== N3  finite-m Trotter inequality (T6) on a grid ===")
# K_m(x_a,x_b) = (P^m)_{ab}/h, P_ij = h rho0(x_i,x_j;eps) exp(-eps V(x_j)), eps = tau/m
# (kernel of (e^{-eps K} e^{-eps V})^m by trapezoid quadrature of the bead integrals).
# R_m = rho0(x_a,x_b;tau) exp(-eps sum_{j=1}^m <V>_{j eps}), <V>_tau := V(x_b).
# Region tested: |x_a|,|x_b| <= 3 and |x_a - x_b| <= 2.5.
# Quadrature error estimated by repeating with h/2. FAIL if min log(K_m/R_m) < -10*(h vs h/2 discrepancy).
def trotter_check(kind, par, D, tau, m, h, Lbox=10.0):
    xg = np.arange(-Lbox, Lbox + h/2, h)
    eps = tau/m
    P = h*np.exp(log_rho0(xg[:, None], xg[None, :], eps, D) - eps*Vfun(kind, xg[None, :], par))
    Pm = np.linalg.matrix_power(P, m)
    sel = np.where(np.abs(xg) <= 3 + 1e-9)[0]
    XA, XB = np.meshgrid(xg[sel], xg[sel], indexing="ij")
    Km = Pm[np.ix_(sel, sel)]/h
    S = np.zeros_like(XA)
    for j in range(1, m):
        S += avgV_closed(kind, XA, XB, j*eps, tau, D, par)
    S += Vfun(kind, XB, par)
    logR = log_rho0(XA, XB, tau, D) - eps*S
    return np.log(Km) - logR, XA, XB          # 2D arrays on the |x|<=3 sub-grid


for kind, par in [("cos", (1.0, 2.0)), ("quad", 1.0)]:
    for m in [2, 4, 8, 16]:
        lr1, XA1, XB1 = trotter_check(kind, par, 0.5, 1.0, m, 0.05)
        lr2, XA2, XB2 = trotter_check(kind, par, 0.5, 1.0, m, 0.025)
        assert np.allclose(XA2[::2, ::2], XA1) and np.allclose(XB2[::2, ::2], XB1)
        mask1 = np.abs(XA1 - XB1) <= 2.5
        mask2 = np.abs(XA2 - XB2) <= 2.5
        disc = np.max(np.abs(lr1 - lr2[::2, ::2])[mask1])
        tol = max(10*disc, 1e-12)
        lr = lr2[mask2]
        print(f"N3 {kind:4s} m={m:2d}: min log(K_m/R_m)={lr.min():+.3e}  max={lr.max():.3e}  h-vs-h/2 disc={disc:.1e}  ->",
              "PASS" if lr.min() > -tol else "FAIL")


# ===========================================================================
print("\n=== N4  oscillator: (*) against the exact (Mehler) kernel ===")
# D = 1/2, kappa = 1 (omega = 1). L = log(R/K); (*) says L <= 0.
# FAIL if max L > 1e-12 (rounding allowance) on the grid x,x' in [-3,3]^2 (121x121).
D, kap = 0.5, 1.0
om = np.sqrt(2*D*kap)
xg = np.linspace(-3, 3, 121)
XA, XB = np.meshgrid(xg, xg, indexing="ij")
print(" tau     max L        min L         at x=x'=0: L        large-tau asympt.")
for tau in [0.05, 0.1, 0.2, 0.5, 1.0, 2.0, 5.0, 10.0]:
    logR = log_rho0(XA, XB, tau, D) - int_avgV_quad_closed(XA, XB, tau, D, kap)
    L = logR - logK_mehler(XA, XB, tau, D, kap)
    L00 = (log_rho0(0.0, 0.0, tau, D) - int_avgV_quad_closed(0.0, 0.0, tau, D, kap)) - logK_mehler(0.0, 0.0, tau, D, kap)
    asym = -kap*D*tau**2/6 + om*tau/2 - 0.5*np.log(2*om*tau)
    print(f" {tau:5.2f}  {L.max():+.3e}  {L.min():+.3e}  {L00:+.6e}  {asym:+.6e}  ->", "PASS" if L.max() <= 1e-12 else "FAIL")

print("\nN4b small tau: -L compared with the leading term of part (b), Dk^2 tau^3 xbar^2/12,")
print("    and with leading + next (eq. (30)); points with |x-x'| <= 2 sqrt(2 D tau), |xbar| >= 0.5")
for tau in [0.4, 0.2, 0.1, 0.05, 0.025]:
    logR = log_rho0(XA, XB, tau, D) - int_avgV_quad_closed(XA, XB, tau, D, kap)
    mL = -(logR - logK_mehler(XA, XB, tau, D, kap))
    xb, Dl = 0.5*(XA + XB), XB - XA
    sel = (np.abs(Dl) <= 2*np.sqrt(2*D*tau)) & (np.abs(xb) >= 0.5)
    P1 = kap**2*D*tau**3*xb**2/12
    P2 = P1 + kap**2*D*tau**3*Dl**2/720 + kap**2*D**2*tau**4/90
    r1 = np.max(np.abs(mL[sel]/P1[sel] - 1))
    r2 = np.max(np.abs(mL[sel]/P2[sel] - 1))
    print(f"   tau={tau:5.3f}  npts={sel.sum():5d}  max|(-L)/P1 - 1|={r1:.3e}  max|(-L)/P2 - 1|={r2:.3e}")
print("   at xbar = 1, Delta = 0:  -L/tau^3 ->", ", ".join(
    f"{(-(log_rho0(1.,1.,t,D)-int_avgV_quad_closed(1.,1.,t,D,kap)-logK_mehler(1.,1.,t,D,kap)))/t**3:.6f}" for t in [0.2, 0.1, 0.05, 0.025, 0.0125]),
    f"   prediction D k^2/12 = {kap**2*D/12:.6f}")


# ===========================================================================
print("\n=== N5  cosine potential, exact kernel by sinc-DVR diagonalization ===")
# V = V0 cos(k x), V0 = 1, k = 1, D = 1/2. Grid h = 0.04 on [-12, 12].
# DVR kinetic for -D d^2/dx^2: T_ii = D pi^2/(3h^2), T_ij = 2D(-1)^(i-j)/(h^2 (i-j)^2).
# The DVR is NOT trusted: it is validated first on V = 0 (against rho0) and on the
# oscillator (against Mehler). FAIL criteria: validation errors > 1e-10.
h, Lb, D = 0.04, 12.0, 0.5
xg = np.arange(-Lb, Lb + h/2, h)
N = len(xg)
idx = np.arange(N)
dif = idx[:, None] - idx[None, :]
with np.errstate(divide="ignore"):
    T = np.where(dif == 0, D*np.pi**2/(3*h**2), 2*D*(-1.0)**dif/(h**2*np.where(dif == 0, 1, dif)**2))


def dvr_kernel(Vdiag, taus):
    E, U = linalg.eigh(T + np.diag(Vdiag))
    return {t: (U*np.exp(-t*E))@U.T/h for t in taus}


taus = [0.025, 0.05, 0.1, 0.2, 0.4, 1.0, 2.0, 4.0]
cen = np.where(np.abs(xg) <= 4 + 1e-9)[0]
Kfree = dvr_kernel(np.zeros(N), taus)
Kosc = dvr_kernel(0.5*xg**2, taus)
for t in taus[:6]:
    XA, XB = np.meshgrid(xg[cen], xg[cen], indexing="ij")
    near = np.abs(XA - XB) <= 3*np.sqrt(2*D*t)
    e_free = np.max(np.abs(np.log(Kfree[t][np.ix_(cen, cen)][near]) - log_rho0(XA, XB, t, D)[near]))
    e_osc = np.max(np.abs(np.log(Kosc[t][np.ix_(cen, cen)][near]) - logK_mehler(XA, XB, t, D, 1.0)[near]))
    print(f"N5 validation tau={t:5.3f}: max|log K_dvr - log rho0|={e_free:.1e}   max|log K_dvr - log K_Mehler|={e_osc:.1e}  ->",
          "PASS" if max(e_free, e_osc) < 1e-10 else "FAIL")

V0, k = 1.0, 1.0
Kcos = dvr_kernel(V0*np.cos(k*xg), taus)
print("\nN5b small-tau coefficient at Delta = 0: y(tau) = log(K/R)/tau^3, fit y = a + b tau + c tau^2")
print("    predictions: a = D V'(xbar)^2/12, b = D^2 (V''^2/90 + V' V'''/30)   [eqs. (26), (29)]")
for xb in [0.4, 0.8, 1.2, 1.6, 2.0, 2.8]:
    i = int(round((xb + Lb)/h))
    assert abs(xg[i] - xb) < 1e-9
    ys = []
    small = [0.025, 0.05, 0.1, 0.2, 0.4]
    for t in small:
        logR = log_rho0(xb, xb, t, D) - int_avgV_closed("cos", xb, xb, t, D, (V0, k))
        ys.append((np.log(Kcos[t][i, i]) - logR)/t**3)
    cfit = np.polyfit(small, ys, 2)
    a_pred = D*(V0*k*np.sin(k*xb))**2/12
    b_pred = D**2*((V0*k**2*np.cos(k*xb))**2/90 + (-V0*k*np.sin(k*xb))*(V0*k**3*np.sin(k*xb))/30)
    print(f"   xbar={xb:3.1f}: a_fit={cfit[2]:+.6e} a_pred={a_pred:+.6e} | b_fit={cfit[1]:+.5e} b_pred={b_pred:+.5e} | y(0.025)={ys[0]:+.6e}")

print("\nN5c inequality (*) for the cosine at moderate/large tau; region |x|,|x'|<=4, |x-x'|<=3 sqrt(2 D tau)")
for t in [0.2, 0.4, 1.0, 2.0, 4.0]:
    XA, XB = np.meshgrid(xg[cen], xg[cen], indexing="ij")
    near = np.abs(XA - XB) <= 3*np.sqrt(2*D*t)
    logR = log_rho0(XA, XB, t, D) - int_avgV_closed("cos", XA, XB, t, D, (V0, k))
    L = (logR - np.log(Kcos[t][np.ix_(cen, cen)]))[near]
    print(f"   tau={t:3.1f}: max L = {L.max():+.3e}   min L = {L.min():+.3e}  ->", "PASS" if L.max() <= 1e-10 else "FAIL")


# ===========================================================================
print("\n=== N6  oscillator partition-function approximant Zhat_m ===")
# Circulant evaluation (eq. (37)): Zhat_m = prod_k [2(1-cos th_k) + (2 kap D tau^2/3)(2+cos th_k)]^(-1/2) e^{-m kap D tau^2/6}
# Cross-checked against a grid evaluation Tr(M^m), M_ij = h rho0(x_i,x_j;tau) exp(-int<V>_u du).
# Z = 1/(2 sinh(beta om/2)). Prediction (eq. (35)): m^2 (1 - Zhat_m/Z) -> A = D beta^3 kap^2 <x^2>/12,
# <x^2> = (D/om) coth(beta om/2). FAIL if any Zhat_m > Z, or if the Richardson-extrapolated
# m^2(1 - Zhat/Z) at the largest m differs from A by more than 1e-3 relative.
D, kap = 0.5, 1.0
om = np.sqrt(2*D*kap)


def logZhat_circ(beta, m):
    tau = beta/m
    th = 2*np.pi*np.arange(m)/m
    return -0.5*np.sum(np.log(4*np.sin(th/2)**2 + (2*kap*D*tau**2/3)*(2 + np.cos(th)))) - m*kap*D*tau**2/6


def logZprim_circ(beta, m):
    tau = beta/m
    th = 2*np.pi*np.arange(m)/m
    return -0.5*np.sum(np.log(4*np.sin(th/2)**2 + 2*kap*D*tau**2))


def logZhat_grid(beta, m, h=0.02, Lbox=10.0):
    tau = beta/m
    x_ = np.arange(-Lbox, Lbox + h/2, h)
    XA, XB = np.meshgrid(x_, x_, indexing="ij")
    M = h*np.exp(log_rho0(XA, XB, tau, D) - int_avgV_quad_closed(XA, XB, tau, D, kap))
    mu = np.linalg.eigvalsh(M)
    return np.log(np.sum(mu**m))


for m in [1, 2, 4, 8, 16]:
    a_, b_ = logZhat_circ(4.0, m), logZhat_grid(4.0, m)
    print(f"N6a beta=4 m={m:2d}: log Zhat circulant={a_:+.12f}  grid={b_:+.12f}  diff={a_-b_:+.1e}")

for beta in [1.0, 4.0, 10.0]:
    logZ = -np.log(2*np.sinh(beta*om/2))
    A = D*beta**3*kap**2*(D/om)/np.tanh(beta*om/2)/12
    print(f"\nN6b beta={beta}: Z={np.exp(logZ):.10e}, predicted A = {A:.8f}")
    ms = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048]
    f = {}
    allbelow, primabove = True, True
    for m in ms:
        lz = logZhat_circ(beta, m)
        lp = logZprim_circ(beta, m)
        r = np.exp(lz - logZ)
        f[m] = m**2*(-np.expm1(lz - logZ))
        allbelow &= (lz <= logZ)
        primabove &= (lp >= logZ)
        if m in (1, 2, 4, 8, 64, 512, 2048):
            print(f"   m={m:5d}  Zhat/Z={r:.12f}  m^2(1-Zhat/Z)={f[m]:.8f}  Zprim/Z={np.exp(lp-logZ):.12f}")
    rich = 2*f[2048] - f[1024]
    print(f"   Richardson 2f(2048)-f(1024) = {rich:.8f}   rel. dev. from A = {abs(rich/A-1):.2e}")
    print("   all Zhat_m <= Z:", allbelow, "  all Zprim_m >= Z:", primabove, " ->",
          "PASS" if (allbelow and abs(rich/A - 1) < 1e-3) else "FAIL")


# ===========================================================================
print("\n=== N7  Coulomb: Gaussian average of 1/|y| in d = 3 ===")
# Claim (eq. (44)): for y ~ N(mu, s^2 I_3), <1/|y|> = erf(|mu|/(sqrt2 s))/|mu|, -> sqrt(2/pi)/s at mu = 0.
# Checked against (i) Monte Carlo, (ii) 2D quadrature in (r, cos theta) done numerically.
# FAIL if |z_MC| > 4 or quadrature rel. err > 1e-8.
def inv_r_closed(mu, s):
    return np.sqrt(2/np.pi)/s if mu == 0 else special.erf(mu/(np.sqrt(2)*s))/mu


for mu, s in [(0.0, 0.2), (0.0, 1.0), (0.3, 0.2), (0.3, 1.0), (1.0, 0.5), (3.0, 1.0)]:
    y = rng.normal(0, s, size=(1_000_000, 3)); y[:, 2] += mu
    g = 1/np.linalg.norm(y, axis=1)
    z = (g.mean() - inv_r_closed(mu, s))/(g.std()/np.sqrt(len(g)))
    dens = lambda c, r: 2*np.pi*r*(2*np.pi*s**2)**-1.5*np.exp(-(r**2 + mu**2 - 2*r*mu*c)/(2*s**2))
    q = integrate.dblquad(dens, 0, mu + 15*s, -1, 1, epsabs=0, epsrel=1e-12)[0]
    rel = abs(q/inv_r_closed(mu, s) - 1)
    print(f"N7a mu={mu:3.1f} s={s:3.1f}: closed={inv_r_closed(mu, s):.10f}  quad rel err={rel:.1e}  MC z={z:+.2f}  ->",
          "PASS" if (abs(z) < 4 and rel < 1e-8) else "FAIL")

print("\nN7b  I(x,x') = int_0^tau <1/r>_u du vs bound sqrt(pi tau/D) (eq. (46)); D = 0.5, tau = 1")
D, tau = 0.5, 1.0
gq, wq = np.polynomial.legendre.leggauss(200)
th = 0.25*np.pi*(gq + 1); wth = 0.25*np.pi*wq          # u = tau sin^2(theta), theta in (0, pi/2)
for xv, xpv in [((0, 0, 0), (0, 0, 0)), ((0.3, 0, 0), (0, 0, 0)), ((0.5, 0, 0), (-0.5, 0, 0)), ((1, 1, 0), (1, 0, 1)), ((3, 0, 0), (3, 0, 0))]:
    xv, xpv = np.array(xv, float), np.array(xpv, float)
    tot = 0.0
    for t_, wt in zip(th, wth):
        u = tau*np.sin(t_)**2
        mu = np.linalg.norm(xv + (u/tau)*(xpv - xv))
        s = np.sqrt(2*D*tau*np.sin(t_)**2*np.cos(t_)**2)   # run 2: tau-u written as tau cos^2
        tot += wt*2*tau*np.sin(t_)*np.cos(t_)*inv_r_closed(mu, s)
    print(f"   x={xv}, x'={xpv}:  I={tot:.10f}   bound={np.sqrt(np.pi*tau/D):.10f}   I-bound={tot-np.sqrt(np.pi*tau/D):+.1e}  I<=bound(+1e-12): {tot <= np.sqrt(np.pi*tau/D)+1e-12}")

print("\nN7c  monotone convergence of the truncation, x = x' = 0, D = 0.5, tau = 1:")
print("     int_0^tau <min(1/r, N)>_u du  (radial quadrature) should increase to sqrt(2 pi) =", f"{np.sqrt(2*np.pi):.10f}")
for Ntr in [1, 3, 10, 30, 100, 1000, 10000]:
    tot = 0.0
    for t_, wt in zip(th, wth):
        u = tau*np.sin(t_)**2
        s = np.sqrt(2*D*tau*np.sin(t_)**2*np.cos(t_)**2)   # run 2: tau-u written as tau cos^2
        p = lambda r: 4*np.pi*r**2*(2*np.pi*s**2)**-1.5*np.exp(-r**2/(2*s**2))
        val = integrate.quad(lambda r: min(1/r, Ntr)*p(r) if r > 0 else 0.0, 0, 15*s, points=[min(1/Ntr, 15*s)], limit=200)[0]
        tot += wt*2*tau*np.sin(t_)*np.cos(t_)*val
    print(f"     N={Ntr:6d}: {tot:.10f}")
```

Round-2 output, with stderr merged; the first six lines are the two warnings discussed in R4 and in N1:

```text
/home/claude/checks/round2/check_numeric.py:85: IntegrationWarning: The occurrence of roundoff error is detected, which prevents 
  the requested tolerance from being achieved.  The error may be 
  underestimated.
  num = integrate.quad(lambda y: f(y)*Vfun(kind, y, par), lo, hi, points=pts, limit=400, epsabs=0, epsrel=1e-13)[0]
/home/claude/checks/round2/check_numeric.py:257: RuntimeWarning: invalid value encountered in log
  L = (logR - np.log(Kcos[t][np.ix_(cen, cen)]))[near]
numpy 2.5.3 scipy 1.18.1

=== N1  <V>_u: quadrature from the definition vs closed form ===
N1 quad     draws=150  max rel err=1.32e-13  max |norm-1|=1.31e-13  -> PASS
N1 cos      draws=150  max rel err=1.56e-13  max |norm-1|=1.57e-13  -> PASS
N1 quartic  draws=150  max rel err=9.84e-14  max |norm-1|=8.79e-14  -> PASS

=== N2  weighted free-walk Monte Carlo (definition of the bridge) ===
N2 z-scores, j=1..15: +0.15 +1.83 +0.96 -0.07 +0.46 +0.40 -0.43 -0.49 +0.03 -0.48 -2.15 -2.23 -3.19 -2.47 -1.64
N2 effective sample size: 109598  max|z| = 3.19 -> PASS

=== N3  finite-m Trotter inequality (T6) on a grid ===
N3 cos  m= 2: min log(K_m/R_m)=+2.245e-02  max=5.382e-02  h-vs-h/2 disc=3.1e-15  -> PASS
N3 cos  m= 4: min log(K_m/R_m)=+2.038e-02  max=7.211e-02  h-vs-h/2 disc=2.7e-15  -> PASS
N3 cos  m= 8: min log(K_m/R_m)=+1.861e-02  max=7.764e-02  h-vs-h/2 disc=2.9e-15  -> PASS
N3 cos  m=16: min log(K_m/R_m)=+1.805e-02  max=7.912e-02  h-vs-h/2 disc=3.6e-15  -> PASS
N3 quad m= 2: min log(K_m/R_m)=+3.608e-03  max=2.536e-01  h-vs-h/2 disc=2.7e-15  -> PASS
N3 quad m= 4: min log(K_m/R_m)=+2.980e-03  max=3.208e-01  h-vs-h/2 disc=3.6e-15  -> PASS
N3 quad m= 8: min log(K_m/R_m)=+2.713e-03  max=3.378e-01  h-vs-h/2 disc=2.7e-15  -> PASS
N3 quad m=16: min log(K_m/R_m)=+2.639e-03  max=3.421e-01  h-vs-h/2 disc=2.9e-15  -> PASS

=== N4  oscillator: (*) against the exact (Mehler) kernel ===
 tau     max L        min L         at x=x'=0: L        large-tau asympt.
  0.05  -1.736e-08  -4.688e-05  -1.735836e-08  +1.176084e+00  -> PASS
  0.10  -2.776e-07  -3.749e-04  -2.776015e-07  +8.538856e-01  -> PASS
  0.20  -4.433e-06  -2.992e-03  -4.433191e-06  +5.548120e-01  -> PASS
  0.50  -1.709e-04  -4.590e-02  -1.709060e-04  +2.291667e-01  -> PASS
  1.00  -2.614e-03  -3.436e-01  -2.613653e-03  +7.009308e-02  -> PASS
  2.00  -3.572e-02  -2.181e+00  -3.572324e-02  -2.648051e-02  -> PASS
  5.00  -7.346e-01  -1.436e+01  -7.346486e-01  -7.346259e-01  -> PASS
 10.00  -4.831e+00  -4.083e+01  -4.831199e+00  -4.831199e+00  -> PASS

N4b small tau: -L compared with the leading term of part (b), Dk^2 tau^3 xbar^2/12,
    and with leading + next (eq. (30)); points with |x-x'| <= 2 sqrt(2 D tau), |xbar| >= 0.5
   tau=0.400  npts= 4508  max|(-L)/P1 - 1|=1.855e-01  max|(-L)/P2 - 1|=1.573e-02
   tau=0.200  npts= 3234  max|(-L)/P1 - 1|=9.184e-02  max|(-L)/P2 - 1|=3.982e-03
   tau=0.100  npts= 2372  max|(-L)/P1 - 1|=4.965e-02  max|(-L)/P2 - 1|=9.987e-04
   tau=0.050  npts= 1646  max|(-L)/P1 - 1|=2.375e-02  max|(-L)/P2 - 1|=2.499e-04
   tau=0.025  npts= 1272  max|(-L)/P1 - 1|=1.260e-02  max|(-L)/P2 - 1|=6.251e-05
   at xbar = 1, Delta = 0:  -L/tau^3 -> 0.042055, 0.041903, 0.041795, 0.041734, 0.041701    prediction D k^2/12 = 0.041667

=== N5  cosine potential, exact kernel by sinc-DVR diagonalization ===
N5 validation tau=0.025: max|log K_dvr - log rho0|=4.1e-12   max|log K_dvr - log K_Mehler|=1.0e-12  -> PASS
N5 validation tau=0.050: max|log K_dvr - log rho0|=2.3e-12   max|log K_dvr - log K_Mehler|=4.6e-13  -> PASS
N5 validation tau=0.100: max|log K_dvr - log rho0|=1.8e-12   max|log K_dvr - log K_Mehler|=7.9e-13  -> PASS
N5 validation tau=0.200: max|log K_dvr - log rho0|=2.6e-12   max|log K_dvr - log K_Mehler|=1.9e-12  -> PASS
N5 validation tau=0.400: max|log K_dvr - log rho0|=3.9e-12   max|log K_dvr - log K_Mehler|=4.9e-12  -> PASS
N5 validation tau=1.000: max|log K_dvr - log rho0|=7.1e-12   max|log K_dvr - log K_Mehler|=1.4e-11  -> PASS

N5b small-tau coefficient at Delta = 0: y(tau) = log(K/R)/tau^3, fit y = a + b tau + c tau^2
    predictions: a = D V'(xbar)^2/12, b = D^2 (V''^2/90 + V' V'''/30)   [eqs. (26), (29)]
   xbar=0.4: a_fit=+6.318462e-03 a_pred=+6.318610e-03 | b_fit=+1.09786e-03 b_pred=+1.09282e-03 | y(0.025)=+6.346076e-03
   xbar=0.8: a_fit=+2.144021e-02 a_pred=+2.144166e-02 | b_fit=-2.89190e-03 b_pred=-2.94000e-03 | y(0.025)=+2.136923e-02
   xbar=1.2: a_fit=+3.619401e-02 a_pred=+3.619570e-02 | b_fit=-6.81884e-03 b_pred=-6.87441e-03 | y(0.025)=+3.602516e-02
   xbar=1.6: a_fit=+4.163082e-02 a_pred=+4.163114e-02 | b_fit=-8.31388e-03 b_pred=-8.32386e-03 | y(0.025)=+4.142360e-02
   xbar=2.0: a_fit=+3.445220e-02 a_pred=+3.445091e-02 | b_fit=-6.45200e-03 b_pred=-6.40913e-03 | y(0.025)=+3.429026e-02
   xbar=2.8: a_fit=+4.676079e-03 a_pred=+4.675711e-03 | b_fit=+1.51909e-03 b_pred=+1.53092e-03 | y(0.025)=+4.713455e-03

N5c inequality (*) for the cosine at moderate/large tau; region |x|,|x'|<=4, |x-x'|<=3 sqrt(2 D tau)
   tau=0.2: max L = -4.257e-06   min L = -3.203e-04  -> PASS
   tau=0.4: max L = -6.477e-05   min L = -2.463e-03  -> PASS
   tau=1.0: max L = -2.142e-03   min L = -3.423e-02  -> PASS
   tau=2.0: max L = -2.525e-02   min L = -2.254e-01  -> PASS
   tau=4.0: max L = -2.208e-01   min L = -1.198e+00  -> PASS

=== N6  oscillator partition-function approximant Zhat_m ===
N6a beta=4 m= 1: log Zhat circulant=-2.719627694453  grid=-2.719627694453  diff=-2.4e-14
N6a beta=4 m= 2: log Zhat circulant=-2.196802064012  grid=-2.196802064012  diff=-4.3e-14
N6a beta=4 m= 4: log Zhat circulant=-2.047331120742  grid=-2.047331120742  diff=-8.5e-14
N6a beta=4 m= 8: log Zhat circulant=-2.000161919043  grid=-2.000161919042  diff=-1.7e-13
N6a beta=4 m=16: log Zhat circulant=-1.986517385831  grid=-1.986517385830  diff=-3.4e-13

N6b beta=1.0: Z=9.5951737567e-01, predicted A = 0.04508236
   m=    1  Zhat/Z=0.958861650618  m^2(1-Zhat/Z)=0.04113835  Zprim/Z=1.042190610987
   m=    2  Zhat/Z=0.989405070226  m^2(1-Zhat/Z)=0.04237972  Zprim/Z=1.011073404971
   m=    4  Zhat/Z=0.997278535555  m^2(1-Zhat/Z)=0.04354343  Zprim/Z=1.002805029432
   m=    8  Zhat/Z=0.999308369616  m^2(1-Zhat/Z)=0.04426434  Zprim/Z=1.000703618513
   m=   64  Zhat/Z=0.999989019861  m^2(1-Zhat/Z)=0.04497465  Zprim/Z=1.000011006242
   m=  512  Zhat/Z=0.999999828076  m^2(1-Zhat/Z)=0.04506884  Zprim/Z=1.000000171975
   m= 2048  Zhat/Z=0.999999989252  m^2(1-Zhat/Z)=0.04508132  Zprim/Z=1.000000010748
   Richardson 2f(2048)-f(1024) = 0.04508681   rel. dev. from A = 9.87e-05
   all Zhat_m <= Z: True   all Zprim_m >= Z: True  -> PASS

N6b beta=4.0: Z=1.3786028239e-01, predicted A = 1.38308629
   m=    1  Zhat/Z=0.478015011927  m^2(1-Zhat/Z)=0.52198499  Zprim/Z=1.813430203924
   m=    2  Zhat/Z=0.806309584104  m^2(1-Zhat/Z)=0.77476166  Zprim/Z=1.282288794403
   m=    4  Zhat/Z=0.936302596803  m^2(1-Zhat/Z)=1.01915845  Zprim/Z=1.081320855580
   m=    8  Zhat/Z=0.981525420587  m^2(1-Zhat/Z)=1.18237308  Zprim/Z=1.021263361088
   m=   64  Zhat/Z=0.999669027436  m^2(1-Zhat/Z)=1.35566362  Zprim/Z=1.000337580242
   m=  512  Zhat/Z=0.999994737169  m^2(1-Zhat/Z)=1.37961969  Zprim/Z=1.000005276034
   m= 2048  Zhat/Z=0.999999670453  m^2(1-Zhat/Z)=1.38222095  Zprim/Z=1.000000329753
   Richardson 2f(2048)-f(1024) = 1.38309012   rel. dev. from A = 2.77e-06
   all Zhat_m <= Z: True   all Zprim_m >= Z: True  -> PASS

N6b beta=10.0: Z=6.7382529153e-03, predicted A = 20.83522508
   m=    1  Zhat/Z=0.003567237375  m^2(1-Zhat/Z)=0.99643276  Zprim/Z=14.840642115558
   m=    2  Zhat/Z=0.131033430714  m^2(1-Zhat/Z)=3.47586628  Zprim/Z=5.511676112826
   m=    4  Zhat/Z=0.485971982819  m^2(1-Zhat/Z)=8.22444827  Zprim/Z=2.247485001725
   m=    8  Zhat/Z=0.794072797280  m^2(1-Zhat/Z)=13.17934097  Zprim/Z=1.321654570042
   m=   64  Zhat/Z=0.995176568157  m^2(1-Zhat/Z)=19.75677683  Zprim/Z=1.005085695127
   m=  512  Zhat/Z=0.999921037054  m^2(1-Zhat/Z)=20.69966242  Zprim/Z=1.000079479824
   m= 2048  Zhat/Z=0.999995040578  m^2(1-Zhat/Z)=20.80132288  Zprim/Z=1.000004967503
   Richardson 2f(2048)-f(1024) = 20.83522020   rel. dev. from A = 2.34e-07
   all Zhat_m <= Z: True   all Zprim_m >= Z: True  -> PASS

=== N7  Coulomb: Gaussian average of 1/|y| in d = 3 ===
N7a mu=0.0 s=0.2: closed=3.9894228040  quad rel err=2.2e-16  MC z=-0.62  -> PASS
N7a mu=0.0 s=1.0: closed=0.7978845608  quad rel err=3.3e-16  MC z=-0.65  -> PASS
N7a mu=0.3 s=0.2: closed=2.8879519915  quad rel err=2.2e-16  MC z=-1.96  -> PASS
N7a mu=0.3 s=1.0: closed=0.7860761479  quad rel err=2.2e-16  MC z=-0.93  -> PASS
N7a mu=1.0 s=0.5: closed=0.9544997361  quad rel err=2.2e-16  MC z=-0.10  -> PASS
N7a mu=3.0 s=1.0: closed=0.3324334013  quad rel err=0.0e+00  MC z=-2.14  -> PASS

N7b  I(x,x') = int_0^tau <1/r>_u du vs bound sqrt(pi tau/D) (eq. (46)); D = 0.5, tau = 1
   x=[0. 0. 0.], x'=[0. 0. 0.]:  I=2.5066282746   bound=2.5066282746   I-bound=-1.3e-15  I<=bound(+1e-12): True
   x=[0.3 0.  0. ], x'=[0. 0. 0.]:  I=2.2401862525   bound=2.5066282746   I-bound=-2.7e-01  I<=bound(+1e-12): True
   x=[0.5 0.  0. ], x'=[-0.5  0.   0. ]:  I=1.8038160253   bound=2.5066282746   I-bound=-7.0e-01  I<=bound(+1e-12): True
   x=[1. 1. 0.], x'=[1. 0. 1.]:  I=0.7725925307   bound=2.5066282746   I-bound=-1.7e+00  I<=bound(+1e-12): True
   x=[3. 0. 0.], x'=[3. 0. 0.]:  I=0.3333333332   bound=2.5066282746   I-bound=-2.2e+00  I<=bound(+1e-12): True

N7c  monotone convergence of the truncation, x = x' = 0, D = 0.5, tau = 1:
     int_0^tau <min(1/r, N)>_u du  (radial quadrature) should increase to sqrt(2 pi) = 2.5066282746
     N=     1: 0.9787169647
     N=     3: 1.8635976587
     N=    10: 2.3072922841
     N=    30: 2.4399862884
     N=   100: 2.4866289416
     N=  1000: 2.5046266558
     N= 10000: 2.5064377802
```

#### 4.5.3 `check_diagnostics.py` (D1–D3)

```python
# check_diagnostics.py -- P003.S02, follow-up diagnostics to run 1 of check_numeric.py [N].
# Standalone. Python 3.13.18, numpy 2.5.3, scipy 1.18.1. Seeds fixed below.
import numpy as np
from scipy import linalg

print("numpy", np.__version__)


def log_rho0(p, q, t, D):
    return -0.5*np.log(4*np.pi*D*t) - (p - q)**2/(4*D*t)


# D1: size of the run-1 roundoff in N7b at x = x' = 0 (where I = sqrt(pi tau/D) exactly).
D, tau = 0.5, 1.0
gq, wq = np.polynomial.legendre.leggauss(200)
th = 0.25*np.pi*(gq + 1); wth = 0.25*np.pi*wq
I1 = I2 = 0.0
for t_, wt in zip(th, wth):
    u = tau*np.sin(t_)**2
    s1 = np.sqrt(2*D*u*(tau - u)/tau)                       # run-1 formula
    s2 = np.sqrt(2*D*tau*np.sin(t_)**2*np.cos(t_)**2)       # run-2 formula
    I1 += wt*2*tau*np.sin(t_)*np.cos(t_)*np.sqrt(2/np.pi)/s1
    I2 += wt*2*tau*np.sin(t_)*np.cos(t_)*np.sqrt(2/np.pi)/s2
b = np.sqrt(np.pi*tau/D)
print(f"D1 x=x'=0: run-1 I - bound = {I1 - b:+.2e}   run-2 I - bound = {I2 - b:+.2e}")

# D2: where do the NaNs of log(K_dvr) in N5c come from? (negative/zero DVR entries)
h, Lb, D = 0.04, 12.0, 0.5
xg = np.arange(-Lb, Lb + h/2, h); N = len(xg)
idx = np.arange(N); dif = idx[:, None] - idx[None, :]
T = np.where(dif == 0, D*np.pi**2/(3*h**2), 2*D*(-1.0)**dif/(h**2*np.where(dif == 0, 1, dif)**2))
E, U = linalg.eigh(T + np.diag(np.cos(xg)))
cen = np.where(np.abs(xg) <= 4 + 1e-9)[0]
XA, XB = np.meshgrid(xg[cen], xg[cen], indexing="ij")
for t in [0.2, 0.4, 1.0, 2.0, 4.0]:
    K = ((U*np.exp(-t*E))@U.T/h)[np.ix_(cen, cen)]
    near = np.abs(XA - XB) <= 3*np.sqrt(2*D*t)
    bad = K <= 0
    print(f"D2 tau={t}: nonpositive DVR entries inside tested region: {np.sum(bad & near)}, outside: {np.sum(bad & ~near)};"
          f" min |x-x'| among them: {np.min(np.abs(XA-XB)[bad]) if bad.any() else float('nan'):.2f};"
          f" largest |K| among them: {np.max(np.abs(K[bad])) if bad.any() else 0:.1e}")

# D3: N2 repeated with independent seeds and 5x more paths (all runs reported).
def V(y): return np.cos(2.0*y)
def avg_closed(x, xp, u, tau, D):
    m = x + (u/tau)*(xp - x); s2 = 2*D*u*(tau - u)/tau
    return np.cos(2.0*m)*np.exp(-0.5*4.0*s2)
D, tau, x, xp = 0.5, 1.0, 0.3, -0.4
nsteps, npaths = 16, 2_000_000
delta = tau/nsteps
for seed in [20261113, 20261114]:
    rng = np.random.default_rng(seed)
    paths = x + np.cumsum(rng.normal(0.0, np.sqrt(2*D*delta), size=(npaths, nsteps - 1)), axis=1)
    w = np.exp(log_rho0(paths[:, -1], xp, delta, D) - log_rho0(x, xp, tau, D))
    W = w.sum(); zs = []
    for j in range(1, nsteps):
        f = V(paths[:, j - 1]); est = np.sum(w*f)/W
        se = np.sqrt(np.sum(w**2*(f - est)**2))/W
        zs.append((est - avg_closed(x, xp, j*delta, tau, D))/se)
    print(f"D3 seed={seed} paths={npaths}: z =", " ".join(f"{z:+.2f}" for z in zs), f" max|z|={max(map(abs, zs)):.2f}",
          "-> PASS" if max(map(abs, zs)) < 4 else "-> FAIL")
```

Round-2 output:

```text
numpy 2.5.3
D1 x=x'=0: run-1 I - bound = +2.25e-12   run-2 I - bound = -1.33e-15
D2 tau=0.2: nonpositive DVR entries inside tested region: 0, outside: 6110; min |x-x'| among them: 3.56; largest |K| among them: 4.4e-14
D2 tau=0.4: nonpositive DVR entries inside tested region: 0, outside: 3406; min |x-x'| among them: 5.00; largest |K| among them: 2.1e-14
D2 tau=1.0: nonpositive DVR entries inside tested region: 0, outside: 12; min |x-x'| among them: 7.92; largest |K| among them: 6.0e-15
D2 tau=2.0: nonpositive DVR entries inside tested region: 0, outside: 0; min |x-x'| among them: nan; largest |K| among them: 0.0e+00
D2 tau=4.0: nonpositive DVR entries inside tested region: 0, outside: 0; min |x-x'| among them: nan; largest |K| among them: 0.0e+00
D3 seed=20261113 paths=2000000: z = -2.23 -1.61 +0.28 +0.07 +0.78 +1.64 +0.64 +0.11 -0.46 +0.05 -0.94 -0.55 -0.17 -0.13 +0.25  max|z|=2.23 -> PASS
D3 seed=20261114 paths=2000000: z = -0.32 -0.07 +0.87 +0.33 -0.32 +0.09 +0.37 +0.54 +1.03 +0.63 +0.33 -0.03 +0.09 +1.31 +1.10  max|z|=1.31 -> PASS
```

#### 4.5.4 `check_extra.py` (N8)

```python
# check_extra.py -- P003.S02, check N8 [N], added after runs of check_numeric.py.
# Standalone. Python 3.13.18, numpy 2.5.3, scipy 1.18.1. No randomness.
# Tests the Delta-dependent tau^4 terms of eq. (28) for a non-quadratic potential:
#   delta = D tau^3 V'^2/12 + D tau^3 V''^2 Delta^2/720 + D tau^3 V' V''' Delta^2/240
#           + D^2 tau^4 (V''^2/90 + V' V'''/30) + O(tau^5)      (1D, derivatives at xbar)
# With D = 1/2 and Delta = 2 sqrt(tau):  delta/tau^3 = a + b tau + ..., a = D V'^2/12,
#   b = V''^2/180 + V' V'''/60.
# Exact kernel: sinc-DVR exactly as in check_numeric.py N5 (validated there against
# rho0 and Mehler to ~1e-11). tau values chosen so x = xbar - sqrt(tau), x' = xbar + sqrt(tau)
# are grid points (h = 0.04). FAIL if |a_fit/a_pred - 1| > 1e-3 or |b_fit - b_pred| > 0.05 |b_pred|.
import numpy as np
from scipy import linalg

print("numpy", np.__version__)
h, Lb, D = 0.04, 12.0, 0.5
xg = np.arange(-Lb, Lb + h/2, h); N = len(xg)
idx = np.arange(N); dif = idx[:, None] - idx[None, :]
T = np.where(dif == 0, D*np.pi**2/(3*h**2), 2*D*(-1.0)**dif/(h**2*np.where(dif == 0, 1, dif)**2))
V0, k = 1.0, 1.0
E, U = linalg.eigh(T + np.diag(V0*np.cos(k*xg)))


def log_rho0(p, q, t):
    return -0.5*np.log(4*np.pi*D*t) - (p - q)**2/(4*D*t)


def int_avgV_cos(x, xp, tau, n=80):
    g, w = np.polynomial.legendre.leggauss(n)
    u = 0.5*tau*(g + 1)
    m = x + (u/tau)*(xp - x); s2 = 2*D*u*(tau - u)/tau
    return 0.5*tau*np.sum(w*V0*np.cos(k*m)*np.exp(-0.5*k**2*s2))


taus = [0.0256, 0.04, 0.0576, 0.1024, 0.16]
for xb in [0.4, 0.8, 1.2, 2.0, 2.8]:
    ys = []
    for t in taus:
        r = np.sqrt(t)
        i, j = int(round((xb - r + Lb)/h)), int(round((xb + r + Lb)/h))
        assert abs(xg[i] - (xb - r)) < 1e-9 and abs(xg[j] - (xb + r)) < 1e-9
        Kij = (U[i, :]*np.exp(-t*E))@U[j, :]/h
        logR = log_rho0(xg[i], xg[j], t) - int_avgV_cos(xg[i], xg[j], t)
        ys.append((np.log(Kij) - logR)/t**3)
    c = np.polyfit(taus, ys, 2)
    V1, V2, V3 = -V0*k*np.sin(k*xb), -V0*k**2*np.cos(k*xb), V0*k**3*np.sin(k*xb)
    a_pred = D*V1**2/12
    b_pred = V2**2/180 + V1*V3/60
    b_noDelta = D**2*(V2**2/90 + V1*V3/30)   # what b would be if the Delta terms were absent
    ok = abs(c[2]/a_pred - 1) < 1e-3 and abs(c[1] - b_pred) < 0.05*abs(b_pred)
    print(f"N8 xbar={xb}: a_fit={c[2]:+.6e} a_pred={a_pred:+.6e} | b_fit={c[1]:+.5e} b_pred={b_pred:+.5e}"
          f" (b without Delta terms: {b_noDelta:+.5e}) ->", "PASS" if ok else "FAIL")
```

Round-2 output:

```text
numpy 2.5.3
N8 xbar=0.4: a_fit=+6.318586e-03 a_pred=+6.318610e-03 | b_fit=+2.18716e-03 b_pred=+2.18563e-03 (b without Delta terms: +1.09282e-03) -> PASS
N8 xbar=0.8: a_fit=+2.144119e-02 a_pred=+2.144166e-02 | b_fit=-5.85666e-03 b_pred=-5.87999e-03 (b without Delta terms: -2.94000e-03) -> PASS
N8 xbar=1.2: a_fit=+3.619514e-02 a_pred=+3.619570e-02 | b_fit=-1.37210e-02 b_pred=-1.37488e-02 (b without Delta terms: -6.87441e-03) -> PASS
N8 xbar=2.0: a_fit=+3.445124e-02 a_pred=+3.445091e-02 | b_fit=-1.28341e-02 b_pred=-1.28183e-02 (b without Delta terms: -6.40913e-03) -> PASS
N8 xbar=2.8: a_fit=+4.675900e-03 a_pred=+4.675711e-03 | b_fit=+3.05342e-03 b_pred=+3.06184e-03 (b without Delta terms: +1.53092e-03) -> PASS
```

#### 4.5.5 `check_tensor_d2.py` (S9, new in round 2)

```python
# check_tensor_d2.py -- P003.S02, check S9 [N], added in round 2 (response to audit finding F1.1).
# Standalone. Run: PYTHONHASHSEED=0 python3 -P -s check_tensor_d2.py
# Tested with: Python 3.13.18, sympy 1.14.0. Parameters drawn with random.Random(20261113).
#
# Purpose: test the INDEX CONTRACTIONS of eq. (27) in d = 2, where they are not
# reducible to 1D products. For a polynomial potential the bridge action
# S = int_0^tau V(omega(u)) du has an exactly computable variance:
#     Var S = 2 int_0^tau du int_0^u dv Cov( V(h(u)), V(h(v)) ),
#     h(u) = omega(u) - xbar = s(u) Delta + xi(u),  s(u) = u/tau - 1/2,
# with xi the centred bridge, Cov(xi_i(u), xi_j(v)) = delta_ij C(u,v), eq. (8).
# Gaussian moments are computed by Stein's identity E[x_i f(X)] = sum_j Sigma_ij E[d_j f(X)]
# (derived in the text, section 4.3), self-tested below. The potential is taken as its
# Taylor polynomial at xbar, cubic + quartic, with random rational coefficients:
#     V(xbar + h) = V_i h_i + (1/2) V_ij h_i h_j + (1/6) V_ijk h_i h_j h_k + (1/24) V_ijkl h_i h_j h_k h_l
# (the constant V(xbar) does not enter Var S). tau = e^2, Delta = e*dvec (the regime |Delta| ~ sqrt(tau)).
# Eq. (27) predicts, with summation over repeated indices,
#   [e^6]  D V_i V_i / 6
#   [e^8]  D V_ij d_j V_ik d_k / 360 + D V_i V_ijk d_j d_k / 120 + D^2 ( V_ij V_ij / 45 + V_i V_ijj / 15 )
# and no e^0..e^5 or e^7 terms; no fourth-derivative terms through e^8.
# Alternative readings of the contractions are evaluated too, to show the test discriminates.
# FAIL if any predicted coefficient differs from the exact one, or a forbidden coefficient is nonzero.
# Assumptions ([A] in text): D > 0, 0 < v < u < tau; the potential is not bounded below, which is
# irrelevant here: Var S is a Gaussian-moment identity, not a statement about e^{-tau H}.
import itertools
import random
from functools import lru_cache
import sympy as sp

print("sympy", sp.__version__)
rng = random.Random(20261113)
e = sp.symbols('e', positive=True)
u, v = sp.symbols('u v', positive=True)


def make_moment(Sigma, n):
    """Moments of a centred Gaussian vector of length n with covariance Sigma (sympy Matrix)."""
    @lru_cache(maxsize=None)
    def mom(m):
        k = sum(m)
        if k == 0:
            return sp.Integer(1)
        if k % 2:
            return sp.Integer(0)
        i = next(a for a in range(n) if m[a] > 0)
        m1 = list(m); m1[i] -= 1                      # x^m = x_i * x^{m1}
        res = sp.Integer(0)
        for j in range(n):                            # Stein: E[x_i f] = sum_j Sigma_ij E[d_j f]
            if m1[j] > 0 and Sigma[i, j] != 0:
                m2 = list(m1); c = m2[j]; m2[j] -= 1
                res += Sigma[i, j]*c*mom(tuple(m2))
        return sp.expand(res)
    return mom


def expect(poly, X, mom):
    P = sp.Poly(sp.expand(poly), *X)
    return sp.expand(sum(coef*mom(tuple(mon)) for mon, coef in P.terms()))


# ---- self-test of the moment routine against textbook Gaussian moments
s11, s12, s22 = sp.symbols('s11 s12 s22')
Sig = sp.Matrix([[s11, s12], [s12, s22]])
x1, x2 = sp.symbols('x1 x2')
mt = make_moment(Sig, 2)
tests = [(x1**4, 3*s11**2), (x1**6, 15*s11**3), (x1**2*x2**2, s11*s22 + 2*s12**2),
         (x1**3*x2, 3*s11*s12), (x1**4*x2**2, 3*s11**2*s22 + 12*s11*s12**2), (x1**3, 0)]
ok_self = all(sp.expand(expect(p, (x1, x2), mt) - r) == 0 for p, r in tests)
print("S9 self-test of Gaussian moment routine:", "PASS" if ok_self else "FAIL")


def rat(lo=-9, hi=9, dmax=5):
    q = sp.Rational(rng.randint(lo, hi), rng.randint(1, dmax))
    return q


def sym_tensor(order, d=2):
    """Random fully symmetric tensor of given order in d dims (dict index-tuple -> Rational)."""
    T = {}
    for idx in itertools.combinations_with_replacement(range(d), order):
        val = rat()
        for perm in set(itertools.permutations(idx)):
            T[perm] = val
    return T


allpass = ok_self
for run in range(3):
    d = 2
    Dv = sp.Rational(rng.randint(1, 9), rng.randint(1, 4))
    g = [rat() for _ in range(d)]
    H = sym_tensor(2); T3 = sym_tensor(3); T4 = sym_tensor(4)
    dvec = [rat(-5, 5, 3) for _ in range(d)]
    if all(x == 0 for x in dvec):
        dvec[0] = sp.Integer(1)
    tau = e**2
    Delta = [e*dv for dv in dvec]
    s_u, s_v = u/tau - sp.Rational(1, 2), v/tau - sp.Rational(1, 2)
    # covariance on the triangle 0 < v < u < tau, eq. (8)
    Cuu = 2*Dv*u*(tau - u)/tau
    Cvv = 2*Dv*v*(tau - v)/tau
    Cuv = 2*Dv*v*(tau - u)/tau
    X = sp.symbols('a1 a2 b1 b2')                    # xi(u) = (a1,a2), xi(v) = (b1,b2)
    Sigma = sp.Matrix([[Cuu, 0, Cuv, 0], [0, Cuu, 0, Cuv], [Cuv, 0, Cvv, 0], [0, Cuv, 0, Cvv]])
    mom = make_moment(Sigma, 4)

    def Vpoly(h):
        out = sum(g[i]*h[i] for i in range(d))
        out += sp.Rational(1, 2)*sum(H[(i, j)]*h[i]*h[j] for i in range(d) for j in range(d))
        out += sp.Rational(1, 6)*sum(T3[(i, j, k)]*h[i]*h[j]*h[k] for i in range(d) for j in range(d) for k in range(d))
        out += sp.Rational(1, 24)*sum(T4[(i, j, k, l)]*h[i]*h[j]*h[k]*h[l]
                                      for i in range(d) for j in range(d) for k in range(d) for l in range(d))
        return out

    hu = [s_u*Delta[i] + X[i] for i in range(d)]
    hv = [s_v*Delta[i] + X[2 + i] for i in range(d)]
    Vu, Vv = Vpoly(hu), Vpoly(hv)
    cov = expect(Vu*Vv, X, mom) - expect(Vu, X, mom)*expect(Vv, X, mom)
    cov = sp.expand(cov)
    varS = sp.expand(2*sp.integrate(sp.integrate(cov, (v, 0, u)), (u, 0, tau)))
    co = {n: sp.nsimplify(varS.coeff(e, n)) for n in range(0, 13)}

    # predictions of eq. (27), explicit index sums
    R = range(d)
    ViVi = sum(g[i]**2 for i in R)
    HdHd = sum(sum(H[(i, j)]*dvec[j] for j in R)**2 for i in R)
    gTdd = sum(g[i]*T3[(i, j, k)]*dvec[j]*dvec[k] for i in R for j in R for k in R)
    trH2 = sum(H[(i, j)]**2 for i in R for j in R)
    gLap = sum(g[i]*T3[(i, j, j)] for i in R for j in R)
    p6 = Dv*ViVi/6
    p8 = Dv*HdHd/360 + Dv*gTdd/120 + Dv**2*(trH2/45 + gLap/15)
    # alternative readings (should NOT match)
    gd = sum(g[i]*dvec[i] for i in R)
    alt_gT = gd*sum(T3[(i, j, j)]*dvec[i] for i in R for j in R)            # (V_i d_i)(V_ijj d_j)
    trH = sum(H[(i, i)] for i in R)
    alt8_a = Dv*HdHd/360 + Dv*alt_gT/120 + Dv**2*(trH2/45 + gLap/15)
    alt8_b = Dv*HdHd/360 + Dv*gTdd/120 + Dv**2*(trH**2/45 + gLap/15)        # (tr H)^2 instead of tr H^2
    forbidden = [n for n in (0, 1, 2, 3, 4, 5, 7) if co[n] != 0]
    r6, r8 = sp.simplify(co[6] - p6), sp.simplify(co[8] - p8)
    passed = (r6 == 0 and r8 == 0 and not forbidden)
    allpass &= passed
    print(f"\nS9 run {run}: D={Dv}, grad={g}, dvec={dvec}")
    print(f"   H={[[H[(i, j)] for j in R] for i in R]}, V_111,V_112,V_122,V_222={[T3[(0,0,0)],T3[(0,0,1)],T3[(0,1,1)],T3[(1,1,1)]]}")
    print(f"   exact [e^6]={co[6]}  pred={p6}  resid={r6}")
    print(f"   exact [e^8]={co[8]}  pred={p8}  resid={r8}")
    print(f"   alternative (V_i d_i)(V_ijj d_j) in place of V_i V_ijk d_j d_k: resid={sp.simplify(co[8]-alt8_a)}")
    print(f"   alternative (tr H)^2 in place of tr(H^2):                      resid={sp.simplify(co[8]-alt8_b)}")
    print(f"   nonzero coefficients among e^0..e^5, e^7: {forbidden}   [e^10] (tau^5, not predicted) = {co[10]}")
    print("   ->", "PASS" if passed else "FAIL")

print("\nS9 overall:", "PASS" if allpass else "FAIL")
```

Round-2 output with `PYTHONHASHSEED=0`; the outputs for seeds 1, 2 and 3 are byte-identical (`cmp`):

```text
sympy 1.14.0
S9 self-test of Gaussian moment routine: PASS

S9 run 0: D=3, grad=[-5/3, -9/4], dvec=[-3, -2]
   H=[[-7/5, -5], [-5, -2]], V_111,V_112,V_122,V_222=[-8/5, -6/5, 0, 0]
   exact [e^6]=1129/288  pred=1129/288  resid=0
   exact [e^8]=125449/6000  pred=125449/6000  resid=0
   alternative (V_i d_i)(V_ijj d_j) in place of V_i V_ijk d_j d_k: resid=39/400
   alternative (tr H)^2 in place of tr(H^2):                      resid=222/25
   nonzero coefficients among e^0..e^5, e^7: []   [e^10] (tau^5, not predicted) = -5540639/1008000
   -> PASS

S9 run 1: D=2, grad=[-1/4, 1/5], dvec=[-1, 0]
   H=[[-8/5, 5/4], [5/4, 2/5]], V_111,V_112,V_122,V_222=[5, 0, -9, -2]
   exact [e^6]=41/1200  pred=41/1200  resid=0
   exact [e^8]=5453/8000  pred=5453/8000  resid=0
   alternative (V_i d_i)(V_ijj d_j) in place of V_i V_ijk d_j d_k: resid=-3/80
   alternative (tr H)^2 in place of tr(H^2):                      resid=881/2250
   nonzero coefficients among e^0..e^5, e^7: []   [e^10] (tau^5, not predicted) = 739831/100800
   -> PASS

S9 run 2: D=1, grad=[-2/5, 4/5], dvec=[0, 2]
   H=[[-7/2, -9/5], [-9/5, 8/5]], V_111,V_112,V_122,V_222=[-9/2, 4/5, -1, -3/4]
   exact [e^6]=2/15  pred=2/15  resid=0
   exact [e^8]=3061/4500  pred=3061/4500  resid=0
   alternative (V_i d_i)(V_ijj d_j) in place of V_i V_ijk d_j d_k: resid=-1/125
   alternative (tr H)^2 in place of tr(H^2):                      resid=442/1125
   nonzero coefficients among e^0..e^5, e^7: []   [e^10] (tau^5, not predicted) = 24937/84000
   -> PASS

S9 overall: PASS
```

### 4.6 What the part (d) test shows, read off from the output

Everything below is read directly from the round-2 output in §4.5. The numbers coincide with round 1.

Validity of $(\ast)$. For the oscillator ($D=\tfrac12$, $\kappa=1$), the maximum of $\ln(R/K)$ over the $121\times121$ grid on $[-3,3]^2$ is negative at every tested $\tau$: $-1.7\times10^{-8}$ at $\tau=0.05$, $-2.6\times10^{-3}$ at $\tau=1$, and $-4.83$ at $\tau=10$. The maximum is attained at $x=x'=0$.

Approach to 1 at small $\tau$. $1-R/K\approx-L$ approaches the part (b) prediction $P_1=\kappa^2D\tau^3\bar x^2/12$ with relative deviation decreasing linearly in $\tau$: 18.6%, 9.2%, 5.0%, 2.4%, 1.3% at $\tau=0.4,0.2,0.1,0.05,0.025$, for $|\bar x|\ge0.5$ and $|\Delta|\le2\sqrt{2D\tau}$. Including the next-order terms (30), the deviation decreases as $\tau^2$: $1.6\times10^{-2}$ down to $6.3\times10^{-5}$. At $\bar x=1$, $\Delta=0$, $-L/\tau^3\to0.041701$ at $\tau=0.0125$, against $D\kappa^2/12=0.041667$; the difference $3.4\times10^{-5}$ equals the predicted $\kappa^2D^2\tau/90=3.5\times10^{-5}$.

Large $\tau$. $\ln(R/K)(0,0)$ matches the asymptotic form (51) to $2\times10^{-5}$ at $\tau=5$ and to all printed digits at $\tau=10$. The ratio falls super-exponentially.

Non-quadratic potential. For $V=\cos x$, with the exact kernel from the DVR, the fitted $\tau^3$ coefficient at $\Delta=0$ agrees with $DV'(\bar x)^2/12$ to between $8\times10^{-6}$ and $8\times10^{-5}$ relative at six points (N5b), and to between $4\times10^{-6}$ and $4\times10^{-5}$ at five points with $\Delta=2\sqrt\tau$ (N8). The $\tau^4$ coefficient agrees with (29) to 0.1–1.6% (N5b), and with the $\Delta$-dependent version of (28) to 0.07–0.4% (N8). If the $\Delta$ terms of (28) were dropped, N8's prediction would be off by a factor 2.

Independent checks of $\langle V\rangle_u$. S1 (symbolic, from (3)); N1 (quadrature from (4); 450 random draws over three potentials; maximum relative error $1.6\times10^{-13}$); N2 (Monte Carlo from free random walks, i.e. from the definition of the bridge, not from (5); three runs, all within $|z|<4$, with the two follow-up runs within $|z|<2.3$); S5 (symbolic $\Phi_\tau$ for the oscillator).

## 5. Result

(a) Let $V$ be real, continuous and bounded below, and assume the growth condition [A3]: $V(y)\le C_ae^{a|y|^2}$ for every $a>0$, which every polynomially bounded potential satisfies. Let $H=K\dotplus V$. Then for every $\tau>0$ and all $x,x'\in\mathbb R^d$,
$$\langle x|e^{-\tau H}|x'\rangle\ \ge\ \rho_0(x,x';\tau)\exp\Big(-\int_0^\tau du\,\langle V\rangle_u(x,x')\Big),\qquad \langle V\rangle_u(x,x')=\int d^dy\,\frac{\rho_0(x,y;u)V(y)\rho_0(y,x';\tau-u)}{\rho_0(x,x';\tau)},$$
and equivalently $\langle V\rangle_u$ is the average of $V$ over $\mathcal N\big(x+\tfrac u\tau(x'-x),\,\tfrac{2Du(\tau-u)}\tau\mathbf 1_d\big)$. This is eq. (18). Equality holds iff the bridge action is a.s. constant, e.g. for constant $V$. Both derivations are given: the product formula in §3.2, with finite-$m$ bead marginals (16) at times $t_j=j\tau/m$, and Feynman–Kac in §3.3. Without [A3], the Feynman–Kac route still gives the inequality in integrated (bilinear) form, hence almost everywhere. The positivity of $\rho_0$ is used at P1–P5 of §3.4. The essential use is that the normalized bead product (15), and the bridge measure, are probability measures, so that Jensen's inequality applies.

(b) The approximant is the bead integral (21). Under [A5], $\hat Z_m(\beta)\le\operatorname{Tr}e^{-\beta H}$ (23). Replacing $\int_0^\tau du\,\langle V\rangle_u$ by the two-point trapezium rule gives exactly the kernel of $e^{-\tau V/2}e^{-\tau K}e^{-\tau V/2}$ (24). For $V\in C^4$, bounded below, with bounded derivatives of orders 1–4, and $|x-x'|=O(\sqrt{D\tau})$,
$$\ln\langle x|e^{-\tau H}|x'\rangle-\ln[\text{right side of }(\ast)]=\frac{D\tau^3}{12}\,\big|\nabla V(\tfrac{x+x'}2)\big|^2+O(D^2\tau^4),$$
with the complete $\tau^4$ term given in (28), written in index notation with every contraction explicit (round 2, F1.1). Consequently
$$\frac{\operatorname{Tr}e^{-\beta H}-\hat Z_m(\beta)}{\operatorname{Tr}e^{-\beta H}}=\frac{D\beta^3}{12\,m^2}\,\langle|\nabla V|^2\rangle_\beta+O(m^{-3}),$$
so the error is of order $1/m^2$ at fixed $\beta$, approached from below (35). For the oscillator the coefficient is $(\beta\omega_0)^3\coth(\beta\omega_0/2)/48$. The remainder estimates rest on power counting (`[?]` items 11–13 in the Risk register).

(c) The Coulomb potential $-q^2/r$ in $d=3$ is not bounded below, so (a) does not apply directly. One needs a self-adjoint, bounded-below $H$ (Kato's theorem), a regularization satisfying (a), and removal of the regulator on both sides. I used $V_N=\max(-q^2/r,-N)$. The left side converges by strong resolvent convergence ($H^2$ is a common core, and $\|(H_N-H)\phi\|\to0$ for $\phi\in H^2$) together with the bounded functional calculus under a uniform lower bound. The right side converges by the monotone convergence theorem applied three times, and the limit is finite because $\int_0^\tau du\,\langle1/r\rangle_u\le\sqrt{\pi\tau/D}$. The result is (47): $\langle x|e^{-\tau H}|x'\rangle\ge\rho_0\exp\!\big(q^2\int_0^\tau du\,\operatorname{erf}(|m(u)|/\sqrt2\sigma_u)/|m(u)|\big)$, valid for all $x,x'$. The error estimate of (b) does not apply: $V$ is not smooth at the origin, the coefficient $q^4\langle r^{-4}\rangle_\beta$ diverges for any state with nonzero density at the origin, and within $\sqrt{D\tau}$ of the origin the local defect is $O(q^4\tau/D)$ (48) rather than $O(\tau^3)$. A heuristic, not derived, suggests an $m^{-3/2}$ law in a confined setting (49). On $L^2(\mathbb R^3)$ the trace itself is infinite, so the trace-level statement is vacuous there.

(d) For the oscillator ($D=\tfrac12$, $\kappa=1$), $R/K\le1$ held on the whole grid at every $\tau$ from 0.05 to 10. At small $\tau$, $1-R/K$ approaches the part (b) leading term with relative deviation $\propto\tau$, and approaches the next-order expression (30) with deviation $\propto\tau^2$. At large $\tau$ the ratio collapses as $e^{-\kappa D\tau^2/6+\omega_0\tau/2}/\sqrt{2\omega_0\tau}$, so the bound is valid but uninformative. $\hat Z_m\le Z$ for all $m$, and $m^2(1-\hat Z_m/Z)$ converges to the predicted coefficient to between $10^{-4}$ and $2\times10^{-7}$ relative, depending on $\beta$. The formula for $\langle V\rangle_u$ was checked independently by symbolic integration, by quadrature, and by Monte Carlo from free random walks. The $\tau^3$ and $\tau^4$ coefficients were also confirmed for the non-quadratic $V=\cos x$ against an independent DVR kernel.

Confidence by section:

(a): high. Two independent derivations, plus direct numerical tests of the finite-$m$ inequality (N3) and of $(\ast)$ (N4, N5c). Confidence would drop if the hypotheses of Kato's product formula or of the kernel-continuity result were misread; both were retrieved.

(b): high for the inequality and the trapezium identity. High for the leading coefficient $1/12$, which has five independent confirmations (S7, S8, N4b, N5b, N8). High for the index structure of the $\tau^4$ term in $d\ge2$, which S9 confirms exactly in $d=2$ (round 2). High for the $1/m^2$ order for smooth confining potentials (N6b). Medium for the rigour of the remainder and tail estimates, which would rise with a proof of open question 1.

(c): medium-high for the regularization argument. It depends on four Reed–Simon locators that were corroborated through papers citing them but were not read in the books. High that the (b) estimate does not apply. Medium for (48). Low for (49).

(d): high.

## 6. Convergence check

Does the derivation reproduce the declared result? Yes, for every item declared in §1(2): the form of $(\ast)$ and of $\langle V\rangle_u$, $\hat Z_m\le Z$, the trapezium identity, an $O(\tau^3)$ local defect, an $O(1/m^2)$ global error, and the Coulomb picture. One thing I had not declared, because I did not know it: the leading local defect $D\tau^3|\nabla V|^2/12$ equals the Takahashi–Imada correction term. The retrieved abstract gives $V\to V+(\hbar^2/24m)(\beta/M)^2\sum_i(\partial V/\partial r_i)^2$; in the present units $\hbar^2/24m=2D/24=D/12$ and $\beta/M=\tau$, so the added action per slice is $\tau\cdot D\tau^2|\nabla V|^2/12$. I noticed this after the computation, and nothing in the derivation uses it. There is no disagreement to report between the declared and the derived results.

Steps that someone who did not know the target might not have chosen as I did. I list them even where I believe each is justified.
1. Passing to the limit through test functions in T6. This is forced by the gap between strong operator convergence and pointwise kernel convergence, not by the answer.
2. Using Kato's form-sum product formula rather than the operator-sum version. This was chosen to avoid an essential-self-adjointness hypothesis, and it is independent of the answer.
3. Expanding about the midpoint $\bar x$. This is motivated by the $x\leftrightarrow x'$ symmetry. Any expansion point within $O(\sqrt{D\tau})$ gives the same leading term; the midpoint only makes the $\tau^{7/2}$ terms vanish.
4. The tilted-variance representation $\delta=\int_0^1(1-\lambda)\operatorname{Var}_\lambda Y\,d\lambda$. This is a standard convexity device, used to make the sign manifest and to organize the cumulant expansion.
5. The truncation $V_N=\max(V,-N)$. It was chosen because it is monotone, which makes the monotone convergence theorem available. Smoothing, $-q^2/\sqrt{r^2+\epsilon^2}$, is also monotone in $\epsilon$ and would serve equally.
6. The cutoff $f(\lambda)=e^{-\tau\max(\lambda,-E_*-1)}$ in (41). This is a standard device for applying the bounded functional calculus to semibounded operators.
7. In the checks: restricting N4b to $|\bar x|\ge0.5$, to avoid dividing by a vanishing leading term, and choosing $\Delta=2\sqrt\tau$ in N8, so that the points fall on the DVR grid. Neither choice is informed by the expected numbers.
No ansatz or substitution was chosen to reproduce a known coefficient. The integrals $I_1$–$I_5$ are dictated by the Taylor expansion, and their values come from S4.

Would the derivation still run if the standard result were slightly different? The coefficient $1/12$ is $\tfrac12\cdot I_1/(D\tau^3)$ with $I_1=D\tau^3/6$. A different value would require an error in $I_1$ (checked by S4) or in the factor $\tfrac12$ of the cumulant expansion (checked exactly by S8, where the alternative $1/24$ leaves a PDE residual $-DF^2s^2/8$). The numerics would have caught such an error independently: a coefficient $1/24$ makes $(-L)/P_1\to2$ in N4b and halves $a_{\rm pred}$ in N5b and N8. If the true local defect were $O(\tau^2)$, the global error would be $O(1/m)$ and $m^2(1-\hat Z/Z)$ would grow linearly in $m$ in N6b; instead it converges to the predicted $A(\beta)$. What is not protected: the Coulomb heuristic (49) is untested and could be wrong by a logarithm or a power without my noticing. In answer-1 I noted that the $d>1$ tensor structure of (28) was untested. Round 2 closes that for $d=2$: S9 computes $\operatorname{Var}S$ exactly for cubic-plus-quartic potentials and matches every contraction in (27), and two wrong readings of the contractions fail. $d\ge3$ is not computed. The index expressions are dimension-independent, so I expect no surprise there, but that expectation is not a test.

## 7. Risk register

Each line: what the item is, and what happens if it is wrong.

1. `[R]` Reed–Simon II Thm X.28 (form sum = closure of $K+V$ on $C_c^\infty$). Used only to identify $H$. If wrong, every result still holds for the form-sum $H$.
2. `[R]` Rudin Thm 1.34 (dominated convergence), Thm 1.26 (monotone convergence, corroborated), Thm 3.3 (Jensen). Standard theorems. A wrong locator does not affect any result, and Lemma J is proved in the text.
3. `[R]` Reed–Simon I Thm VI.23 (HS ⇔ $L^2$ kernel), used for $\operatorname{Tr}e^{-\beta H}=\int K_\beta(x,x)dx$ in (22). If wrong, (23) needs another justification of this trace formula.
4. `[R]` Reed–Simon II Thm X.15 (Kato's theorem), corroborated, used in (38). If wrong, define $H$ as a form sum by KLMN instead; the argument is otherwise unchanged.
5. `[R]` Reed–Simon II Thm IX.28 ($H^2(\mathbb R^3)\subset L^\infty$), corroborated, used in (41). If wrong, use Hardy's inequality for the same estimate.
6. `[R]` Reed–Simon I Thms VIII.25(a) and VIII.20(b), corroborated, used in (41). If wrong, the regulator route to (47) is incomplete; the direct Feynman–Kac route via Bodmann–Leschke–Warzel remains.
7. `[V]` Kernel continuity (Bodmann–Leschke–Warzel §1.4), load-bearing for the pointwise statements (18) and (47). If wrong, both hold almost everywhere.
8. `[V]` Simon's Feynman–Kac Thm 1.1 and Kato's product formula via Simon's survey, load-bearing for §3.2–3.3 and (25). Retrieved and read.
9. `[?]` §3.3: (18) at every point without [A3]. If wrong, (18) holds a.e. for super-Gaussian $V$.
10. `[?]` §3.2 remark: truncation within the product-formula route. If wrong, route T needs [A3]; route FK does not.
11. `[?]` (25a): differentiation under the expectation (exponential moments of $Y$). If wrong, the exact representation fails, but the cumulant power counting and the numerical evidence remain.
12. `[?]` (26): the remainder is controlled only by formal power counting. If wrong, the $O(\tau^4)$ might be weaker; the numerics show $\tau^4$ behaviour for the oscillator and the cosine.
13. `[?]` (34)→(35): integrability of the remainder against the exact pair measure, including $|\Delta|\gg\sqrt{D\tau}$. If wrong, the $O(m^{-3})$ correction could be weaker; the $1/m^2$ leading term is confirmed numerically for the oscillator.
14. `[?]` (48): exponential moments of $X$ (Khas'minskii, `[R]`). If wrong, the $O(\tau)$ scaling at the origin is unproven, though dimensional analysis still fixes it as a function of $q^2\sqrt{\tau/D}$.
15. `[?]` (49): a heuristic $m^{-3/2}$. It could be wrong by a logarithm or a power.
16. `[A3]`, load-bearing for the pointwise conclusion via route T. Without it see items 9 and 10.
17. `[A4]`, load-bearing for (26)–(35). It deliberately fails for Coulomb, which is the content of (c).
18. `[A5]`, load-bearing for (23). Without it (23) is vacuous, as for Coulomb on $\mathbb R^3$.
19. `[A6]`, the interpretation of "free Brownian bridge". If another diffusion constant were meant, (6) and $(\ast)$ change.
20. `[R]` Hydrogen ground-state energy $-q^4/4D$, and $\operatorname{Tr}e^{-\beta H}=\infty$ for Coulomb. Neither is load-bearing.
21. `[R]` The Colbert–Miller DVR kinetic matrix. Validated numerically (N5), so not load-bearing.
22. `[R]` Uniqueness of the heat-kernel solution, used to identify the Mehler kernel through S6. If wrong, Mehler remains the standard result anyway.
23. Reproducibility. Sympy series output depends on the hash seed (R5). Mitigated by pinning the seed and checking four seeds, and by the 40-digit arbiter S7c, which does not rely on series expansion. Round 2: S9 was also run under four seeds, with identical output.
24. `[N]` (27)–(28) in $d\ge3$. S9 verifies the index contractions in $d=2$ only. If an index expression behaved differently in $d\ge3$, the higher-dimensional $\tau^4$ term would be wrong; the leading term (26) and the $1/m^2$ order would not be affected.
25. Second-party coverage (round 2). Audit 1 did not execute code (its Pass 6 was not performed) and had no web access. So no one but me has examined the verification code, or checked the `{ver: no}` locators (items 1–6), against their sources. If any check is circular or any locator wrong, audit 1 would not have caught it.

## 8. Sources

Round 2 added, removed and re-retrieved no source. The only new tool, Stein's identity in S9, is derived in §4.3. The lists below are unchanged from answer-1.

### Used

U1. B. Simon, "A Feynman–Kac formula for unbounded semigroups", arXiv:math-ph/9907022 (1999), Thm 1.1 and eqs. (1.1)–(1.2). `{ver: tool}`. Retrieval note: I fetched the arXiv PDF. Thm 1.1 states, for $V$ continuous on $\mathbb R^\nu$ and bounded below, $H=H_0+V$, $t>0$, $\varphi,\psi\in L^2$: $\langle\varphi,e^{-tH}\psi\rangle=\int\overline{\varphi(x)}\psi(y)e^{-tH_0}(x,y)Q(x,y;V,t)$. Here $H_0=-\tfrac12\Delta$, $e^{-tH_0}(x,y)=(2\pi t)^{-\nu/2}\exp(-|x-y|^2/2t)$, $Q$ is defined in (1.1) through the bridge $\alpha$ with $\mathbb E\alpha_i(t)\alpha_j(s)=\delta_{ij}\min(t,s)[1-\max(t,s)]$, and $\alpha(s)=b(s)-sb(1)$. The introduction says this form is Thm 6.6 of Simon, *Functional Integration and Quantum Physics* (Academic Press 1979; 2nd ed. AMS Chelsea 2005). That book was not retrieved, so its locator is `{ver: no}`.

U2. B. Simon, "Tosio Kato's work on non-relativistic quantum mechanics", arXiv:1711.00528, §18, Thm 18.2 (Kato's ultimate Trotter product formula), eq. (18.6), Remark 1. `{ver: tool}`. Retrieval note: I fetched characters 300000–400000. The theorem is stated for two closed quadratic forms with associated semigroups. The form sum $q_C=q_A+q_B$ "is always a closed form but $V_{q_C}$ may not be dense", and $e^{-t\dot C}=e^{-tC}P$ with $P$ the orthogonal projection onto the closure of the form domain (18.6). Remark 1 refers to Kato's paper and to Reed–Simon Thm S.21. The displayed limit (18.7) was garbled in the retrieved text; I took its content from the surrounding statement and from the Encyclopedia of Mathematics entry (C3).

U3. M. Reed, B. Simon, *Methods of Modern Mathematical Physics I: Functional Analysis*, revised and enlarged ed. (1980). Thm S.21: `{ver: no}`, content corroborated by U2. Thm VIII.25(a): `{ver: no}`, corroborated by arXiv:1912.07325 (proof of its Thm 5: common core plus pointwise convergence implies strong resolvent convergence, citing "[13, Theorem VIII.25 (a)]") and arXiv:1509.01580 §3. Thm VIII.20(b): `{ver: no}`, corroborated by arXiv:2501.04564 Prop. B.3.9 ("$f(T_n)\to f(T)$ strongly for all bounded continuous $f$", citing Thm VIII.20) and by U1's proof of its Thm 1.2 ("([4], Theorem VIII.20) for each fixed $m$, $f_m(A_n)\to f_m(A)$ strongly"). Thm VI.23: `{ver: no}`.

U4. M. Reed, B. Simon, *Methods of Modern Mathematical Physics II: Fourier Analysis, Self-Adjointness* (1975). Thm X.15: `{ver: no}`, corroborated by arXiv:1801.03361 Thm VII.2, which quotes "(Reed–Simon II, 1975, Th. X.15) Given a real potential $v\in L^2+L^\infty$, $n\le3$, the Hamiltonian $-\Delta+v$ is self-adjoint…". Thm IX.28: `{ver: no}`, corroborated by arXiv:1801.03361 Lemma VII.1. Thm X.28: `{ver: no}`, corroborated by T. Ichinose, Publ. RIMS Kyoto Univ. 16, 585 (1980), which cites it for the essential self-adjointness of $-\tfrac12\Delta+V$ with $V\in L^2_{\rm loc}$ bounded below, and by Simon, arXiv:1710.06999, item (3).

U5. B. Bodmann, H. Leschke, S. Warzel, "Wiener integration for quantum systems: a unified approach to the Feynman–Kac formula", arXiv:quant-ph/9703031 (in *Path Integrals: Dubna '96*, JINR E96-321, pp. 95–106), §1.4. `{ver: tool}`. Retrieval note: §1.4 states that for $v_-\in\mathcal K(\mathbb R^d)$ and $v_+\in\mathcal K_{\rm loc}(\mathbb R^d)$ the semigroup has, for each $t>0$, an integral kernel jointly continuous in $(t,q,q')$. It also states that for $v(q)=-\gamma/|q|$, $d\ge2$, the Feynman–Kac formula holds pointwise and the bridge expression defines the continuous kernel.

U6. W. Rudin, *Real and Complex Analysis*, 3rd ed. (1987). Thm 1.26 (monotone convergence): `{ver: no}`, corroborated by an article in the Irish Math. Soc. Bulletin 59 ("Convergence from below suffices", https://www.maths.tcd.ie/pub/ims/bull59/M5902.pdf), which refers to "the standard proof of the monotone convergence theorem ([1, 1.26])" with [1] = Rudin (edition not seen). Thm 1.34 (dominated convergence): `{ver: no}`. Thm 3.3 (Jensen): `{ver: no}`, not load-bearing.

### Consulted

C1. M. Takahashi, M. Imada, "Monte Carlo calculation of quantum systems. II. Higher order correction", J. Phys. Soc. Jpn. 53, 3765 (1984), doi:10.1143/JPSJ.53.3765, abstract. `{ver: tool}`. Retrieval note: the J-STAGE abstract gives the correction $V\to V+(\hbar^2/24m)(\beta/M)^2\sum_i(\partial V/\partial r_i)^2$. Used only in the Convergence check.

C2. T. Kato, "Trotter's product formula for an arbitrary pair of self-adjoint contraction semigroups", in *Topics in Functional Analysis* (I. Gohberg, M. Kac, eds.), Academic Press (1978), pp. 185–195. Bibliographic data from C3, `{ver: tool}`; the content was used via U2.

C3. Encyclopedia of Mathematics, "Trotter product formula" (oldid 42412): the semigroup form holds for $A,B$ bounded below. `{ver: tool}`.

C4. arXiv:2501.04564, App. B.3, which quotes Reed–Simon I Thms VIII.31, VIII.20 and VIII.25. `{ver: tool}`. Used for orientation.

C5. R. P. Feynman, A. R. Hibbs, *Quantum Mechanics and Path Integrals* (1965), ch. 11; R. P. Feynman, *Statistical Mechanics* (1972), ch. 3. Prior knowledge only. `{ver: no}`.

C6. D. T. Colbert, W. H. Miller, J. Chem. Phys. 96, 1982 (1992), the sinc-DVR kinetic matrix used in N5 and N8. `{ver: no}`; validated numerically in N5.

C7. B. Simon, "Schrödinger semigroups", Bull. Amer. Math. Soc. 7, 447 (1982). Retrieval from Project Euclid was blocked by a bot-protection page, so it was not used.

Excluded by the prompt (§5): Kole & De Raedt, Phys. Rev. E 64, 016704 (2001); arXiv:physics/0102015; the GitHub repository AndresMotta77/Introduccion_Fisica_Teorica. None was retrieved or consulted, and none appeared in any search-result list during this session. My search queries were chosen to avoid them.

## 9. Open questions

1. A rigorous remainder for (26). The target is a bound $|\delta-D\tau^3|\nabla V|^2/12|\le C\,D^2\tau^4(1+|\Delta|^2/D\tau)^k$, uniform in $\bar x$, followed by the tail control needed in (34). Suggested method: the tilted-variance representation (25a), together with Gaussian concentration (Poincaré or log-Sobolev) for Lipschitz functionals of the bridge.

2. Coulomb, numerically. Test (47) against an accurate Coulomb kernel, e.g. an s-wave radial propagator from a DVR in $r$ with a Dirichlet condition at $r=0$. Measure $\delta(0,0;\tau)/\tau\to q^4\operatorname{Var}X/4D$, and compute $\operatorname{Var}X$ by Monte Carlo of the 3D bridge. Then test the heuristic (49) in a confined Coulomb system with finite trace (e.g. hydrogen plus a harmonic trap) by fitting $1-\hat Z_m/Z$ against $m$.

3. The sandwich $\hat Z_m\le Z\le\hat Z^{\rm prim}_m$, observed for the oscillator at every tested $m$ (N6). The upper bound for the primitive approximant should follow from Golden–Thompson and Araki–Lieb–Thirring, at least along $m\to2m$ (`[R]`, not checked). It deserves a verified locator.

4. Since the leading defect equals the Takahashi–Imada term, $R_\tau e^{D\tau^3|\nabla V|^2/12}$ has an $O(\tau^4)$ local defect but is no longer a bound. Is there a modification that keeps the bound and improves the order?

5. Monotonicity of $\hat Z_m$ in $m$. N6 shows $\hat Z_m/Z$ increasing in $m$ for the oscillator. Jensen does not imply this, and I have not proved it.

6. Quantum statistics. Boson permutations keep all weights positive, so (23) extends to the bosonic trace. Fermions destroy P2, so no analogue follows.

7. The pointwise form of (18) for $V$ continuous and bounded below but violating [A3] (§3.3, `[?]`).

8. Extend S9 to $d=3$, which is the same script with three components per time. This would test the index form of (27) where the third-derivative tensor has its full set of independent components.

9. A code-executing and source-retrieving audit pass. Audit 1 performed neither. The `{ver: no}` Reed–Simon locators and the verification scripts are the parts of this answer that have so far been checked by no one but me.
