# validate_reruns.py -- (run 1) compare every round-2 output with the output recorded in round 1.
# Python 3.13.18. Run from the round-2 folder: python3 -I validate_reruns.py
# Normalisation: drop the shell timing lines (real/user/sys) and blank lines, and replace the
# absolute script path in Python warning lines by the bare file name. Nothing else is touched.
# The round-1 records of check_c run 0 (C5 block) and of the two diagnostics exist only inside
# answer-1's source (template.md); they are extracted from there.
import re, pathlib
R1 = pathlib.Path('..')

def norm(s):
    out = []
    for l in s.splitlines():
        if re.match(r'^(real|user|sys)\s', l) or not l.strip():
            continue
        l = re.sub(r'^/\S*/(check_b(_run1)?\.py)', 'check_b.py', l)
        out.append(l)
    return out

def block_after(text, marker, skip=0):
    """first fenced block after marker; skip=1 when the marker sits inside a code block,
    so that block's closing fence is passed first (run 0 lacked this and returned '')"""
    i = text.index(marker)
    for _ in range(skip):
        i = text.index("\n```\n", i) + 5
    j = text.index("```\n", i) + 4
    k = text.index("```", j)
    return text[j:k]

tmpl = (R1/'template.md').read_text()
records = {
    'c_run0_C5': block_after(tmpl, "The run-0 C5 lines, verbatim"),
    'dbg_a':     block_after(tmpl, "# dbg_a.py\n", skip=1),
    'dbg_a2':    block_after(tmpl, "# dbg_a2.py\n", skip=1),
}
c0 = pathlib.Path('out_c_run0.txt').read_text()
c1 = pathlib.Path('out_c_run1.txt').read_text()
pathlib.Path('out_c_run0_C5.txt').write_text(c0[c0.index("C5 from grid"):])
pathlib.Path('out_c_run1_C5.txt').write_text(c1[c1.index("C5 from grid"):])

pairs = [
    ('out_algebra.txt',   (R1/'out_algebra.txt').read_text()),
    ('out_a.txt',         (R1/'out_a.txt').read_text()),
    ('out_a_run1.txt',    (R1/'out_a_run1_FAILED.txt').read_text()),
    ('out_a_run2.txt',    (R1/'out_a_run2_1FAIL.txt').read_text()),
    ('out_c.txt',         (R1/'out_c.txt').read_text()),
    ('out_c_run1.txt',    (R1/'out_c_run1_C5FAILED.txt').read_text()),
    ('out_c_run0_C5.txt', records['c_run0_C5']),
    ('out_b.txt',         (R1/'out_b.txt').read_text()),
    ('out_b_run1.txt',    (R1/'out_b_run1.txt').read_text()),
    ('out_table.txt',     (R1/'out_table.txt').read_text()),
    ('out_dbg_a.txt',     records['dbg_a']),
    ('out_dbg_a2.txt',    records['dbg_a2']),
]
nd = 0
for f, old in pairs:
    new = norm(pathlib.Path(f).read_text()); old = norm(old)
    same = (new == old) and len(old) > 0 and len(new) > 0   # an empty side never counts as a match
    nd += (not same)
    print(f"{f:20s} lines={len(new):4d}  identical to round-1 record: {same}")
    if not same:
        for a, b in zip(old, new):
            if a != b:
                print("   round 1:", a); print("   round 2:", b)
c_run0_C1to4 = c0[:c0.index("C5 from grid")]
fin = pathlib.Path('out_c.txt').read_text()
same = c_run0_C1to4 == fin[:fin.index("C5 from grid")]
nd += (not same)
print(f"check_c run 0, sections C1-C4: identical to the final run's C1-C4: {same}")
print("NUMBER OF MISMATCHES:", nd)
