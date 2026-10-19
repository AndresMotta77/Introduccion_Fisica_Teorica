# MISSING — exploration

**Not run** at the time of `/log` (2026-10-19).

`templates/exploration-prompt.md` v1.0 describes the step that follows the final result: a third model generates research branches from the closed problem. Each branch is recorded with its difficulty, prerequisites, first step, expected obstruction, and whether the literature has already done it. The branches then go into `index.yaml` as a queue. The step was not run for P003.S01, so `branches_queued` is empty.

The raw material already exists: `final/final.md` §9 lists seven open questions. The concrete and cheap ones are:

1. Confirm, against the books themselves, the two locators that are still `{ver: no}`: Reed–Simon I, Theorem VIII.31 (the semigroup clause), and Simon 1982, Theorem B.7.1. This needs a human with library access, and the result would be recorded as `{ver: human}`.
2. A third, Feynman–Kac Monte Carlo route to $K_\tau(\mathbf 0,\mathbf 0)$. It would also test finiteness away from the origin, which check C4 does not.
3. A Monte Carlo test of the $N$-th power law (B16) at $N=3$ or 4.

Within P003 these may be superseded by the later subproblems in `../PLAN.md`; that is for the PI to decide, not `/log`.
