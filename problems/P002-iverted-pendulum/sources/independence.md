# Independence record — P002

The file to read first when revisiting this problem. It is the honest account of
what the solver knew going in, and where the derivation could have leaned on it.

Assembled by `/log` from `answers/answer-2.md`: §1 (Prior-knowledge declaration)
and §6 (Convergence check), both verbatim, plus the notes below.

Solver: Claude Opus 5, effort high (user-reported, from `prompts/prompt0.md` §0).
Auditor: Gemini 3.1 Pro Avanzado, extended-reasoning option, effort unknown
(user-reported).

---

## 1. Prior-knowledge declaration

**Do I recognize this problem, and from where?** Yes, immediately, and in two
ways. It is the Kapitza pendulum — dynamic stabilization of the inverted
position by rapid vertical vibration of the support — which I know as a standard
worked example in the classical-mechanics literature. I also recognized the
specific wording as a Harvard "Problem of the Week" sheet by David Morin, which
prompt0 §1 states outright. I did not open either source before deriving; see
the ordering note below.

**What result do I believe is the standard one?** Written out before deriving
anything, from recall alone:

- The pendulum does not fall because the fast shaking of the pivot, averaged
  over a drive period, contributes a term to an effective potential that has a
  minimum at the inverted position. The size of that term goes like the square
  of the amplitude of the fast wiggle, which itself is proportional to the sine
  of the angle from the vertical, so the extra potential is proportional to
  $\sin^2$ of that angle — a hill at the horizontal, hence a well at both
  vertical positions.
- The inverted position is stable when $A^2\omega^2 > 2gl$.
- The slow oscillation frequency is
  $\Omega=\sqrt{\dfrac{A^2\omega^2}{2l^2}-\dfrac{g}{l}}$, reducing to
  $\Omega\approx A\omega/(\sqrt2\,l)$ when $A\omega\gg\sqrt{gl}$.

**What is the standard route, and where is it presented?** The route I recall is
Kapitza's separation of the motion into a slow part and a fast part, with the
fast part solved first and then averaged out, producing an effective potential
for the slow part. I recall this being presented in Landau and Lifshitz,
*Mechanics*, in the section on motion in a rapidly oscillating field, which I
believe is §30 — recalled, not checked at the time of writing this section. I
also recall the alternative route, which treats the linearized problem as a
Mathieu equation and extracts the stability tongue.

**What am I anchored on?** On the three bullets above, which I wrote from memory
and which the derivation below then had to reproduce. Section 3c of prompt0 says
only "we expect some sort of equilibria", which is too weak to anchor anything,
though it is worth sharpening and I do so in §5. The honest statement is that I
knew the target before I started, so the value of this document lies in whether
each step is forced, and in whether the checks in §4 could have failed. I have
tried to make both auditable: every numerical check in §4 is run not only on my
claim but on deliberately mutated versions of it, and the mutants are reported
alongside.

**Ordering note, which matters for the audit.** The derivation in §3 and every
computation in §4 were completed and their outputs recorded before any source
was retrieved. The retrieval in §8 happened afterwards, for the sole purpose of
resolving prompt0's general reference into a locator and checking it, as §6.3
requires. The comparison with what was retrieved is in §6. I mention this
because the previous problem in this repository failed precisely by retrieving a
published solution instead of deriving one, and the ordering is the only thing
that distinguishes the two cases from the outside.

---

---

## Perturbation test

**Not run.** `templates/audit-prompt.md` pass 8 and category C of the
exploration prompt both call for it, and `claude/workflow-feedback.md` §3 calls
it the sharpest test in the system. Neither the round-1 audit nor any later step
performed one for this problem.

What it would have looked like here: change one thing so that the memorised
answer becomes wrong, and see whether the derivation tracks the change or breaks.
Three candidates, in increasing order of how much they would have told us.

1. Drive the pivot **horizontally** instead of vertically,
   $x_p(t)=A\cos\omega t$. The effective potential picks up a $\cos^2$ rather
   than a $\sin^2$ dependence, so the stabilised positions move to the
   horizontal rather than the vertical. A derivation that had memorised
   "$\sin^2\Theta$" would produce the wrong equilibria.
2. Replace the point mass by a **uniform rod** pivoted at one end. Then $l$ is
   replaced by $I/(m\,l_{\rm cm}) = \tfrac{2}{3}l$ in some places and not
   others, and the threshold and the frequency shift by different factors. A
   reconstruction would almost certainly rescale both the same way.
3. Drive at $y_p = A\cos\omega t + B\cos 2\omega t$. The averaging then has two
   fast components and the $\langle\cos^2\rangle = \tfrac12$ step acquires a
   second term; the answer is no longer a single $A^2\omega^2$.

Recorded as not-run rather than as a gap to be filled retroactively: running it
now, after the answer and the audit are both on the record, measures something
different from running it inside the loop.

## What the audit found about independence

Round 1, pass 8 — independence audit: **Pass**. "The timescale separation and
balancing of orders is non-circular and properly motivated." The auditor did not
identify any anchoring step beyond the two the solver self-reported in §6.

Anchoring steps self-reported by the solver: 5 (listed in §6 below, items 1–5).
Anchoring steps found by the auditor and not self-reported: 0.

