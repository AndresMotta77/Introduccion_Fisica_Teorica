# P003.S03 — final

The harmonic oscillator under a bridge-averaged slice weight: closed form, partition functions, levels.

> Release gate failed: `audit_trail_complete`. answer-2, from which this document is derived, was not audited. Audit 1 (of answer-1) returned ACCEPT-WITH-FIXES with one MINOR finding, F1.1. answer-2 applies the fix, adds check P1 and contests part of the finding's evidence, and none of that was reviewed by an auditor. The user closed the loop on 2026-11-13 under the stopping rule of CONVENTIONS.md §6 (audit 1 raised no BLOCKER and no MAJOR).

This document is `answers/answer-2.md` (Claude Opus 5.5, round 2, 2026-11-13) with sections moved out by `assets/code/log/make_final.py`. Section numbers are those of answer-2. §1, the Prior-knowledge declaration, is in `sources/independence.md`, together with a copy of §6. §10, the Response to audit 1, is in `audits/response-to-audit-1.md`. The only other edits redirect two cross-references from §10 to that file.

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

| beta | m | Ehat_m | E_m | exact | Ehat_m - exact | E_m - exact |
|---:|---:|---:|---:|---:|---:|---:|
| 1 | 1 | 1.1666666667 | 1.0000000000 | 1.0819767069 | +8.4690e-02 | -8.1977e-02 |
| 1 | 10 | 1.0829195400 | 1.0810096440 | 1.0819767069 | +9.4283e-04 | -9.6706e-04 |
| 1 | 50 | 1.0820152418 | 1.0819379555 | 1.0819767069 | +3.8535e-05 | -3.8751e-05 |
| 1 | 100 | 1.0819863678 | 1.0819670185 | 1.0819767069 | +9.6610e-06 | -9.6884e-06 |
| 1 | 500 | 1.0819770942 | 1.0819763193 | 1.0819767069 | +3.8732e-07 | -3.8754e-07 |
| 5 | 1 | 1.0333333333 | 0.2000000000 | 0.5067836549 | +5.2655e-01 | -3.0678e-01 |
| 5 | 10 | 0.5194026977 | 0.4919968670 | 0.5067836549 | +1.2619e-02 | -1.4787e-02 |
| 5 | 50 | 0.5073762527 | 0.5061655704 | 0.5067836549 | +5.9260e-04 | -6.1808e-04 |
| 5 | 100 | 0.5069350671 | 0.5066289152 | 0.5067836549 | +1.5141e-04 | -1.5474e-04 |
| 5 | 500 | 0.5067898198 | 0.5067774625 | 0.5067836549 | +6.1648e-06 | -6.1924e-06 |
| 10 | 1 | 1.7666666667 | 0.1000000000 | 0.5000454020 | +1.2666e+00 | -4.0005e-01 |
| 10 | 10 | 0.5431607460 | 0.4472727273 | 0.5000454020 | +4.3115e-02 | -5.2773e-02 |
| 10 | 50 | 0.5023400295 | 0.4975645276 | 0.5000454020 | +2.2946e-03 | -2.4809e-03 |
| 10 | 100 | 0.5006436192 | 0.4994217039 | 0.5000454020 | +5.9822e-04 | -6.2370e-04 |
| 10 | 500 | 0.5000701763 | 0.5000204092 | 0.5000454020 | +2.4774e-05 | -2.4993e-05 |

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
# reconstruct_superseded.py -- rebuild the round-1 superseded versions of check_c.py (runs 0
# and 1) and check_b.py (run 1), which were edited in place in round 1 and not kept, by
# reverse-applying the exact round-1 edits to the final scripts. Every replacement is
# asserted to occur exactly once. The reconstructions are validated by re-running them and
# diffing against the outputs recorded in round 1.
import pathlib

def rev(text, new, old):
    assert text.count(new) == 1, new[:70]
    return text.replace(new, old)

c = pathlib.Path('check_c.py').read_text()

# ---- final -> run 1 (undo round-1 edit 2) ----
c1 = rev(c, '''# ----- C5: small-tau coefficients from GRID eigenvalues -----
# REVISION NOTE (run 2): in run 1 (out_c_run1_C5FAILED.txt) the predictions stopped at
# O(tau^3) in R_n and O(tau^2) in P_n, and the primitive case failed the 5e-6 tolerance at
# tau=0.4, n=2,3 (d = 7.4e-6, 1.0e-5), the omitted remainder scaling as tau^4 (1.0e-5 -> 6.6e-7
# -> 4.3e-8). I changed the CHECK, not the derivation: the next two analytic series terms of
# the closed form (sympy, see check_algebra-style series) were added to the predictions; the
# tolerance was kept at 5e-6. The leading coefficients under test are unchanged.''',
'''# ----- C5: small-tau coefficients from GRID eigenvalues -----''')
c1 = rev(c1, '''        pred = (-1/144 + 3*(2*nn + 1)*t/1280 - t*t/1296 + 103*(2*nn + 1)*t**3/387072
                - t**4/10368 + 187*(2*nn + 1)*t**5/5308416)''',
'''        pred = -1/144 + 3*(2*nn + 1)*t/1280 - t*t/1296 + 103*(2*nn + 1)*t**3/387072''')
c1 = rev(c1, '''        predP = 3*(2*nn + 1)/1280 - 5*(2*nn + 1)*t*t/14336 + 35*(2*nn + 1)*t**4/589824''',
'''        predP = 3*(2*nn + 1)/1280 - 5*(2*nn + 1)*t*t/14336''')
c1 = rev(c1, '''"-1/144 + 3(2n+1)tau/1280 - tau^2/1296 + 103(2n+1)tau^3/387072 - tau^4/10368 + 187(2n+1)tau^5/5308416 + O(tau^6));")''',
'''"-1/144 + 3(2n+1)tau/1280 - tau^2/1296 + 103(2n+1)tau^3/387072 + O(tau^4));")''')
c1 = rev(c1, '''"   P_n = [E_n-(n+1/2) + (2n+1)tau^2/48]/tau^4 (primitive, predicted 3(2n+1)/1280 - 5(2n+1)tau^2/14336 + 35(2n+1)tau^4/589824 + O(tau^6))")''',
'''"   P_n = [E_n-(n+1/2) + (2n+1)tau^2/48]/tau^4 (primitive, predicted 3(2n+1)/1280 - 5(2n+1)tau^2/14336 + O(tau^4))")''')
pathlib.Path('check_c_run1.py').write_text(c1)

# ---- run 1 -> run 0 (undo round-1 edit 1) ----
new_hdr = '''print("C5 from grid eigenvalues: R_n = [E_n-(n+1/2) - (2n+1)tau^2/48]/tau^3 (bridge, predicted "
      "-1/144 + 3(2n+1)tau/1280 - tau^2/1296 + 103(2n+1)tau^3/387072 + O(tau^4));")
print("   P_n = [E_n-(n+1/2) + (2n+1)tau^2/48]/tau^4 (primitive, predicted 3(2n+1)/1280 - 5(2n+1)tau^2/14336 + O(tau^4))")
print("   failure if |R_n - pred| or |P_n - pred| > 5e-6 at any tau <= 0.4, n <= 3")'''
old_hdr = '''print("C5 from grid eigenvalues: R_n = [E_n-(n+1/2) - (2n+1)tau^2/48]/tau^3 (bridge, predicted "
      "-1/144 + 3(2n+1)tau/1280 - tau^2/1296 + O(tau^3));")
print("   P_n = [E_n-(n+1/2) + (2n+1)tau^2/48]/tau^4 (primitive, predicted 3(2n+1)/1280 + O(tau^2))")'''
c0 = rev(c1, new_hdr, old_hdr)
c0 = rev(c0, '''        pred = -1/144 + 3*(2*nn + 1)*t/1280 - t*t/1296 + 103*(2*nn + 1)*t**3/387072
        rowb.append(f"n={nn}: R={R:+.7f} d={R - pred:+.1e}")
        EnP = -np.log(evp[nn])/t
        P = (EnP - (nn + 0.5) + (2*nn + 1)*t*t/48)/t**4
        predP = 3*(2*nn + 1)/1280 - 5*(2*nn + 1)*t*t/14336
        rowp.append(f"n={nn}: P={P:.7f} d={P - predP:+.1e}")
        bad = (abs(R - pred) > 5e-6) or (abs(P - predP) > 5e-6) or not np.isfinite(R + P)
        nfail += bad''',
'''        pred = -1/144 + 3*(2*nn + 1)*t/1280 - t*t/1296
        rowb.append(f"n={nn}: R={R:+.6f} pred={pred:+.6f}")
        EnP = -np.log(evp[nn])/t
        P = (EnP - (nn + 0.5) + (2*nn + 1)*t*t/48)/t**4
        rowp.append(f"n={nn}: P={P:.6f} pred={3*(2*nn + 1)/1280:.6f}")''')
pathlib.Path('check_c_run0.py').write_text(c0)

# ---- check_b final -> run 1 ----
b = pathlib.Path('check_b.py').read_text()
b1 = rev(b, '''        X = E + E[i]                              # rows: e_j + e_i
        X[i] = E[i]                               # row i would be 2 e_i; it is not used (diagonal
                                                  # set below) and for tau=0.002 it underflows w
                                                  # to 0 (run 1 printed a log(0) warning here)
        Sij, dSij = S_and_dS(X)''',
'''        Sij, dSij = S_and_dS(E + E[i])            # rows: e_j + e_i''')
pathlib.Path('check_b_run1.py').write_text(b1)
print("reconstructed: check_c_run0.py, check_c_run1.py, check_b_run1.py")
```

Its output, verbatim: `reconstructed: check_c_run0.py, check_c_run1.py, check_b_run1.py`.

```python
# validate_reruns.py -- (run 1) compare every round-2 output with the output recorded in round 1.
# Python 3.13.18. Run from the round-2 folder: python3 -I validate_reruns.py
# Normalisation: drop the shell timing lines (real/user/sys) and blank lines, and replace the
# absolute script path in Python warning lines by the bare file name. Nothing else is touched.
# The round-1 records of check_c run 0 (C5 block) and of the two diagnostics exist only inside
# answer-1's source (template.md); they are extracted from there.
import re, pathlib
R1 = pathlib.Path('..')

def norm(s):
    out = []
    for l in s.splitlines():
        if re.match(r'^(real|user|sys)\s', l) or not l.strip():
            continue
        l = re.sub(r'^/\S*/(check_b(_run1)?\.py)', 'check_b.py', l)
        out.append(l)
    return out

def block_after(text, marker, skip=0):
    """first fenced block after marker; skip=1 when the marker sits inside a code block,
    so that block's closing fence is passed first (run 0 lacked this and returned '')"""
    i = text.index(marker)
    for _ in range(skip):
        i = text.index("\n```\n", i) + 5
    j = text.index("```\n", i) + 4
    k = text.index("```", j)
    return text[j:k]

tmpl = (R1/'template.md').read_text()
records = {
    'c_run0_C5': block_after(tmpl, "The run-0 C5 lines, verbatim"),
    'dbg_a':     block_after(tmpl, "# dbg_a.py\n", skip=1),
    'dbg_a2':    block_after(tmpl, "# dbg_a2.py\n", skip=1),
}
c0 = pathlib.Path('out_c_run0.txt').read_text()
c1 = pathlib.Path('out_c_run1.txt').read_text()
pathlib.Path('out_c_run0_C5.txt').write_text(c0[c0.index("C5 from grid"):])
pathlib.Path('out_c_run1_C5.txt').write_text(c1[c1.index("C5 from grid"):])

pairs = [
    ('out_algebra.txt',   (R1/'out_algebra.txt').read_text()),
    ('out_a.txt',         (R1/'out_a.txt').read_text()),
    ('out_a_run1.txt',    (R1/'out_a_run1_FAILED.txt').read_text()),
    ('out_a_run2.txt',    (R1/'out_a_run2_1FAIL.txt').read_text()),
    ('out_c.txt',         (R1/'out_c.txt').read_text()),
    ('out_c_run1.txt',    (R1/'out_c_run1_C5FAILED.txt').read_text()),
    ('out_c_run0_C5.txt', records['c_run0_C5']),
    ('out_b.txt',         (R1/'out_b.txt').read_text()),
    ('out_b_run1.txt',    (R1/'out_b_run1.txt').read_text()),
    ('out_table.txt',     (R1/'out_table.txt').read_text()),
    ('out_dbg_a.txt',     records['dbg_a']),
    ('out_dbg_a2.txt',    records['dbg_a2']),
]
nd = 0
for f, old in pairs:
    new = norm(pathlib.Path(f).read_text()); old = norm(old)
    same = (new == old) and len(old) > 0 and len(new) > 0   # an empty side never counts as a match
    nd += (not same)
    print(f"{f:20s} lines={len(new):4d}  identical to round-1 record: {same}")
    if not same:
        for a, b in zip(old, new):
            if a != b:
                print("   round 1:", a); print("   round 2:", b)
