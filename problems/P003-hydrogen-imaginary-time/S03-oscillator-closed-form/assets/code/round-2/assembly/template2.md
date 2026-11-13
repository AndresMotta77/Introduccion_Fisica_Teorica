# P003.S03 — answer-2

Harmonic oscillator under a bridge-averaged slice weight: closed form, partition functions, levels.

Solver: Claude Opus 5.5 (`claude-opus-5-5`), tools: code, web. Conventions v1.5. Round 2, 2026-11-13 (answer-1: 2026-11-12).

Round 2 revises answer-1 in response to audit 1 (verdict ACCEPT-WITH-FIXES, one MINOR finding, F1.1). Section 10, Response to audit 1, gives the outcome for F1.1 and lists every change. In short: the identity matrix, written `\mathbb 1` in answer-1, prints as a wrong glyph under the house LaTeX template, and is now written $\mathbf 1$; part of the finding's evidence is contested in §10. The mathematics and the numbers are unchanged.

All verification code was re-run on 2026-11-13, and every output in §4 comes from that re-run. The re-run includes the superseded scripts that failed in round 1, so those failures are reproduced, not quoted. A new check, P1, tests the presentation fix.

---

## 1. Prior-knowledge declaration

This section was written when the document was assembled, after the derivation had been done in scratch form. I have tried to record only what I believed before starting, and I say explicitly where something was found during the derivation rather than known beforehand.

1. Recognition. I recognise the construction in outline. The weight $w$ is the first-cumulant (Jensen) approximation to the Feynman–Kac short-time density matrix: the potential is averaged over the free Brownian bridge from $x$ to $x'$ in imaginary time $\tau$, and the average is exponentiated. I associate it with Kole and De Raedt, Phys. Rev. E 64, 016704 (2001), which the prompt names and forbids. My recollection of that paper is limited to its use of such a bridge-averaged approximant for attractive Coulomb potentials (where the averaged potential stays finite) and to the fact that Jensen's inequality makes it a lower bound on the partition function. I do not recall any oscillator formula, table or figure from it. I did not retrieve it, nor the arXiv version, nor the GitHub repository named in §5 of the prompt.

2. Results I believed to be standard before deriving.
   - For (a), from familiarity with Brownian-bridge averages, I expected $w = \rho_0\,\exp[-\tau(x^2+xx'+x'^2)/6 - \tau^2/12]$. I was fairly confident of the $x$-dependent part and less confident of the constant $\tau^2/12$.
   - For the primitive product in (b) I recalled the time-sliced oscillator result $Z_m = [2\sinh(m\,\operatorname{arcsinh}(\tau/2))]^{-1}$, equivalently an effective frequency $\tilde\omega$ with $\sinh(\tau\tilde\omega/2) = \tau/2$. I held this with high confidence.
   - For the primitive kernel in (c) I recalled, with moderate confidence, the levels $(n+\tfrac12)(2/\tau)\operatorname{arcsinh}(\tau/2)$.
   - For the bridge weight I had no recalled formula for $\hat Z_m$ or for the eigenvalues. My expectation was that, being a Gaussian kernel, it would have an oscillator-like geometric spectrum with a $\tau$-dependent frequency, with an $O(\tau^2)$ error (a first-cumulant approximation should not beat second order). I also had a vague expectation that the bridge-averaged weight would come out more accurate than the primitive one. It does not (see §5).
   - I did not anticipate that $T_\tau$ stops being a positive operator for $\tau > \sqrt6$. That was found during the derivation of (c).

3. Standard route and where it is presented. The standard route is: complete the square to get the Gaussian bridge marginal; diagonalise the time-sliced quadratic action with discrete Fourier (normal) modes on the ring; evaluate the product over modes with a roots-of-unity identity; and get the spectrum of a Gaussian kernel from Mehler's formula. I associate the time-sliced oscillator with Kleinert's path-integral textbook (chapter 2) and with Feynman and Hibbs, but I cannot give confirmed locators and I did not use them. None of these is cited as a source below.

4. Anchoring. Section 3c of the prompt is empty, so I am not anchored on it. I am anchored on my own recall of the primitive arcsinh formula and of the form of $w$ given above, and on the expectation $\hat Z_m \le Z$ from Jensen's inequality. To counter that anchoring, each of these is recomputed from the problem's definitions by an independent numerical route (§4).

---

## 2. Setup

### 2.1 Conventions

$\hbar = M = \omega = 1$. All quantities ($x$, $\tau$, $\beta$, energies) are dimensionless; restoring units means $x \to x\sqrt{M\omega/\hbar}$, $\tau \to \omega\tau_{\rm phys}$, $\beta \to \hbar\omega\beta_{\rm phys}$, and energies in units of $\hbar\omega$. In (b) paths are closed, $x_{m+1} = x_1$, and $\tau = \beta/m$. All logarithms are natural. $\operatorname{artanh}$ and $\operatorname{arcsinh}$ are real inverse hyperbolic functions.

### 2.2 Symbol table

| Symbol | Meaning |
|---|---|
| $K = -\tfrac12 d^2/dx^2$, $V = \tfrac12 x^2$, $H = K+V$ | kinetic, potential, Hamiltonian |
| $\rho_0(x,x';t)$ | $(2\pi t)^{-1/2}e^{-(x-x')^2/2t}$, free kernel (the kernel of $e^{-tK}$, eq. (0)) |
| $w(x,x';\tau)$ | bridge-averaged slice weight defined in the problem |
| $I(x,x';\tau)$ | the exponent: $w = \rho_0\,e^{-I}$ |
| $\bar y(u)$, $\sigma^2(u)$ | mean and variance of the bridge marginal at time $u$ (eq. (4)) |
| $T_\tau$ | integral operator on $L^2(\mathbb R)$ with kernel $w(\cdot,\cdot;\tau)$ |
| $T^P_\tau$ | integral operator with kernel $e^{-\tau V(x)/2}\rho_0(x,x';\tau)e^{-\tau V(x')/2}$ |
| $N, A, B$ | parameters of a symmetric Gaussian kernel $N e^{-A(x^2+x'^2)/2 + Bxx'}$ |
| $\kappa = \sqrt{1+\tau^2/12}$, $s_\pm = \kappa \pm \tau/2$ | bridge-kernel parameters |
| $\kappa_P = \sqrt{1+\tau^2/4}$, $s^P_\pm = \kappa_P \pm \tau/2$ | primitive-kernel parameters |
| $q = s_-/s_+$, $q_P = s^P_-/s^P_+$ | eigenvalue ratios |
| $\varphi = 2\operatorname{arcsinh}(\tau/2)$ | so $s^P_\pm = e^{\pm\varphi/2}$ |
| $\lambda_n(\tau)$, $\lambda^P_n(\tau)$ | eigenvalues of $T_\tau$, $T^P_\tau$, labelled by Hermite index $n = 0,1,2,\dots$ |
| $E_n(\tau) = -\tau^{-1}\ln\lambda_n$, $E^P_n(\tau) = -\tau^{-1}\ln\lambda^P_n$ | approximate levels (bridge, primitive) |
| $\Omega(\tau)$, $\Omega_P(\tau)$ | level spacings, eqs. (25), (28) |
| $P$ | $m\times m$ cyclic shift, $(Px)_n = x_{n+1}$, indices mod $m$ |
| $\mathbf 1$ | $m\times m$ identity matrix |
| $\hat A$, $A^P$ | $m\times m$ matrices of the quadratic actions, eqs. (12), (19a) |
| $\theta_k = 2\pi k/m$, $k = 0,\dots,m-1$ | ring wave numbers |
| $D_m = s_+^m - s_-^m$, $D^P_m = (s^P_+)^m - (s^P_-)^m$ | denominators of $\hat Z_m$, $Z_m$ |
| $\hat Z_m(\beta)$, $Z_m(\beta)$ | bridge and primitive partition functions of (b) |
| $\hat E_m = -\partial_\beta\ln\hat Z_m$, $E_m = -\partial_\beta\ln Z_m$ | their energies, derivative taken at fixed $m$ |
| $U(\beta) = \tfrac12\coth(\beta/2)$ | exact thermal energy (given, §3a of the prompt) |
| $H_n$ | physicists' Hermite polynomials, $e^{2\xi z - z^2} = \sum_n H_n(\xi)z^n/n!$ |
| $\phi_n(x) = H_n(\sqrt\kappa\,x)e^{-\kappa x^2/2}$ | Hermite functions of scale $\kappa$ |

### 2.3 Problem restated, and how I read it

(a) Evaluate $I(x,x';\tau) = \int_0^\tau du\,\rho_0(x,x';\tau)^{-1}\int dy\,\rho_0(x,y;u)V(y)\rho_0(y,x';\tau-u)$ in closed form; then $w = \rho_0 e^{-I}$.

(b) With $\tau = \beta/m$, evaluate the closed-ring integrals $\hat Z_m$ (product of $w$) and $Z_m$ (product of $\rho_0(x_n,x_{n+1};\tau)e^{-\tau V(x_n)}$) by diagonalising their quadratic forms. Then find $\hat E_m$, $E_m$, tabulate at $\beta\in\{1,5,10\}$, $m\in\{1,10,50,100,500\}$, and compare with $U(\beta)$.

(c) Find the spectrum of $T_\tau$ for all $\tau>0$ and the small-$\tau$ expansion of $E_n(\tau) - (n+\tfrac12)$; do the same for $T^P_\tau$; relate (b) to (c) and check the relation.

Two points of reading need stating.

First, $E_n(\tau) = -\tau^{-1}\ln\lambda_n$ is a real number only when $\lambda_n > 0$. I find below that for $\tau>\sqrt6$ the odd-$n$ eigenvalues of $T_\tau$ are negative, and that at $\tau=\sqrt6$ all eigenvalues with $n\ge1$ vanish. For those cases the requested quantity is not defined as a real energy. I give the eigenvalues in closed form for every $\tau>0$ as asked, and I state what $-\tau^{-1}\ln\lambda_n$ becomes there (eq. (26)). I do not replace it with a nearby quantity.

Second, I label eigenvalues by the Hermite index $n$ of their eigenfunction. Because $|q|<1$ for all $\tau$, this is the same as ordering by decreasing $|\lambda_n|$.

The free kernel is the kernel of $e^{-tK}$, and I need this identification for the primitive operator of (c):

$$
\langle x|e^{-tK}|x'\rangle = \int\frac{dk}{2\pi}\,e^{ik(x-x')}e^{-tk^2/2} = (2\pi t)^{-1/2}e^{-(x-x')^2/2t} = \rho_0(x,x';t). \tag{0}
$$

`[D]` Plane waves $e^{ikx}$ are eigenfunctions of $K$ with eigenvalue $k^2/2$, and Fourier inversion gives the first equality. The second follows from the Gaussian integral (G) below with $p=t$ and $J = i(x-x')$. (G) holds for complex $J$ because both sides are entire in $J$ and agree for real $J$.

The one Gaussian integral used repeatedly is, for $p>0$,

$$
\int_{-\infty}^{\infty}dk\,e^{-pk^2/2 + Jk} = \sqrt{2\pi/p}\;e^{J^2/2p}, \tag{G}
$$

`[D]` This comes from writing $-pk^2/2+Jk = -\tfrac p2(k - J/p)^2 + J^2/2p$ and using $\int e^{-pt^2/2}dt = \sqrt{2\pi/p}$.

---

## 3. Derivation

### 3.1 Part (a): the slice weight

Fix $0<u<\tau$.

`[A1]` The $y$-integral is evaluated for $0<u<\tau$ strictly. It buys finite variances $u$ and $\tau-u$ in the two free kernels. The endpoints $u=0,\tau$ have measure zero in the $u$-integral, and I show below that the $y$-integral is a polynomial in $u$ that extends continuously to $[0,\tau]$, so nothing is lost. Without this restriction one of the kernels is a delta function and the formula must be read as a limit.

The product of the two free kernels is

$$
\rho_0(x,y;u)\rho_0(y,x';\tau-u) = \frac{1}{2\pi\sqrt{u(\tau-u)}}\exp\Big\{-\tfrac12\Big[\frac{(y-x)^2}{u} + \frac{(y-x')^2}{\tau-u}\Big]\Big\}. \tag{1}
$$

Expand the bracket in powers of $y$:

