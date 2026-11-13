# make_template2.py -- derive template2.md (answer-2) from template.md (answer-1).
# Every edit is an exact replacement asserted to occur the stated number of times.
import re, pathlib
t = pathlib.Path('template.md').read_text()

def rep(old, new, count=1):
    global t
    n = t.count(old)
    assert n == count, (n, old[:80])
    t = t.replace(old, new)

def cut_block(start_marker, end_marker, new):
    """replace text from start_marker (inclusive) up to end_marker (exclusive)"""
    global t
    i = t.index(start_marker); j = t.index(end_marker, i)
    assert t.count(start_marker) == 1
    t = t[:i] + new + t[j:]

# ---------- identity matrix ----------
n_mbb = len(re.findall(r'\\mathbb\s*1', t))
assert n_mbb == 8, n_mbb
t = re.sub(r'\\mathbb\s*1', r'\\mathbf 1', t)
# ---------- header ----------
rep("""# P003.S03 — answer-1

Harmonic oscillator under a bridge-averaged slice weight: closed form, partition functions, levels.

Solver: Claude Opus 5.5 (`claude-opus-5-5`), tools: code, web. Conventions v1.5. Date of run: 2026-11-12.""",
"""# P003.S03 — answer-2

Harmonic oscillator under a bridge-averaged slice weight: closed form, partition functions, levels.

Solver: Claude Opus 5.5 (`claude-opus-5-5`), tools: code, web. Conventions v1.5. Round 2, 2026-11-13 (answer-1: 2026-11-12).

Round 2 revises answer-1 in response to audit 1 (verdict ACCEPT-WITH-FIXES, one MINOR finding, F1.1). Section 10, Response to audit 1, gives the outcome for F1.1 and lists every change. In short: the identity matrix, written `\\mathbb 1` in answer-1, prints as a wrong glyph under the house LaTeX template, and is now written $\\mathbf 1$; part of the finding's evidence is contested in §10. The mathematics and the numbers are unchanged.

All verification code was re-run on 2026-11-13, and every output in §4 comes from that re-run. The re-run includes the superseded scripts that failed in round 1, so those failures are reproduced, not quoted. A new check, P1, tests the presentation fix.""")

rep("`[D]` With the cyclic shift $(Px)_n = x_{n+1}$ one has",
    "`[D]` With the cyclic shift $(Px)_n = x_{n+1}$ and the $m\\times m$ identity matrix $\\mathbf 1$, one has")
rep("| $P$ | $m\\times m$ cyclic shift, $(Px)_n = x_{n+1}$, indices mod $m$ |",
    "| $P$ | $m\\times m$ cyclic shift, $(Px)_n = x_{n+1}$, indices mod $m$ |\n| $\\mathbf 1$ | $m\\times m$ identity matrix |")

# ---------- 4.2 run log ----------
rep("""### 4.2 Run log (all runs, including failures)

| Script | Runs | Outcome |""",
"""### 4.2 Run log (all runs, including failures)

Round 2. Every script was re-run on 2026-11-13, in a fresh folder and from a clean interpreter. That includes the superseded round-1 versions, so the failures described below are reproduced rather than quoted. Two superseded versions of `check_c.py` and one of `check_b.py` had been edited in place in round 1 and not kept. I rebuilt them by reverse-applying the exact round-1 edits to the final scripts (`reconstruct_superseded.py`, below).

The rebuilds are validated by their outputs. `validate_reruns.py` finds every round-2 output identical to the round-1 record, after dropping the shell timing lines and the absolute path in two warning lines. That would not hold if a rebuild differed in any line that affects output.

The code of all final checks is unchanged from round 1. Some outputs below end with shell timing lines (`real`, `user`, `sys`), because those scripts were run as `(time python3 -I script.py) > out.txt 2>&1`; the others were run without `time`.

| Script (round 2) | Outcome |
|---|---|
| `check_algebra.py` | all differences 0; identical to round 1 |
| `check_a.py` (final) | 0 FAIL; identical to round 1 |
| `check_a_run1.py`, `check_a_run2.py` (superseded, kept since round 1) | 5 FAIL and 1 FAIL, reproducing round 1 |
| `dbg_a.py`, `dbg_a2.py` (round-1 diagnostics; only the name of the file they read changed) | identical to round 1 |
| `check_c.py` (final) | 0 FAIL; identical to round 1 |
| `check_c_run0.py`, `check_c_run1.py` (rebuilt) | 0 FAIL (no C5 criterion yet) and 2 FAIL, reproducing round 1 |
| `check_b.py` (final), `check_b_run1.py` (rebuilt) | 0 FAIL; the rebuild reproduces the two round-1 warnings |
| `table.py` | identical to round 1 |
| `check_p1.py` (new, presentation, §4.3) | run 0: false positives from a regex bug; run 1: answer-1 has 8 hits, answer-2 has 0 hits and compiles with 0 errors |
| `reconstruct_superseded.py`, `validate_reruns.py` (new, bookkeeping) | validator run 0, made while `check_a_run2.py` was still running: 3 mismatches. One was the unfinished output. Two were the diagnostic outputs, compared against empty records because the extraction skipped to the wrong fence; the comparison could only fail, never pass vacuously. Fixed the extraction, and an empty side now never counts as a match. Run 1: 0 mismatches |

```python
{{CODE:r2/reconstruct_superseded.py}}
```

Its output, verbatim: `reconstructed: check_c_run0.py, check_c_run1.py, check_b_run1.py`.

```python
{{CODE:r2/validate_reruns.py}}
```

Output of `validate_reruns.py` (verbatim):

{{OUT:r2/out_validate.txt}}

The superseded validator (`validate_reruns_run0.py`) differs from the final one as follows (`diff validate_reruns_run0.py validate_reruns.py`):

{{OUT:r2/diff_validate.txt}}

Re-run after all outputs existed, it reports only the two spurious diagnostic mismatches. Its first execution had also counted the then-unfinished `out_a_run2.txt`. Last lines, verbatim:

{{OUT:r2/out_validate_run0_tail.txt}}

Round-1 history. The rest of this subsection is the round-1 account. It is unchanged, except that each output shown is now the round-2 re-run of the corresponding script.

| Script | Runs | Outcome |""")

