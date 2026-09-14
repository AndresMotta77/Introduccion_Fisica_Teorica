---
name: log
description: Close out a Vibe Physics problem — collect prompt0, every answer, every corrector prompt and audit report, build final.md/.tex/.pdf, write the provenance and source ledgers with per-run model and effort metadata, run the release gates, and commit the problem folder to the repository. Use when the user says /log, "log this problem", "close out P###", or asks to write up and commit a finished derivation.
---

# /log — close out a problem

Turns a solving session into a committed, auditable problem folder. This runs
once, at the end, after the loop has converged or been escalated.

Usage: `/log P007` or `/log P007 --title "Hawking temperature via TFD"`

## What this skill must not do

It must not invent. Three things in particular are unknowable from inside the
conversation, and each has a rule:

1. **Effort level.** You can read your own configured model id, but not the
   effort or thinking level the user selected, and not whether the serving model
   changed mid-session. Never write an effort value you were not told. Ask, and
   record `source: user-reported`. If the user declines to say, write `unknown`.
2. **Audit reports.** The auditor ran in another model's context. You only have
   what was pasted back to you. If a round's audit report is not in the
   conversation, do not summarize it from the corrector prompt and do not
   reconstruct it — write the file with a `MISSING` banner naming what is
   absent, and tell the user which rounds are incomplete.
3. **Citation verification status.** Carry the status the answer recorded. Do not
   promote a `{ver: no}` to `{ver: tool}` because the citation looks right.
4. **The compliance probe outcome.** Record what happened. Do not soften a
   `caved` into "partially accepted", and do not take the post-probe answer as
   the final result.

A fifth, related rule: do not record a computational check as a verification.
`/log` writes what the code did and what the auditor said about it. Whether the
result is verified is a conclusion, and it belongs to the verdict, not to the
presence of a script that printed PASS.

## Procedure

### Step 1 — Collect and confirm

Scan the conversation and build an inventory before writing anything. Report it
to the user as a table and ask them to confirm or correct it:

- the human attempt if there is one, in whatever form — a file, a scan, a photo,
  loose notes — and when it was recorded relative to the first answer. This is a
  record, not a requirement: "none" and "unknown" are both fine, and no gate
  turns on it. Do not nag the user for one, and do not write a reconstruction of
  an attempt they described to you in conversation without marking it as such.
- prompt0, and whether it was edited mid-session
- every answer, numbered in order
- every corrector prompt
- every audit report actually present in context, and which rounds are missing
- the blind-solve answer, if stage 0 was run
- the exploration output, if it exists
- the final verdict and round count
- the compliance probe and its outcome, if run
- any external ground truth, and when it arrived relative to the loop
- any code and figures produced

### Step 1a — Split the auditor's reply

The user pastes the auditor's whole reply into the conversation, both parts
together. Split it and file each half verbatim, before doing anything else with
it:

- From the "Part A" heading to the "Part B" heading →
  `audits/audit-report-k.md`. That includes the run header, the pass table,
  every finding with its evidence, the auditor's own code snippets, the frozen
  list and the confidence statement.
- From the "Part B" heading to the end → `prompts/corrector-prompt-k.md`.

Verbatim means verbatim. Do not merge the finding blocks that appear in both
halves, do not renumber them, do not drop a code snippet for being long, and do
not correct the auditor's arithmetic. A wrong number in an audit report is an
accurate record of what the auditor said, and it is often the most useful thing
in the file.

If the reply did not split into two parts, save the whole thing as
`audit-report-k.md`, note the format deviation in one line at the top, and
record that `corrector-prompt-k.md` was assembled by the user rather than
produced by the auditor.

From audit-prompt v1.3 onward Part A opens with a run header giving the
auditor's model, effort, tools and whether it executed code. Take the metadata
from there.

### Step 1b — Metadata you cannot know

Ask for the rest in one message, with your best guess pre-filled so the user
only has to correct it:

- solver model label and effort, per round if it changed
- auditor model label and effort, per round. From audit-prompt v1.3 the report
  carries a run header stating these; use it, record `model_source` and
  `effort_source` as `self-reported`, and say you took them from the report so
  the user can correct it. A model's self-report of its own version is better
  than nothing and still not authoritative.
- exploration model label and effort
- tools available to each

### Step 2 — Release gates

Run these against the final answer and report each as pass/fail. Do not silently
fix a failure; report it, offer to fix it, and if the user says to proceed
anyway, stamp the failure into `meta.yaml` and into a banner at the top of
`final.md`.

