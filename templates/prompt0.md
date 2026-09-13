# prompt0 template — v1.3

Sections 0–5 are filled in per problem. Sections 6–8 are the invariant protocol
and are pasted verbatim every time; if you edit them, bump the template version
so that results stay comparable across problems.

Fill-ins are marked `⟨…⟩`. Delete any section that does not apply, but say that
you deleted it (for example, "3b: none") rather than removing the heading
silently — the auditor reads this document too and needs to know what you gave
the solver.

---

## 0. Run metadata

- Problem id: `⟨P007⟩`
- Title: `⟨Hawking temperature via thermofield dynamics⟩`
- Date: `⟨2026-09-12⟩`
- Solver: `⟨model id⟩`, effort `⟨low | medium | high | max⟩`, tools `⟨code, web⟩`
- Templates: prompt0 `v1.3`, conventions `v1.3`
- Course / context: `⟨optional⟩`

## 1. Problem

⟨The problem statement, verbatim and complete. If it comes from a book or a
problem set, give the source and the exact locator here, and say whether the
solution is publicly available.⟩

## 2. Conventions

⟨Units (SI, Gaussian, natural with ħ = c = k_B = 1). Metric signature. Fourier
convention. Sign of the exponent. Orientation. Any symbol whose meaning is
ambiguous. If a convention is left open, say so and require the solver to choose
one explicitly and stick to it.⟩

## 3. What I already have

**3a. Given and trusted.** ⟨Facts that may be used freely without re-derivation.⟩

**3b. My partial work, unverified.** ⟨Paste whatever of your own attempt you want
checked, or write "none". It does not have to be complete or typed up: a few
transcribed lines from a handwritten page is enough, and the rest can stay in
`human/` as a scan. Then:⟩ Treat everything in 3b as a hypothesis, not a
premise. Check it before using it. If a step of mine is wrong, say which one and
why; do not build on it and do not quietly repair it. List my hypotheses against
the ones you actually use, and name any I am relying on that you consider
unnecessary, and any you need that I did not state.

**3c. Results I expect.** ⟨Only if you actually have an expectation. Be aware
that filling this in anchors the solver — that is why section 6.1 exists.⟩

## 4. What counts as a complete answer

⟨A checklist. For example:⟩

- A closed-form expression for ⟨quantity⟩ in terms of ⟨parameters⟩.
- The full derivation, not a sketch.
- The domain of validity and the approximations used.
- ⟨A numerical value for the case …⟩
- ⟨A plot of …⟩

## 5. Method constraints

⟨How the problem should be approached, and what is off-limits. For example:
"Use the Bogoliubov transformation route, not the Euclidean periodicity
argument." Or: "Do not invoke the final form of the Hawking spectrum at any
point; it is the thing being derived." If you have no constraint, write "none —
choose a method and justify the choice."⟩

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