rep("{{OUT:out_a_run1_FAILED.txt}}", "{{OUT:r2/out_a_run1.txt}}")
cut_block("A diagnostic (two short scripts, deleted afterwards;",
          "These diagnostics compare against $\\bar y$",
"""A diagnostic (two short scripts) showed three things. They were deleted after round 1. For round 2 they were re-created verbatim from the round-1 record, except that the file they read is now named `check_a_run1.py`, and re-run.

```python
{{CODE:r2/dbg_a.py}}
```

{{OUT:r2/out_dbg_a.txt}}

```python
{{CODE:r2/dbg_a2.py}}
```

{{OUT:r2/out_dbg_a2.txt}}

""")
rep("{{OUT:out_a_run2_1FAIL.txt}}", "{{OUT:r2/out_a_run2.txt}}")
rep("{{OUT:diff_a_run1_vs_final.txt}}", "{{OUT:r2/diff_a_run1_vs_final.txt}}")
rep("{{OUT:diff_a_run2_vs_final.txt}}", "{{OUT:r2/diff_a_run2_vs_final.txt}}")
cut_block("```\nC5 from grid eigenvalues: R_n = [E_n-(n+1/2) - (2n+1)tau^2/48]/tau^3 (bridge, predicted -1/144 + 3(2n+1)tau/1280 - tau^2/1296 + O(tau^3));",
          "`check_c.py`, run 1. C5 failed at",
          "{{OUT:r2/out_c_run0_C5.txt}}\n\n")
rep("The run-0 C5 lines, verbatim (C1–C4 and C6 printed the same lines as in the final run, since the code there was unchanged and deterministic):",
    "The run-0 C5 and C6 lines, verbatim from the round-2 re-run of the rebuilt `check_c_run0.py`. Its C1–C4 lines are identical to the final run's, as `validate_reruns.py` confirms:")
cut_block("```\nC5 from grid eigenvalues: R_n = [E_n-(n+1/2) - (2n+1)tau^2/48]/tau^3 (bridge, predicted -1/144 + 3(2n+1)tau/1280 - tau^2/1296 + 103(2n+1)tau^3/387072 + O(tau^4));",
          "`check_b.py`, run 1.",
          "{{OUT:r2/out_c_run1_C5.txt}}\n\n")
rep("The run-1 script was edited in place and not kept separately.",
    "The run-1 script was edited in place in round 1; it was rebuilt for round 2 as `check_c_run1.py`.")
rep("The run-1 C5 lines, verbatim (the rest of the run-1 output is identical to run 2):",
    "The run-1 C5 and C6 lines, verbatim from the round-2 re-run of `check_c_run1.py`. Its full output is identical to the round-1 record, as `validate_reruns.py` confirms:")
rep("Run 2 sets that row to $e_i$; all printed numbers are identical between the runs. Verbatim `diff out_b_run1.txt out_b.txt`:\n\n{{OUT:diff_b.txt}}",
    "Run 2 sets that row to $e_i$; all printed numbers are identical between the runs. Verbatim `diff out_b_run1.txt out_b.txt` for the round-2 re-runs of `check_b_run1.py` (rebuilt) and `check_b.py`; the final script was run under `time`, so its timing lines also appear:\n\n{{OUT:r2/diff_b.txt}}")

