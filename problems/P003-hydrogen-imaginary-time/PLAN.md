# P003 — Guide 15, Project 04: the hydrogen ground state from imaginary time. Plan of work

Draft for discussion, 2026-10-18. Written by Claude in the role of principal investigator,
at the user's request. Configured model id `claude-opus-5-5`; the serving model and the
effort level cannot be observed from inside the session: `unknown`.

Read for this plan, from the clone: `templates/CONVENTIONS.md` v1.5, `prompt0.md` v1.3,
`audit-prompt.md` v1.4, `blind-solve-prompt.md` v1.0, `exploration-prompt.md` v1.0,
`human-attempt.md` v1.1, `skills/log/SKILL.md` and its reference files, `CHANGELOG.md`,
`index.yaml`, and the Project 04 proposal (its README; in `tex/proposal.tex`, Proposition 1
at the start of Section 4, the end of Section 9, and Sections 10–14; check 7 with its output
and coverage note). From the user: *Guía 15: proyectos integrales de camino* (.docx) and
Kole and De Raedt, arXiv:physics/0102015v1 (PDF), read from the text and, for the
equations, from page images.

This plan, the folder `paper/`, and the proposal in
`proposals/guide15-P04-hydrogen-imaginary-time/` are prior knowledge. None of them is
attached to a solver prompt. A subproblem whose solver, or whose human attempt, saw any of
them says so in its `sources/independence.md`.

## 1. What this plan covers

Project 04 of the guide asks whether the ground-state energy of V(r) = −1/r can be extracted
from a path-integral representation without confusing an executable calculation with a
valid probability measure. The guide's minimal goal is the ground state with a correct
treatment of the Coulomb singularity; excited states and the Duru–Kleinert mapping are
extensions. The end point is E_1s with an error budget, an explanation of the mathematical
origin of the singularity, and a radial density compared with an independent solver using
the measure 4πr² dr. The specific deliverables are a proof that the primitive weight
diverges, the code of the chosen method, a table of biases, and a checked radial density.

The plan keeps the guide's four phases and the evidence it asks for at each one, since the
course assesses the project against them. What it changes is the level of detail. Each step
of the guide is rewritten as tasks with a stated pass criterion (Section 3), and each task
that involves a model is assigned to a subproblem that runs through the repository's loop:
prompt0, answer, audit, corrector, `/log` (Section 5). Section 4 gives a procedure for
turning a paper into such subproblems and applies it to Kole and De Raedt, the project's
central reading.

In the repository this is P003, a container for subproblems S01, S02, …, each of which is a
problem in the old sense with the usual layout. Section 7 lists what the templates and
scripts need for that. None of it has been applied yet.

## 2. Decisions needed before work starts

| | decision | PI recommendation | if decided otherwise |
|---|---|---|---|
| D1 | the current course week; team size and members | (needed from you) | the calendar of Section 8 is in course weeks and assumes three people at about four hours a week each |
| D2 | the method | the Kole–De Raedt effective action, in ground-state projection (open path, trial-function ends); guided diffusion Monte Carlo as the fallback | Section 5.2 |
| D3 | repository layout | container `problems/P003-hydrogen-imaginary-time/` with subfolders `S01-…`; P003 is the next free id | a different id or layout is a `git mv` |
| D4 | solver and auditor | Claude solver and Gemini auditor, as in P002; closed-book solver runs in a fresh context outside the Vibe Physics project | declare the context in `independence.md` |
| D5 | precision target | at least 1e-3 hartree with a complete error budget; 1e-4 as the target | statistics in phase 3 scale with it |

On D2. The guide asks the team to fix one method in the protocol, guided diffusion Monte
Carlo or a Coulomb effective action, and does not require both. I recommend the effective
action of Kole and De Raedt used in ground-state projection, for four reasons. It is the
central reading, so reading the paper (Section 4) and building the method are the same
work. Its slice weight is finite by construction, and that turns the guide's demand for a
written normalisability statement into a real proof: the paper's own hydrogen approximant,
eq. (27), is not normalisable on R³ (`paper/kole-deraedt-2001/errata.md`, E14), and showing
that the projected version is takes an argument. The rate at which its energy converges in
Δτ for hydrogen is not given in the paper, so the phase-3 sweep answers a question that has
no published answer to recite (RQ3 of the proposal). And projection gives pure estimators of
⟨r⟩ and P(r) at the middle bead, which avoids the mixed-estimator problem the guide warns
about for diffusion Monte Carlo.

