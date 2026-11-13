# latex_clean.py -- report-only gate latex_clean for final/final.tex (log skill, step 4).
# Lists undefined \ref targets, undefined \cite keys, overfull boxes wider than 10pt, and any
# \emph in final.tex. It changes nothing. Run: python3 -I latex_clean.py S03/final
import re, sys, pathlib
d = pathlib.Path(sys.argv[1])
log = (d/'final.log').read_text(errors='replace')
tex = (d/'final.tex').read_text(encoding='utf-8')
undef_ref = sorted(set(re.findall(r"Reference `([^']+)' on page", log)))
undef_cit = sorted(set(re.findall(r"Citation `([^']+)' on page", log)))
over = re.findall(r"Overfull \\hbox \(([\d.]+)pt too wide\) (in paragraph|in alignment|detected) at lines? (\d+)(?:--(\d+))?", log)
big = [(float(w), kind, a, b) for (w, kind, a, b) in over if float(w) > 10.0]
emph = [m.start() for m in re.finditer(r"\\emph\b", tex)]
texlines = tex.split('\n')
print(f"undefined references: {len(undef_ref)} {undef_ref}")
print(f"undefined citations : {len(undef_cit)} {undef_cit}")
print(f"\\emph in final.tex  : {len(emph)}")
print(f"overfull hboxes > 10pt: {len(big)} (of {len(over)} overfull boxes in total)")
def where(a):
    # nearest preceding sectioning command in final.tex, to say where the box is
    for k in range(int(a) - 1, -1, -1):
        m = re.match(r"\\(sub)*section\{(.{0,50})", texlines[k]) if k < len(texlines) else None
        if m: return m.group(2)
    return "?"
for w, kind, a, b in sorted(big, reverse=True):
    print(f"  {w:8.1f}pt  {kind} at final.tex lines {a}{'--'+b if b else ''}  [in: {where(a)}]")
print("GATE latex_clean:", "pass" if not (undef_ref or undef_cit or emph or big) else "fail")
