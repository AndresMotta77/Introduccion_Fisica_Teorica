# Independence record — P003.S03

Read this first when revisiting the problem. It holds what the solver (Claude Opus 5.5) declared it knew before deriving, the convergence check it wrote afterwards, what is known about a perturbation test, and an access record.

## Prior-knowledge declaration

Verbatim §1 of `answers/answer-2.md`. It is unchanged from answer-1, and was written when answer-1 was assembled, after the derivation had been done in scratch form, as its first paragraph says.

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

## Convergence check

Verbatim §6 of `answers/answer-2.md`, unchanged from answer-1. It also remains in `final/final.md`.

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

## Perturbation test

No result is on record. According to the comments in `meta.yaml`, the decisive test and its perturbation variant were to reach the auditor in the [FOCUS] block of `prompts/audit-prompt-1.md`, and the solver never sees that block. `audits/audit-report-1.md` does not mention a [FOCUS] block, a decisive test or a perturbation variant. The logger is the solver, so it did not open `audit-prompt-1.md`, and it cannot say whether the block was sent. Recorded as `perturbation_test_run: unknown`.

## Access record

- Forbidden sources (prompt0 §5). The solver's web activity is listed in answer-2 §8. It consisted of DLMF pages, the MaRDI mirror of one DLMF formula, a search-result snippet of arXiv:2112.11166, and search queries on Hermite, Mehler and completeness keywords. None of the forbidden sources was retrieved.
- The local problem folder sits in a repository whose name, `Introduccion_Fisica_Teorica`, matches the forbidden GitHub repository. The solver first touched it at /log time, 2026-11-13, after answer-2 was final. Access was granted for this subproblem folder only, and nothing above it was listed or read.
- Read at /log time: `meta.yaml`, `README.md`, `human/attempt.md` (an unfilled template), `prompts/prompt0.md` (compared with the prompt received; identical apart from line endings) and `answers/answer-1.md` (compared with the delivered file; identical).
- `meta.yaml` comments name the paper chunk (K5), `../PLAN.md`, `../paper/kole-deraedt-2001/chunks.md`, and the PI checks pc1, pc1b, pc2 and pc3. The solver saw these names but no content, and opened none of those files.
- `prompts/audit-prompt-1.md` was copied into the container by the staging call that read the other files, and was never opened.