The costs are real. Each slice needs a one-dimensional quadrature of the effective
potential, which must be tabulated with a measured interpolation error, and a small Δτ means
many beads, which needs the staging moves of the paper's appendix. The fallback condition,
to be written into the protocol: if at the phase-2 gate the code fails the positive
control, or the cost per independent sample puts 1e-3 hartree out of reach in the computing
time available, switch to guided diffusion Monte Carlo, whose pilot already exists
(proposal, check 4). S01, S07 and most of the estimator work carry over.

## 3. The guide's phases, step by step

For each phase: what the guide asks (translated), what it leaves unspecified, the steps as
we will run them, and the evidence at the gate. Subproblem ids refer to Section 5.

### Phase 1 (weeks 1–4): formulation, sources, proofs, protocol

The guide asks: "derive the Euclidean representation and prove why the primitive weight
fails; ask the AI to review the proof, check it analytically, and fix the energy
estimator." The common table adds a short protocol with units, boundary conditions, an
analytic proof and a computing plan, and says the scope is accepted or reduced in this
phase.

What it leaves unspecified. "The Euclidean representation" names no object, and for
hydrogen there are two candidates that fail in different ways. The trace Z(β) = Tr e^{−βH}
is infinite with no discretisation at all, because of the Rydberg series and the continuum.
The projection with trial-function ends is finite in the continuum and becomes infinite only
in the primitive discretisation. A proof that does not separate the two can be correct line
by line and still explain nothing. "Prove why the primitive weight fails" can be read as the
divergence of one radial integral, while the guide's end point also asks for the
mathematical origin of the singularity: why the product formula behind the discretisation
does not apply to −1/r. "Ask the AI to review the proof" puts the model after the team, which
is the right order, but gives it nothing to review against; in the loop an audit needs
prompt0, the conventions and a decisive test. "Fix the energy estimator" does not say
which, and with the effective action the choice matters (chunk K10). The independent solver
appears only in phase 4, although its reference values are needed for the first control
run.

Steps:

1.1 Fix the objects and the units. Atomic units with an infinitely heavy nucleus, so that
the reference energy is exactly −1/2 hartree; Kole and De Raedt use the reduced mass, which
rescales the energy unit by μ/m_e. Write the trace Z_N(β) and the projection A_N(τ) with
trial-function ends, and state which one the project samples and why. [S01, S05]

1.2 Prove the failure of the primitive weight, in three parts. (a) A_N(τ) = ∞ for every
N ≥ 1 and Δτ > 0 when Ψ_T is bounded below near the nucleus. (b) The exact kernel
⟨r|e^{−τH}|r′⟩ is finite, so the failure belongs to the discretisation. (c) The hypothesis
of the product-formula theorem that −1/r violates. Each team member writes (a) by hand
before the solver runs: the guide's defence asks any member to explain it, and in the loop
this is the human attempt of S01, pasted into prompt0 §3b. The audit's perturbation test
uses V = −1/r^s. Pass: S01 closes with no BLOCKER and no MAJOR, and every member can
reproduce (a) without notes.

1.3 Show in writing that the weight to be sampled is real, positive and normalisable,
before any code runs. With the effective action: derive the slice weight and prove it finite
(S04, chunks K7 and K8), then prove the projected weight normalisable (S05, chunk K9). With
diffusion Monte Carlo: the corresponding statements for the importance-sampled weight, and
where its branching factor is unbounded. The person in the verification role signs the
statement, as the proposal already asks. Pass: S04 and S05 closed and the statement
written.

1.4 Fix the estimators before any code (S06, chunk K10): energy, ⟨r⟩, and P(r) with the
measure 4πr² dr, each marked mixed or pure, with the sign of its finite-Δτ bias where it can
be derived. Pass: the energy estimator, applied to the oscillator weight, reproduces the
closed form of S03 to 1e-8.

