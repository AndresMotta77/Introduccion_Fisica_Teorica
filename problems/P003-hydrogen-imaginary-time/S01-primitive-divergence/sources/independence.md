# Independence record — P003.S01

This is the file to read first when revisiting this subproblem. It is the solver's account of what it knew going in, and of where the derivation could have leaned on that knowledge.

`/log` assembled it from `answers/answer-2.md`. Sections 1 (Prior-knowledge declaration) and 6 (Convergence check) are reproduced verbatim; the notes at the end are by `/log`. Both sections are identical in answer-1 and answer-2, because they were on the round-1 frozen list.

- Solver: Claude Opus 5.5 (`claude-opus-5-5`, self-reported, configured model id); effort "extra" (user-reported, from `prompts/prompt0.md` §0).
- Auditor: "Gemini", effort high, both self-reported in the report's run header; no code execution, no web.

---

## 1. Prior-knowledge declaration

1. Do I recognize the problem? Yes. The failure of the primitive (Trotter) approximation for an attractive Coulomb potential is a known obstruction in path-integral Monte Carlo. I recall it from three sources, none retrieved in this session, all with unconfirmed locators: Ceperley's review of path-integral methods (Rev. Mod. Phys. 67, 279 (1995)); the discussion of the Coulomb path integral and "path collapse" in Kleinert's book on path integrals; and Kole and De Raedt, Phys. Rev. E 64, 016704 (2001). The project instructions required me to read the project document `claude/start-here.md` at the start of the session. It told me that this subproblem belongs to a larger problem on the hydrogen ground state from imaginary-time path integrals, that it corresponds to the first chunk of the Kole–De Raedt paper, and that the project has chosen the Kole–De Raedt effective action as its method. A memory note on the user's workflow says the same. I did not read the project's plan, its claim map or any repository file.

2. What do I believe the standard result is?
   - (i) Written as a bead integral, the primitive trace is $+\infty$ for every $N$ and every $\Delta\tau>0$. The potential weight $e^{\Delta\tau/r}$ is not integrable at $r=0$ in three dimensions, and the Gaussian kinetic factors are bounded below near the singular configurations, so they cannot compensate.
   - (ii) The exact kernel $\langle\mathbf r|e^{-\tau H}|\mathbf r'\rangle$ is finite and continuous, including at the origin, because $-1/r$ is in the Kato class (Simon's 1982 review).
   - (iii) For hydrogen in infinite space, the exact trace $\operatorname{Tr}e^{-\beta H}$ is also infinite, for an unrelated reason: infinitely many bound states accumulate at zero energy, and there is a continuum.
   - (iv) The imaginary-time Trotter product formula requires both summands to be bounded below, and $-1/r$ is not.

3. What is the standard route, and where is it presented? Prove a lower bound on the bead integral restricted to a neighbourhood of the singular configuration. Simon 1982 covers kernels, and Reed and Simon volume I, §VIII.8, covers the Trotter formula.

4. What am I anchored on? Section 3c gives no expected result. I am anchored on item 2 and on the notes' own conclusions (H4 to H6 assert the divergence). Before deriving anything, I wrote down the checks I intended to run: a radial growth law, bead integrals with a cutoff, a collapse configuration, the exact kernel at the origin, and a bound for the Kato condition. So the shape of the verification was chosen with the expected answer in mind. Item 2(iii) is what made me look for a large-$r$ divergence of $Z_N$, which the problem statement does not mention.

## 6. Convergence check

Does the derivation reproduce the declared result? Yes, items 2(i) to 2(iv) of the prior-knowledge declaration are all reproduced, and nothing in the derivation contradicts them. Several results go beyond what I declared:

- the sharp statement (B16) that the kinetic factors do not change the leading growth;
- Remark B.6, that $T^N$ is defined only on the zero vector;
- the observation that the real-time product formula does hold;
- the explicit value of $K_\tau(\mathbf 0,\mathbf 0)$.

Steps where someone who did not already know the target might not have chosen as I did:

