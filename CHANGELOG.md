# Changelog

Template versions are recorded per problem in `meta.yaml`. Bump on every change,
so that runs stay comparable.

## v1.7 — 2026-09-14

The compliance probe comes back as a human note rather than a test.

Removing it in v1.6 left nothing recording whether a model's agreement meant
anything. The probe was one way to find out and it had costs: an extra call, a
contaminated conversation, and a test run on the model rather than an
observation of it. The observation is the part worth keeping.

- `CONVENTIONS.md` v1.5 — §6 regains an "after the loop" step: write your own
  account of how the model behaved while being corrected. Not a test, not a
  gate, no template.
- `New-Problem.ps1` — the problem README skeleton gains §5, "How the model
  handled being corrected", with prompts for what tends to be worth noting.
- `/log` — collects that section if the user wrote one, and is explicitly
  forbidden from writing it or editing their wording. A model grading its own
  conduct in the conversation it was part of is not evidence.
- `README.md` — the note appears in the method diagram and the starting steps.

## v1.6 — 2026-09-14

The compliance probe is removed from the workflow at the user's request.

- `templates/compliance-probe.md` deleted.
- `CONVENTIONS.md` v1.4 — §6 loses the "after the loop" step.
- `/log` v1.6 — the `compliance_probe_run` gate, the collect-step item and the
  must-not-do rule about softening a `caved` outcome are all gone.
- `meta.yaml` — the `compliance_probe` block and its template version entry
  removed; `New-Problem.ps1` no longer seeds either.
- `README.md` — removed from the method diagram, the file table, the four
  things that matter, and the starting-a-problem steps.

P001's records are left untouched. `audits/compliance-probe.md` there, and the
`compliance_probe` entry in its `index.yaml` row, describe an exchange that
actually happened, and rewriting past records to match current rules is what
this repository exists to avoid.

What goes unmeasured now: whether a model's agreement with an audit finding
means it was persuaded or only that agreeing is the cooperative move. The
corrector prompt's disagreement clause and `rebuttals_upheld` in `meta.yaml`
remain as the weaker signal.

## v1.5 — 2026-09-14

Three of the six changes proposed on 2026-09-13, plus the `latex_clean` gate.

- `audit-prompt.md` v1.4 — new ground rule 8: never report a computation you did
  not run. If code execution is unavailable, say so in the run header, mark
  passes 3, 5 and 6b "not performed", and say what was checked by reasoning
  instead. Prompted by the P002 round-1 audit, which reported a Floquet value of
  4.2764 from a snippet that prints 4.2867 when actually executed.
- `audit-prompt.md` v1.4 — INPUTS rewritten: attachments first, pasting as the
  fallback, with the typed message reserved for the audit prompt itself.
  prompt0 is named as the complete prompt, sections 0 through 8, since the
  compliance passes check against §4, §5 and §6. New `[CODE]` entry for scripts
  uploaded separately, which pass 6a otherwise has no instruction to read, and
  which flags a script that diverges from the code shown inline in the answer.
- `/log` v1.5 — new Step 1a: how to split the auditor's pasted reply into
  `audits/audit-report-k.md` and `prompts/corrector-prompt-k.md`, verbatim,
  including not correcting the auditor's arithmetic. This is how Part A reaches
  the repository now that both parts go to the solver, and it replaces the
  proposed template change that would have had the auditor append Part A to
  Part B.
- `/log` v1.5 — new `latex_clean` gate, report-only: undefined references,
  undefined citations, overfull boxes past 10pt, and `\emph` in `final.tex`,
  parsed from the compile log after a successful build. Report-only because
  Step 3 forbids rewriting the final document; prose typos are raised as audit
  pass 10 findings in a round instead of being patched at log time.

Still queued from the 2026-09-13 proposal: the pass 1 drift fix, the
partial-answer verdict rule, and the findings cap. The Part A record change is
now handled in `/log` instead, and the compliance-delegation refactor remains
out of scope.

## v1.4 — 2026-09-14

- `audit-prompt.md` v1.3 — new pass 10, presentation: LaTeX-inside-markdown
  problems, symbol consistency, grouping, delimiters, macros outside the
  template's packages, equation numbering, units, and prose typos. Ordered by
  importance rather than by visibility, since a symbol typo is a physics error
  in disguise while a misspelt word is not. Two rules attached: collapse typos
  into one finding rather than one finding each, and report without rewriting,
  because the solver owns the text.
- `audit-prompt.md` v1.3 — Part A now opens with a run header stating the
  auditor's model, effort, tools and whether it actually executed code, with
  `unknown` required rather than a guess. This is the auditor half of the
  model-and-effort record; previously it could only come from the user.
- `/log` — takes the auditor's model and effort from that header when present,
  recorded as `self-reported`, and says so rather than presenting it as
  confirmed.

Not included, still queued: the six changes proposed on 2026-09-13 (attachments
in INPUTS, the pass 1 drift fix, no-un-run-computations, the partial-answer
verdict rule, Part A reaching the record, and the findings cap), plus the
`latex_clean` report-only gate for `/log`.

## v1.3 — 2026-09-13

The human attempt stops being a requirement. It was never the file that
mattered, only the fact that something of your own predated the model's answer,
and demanding a markdown file made a handwritten draft look like a failure.

- `human-attempt.md` v1.1 — reframed as recommended rather than required, and
  format-agnostic: a scan, a photo, loose notes, or nothing. Explicit
  instruction not to retype handwriting for the template's sake. The one thing
  kept strict is honesty about *when* it was recorded.
- `/log` v1.3 — the `human_attempt_first` gate is removed. The collect step now
  records the attempt if there is one, in whatever form, and is told not to nag
  and not to reconstruct an attempt from conversation without marking it.
- `meta.yaml` — `human_attempt` is optional and every field may be `unknown`.
  `committed_before_prompt0` becomes `recorded: before-answer | after-answer |
  unknown`, and a `form` field records what it actually is.
- `CONVENTIONS.md` v1.3 — §6 "before the loop" is a recommendation.
- `prompt0.md` v1.3 — §3b no longer points at a committed file. Paste whatever
  you want checked, or "none".
- `New-Problem.ps1` — the seeded `human/attempt.md` says it is optional and can
  be deleted in favour of a scan; the printed next steps no longer impose a
  commit order.

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
