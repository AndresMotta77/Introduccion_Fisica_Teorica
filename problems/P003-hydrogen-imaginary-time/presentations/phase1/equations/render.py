"""Render every entry of equations.py to png/<id>.png.

Each equation is typeset by pdflatex in a standalone document (Latin Modern, ink #14213D)
and converted to a transparent PNG at 480 dpi with pdftocairo. The deck shows each image
at half its pixel size, about twice the resolution of the display.

Needs pdflatex (with the lmodern, amsmath, amssymb and xcolor packages), pdftocairo
(poppler) and Pillow. Run from this folder:  python render.py
Writes png/ and sizes.json (pixel size and display size of each image).
"""
import json
import pathlib
import shutil
import subprocess
import tempfile

from PIL import Image

from equations import EQ

DPI = 480
TEMPLATE = r"""\documentclass[border=3pt]{standalone}
\usepackage[T1]{fontenc}\usepackage{lmodern}\usepackage{amsmath,amssymb,xcolor}
\definecolor{ink}{HTML}{14213D}
\begin{document}\color{ink}$\displaystyle %s$\end{document}
"""

here = pathlib.Path(__file__).resolve().parent
out = here / "png"
out.mkdir(exist_ok=True)
sizes = {}
with tempfile.TemporaryDirectory() as tmp:
    tmp = pathlib.Path(tmp)
    for key, tex in EQ.items():
        (tmp / f"{key}.tex").write_text(TEMPLATE % tex, encoding="utf-8")
        run = subprocess.run(["pdflatex", "-interaction=nonstopmode", "-halt-on-error", f"{key}.tex"],
                             cwd=tmp, capture_output=True, text=True)
        if run.returncode:
            print("LaTeX failed:", key)
            print(run.stdout[-800:])
            continue
        subprocess.run(["pdftocairo", "-png", "-transp", "-singlefile", "-r", str(DPI), f"{key}.pdf", key],
                       cwd=tmp, check=True)
        shutil.copy(tmp / f"{key}.png", out / f"{key}.png")
        w, h = Image.open(out / f"{key}.png").size
        sizes[key] = {"png_w": w, "png_h": h, "display_w": round(w / 2), "display_h": round(h / 2)}
        print(f"{key:10s} display {round(w / 2):5d} x {round(h / 2):4d}")
(here / "sizes.json").write_text(json.dumps(sizes, indent=1), encoding="utf-8")
