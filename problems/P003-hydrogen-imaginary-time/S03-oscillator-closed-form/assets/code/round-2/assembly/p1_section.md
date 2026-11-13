#### P1: `check_p1.py` — the math under the house LaTeX template `[N]` (new in round 2)

What it tests.

- P1a scans the markdown for every `\mathbb` whose argument is not a single uppercase letter, with fenced code blocks and inline code spans removed first. `amsfonts.sty` declares `\mathbb` as the alphabet of the AMSb (msbm) symbol font, and that font has double-struck glyphs only in the uppercase-letter slots. Any other argument silently prints whatever symbol occupies that slot. For the digit 1 that is slot "31, which `amssymb.sty` assigns to $\nVdash$.
- P1b converts the markdown with pandoc, using `texprobe/house-pandoc.latex`, whose preamble is copied from the house template. It compiles the result with `latexmk -pdf -g` and reports every TeX error and every missing-character warning.

P1 runs on answer-1 (the pre-fix document, for comparison only) and on answer-2. Failure, for answer-2 only: any P1a hit, any TeX error, any missing character, or no PDF.

Probe. Before writing P1 I compiled two one-page probes. One has the house math preamble. The other has only amsmath, physics and siunitx, the package set named in F1.1.
- Under the house preamble, `\mathbb 1` and `\mathbb{1}` print $\nVdash$ with no error and no warning. `\mathbf 1`, `\mathbb{I}`, `\mathbb R`, `\mathbb E`, `\square`, `\lesssim` and `\gtrsim` print correctly. I inspected the rendered page visually; it is `probe_house-1.png` in the bundle.
- Under the F1.1 set there are eight `Undefined control sequence` errors, one for each `\mathbb` and each amssymb symbol.

What it would catch:
- any `\mathbb` with a non-A–Z argument in prose or equations, anywhere outside code;
- any construct that fails to compile under the house preamble, including clashes with `physics`;
- any glyph missing from the fonts.

What it would not catch:
- a construct that compiles but renders wrongly by some other route (P1b sees only errors and missing characters, and P1a looks only for `\mathbb`);
- layout problems: the pandoc build has overfull lines, e.g. eq. (6), and these are raised as SR2.1 in §10, not tested;
- rendering in a markdown viewer (MathJax or KaTeX), where `\mathbf 1` is standard but was not tested;
- the `/log` conversion itself, for which pandoc is a stand-in, not the real thing.

Run log for P1 and the probe.
- `check_p1.py` run 0 used the pattern `\\mathbb\s*(?:\{\s*)?(?![A-Z][\s}\\$^_,.)])`. Because `\s*` can backtrack to zero width, the lookahead then saw a space, so `\mathbb R` and `\mathbb E` were flagged: 15 hits on answer-1, 7 of them false. I replaced the pattern with a lookahead anchored directly after `\mathbb`. That change makes the check pass for `\mathbb R` and `\mathbb E`, which the probe shows render correctly, and it leaves all 8 true hits flagged.
- Before the round-2 runs shown here, I also added `-g` and deletion of old build files. A first execution of the run-0 script had reused a cached PDF, because latexmk judged it up to date.
- `run_probe.sh` first listed only four of the seven error locations, because overlapping `grep -A2` matches dropped some. The counts were right; the listing was fixed.
- Probe line (g), `\mathbb E`, was added after those first runs, so that the probe covers every amssymb construct the answer uses. The probe was then re-run; the output shown is from that re-run.

The superseded run-0 script differs from the final one only in its first comment line and the pattern. Both are re-run below.

```latex
{{CODE:r2/texprobe/probe_house.tex}}
```

`probe_auditor.tex` is the same file with the line `\usepackage{amsmath,amssymb,amsthm,mathtools}` replaced by `\usepackage{amsmath}` (and the first comment changed).

```bash
{{CODE:r2/texprobe/run_probe.sh}}
```

Output of `run_probe.sh` (verbatim):

{{OUT:r2/out_probe.txt}}

```latex
{{CODE:r2/texprobe/house-pandoc.latex}}
```

```python
{{CODE:r2/check_p1.py}}
```

Output of run 0, `check_p1_run0.py answer-1.md` (verbatim):

{{OUT:r2/out_p1_run0.txt}}

Output of run 1, `check_p1.py answer-1.md answer-2.md` (verbatim; run without `time`). This is the run on the final answer-2 file. Because answer-2 contains this very output, I repeated build and P1 until P1 reproduced the embedded output byte for byte. Only the page count moved between iterations:

{{OUT:r2/out_p1.txt}}