1.5 Build the independent reference now (S07): a radial solver (finite differences with
Richardson extrapolation, or shooting) giving E_1s, u(r), ⟨r⟩, ⟨1/r⟩ and ⟨r²⟩, and for each
trial function the mixed averages by quadrature. It is written by someone who will not write
the sampler. Pass: E_1s = −1/2 to 1e-8 and ⟨r⟩ = 3/2 to 1e-6 with grid convergence shown,
and one modified potential (a truncated V_δ) checked by a second method.

1.6 Read the central paper through the chunk procedure of Section 4. In phase 1 the required
chunks are K1, K2, K5, K7, K8, K9 and K10, run as S01–S06. K5, the oscillator, is the
positive control that the phase-2 code will be tested against.

1.7 Write the protocol, about two pages, by the team: the objects and units of 1.1, the
finiteness statement of 1.3, the estimators of 1.4, the reference values of 1.5, the method
with its fallback condition, the pre-registered parameter grid for phase 3 (step 3.1), and
the computing budget. Accept or reduce the scope here, as the guide says, and record the
decision.

Gate: the protocol; S01, S04, S05 and S07 closed; S02, S03 and S06 closed or deferred with
a recorded reason.

### Phase 2 (weeks 4–6): minimal implementation and the control case

The guide asks: "implement the chosen method with an inexact trial function and show the
control case in the first presentation." The common table adds executable code, a first
figure, the AI log and the first presentation, freezes the figures for that presentation,
and asks whether the minimal result already has a control case.

What it leaves unspecified. "The control case" is one case, unspecified. A single control
that passes says little about a Monte Carlo code, because many errors produce plausible
energies. The code needs a case it must reproduce exactly, a case that isolates the
estimator, and a case that must fail. The guide also says nothing about how the code is
produced, and the proposal notes that a request for "a path-integral Monte Carlo code for
hydrogen" usually returns the primitive discretisation, which runs.

Steps:

2.1 Build the code from small units, each an implementation consult in the guide's sense
(one agreed equation, one function, one limiting test), run as light subproblems S08–S11:
the tabulated slice weight, with its interpolation error measured against direct quadrature;
the staging moves of the paper's appendix (chunk K12); the estimators of S06; and a blocking
analysis, tested on synthetic correlated data with a known autocorrelation time. The driver
(the Metropolis loop, parameter files, seeds, output) is written by the person in the
implementation role. No program generated as a whole enters the code.

2.2 Run three controls, each with its pass criterion written in the protocol beforehand.
(a) Positive control: the same code with V = x²/2 reproduces the closed form of S03 at two
(β, m) pairs within two standard errors. (b) Exact trial function on hydrogen,
Ψ_T = e^{−r}: the end-bead local energy is −1/2 for every sample, which tests the local
energy and says nothing about the propagator. (c) Negative control: the primitive weight on
hydrogen with a cutoff η, showing the dependence on η that S01 predicts. The guide's
control case for the first presentation is (a), with (b) and (c) shown in support.

2.3 First estimate with an inexact trial function (Ψ_T = e^{−0.8r} recommended): E_1s at one
Δτ, with its error bar from blocking and the integrated autocorrelation time reported.

2.4 First presentation, week 6, nine minutes, all three members speaking: the question, the
action with its finiteness statement, the reference case (controls a–c), the preliminary
estimate, and the main risk. Figures frozen at the end of the phase.

Gate: each control recorded as passed or failed; the AI log complete for every unit; the
method confirmed or the fallback taken.

### Phase 3 (weeks 7–11): convergence, biases, draft

The guide asks: "sweep the time step and, depending on the technique, population or
discretisation; ask another model to identify sources of bias and verify the objections
with numerical tests." The common table adds a draft article, figures with error bars and a
table of controls, freezes the main results for the second presentation, and assigns the
draft to a team from another cohort for review.

What it leaves unspecified. A sweep designed after the results are seen tends to stop where
the answer looks right, so the sweep, the fit model and the acceptance criteria have to be
fixed before the runs. And a model asked for sources of bias after it has seen the results is
anchored on them; asking before is more useful.

Steps:

