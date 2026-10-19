## 0. Run metadata

- Problem id: `P003.S01`
- Title: `Failure of the primitive path integral at r = 0 for the Coulomb potential`
- Date: `⟨26-10-10⟩`
- Solver: `⟨Opus 5.5⟩`, effort `⟨extra⟩`, tools `code, web`, context `⟨project⟩`
- Attachments: `CONVENTIONS.md`; our notes, `Integrales_de_Camino_de_Feynman_261017_174852_2.pdf`
- Templates: prompt0 `v1.3`, conventions `v1.5`

## 1. Problem

Take $H = K + V$ with $K = -\frac{1}{2}\nabla^{2}$ and $V(\mathbf r) = -1/r$ in three dimensions
(hydrogen with an infinitely heavy nucleus, atomic units).

(a) Write the standard time-sliced (primitive) path integral for
$Z_N(\beta) = \operatorname{Tr}\big(e^{-\Delta\tau K} e^{-\Delta\tau V}\big)^{N}$, with $\Delta\tau = \beta/N$, as an
integral over bead positions with every prefactor.

(b) Decide whether $Z_N(\beta)$ is finite for every $N \ge 1$ and $\Delta\tau > 0$, and prove it. If
it is not, identify the region of configuration space responsible, and show whether the
kinetic factors can compensate.

(c) Compare with the continuum. Are the exact kernel $\langle \mathbf r | e^{-\tau H} | \mathbf r' \rangle$
and the exact trace $\operatorname{Tr} e^{-\beta H}$ finite? State the theorem that justifies time
slicing and say which of its hypotheses, if any, $V = -1/r$ violates.

## 2. Conventions

Atomic units, $\hbar = m_e = e^{2}/4\pi\varepsilon_0 = 1$; $\mathbf r \in \mathbb R^{3}$, $r = |\mathbf r|$. Our notes
keep $\hbar$, a mass $\mu$, $k = e^{2}/4\pi\varepsilon_0$ and $\Delta\beta = \beta/m$; state the dictionary
if you compare with them.

## 3. What I already have

**3a. Given and trusted.** The free kernel
$\langle \mathbf r | e^{-tK} | \mathbf r' \rangle = (2\pi t)^{-3/2} \exp\!\big(-|\mathbf r - \mathbf r'|^{2}/2t\big)$.

**3b. Our partial work, unverified.** Attached PDF, in Spanish: pages 4 to 9 are our
attempt, pages 1 to 3 background. The main steps, transcribed as written:

- **H1** (p. 4). $Z(\beta) = \sum_n e^{-\beta E_n} \simeq e^{-\beta E_0}$, so $E_0 \approx -\ln Z(\beta)/\beta$; the trace
  makes the paths closed, $x(\beta) = x(0)$.
- **H2** (p. 5). $e^{-\Delta\beta(K+V)} \approx e^{-\Delta\beta K} e^{-\Delta\beta V}$, justified by expanding each
  exponential to first order in Taylor series, "valid only for very small intervals".
- **H3** (p. 6). $Z_m = \Big(\dfrac{\mu}{2\pi\hbar^{2}\Delta\beta}\Big)^{m/2} \int dx_1 \cdots dx_m\, \exp\!\Big(-\sum_{j=1}^{m} \Big[\dfrac{\mu(x_{j+1}-x_j)^{2}}{2\hbar^{2}\Delta\beta} + \beta V(x_j)\Big]\Big)$, with $x_{m+1} = x_1$.
- **H4** (p. 8). The potential weight $w_{pot}(r) = e^{\Delta\tau k/(\hbar r)} \to +\infty$ as $r \to 0^{+}$: "the
  primitive weight is unbounded".
- **H5** (p. 8). $I(\varepsilon) = 4\pi \int_0^{\varepsilon} r^{2} e^{\Delta\tau/\hbar r}\, dr = +\infty$, because "$r^{2}$ does not
  compensate $e^{a/r}$".
- **H6** (p. 9). "The sum diverges; the kinetic term does not compensate the divergence
  either."

Treat everything in 3b as a hypothesis, not a premise. Check it before using it. If a step
of mine is wrong, say which one and why; do not build on it and do not quietly repair it.
List my hypotheses against the ones you actually use, and name any I am relying on that you
consider unnecessary, and any you need that I did not state.

**3c. Results I expect.** None.

## 4. What counts as a complete answer