# ---------- 4.3 outputs and code from round-2 folder ----------
for f in ["check_algebra.py", "check_a.py", "check_c.py", "check_b.py", "table.py"]:
    rep("{{CODE:%s}}" % f, "{{CODE:r2/%s}}" % f)
rep("Output (verbatim):\n\n{{OUT:out_algebra.txt}}", "Output (verbatim, round-2 re-run):\n\n{{OUT:r2/out_algebra.txt}}")
rep("Output (verbatim, run 3):\n\n{{OUT:out_a.txt}}", "Output (verbatim, round-2 re-run of the final script):\n\n{{OUT:r2/out_a.txt}}")
rep("Output (verbatim, run 2):\n\n{{OUT:out_c.txt}}", "Output (verbatim, round-2 re-run of the final script):\n\n{{OUT:r2/out_c.txt}}")
rep("Output (verbatim, run 2):\n\n{{OUT:out_b.txt}}", "Output (verbatim, round-2 re-run of the final script):\n\n{{OUT:r2/out_b.txt}}")
rep("{{RAW:out_table.txt}}", "{{RAW:r2/out_table.txt}}")
rep("Table (closed forms (20), (21), evaluated with 30-digit arithmetic by `table.py`; printed verbatim):",
    "Table (closed forms (20), (21), evaluated with 30-digit arithmetic by `table.py`; printed verbatim from the round-2 re-run):")

p1 = pathlib.Path('p1_section.md').read_text()
rep("""#### Table script: `table.py`

```python
{{CODE:r2/table.py}}
```
""", """#### Table script: `table.py`

```python
{{CODE:r2/table.py}}
```

""" + p1)

# ---------- 7 risk register ----------
rep("| Check revisions (`check_a` ×3, `check_c` ×1) | process | checks changed after failures, disclosed in §4.2 | an auditor should verify that each change is a correction and not a weakening |",
"""| Check revisions (`check_a` ×3, `check_c` ×1 in round 1; `check_p1`, `validate_reruns.py` and `run_probe.sh` ×1 each in round 2) | process | checks changed after failures, disclosed in §4.2 and §4.3 | an auditor should verify that each change is a correction and not a weakening |
| Rebuilt round-1 scripts (`check_c_run0.py`, `check_c_run1.py`, `check_b_run1.py`) | process | rebuilt in round 2 by reverse-applying the round-1 edits | a wrong rebuild would misreport the round-1 history; `validate_reruns.py` shows their outputs identical to the round-1 records |
| Rendering of the math in the `/log` PDF | presentation | checked by P1: no `\\mathbb` with a non-A–Z argument; compiles under the house preamble with 0 errors and 0 missing characters | not checked: MathJax/KaTeX viewers, other wrong renderings that compile silently, layout (SR2.1); no effect on content |""")

# ---------- 8 sources ----------
rep("### Consulted\n", """Used in round 2. These are load-bearing only for §10 (Response to audit 1). No physics result depends on them.

- House LaTeX template of the `/log` step: log skill, file `reference/final-tex-template.tex` as embedded in the skill's SKILL.md (synced copy on this machine, lines 434–447), preamble `\\usepackage{amsmath,amssymb,amsthm,mathtools}`, `\\usepackage{physics}`, `\\usepackage{siunitx}`. {ver: tool}. Retrieval note: file read on disk on 2026-11-13; the three lines are as quoted.
- `amsmath.sty` v2.17o (2023/05/13), TeX Live 2023/Debian, lines 127–129: `\\RequirePackage{amstext}`, `{amsbsy}`, `{amsopn}`; no amssymb. {ver: tool}. Retrieval note: grep of the installed file.
- `physics.sty`, TeX Live 2023/Debian, lines 15–16: `\\RequirePackage{xparse}`, `\\RequirePackage{amsmath}`; no amssymb. {ver: tool}. Retrieval note: grep of the installed file.
- `amsfonts.sty` v3.01 (2013/01/14), line 108: `\\DeclareSymbolFontAlphabet{\\mathbb}{AMSb}`; `amssymb.sty` v3.01, line 34: `\\RequirePackage{amsfonts}`, and line 220: `\\DeclareMathSymbol{\\nVdash}{\\mathrel}{AMSb}{"31}`. {ver: tool}. Retrieval note: grep of the installed files.

### Consulted
""")

# ---------- 10 response ----------
resp = pathlib.Path('response_section.md').read_text()
t = t.rstrip('\n') + "\n\n---\n\n" + resp
pathlib.Path('template2.md').write_text(t)
print("template2.md written;", n_mbb, "identity-matrix occurrences replaced")