3.1 Pre-register the sweep in the protocol. At least five values of Δτ spanning a factor of
eight or more. Three projection times a factor of two apart, the shortest long enough that
the 2s admixture is suppressed by e^{−(3/8)τ} < 10⁻³, which needs τ ≥ 19 for the end-bead
energy and twice that for estimators at the middle bead, which sees only half the projection
on each side. The number of beads follows from Δτ and τ. For diffusion Monte Carlo, three
populations a factor of four apart. The fit model: for the effective action the order of the
Δτ error is not known (RQ3), so fit E_0 + aΔτ^p with p free and with p = 1 and p = 2 fixed,
report all three, and accept a fit when χ²/dof is consistent with one and E_0 moves by less
than its error when the largest Δτ is dropped.

3.2 Bias enumeration, in two steps. First, a second model in a fresh context receives the
protocol, the equations and the code, with no results, and lists mechanisms that could
produce false convergence, each with the symptom it would leave (new template, Section 7).
Second, each mechanism becomes a test whose criterion is written before it runs. Only then
does the audit loop see results, with the list in its `[FOCUS]` block: the results section
of the draft, written by the team, is answer-1 of S12, and the solver in that subproblem is
the team.

3.3 The guide's table of controls: mechanism, test, criterion, result, decision. It holds
the controls of 2.2 and every mechanism from 3.2.

3.4 The error budget: statistical (blocking), extrapolation in Δτ (the spread across fit
models), projection time, number of beads or population, the trial-function dependence of
any mixed estimator, the interpolation of the tabulated weight, and the box if one is used.
Each entry says how it was estimated.

3.5 Reproduce the hydrogen rows of the paper's Table II and test its claim that the
discretisation error is hidden in the statistical noise (S13, chunk K11). The second
presentation needs this comparison with the central reading.

3.6 One research question from the proposal, RQ1–RQ4, chosen in the protocol. With the
effective action, RQ3 comes out of 3.1 at no extra cost.

3.7 The draft article, and the cross-review by a team from another cohort, which tries to
reproduce one figure from the repository's instructions.

Gate: the draft, the table of controls and the error budget; main results frozen.

### Phase 4 (weeks 12–16): independent comparison, extension, article

The guide asks: "compare energy and radial distribution with the independent solver, and
write the article." The common table adds the second presentation, the extension, the final
article, the repository and the individual defence.

What it leaves unspecified. "Compare" comes with no measure of agreement. Elsewhere the
guide warns that a mixed average of r must not be presented as pure, and that a density per
unit volume must not be plotted as a radial probability. The comparison should be set up so
that neither mistake can happen without being visible.

Steps:

4.1 Energy: E_1s with its total uncertainty against −1/2, the difference stated in units of
that uncertainty.

4.2 Radial distribution: P(r) = 4πr²|ψ_0(r)|² from a pure estimator (the middle bead of the
projection; forward walking in diffusion Monte Carlo; an extrapolated estimator only if
labelled as one), histogrammed with an error per bin and compared with the radial solver
through χ²/dof. Also ⟨r⟩ = 3/2, ⟨1/r⟩ = 1, ⟨r²⟩ = 3, and the virial relation ⟨V⟩ = 2E. A
density per unit volume, if plotted, says so on its axis.

4.3 One extension, started only after the phase-3 gate. In order of value for the time: the
anharmonic perturbation λx⁴ of K5 together with K6, which asks why the average of the two
approximants works, a question the paper leaves open; the Yukawa perturbation of K8, which
shares ground with Project 05; the oscillator reference of K14; helium, K13; Duru–Kleinert.

4.4 Second presentation, week 13: the observable, the convergence controls, the independent
comparison, the interpretation, the extension, and a conclusion as strong as the evidence.

4.5 The article, ten to twelve pages, written by the team. The final documents of the
subproblems are technical annexes, and the declaration of AI assistance is assembled from
their `meta.yaml` files. One section discusses the central reading: what was confirmed, what
was corrected, and what is still open, from `errata.md` and the closed chunks.

4.6 Close-out: `/log` every open subproblem, write the container README, and run the
exploration prompt on the project as a whole, so that what is left goes to the queue in
`index.yaml`.

## 4. Dividing a paper into chunks

### 4.1 What a chunk is