- Explicit answers to (a), (b) and (c), with every inequality in a proof justified.
- An assessment of H1 to H6: correct; wrong, and where; or unproven, and what is missing.
- At least one computational check that could fail, for example the radial integral with an
  inner cutoff $\eta$ against the growth law you predict as $\eta \to 0$.

## 5. Method constraints

- Do not consult the GitHub repository AndresMotta77/Introduccion_Fisica_Teorica.
- Diagnosis only: do not propose ways around the singularity.

---

# 6. Protocol (invariant — do not edit per problem)

You are solving a physics problem inside a workflow whose purpose is to produce
derivations that can be trusted and audited, not answers that sound right. A
correct answer with an unauditable derivation is a failure of this workflow. An
honest partial answer is a success.

Read `CONVENTIONS.md` (provided alongside this prompt) and use its tags,
locator format, and severity vocabulary throughout.

## 6.1 Prior-knowledge declaration

Before you derive anything, write a section titled **Prior-knowledge
declaration** and answer these, plainly:

1. Do you recognize this problem? From where?
2. What result do you believe is the standard one? Write it out.
3. What is the standard route to it, and where is that route presented in the
   literature?
4. What in section 3c of this prompt, or in your own recall, are you now
   anchored on?

State this up front and then derive independently of it. The point is not to
pretend you do not know the answer; it is to make what you know visible so that
an auditor can tell the difference between a derivation and a reconstruction.

At the end of your answer, write a section titled **Convergence check**:

- Does your derivation reproduce the declared result? If not, report both and
  say which you believe and why. Do not silently reconcile them.
- Name every step where a person who did not already know the target could not
  have chosen as you did: an ansatz that appears without motivation, a factor
  inserted for later convenience, a substitution that happens to be exactly the
  right one, a limit taken in exactly the order that works. List them even if
  you believe each is justified. If there are none, say what makes the
  derivation forced at each branch point.
- Would the derivation still run if the standard result were slightly different
  — a different power, a different numerical factor? If yes, at what point would
  it break, and would you have noticed?

## 6.2 Derivation rules

- Write out intermediate algebraic steps even when they are easy. Do not write
  "it follows that", "it can be shown", "after some algebra", or "clearly". If a
  step takes six lines, write six lines.
- Tag every non-trivial step per `CONVENTIONS.md` §1.
- State every assumption as `[A]` at the moment you make it, with what it buys
  you and what breaks without it.
- If you get stuck, stop and say where. Report the obstruction and what you
  would need in order to pass it. Do not produce a plausible bridge.

## 6.3 Sources and bibliography

- Maintain a **Sources** section, split into *Used* and *Consulted* per
  `CONVENTIONS.md` §3.
- Every entry carries a locator at section, equation or page granularity, and a
  verification status `{ver: tool | human | no}`.
- If I have given you a general reference in section 1 or 3 ("see Carroll"),
  that is not a citation. Resolve it to the specific chapter, section and
  equation you actually used, and say which edition.
- You have web access. For each *Used* source, attempt to retrieve it and
  confirm that the locator says what you claim. Mark the ones you confirmed as
  `{ver: tool}` and give the retrieval note (what you fetched, what it said).
  Mark the rest `{ver: no}`. Do not guess an equation number to make a citation
  look complete.
- If a result is standard but you cannot produce a locator, tag it `[R]`, use
  it, and enter it in the Risk register. That is an acceptable outcome. A
  fabricated locator is not.

## 6.4 Computational checks

You have code execution. Use it, but understand what it is worth. A
computational check is evidence, not proof, and it is not an oracle: you wrote
the code, so it can encode the same misunderstanding as the derivation. A model
that misremembers a result will cheerfully write a check that confirms the
misremembering, and the check will print PASS. Code has one real advantage over
prose — it fails loudly, deterministically, and in a form another party can read
line by line — and that advantage exists only if you write it so that it *can*
fail and so that someone else can see what it actually tested.

Your verification code is an artifact under audit, exactly like the derivation.
It will be read by the auditor with the same suspicion.

**What to check.**

- Key algebraic identities, symbolically.
- Both sides of every non-obvious equality, at random numerical values drawn
  from the region where the claim is supposed to hold, and also at values near
  its stated boundary.
- Where the problem admits a second route — quadrature, ODE integration, direct
  summation, a lattice or Monte Carlo estimate — compute it that way and compare
  against the closed form.