c_run0_C1to4 = c0[:c0.index("C5 from grid")]
fin = pathlib.Path('out_c.txt').read_text()
same = c_run0_C1to4 == fin[:fin.index("C5 from grid")]
nd += (not same)
print(f"check_c run 0, sections C1-C4: identical to the final run's C1-C4: {same}")
print("NUMBER OF MISMATCHES:", nd)
```

Output of `validate_reruns.py` (verbatim):

```
out_algebra.txt      lines=  33  identical to round-1 record: True
out_a.txt            lines=  20  identical to round-1 record: True
out_a_run1.txt       lines=  20  identical to round-1 record: True
out_a_run2.txt       lines=  20  identical to round-1 record: True
out_c.txt            lines=  81  identical to round-1 record: True
out_c_run1.txt       lines=  81  identical to round-1 record: True
out_c_run0_C5.txt    lines=  12  identical to round-1 record: True
out_b.txt            lines=  59  identical to round-1 record: True
out_b_run1.txt       lines=  63  identical to round-1 record: True
out_table.txt        lines=  17  identical to round-1 record: True
out_dbg_a.txt        lines=   8  identical to round-1 record: True
out_dbg_a2.txt       lines=   3  identical to round-1 record: True
check_c run 0, sections C1-C4: identical to the final run's C1-C4: True
NUMBER OF MISMATCHES: 0
```

The superseded validator (`validate_reruns_run0.py`) differs from the final one as follows (`diff validate_reruns_run0.py validate_reruns.py`):

```
1c1
< # validate_reruns.py -- compare every round-2 output with the output recorded in round 1.
---
> # validate_reruns.py -- (run 1) compare every round-2 output with the output recorded in round 1.
19c19,21
< def block_after(text, marker):
---
> def block_after(text, marker, skip=0):
>     """first fenced block after marker; skip=1 when the marker sits inside a code block,
>     so that block's closing fence is passed first (run 0 lacked this and returned '')"""
20a23,24
>     for _ in range(skip):
>         i = text.index("\n```\n", i) + 5
28,29c32,33
<     'dbg_a':     block_after(tmpl, "# dbg_a.py\n"),
<     'dbg_a2':    block_after(tmpl, "# dbg_a2.py\n"),
---
>     'dbg_a':     block_after(tmpl, "# dbg_a.py\n", skip=1),
>     'dbg_a2':    block_after(tmpl, "# dbg_a2.py\n", skip=1),
53c57
<     same = (new == old)
---
>     same = (new == old) and len(old) > 0 and len(new) > 0   # an empty side never counts as a match
```

Re-run after all outputs existed, it reports only the two spurious diagnostic mismatches. Its first execution had also counted the then-unfinished `out_a_run2.txt`. Last lines, verbatim:

```
out_dbg_a.txt        lines=   8  identical to round-1 record: False
out_dbg_a2.txt       lines=   3  identical to round-1 record: False
check_c run 0, sections C1-C4: identical to the final run's C1-C4: True
NUMBER OF MISMATCHES: 2
```

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

```
        x        xp         tau                  I_num               I_closed     relerr   w relerr
   2.2477   -2.4016    0.107549   0.098149468681861646  0.0981494721219007529     3.5e-8    3.44e-9 FAIL
   2.3127   -2.2680   0.0974188  0.0859851765624651545  0.0859851795829655646    3.51e-8    3.02e-9 FAIL
  -1.0765    0.9027   0.0242251 0.00409409769255544469 0.00409409783494425554    3.48e-8   1.42e-10 FAIL
  -1.1283   -2.4229    0.159145   0.264092691081447326   0.264092691081447326   1.87e-31        0.0 ok
  -2.6895   -0.5887     4.74681    9.12709027547319101    9.12709027547319101   1.73e-31   1.58e-30 ok
  -2.4006    1.8476   0.0330348  0.0261952000467325199   0.026195200985980636    3.59e-8   9.39e-10 FAIL
  -2.2063   -2.4695     4.59742    14.3389344162538047    14.3389344162538047    1.1e-31   1.58e-30 ok
  -0.6498    0.1282     3.91834    1.51150624118418907    1.51150624118418907    1.3e-31   1.97e-31 ok
   0.0000    0.0000           1  0.0833333333333333333  0.0833333333333333333        0.0        0.0 ok
   2.0000   -2.0000       0.001 0.000666749975809656063 0.000666750000000000014    3.63e-8   2.42e-11 FAIL
   1.5000    1.5000          20    55.8333333333333333    55.8333333333333333        0.0        0.0 ok
  -4.0000    3.0000           5    12.9166666666666667    12.9166666666666667   3.66e-31   4.73e-30 ok
   0.7000   -0.7000     2.44949   0.700041662327292746   0.700041662327292746   1.41e-31   9.86e-32 ok
points tested: 13  failures: 5
max relative discrepancy of WRONG candidates against the same numerics:
    prim  tau(x^2+x'^2)/4        2.0
    no tau^2/12 term             1.0
    cross-term coeff doubled     0.9999
    tau^2/6 instead of tau^2/12  1.0

real	9m44.695s
user	8m32.443s
sys	0m0.623s
```

A diagnostic (two short scripts) showed three things. They were deleted after round 1. For round 2 they were re-created verbatim from the round-1 record, except that the file they read is now named `check_a_run1.py`, and re-run.

```python
# dbg_a.py -- round-1 diagnostic, re-run in round 2 against check_a_run1.py
# (round 1 read 'check_a.py', which at that time was the run-1 version; that filename is the only change)
import sys; sys.argv=['x']
exec(open('check_a_run1.py').read().split("wrong = {")[0])
x,xp,tau=mp.mpf(2),mp.mpf(-2),mp.mpf('0.001')
r=rho0(x,xp,tau)
for fr in ['1e-14','1e-11','1e-9','1e-8','1e-7','1e-5','1e-3','0.3']:
    u=tau*mp.mpf(fr)
    val=inner(x,xp,tau,u)/r
    yb=((tau-u)*x+u*xp)/tau; s2=u*(tau-u)/tau
    print(fr, mp.nstr(val,15), mp.nstr((yb**2+s2)/2,15))
```

```
1e-14 1.9999999274062 1.99999999999992
1e-11 1.99999992732628 1.99999999992
1e-9 1.99999991940678 1.9999999920005
1e-8 1.99999984741128 1.999999920005
1e-7 1.99999912745639 1.99999920005008
1e-5 1.99991993320913 1.99992000579995
1e-3 1.99200842719641 1.9920084995
0.3 0.320104988394535 0.320105
```

```python
# dbg_a2.py -- round-1 diagnostic, re-run in round 2 against check_a_run1.py
# (round 1 read 'check_a.py', which at that time was the run-1 version; that filename is the only change)
exec(open('check_a_run1.py').read().split("wrong = {")[0])
x,xp,tau=mp.mpf(2),mp.mpf(-2),mp.mpf('0.001')
for fr in ['1e-9','1e-3','0.3']:
    u=tau*mp.mpf(fr)
    g = lambda yy: -(yy - x)**2/(2*u) - (yy - xp)**2/(2*(tau - u))
    dg = lambda yy: mp.diff(g, yy)
    ystar = mp.findroot(dg, (x, xp + mp.mpf('1e-3')), solver='secant', verify=False)
    curv = -mp.diff(g, ystar, 2); s=1/mp.sqrt(curv)
    yb=((tau-u)*x+u*xp)/tau; s2=u*(tau-u)/tau
    f = lambda yy: rho0(x, yy, u)*V(yy)*rho0(yy, xp, tau - u)
    pts = [-mp.inf] + [ystar + k*s for k in (-40, -12, -5, -2, 0, 2, 5, 12, 40)] + [mp.inf]
    v,err=mp.quad(f, pts, error=True)
    v2=mp.quad(f, [-mp.inf]+[yb+k*mp.sqrt(s2) for k in range(-40,41,2)]+[mp.inf])
    print(fr, mp.nstr(ystar-yb,5), mp.nstr(s/mp.sqrt(s2),10), mp.nstr(v/rho0(x,xp,tau),15), mp.nstr(err/v,3), mp.nstr(v2/rho0(x,xp,tau),15))
```

```
1e-9 -4.4399e-31 1.0 1.99999991940678 0.000576 1.99999996289129
1e-3 -2.0016e-31 1.0 1.99200842719641 0.000576 1.99200847050717
0.3 3.9443e-32 1.0 0.320104988394535 0.000575 0.320104995356076
```

These diagnostics compare against $\bar y$, $\sigma^2$ from the derivation; they were used only to locate the fault, not as verification. The diagnosis: the peak location and width were correct to $10^{-31}$. The inner integral was low by $3.6\times10^{-8}$ relative at every $u$. mpmath's own error estimate for the inner integral was $5.8\times10^{-4}$ relative. The integrand was $\sim e^{-(x-x')^2/2\tau}$ (e.g. $e^{-8000}$), and tanh-sinh's stopping test is absolute, so it stopped at low degree. Change (run 2): divide by the constant $\rho_0(x,x';\tau)$ inside the $y$-integral, so that the integrand is $O(1)$. This is mathematically identical to the definition. I also record mpmath's error estimates and fail the point if they exceed tolerance.

`check_a.py`, run 2. All thirteen values agreed with the closed form to $\sim10^{-31}$, but point $(0,0,1)$ was flagged by the new criterion (quad\_y $=6.8\times10^{-7}$). Verbatim output:

```
        x        xp         tau                  I_num               I_closed     relerr   w relerr   quad_u   quad_y
   2.2477   -2.4016    0.107549  0.0981494721219007529  0.0981494721219007529        0.0        0.0  4.1e-54  1.5e-36 ok
   2.3127   -2.2680   0.0974188  0.0859851795829655646  0.0859851795829655646   1.43e-31        0.0  4.7e-54  1.6e-36 ok
  -1.0765    0.9027   0.0242251 0.00409409783494425554 0.00409409783494425554        0.0        0.0  9.8e-56  2.1e-36 ok
  -1.1283   -2.4229    0.159145   0.264092691081447326   0.264092691081447326        0.0        0.0  1.5e-56  2.9e-38 ok
  -2.6895   -0.5887     4.74681    9.12709027547319101    9.12709027547319101   1.73e-31   1.58e-30  4.4e-57  2.3e-37 ok
  -2.4006    1.8476   0.0330348   0.026195200985980636   0.026195200985980636   1.18e-31        0.0  1.5e-54  6.5e-37 ok
  -2.2063   -2.4695     4.59742    14.3389344162538047    14.3389344162538047        0.0        0.0  2.8e-54  4.1e-39 ok
  -0.6498    0.1282     3.91834    1.51150624118418907    1.51150624118418907    1.3e-31   1.97e-31  2.6e-54  3.0e-36 ok
   0.0000    0.0000           1  0.0833333333333333333  0.0833333333333333333        0.0        0.0  4.8e-55   6.8e-7 FAIL
   2.0000   -2.0000       0.001 0.000666750000000000014 0.000666750000000000014        0.0        0.0  6.0e-57  1.6e-34 ok
   1.5000    1.5000          20    55.8333333333333333    55.8333333333333333        0.0        0.0  7.2e-53  8.9e-39 ok
  -4.0000    3.0000           5    12.9166666666666667    12.9166666666666667   1.22e-31   1.58e-30  3.1e-52  8.1e-39 ok
   0.7000   -0.7000     2.44949   0.700041662327292746   0.700041662327292746        0.0        0.0  5.7e-56  1.3e-37 ok
points tested: 13  failures: 1
max relative discrepancy of WRONG candidates against the same numerics:
    prim  tau(x^2+x'^2)/4        2.0
    no tau^2/12 term             1.0
    cross-term coeff doubled     0.9999
    tau^2/6 instead of tau^2/12  1.0

real	13m16.778s
user	13m5.714s
sys	0m0.467s
```

Cause: I had used the relative error estimate of each inner integral. At $x=x'=0$ the inner value is $\sigma^2/2\to0$ as $u\to0$, so an absolute estimate of $\sim10^{-37}$ became large in relative terms. Change (run 3): the criterion now bounds the contribution of inner-integral errors to $I$, namely $\tau\max|{\rm err}_y|/I$. A non-convergence of run 1's kind (inner relative error $\sim6\times10^{-4}$ on values of order one, now that the integrand is scaled) would give $\sim10^{-3}$ here and would still be flagged. The code changes are shown verbatim below. For run 0 the single changed line was `ystar = mp.findroot(dg, (x + xp)/2)` (default solver, default verification), which became the secant call visible in the final code. Diff of the run-1 script against the final script (`diff check_a_run1.py check_a.py`):

```
23a24,39
> # REVISION NOTE (run 2). Run 1 (check_a_run1.py, output out_a_run1_FAILED.txt) integrated
> # rho0*V*rho0 over y and divided by rho0(x,x';tau) afterwards. At the 5 points with large
> # (x-x')^2/tau the integrand is ~exp(-(x-x')^2/(2 tau)) (e.g. e^-8000), mpmath's tanh-sinh
> # stopping test is absolute, so it stopped at low degree (its own error estimate was 5.8e-4
> # relative) and I_num came out low by 3.5e-8 relative. The fix moves the constant factor
> # 1/rho0(x,x';tau) inside the y-integral (an identity), so the integrand is O(1), and records
> # mpmath's own error estimates so a non-converged quadrature is visible.
> # REVISION NOTE (run 3). Run 2 (check_a_run2.py, out_a_run2_1FAIL.txt) agreed with the closed
> # form to ~1e-31 at all 13 points but flagged (0,0,1) as FAIL because the new quadrature
> # criterion used the RELATIVE error estimate of each inner y-integral; at x=x'=0 the inner
> # value is sigma^2/2 -> 0 as u -> 0, so a ~1e-37 absolute estimate became 6.8e-7 relative.
> # The criterion now bounds the contribution of inner errors to I: tau*max|err_y| / I. A
> # non-convergence like run 1's (relative error ~6e-4 on inner values of order 1, now that the
> # integrand is scaled by 1/rho0) would give ~1e-3 here and still be flagged.
> MAXERR = [mp.mpf(0)]
> 
25c41
<     """int dy rho0(x,y;u) V(y) rho0(y,xp;tau-u), by quadrature."""
---
>     """(1/rho0(x,xp;tau)) int dy rho0(x,y;u) V(y) rho0(y,xp;tau-u), by quadrature."""
34,35c50,54
<     f = lambda yy: rho0(x, yy, u)*V(yy)*rho0(yy, xp, tau - u)
<     return mp.quad(f, pts)
---
>     r = rho0(x, xp, tau)
>     f = lambda yy: rho0(x, yy, u)*V(yy)*rho0(yy, xp, tau - u)/r
>     val, err = mp.quad(f, pts, error=True)
>     MAXERR[0] = max(MAXERR[0], abs(err))           # absolute error estimate of inner integral
>     return val
39,40c58,60
<     r = rho0(x, xp, tau)
<     return mp.quad(lambda uu: inner(x, xp, tau, uu)/r, [0, tau/4, tau/2, 3*tau/4, tau])
---
>     MAXERR[0] = mp.mpf(0)
>     val, err = mp.quad(lambda uu: inner(x, xp, tau, uu), [0, tau/4, tau/2, 3*tau/4, tau], error=True)
>     return val, abs(err)/abs(val), tau*MAXERR[0]/abs(val)
64c84,85
< print(f"{'x':>9} {'xp':>9} {'tau':>11} {'I_num':>22} {'I_closed':>22} {'relerr':>10} {'w relerr':>10}")
---
> print(f"{'x':>9} {'xp':>9} {'tau':>11} {'I_num':>22} {'I_closed':>22} {'relerr':>10} "
>       f"{'w relerr':>10} {'quad_u':>8} {'quad_y':>8}")
66c87
<     In = I_num(a, b, t)
---
>     In, eu, ey = I_num(a, b, t)
70c91
<     ok = (rel < TOL) and mp.isfinite(In)
---
>     ok = (rel < TOL) and mp.isfinite(In) and eu < TOL and ey < TOL
73c94,95
<           f"{mp.nstr(rel, 3):>10} {mp.nstr(wrel, 3):>10} {'ok' if ok else 'FAIL'}")
---
>           f"{mp.nstr(rel, 3):>10} {mp.nstr(wrel, 3):>10} {mp.nstr(eu, 2):>8} {mp.nstr(ey, 2):>8} "
>           f"{'ok' if ok else 'FAIL'}")
```

Diff of the run-2 script against the final script (`diff check_a_run2.py check_a.py`):

```
30a31,37
> # REVISION NOTE (run 3). Run 2 (check_a_run2.py, out_a_run2_1FAIL.txt) agreed with the closed
> # form to ~1e-31 at all 13 points but flagged (0,0,1) as FAIL because the new quadrature
> # criterion used the RELATIVE error estimate of each inner y-integral; at x=x'=0 the inner
> # value is sigma^2/2 -> 0 as u -> 0, so a ~1e-37 absolute estimate became 6.8e-7 relative.
> # The criterion now bounds the contribution of inner errors to I: tau*max|err_y| / I. A
> # non-convergence like run 1's (relative error ~6e-4 on inner values of order 1, now that the
> # integrand is scaled by 1/rho0) would give ~1e-3 here and still be flagged.
46c53
<     MAXERR[0] = max(MAXERR[0], abs(err)/max(abs(val), mp.mpf('1e-300')))
---
>     MAXERR[0] = max(MAXERR[0], abs(err))           # absolute error estimate of inner integral
53c60
<     return val, abs(err)/abs(val), MAXERR[0]
---
>     return val, abs(err)/abs(val), tau*MAXERR[0]/abs(val)
```

`check_c.py`, run 0. In the first version C5 printed $R_n$, $P_n$ next to a prediction truncated at $O(\tau^2)$ (bridge) and $O(1)$ (primitive), with no failure criterion. Because a check that cannot fail is worth little, I added a quantitative criterion before run 1. That made the check stricter, not looser. The run-0 C5 and C6 lines, verbatim from the round-2 re-run of the rebuilt `check_c_run0.py`. Its C1–C4 lines are identical to the final run's, as `validate_reruns.py` confirms:

```
C5 from grid eigenvalues: R_n = [E_n-(n+1/2) - (2n+1)tau^2/48]/tau^3 (bridge, predicted -1/144 + 3(2n+1)tau/1280 - tau^2/1296 + O(tau^3));
   P_n = [E_n-(n+1/2) + (2n+1)tau^2/48]/tau^4 (primitive, predicted 3(2n+1)/1280 + O(tau^2))
  tau=0.40 bridge  n=0: R=-0.006116 pred=-0.006130  n=1: R=-0.004206 pred=-0.004255  n=2: R=-0.002296 pred=-0.002380  n=3: R=-0.000386 pred=-0.000505
  tau=0.40 prim    n=0: P=0.002289 pred=0.002344  n=1: P=0.006868 pred=0.007031  n=2: P=0.011447 pred=0.011719  n=3: P=0.016026 pred=0.016406
  tau=0.20 bridge  n=0: R=-0.006505 pred=-0.006507  n=1: R=-0.005563 pred=-0.005569  n=2: R=-0.004621 pred=-0.004632  n=3: R=-0.003679 pred=-0.003694
  tau=0.20 prim    n=0: P=0.002330 pred=0.002344  n=1: P=0.006990 pred=0.007031  n=2: P=0.011649 pred=0.011719  n=3: P=0.016309 pred=0.016406
  tau=0.10 bridge  n=0: R=-0.006718 pred=-0.006718  n=1: R=-0.006248 pred=-0.006249  n=2: R=-0.005779 pred=-0.005780  n=3: R=-0.005310 pred=-0.005312
  tau=0.10 prim    n=0: P=0.002340 pred=0.002344  n=1: P=0.007021 pred=0.007031  n=2: P=0.011701 pred=0.011719  n=3: P=0.016382 pred=0.016406
  tau=0.05 bridge  n=0: R=-0.006829 pred=-0.006829  n=1: R=-0.006595 pred=-0.006595  n=2: R=-0.006360 pred=-0.006360  n=3: R=-0.006126 pred=-0.006126
  tau=0.05 prim    n=0: P=0.002343 pred=0.002344  n=1: P=0.007029 pred=0.007031  n=2: P=0.011714 pred=0.011719  n=3: P=0.016400 pred=0.016406