A chunk is the part of a paper that becomes one subproblem. It has a statement that can be
written in prompt0 §1 without the rest of the paper; inputs that come either from that
statement or from chunks already closed; one output, which is a formula, a number, or a
verdict on an assertion; at least one test that could fail, decided before the run; and at
most one technique the solver has not used in an earlier chunk. A chunk whose answer would
need more than three independent checks, or more than about eight pages of derivation, is
split.

### 4.2 Procedure

1. Claim inventory. Read the paper once through and list every numbered equation, table
   entry and figure, and every sentence that asserts something without showing it: "it is
   easy to check", "a straightforward manipulation gives", "only makes things worse", "an
   observation for which we have no mathematical justification". For each, record the
   locator with the version of the paper; the kind (definition, derivation, quoted result,
   numerical result, assertion, observation); how the paper supports it (derived, cited,
   asserted, not at all); and what it depends on. The weakly supported claims are where the
   loop adds most.
2. Dependency graph and main path. Draw the dependencies and mark the path from the
   definitions to the main result. Chunks on the main path are required. The others are
   optional and are scheduled by value.
3. Cut. Cut where an output is a single formula, number or verdict that later claims use; at
   each new technique; and wherever the work changes from derivation to implementation.
   Merge neighbours that share a technique and are each too small to carry a test that could
   fail.
4. Classify each chunk by type and loop weight (4.3).
5. Decide what the solver sees. When the derivation is the point, the chunk runs
   closed-book: the problem in our own words, without the paper's formula for the result.
   When checking a printed result is the point, it runs open-book: the printed statement is
   given, with the instruction to establish it or find the error. Many chunks run
   closed-book in round 1 and open-book in round 2, through the corrector prompt. The mode
   is recorded in `meta.yaml` and `independence.md`.
6. Write the decisive test before the run, in the chunk ledger: the result that would show
   the solver reconstructed the answer from memory, the printed discrepancy it should find
   in the open-book round, and a perturbation variant. The auditor receives the test in
   `[FOCUS]` once the answer exists. The solver never receives it.
7. Keep a discrepancy ledger for the paper. Every difference between the print and a
   re-derivation gets an entry with its evidence and a status, and a subproblem settles it.
   Locators name the version, since an arXiv preprint and the journal version can differ.
8. Respect the interfaces. A downstream chunk uses an upstream result through prompt0 §3a
   only after the upstream subproblem has closed and frozen that section (proposed rule,
   Section 7). If an upstream result is reopened, the downstream subproblems are marked
   stale until rechecked.
9. Record who has read what. The paper, the proposal, this plan and the ledgers are prior
   knowledge, and whoever saw them, model or person, says so.
10. Close the paper. When the main-path chunks have closed, write a one-page reading note for
    the article: what was confirmed, what was corrected, what is still open.

### 4.3 Chunk types and loop weights

