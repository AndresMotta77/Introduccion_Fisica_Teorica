<!-- Extracted verbatim by /log from answers/answer-2.md (the section "Response to audit 1"). This is the solver's response to audit-report-1, not an auditor's document. -->

## Response to audit 1

| id | Disposition | What changed | Where |
|---|---|---|---|
| F1.1 (QUESTION: notation $\nabla V\cdot\nabla^3V[\Delta,\Delta,\cdot\,]$ ambiguous without indices) | accepted | The intended contraction is exactly the auditor's $\sum_{i,j,k}\partial_iV\,\partial_i\partial_j\partial_kV\,\Delta_j\Delta_k$. §3.5.4 now uses component notation with summation over repeated indices throughout: the decomposition $A_1,\dots,C_3$, the Isserlis moments written in components, every covariance, and (27)–(28). A dictionary maps each vector expression of answer-1 to its index form; it also makes explicit that $\operatorname{tr}\mathsf H^2=V_{ij}V_{ij}$ (not $(\nabla^2V)^2$) and that $\nabla V\cdot\nabla(\nabla^2V)=V_iV_{ijj}$. The symmetrization shorthand $3\delta_{a(b}\delta_{cd)}$ is replaced by the explicit three-term sum. Beyond notation, I added a check that makes the contractions testable rather than only legible: S9 computes $\operatorname{Var}S$ exactly in $d=2$ for cubic-plus-quartic potentials with random rational coefficients and matches every term of (27) through $O(\tau^4)$. It also rejects two wrong readings: $(V_i\Delta_i)(V_{jkk}\Delta_j)$ in place of $V_iV_{ijk}\Delta_j\Delta_k$, and $(\operatorname{tr}\mathsf H)^2$ in place of $\operatorname{tr}\mathsf H^2$. No coefficient, sign or power changed. | §2.2 (two new rows); §3.5.4; §4.1 items 1, 3, 4; §4.2; §4.3 (S9); §4.4 (R8–R11); §4.5.5; §5; §6; §7 items 23–25; §9 items 8–9 |

Remarks on audit 1. These are not rebuttals of F1.1; they are points the next reader of this loop should have.

1. Verdict versus CONVENTIONS §5. ACCEPT is defined as "no BLOCKER, no MAJOR, no open QUESTION", so with F1.1 open the conventions did not permit ACCEPT. None of the other verdicts fits either: ACCEPT-WITH-FIXES covers only MINOR and NIT, and REVISE needs a MAJOR. I read this as a gap in the conventions, which define no verdict for "open QUESTION only", rather than as an error of the auditor. If the next audit closes F1.1, ACCEPT applies cleanly.

2. What audit 1 did not cover. Its metadata reports no code execution and no web access, and its Pass 6 (code audit) is marked not performed. The verification code and the `{ver: no}` locators (Reed–Simon I Thms S.21, VI.23, VIII.20(b), VIII.25(a); Reed–Simon II Thms IX.28, X.15, X.28; Rudin Thms 1.26, 1.34, 3.3) have therefore been examined only by me. The ACCEPT should be read with that scope. I have added this to the Risk register (item 25) and to Open questions (item 9).

3. Frozen sections carry open `[?]` flags. Three of them, all now frozen and reproduced unchanged, contain flagged items: §3.2 (the remark on removing [A3] within the product-formula route); §3.3 (the pointwise form of (18) without [A3]); and §3.6 ((48) needs exponential moments of $X$, and (49) is a heuristic). Freezing a section does not discharge its flags, so they remain in the Risk register as items 9, 10, 14 and 15.

4. Audit 1 reports recomputing $\iint C\,du\,dv$ and the circulant eigenvalues. Both agree with S4 ($I_1=D\tau^3/6$) and with (37) in this document.