C6 E_0^bridge(tau) >= 1/2 on 400 log-spaced tau in [1e-3, 31.6]: violations = 0; min(E_0 - 1/2) = 2.083e-08 at tau = 1.000e-03
TOTAL FAILURES: 0
```

`check_c.py`, run 1. C5 failed at $\tau=0.4$, primitive, $n=2,3$ ($d = 7.4\times10^{-6}$, $1.0\times10^{-5}$ against a tolerance of $5\times10^{-6}$). The predictions then stopped at the leading omitted order. The omitted remainder visibly scales as $\tau^4$ ($1.0\times10^{-5}\to6.6\times10^{-7}\to4.3\times10^{-8}$ for $n=3$ as $\tau$ halves), and its size matches the next series term $35(2n+1)\tau^4/589824 = 1.06\times10^{-5}$ at $n=3$, $\tau=0.4$. Change (run 2): add the next analytic series terms of the closed form to the prediction, keeping the tolerance. The run-1 prediction lines were `pred = -1/144 + 3*(2*nn + 1)*t/1280 - t*t/1296 + 103*(2*nn + 1)*t**3/387072` and `predP = 3*(2*nn + 1)/1280 - 5*(2*nn + 1)*t*t/14336`; the final ones are in the listing below. The run-1 script was edited in place in round 1; it was rebuilt for round 2 as `check_c_run1.py`. The coefficients under test ($\tau^2$, $\tau^3$, $\tau^4$) were unchanged. The run-1 C5 and C6 lines, verbatim from the round-2 re-run of `check_c_run1.py`. Its full output is identical to the round-1 record, as `validate_reruns.py` confirms:

```
C5 from grid eigenvalues: R_n = [E_n-(n+1/2) - (2n+1)tau^2/48]/tau^3 (bridge, predicted -1/144 + 3(2n+1)tau/1280 - tau^2/1296 + 103(2n+1)tau^3/387072 + O(tau^4));
   P_n = [E_n-(n+1/2) + (2n+1)tau^2/48]/tau^4 (primitive, predicted 3(2n+1)/1280 - 5(2n+1)tau^2/14336 + O(tau^4))
   failure if |R_n - pred| or |P_n - pred| > 5e-6 at any tau <= 0.4, n <= 3
  tau=0.40 bridge  n=0: R=-0.0061155 d=-2.2e-06  n=1: R=-0.0042057 d=-1.4e-06  n=2: R=-0.0022959 d=-6.8e-07  n=3: R=-0.0003861 d=+5.8e-08
  tau=0.40 prim    n=0: P=0.0022894 d=+1.5e-06  n=1: P=0.0068683 d=+4.4e-06  n=2: P=0.0114471 d=+7.4e-06  n=3: P=0.0160260 d=+1.0e-05
  tau=0.20 bridge  n=0: R=-0.0065046 d=-1.4e-07  n=1: R=-0.0055628 d=-1.2e-07  n=2: R=-0.0046210 d=-9.8e-08  n=3: R=-0.0036792 d=-7.6e-08
  tau=0.20 prim    n=0: P=0.0023299 d=+9.4e-08  n=1: P=0.0069897 d=+2.8e-07  n=2: P=0.0116495 d=+4.7e-07  n=3: P=0.0163093 d=+6.6e-07
  tau=0.10 bridge  n=0: R=-0.0067175 d=-9.2e-09  n=1: R=-0.0062482 d=-8.5e-09  n=2: R=-0.0057790 d=-7.7e-09  n=3: R=-0.0053097 d=-7.0e-09
  tau=0.10 prim    n=0: P=0.0023403 d=+7.4e-09  n=1: P=0.0070208 d=+1.9e-08  n=2: P=0.0117013 d=+3.1e-08  n=3: P=0.0163819 d=+4.3e-08
  tau=0.05 bridge  n=0: R=-0.0068292 d=-5.5e-12  n=1: R=-0.0065947 d=+3.7e-10  n=2: R=-0.0063603 d=+3.1e-10  n=3: R=-0.0061258 d=+3.3e-11
  tau=0.05 prim    n=0: P=0.0023429 d=+1.9e-08  n=1: P=0.0070286 d=+1.3e-08  n=2: P=0.0117144 d=+1.0e-08  n=3: P=0.0164002 d=+2.0e-08
C6 E_0^bridge(tau) >= 1/2 on 400 log-spaced tau in [1e-3, 31.6]: violations = 0; min(E_0 - 1/2) = 2.083e-08 at tau = 1.000e-03
TOTAL FAILURES: 2
```

`check_b.py`, run 1. It printed two `RuntimeWarning: divide by zero encountered in log` lines. The source was the row $2e_i$ of the polarisation matrix, where $w$ underflows to 0 at $\tau=0.002$. That row is overwritten by the diagonal formula and never used. Run 2 sets that row to $e_i$; all printed numbers are identical between the runs. Verbatim `diff out_b_run1.txt out_b.txt` for the round-2 re-runs of `check_b_run1.py` (rebuilt) and `check_b.py`; the final script was run under `time`, so its timing lines also appear:

```
1,4d0
< /home/claude/p003/r2/check_b_run1.py:74: RuntimeWarning: divide by zero encountered in log
<   return -np.log(w)
< /home/claude/p003/r2/check_b_run1.py:78: RuntimeWarning: divide by zero encountered in log
<   return -np.log(w)
63a60,63
> 
> real	1m23.918s
> user	0m57.163s
> sys	0m0.034s
```

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
# check_algebra.py -- symbolic checks for P003.S03
# Python 3.13.18, sympy 1.14.0, mpmath 1.3.0. Deterministic (no random numbers).
# Run: python3 -I check_algebra.py
#
# S1  recomputes the bridge integral from the DEFINITION with sympy's own integrator
#     (no completing-the-square supplied by hand), under the assumption 0 < u < tau.
# S2  checks the hand completion of the square (algebra only).
# S3  builds the m x m Hessian of the closed-ring action from w (eq. a) for m = 1..7,
#     symbolically, and compares det(tau*A) with the closed form D_m^2.
# S4  same for the primitive product rho0 * exp(-tau V(x_n)).
# S5  identities c = (kappa+tau/2)^2, q = (kappa-tau/2)/(kappa+tau/2) from A, B.
# S6  small-tau series of E_n(tau), n symbolic, both kernels.
import sympy as sp

x, xp, y = sp.symbols('x xp y', real=True)
u, tau = sp.symbols('u tau', positive=True)
n = sp.symbols('n', nonnegative=True, integer=True)

def rho0(a, b, t):
    return (2*sp.pi*t)**sp.Rational(-1, 2)*sp.exp(-(a - b)**2/(2*t))

V = lambda z: z**2/2

# ---------- S1: y- and u-integrals from the definition ----------
# Assumption [A1]: 0 < u < tau (encoded as v = tau - u > 0).
v = sp.symbols('v', positive=True)
integrand_y = rho0(x, y, u)*V(y)*rho0(y, xp, v)/rho0(x, xp, u + v)
Iy = sp.integrate(sp.expand(integrand_y), (y, -sp.oo, sp.oo), conds='none')
Iy = sp.simplify(Iy)
Iy_tau = sp.simplify(Iy.subs(v, tau - u))
print("S1 inner y-integral (sympy):", sp.factor(Iy_tau))
Iu = sp.integrate(sp.expand(Iy_tau), (u, 0, tau))
Iu = sp.simplify(Iu)
claimed = tau*(x**2 + x*xp + xp**2)/6 + tau**2/12
print("S1 u-integral (sympy):", sp.expand(Iu))
print("S1 claimed           :", sp.expand(claimed))
print("S1 difference simplifies to:", sp.simplify(Iu - claimed))

# ---------- S2: hand completion of the square ----------
ybar = ((tau - u)*x + u*xp)/tau
sig2 = u*(tau - u)/tau
lhs = sp.log(rho0(x, y, u)*rho0(y, xp, tau - u)/rho0(x, xp, tau))
rhs = sp.log((2*sp.pi*sig2)**sp.Rational(-1, 2)*sp.exp(-(y - ybar)**2/(2*sig2)))
print("S2 log(bridge ratio) - log(Gaussian(ybar, sig2)) =",
      sp.simplify(sp.expand_log(lhs - rhs, force=True)))

# ---------- S3/S4: Hessians of closed-ring actions ----------
kap = sp.sqrt(1 + tau**2/12)
kapP = sp.sqrt(1 + tau**2/4)

def w_closed(a, b, t):
    return rho0(a, b, t)*sp.exp(-t*(a**2 + a*b + b**2)/6 - t**2/12)

def bond_prim(a, b, t):
    return rho0(a, b, t)*sp.exp(-t*V(a))

def D_closed(k, t, m):
    return (k + t/2)**m - (k - t/2)**m

for label, bond, k in (("S3 bridge   ", w_closed, kap), ("S4 primitive", bond_prim, kapP)):
    for m in range(1, 8):
        xs = sp.symbols('x1:%d' % (m + 1), real=True)
        S = 0
        for i in range(m):
            S += -sp.expand_log(sp.log(bond(xs[i], xs[(i + 1) % m], tau)), force=True)
        H = sp.hessian(S, xs)
        det_tauA = sp.expand((tau*H).det())
        Dm2 = sp.expand(D_closed(k, tau, m)**2)
        diff = sp.simplify(det_tauA - Dm2)
        print(f"{label} m={m}: det(tau*A) - D_m^2 = {diff}")

# ---------- S5: kernel parameters -> c, q ----------
A = 1/tau + tau/3
B = 1/tau - tau/6
kk = sp.sqrt(A**2 - B**2)
print("S5 kappa^2 - (1+tau^2/12) =", sp.simplify(kk**2 - (1 + tau**2/12)))
c_expr = tau*(A + kap)
print("S5 tau(A+kappa) - (kappa+tau/2)^2 =", sp.simplify(sp.expand(c_expr - (kap + tau/2)**2)))
q_expr = B/(A + kap)
print("S5 B/(A+kappa) - (kappa-tau/2)/(kappa+tau/2) =",
      sp.simplify(q_expr - (kap - tau/2)/(kap + tau/2)))
AP = 1/tau + tau/2
BP = 1/tau
print("S5 primitive: AP^2-BP^2 - (1+tau^2/4) =", sp.simplify(AP**2 - BP**2 - (1 + tau**2/4)))
print("S5 primitive: tau(AP+kapP) - (kapP+tau/2)^2 =",
      sp.simplify(sp.expand(tau*(AP + kapP) - (kapP + tau/2)**2)))
print("S5 primitive: BP/(AP+kapP) - (kapP-tau/2)/(kapP+tau/2) =",
      sp.simplify(BP/(AP + kapP) - (kapP - tau/2)/(kapP + tau/2)))

# ---------- S6: small-tau series ----------
En_b = tau/12 + sp.log(kap + tau/2)/tau + n/tau*sp.log((kap + tau/2)/(kap - tau/2))
En_p = -(sp.log(1/(kapP + tau/2)) + n*sp.log((kapP - tau/2)/(kapP + tau/2)))/tau
sb = sp.series(En_b - (n + sp.Rational(1, 2)), tau, 0, 7).removeO()
sp_ = sp.series(En_p - (n + sp.Rational(1, 2)), tau, 0, 7).removeO()
print("S6 bridge   E_n-(n+1/2) =", sp.collect(sp.expand(sb), tau, sp.factor))
print("S6 primitive E_n-(n+1/2) =", sp.collect(sp.expand(sp_), tau, sp.factor))
# alternative closed form of the bridge levels: (n+1/2)*Omega + tau/12 + log(1-tau^2/6)/(2 tau)
Om = 2/tau*sp.atanh(tau/(2*kap))
alt = (n + sp.Rational(1, 2))*Om + tau/12 + sp.log(1 - tau**2/6)/(2*tau)
for tv in (sp.Rational(1, 10), sp.Rational(7, 5), sp.Rational(12, 5)):
    for nv in (0, 3):
        d = (En_b - alt).subs({tau: tv, n: nv}).evalf(30)
        print(f"S6 alt-form difference at tau={tv}, n={nv}: {d}")
```

