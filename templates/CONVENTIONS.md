# Conventions — v1.2

Shared vocabulary for every prompt, answer, audit and log in this repository.
Both the solver and the auditor are given this file. Changing it means bumping
the version and recording the bump in each affected problem's `meta.yaml`.

---

## 1. Provenance tags

Every non-trivial claim, equation or step carries exactly one tag, written at
the start of the line or immediately after the equation number.

| Tag | Meaning | Requirement |
|-----|---------|-------------|
| `[D]` | Derived here, in this document, from premises stated here. | Nothing external is load-bearing. |
| `[S]` | Standard result invoked rather than re-derived. | Requires a locator (§2). |
| `[V]` | Claim checked against a source actually retrieved during this session. | Requires a locator and the retrieval note. |
| `[R]` | Recalled from training. No source retrieved, locator not confirmed. | Must also appear in the Risk register. |
| `[A]` | Assumption, ansatz, gauge choice, branch choice, convention. | Requires a justification and a note on what fails if it is wrong. |
| `[N]` | Numerical or symbolic computation. | See §1.1. |
| `[?]` | Step the solver is not confident in. | Flagged for the auditor by construction. |

Rules:

- A result may not rest on `[R]` alone unless the Risk register says so explicitly.
- `[S]` without a locator is not `[S]`. Downgrade it to `[R]` and say so. A
  missing citation declared honestly is acceptable; an invented one is a BLOCKER.
- Routine algebra does not need a tag. Anything a reader could dispute does.

## 1.1 What an `[N]` claim must carry

A computation is not an oracle. The code was written by the same party that
produced the derivation, so it can encode the same error and still report a
pass. `[N]` therefore carries more than a printout:

- The code verbatim, standalone and runnable from a clean interpreter, with a
  fixed seed and library versions noted.
- Its output verbatim, not paraphrased, for every run made — not only the ones
  that agreed.
- A **coverage note**: what this check would have caught, and what it would not.
  Both halves. A check with no stated blind spot has not been thought about.
- Every assumption the check relies on — positivity, reality, a branch, a
  principal value, a sign convention — restated as an `[A]` in the text. An
  assumption that lives only inside a `simplify` call is a laundered assumption
  and counts as a defect even when the result is right.
- Where the quantities in the check came from. A check whose inputs are
  intermediate results of the derivation it is checking is circular; a check
  that recomputes from the problem statement is not.

Failing a check is a normal outcome and is reported as such. Editing the check
so that it passes, without saying so, is the most damaging thing that can happen
in this workflow, because it converts an error into a logged verification.

## 2. Citation locators

A general reference is not a citation. The locator must let a reader find the
claim in under a minute.

- Books: `Author, Title, edition, §section, eq. (n)` or `p. n`.
  Acceptable: `Jackson, Classical Electrodynamics, 3rd ed., §3.3, eq. (3.33)`.
  Not acceptable: `Jackson, chapter 3` or `Jackson`.
- Papers: `Author et al., Journal vol, page (year), eq. (n)` plus DOI or arXiv id.
- Lecture notes and theses: author, title, year, section, and a URL.

Every citation carries a verification status:

- `{ver: tool}` — retrieved this session; the locator was read and confirmed.
- `{ver: human}` — the user confirmed it.
- `{ver: no}` — from memory. The claim may be right and the locator wrong.

## 3. Used vs consulted

The Sources section is split in two and the split is not optional.

- **Used** — the result would change if this source were removed or wrong.
- **Consulted** — background, notation, orientation. Did not affect the result.

## 4. Severity levels (audit findings)

| Level | Meaning |
|-------|---------|
| `BLOCKER` | The final result is wrong, or a step is invalid in a way that changes it. |
| `MAJOR` | The result may survive, but the text as written does not establish it: a gap, a circularity, an unjustified step, a load-bearing unverified citation. |
| `MINOR` | Correct but incomplete or imprecise: a missing intermediate step, an unstated domain of validity, inconsistent notation. |
| `NIT` | Presentation only. |
| `QUESTION` | The auditor is unsure and is asking, not asserting. |

## 5. Verdicts

- `ACCEPT` — no BLOCKER, no MAJOR, no open QUESTION.
- `ACCEPT-WITH-FIXES` — only MINOR and NIT remain; one more pass closes them.
- `REVISE` — at least one MAJOR.
- `REJECT` — at least one BLOCKER, or the answer does not address the problem.

## 6. Loop control

- **Before the loop.** The human attempt (`templates/human-attempt.md`) is
  written and committed before prompt0 is sent. It is a prior, and a prior
  recorded after seeing the model's answer is not one.
- **After the loop.** The compliance probe (`templates/compliance-probe.md`) is
  run once on a claim known to be right, and its outcome recorded. The final
  result is taken from the last pre-probe answer.
- **Ground truth.** Where an external check exists — a professor's correction,
  an answer key, a measurement — record it in `meta.yaml` along with *when* it
  arrived relative to the loop. Ground truth that arrived mid-loop shaped the
  later rounds and cannot also be used to validate them.
- **Stopping rule.** Stop when a full audit round returns no BLOCKER and no MAJOR.
- **Escalation.** At round 4, stop and hand the problem to a human regardless of
  verdict. A loop that has not converged in three rounds is not converging.
- **Thrash detector.** If a finding reappears that was recorded as resolved two
  rounds earlier, halt the loop and log it. Recurrence means the two models
  disagree about a fact, and no further rounds will settle it.
- **Frozen list.** Each audit publishes the sections it verified as correct.
  Those may not be rewritten in the next round without a new finding against them.

## 7. Writing conventions for the final document

- Natural prose. No `\emph`, no bolded keyword openers, no bulleted summaries
  standing in for argument.
- Intermediate algebraic steps are written out even when they are easy. The
  reader should never have to reconstruct a line.
- Every symbol is defined at first use, and a symbol table appears at the front.
- Equations that are referred to later are numbered.

## 8. Identifiers

- Problems: `P007`, folder `problems/P007-short-slug/`.
- Rounds: `k = 1, 2, 3, …`; `answer-1.md` is the first answer, audited by
  `audit-report-1.md`, which produces `corrector-prompt-1.md`, which produces
  `answer-2.md`.
- Findings: `F<round>.<n>`, e.g. `F2.3`. Finding ids are stable across the whole
  problem so that a rebuttal in round 3 can refer to `F1.4`.
