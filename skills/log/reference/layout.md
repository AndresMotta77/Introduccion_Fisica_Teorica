# Problem folder layout

```
problems/P007-hawking-temperature-tfd/
├── README.md                     # the bitácora: the narrative account, written by you
├── meta.yaml                     # see meta-schema.md
├── human/
│   └── attempt.md                # written and committed BEFORE prompt0
├── prompts/
│   ├── prompt0.md                # exactly as sent, including the filled §0
│   ├── audit-prompt-1.md         # the audit prompt as sent, with its INPUTS block
│   ├── audit-prompt-2.md
│   ├── corrector-prompt-1.md     # Part B of audit 1, as pasted to the solver
│   ├── corrector-prompt-2.md
│   └── exploration-prompt.md
├── answers/
│   ├── blind-solve.md            # stage 0, if run
│   ├── answer-1.md
│   ├── answer-2.md
│   └── answer-3.md
├── audits/
│   ├── audit-report-1.md         # Part A, verbatim auditor output
│   ├── audit-report-2.md
│   ├── compliance-probe.md       # the probe as sent, the reply, the outcome
│   └── findings.yaml             # every finding id, severity, disposition, round closed
├── final/
│   ├── final.md
│   ├── final.tex
│   └── final.pdf
├── sources/
│   ├── sources.bib
│   ├── provenance.md             # per-claim tag ledger
│   └── independence.md           # prior-knowledge declaration + convergence check + perturbation test
├── explore/
│   └── exploration-1.md
└── assets/
    ├── code/                     # every script that was run, with its output captured
    └── figures/
```

Rules:

- Nothing is edited after it is written except `README.md` and `meta.yaml`.
  `answer-2.md` is what the model said in round 2, mistakes included. The
  mistakes are the data.
- A missing file gets written anyway, with a single line saying what is missing
  and why. An absent file is ambiguous; a `MISSING` file is a record.
- `assets/code/` holds the scripts as executed, each paired with a `.out` file
  containing the verbatim output, and a `.coverage.md` saying what that check
  would and would not have caught. Not a cleaned-up version, and not only the
  runs that agreed. The coverage note is the part that stops a passing script
  from being read later as a proof.
- `independence.md` is the file to read first when revisiting a problem months
  later. It is the honest account of what the model knew going in.
- `human/attempt.md` is never edited after prompt0 is sent. Its git commit is
  the evidence for the `human_attempt_first` gate, so commit it on its own
  rather than bundling it with the first prompt.
- `README.md` is yours. Everything else in the folder is a record of what the
  models did; the README is the narrative that says what you concluded from it.
