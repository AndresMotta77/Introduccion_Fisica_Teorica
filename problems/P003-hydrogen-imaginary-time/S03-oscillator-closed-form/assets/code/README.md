# assets/code — P003.S03

Every script that was run, paired with its verbatim output (`<script>.out`) and a coverage note (`<script>.coverage.md`). The coverage notes of the `[N]` checks are copied verbatim from `final/final.md` §4.3. Superseded, diagnostic and bookkeeping scripts carry a short note saying that they are not verifications. Where a script or an output was not kept, a `MISSING` file says so and points to where the record is.

`round-1/` holds the runs of 2026-11-12 (answer-1). `round-2/` holds the re-runs of 2026-11-13 (answer-2), including the superseded scripts, so that the round-1 failures are reproduced. `log/` holds the scripts /log ran to derive `final/` and `sources/provenance.md`. The `assembly/` subfolders contain the scripts and sources that assembled answer-1 and answer-2 from their templates.

Original output filenames. The scripts and the answers refer to outputs by these names:

| `.out` file | original name (round 1) | original name (round 2) |
|---|---|---|
| check_algebra.out | out_algebra.txt | out_algebra.txt |
| check_a.out | out_a.txt | out_a.txt |
| check_a_run1.out | out_a_run1_FAILED.txt | out_a_run1.txt |
| check_a_run2.out | out_a_run2_1FAIL.txt | out_a_run2.txt |
| check_c.out | out_c.txt | out_c.txt |
| check_c_run0.out | (not kept) | out_c_run0.txt |
| check_c_run1.out | out_c_run1_C5FAILED.txt | out_c_run1.txt |
| check_b.out | out_b.txt | out_b.txt |
| check_b_run1.out | out_b_run1.txt | out_b_run1.txt |
| table.out | out_table.txt | out_table.txt |
| dbg_a.out, dbg_a2.out | (not kept) | out_dbg_a.txt, out_dbg_a2.txt |
| check_p1.out, check_p1_run0.out | — | out_p1.txt, out_p1_run0.txt |
| check_p1.fixed-point.out | — | out_p1_second.txt (the confirming P1 run on the final answer-2) |
| validate_reruns.out, validate_reruns_run0.out | — | out_validate.txt, out_validate_run0.txt |
| texprobe/run_probe.out | — | out_probe.txt |

`validate_reruns.py` reads the original names, in the round-2 folder and in its parent, the round-1 folder. To re-run it, restore those names.

Execution environment: Python 3.13.18, sympy 1.14.0, mpmath 1.3.0, numpy 2.5.3, scipy 1.18.1, pandoc 3.1.3, pdfTeX 3.141592653-2.6-1.40.25 (TeX Live 2023/Debian). The auditor of round 1 executed no code.
