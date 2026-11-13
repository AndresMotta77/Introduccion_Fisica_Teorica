# check_p1_run0.py -- (superseded: buggy regex) presentation check for F1.1 (round 2).
# Python 3.13.18, pandoc 3.1.3, pdfTeX 3.141592653-2.6-1.40.25 (TeX Live 2023/Debian), latexmk.
# Run: python3 -I check_p1.py answer-1.md answer-2.md
#
# P1a  static scan: every \mathbb whose argument is not a single uppercase letter A-Z, outside
#      fenced code blocks and inline code spans. amssymb's \mathbb (font msbm) has
#      double-struck glyphs only for A-Z; any other argument silently prints a different
#      symbol (probe_house.tex shows \mathbb 1 printing a negated-turnstile glyph).
#      Failure: any hit.
# P1b  convert the markdown with pandoc using texprobe/house-pandoc.latex, whose math preamble
#      is copied from the house template (amsmath, amssymb, amsthm, mathtools, physics,
#      siunitx), compile with latexmk -pdf, and report every TeX error ("!" lines) and every
#      "Missing character" warning. Failure: any error, any missing character, or no PDF.
import re, subprocess, sys, pathlib

def strip_code(text):
    text = re.sub(r'^```.*?^```', '', text, flags=re.S | re.M)   # fenced blocks
    return re.sub(r'`[^`\n]*`', '', text)                          # inline code spans

pat = re.compile(r'\\mathbb\s*(?:\{\s*)?(?![A-Z][\s}\\$^_,.)])')
nfail = 0
for md in sys.argv[1:]:
    src = pathlib.Path(md).read_text()
    body = strip_code(src)
    hits = []
    for ln, line in enumerate(body.splitlines(), 1):
        for m in pat.finditer(line):
            hits.append((ln, line[max(0, m.start() - 15):m.end() + 6]))
    print(f"P1a {md}: {len(hits)} \\mathbb use(s) with a non-A-Z argument (outside code)")
    for ln, ctx in hits:
        print(f"      line {ln} (code-stripped text): ...{ctx}...")
    stem = pathlib.Path(md).stem
    tex = f"p1_{stem}.tex"
    subprocess.run(["pandoc", md, "-f", "markdown", "-t", "latex", "--listings",
                    "--template", "texprobe/house-pandoc.latex", "-o", tex], check=True)
    for old in pathlib.Path('.').glob(f"p1_{stem}.*"):     # force a fresh build every run
        if old.suffix != ".tex":
            old.unlink()
    r = subprocess.run(["latexmk", "-pdf", "-g", "-interaction=nonstopmode", tex],
                       capture_output=True, text=True)
    log = pathlib.Path(f"p1_{stem}.log").read_text(errors="replace")
    errs = [l for l in log.splitlines() if l.startswith("!")]
    miss = [l for l in log.splitlines() if "Missing character" in l]
    pdf = pathlib.Path(f"p1_{stem}.pdf")
    pages = re.findall(r'Output written on .*?\((\d+) pages', log)
    print(f"P1b {md}: TeX errors = {len(errs)}, missing characters = {len(miss)}, "
          f"PDF = {'yes' if pdf.exists() else 'no'}, pages = {pages[-1] if pages else '?'}")
    for l in (errs + miss)[:10]:
        print("      ", l)
    bad = (len(errs) > 0) or (len(miss) > 0) or (not pdf.exists())
    if stem != "answer-1":          # answer-1 is the pre-fix document, run for comparison only
        nfail += bad or (len(hits) > 0)
print("TOTAL FAILURES (answer-2 only):", nfail)