| type | what it asks | loop weight |
|---|---|---|
| derivation | derive a printed result, closed-book | full on the main path, otherwise standard |
| reproduction | recompute printed numbers | standard |
| assertion test | establish or refute a sentence the paper does not prove | standard |
| gap | explain something the paper leaves open | full |
| implementation | one function and one limiting test (the guide's implementation consult) | light |
| extension | the paper's method taken where the paper did not go | full |

Full: human attempt recommended, blind solve optional, audit loop to the stopping rule,
perturbation test, `/log`. Standard: audit loop to the stopping rule, perturbation test when
a variant exists, `/log`. Light: one audit round concentrated on pass 6a, the code; `/log`;
no blind solve.

### 4.4 Kole and De Raedt in chunks

The inventory gives 43 claims (`paper/kole-deraedt-2001/chunks.md`, §1), which cut into
fifteen chunks:

| chunk | content (arXiv v1) | type | weight | phase | depends on | needed |
|---|---|---|---|---|---|---|
| K1 | the primitive discretisation fails, (1)–(6) | derivation | full | 1 | — | yes |
| K1b | higher-order product formulas, p. 2 | assertion | standard | 1 or 3 | K1 | no |
| K2 | the lower bound (14), from (7)–(13) | derivation | standard | 1 | — | yes |
| K3 | the upper bound (15) and the trapezium remark | assertion | standard | 3 | K2 | no |
| K4 | the approximant (16); Ẑ1 and Feynman's bound | assertion | standard | 3–4 | K2 | no |
| K5 | the oscillator, (17)–(20) and Table I | derivation, reproduction | standard | 1 | — | yes |
| K6 | why (E_m + Ê_m)/2 works | gap | full | 3–4 | K5 | no |
| K7 | the bridge average as a Gaussian convolution, (23)–(24) | derivation | standard | 1 | K2 | yes |
| K8 | the Coulomb slice weight (25) and its finiteness | derivation | full | 1 | K7 | yes |
| K9 | is the hydrogen weight (27) a measure? | derivation, assertion | full | 1 | K8 | yes |
| K10 | energy and radial estimators | derivation | standard | 1 | K9, K5 | yes |
| K11 | Table II and the claim about discretisation error | reproduction | standard | 3 | code, K10 | yes |
| K12 | staging coordinates, appendix (28)–(30) | implementation | light | 2 | — | if used |
| K13 | helium, (21)–(22), (26), Table III | extension | full | 4 | K8, K10 | option |
| K14 | an oscillator reference in place of K, §V | extension | full | 4 | K2, K4 | option |

The draft statement, inputs, paper access, decisive test and perturbation variant of each
chunk are in `chunks.md` §3.

The inventory alone turned up sixteen candidate discrepancies or unsupported claims, besides
the reference error the proposal had already found. They are in
`paper/kole-deraedt-2001/errata.md` with their evidence, and three PI checks are in
`paper/kole-deraedt-2001/pi-checks/`. Three of them show what the procedure catches that a
summary reading does not. The printed eq. (19) grows without bound with m and cannot have
produced Table I; the formula re-derived from (17) reproduces twelve of the fifteen rows to
within a few units of the last printed digit, and the other three disagree with it by
far more than rounding (E6, E7). The proposal's
check 7 compared four rows and missed all of this. The hydrogen approximant (27) has a finite
integrand, which the paper takes as enough to sample it, but its integral over all space is
infinite (E14): the guide's distinction between an executable calculation and a valid
measure turns up inside the central reading itself. And the remark below Table I, that the
average of the two approximants is remarkably close to the exact energy, has a definite form
for the oscillator: the leading 1/m² errors cancel exactly and the average converges as m⁻³
(pc2), which makes K6 a well-posed question. All of these remain candidates until a
subproblem settles them.

### 4.5 Other papers

The same procedure applies to any paper the project reads closely. For this project the
likely next ones are a pair-density-matrix paper, if the effective action is replaced by the
exact pair action, and Duru–Kleinert, if that extension is chosen. Other teams in the course
can use it on their own central readings (R1–R10 of the guide). It is written here as a
draft; once it has been used on one paper it moves into `templates/` as a versioned template
(Section 7).

## 5. Subproblems

### 5.1 With the effective action (recommended)

| id | title | chunks | weight | guide phase, consult | owner role | depends on | hours |
|---|---|---|---|---|---|---|---|
| S01 | Failure of the primitive weight for −1/r | K1; K1b optional in round 2 | full | 1, derivation | formulation | — | 8 |
| S02 | The Jensen lower bound on the propagator | K2 | standard | 1, derivation | formulation | — | 5 |
| S03 | The oscillator in closed form; Table I | K5 | standard | 1, derivation | verification | — | 5 |
| S04 | The Coulomb slice weight and its finiteness | K7, K8 | full | 1, derivation | formulation | S02 helpful | 8 |
| S05 | Normalisability of the projected weight | K9 | full | 1, derivation and audit | verification | S04 | 8 |
| S06 | Estimators of E, ⟨r⟩ and P(r) | K10 | standard | 1, derivation | implementation | S05, S03 | 5 |
| S07 | Radial reference solver | — | light | 1, implementation | verification | — | 3 |
| S08–S11 | Code units: slice-weight table, staging moves, estimator functions, blocking | K12 | light | 2, implementation | implementation | S04, S06 | 3 each |
| S12 | Results and error budget (answer written by the team) | — | standard | 3, audit | verification | phase-2 code | 6 |
| S13 | Table II of Kole and De Raedt | K11 | standard | 3, audit | implementation | S12 | 5 |
| S14 | Extension | one of: K6 with λx⁴, K8 with Yukawa, K14, K13, Duru–Kleinert | full | 4, derivation | rotates | phase-3 gate | 8 |

Hours count the team's own time per subproblem: writing prompt0, the human attempt where
there is one, reading the answer, running the audit and the corrector, checking the code,
deciding, and `/log`. They are planning estimates, to be replaced by the recorded times
after S01 and S02.

Order in phase 1. S01, S03 and S07 have no inputs and start together. S02 runs alongside
them. S04 waits for S02 only if its owner wants S02's result in §3a. S05 waits for S04, and
S06 for S05 and S03. The critical path is S04 → S05 → S06, about three weeks at the one to
two rounds the loop has needed so far.

### 5.2 With guided diffusion Monte Carlo (fallback)

S01 and S07 are unchanged. S02–S06 become three subproblems: the importance-sampled
diffusion equation and its short-time Green's function with drift and branching (derivation,
full); the local energy of the trial functions, the cusp condition and the tail of the
branching factor, which is RQ2 of the proposal (derivation, full); and the mixed,
extrapolated and forward-walking estimators (derivation, standard). Kole and De Raedt are
then read through K1, K2, K5 and K8 only, as the comparison method in the article, and S13
becomes a comparison with Table II.