$$
\frac{(y-x)^2}{u} + \frac{(y-x')^2}{\tau-u} = y^2\Big(\frac1u + \frac1{\tau-u}\Big) - 2y\Big(\frac xu + \frac{x'}{\tau-u}\Big) + \frac{x^2}{u} + \frac{x'^2}{\tau-u}.
$$

The two coefficients are

$$
\frac1u+\frac1{\tau-u} = \frac{\tau}{u(\tau-u)} \equiv \frac1{\sigma^2},\qquad
\frac xu+\frac{x'}{\tau-u} = \frac{(\tau-u)x + ux'}{u(\tau-u)} = \frac{\bar y}{\sigma^2},
$$

with

$$
\sigma^2(u) = \frac{u(\tau-u)}{\tau},\qquad \bar y(u) = \frac{(\tau-u)x + ux'}{\tau} = x + \frac{u}{\tau}(x'-x).
$$

Completing the square in $y$:

$$
\frac{(y-x)^2}{u} + \frac{(y-x')^2}{\tau-u} = \frac{(y-\bar y)^2}{\sigma^2} + R,\qquad R = \frac{x^2}{u} + \frac{x'^2}{\tau-u} - \frac{\bar y^2}{\sigma^2}. \tag{2}
$$

`[D]` Now compute $R$. Over the common denominator $\tau u(\tau-u)$,

$$
\frac{x^2}{u} + \frac{x'^2}{\tau-u} = \frac{\tau(\tau-u)x^2 + \tau u\,x'^2}{\tau u(\tau-u)},\qquad
\frac{\bar y^2}{\sigma^2} = \frac{[(\tau-u)x+ux']^2}{\tau^2}\cdot\frac{\tau}{u(\tau-u)} = \frac{(\tau-u)^2x^2 + 2u(\tau-u)xx' + u^2x'^2}{\tau u(\tau-u)}.
$$

The numerator of the difference is

$$
x^2(\tau-u)[\tau-(\tau-u)] + x'^2u[\tau-u] - 2u(\tau-u)xx' = u(\tau-u)\,(x^2 - 2xx' + x'^2),
$$

so

$$
R = \frac{(x-x')^2}{\tau}. \tag{3}
$$

`[D]` Insert (2) and (3) into (1) and divide by $\rho_0(x,x';\tau) = (2\pi\tau)^{-1/2}e^{-(x-x')^2/2\tau}$. The factor $e^{-R/2} = e^{-(x-x')^2/2\tau}$ cancels, and the prefactors combine as $(2\pi\tau)^{1/2}/(2\pi\sqrt{u(\tau-u)}) = (2\pi\sigma^2)^{-1/2}$:

$$
p_u(y) \equiv \frac{\rho_0(x,y;u)\rho_0(y,x';\tau-u)}{\rho_0(x,x';\tau)} = \frac{1}{\sqrt{2\pi\sigma^2}}\exp\Big[-\frac{(y-\bar y)^2}{2\sigma^2}\Big]. \tag{4}
$$

This is a normalised Gaussian density in $y$ (the Brownian-bridge marginal). The $y$-integral is therefore

$$
\int dy\,p_u(y)\,\tfrac12 y^2 = \tfrac12\int dy\,p_u(y)\,(\bar y + (y-\bar y))^2 = \tfrac12\big[\bar y^2 + 2\bar y\cdot 0 + \sigma^2\big] = \tfrac12\big[\bar y(u)^2 + \sigma^2(u)\big]. \tag{5}
$$

`[D]` Here I used $\int p_u = 1$, $\int (y-\bar y)p_u = 0$ (odd integrand), and $\int(y-\bar y)^2p_u = \sigma^2$. The last follows from differentiating (G) twice in $J$ at $J=0$ with $p = 1/\sigma^2$.

Explicitly, (5) is the polynomial $[\tau^2x^2 - 2\tau u x^2 + u^2x^2 + 2\tau u xx' - 2u^2xx' + u^2x'^2 + \tau^2u - \tau u^2]/(2\tau^2)$, which is continuous on $[0,\tau]$, as promised in [A1].

The $u$-integrals. Substitute $s = u/\tau$, $du = \tau\,ds$:

$$
\int_0^\tau \bar y(u)^2\,du = \tau\int_0^1\big(x + s(x'-x)\big)^2ds = \tau\Big[x^2 + x(x'-x) + \tfrac13(x'-x)^2\Big] = \tau\Big[xx' + \tfrac13(x^2-2xx'+x'^2)\Big] = \frac{\tau}{3}\big(x^2+xx'+x'^2\big), \tag{6}
$$

$$
\int_0^\tau\sigma^2(u)\,du = \frac1\tau\int_0^\tau(\tau u - u^2)\,du = \frac1\tau\Big(\frac{\tau^3}{2} - \frac{\tau^3}{3}\Big) = \frac{\tau^2}{6}. \tag{7}
$$

Adding, with the factor $\tfrac12$ of (5):

$$
I(x,x';\tau) = \frac{\tau}{6}\big(x^2 + xx' + x'^2\big) + \frac{\tau^2}{12}. \tag{8}
$$

`[D]` Hence

$$
\boxed{\,w(x,x';\tau) = \frac{1}{\sqrt{2\pi\tau}}\exp\Big[-\frac{(x-x')^2}{2\tau} - \frac{\tau}{6}\big(x^2+xx'+x'^2\big) - \frac{\tau^2}{12}\Big]\,} \tag{9}
$$

For later use I collect the exponent of (9) by monomials:

$$
w = N\exp\Big[-\frac A2(x^2+x'^2) + Bxx'\Big],\qquad N = \frac{e^{-\tau^2/12}}{\sqrt{2\pi\tau}},\quad A = \frac1\tau + \frac\tau3,\quad B = \frac1\tau - \frac\tau6. \tag{10}
$$

The derivation of (10) from (9): the coefficient of $x^2$ in the exponent is $-1/(2\tau) - \tau/6 = -A/2$, and the coefficient of $xx'$ is $+1/\tau - \tau/6 = B$.

On the diagonal, $w(x,x;\tau) = (2\pi\tau)^{-1/2}e^{-\tau x^2/2 - \tau^2/12}$. That is the primitive weight $\rho_0 e^{-\tau V}$ times $e^{-\tau^2/12}$, the bridge-fluctuation average $\tfrac12\int_0^\tau\sigma^2du$. The cross term in (9) has the opposite sign to the kinetic cross term, and this is what produces the sign change found in (c).

Remark, not load-bearing. `[R]` By the Feynman–Kac formula the exact kernel is $\rho(x,x';\tau) = \rho_0\,\mathbb E_{\rm bridge}[e^{-\int_0^\tau V(y(u))du}]$, and $p_u$ of (4) is the bridge marginal. Jensen's inequality then gives $w \le \rho$ pointwise, hence $\hat Z_m \le Z_{\rm exact}$, and (Perron argument for nonnegative kernels) $\lambda_0(T_\tau) \le e^{-\tau/2}$, i.e. $E_0(\tau)\ge\tfrac12$. These are used only as self-checks (B4, C6).

### 3.2 Part (b): the closed-ring Gaussian integrals

Bridge product. By (9), with $x_{m+1}=x_1$,

$$
\prod_{n=1}^m w(x_n,x_{n+1};\tau) = (2\pi\tau)^{-m/2}e^{-m\tau^2/12}\,e^{-\hat S(x)},\quad
\hat S(x) = \sum_{n=1}^m\Big[\frac{(x_n-x_{n+1})^2}{2\tau} + \frac\tau6\big(x_n^2 + x_nx_{n+1} + x_{n+1}^2\big)\Big]. \tag{11}
$$

`[D]` With the cyclic shift $(Px)_n = x_{n+1}$ and the $m\times m$ identity matrix $\mathbf 1$, one has $x^{\rm T}Px = \sum_n x_nx_{n+1}$ and $x^{\rm T}(P+P^{\rm T})x = 2\sum_nx_nx_{n+1}$. Also $\sum_n x_{n+1}^2 = \sum_n x_n^2$ on the ring. Therefore

$$
\sum_n(x_n-x_{n+1})^2 = 2\sum_nx_n^2 - 2\sum_nx_nx_{n+1} = x^{\rm T}(2\mathbf 1 - P - P^{\rm T})x,
$$

$$
\sum_n\big(x_n^2+x_nx_{n+1}+x_{n+1}^2\big) = 2\sum_nx_n^2 + \sum_nx_nx_{n+1} = \tfrac12x^{\rm T}(4\mathbf 1 + P + P^{\rm T})x,
$$

and $\hat S = \tfrac12x^{\rm T}\hat Ax$ with

$$
\hat A = \frac1\tau\big(2\mathbf 1 - P - P^{\rm T}\big) + \frac\tau6\big(4\mathbf 1 + P + P^{\rm T}\big). \tag{12}
$$

The small rings need a separate look, because there $P$ and $P^{\rm T}$ are not distinct permutations.

- For $m=1$, $P = (1)$ and $P+P^{\rm T} = 2$. Then (12) gives $\hat A = \tau$, and indeed $\hat S = \tfrac\tau6\cdot3x_1^2 = \tfrac12\tau x_1^2$.
- For $m=2$, $P = P^{\rm T}$ is the swap. Then $x^{\rm T}(2\mathbf 1 - 2P)x = 2(x_1-x_2)^2$, which is the sum of the two bonds $(x_1-x_2)^2 + (x_2-x_1)^2$. Likewise $\tfrac12x^{\rm T}(4\mathbf 1+2P)x = 2(x_1^2+x_1x_2+x_2^2)$, which is the sum of the two potential bonds.

So (12) holds for every $m\ge1$. Check S3 confirms this symbolically for $m=1,\dots,7$, working from the action itself.

The integral is then

$$
\hat Z_m = (2\pi\tau)^{-m/2}e^{-m\tau^2/12}\int_{\mathbb R^m}d^mx\,e^{-\frac12x^{\rm T}\hat Ax} = (2\pi\tau)^{-m/2}e^{-m\tau^2/12}(2\pi)^{m/2}(\det\hat A)^{-1/2} = e^{-m\tau^2/12}\,\det(\tau\hat A)^{-1/2}. \tag{13}
$$

`[D]` The middle equality holds for real symmetric positive-definite $\hat A$ (positivity is shown below). Rotate $x = Oz$ with $O$ orthogonal so that $O^{\rm T}\hat AO = {\rm diag}(a_k)$. The Jacobian is 1, the integral factorises into $\prod_k\int dz_k\,e^{-a_kz_k^2/2} = \prod_k\sqrt{2\pi/a_k}$ by (G) with $J=0$, and $\prod_ka_k = \det\hat A$.

Diagonalisation. The vectors $v^{(k)}_n = m^{-1/2}e^{i\theta_kn}$, $\theta_k = 2\pi k/m$, $k=0,\dots,m-1$, satisfy $(Pv^{(k)})_n = v^{(k)}_{n+1} = e^{i\theta_k}v^{(k)}_n$. They do so also at $n=m$, because $e^{i\theta_k m} = 1$. So $Pv^{(k)} = e^{i\theta_k}v^{(k)}$ and $P^{\rm T}v^{(k)} = P^{-1}v^{(k)} = e^{-i\theta_k}v^{(k)}$, and the $m$ vectors are orthonormal (discrete Fourier basis). Hence

$$
\hat Av^{(k)} = a_kv^{(k)},\qquad \tau a_k = (2-2\cos\theta_k) + \frac{\tau^2}{6}(4 + 2\cos\theta_k) = \alpha - \gamma\cos\theta_k,\qquad \alpha = 2 + \frac{2\tau^2}{3},\ \gamma = 2 - \frac{\tau^2}{3}. \tag{14}
$$

The complex eigenvectors are an orthonormal eigenbasis of the real symmetric $\hat A$. A real orthogonal $O$ for (13) is obtained from the combinations $(v^{(k)} \pm v^{(m-k)})$, since $a_k = a_{m-k}$. The determinant is the same product either way:

$$
\det(\tau\hat A) = \prod_{k=0}^{m-1}(\alpha - \gamma\cos\theta_k). \tag{15}
$$

Positivity: $\alpha - \gamma = \tau^2 > 0$ and $\alpha+\gamma = 4 + \tau^2/3 > 0$, so $\alpha - \gamma\cos\theta \ge \alpha - |\gamma| > 0$ for all $\theta$. Hence $\hat A$ is positive definite, for every $\tau>0$.

Evaluating the product. Write each factor as $C(1 - 2z\cos\theta + z^2)$ with $C>0$ and $|z|<1$, because for that form a closed product is available (eq. (17)). Matching the constant and the $\cos\theta$ coefficient requires $C(1+z^2) = \alpha$ and $2Cz = \gamma$. Adding and subtracting:

$$
C(1+z)^2 = \alpha+\gamma = 4\Big(1+\frac{\tau^2}{12}\Big) = 4\kappa^2,\qquad C(1-z)^2 = \alpha-\gamma = \tau^2.
$$

`[D]` With $|z|<1$ both $1\pm z$ are positive, so the positive square roots give $\sqrt C(1+z) = 2\kappa$ and $\sqrt C(1-z) = \tau$. Adding and subtracting these,

$$
\sqrt C = \kappa + \frac\tau2 = s_+,\qquad z = \frac{\kappa - \tau/2}{\kappa+\tau/2} = \frac{s_-}{s_+}. \tag{16}
$$

This $z$ does satisfy $|z|<1$, because $\kappa>0$ and $\tau>0$ give $|\kappa - \tau/2| < \kappa+\tau/2$, so the choice is consistent. Note that $z$ changes sign at $\kappa = \tau/2$, i.e. $\tau^2 = 6$.

For real $z$, $1 - 2z\cos\theta_k + z^2 = (1-ze^{i\theta_k})(1-ze^{-i\theta_k})$. From $X^m - 1 = \prod_k(X - e^{i\theta_k})$ (the $e^{i\theta_k}$ are the $m$-th roots of unity), put $X = 1/z$ and multiply by $z^m$:

$$
\prod_{k=0}^{m-1}(1 - ze^{i\theta_k}) = 1 - z^m. \tag{17}
$$

`[D]` This holds for $z\ne0$, and for $z=0$ it is trivial. The set $\{e^{-i\theta_k}\}$ equals $\{e^{i\theta_k}\}$, so the conjugate product is also $1-z^m$. Therefore

$$
\det(\tau\hat A) = C^m(1-z^m)^2 = s_+^{2m}\Big(1 - \frac{s_-^m}{s_+^m}\Big)^2 = \big(s_+^m - s_-^m\big)^2 = D_m^2,
$$

and by (13), since $D_m>0$ (because $s_+^m > |s_-|^m$):

$$
\boxed{\,\hat Z_m(\beta) = \frac{e^{-m\tau^2/12}}{s_+^m - s_-^m} = \frac{e^{-\beta^2/12m}}{\big(\kappa+\frac\tau2\big)^m - \big(\kappa-\frac\tau2\big)^m},\qquad \kappa = \sqrt{1+\frac{\tau^2}{12}},\ \tau = \frac\beta m.\,} \tag{18}
$$

For $m=1$, $D_1 = \tau$ and $\hat Z_1 = e^{-\beta^2/12}/\beta$. Directly from (9), $\int w(x,x;\beta)dx = (2\pi\beta)^{-1/2}e^{-\beta^2/12}\sqrt{2\pi/\beta}$, which is the same.

Primitive product. $\prod_n\rho_0(x_n,x_{n+1};\tau)e^{-\tau V(x_n)} = (2\pi\tau)^{-m/2}e^{-\frac12x^{\rm T}A^Px}$ with

$$
A^P = \frac1\tau(2\mathbf 1 - P - P^{\rm T}) + \tau\mathbf 1,\qquad \tau a^P_k = 2 + \tau^2 - 2\cos\theta_k. \tag{19a}
$$

`[D]` Here $\alpha_P = 2+\tau^2$, $\gamma_P = 2$, $\alpha_P+\gamma_P = 4\kappa_P^2$, $\alpha_P - \gamma_P = \tau^2$, and the same steps (13)–(17) give $\sqrt{C_P} = s^P_+$, $z_P = s^P_-/s^P_+$. Because $s^P_+s^P_- = \kappa_P^2 - \tau^2/4 = 1$, one can write $s^P_\pm = e^{\pm\varphi/2}$ with $\sinh(\varphi/2) = \tau/2$. Then

$$
\boxed{\,Z_m(\beta) = \frac{1}{(s^P_+)^m - (s^P_-)^m} = \frac{1}{2\sinh\big(m\operatorname{arcsinh}(\beta/2m)\big)}.\,} \tag{19}
$$

Energies. $\partial_\beta = m^{-1}\partial_\tau$ at fixed $m$, and $ds_\pm/d\tau = \kappa'\pm\tfrac12$ with $\kappa' = \tau/(12\kappa)$. From (18), $\ln\hat Z_m = -\beta^2/(12m) - \ln D_m$, so

$$
\hat E_m = \frac{\beta}{6m} + \frac1m\frac{\partial_\tau D_m}{D_m} = \frac\tau6 + \frac{s_+^{m-1}\big(\kappa' + \frac12\big) - s_-^{m-1}\big(\kappa'-\frac12\big)}{s_+^m - s_-^m}. \tag{20}
$$

`[D]` The step uses $\partial_\tau D_m = m[s_+^{m-1}(\kappa'+\tfrac12) - s_-^{m-1}(\kappa'-\tfrac12)]$. The same steps applied to (19), with $\kappa_P' = \tau/(4\kappa_P)$, give

$$
E_m = \frac{(s^P_+)^{m-1}\big(\kappa_P'+\frac12\big) - (s^P_-)^{m-1}\big(\kappa_P'-\frac12\big)}{(s^P_+)^m - (s^P_-)^m} = \frac{\coth\big(m\operatorname{arcsinh}(\tau/2)\big)}{\sqrt{4+\tau^2}}. \tag{21}
$$

`[D]` The second form follows from $\partial_\beta[m\operatorname{arcsinh}(\beta/2m)] = \tfrac12(1+\tau^2/4)^{-1/2} = (4+\tau^2)^{-1/2}$.

Checks at $m=1$: (20) gives $\hat E_1 = \tau/6 + [(\kappa'+\tfrac12) - (\kappa'-\tfrac12)]/\tau = \beta/6 + 1/\beta$, which agrees with $-\partial_\beta\ln(e^{-\beta^2/12}/\beta)$. (21) gives $E_1 = \sqrt{4+\beta^2}/\beta\cdot(4+\beta^2)^{-1/2} = 1/\beta$, the classical result.

Table (closed forms (20), (21), evaluated with 30-digit arithmetic by `table.py`; printed verbatim from the round-2 re-run):

{{RAW:r2/out_table.txt}}

In all fifteen cases $\hat E_m > U > E_m$. For $m\ge50$ the two errors fall off as $m^{-2}$ with nearly equal magnitudes and opposite signs; at small $m$ they are unequal. At $m=1$ the bridge result is far off at low temperature ($\hat E_1 = \beta/6 + 1/\beta$), because of the $e^{-\tau^2/12}$ factor. The large-$m$ behaviour is derived in §3.4, eq. (31).

### 3.3 Part (c): spectra of $T_\tau$ and $T^P_\tau$

Both kernels have the form $N\exp[-\tfrac A2(x^2+x'^2) + Bxx']$. For $T_\tau$ the parameters are those of (10). For $T^P_\tau$, eq. (0) gives the kernel $e^{-\tau x^2/4}\rho_0(x,x';\tau)e^{-\tau x'^2/4}$, i.e. $N_P = (2\pi\tau)^{-1/2}$, $A_P = 1/\tau + \tau/2$, $B_P = 1/\tau$. In both cases $A>|B|$: $A - B = \tau/2$ for both, $A+B = 2/\tau+\tau/6$ (bridge), and $A_P+B_P = 2/\tau + \tau/2$.

Lemma (Gaussian kernel). Let $N>0$ and $A>|B|$, and set $\kappa_K = \sqrt{A^2-B^2}>0$ and $q_K = B/(A+\kappa_K)$. Then the kernel's operator $K$ satisfies $K\phi_n = \lambda_0q_K^n\phi_n$, with $\phi_n(x) = H_n(\sqrt{\kappa_K}x)e^{-\kappa_Kx^2/2}$ and $\lambda_0 = N\sqrt{2\pi/(A+\kappa_K)}$. These are all of its nonzero eigenvalues, each simple, and $|q_K|<1$.

Proof, route 2 (explicit eigenfunctions). Let $G(x;s) = \exp(-\kappa_Kx^2/2 + 2\sqrt{\kappa_K}sx - s^2)$. `[S]` By the Hermite generating function (DLMF 18.12.15, $e^{2\xi z - z^2} = \sum_nH_n(\xi)z^n/n!$, with $\xi = \sqrt{\kappa_K}x$ and $z = s$), $G(x;s) = \sum_n\phi_n(x)s^n/n!$, so $\phi_n(x) = \partial_s^nG(x;s)|_{s=0}$. Apply $K$ using (G) with $p = A+\kappa_K$ and $J = Bx + 2\sqrt{\kappa_K}s$:

$$
(KG)(x;s) = N\sqrt{\frac{2\pi}{A+\kappa_K}}\exp\Big[-\frac A2x^2 + \frac{(Bx+2\sqrt{\kappa_K}s)^2}{2(A+\kappa_K)} - s^2\Big].
$$

Collect the exponent term by term.

The $x^2$ coefficient is $-\tfrac12[A - B^2/(A+\kappa_K)] = -\tfrac12[A(A+\kappa_K) - (A^2-\kappa_K^2)]/(A+\kappa_K) = -\tfrac12\kappa_K(A+\kappa_K)/(A+\kappa_K) = -\kappa_K/2$.

The $sx$ term is $2\sqrt{\kappa_K}\,[B/(A+\kappa_K)]\,s\,x = 2\sqrt{\kappa_K}(q_Ks)x$.

The $s^2$ coefficient is $2\kappa_K/(A+\kappa_K) - 1 = -(A-\kappa_K)/(A+\kappa_K) = -(A-\kappa_K)(A+\kappa_K)/(A+\kappa_K)^2 = -B^2/(A+\kappa_K)^2 = -q_K^2$.

Hence

$$
(KG)(\cdot\,;s) = \lambda_0\,G(\cdot\,;q_Ks). \tag{22}
$$

`[A2]` Next, differentiate (22) $n$ times in $s$ at $s=0$, passing $\partial_s^n$ under the $x'$-integral on the left. This is justified because $s\mapsto K(x,x')G(x';s)$ is entire, and for $|s|\le r$ it is bounded by $|K(x,x')|\exp(-\kappa_Kx'^2/2 + 2\sqrt{\kappa_K}r|x'| + r^2)$, which is integrable in $x'$ (standard differentiation of holomorphic parameter integrals). If [A2] failed, route 2 would not establish $K\phi_n = \lambda_n\phi_n$, but route 1 below and checks C1, C2 do not use it. The result is $K\phi_n = \lambda_0q_K^n\phi_n$.

Completeness: `[S]` DLMF §18.18(i) states that every $f$ in $L^2(\mathbb R, e^{-\xi^2}d\xi)$ has a Hermite expansion (18.18.6)–(18.18.7) converging in the $L^2$ sense (citing Szegő, Theorems 3.1.5 and 5.7.1). The map $f(x)\mapsto g(\xi) = f(\xi/\sqrt{\kappa_K})e^{\xi^2/2}$ is a bijection of $L^2(\mathbb R,dx)$ onto that space, with $\int|g|^2e^{-\xi^2}d\xi = \sqrt{\kappa_K}\int|f|^2dx$. So $\{\phi_n\}$ is a complete orthogonal set in $L^2(\mathbb R)$. If $Kf = \mu f$ with $\mu\notin\{\lambda_0q_K^n\}$, then $(\lambda_0q_K^n - \mu)\langle\phi_n,f\rangle = \langle K\phi_n,f\rangle - \langle\phi_n,Kf\rangle = 0$ (since $K$ is symmetric), so $f\perp\phi_n$ for all $n$ and $f = 0$. Finally, $|q_K|<1$ because $A+\kappa_K > A > |B|$. $\square$

Route 1 (spectrum from (b), no ansatz). `[D]` with `[R]` operator facts. $T_\tau$ is Hilbert–Schmidt (square-integrable Gaussian kernel, $A>|B|$) and self-adjoint, hence compact. `[R]` For $m\ge2$, $T^m$ is trace class with $\operatorname{Tr}T^m = \sum_j\mu_j^m$ over all its eigenvalues $\mu_j$ counted with multiplicity, and $\operatorname{Tr}T^m = \int dx_1\cdots dx_m\prod w(x_n,x_{n+1})$ (trace of a product of Hilbert–Schmidt operators as an integral of kernels). The right side is $\hat Z_m$ of (18) at $\beta = m\tau$:

$$
\sum_j\mu_j^m = \frac{e^{-m\tau^2/12}}{s_+^m - s_-^m} = \frac{(e^{-\tau^2/12}/s_+)^m}{1-q^m} = \sum_{n\ge0}\big(e^{-\tau^2/12}s_+^{-1}q^n\big)^m,\qquad m\ge2.
$$

The generating function $F(\zeta) = \sum_{m\ge2}\zeta^m\sum_j\mu_j^m = \sum_j\mu_j^2\zeta^2/(1-\mu_j\zeta)$ is meromorphic, with a simple pole at each $\zeta = 1/\mu_j$ whose residue counts the multiplicity. So the nonzero spectrum with multiplicities is fixed by the power sums. It is $\{e^{-\tau^2/12}s_+^{-1}q^n\}_{n\ge0}$, each simple, which agrees with route 2. Route 1 rests on (b), and that derivation never used (c), so the agreement of the two routes is a non-trivial consistency check.

Application to $T_\tau$. From (10), $\kappa_K^2 = A^2 - B^2 = (A-B)(A+B) = \frac\tau2\big(\frac2\tau + \frac\tau6\big) = 1 + \frac{\tau^2}{12} = \kappa^2$. Next, $\tau(A+\kappa) = 1 + \tau^2/3 + \tau\kappa = (\kappa+\tau/2)^2$, using $(\kappa+\tau/2)^2 = \kappa^2+\tau\kappa+\tau^2/4 = 1 + \tau^2/3 + \tau\kappa$. Then

$$
\lambda_0 = \frac{e^{-\tau^2/12}}{\sqrt{2\pi\tau}}\sqrt{\frac{2\pi}{A+\kappa}} = \frac{e^{-\tau^2/12}}{\sqrt{\tau(A+\kappa)}} = \frac{e^{-\tau^2/12}}{\kappa+\tau/2},\qquad
q = \frac{\tau B}{\tau(A+\kappa)} = \frac{1-\tau^2/6}{(\kappa+\tau/2)^2} = \frac{\kappa-\tau/2}{\kappa+\tau/2},
$$

where the last step uses $(\kappa-\tau/2)(\kappa+\tau/2) = \kappa^2 - \tau^2/4 = 1-\tau^2/6$. So, for every $\tau>0$,

$$
\boxed{\,\lambda_n(\tau) = e^{-\tau^2/12}\,\frac{(\kappa - \tau/2)^n}{(\kappa+\tau/2)^{n+1}},\qquad \kappa = \sqrt{1+\tau^2/12},\quad n = 0,1,2,\dots\,} \tag{23}
$$

The eigenfunctions are $H_n(\kappa^{1/2}x)e^{-\kappa x^2/2}$: oscillator states of frequency $\kappa>1$.

Application to $T^P_\tau$. Here $\kappa_K^2 = (\tau/2)(2/\tau + \tau/2) = 1+\tau^2/4 = \kappa_P^2$ and $\tau(A_P+\kappa_P) = (\kappa_P+\tau/2)^2$. With $s^P_+s^P_- = 1$ this gives

$$
\boxed{\,\lambda^P_n(\tau) = \frac{(\kappa_P-\tau/2)^n}{(\kappa_P+\tau/2)^{n+1}} = e^{-(n+\frac12)\varphi},\qquad \varphi = 2\operatorname{arcsinh}(\tau/2).\,} \tag{24}
$$

Levels of $T_\tau$, regime $0<\tau<\sqrt6$ (where $s_->0$ and all $\lambda_n>0$). From (23),

$$
E_n(\tau) = \frac\tau{12} + \frac1\tau\big[(n+1)\ln s_+ - n\ln s_-\big] = \Big(n+\frac12\Big)\Omega(\tau) + \frac{\tau}{12} + \frac{\ln(1-\tau^2/6)}{2\tau},\qquad \Omega(\tau) = \frac1\tau\ln\frac{s_+}{s_-} = \frac2\tau\operatorname{artanh}\frac{\tau}{2\kappa}. \tag{25}
$$

`[D]` The second form uses $\ln s_+ = \tfrac12\ln(s_+/s_-) + \tfrac12\ln(s_+s_-)$, $\ln s_- = -\tfrac12\ln(s_+/s_-) + \tfrac12\ln(s_+s_-)$, and $s_+s_- = 1-\tau^2/6$. Then $(n+1)\ln s_+ - n\ln s_- = (n+\tfrac12)\ln(s_+/s_-) + \tfrac12\ln(1-\tau^2/6)$. The artanh form follows from $\ln\frac{1+r}{1-r} = 2\operatorname{artanh}r$ with $r = \tau/(2\kappa)$. Check S6 confirms the equivalence of the two forms at three $\tau$ values.

Regimes $\tau\ge\sqrt6$. `[D]`
- At $\tau=\sqrt6$, $B=0$: $w$ is the separable kernel $N e^{-A(x^2+x'^2)/2}$ of rank one. Its only nonzero eigenvalue is $\lambda_0 = e^{-1/2}/(\kappa+\tau/2)$ with $\kappa = \sqrt{3/2}$ (this agrees with (23)), and $\lambda_n = 0$ for $n\ge1$.
- For $\tau>\sqrt6$, $s_-<0$, so $q<0$ and $\operatorname{sign}\lambda_n = (-1)^n$. As $\tau\to\infty$, $q\to(1/\sqrt{12} - 1/2)/(1/\sqrt{12}+1/2) = -(2-\sqrt3)$. Hence

$$
E_n(\tau) = \frac\tau{12} + \frac1\tau\big[(n+1)\ln s_+ - n\ln|s_-|\big] + \begin{cases}0, & n \text{ even}\\ -i\pi/\tau \ (\text{principal log}), & n\text{ odd}\end{cases}\qquad(\tau>\sqrt6), \tag{26}
$$

and $E_n(\sqrt6) = +\infty$ for $n\ge1$. For odd $n$ and $\tau>\sqrt6$ the requested real energy does not exist; $T_\tau$ is not a positive operator there, so it is not $e^{-\tau h}$ for any self-adjoint $h$. This is a property of the approximant, not an artefact: the grid diagonalisation C1 shows the sign pattern $+-+-\cdots$ directly from the kernel (9).

Small-$\tau$ expansion, bridge. `[D]` By hand to the leading terms:
- $\kappa^{-1} = 1 - \tau^2/24 + O(\tau^4)$, so $r = \tau/(2\kappa) = \tau/2 - \tau^3/48 + O(\tau^5)$.
- $\operatorname{artanh}r = r + r^3/3 + O(r^5) = \tau/2 - \tau^3/48 + \tau^3/24 + O(\tau^5) = \tau/2 + \tau^3/48 + O(\tau^5)$, so $\Omega = 1 + \tau^2/24 + O(\tau^4)$.
- $\ln(1-\tau^2/6) = -\tau^2/6 - \tau^4/72 + O(\tau^6)$, so $\tau/12 + \ln(1-\tau^2/6)/(2\tau) = -\tau^3/144 + O(\tau^5)$.

Then (25) gives

$$
\boxed{\,E_n(\tau) - \Big(n+\frac12\Big) = \frac{2n+1}{48}\tau^2 - \frac{\tau^3}{144} + \frac{3(2n+1)}{1280}\tau^4 - \frac{\tau^5}{1296} + \frac{103(2n+1)}{387072}\tau^6 + O(\tau^7).\,} \tag{27}
$$

The terms beyond $\tau^3$ come from the symbolic series of (25) (check S6, `[N]`). The odd terms are $n$-independent: they come entirely from the shift $\tau/12 + \ln(1-\tau^2/6)/2\tau$, whose expansion is odd in $\tau$, while $(n+\tfrac12)\Omega$ is even in $\tau$. The ground state is pushed up, consistent with $E_0\ge\tfrac12$ from the Jensen–Perron remark.

Levels of $T^P_\tau$, all $\tau>0$. From (24), $E^P_n(\tau) = (n+\tfrac12)\Omega_P(\tau)$ with $\Omega_P = \varphi/\tau = (2/\tau)\operatorname{arcsinh}(\tau/2)$. Since $\frac{d}{dy}\operatorname{arcsinh}y = (1+y^2)^{-1/2} = 1 - y^2/2 + 3y^4/8 - \dots$, one has $\operatorname{arcsinh}y = y - y^3/6 + 3y^5/40 - \dots$, and

$$
\boxed{\,E^P_n(\tau) - \Big(n+\frac12\Big) = -\frac{2n+1}{48}\tau^2 + \frac{3(2n+1)}{1280}\tau^4 - \frac{5(2n+1)}{14336}\tau^6 + O(\tau^8).\,} \tag{28}
$$

`[D]` The first two terms are by hand, the $\tau^6$ term from check S6.

The two approximants make equal and opposite errors at order $\tau^2$, and identical errors at order $\tau^4$. Their arithmetic mean has error $-\tau^3/288 + 3(2n+1)\tau^4/1280 + O(\tau^5)$, so the $n$-dependence of the mean first enters at order $\tau^4$. All expansions are at fixed $n$. Their coefficients grow linearly in $n$, so they describe the levels only for $n\tau^2\ll1$. At fixed $\tau$, $E_n/(n+\tfrac12)\to\Omega(\tau)\ne1$ as $n\to\infty$.

### 3.4 Relation between (b) and (c), and the energies

`[D]` The $m$-fold integral in $\hat Z_m$ is the trace of the $m$-fold composition of the kernel:

$$
\hat Z_m(\beta) = \operatorname{Tr}T_{\beta/m}^m = \sum_{n\ge0}\lambda_n(\beta/m)^m,\qquad Z_m(\beta) = \operatorname{Tr}(T^P_{\beta/m})^m = \sum_{n\ge0}\lambda^P_n(\beta/m)^m. \tag{29}
$$

For $Z_m$ I used that on a closed ring $\sum_nV(x_n) = \sum_n\tfrac12[V(x_n)+V(x_{n+1})]$, so the asymmetric product of (b) equals the product of the symmetric kernels of $T^P$. Algebraically, $\sum_n\lambda_0^mq^{nm} = \lambda_0^m/(1-q^m) = e^{-m\tau^2/12}s_+^{-m}/(1-s_-^m/s_+^m) = e^{-m\tau^2/12}/(s_+^m-s_-^m)$, which is (18) term by term. This holds also for $q<0$, i.e. for $\tau>\sqrt6$: the alternating eigenvalues still sum to a positive $\hat Z_m$. For $m=1$, (29) is checked directly: $\lambda_0/(1-q) = e^{-\tau^2/12}/(s_+-s_-) = e^{-\tau^2/12}/\tau = \int w(x,x;\tau)dx$.

The thermodynamic energy is not the Boltzmann average of $E_n(\tau)$, because the levels themselves depend on $\beta$ through $\tau = \beta/m$. Differentiating (29),

$$
\hat E_m = \frac{\sum_n\varepsilon_n(\tau)\lambda_n^m}{\sum_n\lambda_n^m},\qquad \varepsilon_n(\tau) = -\frac{d\ln|\lambda_n|}{d\tau} = \frac{d}{d\tau}\big[\tau E_n(\tau)\big]\ (\tau<\sqrt6),\qquad \tau = \frac\beta m. \tag{30}
$$

At fixed $\tau$ and $\beta\to\infty$ this gives $\hat E_m\to\varepsilon_0(\tau)$, not $E_0(\tau)$; the same holds for $E_m$.

Large-$m$ asymptotics. `[D]` + `[A3]`. From (25), $\tau E_n = (n+\tfrac12)(\tau + \tau^3/24) - \tau^4/144 + O(\tau^5)$, so $\varepsilon_n = (n+\tfrac12)(1+\tau^2/8) - \tau^3/36 + O(\tau^4)$. In $\lambda_n^m = e^{-\beta E_n}$, the $n$-independent $\tau^3$ term cancels between numerator and denominator of (30). What remains are the weights of the exact oscillator at $\beta' = \beta(1+\tau^2/24)$, up to $O(\tau^4)$. `[A3]` I expand in $\tau$ inside the sum over $n$; the sum is dominated by geometric weights $e^{-\beta n}$, and this is checked numerically in B6. Using $\langle n+\tfrac12\rangle_{\beta'} = U(\beta') = U + \beta\tau^2U'/24 + O(\tau^4)$:

$$
\hat E_m = U + \frac{\beta^2}{m^2}\Big[\frac U8 + \frac{\beta U'}{24}\Big] - \frac{\beta^3}{36m^3} + O(m^{-4}),\qquad
E_m = U - \frac{\beta^2}{m^2}\Big[\frac U8 + \frac{\beta U'}{24}\Big] + O(m^{-4}), \tag{31}
$$

with $U' = -\tfrac14\operatorname{csch}^2(\beta/2)$. For example, at $\beta=10$, $m=500$: (31) gives $\hat E_m - U \approx 2.4995\times10^{-5} - 2.2\times10^{-7} = 2.477\times10^{-5}$, against $2.4774\times10^{-5}$ in the table.

---

## 4. Verification

### 4.1 Self-check battery

1. Dimensions. With units restored, $\tau(x^2+xx'+x'^2)/6\to M\omega^2\tau_{\rm ph}(x^2+xx'+x'^2)/6\hbar$ and $\tau^2/12\to\omega^2\tau_{\rm ph}^2/12$; both are dimensionless. $w$ carries $[{\rm length}]^{-1}$, like $\rho_0$, so $T_\tau$ is dimensionless and the $\lambda_n$ are pure numbers. $E_n$, $\hat E_m$, $E_m$ are in units of $\hbar\omega$. All displayed results respect this. Pass.
2. Limits.
   - $\tau\to0$: $E_n,E^P_n\to n+\tfrac12$ by (27), (28).
   - $m\to\infty$ at fixed $\beta$: $\hat E_m,E_m\to U$ (table, (31), B6).
   - $\beta\to0$ at fixed $m$: $D_m\approx m\tau$, so $\hat Z_m\approx1/\beta$ and $Z_m\approx 1/\beta$, the classical limit; the energies $\to1/\beta$.
   - $\beta\to\infty$ at fixed $m$: $\tau\to\infty$, $\hat E_m\to\varepsilon_0(\tau)\sim\tau/6\to\infty$, and $E_m\to(4+\tau^2)^{-1/2}\to0$. Both approximants fail when the slice length diverges, as expected.
   - $|x|,|x'|\to\infty$: $w$ decays as a Gaussian, and $w\le\rho_0$ because $I\ge0$ ($x^2+xx'+x'^2\ge0$).
   - $\tau\to\infty$ in (c): $q\to-(2-\sqrt3)$ and $E_0\sim\tau/12$.

   Pass.
3. Reduction to known cases. Setting $V\to0$ in the definition gives $w\to\rho_0$ trivially. The primitive results reduce to the recalled time-sliced oscillator formula (19). $m=1$ reduces to the explicit one-dimensional integrals ($\hat Z_1 = e^{-\beta^2/12}/\beta$, $Z_1 = 1/\beta$). The rank-one case $\tau=\sqrt6$ is computed directly. Pass.
4. Symmetries.
   - $w(x,x') = w(x',x)$, so $T_\tau$ is self-adjoint.
   - $w(-x,-x') = w(x,x')$, so the eigenfunctions have definite parity $(-1)^n$, as the $H_n$ do.
   - $u\leftrightarrow\tau-u$ with $x\leftrightarrow x'$ maps $\bar y\to\bar y$ and $\sigma^2\to\sigma^2$, and (8) is symmetric.
   - Ring translation and reflection give $a_k = a_{m-k}$ in (14).

   Pass.
5. Signs. $\hat Z_m\le Z_{\rm exact}\le Z_m$ at all 15 points (B4), as required by Jensen ($w\le\rho$) and by $\operatorname{arcsinh}y\le y$. $E_0(\tau)\ge\tfrac12$ on 400 values of $\tau$ (C6). The sign alternation of $\lambda_n$ for $\tau>\sqrt6$ is seen in the grid spectrum (C1). Pass.
6. Order of magnitude. A C–C stretch ($\hbar\omega\approx0.12$ eV) at 300 K has $\beta\approx4.6$; an O–H stretch ($\approx0.45$ eV) has $\beta\approx17$. At $\beta=10$ ($U\approx\tfrac12$, $U'\approx0$), a relative accuracy of $10^{-3}$ in the energy requires $\beta^2/(8m^2)\lesssim10^{-3}$ by (31), i.e. $m\gtrsim110$. That agrees with the table ($m=100$: error $6\times10^{-4}$) and with typical slice numbers in path-integral simulations of stiff modes. Pass.
7. Boundary conditions. Periodicity $x_{m+1}=x_1$ enters through the cyclic $P$. It is verified for the smallest rings $m=1,2$ explicitly and symbolically for $m\le7$ (S3, S4). The eigenfunctions are in $L^2$ since $\kappa>0$. The inner integral (5) tends to $V(x)$ as $u\to0$ and to $V(x')$ as $u\to\tau$, as the delta-function limit of the free kernels requires. Pass.
8. Degenerate cases and limit exchanges.
   - $\ln s_-$ in (25) is singular at $\tau=\sqrt6$; that case is treated separately (26).
   - $D_m>0$ for all $\tau>0$ and $m\ge1$, so (18) and (20) never divide by zero. For $m=1$, $s_\pm^{m-1}=1$.
   - In (a), the division by $u(\tau-u)$ is only at the measure-zero endpoints [A1].
   - The exchanges are: [A2] differentiation under the integral in route 2 (bypassed by route 1 and by checks C1, C2); [A3] the small-$\tau$ expansion inside $\sum_n$ for (31) (checked by B6).
   - In (b) there is no exchange: the Gaussian integral is evaluated exactly.

   Pass, with [A2] and [A3] recorded in the risk register.

### 4.2 Run log (all runs, including failures)

Round 2. Every script was re-run on 2026-11-13, in a fresh folder and from a clean interpreter. That includes the superseded round-1 versions, so the failures described below are reproduced rather than quoted. Two superseded versions of `check_c.py` and one of `check_b.py` had been edited in place in round 1 and not kept. I rebuilt them by reverse-applying the exact round-1 edits to the final scripts (`reconstruct_superseded.py`, below).

The rebuilds are validated by their outputs. `validate_reruns.py` finds every round-2 output identical to the round-1 record, after dropping the shell timing lines and the absolute path in two warning lines. That would not hold if a rebuild differed in any line that affects output.

The code of all final checks is unchanged from round 1. Some outputs below end with shell timing lines (`real`, `user`, `sys`), because those scripts were run as `(time python3 -I script.py) > out.txt 2>&1`; the others were run without `time`.

| Script (round 2) | Outcome |
|---|---|
| `check_algebra.py` | all differences 0; identical to round 1 |
| `check_a.py` (final) | 0 FAIL; identical to round 1 |
| `check_a_run1.py`, `check_a_run2.py` (superseded, kept since round 1) | 5 FAIL and 1 FAIL, reproducing round 1 |
| `dbg_a.py`, `dbg_a2.py` (round-1 diagnostics; only the name of the file they read changed) | identical to round 1 |
| `check_c.py` (final) | 0 FAIL; identical to round 1 |
| `check_c_run0.py`, `check_c_run1.py` (rebuilt) | 0 FAIL (no C5 criterion yet) and 2 FAIL, reproducing round 1 |
| `check_b.py` (final), `check_b_run1.py` (rebuilt) | 0 FAIL; the rebuild reproduces the two round-1 warnings |
| `table.py` | identical to round 1 |
| `check_p1.py` (new, presentation, §4.3) | run 0: false positives from a regex bug; run 1: answer-1 has 8 hits, answer-2 has 0 hits and compiles with 0 errors |
| `reconstruct_superseded.py`, `validate_reruns.py` (new, bookkeeping) | validator run 0, made while `check_a_run2.py` was still running: 3 mismatches. One was the unfinished output. Two were the diagnostic outputs, compared against empty records because the extraction skipped to the wrong fence; the comparison could only fail, never pass vacuously. Fixed the extraction, and an empty side now never counts as a match. Run 1: 0 mismatches |

```python
{{CODE:r2/reconstruct_superseded.py}}
```

Its output, verbatim: `reconstructed: check_c_run0.py, check_c_run1.py, check_b_run1.py`.

```python
{{CODE:r2/validate_reruns.py}}
```

Output of `validate_reruns.py` (verbatim):

{{OUT:r2/out_validate.txt}}

The superseded validator (`validate_reruns_run0.py`) differs from the final one as follows (`diff validate_reruns_run0.py validate_reruns.py`):

{{OUT:r2/diff_validate.txt}}

Re-run after all outputs existed, it reports only the two spurious diagnostic mismatches. Its first execution had also counted the then-unfinished `out_a_run2.txt`. Last lines, verbatim:

{{OUT:r2/out_validate_run0_tail.txt}}

Round-1 history. The rest of this subsection is the round-1 account. It is unchanged, except that each output shown is now the round-2 re-run of the corresponding script.

| Script | Runs | Outcome |
|---|---|---|
| `scratch.py` (informal series of (25), (28) before S6 existed) | 1 | same coefficients as S6; not otherwise used |
| `check_algebra.py` | 1 | all differences 0 |
| `check_a.py` | 4 | run 0 crashed; run 1: 5 FAIL; run 2: 1 FAIL; run 3: 0 FAIL (details below) |
| two throw-away diagnostic scripts for the run-1 failure of `check_a.py` | 2 | located the cause (below) |
| `check_c.py` | 3 | run 0: C5 had no pass/fail criterion (qualitative), 0 FAIL elsewhere; run 1: criterion added, 2 FAIL in C5 (tolerance); run 2: 0 FAIL |
| `check_b.py` | 2 | run 1: numerically identical, but printed two `log(0)` warnings; run 2: no warnings |
| `table.py` | 1 | table above |

In every revision below I changed a check, never the derivation. I state what failed and why the change does not make the check weaker at detecting the error it was built for.

`check_a.py`, run 0. The first version located the peak of the $y$-integrand with `mp.findroot` (default solver). It raised, at the first point, verbatim: `ValueError: Could not find root within given tolerance. (3.66903531456823378591985146146897574105138e-38 > 1.83670992315982423120115083940975887159166e-40)`. The cause: for small $u$ the derivative is $O(1/u)$ and an absolute residual test is meaningless. Change: secant solver with `verify=False`. The peak location only sets quadrature breakpoints. It cannot bias the value of the integral; a misplaced peak would show up as a large quadrature error estimate, which run 2 onward records.

`check_a.py`, run 1. Five of thirteen points failed, all with relative error $\approx3.5\times10^{-8}$, and all at large $(x-x')^2/\tau$. Verbatim output:

{{OUT:r2/out_a_run1.txt}}

A diagnostic (two short scripts) showed three things. They were deleted after round 1. For round 2 they were re-created verbatim from the round-1 record, except that the file they read is now named `check_a_run1.py`, and re-run.

```python
{{CODE:r2/dbg_a.py}}
```

{{OUT:r2/out_dbg_a.txt}}

```python
{{CODE:r2/dbg_a2.py}}
```

{{OUT:r2/out_dbg_a2.txt}}

These diagnostics compare against $\bar y$, $\sigma^2$ from the derivation; they were used only to locate the fault, not as verification. The diagnosis: the peak location and width were correct to $10^{-31}$. The inner integral was low by $3.6\times10^{-8}$ relative at every $u$. mpmath's own error estimate for the inner integral was $5.8\times10^{-4}$ relative. The integrand was $\sim e^{-(x-x')^2/2\tau}$ (e.g. $e^{-8000}$), and tanh-sinh's stopping test is absolute, so it stopped at low degree. Change (run 2): divide by the constant $\rho_0(x,x';\tau)$ inside the $y$-integral, so that the integrand is $O(1)$. This is mathematically identical to the definition. I also record mpmath's error estimates and fail the point if they exceed tolerance.

`check_a.py`, run 2. All thirteen values agreed with the closed form to $\sim10^{-31}$, but point $(0,0,1)$ was flagged by the new criterion (quad\_y $=6.8\times10^{-7}$). Verbatim output:

{{OUT:r2/out_a_run2.txt}}

Cause: I had used the relative error estimate of each inner integral. At $x=x'=0$ the inner value is $\sigma^2/2\to0$ as $u\to0$, so an absolute estimate of $\sim10^{-37}$ became large in relative terms. Change (run 3): the criterion now bounds the contribution of inner-integral errors to $I$, namely $\tau\max|{\rm err}_y|/I$. A non-convergence of run 1's kind (inner relative error $\sim6\times10^{-4}$ on values of order one, now that the integrand is scaled) would give $\sim10^{-3}$ here and would still be flagged. The code changes are shown verbatim below. For run 0 the single changed line was `ystar = mp.findroot(dg, (x + xp)/2)` (default solver, default verification), which became the secant call visible in the final code. Diff of the run-1 script against the final script (`diff check_a_run1.py check_a.py`):

{{OUT:r2/diff_a_run1_vs_final.txt}}

Diff of the run-2 script against the final script (`diff check_a_run2.py check_a.py`):

{{OUT:r2/diff_a_run2_vs_final.txt}}

`check_c.py`, run 0. In the first version C5 printed $R_n$, $P_n$ next to a prediction truncated at $O(\tau^2)$ (bridge) and $O(1)$ (primitive), with no failure criterion. Because a check that cannot fail is worth little, I added a quantitative criterion before run 1. That made the check stricter, not looser. The run-0 C5 and C6 lines, verbatim from the round-2 re-run of the rebuilt `check_c_run0.py`. Its C1–C4 lines are identical to the final run's, as `validate_reruns.py` confirms:

{{OUT:r2/out_c_run0_C5.txt}}

`check_c.py`, run 1. C5 failed at $\tau=0.4$, primitive, $n=2,3$ ($d = 7.4\times10^{-6}$, $1.0\times10^{-5}$ against a tolerance of $5\times10^{-6}$). The predictions then stopped at the leading omitted order. The omitted remainder visibly scales as $\tau^4$ ($1.0\times10^{-5}\to6.6\times10^{-7}\to4.3\times10^{-8}$ for $n=3$ as $\tau$ halves), and its size matches the next series term $35(2n+1)\tau^4/589824 = 1.06\times10^{-5}$ at $n=3$, $\tau=0.4$. Change (run 2): add the next analytic series terms of the closed form to the prediction, keeping the tolerance. The run-1 prediction lines were `pred = -1/144 + 3*(2*nn + 1)*t/1280 - t*t/1296 + 103*(2*nn + 1)*t**3/387072` and `predP = 3*(2*nn + 1)/1280 - 5*(2*nn + 1)*t*t/14336`; the final ones are in the listing below. The run-1 script was edited in place in round 1; it was rebuilt for round 2 as `check_c_run1.py`. The coefficients under test ($\tau^2$, $\tau^3$, $\tau^4$) were unchanged. The run-1 C5 and C6 lines, verbatim from the round-2 re-run of `check_c_run1.py`. Its full output is identical to the round-1 record, as `validate_reruns.py` confirms:

{{OUT:r2/out_c_run1_C5.txt}}

`check_b.py`, run 1. It printed two `RuntimeWarning: divide by zero encountered in log` lines. The source was the row $2e_i$ of the polarisation matrix, where $w$ underflows to 0 at $\tau=0.002$. That row is overwritten by the diagonal formula and never used. Run 2 sets that row to $e_i$; all printed numbers are identical between the runs. Verbatim `diff out_b_run1.txt out_b.txt` for the round-2 re-runs of `check_b_run1.py` (rebuilt) and `check_b.py`; the final script was run under `time`, so its timing lines also appear:

{{OUT:r2/diff_b.txt}}

### 4.3 Checks, code and output

Assumptions used by the checks, restated as `[A]`. [A1] ($0<u<\tau$) is encoded in S1 by declaring $u,v>0$ with $\tau = u+v$. No other positivity or branch assumption is passed to sympy except `positive=True` on $u,\tau,v$ and `real=True` on $x,x',y$; both are true in the problem. The principal branch of `log` appears only in `check_b.py`, applied to $w$ at real or nearly real (complex-step, $10^{-30}$) arguments, where $w>0$. Grid checks use the trapezoid (Nyström) rule on $[-L,L]$, $L = 10$ or $12$. This is legitimate because the kernels and the low eigenfunctions are Gaussian-decaying, so the truncation and discretisation errors are far below tolerance. Grid refinement by a factor two is reported in C1.

#### S1–S6: `check_algebra.py`

What it tests.
- S1 recomputes $I$ from the definition with sympy's own Gaussian integration, with no completion of the square supplied by hand; this is the strongest check on (8).
- S2 checks my completion of the square (algebra only).
- S3 and S4 build the $m\times m$ Hessian of the actual ring action for $m=1..7$ and compare $\det(\tau A)$ with $D_m^2$. This tests the circulant diagonalisation, the product formula and the small-ring cases.
- S5 checks the parameter identities behind (23) and (24).
- S6 produces the series (27), (28) and checks the equivalence of the two forms of (25).

What it would catch: any error in the $y$- or $u$-integrals (S1); a wrong eigenvalue, a wrong product identity or a wrong treatment of $m=1,2$ (S3, S4); algebra slips in $\kappa$, $s_\pm$, $q$ (S5); wrong series coefficients (S6).

What it would not catch. S2, S5 and S6 test my algebra, not the physics: they take my intermediate expressions as input. S3 and S4 take $w$ from (9) as input, so an error in (9) would propagate into them unnoticed (that is covered by S1 and `check_a.py`). S6 expands my closed form (25), so it cannot detect an error in (25) itself (C1, C5 do). S1 relies on sympy's integrator being right, which `check_a.py` covers independently.

```python
{{CODE:r2/check_algebra.py}}
```

Output (verbatim, round-2 re-run):

{{OUT:r2/out_algebra.txt}}

#### A: `check_a.py` — $w$ against direct numerical evaluation of its definition `[N]`

What it tests. At 13 points ($8$ random with seed 20261112, plus $(0,0,1)$; widely separated endpoints at small $\tau$, $(2,-2,10^{-3})$; large $\tau=20$; $\tau=5$ with $x=-4$, $x'=3$; and $\tau=\sqrt6$), it computes $I$ by nested 30-digit tanh-sinh quadrature of the definition. The $y$-breakpoints are found numerically from the integrand, so the check does not import $\bar y$ or $\sigma^2$. It compares the result with (8). Failure: relative difference $>10^{-12}$, or mpmath error estimates above that level. It also reports the discrepancy of four wrong candidate formulas (primitive symmetric split, missing $\tau^2/12$, doubled cross term, $\tau^2/6$) against the same numerics, to show the check discriminates.

What it would catch: any error in (8) or (9) larger than $10^{-12}$ relative at these points, including wrong coefficients of $x^2$, $xx'$, $x'^2$ or of the constant, since the points vary all of these.

What it would not catch: an error that vanishes at all 13 points (implausible for a polynomial in $x,x'$ with $\tau$-dependent coefficients, but not excluded). It also would not catch a misreading of the problem's definition shared between the code and the derivation; the code transcribes the definition literally, as written in the prompt.

```python
{{CODE:r2/check_a.py}}
```

Output (verbatim, round-2 re-run of the final script):

{{OUT:r2/out_a.txt}}

#### C: `check_c.py` — spectra `[N]`

What it tests.
- C1 diagonalises the kernels (9) and $e^{-\tau x^2/4}\rho_0e^{-\tau x'^2/4}$ on uniform grids at nine $\tau$ values, including $\tau>\sqrt6$ and $\tau=\sqrt6$. It compares the eight largest-magnitude eigenvalues, with signs, against (23) and (24), at grid spacing $h$ and $h/2$. Failure: error $>10^{-10}\lambda_0$.
- C2 rebuilds the kernel from the claimed $\lambda_0$, $q$, $\kappa$ via Mehler's formula (DLMF 18.18.28). This is an analytic identity independent of the grid and of the generating-function argument. It also does an explicit 60-term spectral sum at $\tau=5$, where $q<0$.
- C3 compares $\iint w^2$ on a grid with $\sum\lambda_n^2$; agreement means no eigenvalue is missing.
- C4 tests relation (29): $\operatorname{Tr}(hW)^m$ on the grid against the closed forms (18), (19), at nine $(\beta,m)$ pairs, including odd $m$ with $\tau>\sqrt6$.
- C5 extracts the small-$\tau$ coefficients of (27), (28) from grid eigenvalues alone.
- C6 checks $E_0\ge\tfrac12$.

What it would catch: any wrong eigenvalue, sign or degeneracy among the first eight levels; a missing part of the spectrum (C3); a wrong relation between (b) and (c) (C4); wrong leading series coefficients, including their $n$-dependence (C5).

What it would not catch: errors in (9) itself, since the grid uses the closed form of (a) (covered by `check_a.py` and S1). Nor eigenvalues beyond the first eight in C1; the higher ones are covered collectively by C2 and C3. C2 uses the norm $\|H_n\|^2 = 2^nn!\sqrt\pi$ only in the explicit 60-term sum, and that norm is `[R]` (not retrieved); a wrong norm would make that line fail rather than pass.

```python
{{CODE:r2/check_c.py}}
```

Output (verbatim, round-2 re-run of the final script):

{{OUT:r2/out_c.txt}}

#### B: `check_b.py` — partition functions and energies `[N]`

What it tests.
- B1 prints the closed forms and compares the two forms of (21).
- B2 is the second route: for each of the 15 $(\beta,m)$ it builds the $m\times m$ Hessian of the action numerically, by polarisation of $S(x) = -\sum\ln w(x_n,x_{n+1})$, and its $\beta$-derivative by complex-step differentiation. It then evaluates the Gaussian integral and $\hat E_m = \partial_\beta S(0) + \tfrac12\operatorname{tr}(H^{-1}\partial_\beta H)$ with LAPACK. It uses no circulant algebra, no product formula and no analytic derivative. Failure: $|\Delta E|$ or $|\Delta\ln Z|>10^{-8}$.
- B3 checks the analytic derivative (20), (21) against mpmath's numerical derivative of (18), (19).
- B4 checks the two bounds.
- B5 recomputes $\hat Z_m$, $\hat E_m$ from the spectrum (23) via (29), (30).
- B6 tests (31): $m^2\times$ (residual after the $m^{-2}$ and $m^{-3}$ terms) must stay bounded as $m$ doubles.

What it would catch: errors in (12)–(21) (B2, B3), in the relation (29), (30) (B5), or in the asymptotic coefficients (31) (B6).

What it would not catch: errors in (9) (B2 starts from (9); covered by A and S1). B2's accuracy at $\beta=1$, $m=500$ ($6.3\times10^{-9}$ bridge, $8.2\times10^{-9}$ primitive) is limited by the conditioning of $H$ (eigenvalues from $\tau=0.002$ to $4/\tau$). This is adequate for six-decimal claims but would not resolve errors below $10^{-8}$. B6 is a statement about the closed form's asymptotics, not an independent computation of $\hat E_m$.

```python
{{CODE:r2/check_b.py}}
```

Output (verbatim, round-2 re-run of the final script):

{{OUT:r2/out_b.txt}}

#### Table script: `table.py`

```python
{{CODE:r2/table.py}}
```

#### P1: `check_p1.py` — the math under the house LaTeX template `[N]` (new in round 2)

What it tests.

- P1a scans the markdown for every `\mathbb` whose argument is not a single uppercase letter, with fenced code blocks and inline code spans removed first. `amsfonts.sty` declares `\mathbb` as the alphabet of the AMSb (msbm) symbol font, and that font has double-struck glyphs only in the uppercase-letter slots. Any other argument silently prints whatever symbol occupies that slot. For the digit 1 that is slot "31, which `amssymb.sty` assigns to $\nVdash$.
- P1b converts the markdown with pandoc, using `texprobe/house-pandoc.latex`, whose preamble is copied from the house template. It compiles the result with `latexmk -pdf -g` and reports every TeX error and every missing-character warning.

P1 runs on answer-1 (the pre-fix document, for comparison only) and on answer-2. Failure, for answer-2 only: any P1a hit, any TeX error, any missing character, or no PDF.

Probe. Before writing P1 I compiled two one-page probes. One has the house math preamble. The other has only amsmath, physics and siunitx, the package set named in F1.1.
- Under the house preamble, `\mathbb 1` and `\mathbb{1}` print $\nVdash$ with no error and no warning. `\mathbf 1`, `\mathbb{I}`, `\mathbb R`, `\mathbb E`, `\square`, `\lesssim` and `\gtrsim` print correctly. I inspected the rendered page visually; it is `probe_house-1.png` in the bundle.
- Under the F1.1 set there are eight `Undefined control sequence` errors, one for each `\mathbb` and each amssymb symbol.

What it would catch:
- any `\mathbb` with a non-A–Z argument in prose or equations, anywhere outside code;
- any construct that fails to compile under the house preamble, including clashes with `physics`;
- any glyph missing from the fonts.

What it would not catch:
- a construct that compiles but renders wrongly by some other route (P1b sees only errors and missing characters, and P1a looks only for `\mathbb`);
- layout problems: the pandoc build has overfull lines, e.g. eq. (6), and these are raised as SR2.1 in §10, not tested;
- rendering in a markdown viewer (MathJax or KaTeX), where `\mathbf 1` is standard but was not tested;
- the `/log` conversion itself, for which pandoc is a stand-in, not the real thing.

Run log for P1 and the probe.
- `check_p1.py` run 0 used the pattern `\\mathbb\s*(?:\{\s*)?(?![A-Z][\s}\\$^_,.)])`. Because `\s*` can backtrack to zero width, the lookahead then saw a space, so `\mathbb R` and `\mathbb E` were flagged: 15 hits on answer-1, 7 of them false. I replaced the pattern with a lookahead anchored directly after `\mathbb`. That change makes the check pass for `\mathbb R` and `\mathbb E`, which the probe shows render correctly, and it leaves all 8 true hits flagged.
- Before the round-2 runs shown here, I also added `-g` and deletion of old build files. A first execution of the run-0 script had reused a cached PDF, because latexmk judged it up to date.
- `run_probe.sh` first listed only four of the seven error locations, because overlapping `grep -A2` matches dropped some. The counts were right; the listing was fixed.
- Probe line (g), `\mathbb E`, was added after those first runs, so that the probe covers every amssymb construct the answer uses. The probe was then re-run; the output shown is from that re-run.

The superseded run-0 script differs from the final one only in its first comment line and the pattern. Both are re-run below.

```latex
{{CODE:r2/texprobe/probe_house.tex}}
```

`probe_auditor.tex` is the same file with the line `\usepackage{amsmath,amssymb,amsthm,mathtools}` replaced by `\usepackage{amsmath}` (and the first comment changed).

```bash
{{CODE:r2/texprobe/run_probe.sh}}
```

Output of `run_probe.sh` (verbatim):

{{OUT:r2/out_probe.txt}}

```latex
{{CODE:r2/texprobe/house-pandoc.latex}}
```

```python
{{CODE:r2/check_p1.py}}
```

Output of run 0, `check_p1_run0.py answer-1.md` (verbatim):

{{OUT:r2/out_p1_run0.txt}}

Output of run 1, `check_p1.py answer-1.md answer-2.md` (verbatim; run without `time`). This is the run on the final answer-2 file. Because answer-2 contains this very output, I repeated build and P1 until P1 reproduced the embedded output byte for byte. Only the page count moved between iterations:

{{OUT:r2/out_p1.txt}}

---

## 5. Result

(a) For all real $x,x'$ and $\tau>0$:

$$
w(x,x';\tau) = (2\pi\tau)^{-1/2}\exp\Big[-\frac{(x-x')^2}{2\tau} - \frac\tau6(x^2+xx'+x'^2) - \frac{\tau^2}{12}\Big].
$$

(b) For $\beta>0$, $m\ge1$, $\tau=\beta/m$, with $\kappa=\sqrt{1+\tau^2/12}$, $s_\pm=\kappa\pm\tau/2$, $\kappa_P=\sqrt{1+\tau^2/4}$, $s^P_\pm = \kappa_P\pm\tau/2$:

$$
\hat Z_m = \frac{e^{-\beta^2/12m}}{s_+^m - s_-^m},\qquad Z_m = \frac{1}{2\sinh(m\operatorname{arcsinh}(\beta/2m))},
$$

$$
\hat E_m = \frac\tau6 + \frac{s_+^{m-1}(\kappa'+\frac12) - s_-^{m-1}(\kappa'-\frac12)}{s_+^m - s_-^m}\ \ (\kappa' = \tfrac{\tau}{12\kappa}),\qquad E_m = \frac{\coth(m\operatorname{arcsinh}(\tau/2))}{\sqrt{4+\tau^2}}.
$$

Numerical values are in the table of §3.2. In all fifteen cases $\hat E_m>\tfrac12\coth(\beta/2)>E_m$, and

$$
\hat E_m - U = \frac{\beta^2}{m^2}\Big(\frac U8 + \frac{\beta U'}{24}\Big) - \frac{\beta^3}{36m^3} + O(m^{-4}),\qquad E_m - U = -\frac{\beta^2}{m^2}\Big(\frac U8 + \frac{\beta U'}{24}\Big) + O(m^{-4}).
$$

(c) For every $\tau>0$, $T_\tau$ has the simple eigenvalues

$$
\lambda_n(\tau) = e^{-\tau^2/12}\frac{(\kappa-\tau/2)^n}{(\kappa+\tau/2)^{n+1}}
$$

with eigenfunctions $H_n(\sqrt\kappa x)e^{-\kappa x^2/2}$, and no others except possibly 0.
- For $0<\tau<\sqrt6$ all are positive, and $E_n(\tau) = (n+\tfrac12)\tfrac2\tau\operatorname{artanh}\tfrac{\tau}{2\kappa} + \tfrac\tau{12} + \tfrac{1}{2\tau}\ln(1-\tfrac{\tau^2}6)$. Its expansion is $E_n - (n+\tfrac12) = \tfrac{2n+1}{48}\tau^2 - \tfrac{\tau^3}{144} + \tfrac{3(2n+1)}{1280}\tau^4 + O(\tau^5)$.
- At $\tau=\sqrt6$, $T_\tau$ has rank one.
- For $\tau>\sqrt6$, $\operatorname{sign}\lambda_n = (-1)^n$, so $E_n(\tau)$ is not real for odd $n$ (eq. (26)). The problem's $E_n$ is ill-defined there.

The symmetric primitive kernel has $\lambda^P_n = e^{-(n+\frac12)\varphi}$, $\varphi = 2\operatorname{arcsinh}(\tau/2)$, so $E^P_n = (n+\tfrac12)\tfrac2\tau\operatorname{arcsinh}\tfrac\tau2$, with expansion $E^P_n - (n+\tfrac12) = -\tfrac{2n+1}{48}\tau^2 + \tfrac{3(2n+1)}{1280}\tau^4 + O(\tau^6)$. This holds for all $\tau>0$.

The relation between (b) and (c) is $\hat Z_m(\beta) = \sum_n\lambda_n(\beta/m)^m$ and $Z_m(\beta) = \sum_n\lambda^P_n(\beta/m)^m$, verified algebraically and numerically (C4, B5). The energies are averages of $\varepsilon_n = d(\tau E_n)/d\tau$, not of $E_n$ (eq. (30)).

Confidence:
- (a): high. Two independent recomputations from the definition (sympy S1, mpmath quadrature A) agree to 31 digits.
- (b): high. A second numerical route (B2) agrees to $\le8.2\times10^{-9}$ at all 15 points, and the spectrum route (B5) to $10^{-29}$.
- (c) eigenvalues: high. Grid C1 agrees to $\le2.4\times10^{-14}\lambda_0$, the Mehler identity C2 to $\le7.5\times10^{-13}$, and two analytic routes agree.
- Small-$\tau$ series: high (symbolic, plus grid extraction C5).
- Interpretation for $\tau\ge\sqrt6$: medium. The mathematics is certain, but what the problem intends there is not.
- Large-$m$ asymptotics (31): medium-high. It rests on [A3], confirmed numerically by B6.

What would move these: a failure of the grid or quadrature checks under an independent implementation (lower); an analytic control of [A3] (raise (31) to high).

---

## 6. Convergence check

Does the derivation reproduce the declared result?
- (a): yes, including the constant $\tau^2/12$, which I had been less sure of.
- Primitive (19), (24): yes.
- For the bridge $\hat Z_m$ and $\lambda_n$ I had declared no formula, so there was nothing to reproduce.
- My vague expectation that the bridge weight is more accurate than the primitive one was wrong. At order $\tau^2$ the level errors are equal and opposite, $\pm(2n+1)\tau^2/48$, and the thermal-energy errors are equal and opposite at order $m^{-2}$. I report this as found, not reconciled.
- I had not anticipated the loss of positivity of $T_\tau$ at $\tau=\sqrt6$.

Steps where someone who did not know the target might not have chosen as I did:
1. Writing $\alpha-\gamma\cos\theta$ as $C(1-2z\cos\theta+z^2)$ (eq. (16)). This is motivated by the wish to use the roots-of-unity product (17), which I knew in advance. Once that form is chosen, $C$ and $z$ are forced by two linear conditions on $\sqrt C(1\pm z)$. The alternative without foresight is to evaluate $\det$ by the transfer-matrix recursion for a cyclic tridiagonal matrix; it gives the same result (S3 computes the determinant directly, without (16)–(17), for $m\le7$).
2. The Hermite generating-function ansatz in route 2. Choosing $G(x;s)$ presupposes that the eigenfunctions are Hermite functions of some scale. This is motivated by the kernel being Gaussian, but it is the step where prior knowledge helps most. Route 1 removes it: the spectrum follows from the power sums $\operatorname{Tr}T^m = \hat Z_m(m\tau)$ of (b) with no ansatz. Route 1 in turn rests on `[R]` trace identities for Hilbert–Schmidt operators.
3. The choice of the positive root $\kappa_K = +\sqrt{A^2-B^2}$ in the lemma. It is forced by normalisability of $G$.
4. Rewriting (25) in the artanh form. This is a presentational choice made because it separates the even (spacing) and odd (shift) parts of the series; the series coefficients do not depend on it.
5. The form of the asymptotic statement (31). I derived the coefficient from (25), (30) before checking it numerically. The $\beta^3/(36m^3)$ term was included because it follows from the $n$-independent $-\tau^3/144$; B6 shows the residual is $O(m^{-4})$ only with it included.

There is no factor inserted for later convenience. The substitution $s = u/\tau$ in (6) and the choice of breakpoints in check A are routine.

Would the derivation still run if the standard result were slightly different? Each closed form is tested by a route that does not pass through it.
- Had (8) had $\tau^2/6$ instead of $\tau^2/12$, or a doubled cross term, check A shows the wrong candidates disagree with the numerics by order one, so this would have been noticed.
- Had I made a factor error in the circulant eigenvalues (14), S3 and B2 compute determinants directly from the action and would fail.
- Had the eigenvalue formula (23) had a wrong power (say $s_+^{-n}$ instead of $s_+^{-(n+1)}$), C1 compares eigenvalues individually at nine $\tau$ values and would fail at the $10^{-10}$ level.
- The one place where a shared misunderstanding could pass unnoticed is a misreading of the definition of $w$ in the prompt, since both check A and the derivation transcribe it. I transcribed it literally: $V(y)$ inside, $1/\rho_0(x,x';\tau)$ outside the $y$-integral, $u\in(0,\tau)$.

---

## 7. Risk register

| Item | Type | What it is | If wrong |
|---|---|---|---|
| [A1] | assumption | $y$-integral evaluated for $0<u<\tau$; endpoints have measure zero | none in practice: the integrand extends to a polynomial on $[0,\tau]$ (S1, A) |
| [A2] | assumption | differentiation under the integral sign for the holomorphic parameter $s$ in route 2 | route 2 incomplete; eigenvalues still established by route 1 and checks C1–C3 |
| [A3] | assumption | small-$\tau$ expansion taken inside $\sum_n$ for the large-$m$ asymptotics (31) | (31) could have a wrong $m^{-3}$ or higher coefficient; B6 confirms numerically up to $m=8000$ |
| Trace identities for Hilbert–Schmidt and compact self-adjoint operators ($\operatorname{Tr}T^m = \sum\mu^m$ for $m\ge2$; trace as an integral of composed kernels) | [R] | used in route 1 and in (29) | route 1 would fail; route 2 and the numerical C4, B5 still stand |
| Feynman–Kac representation, used with Jensen for $w\le\rho$ | [R] | used only for the self-checks B4, C6 | the bounds lose their justification; no result changes |
| Hermite norm $\|H_n\|^2 = 2^nn!\sqrt\pi$ (DLMF Table 18.3.1, not retrieved) | [R] | used only in the explicit 60-term sum in C2 | that check line would be meaningless; it passed, which corroborates the norm |
| DLMF 18.12.15 | [S], {ver: tool} via a mirror | Hermite generating function, used in route 2 | route 2 would need another basis; not an issue given route 1 |
| DLMF §18.18(i) | [S], {ver: tool} | $L^2$ completeness of Hermite expansions, used in route 2 to exclude other eigenvalues | route 1 excludes missing nonzero eigenvalues analytically (given the [R] trace identities); C3 (Hilbert–Schmidt norm saturation to $\sim10^{-13}$) excludes numerically any missing eigenvalue with $|\mu|\gtrsim10^{-6}\lambda_0$ |
| Ill-posedness for $\tau\ge\sqrt6$ | reading | $E_n=-\tau^{-1}\ln\lambda_n$ not real (odd $n$) or infinite ($n\ge1$, $\tau=\sqrt6$) | if the intended quantity were $-\tau^{-1}\ln|\lambda_n|$, use (26) without the $-i\pi/\tau$ |
| Check revisions (`check_a` ×3, `check_c` ×1 in round 1; `check_p1`, `validate_reruns.py` and `run_probe.sh` ×1 each in round 2) | process | checks changed after failures, disclosed in §4.2 and §4.3 | an auditor should verify that each change is a correction and not a weakening |
| Rebuilt round-1 scripts (`check_c_run0.py`, `check_c_run1.py`, `check_b_run1.py`) | process | rebuilt in round 2 by reverse-applying the round-1 edits | a wrong rebuild would misreport the round-1 history; `validate_reruns.py` shows their outputs identical to the round-1 records |
| Rendering of the math in the `/log` PDF | presentation | checked by P1: no `\mathbb` with a non-A–Z argument; compiles under the house preamble with 0 errors and 0 missing characters | not checked: MathJax/KaTeX viewers, other wrong renderings that compile silently, layout (SR2.1); no effect on content |

No `{ver: no}` citation is load-bearing.

---

## 8. Sources

### Used

- F. W. J. Olver et al. (eds.), NIST Digital Library of Mathematical Functions, https://dlmf.nist.gov/ (online, retrieved 2026-11-12), §18.12, eq. (18.12.15): $e^{2xz-z^2} = \sum_{n\ge0}H_n(x)z^n/n!$. Used in route 2 of the lemma in §3.3. {ver: tool}. Retrieval note: dlmf.nist.gov/18.12 was not reachable from this session (allowlist). I fetched the MaRDI portal page `https://portal.mardi4nfdi.de/wiki/Formula:6354`, labelled "DLMF:18.12.E15", which reproduces the formula exactly as written here, with $z$ complex and $x$ real. This is a mirror of the DLMF formula database, not the DLMF page itself.
- F. W. J. Olver et al. (eds.), NIST Digital Library of Mathematical Functions (online, retrieved 2026-11-12), §18.18(i), eqs. (18.18.6)–(18.18.7) and the paragraph "Expansion of $L^2$ functions": for Jacobi, Laguerre and Hermite, if $f$ is $L^2$ with respect to the weight ($e^{-x^2}$ for Hermite), the expansions converge in the $L^2$ sense, citing Szegő (1975), Theorems 3.1.5 and 5.7.1. Used for completeness in §3.3. {ver: tool}. Retrieval note: fetched `https://dlmf.nist.gov/18.18`. The page gives (18.18.6) $f(x) = \sum d_nH_n(x)$ and (18.18.7) $d_n = (\sqrt\pi2^nn!)^{-1}\int fH_ne^{-x^2}dx$ (the fetch tool noted that it restored a square root dropped in rendering), and the $L^2$-convergence sentence with the Szegő theorems.

Used in round 2. These are load-bearing only for §10 (Response to audit 1). No physics result depends on them.

- House LaTeX template of the `/log` step: log skill, file `reference/final-tex-template.tex` as embedded in the skill's SKILL.md (synced copy on this machine, lines 434–447), preamble `\usepackage{amsmath,amssymb,amsthm,mathtools}`, `\usepackage{physics}`, `\usepackage{siunitx}`. {ver: tool}. Retrieval note: file read on disk on 2026-11-13; the three lines are as quoted.
- `amsmath.sty` v2.17o (2023/05/13), TeX Live 2023/Debian, lines 127–129: `\RequirePackage{amstext}`, `{amsbsy}`, `{amsopn}`; no amssymb. {ver: tool}. Retrieval note: grep of the installed file.
- `physics.sty`, TeX Live 2023/Debian, lines 15–16: `\RequirePackage{xparse}`, `\RequirePackage{amsmath}`; no amssymb. {ver: tool}. Retrieval note: grep of the installed file.
- `amsfonts.sty` v3.01 (2013/01/14), line 108: `\DeclareSymbolFontAlphabet{\mathbb}{AMSb}`; `amssymb.sty` v3.01, line 34: `\RequirePackage{amsfonts}`, and line 220: `\DeclareMathSymbol{\nVdash}{\mathrel}{AMSb}{"31}`. {ver: tool}. Retrieval note: grep of the installed files.

### Consulted

- NIST DLMF (online, retrieved 2026-11-12), §18.18(vii), eq. (18.18.28), Mehler's formula, $\sum_n H_n(x)H_n(y)z^n/(2^nn!) = (1-z^2)^{-1/2}\exp\{[2xyz - (x^2+y^2)z^2]/(1-z^2)\}$, $|z|<1$. Used only inside check C2, not in the derivation. {ver: tool}. Retrieval note: the second part of `https://dlmf.nist.gov/18.18`; the tool reconstructed the formula from the page's LaTeX and reported the condition $|z|<1$. The equation number was also cited as (18.18.28) in arXiv:2606.02405 (search result), which I did not otherwise use.
- J. van Neerven, Functional Analysis (Cambridge Univ. Press; arXiv:2112.11166), §3.5.b, Theorem 3.33 (Hermite polynomials form an orthonormal basis of $L^2(\mathbb R,\gamma)$). Seen only in a search-result snippet. The full-text fetch was truncated before chapter 3, so the locator is not confirmed. Not relied on. {ver: no}.
- Not consulted, by instruction: Kole and De Raedt, Phys. Rev. E 64, 016704 (2001); arXiv:physics/0102015; the repository AndresMotta77/Introduccion_Fisica_Teorica; any published table of these approximants. My searches were restricted to DLMF/Hermite/Mehler/completeness keywords, and none of the results returned was from these sources.

---

## 9. Open questions

1. An independent computation of $w$ by a different method: Monte Carlo sampling of Brownian bridges to estimate $\int_0^\tau V$ along bridges, compared with (8) at a few points. This would test the reading of the definition in a way that does not share code with check A.
2. A human comparison of (18), (20), (23) with any oscillator results in the forbidden reference, done by someone allowed to read it.
3. Whether the intended $E_n(\tau)$ for $\tau\ge\sqrt6$ is $-\tau^{-1}\ln|\lambda_n|$, or whether the problem implicitly restricts to $\tau<\sqrt6$. For the table this matters only at $(\beta,m) = (5,1)$ and $(10,1)$, where $\tau>\sqrt6$; there $\hat Z_m$ and $\hat E_m$ are still well defined and positive.
4. An analytic proof of (31) controlling [A3], e.g. by writing $\hat Z_m$ from (18) directly as a function of $1/m$ and expanding $\ln\hat Z_m$. This is mechanical with a computer-algebra system and would replace the numerical B6.
5. An independent derivation of the $O(\tau^2)$ coefficient $(2n+1)/48$ from the second cumulant of $\int_0^\tau V(y(u))du$ over the bridge, which is the leading term Jensen discards. This would explain why it is exactly the negative of the primitive coefficient.
6. An auditor re-implementation of C1 with a different quadrature (e.g. Gauss–Hermite Nyström) to remove any shared-code blind spot in my grid construction.

---

## 10. Response to audit 1

| Finding | Outcome | What changed | Where |
|---|---|---|---|
| F1.1 (MINOR) | partial: the defect is accepted and fixed; part of the evidence and one of the suggested fixes are rejected | `\mathbb 1` replaced by $\mathbf 1$ at all 8 occurrences; $\mathbf 1$ defined at first use and added to the symbol table; new check P1 | §2.2; §3.2 (the two sums before eq. (12), eq. (12), the $m=2$ item, eq. (19a)); §4.2; §4.3 (P1); §7; §8 |

### F1.1, accepted part

The defect is real. Under the house LaTeX template, the identity matrix printed as $\nVdash$ instead of a double-struck one. This affected eqs. (12) and (19a), the two sums just before (12), and the $m=2$ item. It happened silently: on answer-1, P1b reports 0 TeX errors and 0 missing characters, while P1a finds 8 hits.

The mechanism, read from the installed files:
- `amsfonts.sty` (line 108) declares `\mathbb` as the alphabet of the AMSb symbol font;
- that font has blackboard glyphs only in the uppercase-letter slots;
- the slot of the digit 1, "31, holds `\nVdash` (`amssymb.sty`, line 220).

I replaced every instance with $\mathbf 1$, which is the third option the finding supplies. `\mathbf` is a LaTeX kernel command, so it works under any package set; MathJax and KaTeX also support it, though I did not test a viewer. I also defined the symbol at first use and in the symbol table. Answer-1 used it without a definition, which is a separate omission of the same kind (Conventions §7).

After the change, P1a finds 0 hits in answer-2, and P1b compiles answer-2 under the house preamble with 0 errors and 0 missing characters.

### F1.1, rejected part, with evidence

1. The premise that the allowed packages are amsmath, physics and siunitx. The house template used by the `/log` step (log skill, `reference/final-tex-template.tex`) loads `\usepackage{amsmath,amssymb,amsthm,mathtools}`, then physics and siunitx. Neither prompt0 nor CONVENTIONS.md restricts packages.
2. The claim that amssymb is "loaded by `amsmath` or `physics`". Neither package loads it. `amsmath.sty` v2.17o requires only amstext, amsbsy and amsopn (lines 127–129). `physics.sty` requires only xparse and amsmath (lines 15–16). Under the package set the finding states, `\mathbb` is not defined at all, and the probe gives `Undefined control sequence`, not a wrong glyph.
3. The first suggested fix, `\mathbb{I}`. It renders correctly under the house template. Under the finding's own premise it would be an undefined control sequence, as would the `\mathbb R` and `\mathbb E` used elsewhere in the answer, which the finding did not flag. I chose $\mathbf 1$ because it is right under both readings. I also avoided a plain $I$, which already denotes the exponent $I(x,x';\tau)$ of eq. (8).
4. "An illegible glyph or a blank space." What is printed is a legible but wrong glyph, the relation symbol $\nVdash$. This makes the finding stronger, not weaker, since a reader can take it for an operator.

Consequence for the rest of the answer. Under the actual house template, the other amssymb constructs in the answer render correctly (probe and P1b): `\mathbb R`, `\mathbb E`, `\square`, `\lesssim`, `\gtrsim`. So no further change is needed. Had the finding's package set been the real one, all of them would have needed changing, and changing only the identity would not have satisfied the finding's own test.

### Solver-raised item, not acted on

SR2.1 (NIT, presentation, frozen sections). In the pandoc build under the house preamble, some displays and long table rows run into the right margin: eqs. (6), (13) and (14) are visibly cut, and the build log reports several overfull lines. In markdown they display normally. Fixing them means re-laying-out equations in frozen sections, so I raise the item for the next audit or for the `/log` step rather than editing.

### Changes outside F1.1

There are no changes to the mathematics, to any number, or to §§1, 3.1, 3.3, 3.4, 5, 6 and 9. §3.2 changed only in the identity-matrix notation and in the table caption, which now names the round-2 re-run. §2.2 gained one row. The header has a new paragraph describing round 2.

§4 changed only by the round-2 re-runs (new outputs, identical to round 1 apart from timing lines), by the rebuilt superseded scripts and their validation, and by the new P1 subsection. §7 has three updated or new rows, and §8 has four new Used entries, which are load-bearing only for this section.

### On the audit itself

The auditor reports that no code was executed. The executed verification is therefore still only mine, now re-run in round 2; Pass 6b recomputed $\hat Z_1$ analytically. An auditor-run re-implementation of C1 or B2 would still add independent evidence (§9, item 6).
