# Changelog

Template versions are recorded per problem in `meta.yaml`. Bump on every change,
so that runs stay comparable.

## v1.2 — 2026-09-12

Two additions taken from the practice already visible in problem 01 of this
repository, which did both of these by hand.

- `human-attempt.md` v1.0, new — the timed attempt, written and committed before
  prompt0 is sent. Git history is what makes the ordering checkable, hence the
  `human_attempt_first` gate. This closes the gap noted in the original feedback,
  where the human node in the workflow diagram led nowhere.
- `compliance-probe.md` v1.0, new — after the loop converges, one bare assertion
  with no argument against a claim known to be right, and a recorded outcome of
  `held`, `asked` or `caved`. A `caved` outcome does not invalidate the answer;
  it means the audit agreements along the way were weaker evidence than they
  looked, since the same disposition produced them.
- `CONVENTIONS.md` v1.2 — §6 gains the before-loop and after-loop steps, and a
  rule that external ground truth records *when* it arrived. Ground truth that
  arrived mid-loop shaped the later rounds and cannot also validate them.
- `prompt0.md` v1.2 — §3b now draws from `human/attempt.md` and requires the
  solver to compare its hypotheses against the user's, naming the ones the user
  relies on that are unnecessary and the ones the solver needs that the user
  never stated.
- `audit-prompt.md` v1.2 — pass 1 checks that the comparison was actually made.
- `/log` v1.2 — three new gates (`human_attempt_first`, `compliance_probe_run`,
  `ground_truth_timing`), a `human/` folder and `audits/compliance-probe.md` in
  the layout, and `human_attempt`, `ground_truth` and `compliance_probe` blocks
  in `meta.yaml`.

## v1.1 — 2026-09-12

Correction: code was framed as an oracle. It is not. The solver writes the
verification code, so the code can encode the same misunderstanding as the
derivation and still print PASS. A self-written check is evidence, and it is an
artifact under audit like any other.

- `CONVENTIONS.md` v1.1 — new §1.1 setting out what an `[N]` claim must carry:
  standalone reproducible code, all runs and not only the agreeing ones, a
  coverage note saying what the check would and would not have caught,
  every in-code assumption restated as an `[A]` in the text, and the provenance
  of the check's own inputs.
- `prompt0.md` v1.1 — §6.4 rewritten from "Independent verification" to
  "Computational checks". Adds the rule that a check should recompute from the
  problem statement rather than from the derivation's intermediate results, the
  list of ways a check fails silently (circular, vacuous, laundered assumptions,
  wrong quantity, unfailable tolerance, selective reporting), and the requirement
  to disclose when a check was edited to make it pass.
- `audit-prompt.md` v1.1 — pass 6 split into 6a (read the solver's code for
  circularity, vacuity, laundered assumptions, wrong quantity, selective
  reporting, library semantics) and 6b (compute independently from the problem
  statement, and state what your own check does not cover). Ground rule 2
  rewritten accordingly.
- `/log` v1.1 — three new gates: `code_coverage_notes`, `code_not_circular`,
  `code_audited`. `code_output_present` now requires every run, not only the
  agreeing ones. `assets/code/` gains a `.coverage.md` per script.
- `FEEDBACK.md` §1 and `README.md` corrected: "executable oracle" → "executable
  check, treated as evidence rather than proof".

## v1.0 — 2026-09-12

Initial structure: conventions, prompt0, audit prompt, blind-solve prompt,
exploration prompt, the `/log` skill, and the problem folder layout.
