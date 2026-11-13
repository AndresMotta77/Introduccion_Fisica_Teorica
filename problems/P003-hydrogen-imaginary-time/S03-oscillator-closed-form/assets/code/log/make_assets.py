# make_assets.py -- assemble assets/code/ for P003.S03 from the solver's working folders.
# Scripts are copied byte for byte. Each output is copied to <script>.out; the original
# filename is kept in the folder README. Coverage notes for the [N] checks are copied
# verbatim from final.md (the "What it tests / would catch / would not catch" paragraphs).
import pathlib, shutil, re
P = pathlib.Path('/home/claude/p003'); R2 = P / 'r2'
A = pathlib.Path('/home/claude/log/S03/assets/code')
final = pathlib.Path('/home/claude/log/S03/final/final.md').read_text(encoding='utf-8')

def section(head):
    i = final.index(head); j = final.index("```", i)
    return final[i:j].rstrip() + "\n"

cov_final = {
    'check_algebra': section("#### S1–S6: `check_algebra.py`"),
    'check_a': section("#### A: `check_a.py`"),
    'check_c': section("#### C: `check_c.py`"),
    'check_b': section("#### B: `check_b.py`"),
    'check_p1': section("#### P1: `check_p1.py`"),
}

def note(text):
    return text.strip() + "\n"

rows = {'round-1': [], 'round-2': []}

def put(rnd, script, out=None, outname=None, cov=None, missing_script=None, missing_out=None):
    d = A / rnd; d.mkdir(parents=True, exist_ok=True)
    stem = pathlib.Path(script).stem if script else pathlib.Path(outname).stem
    if script and pathlib.Path(script).exists():
        shutil.copyfile(script, d / pathlib.Path(script).name)
    elif missing_script:
        (d / f"{stem}.py.MISSING.md").write_text(note(missing_script), encoding='utf-8')
    if out:
        shutil.copyfile(out, d / f"{stem}.out")
    elif missing_out:
        (d / f"{stem}.out").write_text(note(missing_out), encoding='utf-8')
    if cov:
        (d / f"{stem}.coverage.md").write_text(note(cov), encoding='utf-8')
    rows[rnd].append((stem, pathlib.Path(out).name if out else '(none)'))

SUP = "Superseded version, kept as a record of a run; not a verification. See final.md §4.2 for what failed and what changed."
BOOK = "Bookkeeping script; not a verification of any physics claim. See final.md §4.2."
DIAG = "Diagnostic used to locate the cause of a failed check; it compares against intermediate results of the derivation, so it is not a verification. See final.md §4.2."

# ---------------- round 1 (2026-11-12) ----------------
r = 'round-1'
put(r, str(P/'scratch.py'), None, cov="Informal series check run before S6 existed; not a verification.",
    missing_out="MISSING — the output of scratch.py was printed to the session and not saved to a file. answer-1 §4.2 reports that it gave the same coefficients as S6.")
put(r, None, None, outname='check_a_run0', missing_script="MISSING — check_a.py run 0 was edited in place and not kept. It differed from check_a_run1.py only in the line `ystar = mp.findroot(dg, (x + xp)/2)` (default solver, default verification).",
    missing_out="MISSING as a file. The run crashed at the first point with, verbatim as quoted in answer-1 and answer-2 §4.2: ValueError: Could not find root within given tolerance. (3.66903531456823378591985146146897574105138e-38 > 1.83670992315982423120115083940975887159166e-40)",
    cov=SUP)
put(r, str(P/'check_a_run1.py'), str(P/'out_a_run1_FAILED.txt'), cov=SUP)
put(r, str(P/'check_a_run2.py'), str(P/'out_a_run2_1FAIL.txt'), cov=SUP)
for s, o in (('check_algebra', 'out_algebra.txt'), ('check_a', 'out_a.txt'), ('check_c', 'out_c.txt'), ('check_b', 'out_b.txt')):
    put(r, str(P/f'{s}.py'), str(P/o), cov=cov_final[s])
put(r, None, None, outname='check_c_run0', missing_script="MISSING — edited in place in round 1 and not kept. Rebuilt in round 2 as round-2/check_c_run0.py (validated by identical output).",
    missing_out="MISSING as a file. Its C5 and C6 lines were recorded verbatim in answer-1 §4.2; the round-2 rebuild reproduces them (round-2/validate_reruns.out).", cov=SUP)