| Gate | Condition |
|---|---|
| `locators_complete` | Every `[S]` and `[V]` claim has a locator at section/equation/page granularity. |
| `no_unflagged_recall` | Every `[R]` and every load-bearing `{ver: no}` appears in the Risk register. |
| `sources_split` | Sources section exists and separates Used from Consulted. |
| `general_refs_resolved` | No citation of the form "see Author" or "Author, ch. N" without a specific locator. |
| `convergence_check` | The Convergence check section exists and names specific steps or explicitly states there are none and why. |
| `code_output_present` | Verification code is included with its verbatim output, for every run made and not only the agreeing ones, and the output matches the claims made about it. |
| `code_coverage_notes` | Every `[N]` check states what it would and would not have caught. |
| `code_not_circular` | No check draws its inputs from intermediate results of the derivation it is testing, and every assumption inside the code (positivity, reality, branch, principal value, sign convention) also appears as an `[A]` in the text. |
| `code_audited` | At least one audit report contains a pass 6a review of the solver's verification code. A derivation whose code was never read by the auditor has an unaudited verification section. |
| `audit_trail_complete` | An audit report exists for every round. |
| `findings_closed` | Every finding id has a disposition: accepted, rejected with rebuttal, or explicitly deferred. |
| `stopping_rule` | The loop ended per CONVENTIONS.md §6, or the deviation is recorded. |
| `latex_clean` | Report-only. The compile log shows no undefined `\ref` targets, no undefined `\cite` keys, and no overfull box beyond 10pt; `final.tex` contains no `\emph`. Report the list and stop — never edit the final document to clear this gate. |
| `compliance_probe_run` | The probe was run on a claim known to be right, and its outcome recorded. A `caved` outcome does not fail this gate — not running the probe does. |
| `ground_truth_timing` | If external ground truth exists, `meta.yaml` records when it arrived. Ground truth that arrived mid-loop is not also evidence that the loop worked. |

### Step 3 — Write the folder

Layout in `reference/layout.md`. Create `problems/P###-slug/` and write every
file. Filenames are fixed; do not improvise variants.

Derive `final.md` from the last answer, not from a fresh summary: strip the
Prior-knowledge declaration and the Response-to-audit sections into
`sources/independence.md` and `audits/`, keep the derivation, verification,
result, risk register and sources intact. The final document is the last answer
cleaned up, never a rewrite — a rewrite reintroduces the errors the loop removed.

Build `sources/provenance.md` as a table with one row per tagged claim:
equation or section, tag, source, locator, verification status, load-bearing
yes/no. This is the file that answers "did the model derive this or recall it",
and it is the reason the whole workflow exists, so build it from the tags in the
text rather than from the Sources section.

Build `sources/sources.bib` in BibTeX from the Used entries, with the locator in
a `note` field since BibTeX has no field for it.

### Step 4 — Build the PDF

Use `reference/final-tex-template.tex`. Convert `final.md` to LaTeX preserving
equation numbering and the tag annotations (tags go in the margin or as a
superscript, defined once in the preamble — do not drop them, they are the
audit trail).

House style, non-negotiable: no `\emph`, no bolded lead-ins, prose paragraphs
rather than bullet fragments, and every intermediate algebraic step kept.

Compile with `latexmk -pdf` (fall back to `tectonic`). If compilation fails,
fix the LaTeX and retry up to three times, then report the error and ship
`final.md` and `final.tex` without the PDF rather than mangling the content to
make it compile.

Keep the compile log. Once it builds, parse the log for the `latex_clean` gate:
undefined references, undefined citations, and overfull boxes past 10pt. Grep
`final.tex` for `\emph` while you are there. A document can compile cleanly and
still ship `??` where a cross-reference should be, which is why this is checked
after a successful build rather than only on failure.

Report what you find as a list and stop. Step 3 forbids rewriting the final
document, and that rule does not bend for cosmetics: the final is the last
answer cleaned up, and a silent fix is the beginning of a final document that
nobody can trace to an answer. The user fixes or waves through; either way the
gate result goes into `meta.yaml`. Typos in the prose belong to the solver and
are raised as audit pass 10 findings in a round, not patched here.

### Step 5 — Metadata and index

Write `meta.yaml` per `reference/meta-schema.md`. Append a row to the repository
`index.md` and to `index.yaml`: id, title, date closed, verdict, rounds, gate
failures, one-line result, open branches from the exploration step.

### Step 6 — Commit

```
git add problems/P###-slug index.md index.yaml
git commit
git push
```

Commit message:

```
P###: <title>

verdict: <ACCEPT|...>  rounds: <n>  gates: <pass|N failed: names>
solver: <model> (<effort>)   auditor: <model> (<effort>)
result: <one line>
```

Then report to the user: the folder path, the gate results, anything logged as
MISSING or unknown, and the exploration branches now queued.

## Mapping to the original file list

The workflow diagram named `prompt.md`, `answer#.md`, `corrector-prompt.md`,
`finalresult.md/.tex/.pdf`. Those are all here under the names in
`reference/layout.md`. Three files were added because they carry information the
original list had nowhere to put: `sources/provenance.md`, `meta.yaml`, and
`audits/audit-report-k.md`. Without the first, the bibliography requirement is
not actually enforceable; without the second, the model and effort requirement
has no home; without the third, the audit half of the loop leaves no trace in
the repository at all.