Output (verbatim, round-2 re-run):

```
S1 inner y-integral (sympy): (tau**2*u + tau**2*x**2 - tau*u**2 - 2*tau*u*x**2 + 2*tau*u*x*xp + u**2*x**2 - 2*u**2*x*xp + u**2*xp**2)/(2*tau**2)
S1 u-integral (sympy): tau**2/12 + tau*x**2/6 + tau*x*xp/6 + tau*xp**2/6
S1 claimed           : tau**2/12 + tau*x**2/6 + tau*x*xp/6 + tau*xp**2/6
S1 difference simplifies to: 0
S2 log(bridge ratio) - log(Gaussian(ybar, sig2)) = 0
S3 bridge    m=1: det(tau*A) - D_m^2 = 0
S3 bridge    m=2: det(tau*A) - D_m^2 = 0
S3 bridge    m=3: det(tau*A) - D_m^2 = 0
S3 bridge    m=4: det(tau*A) - D_m^2 = 0
S3 bridge    m=5: det(tau*A) - D_m^2 = 0
S3 bridge    m=6: det(tau*A) - D_m^2 = 0
S3 bridge    m=7: det(tau*A) - D_m^2 = 0
S4 primitive m=1: det(tau*A) - D_m^2 = 0
S4 primitive m=2: det(tau*A) - D_m^2 = 0
S4 primitive m=3: det(tau*A) - D_m^2 = 0
S4 primitive m=4: det(tau*A) - D_m^2 = 0
S4 primitive m=5: det(tau*A) - D_m^2 = 0
S4 primitive m=6: det(tau*A) - D_m^2 = 0
S4 primitive m=7: det(tau*A) - D_m^2 = 0
S5 kappa^2 - (1+tau^2/12) = 0
S5 tau(A+kappa) - (kappa+tau/2)^2 = 0
S5 B/(A+kappa) - (kappa-tau/2)/(kappa+tau/2) = 0
S5 primitive: AP^2-BP^2 - (1+tau^2/4) = 0
S5 primitive: tau(AP+kapP) - (kapP+tau/2)^2 = 0
S5 primitive: BP/(AP+kapP) - (kapP-tau/2)/(kapP+tau/2) = 0
S6 bridge   E_n-(n+1/2) = 103*tau**6*(2*n + 1)/387072 - tau**5/1296 + 3*tau**4*(2*n + 1)/1280 - tau**3/144 + tau**2*(2*n + 1)/48
S6 primitive E_n-(n+1/2) = -5*tau**6*(2*n + 1)/14336 + 3*tau**4*(2*n + 1)/1280 - tau**2*(2*n + 1)/48
S6 alt-form difference at tau=1/10, n=0: -0E-167
S6 alt-form difference at tau=1/10, n=3: -0E-165
S6 alt-form difference at tau=7/5, n=0: -0E-165
S6 alt-form difference at tau=7/5, n=3: 0E-165
S6 alt-form difference at tau=12/5, n=0: -0E-166
S6 alt-form difference at tau=12/5, n=3: 0E-165

real	0m10.299s
user	0m6.051s
sys	0m0.104s
```

#### A: `check_a.py` — $w$ against direct numerical evaluation of its definition `[N]`