put(r, None, str(P/'out_c_run1_C5FAILED.txt'), outname='check_c_run1', missing_script="MISSING — edited in place in round 1 and not kept. Rebuilt in round 2 as round-2/check_c_run1.py (validated by identical output).", cov=SUP)
put(r, None, str(P/'out_b_run1.txt'), outname='check_b_run1', missing_script="MISSING — edited in place in round 1 and not kept. Rebuilt in round 2 as round-2/check_b_run1.py (validated by identical output).", cov=SUP)
put(r, str(P/'table.py'), str(P/'out_table.txt'), cov="Prints the table of part (b) from the closed forms; not a check.")
put(r, None, None, outname='dbg_a', missing_script="MISSING — the two round-1 diagnostics dbg_a.py and dbg_a2.py were deleted after use; their code and output are reproduced verbatim in answer-1 §4.2, and they were recreated and re-run in round 2 (round-2/dbg_a.py, dbg_a2.py).", cov=DIAG)
for f in ('diff_a_run1_vs_final.txt', 'diff_a_run2_vs_final.txt', 'diff_b.txt'):
    shutil.copyfile(P/f, A/r/f)
asm = A/r/'assembly'; asm.mkdir(exist_ok=True)
for f in ('build.py', 'template.md'):
    shutil.copyfile(P/f, asm/f)

# ---------------- round 2 (2026-11-13) ----------------
r = 'round-2'
for s, o in (('check_algebra', 'out_algebra.txt'), ('check_a', 'out_a.txt'), ('check_c', 'out_c.txt'), ('check_b', 'out_b.txt')):
    put(r, str(R2/f'{s}.py'), str(R2/o), cov=cov_final[s])
put(r, str(R2/'check_a_run1.py'), str(R2/'out_a_run1.txt'), cov=SUP)
put(r, str(R2/'check_a_run2.py'), str(R2/'out_a_run2.txt'), cov=SUP)
put(r, str(R2/'check_c_run0.py'), str(R2/'out_c_run0.txt'), cov=SUP + " Rebuilt in round 2 by reconstruct_superseded.py.")
put(r, str(R2/'check_c_run1.py'), str(R2/'out_c_run1.txt'), cov=SUP + " Rebuilt in round 2 by reconstruct_superseded.py.")
put(r, str(R2/'check_b_run1.py'), str(R2/'out_b_run1.txt'), cov=SUP + " Rebuilt in round 2 by reconstruct_superseded.py.")
put(r, str(R2/'table.py'), str(R2/'out_table.txt'), cov="Prints the table of part (b) from the closed forms; not a check.")
put(r, str(R2/'dbg_a.py'), str(R2/'out_dbg_a.txt'), cov=DIAG)
put(r, str(R2/'dbg_a2.py'), str(R2/'out_dbg_a2.txt'), cov=DIAG)
put(r, str(R2/'check_p1.py'), str(R2/'out_p1.txt'), cov=cov_final['check_p1'])
shutil.copyfile(R2/'out_p1_second.txt', A/r/'check_p1.fixed-point.out')
put(r, str(R2/'check_p1_run0.py'), str(R2/'out_p1_run0.txt'), cov=SUP)
put(r, str(R2/'reconstruct_superseded.py'), None, cov=BOOK,
    missing_out="reconstructed: check_c_run0.py, check_c_run1.py, check_b_run1.py\n\n(printed to the terminal, not saved to a file in round 2; reproduced verbatim in final.md §4.2)")
put(r, str(R2/'validate_reruns.py'), str(R2/'out_validate.txt'), cov=BOOK)
put(r, str(R2/'validate_reruns_run0.py'), str(R2/'out_validate_run0.txt'), cov=BOOK + " Superseded version (record-extraction bug).")
for f in ('diff_a_run1_vs_final.txt', 'diff_a_run2_vs_final.txt', 'diff_b.txt', 'diff_validate.txt',
          'out_c_run0_C5.txt', 'out_c_run1_C5.txt', 'out_validate_run0_tail.txt'):
    shutil.copyfile(R2/f, A/r/f)
tp = A/r/'texprobe'; tp.mkdir(exist_ok=True)
for f in ('probe_house.tex', 'probe_auditor.tex', 'run_probe.sh', 'house-pandoc.latex', 'probe_house-1.png'):
    shutil.copyfile(R2/'texprobe'/f, tp/f)
shutil.copyfile(R2/'out_probe.txt', tp/'run_probe.out')
(tp/'run_probe.coverage.md').write_text(note("Part of check P1; see ../check_p1.coverage.md."), encoding='utf-8')
asm = A/r/'assembly'; asm.mkdir(exist_ok=True)
for f in ('make_template2.py', 'build2.py', 'p1_section.md', 'response_section.md', 'template2.md'):
    shutil.copyfile(P/f, asm/f)

# ---------------- /log scripts (2026-11-13) ----------------
lg = A/'log'; lg.mkdir(exist_ok=True)
for f in ('make_final.py', 'make_final.out', 'extract_tags.py', 'extract_tags.out', 'make_assets.py'):
    shutil.copyfile(pathlib.Path('/home/claude/log')/f, lg/f)

for rnd, rr in rows.items():
    print(rnd, len(rr), "entries")
print("files:", sum(1 for _ in A.rglob('*') if _.is_file()))