That asymmetry is worth noticing rather than celebrating. An auditor that finds
nothing the solver did not already confess has not independently probed the
anchoring; it has read the confession and agreed with it. The blind-solve stage
(`templates/blind-solve-prompt.md`) exists for exactly this and was not run for
P002.

---

## 6. Convergence check

**Does the derivation reproduce the declared result?** Yes, in all three parts.
§1 declared $A^2\omega^2>2gl$ and
$\Omega=\sqrt{A^2\omega^2/(2l^2)-g/l}$ and the $\sin^2$ effective potential;
(37), (41) and (31) are those. There is nothing to reconcile and no
disagreement to report.

It also agrees with the published solution, retrieved after the fact (§8): that
solution's equation (4) is $l\ddot\theta-\ddot y\sin\theta=g\sin\theta$, which is
(15) here, and its equation (10) is $\Omega=\sqrt{a^2\omega^2/2-g/l}$ with
$a=A/l$, which is (41) here. The routes differ: the published solution
linearizes first and works with the resulting Mathieu-type equation and an
envelope ansatz, while §3 keeps the nonlinearity and constructs an effective
potential. The effective-potential route yields $\Theta_{\rm c}$ and the
$\Theta=\pi$ results as by-products, which the linearized route does not reach.

It agrees, third, with a computation performed by a party that did not write
this derivation: the round-1 auditor extracted the slow frequency from the
Floquet phase of the linearized equation and found it consistent with (41) to
$O(\varepsilon^2)$. That is the only check in this document whose *method* was
not chosen by me, which makes it worth more than its arithmetic. I reproduced it
(§4.9), corrected the sign of its reported deviation, and extended it into a
sweep. Its real value turned out not to be the single point at all but the
constraint it places on N4: the frequency it measures must vanish exactly where
N4's independent bisection puts the boundary, and it does.

**Steps a person who did not know the target could not have chosen as I did.**
Listed even where I believe each is justified.

1. **The split $\theta=\Theta+\xi$ (18).** This is the method, and it is not
   forced by the problem. Someone meeting this cold could arrive at it by
   noticing that the equation contains exactly one imposed fast timescale, but
   they could equally linearize and reach for Floquet theory, as the published
   solution effectively does. I knew the method. Mitigation: N4 verifies the
   threshold by the other route entirely, so the answer does not depend on this
   choice being the right one.
2. **Dropping $c_1$ and $c_2$ in (23).** Motivated — $c_1t$ contradicts
   boundedness, $c_2$ is already called $\Theta$ — but a reader who did not know
   that the answer contains no secular term might have hesitated. I regard this
   as forced rather than chosen, because the assumption being used to derive
   $\xi$ is the same assumption that excludes $c_1$.
3. **Keeping $\varepsilon\omega^2\cos(\omega t)\,\xi\cos\Theta$ while
   $\langle\ddot\xi\rangle$ vanishes.** This is the crux, and it is the one step
   where knowing the answer could substitute for an argument. It is forced by
   the order count in §3.3: both that term and $\ddot\Theta$ are
   $O(\varepsilon^2\omega^2)$, whereas $\langle\ddot\xi\rangle$ is exactly zero
   by periodicity rather than small. If I had dropped it, the averaged equation
   would have had no stabilizing term at all and $\Theta=0$ would never be
   stable — the derivation would have failed loudly, not quietly.
4. **Holding $\Theta$ fixed across a drive period** in (21) and in (25)–(27).
   This is the leading order of a systematic expansion and its error is
   $O(\varepsilon^2)$; the point of N3 is that this error was not asserted but
   measured, and came out at the predicted order with a clean coefficient.
5. **Nothing was inserted for later convenience.** The factor $\tfrac12$ in (28)
   is $\langle\cos^2\rangle$ and enters at (27); the factor $\tfrac14$ in (29)
   is half of it, from writing $\sin\Theta\cos\Theta$ as a derivative. Neither
   was available to be tuned.

**Would the derivation still run if the standard result were slightly
different?** No, and the places it would break are identifiable.

- **A different numerical factor.** The $\tfrac12$ comes from
  $\langle\cos^2\omega t\rangle$ at (27) and nowhere else. Had the target been
  $A^2\omega^2>gl$ or $>4gl$, there is no step in §3 that could have been bent
  to produce it; I would have had a derivation disagreeing with my recollection
  and would have had to report both, per the protocol. I would have noticed,
  because the mutation blocks in N3 and N4 reject those factors outright.
- **A different power of $\omega$.** The threshold's $\omega^2$ and the fact
  that $\xi$ is $\omega$-independent both trace to the exact cancellation at
  (21)–(24): $\ddot y_p$ brings down $\omega^2$ and the double integration
  removes it. That cancellation is visible and unforced. If the standard result
  had $\Omega\propto\sqrt\omega$, say, the derivation would have broken at (24),
  where there is simply nowhere for a half-power to come from.
- **A different power of $A$.** Ruled out independently by the symmetry argument
  in §4.6 item 4: results must be even in $A$.

The most honest statement of residual risk is this. I knew the answer before I
started, and no amount of prose can make that not so. What can be checked from
outside is whether the checks in §4 could have failed, and they could: N2 did
fail on its first run and the failure is reported; every claim is run against
mutants that are rejected; and the two strongest checks, N3 and N4, are
convergence tests against exact routes that share no algebra with §3.3–§3.6.

---