What it tests. At 13 points ($8$ random with seed 20261112, plus $(0,0,1)$; widely separated endpoints at small $\tau$, $(2,-2,10^{-3})$; large $\tau=20$; $\tau=5$ with $x=-4$, $x'=3$; and $\tau=\sqrt6$), it computes $I$ by nested 30-digit tanh-sinh quadrature of the definition. The $y$-breakpoints are found numerically from the integrand, so the check does not import $\bar y$ or $\sigma^2$. It compares the result with (8). Failure: relative difference $>10^{-12}$, or mpmath error estimates above that level. It also reports the discrepancy of four wrong candidate formulas (primitive symmetric split, missing $\tau^2/12$, doubled cross term, $\tau^2/6$) against the same numerics, to show the check discriminates.

What it would catch: any error in (8) or (9) larger than $10^{-12}$ relative at these points, including wrong coefficients of $x^2$, $xx'$, $x'^2$ or of the constant, since the points vary all of these.

What it would not catch: an error that vanishes at all 13 points (implausible for a polynomial in $x,x'$ with $\tau$-dependent coefficients, but not excluded). It also would not catch a misreading of the problem's definition shared between the code and the derivation; the code transcribes the definition literally, as written in the prompt.

```python
# check_a.py -- part (a): closed-form w against direct numerical evaluation of its DEFINITION.
# Python 3.13.18, mpmath 1.3.0, numpy 2.5.3 (numpy only for the seeded RNG).
# Run: python3 -I check_a.py
#
# The exponent I(x,x';tau) = int_0^tau du (1/rho0(x,x';tau)) int dy rho0(x,y;u) V(y) rho0(y,x';tau-u)
# is computed by nested tanh-sinh quadrature (mpmath.quad), working only with the integrand
# as written in the problem. The y-range is split at points found numerically from the
# integrand itself (the maximiser of the Gaussian part, located by mp.findroot on its
# numerical derivative, and its numerical curvature), so the quadrature does not import the
# bridge mean/variance derived in the text.
# Failure criterion: relative difference between I_num and I_closed above 1e-12 at any point.
# Discrimination: four wrong candidate closed forms are evaluated against the same I_num.
import numpy as np
import mpmath as mp

mp.mp.dps = 30

def rho0(a, b, t):
    return (2*mp.pi*t)**mp.mpf(-0.5)*mp.exp(-(a - b)**2/(2*t))

def V(z):
    return z**2/2

# REVISION NOTE (run 2). Run 1 (check_a_run1.py, output out_a_run1_FAILED.txt) integrated
# rho0*V*rho0 over y and divided by rho0(x,x';tau) afterwards. At the 5 points with large
# (x-x')^2/tau the integrand is ~exp(-(x-x')^2/(2 tau)) (e.g. e^-8000), mpmath's tanh-sinh
# stopping test is absolute, so it stopped at low degree (its own error estimate was 5.8e-4
# relative) and I_num came out low by 3.5e-8 relative. The fix moves the constant factor
# 1/rho0(x,x';tau) inside the y-integral (an identity), so the integrand is O(1), and records
# mpmath's own error estimates so a non-converged quadrature is visible.
# REVISION NOTE (run 3). Run 2 (check_a_run2.py, out_a_run2_1FAIL.txt) agreed with the closed
# form to ~1e-31 at all 13 points but flagged (0,0,1) as FAIL because the new quadrature
# criterion used the RELATIVE error estimate of each inner y-integral; at x=x'=0 the inner
# value is sigma^2/2 -> 0 as u -> 0, so a ~1e-37 absolute estimate became 6.8e-7 relative.
# The criterion now bounds the contribution of inner errors to I: tau*max|err_y| / I. A
# non-convergence like run 1's (relative error ~6e-4 on inner values of order 1, now that the
# integrand is scaled by 1/rho0) would give ~1e-3 here and still be flagged.
MAXERR = [mp.mpf(0)]

def inner(x, xp, tau, u):
    """(1/rho0(x,xp;tau)) int dy rho0(x,y;u) V(y) rho0(y,xp;tau-u), by quadrature."""
    g = lambda yy: -(yy - x)**2/(2*u) - (yy - xp)**2/(2*(tau - u))   # log of Gaussian part
    dg = lambda yy: mp.diff(g, yy)
    # numerical maximiser: secant iteration on the numerical derivative (verify=False because
    # for tiny u the derivative is O(1/u) and the absolute residual test is meaningless)
    ystar = mp.findroot(dg, (x, xp + mp.mpf('1e-3')), solver='secant', verify=False)
    curv = -mp.diff(g, ystar, 2)                                       # numerical curvature
    s = 1/mp.sqrt(curv)
    pts = [-mp.inf] + [ystar + k*s for k in (-40, -12, -5, -2, 0, 2, 5, 12, 40)] + [mp.inf]
    r = rho0(x, xp, tau)
    f = lambda yy: rho0(x, yy, u)*V(yy)*rho0(yy, xp, tau - u)/r
    val, err = mp.quad(f, pts, error=True)
    MAXERR[0] = max(MAXERR[0], abs(err))           # absolute error estimate of inner integral
    return val

def I_num(x, xp, tau):
    x, xp, tau = mp.mpf(x), mp.mpf(xp), mp.mpf(tau)
    MAXERR[0] = mp.mpf(0)
    val, err = mp.quad(lambda uu: inner(x, xp, tau, uu), [0, tau/4, tau/2, 3*tau/4, tau], error=True)
    return val, abs(err)/abs(val), tau*MAXERR[0]/abs(val)

def I_closed(x, xp, tau):
    return tau*(x**2 + x*xp + xp**2)/6 + tau**2/12

wrong = {
    "prim  tau(x^2+x'^2)/4       ": lambda x, xp, t: t*(x**2 + xp**2)/4,
    "no tau^2/12 term            ": lambda x, xp, t: t*(x**2 + x*xp + xp**2)/6,
    "cross-term coeff doubled    ": lambda x, xp, t: t*(x**2 + 2*x*xp + xp**2)/6 + t**2/12,
    "tau^2/6 instead of tau^2/12 ": lambda x, xp, t: t*(x**2 + x*xp + xp**2)/6 + t**2/6,
}

rng = np.random.default_rng(20261112)
pts = []
for _ in range(8):
    x0, x1 = rng.uniform(-3, 3, size=2)
    t0 = 10**rng.uniform(-2, 1)
    pts.append((float(x0), float(x1), float(t0)))
# boundary / special points
pts += [(0.0, 0.0, 1.0), (2.0, -2.0, 1e-3), (1.5, 1.5, 20.0), (-4.0, 3.0, 5.0), (0.7, -0.7, 2.449489742783178)]

TOL = mp.mpf('1e-12')
nfail = 0
worst = {k: mp.mpf(0) for k in wrong}
print(f"{'x':>9} {'xp':>9} {'tau':>11} {'I_num':>22} {'I_closed':>22} {'relerr':>10} "
      f"{'w relerr':>10} {'quad_u':>8} {'quad_y':>8}")
for (a, b, t) in pts:
    In, eu, ey = I_num(a, b, t)
    Ic = I_closed(mp.mpf(a), mp.mpf(b), mp.mpf(t))
    rel = abs(In - Ic)/abs(Ic)
    wrel = abs(mp.exp(Ic - In) - 1)        # relative error of w = rho0*exp(-I)
    ok = (rel < TOL) and mp.isfinite(In) and eu < TOL and ey < TOL
    nfail += (not ok)
    print(f"{a:9.4f} {b:9.4f} {t:11.6g} {mp.nstr(In, 18):>22} {mp.nstr(Ic, 18):>22} "
          f"{mp.nstr(rel, 3):>10} {mp.nstr(wrel, 3):>10} {mp.nstr(eu, 2):>8} {mp.nstr(ey, 2):>8} "
          f"{'ok' if ok else 'FAIL'}")
    for k, fw in wrong.items():
        worst[k] = max(worst[k], abs(In - fw(mp.mpf(a), mp.mpf(b), mp.mpf(t)))/abs(In))
print("points tested:", len(pts), " failures:", nfail)
print("max relative discrepancy of WRONG candidates against the same numerics:")
for k in wrong:
    print("   ", k, mp.nstr(worst[k], 4))
```

Output (verbatim, round-2 re-run of the final script):

```
        x        xp         tau                  I_num               I_closed     relerr   w relerr   quad_u   quad_y
   2.2477   -2.4016    0.107549  0.0981494721219007529  0.0981494721219007529        0.0        0.0  4.1e-54  2.3e-38 ok
   2.3127   -2.2680   0.0974188  0.0859851795829655646  0.0859851795829655646   1.43e-31        0.0  4.7e-54  2.4e-38 ok
  -1.0765    0.9027   0.0242251 0.00409409783494425554 0.00409409783494425554        0.0        0.0  9.8e-56  1.8e-37 ok
  -1.1283   -2.4229    0.159145   0.264092691081447326   0.264092691081447326        0.0        0.0  1.5e-56  1.3e-38 ok
  -2.6895   -0.5887     4.74681    9.12709027547319101    9.12709027547319101   1.73e-31   1.58e-30  4.4e-57  2.1e-38 ok
  -2.4006    1.8476   0.0330348   0.026195200985980636   0.026195200985980636   1.18e-31        0.0  1.5e-54  2.6e-38 ok
  -2.2063   -2.4695     4.59742    14.3389344162538047    14.3389344162538047        0.0        0.0  2.8e-54  3.2e-39 ok
  -0.6498    0.1282     3.91834    1.51150624118418907    1.51150624118418907    1.3e-31   1.97e-31  2.6e-54  1.0e-37 ok
   0.0000    0.0000           1  0.0833333333333333333  0.0833333333333333333        0.0        0.0  4.8e-55  3.4e-37 ok
   2.0000   -2.0000       0.001 0.000666750000000000014 0.000666750000000000014        0.0        0.0  6.0e-57  4.6e-38 ok
   1.5000    1.5000          20    55.8333333333333333    55.8333333333333333        0.0        0.0  7.2e-53  3.7e-39 ok
  -4.0000    3.0000           5    12.9166666666666667    12.9166666666666667   1.22e-31   1.58e-30  3.1e-52  3.9e-39 ok
   0.7000   -0.7000     2.44949   0.700041662327292746   0.700041662327292746        0.0        0.0  5.7e-56  1.1e-37 ok
points tested: 13  failures: 0
max relative discrepancy of WRONG candidates against the same numerics:
    prim  tau(x^2+x'^2)/4        2.0
    no tau^2/12 term             1.0
    cross-term coeff doubled     0.9999
    tau^2/6 instead of tau^2/12  1.0

real	14m38.427s
user	13m19.374s
sys	0m0.787s
```

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
# check_c.py -- part (c): eigenvalues of T_tau (bridge kernel w) and of the symmetric
# primitive kernel exp(-tau V/2) exp(-tau K) exp(-tau V/2), checked against
#   C1  Nystrom (trapezoid) diagonalisation of the kernel on a uniform grid, two grid sizes;
#   C2  reconstruction of the kernel from the claimed spectrum via Mehler's formula
#       (DLMF 18.18.28), an independent identity;
#   C3  Hilbert-Schmidt norm: grid value of int int w^2 against sum_n lambda_n^2
#       (tests that no eigenvalue is missing, without invoking completeness);
#   C4  the (b)-(c) relation: Tr (h W)^m on the grid against the closed form of Zhat_m from (b);
#   C5  small-tau coefficients of E_n - (n+1/2) extracted from GRID eigenvalues;
#   C6  variational bound E_0(tau) >= 1/2 for the bridge kernel (Jensen + Perron argument).
# Python 3.13.18, numpy 2.5.3, scipy 1.18.1, mpmath 1.3.0. Deterministic (seeded RNG).
# Run: python3 -I check_c.py
#
# The kernels are evaluated from the closed form of (a), which is checked independently
# against its definition in check_a.py. Closed forms of (c) are typed in here from the text.
import numpy as np
import mpmath as mp
from scipy.special import eval_hermite

def rho0(a, b, t):
    return np.exp(-(a - b)**2/(2*t))/np.sqrt(2*np.pi*t)

def w_bridge(a, b, t):                   # eq. (a) of the text
    return rho0(a, b, t)*np.exp(-t*(a*a + a*b + b*b)/6 - t*t/12)

def w_prim(a, b, t):                     # kernel of e^{-tV/2} e^{-tK} e^{-tV/2}
    return np.exp(-t*a*a/4)*rho0(a, b, t)*np.exp(-t*b*b/4)

# ----- closed forms of (c), as stated in the text -----
def spec_bridge(t, nmax):
    k = np.sqrt(1 + t*t/12)
    a, b = k + t/2, k - t/2
    lam = np.array([np.exp(-t*t/12)*b**n/a**(n + 1) for n in range(nmax)])
    return lam, k, b/a, np.exp(-t*t/12)/a

def spec_prim(t, nmax):
    k = np.sqrt(1 + t*t/4)
    a, b = k + t/2, k - t/2
    lam = np.array([b**n/a**(n + 1) for n in range(nmax)])
    return lam, k, b/a, 1/a

def grid_eigs(kern, t, L, h):
    xs = np.arange(-L, L + h/2, h)
    X, Y = np.meshgrid(xs, xs, indexing='ij')
    M = h*kern(X, Y, t)
    ev = np.linalg.eigvalsh(M)
    ev = ev[np.argsort(-np.abs(ev))]
    return ev, M, xs

NMAX = 8
TOL = 1e-10                    # absolute, in units of lambda_0
taus = [0.05, 0.2, 0.5, 1.0, 2.0, np.sqrt(6.0), 3.0, 5.0, 10.0]
nfail = 0
print("C1 grid diagonalisation: max_n |lam_grid - lam_closed|/lam_0 over n < 8 "
      "(h and h/2), sign pattern of grid eigenvalues")
for name, kern, spec in (("bridge", w_bridge, spec_bridge), ("prim  ", w_prim, spec_prim)):
    for t in taus:
        lam, k, q, l0 = spec(t, NMAX)
        A = 1/t + (t/3 if name == "bridge" else t/2)
        h = min(0.1, np.sqrt(t)/4, 1/(4*np.sqrt(A)))
        L = 12.0
        ev1, _, _ = grid_eigs(kern, t, L, h)
        ev2, _, _ = grid_eigs(kern, t, L, h/2)
        e1 = np.max(np.abs(ev1[:NMAX] - lam))/lam[0]
        e2 = np.max(np.abs(ev2[:NMAX] - lam))/lam[0]
        signs = ''.join('+' if s > 0 else '-' for s in ev2[:NMAX])
        ok = (e1 < TOL) and (e2 < TOL) and np.all(np.isfinite(ev2[:NMAX]))
        nfail += (not ok)
        print(f"  {name} tau={t:8.5f} q={q:+.6f} N={len(ev2):5d} err(h)={e1:.2e} err(h/2)={e2:.2e} "
              f"grid signs {signs}  {'ok' if ok else 'FAIL'}")
# tau = sqrt(6): rank one
ev, _, _ = grid_eigs(w_bridge, np.sqrt(6.0), 12.0, 0.05)
print(f"  bridge tau=sqrt6: |lam_1/lam_0| on grid = {abs(ev[1]/ev[0]):.2e} (closed form: 0)")
nfail += not (abs(ev[1]/ev[0]) < TOL)

# ----- C2: Mehler reconstruction -----
# DLMF 18.18.28: sum_n H_n(X)H_n(Y) z^n/(2^n n!) = (1-z^2)^{-1/2} exp((2XYz-(X^2+Y^2)z^2)/(1-z^2)), |z|<1.
# Claimed: kernel = sum_n lam_0 q^n phi_n(x)phi_n(x')/||phi_n||^2, phi_n = H_n(sqrt(k) x) e^{-k x^2/2},
# ||phi_n||^2 = 2^n n! sqrt(pi)/sqrt(k).  Then kernel = lam_0 sqrt(k/pi) e^{-k(x^2+x'^2)/2} * Mehler(X,Y,q).
print("C2 Mehler reconstruction of the kernel from the claimed spectrum (max relative error)")
rng = np.random.default_rng(7)
for name, kern, spec in (("bridge", w_bridge, spec_bridge), ("prim  ", w_prim, spec_prim)):
    for t in taus:
        lam, k, q, l0 = spec(t, 1)
        xs = rng.uniform(-3, 3, size=(20, 2))
        worst = 0.0
        for (a, b) in xs:
            X, Y = np.sqrt(k)*a, np.sqrt(k)*b
            mehler = (1 - q*q)**-0.5*np.exp((2*X*Y*q - (X*X + Y*Y)*q*q)/(1 - q*q))
            rec = l0*np.sqrt(k/np.pi)*np.exp(-k*(a*a + b*b)/2)*mehler
            worst = max(worst, abs(rec/kern(a, b, t) - 1))
        ok = worst < 1e-12
        nfail += (not ok)
        print(f"  {name} tau={t:8.5f}: {worst:.2e} {'ok' if ok else 'FAIL'}")
# and a truncated-series version (explicit Hermite functions), one case with q<0
t = 5.0
lam, k, q, l0 = spec_bridge(t, 60)
a, b = 0.37, -1.21
s = sum(lam[n]*eval_hermite(n, np.sqrt(k)*a)*eval_hermite(n, np.sqrt(k)*b)
        *np.exp(-k*(a*a + b*b)/2)/(2.0**n*mp.factorial(n)*np.sqrt(np.pi)/np.sqrt(k)) for n in range(60))
print(f"  explicit 60-term spectral sum, bridge tau=5 (q<0): rel. err = {abs(float(s)/w_bridge(a, b, t) - 1):.2e}")

# ----- C3: Hilbert-Schmidt norm -----
print("C3 Hilbert-Schmidt norm: grid int int kernel^2 vs sum_n lam_n^2 = lam_0^2/(1-q^2)")
for name, kern, spec in (("bridge", w_bridge, spec_bridge), ("prim  ", w_prim, spec_prim)):
    for t in (0.2, 1.0, 3.0, 10.0):
        lam, k, q, l0 = spec(t, 1)
        A = 1/t + (t/3 if name == "bridge" else t/2)
        h = min(0.05, np.sqrt(t)/6, 1/(6*np.sqrt(A)))
        xs = np.arange(-12, 12 + h/2, h)
        X, Y = np.meshgrid(xs, xs, indexing='ij')
        hs_grid = h*h*np.sum(kern(X, Y, t)**2)
        hs_closed = l0**2/(1 - q*q)
        rel = abs(hs_grid/hs_closed - 1)
        ok = rel < 1e-10
        nfail += (not ok)
        print(f"  {name} tau={t:5.2f}: grid {hs_grid:.15e} closed {hs_closed:.15e} rel {rel:.1e} "
              f"{'ok' if ok else 'FAIL'}")

# ----- C4: (b)-(c) relation via grid traces -----
def Zhat_closed(beta, m):                 # closed form of (b), typed from the text
    t = beta/m
    k = np.sqrt(1 + t*t/12)
    return np.exp(-beta*t/12)/((k + t/2)**m - (k - t/2)**m)

def Z_closed(beta, m):
    t = beta/m
    return 1/(2*np.sinh(m*np.arcsinh(t/2)))

print("C4 Tr (hW)^m on the grid vs closed forms of (b)")
for (beta, m) in [(1, 1), (1, 2), (1, 5), (5, 10), (10, 10), (10, 1), (10, 3), (10, 4), (5, 2)]:
    t = beta/m
    for name, kern, Zc in (("bridge", w_bridge, Zhat_closed), ("prim  ", w_prim, Z_closed)):
        A = 1/t + (t/3 if name == "bridge" else t/2)
        h = min(0.05, np.sqrt(t)/6, 1/(6*np.sqrt(A)))
        ev, M, xs = grid_eigs(kern, t, 12.0, h)
        tr = np.trace(np.linalg.matrix_power(M, m))
        rel = abs(tr/Zc(beta, m) - 1)
        ok = rel < 1e-9
        nfail += (not ok)
        print(f"  {name} beta={beta:2d} m={m:2d} tau={t:6.3f}: Tr={tr:.12e} closed={Zc(beta, m):.12e} "
              f"rel={rel:.1e} {'ok' if ok else 'FAIL'}")

# ----- C5: small-tau coefficients from GRID eigenvalues -----
# REVISION NOTE (run 2): in run 1 (out_c_run1_C5FAILED.txt) the predictions stopped at
# O(tau^3) in R_n and O(tau^2) in P_n, and the primitive case failed the 5e-6 tolerance at
# tau=0.4, n=2,3 (d = 7.4e-6, 1.0e-5), the omitted remainder scaling as tau^4 (1.0e-5 -> 6.6e-7
# -> 4.3e-8). I changed the CHECK, not the derivation: the next two analytic series terms of
# the closed form (sympy, see check_algebra-style series) were added to the predictions; the
# tolerance was kept at 5e-6. The leading coefficients under test are unchanged.
print("C5 from grid eigenvalues: R_n = [E_n-(n+1/2) - (2n+1)tau^2/48]/tau^3 (bridge, predicted "
      "-1/144 + 3(2n+1)tau/1280 - tau^2/1296 + 103(2n+1)tau^3/387072 - tau^4/10368 + 187(2n+1)tau^5/5308416 + O(tau^6));")
print("   P_n = [E_n-(n+1/2) + (2n+1)tau^2/48]/tau^4 (primitive, predicted 3(2n+1)/1280 - 5(2n+1)tau^2/14336 + 35(2n+1)tau^4/589824 + O(tau^6))")
print("   failure if |R_n - pred| or |P_n - pred| > 5e-6 at any tau <= 0.4, n <= 3")
for t in (0.4, 0.2, 0.1, 0.05):
    h = min(0.05, np.sqrt(t)/5)
    evb, _, _ = grid_eigs(w_bridge, t, 10.0, h)
    evp, _, _ = grid_eigs(w_prim, t, 10.0, h)
    rowb, rowp = [], []
    for nn in range(4):
        En = -np.log(evb[nn])/t
        R = (En - (nn + 0.5) - (2*nn + 1)*t*t/48)/t**3
        pred = (-1/144 + 3*(2*nn + 1)*t/1280 - t*t/1296 + 103*(2*nn + 1)*t**3/387072
                - t**4/10368 + 187*(2*nn + 1)*t**5/5308416)
        rowb.append(f"n={nn}: R={R:+.7f} d={R - pred:+.1e}")
        EnP = -np.log(evp[nn])/t
        P = (EnP - (nn + 0.5) + (2*nn + 1)*t*t/48)/t**4
        predP = 3*(2*nn + 1)/1280 - 5*(2*nn + 1)*t*t/14336 + 35*(2*nn + 1)*t**4/589824
        rowp.append(f"n={nn}: P={P:.7f} d={P - predP:+.1e}")
        bad = (abs(R - pred) > 5e-6) or (abs(P - predP) > 5e-6) or not np.isfinite(R + P)
        nfail += bad
    print(f"  tau={t:4.2f} bridge  " + "  ".join(rowb))
    print(f"  tau={t:4.2f} prim    " + "  ".join(rowp))

# ----- C6: E_0(tau) >= 1/2 -----
tt = np.concatenate([np.logspace(-3, 1.5, 400)])
k = np.sqrt(1 + tt*tt/12)
E0 = tt/12 + np.log(k + tt/2)/tt
viol = np.sum(E0 < 0.5 - 1e-15)
print(f"C6 E_0^bridge(tau) >= 1/2 on 400 log-spaced tau in [1e-3, 31.6]: violations = {viol}; "
      f"min(E_0 - 1/2) = {np.min(E0 - 0.5):.3e} at tau = {tt[np.argmin(E0 - 0.5)]:.3e}")
nfail += viol > 0
print("TOTAL FAILURES:", nfail)
```

Output (verbatim, round-2 re-run of the final script):

```
C1 grid diagonalisation: max_n |lam_grid - lam_closed|/lam_0 over n < 8 (h and h/2), sign pattern of grid eigenvalues
  bridge tau= 0.05000 q=+0.951224 N=  860 err(h)=8.88e-15 err(h/2)=2.36e-14 grid signs ++++++++  ok
  bridge tau= 0.20000 q=+0.818457 N=  481 err(h)=4.17e-15 err(h/2)=1.50e-14 grid signs ++++++++  ok
  bridge tau= 0.50000 q=+0.603289 N=  481 err(h)=4.14e-15 err(h/2)=1.33e-14 grid signs ++++++++  ok
  bridge tau= 1.00000 q=+0.351000 N=  481 err(h)=4.09e-15 err(h/2)=1.41e-14 grid signs ++++++++  ok
  bridge tau= 2.00000 q=+0.071797 N=  481 err(h)=3.67e-15 err(h/2)=1.44e-14 grid signs ++++++++  ok
  bridge tau= 2.44949 q=+0.000000 N=  481 err(h)=3.81e-15 err(h/2)=1.40e-14 grid signs +-++--++  ok
  bridge tau= 3.00000 q=-0.062746 N=  481 err(h)=3.98e-15 err(h/2)=1.26e-14 grid signs +-+-+-+-  ok
  bridge tau= 5.00000 q=-0.174828 N=  481 err(h)=4.27e-15 err(h/2)=1.35e-14 grid signs +-+-+-+-  ok
  bridge tau=10.00000 q=-0.241457 N=  481 err(h)=3.52e-15 err(h/2)=1.42e-14 grid signs +-+-+-+-  ok
  prim   tau= 0.05000 q=+0.951234 N=  860 err(h)=1.22e-14 err(h/2)=1.34e-14 grid signs ++++++++  ok
  prim   tau= 0.20000 q=+0.819002 N=  481 err(h)=5.03e-15 err(h/2)=1.45e-14 grid signs ++++++++  ok
  prim   tau= 0.50000 q=+0.609612 N=  481 err(h)=3.98e-15 err(h/2)=1.37e-14 grid signs ++++++++  ok
  prim   tau= 1.00000 q=+0.381966 N=  481 err(h)=3.05e-15 err(h/2)=1.42e-14 grid signs ++++++++  ok
  prim   tau= 2.00000 q=+0.171573 N=  481 err(h)=3.62e-15 err(h/2)=1.43e-14 grid signs ++++++++  ok
  prim   tau= 2.44949 q=+0.127017 N=  481 err(h)=3.58e-15 err(h/2)=1.42e-14 grid signs ++++++++  ok
  prim   tau= 3.00000 q=+0.091673 N=  481 err(h)=3.85e-15 err(h/2)=1.41e-14 grid signs ++++++++  ok
  prim   tau= 5.00000 q=+0.037088 N=  481 err(h)=3.60e-15 err(h/2)=1.43e-14 grid signs ++++++++  ok
  prim   tau=10.00000 q=+0.009805 N=  481 err(h)=3.36e-15 err(h/2)=1.43e-14 grid signs ++++++++  ok
  bridge tau=sqrt6: |lam_1/lam_0| on grid = 3.84e-16 (closed form: 0)
C2 Mehler reconstruction of the kernel from the claimed spectrum (max relative error)
  bridge tau= 0.05000: 7.48e-13 ok
  bridge tau= 0.20000: 2.60e-14 ok
  bridge tau= 0.50000: 6.66e-15 ok
  bridge tau= 1.00000: 1.78e-15 ok
  bridge tau= 2.00000: 1.78e-15 ok
  bridge tau= 2.44949: 2.22e-15 ok
  bridge tau= 3.00000: 1.55e-15 ok
  bridge tau= 5.00000: 1.89e-15 ok
  bridge tau=10.00000: 1.21e-14 ok
  prim   tau= 0.05000: 2.67e-13 ok
  prim   tau= 0.20000: 4.17e-14 ok
  prim   tau= 0.50000: 9.33e-15 ok
  prim   tau= 1.00000: 1.78e-15 ok
  prim   tau= 2.00000: 4.00e-15 ok
  prim   tau= 2.44949: 2.33e-15 ok
  prim   tau= 3.00000: 2.66e-15 ok
  prim   tau= 5.00000: 4.22e-15 ok
  prim   tau=10.00000: 4.00e-15 ok
  explicit 60-term spectral sum, bridge tau=5 (q<0): rel. err = 2.22e-16
C3 Hilbert-Schmidt norm: grid int int kernel^2 vs sum_n lam_n^2 = lam_0^2/(1-q^2)
  bridge tau= 0.20: grid 2.479260103155154e+00 closed 2.479260103155370e+00 rel 8.7e-14 ok
  bridge tau= 1.00: grid 4.066366675094277e-01 closed 4.066366675094392e-01 rel 2.8e-14 ok
  bridge tau= 3.00: grid 2.811175779765446e-02 closed 2.811175779765525e-02 rel 2.8e-14 ok
  bridge tau=10.00: grid 9.456060691663023e-10 closed 9.456060691663292e-10 rel 2.8e-14 ok
  prim   tau= 0.20: grid 2.487592975524755e+00 closed 2.487592975524971e+00 rel 8.7e-14 ok
  prim   tau= 1.00: grid 4.472135954999454e-01 closed 4.472135954999579e-01 rel 2.8e-14 ok
  prim   tau= 3.00: grid 9.245003270420225e-02 closed 9.245003270420485e-02 rel 2.8e-14 ok
  prim   tau=10.00: grid 9.805806756908925e-03 closed 9.805806756909204e-03 rel 2.9e-14 ok
C4 Tr (hW)^m on the grid vs closed forms of (b)
  bridge beta= 1 m= 1 tau= 1.000: Tr=9.200444146293e-01 closed=9.200444146293e-01 rel=1.4e-14 ok
  prim   beta= 1 m= 1 tau= 1.000: Tr=1.000000000000e+00 closed=1.000000000000e+00 rel=1.4e-14 ok
  bridge beta= 1 m= 2 tau= 0.500: Tr=9.493513564557e-01 closed=9.493513564557e-01 rel=2.8e-14 ok
  prim   beta= 1 m= 2 tau= 0.500: Tr=9.701425001453e-01 closed=9.701425001453e-01 rel=2.8e-14 ok
  bridge beta= 1 m= 5 tau= 0.200: Tr=9.578355183050e-01 closed=9.578355183050e-01 rel=7.1e-14 ok
  prim   beta= 1 m= 5 tau= 0.200: Tr=9.612426945555e-01 closed=9.612426945555e-01 rel=7.1e-14 ok
  bridge beta= 5 m=10 tau= 0.500: Tr=8.078822830950e-02 closed=8.078822830951e-02 rel=1.4e-13 ok
  prim   beta= 5 m=10 tau= 0.500: Tr=8.479224309907e-02 closed=8.479224309908e-02 rel=1.4e-13 ok
  bridge beta=10 m=10 tau= 1.000: Tr=5.761619158836e-03 closed=5.761619158836e-03 rel=1.4e-13 ok
  prim   beta=10 m=10 tau= 1.000: Tr=8.131156281816e-03 closed=8.131156281817e-03 rel=1.4e-13 ok
  bridge beta=10 m= 1 tau=10.000: Tr=2.403694764195e-05 closed=2.403694764195e-05 rel=1.4e-14 ok
  prim   beta=10 m= 1 tau=10.000: Tr=1.000000000000e-01 closed=1.000000000000e-01 rel=1.4e-14 ok
  bridge beta=10 m= 3 tau= 3.333: Tr=2.180215777399e-03 closed=2.180215777399e-03 rel=4.3e-14 ok
  prim   beta=10 m= 3 tau= 3.333: Tr=2.125984251968e-02 closed=2.125984251969e-02 rel=4.3e-14 ok
  bridge beta=10 m= 4 tau= 2.500: Tr=3.274602129981e-03 closed=3.274602129981e-03 rel=5.7e-14 ok
  prim   beta=10 m= 4 tau= 2.500: Tr=1.514412236495e-02 closed=1.514412236496e-02 rel=5.7e-14 ok
  bridge beta= 5 m= 2 tau= 2.500: Tr=5.722675219466e-02 closed=5.722675219466e-02 rel=2.8e-14 ok
  prim   beta= 5 m= 2 tau= 2.500: Tr=1.249390095109e-01 closed=1.249390095109e-01 rel=2.8e-14 ok
C5 from grid eigenvalues: R_n = [E_n-(n+1/2) - (2n+1)tau^2/48]/tau^3 (bridge, predicted -1/144 + 3(2n+1)tau/1280 - tau^2/1296 + 103(2n+1)tau^3/387072 - tau^4/10368 + 187(2n+1)tau^5/5308416 + O(tau^6));
   P_n = [E_n-(n+1/2) + (2n+1)tau^2/48]/tau^4 (primitive, predicted 3(2n+1)/1280 - 5(2n+1)tau^2/14336 + 35(2n+1)tau^4/589824 + O(tau^6))
   failure if |R_n - pred| or |P_n - pred| > 5e-6 at any tau <= 0.4, n <= 3
  tau=0.40 bridge  n=0: R=-0.0061155 d=-4.6e-08  n=1: R=-0.0042057 d=-3.0e-08  n=2: R=-0.0022959 d=-1.4e-08  n=3: R=-0.0003861 d=+2.0e-09
  tau=0.40 prim    n=0: P=0.0022894 d=-4.3e-08  n=1: P=0.0068683 d=-1.3e-07  n=2: P=0.0114471 d=-2.2e-07  n=3: P=0.0160260 d=-3.0e-07
  tau=0.20 bridge  n=0: R=-0.0065046 d=-7.6e-10  n=1: R=-0.0055628 d=-6.3e-10  n=2: R=-0.0046210 d=-5.1e-10  n=3: R=-0.0036792 d=-3.9e-10
  tau=0.20 prim    n=0: P=0.0023299 d=-6.5e-10  n=1: P=0.0069897 d=-2.0e-09  n=2: P=0.0116495 d=-3.4e-09  n=3: P=0.0163093 d=-4.8e-09
  tau=0.10 bridge  n=0: R=-0.0067175 d=+1.3e-10  n=1: R=-0.0062482 d=+1.2e-10  n=2: R=-0.0057790 d=+1.4e-10  n=3: R=-0.0053097 d=+1.3e-10
  tau=0.10 prim    n=0: P=0.0023403 d=+1.5e-09  n=1: P=0.0070208 d=+1.2e-09  n=2: P=0.0117013 d=+1.3e-09  n=3: P=0.0163819 d=+1.3e-09
  tau=0.05 bridge  n=0: R=-0.0068292 d=+5.9e-10  n=1: R=-0.0065947 d=+9.4e-10  n=2: R=-0.0063603 d=+8.6e-10  n=3: R=-0.0061258 d=+5.6e-10
  tau=0.05 prim    n=0: P=0.0023429 d=+1.9e-08  n=1: P=0.0070286 d=+1.2e-08  n=2: P=0.0117144 d=+8.5e-09  n=3: P=0.0164002 d=+1.8e-08
C6 E_0^bridge(tau) >= 1/2 on 400 log-spaced tau in [1e-3, 31.6]: violations = 0; min(E_0 - 1/2) = 2.083e-08 at tau = 1.000e-03
TOTAL FAILURES: 0

real	0m2.420s
user	0m1.308s
sys	0m0.042s
```

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
# check_b.py -- part (b): closed forms of Zhat_m, Z_m, Ehat_m, E_m; table; second route.
# Python 3.13.18, numpy 2.5.3, mpmath 1.3.0. Deterministic (no random numbers).
# Run: python3 -I check_b.py
#
# B1  table from the closed forms of the text (mpmath, 30 digits), plus exact 1/2 coth(beta/2).
# B2  SECOND ROUTE: for each (beta, m) build the m x m Hessian H of the closed-ring action
#     S(x) = -sum_n ln w(x_n, x_{n+1}) numerically by polarisation (S evaluated from the
#     closed form of (a); no circulant algebra, no product formula), the beta-derivative of H
#     by complex-step differentiation of S, then
#        ln Zhat = -S(0) + (m/2) ln 2pi - (1/2) ln det H,
#        Ehat    = dS(0)/dbeta + (1/2) tr(H^{-1} dH/dbeta),
#     and the same for the primitive product rho0(x_n,x_{n+1}) exp(-tau V(x_n)).
#     Failure: |Delta E| > 1e-8 or |Delta ln Z| > 1e-8 at any of the 15 points.
# B3  analytic beta-derivative vs mpmath numerical derivative of ln Zhat (closed form).
# B4  bounds: Zhat_m <= Z_exact (Jensen), Z_m >= Z_exact.
# B5  Ehat_m from the spectrum of (c): sum_n eps_n lam_n^m / sum_n lam_n^m, eps_n = -d ln|lam_n|/dtau.
# B6  large-m asymptotics: m^2 (Ehat_m - U) -> beta^2 (U/8 + beta U'/24) - beta^3/(36 m) + O(1/m^2),
#     m^2 (E_m - U) -> -beta^2 (U/8 + beta U'/24) + O(1/m^2).
import numpy as np
import mpmath as mp

mp.mp.dps = 30
BETAS = [1, 5, 10]
MS = [1, 10, 50, 100, 500]

# ---------------- closed forms of (b), typed from the text ----------------
def Zhat(beta, m):
    beta = mp.mpf(beta); t = beta/m
    k = mp.sqrt(1 + t**2/12)
    return mp.exp(-beta*t/12)/((k + t/2)**m - (k - t/2)**m)

def Ehat(beta, m):
    beta = mp.mpf(beta); t = beta/m
    k = mp.sqrt(1 + t**2/12); kp = t/(12*k)
    a, b = k + t/2, k - t/2
    return t/6 + (a**(m - 1)*(kp + mp.mpf(1)/2) - b**(m - 1)*(kp - mp.mpf(1)/2))/(a**m - b**m)

def Zprim(beta, m):
    beta = mp.mpf(beta); t = beta/m
    k = mp.sqrt(1 + t**2/4)
    return 1/((k + t/2)**m - (k - t/2)**m)

def Eprim(beta, m):
    beta = mp.mpf(beta); t = beta/m
    k = mp.sqrt(1 + t**2/4); kp = t/(4*k)
    a, b = k + t/2, k - t/2
    return (a**(m - 1)*(kp + mp.mpf(1)/2) - b**(m - 1)*(kp - mp.mpf(1)/2))/(a**m - b**m)

def Eprim_coth(beta, m):          # equivalent form 2 in the text
    t = mp.mpf(beta)/m
    return mp.coth(m*mp.asinh(t/2))/mp.sqrt(4 + t**2)

def U(beta):
    return mp.coth(mp.mpf(beta)/2)/2

nfail = 0
# ---------------- B1: table ----------------
print("B1 closed-form table")
print(f"{'beta':>4} {'m':>4} {'Ehat_m':>16} {'E_m':>16} {'exact':>16} {'Ehat_m-exact':>14} {'E_m-exact':>14}")
table = {}
for beta in BETAS:
    for m in MS:
        eh, ep, ex = Ehat(beta, m), Eprim(beta, m), U(beta)
        table[(beta, m)] = (eh, ep)
        print(f"{beta:4d} {m:4d} {mp.nstr(eh, 12, min_fixed=-1, max_fixed=3):>16} "
              f"{mp.nstr(ep, 12, min_fixed=-1, max_fixed=3):>16} {mp.nstr(ex, 12, min_fixed=-1, max_fixed=3):>16} "
              f"{mp.nstr(eh - ex, 6):>14} {mp.nstr(ep - ex, 6):>14}")
print("    max |E_m(product form) - E_m(coth form)| over table:",
      mp.nstr(max(abs(Eprim(b, m) - Eprim_coth(b, m)) for b in BETAS for m in MS), 3))

# ---------------- B2: second route, numerically assembled m x m matrices ----------------
def bond_bridge(a, b, t):          # -ln w(a,b;t), w from eq. (a); works for complex t
    w = np.exp(-(a - b)**2/(2*t))/np.sqrt(2*np.pi*t)*np.exp(-t*(a*a + a*b + b*b)/6 - t*t/12)
    return -np.log(w)

def bond_prim(a, b, t):            # -ln[rho0(a,b;t) exp(-t V(a))]
    w = np.exp(-(a - b)**2/(2*t))/np.sqrt(2*np.pi*t)*np.exp(-t*a*a/2)
    return -np.log(w)

def action(X, beta, m, bond):      # X: (..., m) array of configurations; closed ring
    t = beta/m
    return np.sum(bond(X, np.roll(X, -1, axis=-1), t), axis=-1)

def route2(beta, m, bond):
    hcs = 1e-30                    # complex-step size
    def S_and_dS(X):
        Sc = action(X.astype(complex), beta + 1j*hcs, m, bond)
        return Sc.real, Sc.imag/hcs
    S0, dS0 = S_and_dS(np.zeros((1, m)))
    S0, dS0 = S0[0], dS0[0]
    E = np.eye(m)
    Se, dSe = S_and_dS(E)                         # S(e_i)
    H = np.zeros((m, m)); dH = np.zeros((m, m))
    for i in range(m):
        X = E + E[i]                              # rows: e_j + e_i
        X[i] = E[i]                               # row i would be 2 e_i; it is not used (diagonal
                                                  # set below) and for tau=0.002 it underflows w
                                                  # to 0 (run 1 printed a log(0) warning here)
        Sij, dSij = S_and_dS(X)
        H[i, :] = Sij - Se[i] - Se + S0
        dH[i, :] = dSij - dSe[i] - dSe + dS0
        H[i, i] = 2*(Se[i] - S0)
        dH[i, i] = 2*(dSe[i] - dS0)
    sign, logdet = np.linalg.slogdet(H)
    lnZ = -S0 + 0.5*m*np.log(2*np.pi) - 0.5*logdet
    En = dS0 + 0.5*np.trace(np.linalg.solve(H, dH))
    asym = np.max(np.abs(H - H.T))
    return lnZ, En, sign, asym

print("B2 second route (numerically assembled m x m Hessians) vs closed forms")
print(f"{'beta':>4} {'m':>4} {'dlnZhat':>10} {'dEhat':>10} {'dlnZ':>10} {'dE':>10} {'sgn':>4}")
for beta in BETAS:
    for m in MS:
        lzb, eb, sb, ab = route2(beta, m, bond_bridge)
        lzp, ep, sp_, ap = route2(beta, m, bond_prim)
        d1 = lzb - float(mp.log(Zhat(beta, m))); d2 = eb - float(table[(beta, m)][0])
        d3 = lzp - float(mp.log(Zprim(beta, m))); d4 = ep - float(table[(beta, m)][1])
        ok = max(abs(d1), abs(d2), abs(d3), abs(d4)) < 1e-8 and sb > 0 and sp_ > 0 \
            and np.all(np.isfinite([d1, d2, d3, d4]))
        nfail += (not ok)
        print(f"{beta:4d} {m:4d} {d1:10.1e} {d2:10.1e} {d3:10.1e} {d4:10.1e} {int(sb*sp_):4d} "
              f"{'ok' if ok else 'FAIL'}")

# ---------------- B3: analytic derivative vs numerical derivative ----------------
worst = mp.mpf(0)
for beta in BETAS:
    for m in MS:
        nd_h = -mp.diff(lambda bb: mp.log(Zhat(bb, m)), beta)
        nd_p = -mp.diff(lambda bb: mp.log(Zprim(bb, m)), beta)
        worst = max(worst, abs(nd_h - Ehat(beta, m)), abs(nd_p - Eprim(beta, m)))
print("B3 max |(-d/dbeta ln Z, mpmath numerical) - (analytic E)| over 30 values:", mp.nstr(worst, 3))
nfail += not (worst < mp.mpf('1e-20'))

# ---------------- B4: bounds ----------------
Zex = lambda beta: 1/(2*mp.sinh(mp.mpf(beta)/2))
v1 = [(b, m) for b in BETAS for m in MS if not (Zhat(b, m) <= Zex(b))]
v2 = [(b, m) for b in BETAS for m in MS if not (Zprim(b, m) >= Zex(b))]
print("B4 violations of Zhat_m <= Z_exact:", v1, "  violations of Z_m >= Z_exact:", v2)
print("    min Z_exact/Zhat_m =", mp.nstr(min(Zex(b)/Zhat(b, m) for b in BETAS for m in MS), 8),
      "  min Z_m/Z_exact =", mp.nstr(min(Zprim(b, m)/Zex(b) for b in BETAS for m in MS), 8))
nfail += len(v1) + len(v2)

# ---------------- B5: Ehat from the spectrum of (c) ----------------
def Ehat_from_spectrum(beta, m):
    t = mp.mpf(beta)/m
    k = mp.sqrt(1 + t**2/12); kp = t/(12*k)
    a, b = k + t/2, k - t/2
    q = b/a
    N = int(mp.ceil(45*mp.log(10)/(-m*mp.log(abs(q))))) + 10 if q != 0 else 1
    num = den = mp.mpf(0)
    for n in range(N):
        lam = mp.exp(-t**2/12)*b**n/a**(n + 1)
        eps = t/6 + (n + 1)*(kp + mp.mpf(1)/2)/a - (n*(kp - mp.mpf(1)/2)/b if n > 0 else 0)
        num += eps*lam**m; den += lam**m
    return num/den, den, N

worstE = worstZ = mp.mpf(0)
for beta in BETAS:
    for m in MS:
        e5, z5, N = Ehat_from_spectrum(beta, m)
        worstE = max(worstE, abs(e5 - Ehat(beta, m)))
        worstZ = max(worstZ, abs(z5/Zhat(beta, m) - 1))
print("B5 spectrum of (c) vs closed forms of (b): max |dE| =", mp.nstr(worstE, 3),
      " max |sum lam^m / Zhat - 1| =", mp.nstr(worstZ, 3))
nfail += not (worstE < mp.mpf('1e-25') and worstZ < mp.mpf('1e-25'))

# ---------------- B6: large-m asymptotics ----------------
print("B6 large-m: D_hat = m^2(Ehat-U) - [beta^2(U/8+beta U'/24) - beta^3/(36m)],  "
      "D_prim = m^2(E-U) + beta^2(U/8+beta U'/24); both should be O(1/m^2)")
for beta in BETAS:
    b = mp.mpf(beta)
    Ub = U(b); Up = -1/(4*mp.sinh(b/2)**2)
    c2 = b**2*(Ub/8 + b*Up/24)
    row = []
    for m in (500, 1000, 2000, 4000, 8000):
        Dh = m**2*(Ehat(b, m) - Ub) - (c2 - b**3/(36*m))
        Dp = m**2*(Eprim(b, m) - Ub) + c2
        row.append(f"m={m}: m^2*Dh={mp.nstr(m**2*Dh, 6)}, m^2*Dp={mp.nstr(m**2*Dp, 6)}")
    print(f"  beta={beta:2d} coeff beta^2(U/8+beta U'/24)={mp.nstr(c2, 10)}")
    for r in row:
        print("     ", r)
print("TOTAL FAILURES (B2-B5):", nfail)
```

Output (verbatim, round-2 re-run of the final script):

```
B1 closed-form table
beta    m           Ehat_m              E_m            exact   Ehat_m-exact      E_m-exact
   1    1    1.16666666667              1.0    1.08197670687        0.08469     -0.0819767
   1   10    1.08291953999      1.081009644    1.08197670687    0.000942833   -0.000967063
   1   50    1.08201524178    1.08193795547    1.08197670687     3.85349e-5    -3.87514e-5
   1  100    1.08198636784    1.08196701848    1.08197670687     9.66097e-6    -9.68839e-6
   1  500    1.08197709419    1.08197631933    1.08197670687     3.87321e-7    -3.87542e-7
   5    1    1.03333333333           2.0e-1 5.06783654906e-1        0.52655      -0.306784
   5   10 5.19402697672e-1  4.9199686703e-1 5.06783654906e-1       0.012619     -0.0147868
   5   50 5.07376252704e-1 5.06165570393e-1 5.06783654906e-1    0.000592598   -0.000618085
   5  100 5.06935067099e-1  5.0662891516e-1 5.06783654906e-1    0.000151412    -0.00015474
   5  500 5.06789819756e-1 5.06777462512e-1 5.06783654906e-1     6.16485e-6    -6.19239e-6
  10    1    1.76666666667           1.0e-1 5.00045401991e-1        1.26662      -0.400045
  10   10 5.43160746042e-1 4.47272727273e-1 5.00045401991e-1      0.0431153     -0.0527727
  10   50 5.02340029474e-1 4.97564527639e-1 5.00045401991e-1     0.00229463    -0.00248087
  10  100 5.00643619201e-1 4.99421703912e-1 5.00045401991e-1    0.000598217   -0.000623698
  10  500 5.00070176332e-1 5.00020409163e-1 5.00045401991e-1     2.47743e-5    -2.49928e-5
    max |E_m(product form) - E_m(coth form)| over table: 4.5e-29
B2 second route (numerically assembled m x m Hessians) vs closed forms
beta    m    dlnZhat      dEhat       dlnZ         dE  sgn
   1    1    6.9e-17    0.0e+00    0.0e+00    2.2e-16    1 ok
   1   10    1.1e-14   -5.0e-14    2.9e-14   -1.0e-14    1 ok
   1   50    9.1e-12    2.9e-11    1.6e-11    2.1e-11    1 ok
   1  100   -9.1e-11   -1.0e-10   -3.6e-11   -1.5e-11    1 ok
   1  500   -1.4e-10   -6.3e-09   -1.7e-10    8.2e-09    1 ok
   5    1   -4.4e-16   -2.2e-16   -2.2e-16   -2.8e-17    1 ok
   5   10   -6.7e-15   -1.6e-15   -1.3e-15   -1.7e-16    1 ok
   5   50   -3.6e-15    1.9e-14   -1.0e-12   -2.5e-13    1 ok
   5  100    7.5e-13    4.3e-13   -9.4e-13   -7.5e-14    1 ok
   5  500   -8.0e-11   -2.3e-10   -5.9e-10   -6.5e-11    1 ok
  10    1   -1.8e-15    2.2e-16    0.0e+00    0.0e+00    1 ok
  10   10   -8.9e-16    2.2e-16    0.0e+00    0.0e+00    1 ok
  10   50   -1.8e-13   -2.4e-14   -4.3e-14    2.4e-14    1 ok
  10  100    2.0e-14    2.9e-13   -3.7e-13    3.0e-13    1 ok
  10  500   -2.4e-12    2.4e-12   -3.5e-11    8.3e-11    1 ok
B3 max |(-d/dbeta ln Z, mpmath numerical) - (analytic E)| over 30 values: 4.52e-29
B4 violations of Zhat_m <= Z_exact: []   violations of Z_m >= Z_exact: []
    min Z_exact/Zhat_m = 1.0000002   min Z_m/Z_exact = 1.0000002
B5 spectrum of (c) vs closed forms of (b): max |dE| = 6.51e-30  max |sum lam^m / Zhat - 1| = 2.82e-29
B6 large-m: D_hat = m^2(Ehat-U) - [beta^2(U/8+beta U'/24) - beta^3/(36m)],  D_prim = m^2(E-U) + beta^2(U/8+beta U'/24); both should be O(1/m^2)
  beta= 1 coeff beta^2(U/8+beta U'/24)=0.0968856886
      m=500: m^2*Dh=0.0179682, m^2*Dp=0.0179774
      m=1000: m^2*Dh=0.0179728, m^2*Dp=0.0179774
      m=2000: m^2*Dh=0.0179751, m^2*Dp=0.0179774
      m=4000: m^2*Dh=0.0179763, m^2*Dp=0.0179774
      m=8000: m^2*Dh=0.0179768, m^2*Dp=0.0179774
  beta= 5 coeff beta^2(U/8+beta U'/24)=1.548127709
      m=500: m^2*Dh=7.27746, m^2*Dp=7.30612
      m=1000: m^2*Dh=7.29184, m^2*Dp=7.30624
      m=2000: m^2*Dh=7.29905, m^2*Dp=7.30627
      m=4000: m^2*Dh=7.30266, m^2*Dp=7.30627
      m=8000: m^2*Dh=7.30447, m^2*Dp=7.30627
  beta=10 coeff beta^2(U/8+beta U'/24)=6.248675689
      m=500: m^2*Dh=116.274, m^2*Dp=117.183
      m=1000: m^2*Dh=116.732, m^2*Dp=117.19
      m=2000: m^2*Dh=116.962, m^2*Dp=117.192
      m=4000: m^2*Dh=117.077, m^2*Dp=117.192
      m=8000: m^2*Dh=117.135, m^2*Dp=117.193
TOTAL FAILURES (B2-B5): 0

real	1m23.918s
user	0m57.163s
sys	0m0.034s
```

#### Table script: `table.py`

```python
# table.py -- prints the markdown table of part (b) from the closed forms (mpmath, 30 digits).
# Python 3.13.18, mpmath 1.3.0.  Run: python3 -I table.py
import mpmath as mp
mp.mp.dps = 30
def Ehat(beta, m):
    beta = mp.mpf(beta); t = beta/m
    k = mp.sqrt(1 + t**2/12); kp = t/(12*k); a, b = k + t/2, k - t/2
    return t/6 + (a**(m-1)*(kp + mp.mpf(1)/2) - b**(m-1)*(kp - mp.mpf(1)/2))/(a**m - b**m)
def Eprim(beta, m):
    t = mp.mpf(beta)/m
    return mp.coth(m*mp.asinh(t/2))/mp.sqrt(4 + t**2)
print("| beta | m | Ehat_m | E_m | exact | Ehat_m - exact | E_m - exact |")
print("|---:|---:|---:|---:|---:|---:|---:|")
for beta in (1, 5, 10):
    ex = mp.coth(mp.mpf(beta)/2)/2
    for m in (1, 10, 50, 100, 500):
        eh, ep = Ehat(beta, m), Eprim(beta, m)
        print(f"| {beta} | {m} | {float(eh):.10f} | {float(ep):.10f} | {float(ex):.10f} | "
              f"{float(eh-ex):+.4e} | {float(ep-ex):+.4e} |")
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
- layout problems: the pandoc build has overfull lines, e.g. eq. (6), and these are raised as SR2.1 in the Response to audit 1 (`audits/response-to-audit-1.md`), not tested;
- rendering in a markdown viewer (MathJax or KaTeX), where `\mathbf 1` is standard but was not tested;
- the `/log` conversion itself, for which pandoc is a stand-in, not the real thing.

Run log for P1 and the probe.
- `check_p1.py` run 0 used the pattern `\\mathbb\s*(?:\{\s*)?(?![A-Z][\s}\\$^_,.)])`. Because `\s*` can backtrack to zero width, the lookahead then saw a space, so `\mathbb R` and `\mathbb E` were flagged: 15 hits on answer-1, 7 of them false. I replaced the pattern with a lookahead anchored directly after `\mathbb`. That change makes the check pass for `\mathbb R` and `\mathbb E`, which the probe shows render correctly, and it leaves all 8 true hits flagged.
- Before the round-2 runs shown here, I also added `-g` and deletion of old build files. A first execution of the run-0 script had reused a cached PDF, because latexmk judged it up to date.
- `run_probe.sh` first listed only four of the seven error locations, because overlapping `grep -A2` matches dropped some. The counts were right; the listing was fixed.
- Probe line (g), `\mathbb E`, was added after those first runs, so that the probe covers every amssymb construct the answer uses. The probe was then re-run; the output shown is from that re-run.

The superseded run-0 script differs from the final one only in its first comment line and the pattern. Both are re-run below.

```latex
% probe_house.tex -- math preamble copied from the house template
% (log skill, reference/final-tex-template.tex): amsmath,amssymb,amsthm,mathtools,physics,siunitx
\documentclass[11pt,a4paper]{article}
\usepackage[T1]{fontenc}
\usepackage[utf8]{inputenc}
\usepackage{lmodern}
\usepackage{amsmath,amssymb,amsthm,mathtools}
\usepackage{physics}
\usepackage{siunitx}
\begin{document}
\Large
(a) \verb|\mathbb 1|: $2\mathbb 1 - P - P^{\mathrm T}$\par
(b) \verb|\mathbb{1}|: $\mathbb{1}$\par
(c) \verb|\mathbf 1|: $2\mathbf 1 - P - P^{\mathrm T}$\par
(d) \verb|\mathbb{I}|: $\mathbb{I}$\par
(e) \verb|\mathbb R|: $L^2(\mathbb R)$\par
(f) \verb|\square, \lesssim, \gtrsim|: $\square\ \lesssim\ \gtrsim$\par
(g) \verb|\mathbb E|: $\rho_0\,\mathbb E_{\rm bridge}$\par
\end{document}
```

`probe_auditor.tex` is the same file with the line `\usepackage{amsmath,amssymb,amsthm,mathtools}` replaced by `\usepackage{amsmath}` (and the first comment changed).

```bash
#!/bin/bash
# run_probe.sh -- compile the two probes and report errors / missing characters.
# pdfTeX 3.141592653-2.6-1.40.25 (TeX Live 2023/Debian). Run from texprobe/: bash run_probe.sh
for f in probe_house probe_auditor; do
  rm -f $f.aux $f.log $f.pdf
  pdflatex -interaction=nonstopmode $f.tex > /dev/null 2>&1
  echo "=== $f: PDF produced: $([ -f $f.pdf ] && echo yes || echo no)"
  echo "    TeX errors: $(grep -c '^!' $f.log); missing-character warnings: $(grep -c 'Missing character' $f.log)"
  grep '^l\.[0-9]' $f.log | sed 's/^/    error at /'
done
pdftoppm -r 110 -png probe_house.pdf probe_house
echo "rendered probe_house.pdf to probe_house-1.png (inspected visually)"
```

Output of `run_probe.sh` (verbatim):

```
=== probe_house: PDF produced: yes
    TeX errors: 0; missing-character warnings: 0
=== probe_auditor: PDF produced: yes
    TeX errors: 8; missing-character warnings: 0
    error at l.12 (a) \verb|\mathbb 1|: $2\mathbb
    error at l.13 (b) \verb|\mathbb{1}|: $\mathbb
    error at l.15 (d) \verb|\mathbb{I}|: $\mathbb
    error at l.16 (e) \verb|\mathbb R|: $L^2(\mathbb
    error at l.17 ...verb|\square, \lesssim, \gtrsim|: $\square
    error at l.17 ...re, \lesssim, \gtrsim|: $\square\ \lesssim
    error at l.17 ...sim, \gtrsim|: $\square\ \lesssim\ \gtrsim
    error at l.18 (g) \verb|\mathbb E|: $\rho_0\,\mathbb
rendered probe_house.pdf to probe_house-1.png (inspected visually)
```

```latex
% house-pandoc.latex -- pandoc template for check P1.
% Math/text preamble copied verbatim from the house template (log skill,
% reference/final-tex-template.tex), lines \documentclass ... hyperref; natbib and
% the tag macros omitted (not used by the markdown). Additions needed only by
% pandoc's LaTeX writer: array (table column specs), \tightlist, \passthrough.
\documentclass[11pt,a4paper]{article}
\usepackage[T1]{fontenc}
\usepackage[utf8]{inputenc}
\usepackage{lmodern}
\usepackage[margin=1in,marginparwidth=1.1in]{geometry}
\usepackage{amsmath,amssymb,amsthm,mathtools}
\usepackage{physics}
\usepackage{siunitx}
\usepackage{graphicx}
\usepackage{booktabs}
\usepackage{longtable}
\usepackage{marginnote}
\usepackage{listings}
\usepackage[hidelinks]{hyperref}
\usepackage{array}
\providecommand{\tightlist}{\setlength{\itemsep}{0pt}\setlength{\parskip}{0pt}}
\newcommand{\passthrough}[1]{#1}
\lstset{basicstyle=\ttfamily\footnotesize,breaklines=true,frame=single,showstringspaces=false}
\begin{document}
$body$
\end{document}
```

```python
# check_p1.py -- presentation check for F1.1 (round 2).
# Python 3.13.18, pandoc 3.1.3, pdfTeX 3.141592653-2.6-1.40.25 (TeX Live 2023/Debian), latexmk.
# Run: python3 -I check_p1.py answer-1.md answer-2.md
#
# P1a  static scan: every \mathbb whose argument is not a single uppercase letter A-Z, outside
#      fenced code blocks and inline code spans. amssymb's \mathbb (font msbm) has
#      double-struck glyphs only for A-Z; any other argument silently prints a different
#      symbol (probe_house.tex shows \mathbb 1 printing a negated-turnstile glyph).
#      Failure: any hit.
# P1b  convert the markdown with pandoc using texprobe/house-pandoc.latex, whose math preamble
#      is copied from the house template (amsmath, amssymb, amsthm, mathtools, physics,
#      siunitx), compile with latexmk -pdf, and report every TeX error ("!" lines) and every
#      "Missing character" warning. Failure: any error, any missing character, or no PDF.
import re, subprocess, sys, pathlib

def strip_code(text):
    text = re.sub(r'^```.*?^```', '', text, flags=re.S | re.M)   # fenced blocks
    return re.sub(r'`[^`\n]*`', '', text)                          # inline code spans

pat = re.compile(r'\\mathbb(?!\s*\{?\s*[A-Z](?![A-Za-z0-9]))')
nfail = 0
for md in sys.argv[1:]:
    src = pathlib.Path(md).read_text()
    body = strip_code(src)
    hits = []
    for ln, line in enumerate(body.splitlines(), 1):
        for m in pat.finditer(line):
            hits.append((ln, line[max(0, m.start() - 15):m.end() + 6]))
    print(f"P1a {md}: {len(hits)} \\mathbb use(s) with a non-A-Z argument (outside code)")
    for ln, ctx in hits:
        print(f"      line {ln} (code-stripped text): ...{ctx}...")
    stem = pathlib.Path(md).stem
    tex = f"p1_{stem}.tex"
    subprocess.run(["pandoc", md, "-f", "markdown", "-t", "latex", "--listings",
                    "--template", "texprobe/house-pandoc.latex", "-o", tex], check=True)
    for old in pathlib.Path('.').glob(f"p1_{stem}.*"):     # force a fresh build every run
        if old.suffix != ".tex":
            old.unlink()
    r = subprocess.run(["latexmk", "-pdf", "-g", "-interaction=nonstopmode", tex],
                       capture_output=True, text=True)
    log = pathlib.Path(f"p1_{stem}.log").read_text(errors="replace")
    errs = [l for l in log.splitlines() if l.startswith("!")]
    miss = [l for l in log.splitlines() if "Missing character" in l]
    pdf = pathlib.Path(f"p1_{stem}.pdf")
    pages = re.findall(r'Output written on .*?\((\d+) pages', log)
    print(f"P1b {md}: TeX errors = {len(errs)}, missing characters = {len(miss)}, "
          f"PDF = {'yes' if pdf.exists() else 'no'}, pages = {pages[-1] if pages else '?'}")
    for l in (errs + miss)[:10]:
        print("      ", l)
    bad = (len(errs) > 0) or (len(miss) > 0) or (not pdf.exists())
    if stem != "answer-1":          # answer-1 is the pre-fix document, run for comparison only
        nfail += bad or (len(hits) > 0)
print("TOTAL FAILURES (answer-2 only):", nfail)
```

Output of run 0, `check_p1_run0.py answer-1.md` (verbatim):

```
P1a answer-1.md: 15 \mathbb use(s) with a non-A-Z argument (outside code)
      line 43 (code-stripped text): ...erator on $L^2(\mathbb R)$ w...
      line 201 (code-stripped text): ...tau) = \rho_0\,\mathbb E_{\r...
      line 215 (code-stripped text): ...} = x^{\rm T}(2\mathbb 1 - P ...
      line 219 (code-stripped text): ...ac12x^{\rm T}(4\mathbb 1 + P ...
      line 225 (code-stripped text): ...frac1\tau\big(2\mathbb 1 - P ...
      line 225 (code-stripped text): ...frac\tau6\big(4\mathbb 1 + P ...
      line 231 (code-stripped text): ...en $x^{\rm T}(2\mathbb1 - 2P...
      line 231 (code-stripped text): ...ac12x^{\rm T}(4\mathbb1+2P)x...
      line 238 (code-stripped text): ...tau^2/12}\int_{\mathbb R^m}d...
      line 294 (code-stripped text): ... = \frac1\tau(2\mathbb1 - P ...
      line 294 (code-stripped text): ...{\rm T}) + \tau\mathbb1,\qqu...
      line 369 (code-stripped text): ...ry $f$ in $L^2(\mathbb R, e^...
      line 369 (code-stripped text): ...ection of $L^2(\mathbb R,dx)...
      line 369 (code-stripped text): ...al set in $L^2(\mathbb R)$. ...
      line 749 (code-stripped text): ... basis of $L^2(\mathbb R,\ga...
P1b answer-1.md: TeX errors = 0, missing characters = 0, PDF = yes, pages = 40
TOTAL FAILURES (answer-2 only): 0

real	0m4.988s
user	0m3.024s
sys	0m0.133s
```

Output of run 1, `check_p1.py answer-1.md answer-2.md` (verbatim; run without `time`). This is the run on the final answer-2 file. Because answer-2 contains this very output, I repeated build and P1 until P1 reproduced the embedded output byte for byte. Only the page count moved between iterations:

```
P1a answer-1.md: 8 \mathbb use(s) with a non-A-Z argument (outside code)
      line 215 (code-stripped text): ...} = x^{\rm T}(2\mathbb 1 - P...
      line 219 (code-stripped text): ...ac12x^{\rm T}(4\mathbb 1 + P...
      line 225 (code-stripped text): ...frac1\tau\big(2\mathbb 1 - P...
      line 225 (code-stripped text): ...frac\tau6\big(4\mathbb 1 + P...
      line 231 (code-stripped text): ...en $x^{\rm T}(2\mathbb1 - 2P...
      line 231 (code-stripped text): ...ac12x^{\rm T}(4\mathbb1+2P)x...
      line 294 (code-stripped text): ... = \frac1\tau(2\mathbb1 - P ...
      line 294 (code-stripped text): ...{\rm T}) + \tau\mathbb1,\qqu...
P1b answer-1.md: TeX errors = 0, missing characters = 0, PDF = yes, pages = 40
P1a answer-2.md: 0 \mathbb use(s) with a non-A-Z argument (outside code)
P1b answer-2.md: TeX errors = 0, missing characters = 0, PDF = yes, pages = 52
TOTAL FAILURES (answer-2 only): 0
```

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

Used in round 2. These are load-bearing only for the Response to audit 1 (`audits/response-to-audit-1.md`). No physics result depends on them.

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
