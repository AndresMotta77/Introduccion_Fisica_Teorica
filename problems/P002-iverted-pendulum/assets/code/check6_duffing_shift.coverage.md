# Coverage note — check6_duffing_shift.py

Checks: N7. Full discussion, with the verbatim output, in
`answers/answer-2.md` §4.8 — "4.8 Check N7 — the amplitude–frequency relation, on the bare Duffing equation".

Required by `CONVENTIONS.md` §1.1: a check with no stated blind spot has not
been thought about. Both halves are reproduced here verbatim from the answer so
that this file can be read on its own.

Output: `out_check6.txt` in this directory.

---

What this would have caught: a wrong coefficient in (53)–(56). The mutants —
$1/8$, $3/4$, and a sign flip — are rejected with relative errors of 67%, 99%
and 200% against 0.3% for the derived value. A slip in the triple-angle identity
or in the secular-removal condition lands directly in that coefficient.

What it would **not** have caught: anything about whether the pendulum's slow
dynamics really is (48) with that particular $\alpha$. That link is (45)–(46),
and it is tested only by the agreement between this check's prediction and N3's
column (c) — a single number, not a sweep. It also tests only the leading
amplitude correction; nothing here speaks to amplitudes approaching
$\Theta_{\rm c}$, where (47)'s quartic truncation fails.