## 6. The guide's AI log, consultation forms and roles

The guide asks for a log with the date, the query, the answer used, the human decision, the
check, and any later correction. The loop already records most of it:

| guide's log field | where it lives in a subproblem |
|---|---|
| date | `meta.yaml`, `runs[].date` |
| query | `prompts/prompt0.md` and `prompts/corrector-prompt-k.md`, verbatim |
| answer used | `answers/answer-k.md`; `final/final.md` for the closed version |
| human decision | `README.md`, a new section "Decisions" (proposed, Section 7) |
| check | `assets/code/` with `.out` and `.coverage.md`; `audits/audit-report-k.md` |
| later correction | the dispositions in `audits/findings.yaml`; later answers |

The guide's four kinds of consultation map onto the subproblem types. Derivation consults
are the derivation and gap chunks; the guide's "no code yet" becomes, in prompt0 §5, a ban
on production code, while the verification checks of prompt0 §6.4 stay required.
Implementation consults are the light code units. Audit consults are the audit loop and the
bias enumeration of phase 3. Writing consults are not subproblems: the team writes the
article, any use of a model to separate observation, inference and the limits of a figure
is logged under "Decisions", and every reference a model proposes is checked in the primary
source and carries `{ver: tool}` or `{ver: human}`.

Roles. The guide rotates formulation, implementation and verification at the start of
phases 2 and 3. Each subproblem has an owner, who writes its prompt0 and human attempt and
takes its decisions. The person in the verification role runs the audits, keeps the table
of controls and signs the normalisability statement. By the end, the rotation should have
made each member the owner of at least one derivation subproblem and one code unit, which is
what the individual defence will test.

If you are working alone, the roles collapse into one person and the hours of Section 5
double in calendar time. The phase-1 set should then be S01, S04, S05 and S07, with S02, S03
and S06 run light.

## 7. Changes the pipeline needs

Proposed; none applied. Each one bumps a version and gets a `CHANGELOG.md` entry when it is
applied.

1. Containers and subproblem ids. `CONVENTIONS.md` §8: `problems/P003-slug/` holds
   `S01-slug/`, `S02-slug/`, …, each with the usual layout. The subproblem id is
   `P003.S01`; finding ids are unchanged inside a subproblem and are written `P003.S01/F1.2`
   from outside it. `layout.md` gains the container files: `README.md` (the project
   logbook), `PLAN.md`, `project.yaml` (method, subproblem list with status and
   dependencies, phase gates), `paper/`, `protocol/`, `controls.md`, `error-budget.md`,
   `article/`. `index.yaml` gets one row per subproblem with a `project` field.
   `New-Problem.ps1` gets `-Project` and `-Sub`. `/log` accepts `P003.S01`, and a project
   close-out builds the AI-use declaration from every subproblem's `meta.yaml`.
