# Independence record — P003.S02

Read this file first when revisiting the problem. It holds three things, each in its own section below: the solver's prior-knowledge declaration, the solver's convergence check, and the status of the perturbation test.

## Prior-knowledge declaration (verbatim from answers/answer-2.md §1; byte-identical to answers/answer-1.md §1)

The declaration was written in round 1, before any derivation, and was carried unchanged into round 2.


1. Do I recognize the problem? In outline, yes. Bounding a Feynman–Kac expectation from below by Jensen's inequality, $\langle e^{-S}\rangle \ge e^{-\langle S\rangle}$, with a Gaussian reference measure is Feynman's variational idea (Feynman & Hibbs, *Quantum Mechanics and Path Integrals*, ch. 11; Feynman, *Statistical Mechanics*, ch. 3; both from memory, locators not verified). As far as I recall, applying it slice by slice with the free Brownian bridge as the reference measure is the construction of the Kole–De Raedt paper excluded in §5 of the prompt. I have not consulted that paper (or the excluded repository) in this session, and I do not remember its specific claims: neither the convergence order it states nor the details of its Coulomb treatment. I know the Gaussian-smeared Coulomb potential $\operatorname{erf}(r/\sqrt2\sigma)/r$ from Ewald sums and Gaussian-basis electronic structure.

2. The result I believed to be standard before deriving anything: inequality $(\ast)$ with $\langle V\rangle_u(\mathbf x,\mathbf x') = \int d^dy\,\rho_0(\mathbf x,\mathbf y;u)V(\mathbf y)\rho_0(\mathbf y,\mathbf x';\tau-u)/\rho_0(\mathbf x,\mathbf x';\tau)$. Equivalently, a Gaussian average of $V$ whose mean lies on the straight line from $\mathbf x$ to $\mathbf x'$ and whose variance is $2Du(\tau-u)/\tau$ per coordinate. Then $\hat Z_m\le \operatorname{Tr}e^{-\beta H}$ by multiplying slice bounds, and the trapezium rule gives the symmetric (primitive) Trotter kernel. On the error, I expected a local defect of order $\tau^3$ and a global error of order $1/m^2$, by analogy with the symmetric Trotter splitting; I had no coefficient in mind. For Coulomb, I expected the smeared potential to be bounded at the origin, so that the averaged action stays finite where the primitive factor $e^{\tau q^2/2r}$ is not integrable. I also expected the smooth-potential error estimate to fail there.

3. The standard route: the Trotter product formula plus Jensen applied to the bead measure, or the Feynman–Kac bridge representation plus Jensen plus Fubini. The bridge form of Feynman–Kac is Simon, *Functional Integration and Quantum Physics*, Thm 6.6. I know that locator only through Simon, arXiv:math-ph/9907022, which I retrieved and which cites it; the book itself was not retrieved.

4. What I am anchored on. Section 3c of the prompt is empty, so nothing comes from the prompt. My own anchors are the expectations listed in item 2, and the most consequential is the $1/m^2$ expectation. Only after deriving the leading local defect $D\tau^3|\nabla V|^2/12$ (§3.5.4) did I notice that it coincides with the Takahashi–Imada correction term. That comparison was made after the computation; it is reported in the Convergence check and was not used in the derivation.


## Convergence check (verbatim from answers/answer-2.md §6; also kept in final/final.md)


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


## Perturbation test

Not run. In `prompts/audit-prompt-01.md` the `[FOCUS]` block was left as the template placeholder. The decisive test and perturbation variant, which `meta.yaml` planned to give the auditor once answer-1 existed, therefore never reached the auditor. The same happened in S01 (meta.yaml comment).

## Auditor's independence pass

`audits/audit-report-1.md`, Pass 8 (independence audit): "pass". The auditor reported no anchoring steps and raised no finding about independence. The auditor ran with no code execution and no web access (run header).

## Context of the runs (recorded by /log)

Solver context: clean, meaning no claude.ai project. Account memory was enabled; it held profile and formatting preferences and nothing about this problem. The solver had web access. Its searches were chosen to avoid the sources excluded in prompt0 §5, and none of them appeared in any search result list (answer-1 §8).

The repository that holds this folder has the same name as the GitHub repository excluded in prompt0 §5 (`Introduccion_Fisica_Teorica`). The solver had no access to it during either round. During /log, after both answers were final, access was granted to this folder only, and nothing above it was read. Reading this folder's `meta.yaml` exposed the logging session to the planning comments, which name Kole and De Raedt's eqs. (14)–(16) and an upper bound (15). Neither answer was affected, but this conversation is no longer a clean context for any further answer on this problem.
