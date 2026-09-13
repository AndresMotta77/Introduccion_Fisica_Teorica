# Exploration prompt — v1.0

Sent to a third model, in a fresh context, once a problem closes. Its output is
not prose for reading; it is the input queue for the next problems.

Attached: `[FINAL RESULT]`, `[RISK REGISTER]`, `[SOURCES]`, `CONVENTIONS.md`.

---

You are given a closed physics problem with its final derivation, its risk
register, and its bibliography. Propose where to go next.

Produce between six and ten branches, in four categories, and do not pad any
category to fill it — say "none worth pursuing" if that is the case.

**A. Harden.** Things this result still rests on that could be made solid: an
assumption in the risk register worth discharging, an unverified citation worth
resolving, a step that was `[R]` and should be `[D]`, an approximation whose
error was never estimated.

**B. Generalize.** The same problem with a constraint removed: another
dimension, a non-symmetric configuration, finite temperature, a curved
background, an interaction turned on, a boundary condition relaxed. Say what
breaks in the existing derivation when the constraint goes.

**C. Perturb.** Small, deliberate modifications that change the answer. These
are worth queueing independently of interest, because a modified problem has no
memorized answer, and solving it is the sharpest available test of whether the
original derivation was real.

**D. Connect.** Places this result already appears, in a different language, in
another part of physics. Name the correspondence precisely enough to check it.

For each branch, give:

- `title` — one line, in the form of a problem statement.
- `category` — A / B / C / D.
- `why` — what it would settle, in two sentences.
- `difficulty` — routine / substantial / research-level, with the reason.
- `prerequisites` — what must be true or known first, including other branches.
- `first_step` — the concrete first move, specific enough to become prompt0 §5.
- `expected_obstruction` — where you think it gets hard.
- `literature` — whether this is done already, with a locator and verification
  status per `CONVENTIONS.md` §2, or "unknown to me" if you cannot confirm it.
  Do not guess. A branch that is already solved in the literature is still
  worth doing here, but you should know which kind it is before starting.

End with `ranked` — the branches in the order you would do them, with one
sentence on why that order.

Return as a markdown document and as a YAML block that the log skill can append
to the problem index.
