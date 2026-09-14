# Corrector prompt 1 — P002

Recorded verbatim as received (Part B of the auditor's reply). Part A is in
`audits/audit-report-1.md`. The answer produced from this prompt is
`answers/answer-2.md`.

---

Part B — Corrector prompt
Round 1. Verdict: ACCEPT-WITH-FIXES. Produce a full rewritten answer rather than a patch.

Findings:

* `id`: `F1.1`

* `severity`: MINOR

* `location`: Section 3.3, Size-counting table

* `claim`: The table claims that $\omega_0^2\sin\Theta$ is $\ll \varepsilon^2\omega^2$ near threshold. This is false.

* `evidence`: At the stability threshold, the boundary is $A^2\omega^2 = 2gl$, which is exactly $\varepsilon^2\omega^2 = 2\omega_0^2$. Therefore, $\omega_0^2$ and $\varepsilon^2\omega^2$ are of the exact same order near threshold.

* `test`: A correct table must establish the actual relative size of $\omega_0^2$ to $\varepsilon^2\omega^2$ near threshold to accurately justify its inclusion in the slow $O(\varepsilon^2\omega^2)$ equation block.

* `fix_supplied`: Yes.

* `id`: `F1.2`

* `severity`: MINOR

* `location`: Section 4.3 and Section 4.4

* `claim`: Standard mathematical and physical results are invoked without the required provenance tags.

* `evidence`: In §4.3, the text states "from (46) and the standard amplitude-frequency relation for a quartic well" without an `[R]` tag (despite it being accurately logged as `R2` in the Risk register). In §4.4, Floquet theory, the monodromy matrix construction, and its $\det M = 1$ property are invoked without any tags.

* `test`: Every standard result or theorem recalled from training must carry an `[R]` or `[S]` tag in the text, per `CONVENTIONS.md` §1.

* `fix_supplied`: No.

Frozen sections:

* `3.1 Coordinates and the Lagrangian`

* `3.2 Equation of motion`

* `3.4 The fast equation`

* `3.5 Averaging, and the effective potential`

* `3.6 Equilibria, stability, and the slow frequency`

* `3.7 Is the timescale separation self-consistent?`

* `3.8 Behaviour exactly at threshold`

Do not rewrite these. If you believe one is wrong, raise it as a rebuttal rather than editing it.

If you believe a finding is mistaken, do not comply with it. Under that finding's id, write a rebuttal with an argument or a computation. A point you concede and a point you contest must be visibly different in your reply. Agreeing with a wrong finding costs more than disagreeing with a right one, because the next round will not catch it.

Return the full answer again in the same section structure, plus a section `Response to audit 1` containing one row per finding id: accepted / rejected / partial, what changed, and where. Update the Risk register and the Sources section to reflect the changes. Re-run the verification code and paste the new output; do not carry the old output forward.

The protocol in prompt0 §6 and the output format in §7 still apply in full.