**How to write a check that means something.**

- **Start from the problem statement, not from your answer.** The strongest
  check recomputes the target quantity from the original definition, the
  original integral, the original equation of motion, and compares it to your
  closed form. A check built out of intermediate results from your own
  derivation tests your algebra at best, and is circular at worst.
- **No circular checks.** Do not verify a result using a routine that already
  contains it. If your numerical evaluator calls the very expression it is
  supposed to be testing, the check is empty. Say explicitly, for each check,
  what it would have caught.
- **No vacuous checks.** `simplify(lhs - rhs) == 0` where both sides came out of
  the same symbolic manipulation tests sympy, not physics. A check that cannot
  distinguish a right answer from a wrong one is worse than no check, because it
  appears in the log as a pass.
- **Do not launder assumptions.** `assume(x > 0)`, `simplify` with positivity or
  reality assumed, a principal-value convention, a branch choice, a chosen FFT
  sign — every one of these is an `[A]` and must be stated in the text as well
  as in the code. A check that only passes under an assumption the derivation
  never declared is a finding, not a verification.
- **Make it able to fail.** State the tolerance and why. Guard against a
  degenerate test set where both sides vanish, against NaN comparisons that
  silently pass, and against tolerances loose enough to absorb the error you are
  hunting. Before running it, note what output would count as a failure.
- **Report all runs.** If you ran ten parameter sets and eight agreed, report
  ten. Do not present the agreeing subset.
- **Make it reproducible.** Fixed seed, pinned library versions in a comment,
  standalone: a script that runs from a clean interpreter with no state carried
  over from earlier cells.

**What to report.**

- The code verbatim, and its output verbatim. Do not paraphrase what it printed.
- For each check: what it tests, what it would have caught, and what it would
  not have caught. That last clause is required and is not optional padding —
  it is the part that keeps a passing check from being read as a proof.
- If a check fails, report the failure. Do not adjust the derivation until the
  check passes and then present only the passing version. If you revised after a
  failed check, say what failed, what you changed, and whether you changed the
  derivation or the check. Changing the check to make it pass is the single most
  damaging thing you can do in this workflow, and if you do it you must say so.
- Tag each check `[N]` per `CONVENTIONS.md`.

## 6.5 Self-check battery

Before you finish, run each of these and report the result, including the ones
that are trivially satisfied:

1. Dimensions and units on every displayed result.
2. Limiting cases: each parameter to zero and to infinity.
3. Reduction to a known simpler case.
4. Symmetries of the problem, and whether the answer respects them.
5. Signs and orientation.
6. Order of magnitude for a physically realistic parameter set.
7. Boundary and initial conditions actually satisfied by the solution.
8. Degenerate and special cases where the derivation might divide by zero,
   exchange a limit and an integral, or assume a nonvanishing quantity.

## 6.6 Honesty rules

- Give a confidence level per major section: high, medium, low. Say what would
  move it.
- Maintain a **Risk register**: every `[R]`, every `[?]`, every `[A]` that is
  load-bearing, and every `{ver: no}` citation that the result depends on. One
  line each: what it is, what happens if it is wrong.
- If your answer disagrees with something I asserted in section 3, say so
  directly. I would rather be corrected than agreed with.
- If the problem as stated is ill-posed, underdetermined, or inconsistent, say
  that instead of solving a nearby problem. If you solve a nearby problem
  anyway, say which one and why.

---

# 7. Output format

Produce one markdown document with these sections, in this order:

1. `Prior-knowledge declaration`
2. `Setup` — conventions, symbol table, the problem restated precisely
3. `Derivation` — numbered equations, tagged steps
4. `Verification` — the self-check battery, the code with its verbatim output,
   and for each check what it would and would not have caught
5. `Result` — the final statement, with its domain of validity
6. `Convergence check`
7. `Risk register`
8. `Sources` — Used / Consulted
9. `Open questions` — what you would want checked, and by what method

Prose, not slideware. No `\emph`. No decorative bolding. Write the way a
careful physicist writes a set of notes for a colleague.

# 8. What I will do with this

Your answer goes to a second model with an adversarial audit prompt. It will
recompute your load-bearing steps, check your citations against their sources,
read your verification code looking for checks that are circular, vacuous, or
quietly assuming what they should be testing, and look specifically for steps
that only make sense if you already knew the answer. You will then see its
findings and get a chance to rebut them. Write for that reader.