2. Interface rule, `CONVENTIONS.md` §6: a result from another subproblem enters prompt0 §3a
   only if that subproblem closed with ACCEPT or ACCEPT-WITH-FIXES and the section is on its
   final frozen list; otherwise it enters §3b. A reopened upstream result marks its
   downstream subproblems stale in `project.yaml`.
3. Paper chunking: Section 4 of this plan becomes `templates/paper-chunking.md` v1.0, after
   it has been used on Kole and De Raedt.
4. Bias enumeration: `templates/bias-enumeration-prompt.md` v1.0 for phase 3. A model in a
   fresh context receives the protocol, equations and code with no results, and lists
   mechanisms of false convergence, each with the symptom it would leave.
5. Implementation units: a filled example of prompt0 §4–§5 for one function and one
   limiting test, first in S07. A template variant only if the pattern recurs.
6. A "Decisions" section in the README skeleton that `New-Problem.ps1` writes: date,
   decision, reason, evidence.
7. The audit-prompt changes already queued in `claude/start-here.md` (a verdict rule for
   honest partial answers, a cap on findings, the pass 1 drift), as audit v1.5, before S01
   is audited. Gap and normalisability chunks are likely to end in honest partial answers,
   which the current verdicts would mark REJECT.
8. Solver context. Closed-book chunks run in a fresh context outside the Vibe Physics
   project, whose memory and documents describe the proposal and this plan, with
   `CONVENTIONS.md` and prompt0 as the only attachments. `meta.yaml` records
   `context: clean` or `context: project`.

## 8. Calendar and budget

In course weeks, following the guide and the proposal. Cohort A presents in weeks 6 and 13;
the last week is for the article, the reproducibility check and the interviews.

| weeks | phase | work | evidence |
|---|---|---|---|
| 1–2 | 1 | S01, S03, S07 and S02 start; human attempts for S01; the paper inventory (done in this plan) | — |
| 3–4 | 1 | S04, S05, S06; the protocol; the scope decision | the protocol; S01, S04, S05, S07 closed |
| 4–6 | 2 | S08–S11; the driver; controls a–c; the first estimate | first presentation, week 6; figures frozen |
| 7–9 | 3 | the pre-registered sweep; bias enumeration; S12 | the table of controls |
| 10–11 | 3 | S13; the error budget; the draft; cross-review | the draft; results frozen |
| 12–13 | 4 | the comparison of 4.1–4.2; S14 starts | second presentation, week 13 |
| 14–16 | 4 | the extension; the article; close-out | article, repository, defence |

Budget, with three people at about four hours a week each, as the proposal assumed: about
190 team-hours. The subproblems of Section 5.1 take about 75. The driver, production runs
and analysis take about 35; the protocol, the two presentations and the article about 45;
that leaves about 35 of slack. If the course is already past week 4, phase 1 shrinks to S01,
S04, S05 and S07, with S02, S03 and S06 run light, and the protocol may take Sections 3–5 of
the proposal as declared prior knowledge.

## 9. Risks the method adds

The physics risks are in Section 12 of the proposal. These are the ones that come from
running the project through the loop.

- Contamination. The guide's own statement of the problem gives the divergence away, the
  proposal contains proofs of its Propositions 1 and 2 and a full reading of the paper, and
  this plan and its ledgers contain the PI's expectations. Controls: closed-book runs in a
  clean context (Section 7, item 8), a perturbation variant in every derivation chunk, and
  honest declarations.
- Errors propagating between subproblems. A wrong result frozen in S04 would flow into S05
  and S06. Control: the interface rule and stale marking (Section 7, item 2).
- The cost of the loop. Fourteen subproblems at one to three rounds each is a lot for a
  semester. Controls: the loop weights, the hour estimates checked against S01 and S02, and
  the reduced phase-1 set.
- Code written by models. The guide does not accept unchecked AI output as a result.
  Controls: code enters only as tested single functions, the driver is written by the team,
  and every unit goes through audit pass 6a.
- Numbers in audits. In P002 an auditor reported a value that its own code did not print.
  Controls: audit ground rule 8, and every number in an audit is re-run before a finding
  that rests on it is accepted.