1. Separating the divergence at the origin from the divergence at infinity. This was prompted by my recollection that the exact hydrogen trace diverges (declared). Someone without that recollection would still reach (B13) from $w\ge1$, but might not look for it.
2. The region $D_\varepsilon$, with the other beads in $B_1$. It is motivated by the need for a lower bound on the Gaussians. The radius 1 is arbitrary; any bounded set works.
3. The power 3 in (B1). This is forced by the measure $r^2dr$, as stated in the text.
4. The substitution $u=a/r$ and the repeated integration by parts. This is the standard treatment of a Laplace-type integral. I carried three terms so that the check could test beyond leading order.
5. The thin-shell lower bound (B15) and the parameter $\theta$. This was chosen after (B6) showed that the integral concentrates at the cutoff.
6. The prediction (B18) and its first correction. Both were derived from the shell structure and stated in the script before it was run (observed 1.027, predicted about 1.025).
7. The translated test states in (C7). I chose these because I knew the divergence is a volume effect. Someone without that knowledge would more likely use the bound-state sum, which needs recalled spectral data.
8. The statement of the Trotter theorem. I recalled it and then checked it against secondary sources. Once the statement is fixed, identifying the failing hypothesis is mechanical.
9. The explicit value at the origin, (C5). This needs recalled Coulomb data. Route (ii) of C4 does not.
10. The real-analyticity argument in B.6. I chose this technique knowing that it would close.

Would the derivation still run if the result were slightly different?

- A different power of $r$. For $V=-1/r^\alpha$ with any $\alpha>0$, the same proof runs with $e^x\ge x^n/n!$ and $n\alpha>3$, so $Z_N=\infty$ for every $\alpha>0$. In contrast, the exact kernel is finite only for $\alpha<2$ (the Kato condition), and for $\alpha=2$ with strong coupling the continuum fails as well. The derivation tracks this change at the step where $n$ is chosen, and I would have noticed.
- A different dimension. In dimension $d$ the condition is $n>d/\alpha$. In one dimension, the notes' setting, $\int dx\,e^{a/|x|}$ also diverges.
- A different growth law. Had the law been $\eta^3e^{a/\eta}$, check C1 would have failed (see its contrast column).
- A different sign of the potential. For a repulsive potential, the proof of (B9) breaks at $w\ge1$, which is visible.
- A different prefactor. A wrong prefactor in (a), for example the one-dimensional power $m/2$, would not be detected by anything in (b) or in the checks, since all the checks are independent of the prefactor. That is a blind spot. The prefactor rests only on the given kernel and the counting in (A2) and (A3).

---

## Notes by /log

Context. The solver ran in a Claude session attached to the user's Vibe Physics project. Before starting, the project instructions required it to read `claude/start-here.md`, which names the subproblem's place in P003, the Kole–De Raedt paper, and the method chosen for P003. The solver declares this in §1 above. It did not open `PLAN.md`, `paper/`, or any file of this repository during the loop. prompt0 §5 forbade the repository, and the repository was first opened at `/log` time, after the user closed the loop.

Ordering. Web retrieval for the Trotter, Kato-class and Coulomb-data citations happened before the derivation was written. The declaration in §1 is the solver's own account of its prior. No published solution of this subproblem was retrieved.

Anchoring steps. The solver self-reported ten (§6, list 1–10). The auditor reported pass 8 as "PASS. No circularity detected" and listed none of its own. That is not independent corroboration:

- the auditor read the declaration before forming a view;
- stage 0 (blind solve) was not run;
- the auditor executed no code.

Perturbation test. No perturbation test was run by anyone. The solver's §6 describes how the derivation would respond to $V=-1/r^\alpha$, to dimension $d$, to the sign of $V$, and to a different growth law, but that is analysis rather than a run. `meta.yaml` notes that the decisive test and the perturbation variant for K1 were to be sent to the auditor in `[FOCUS]` after answer-1 existed. The `[FOCUS]` block of `prompts/audit-prompt-1.md` was left empty, so they were not sent.
