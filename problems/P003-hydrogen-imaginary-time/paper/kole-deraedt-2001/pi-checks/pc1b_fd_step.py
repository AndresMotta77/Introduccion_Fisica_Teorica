"""
pc1b_fd_step.py  (PI check, diagnostic for pc1_table1.py)

pc1 stated beforehand that routes B and C must agree to 1e-7. They did not at m = 500
(max |B - C| = 3.35e-7). This run asks whether the gap is the finite-difference step of
route C (truncation ~ h^2, round-off ~ eps*|ln Z|/h) or a real disagreement between the
re-derived closed form (B) and the matrices built from (17) and (3) (C).
Expected if it is numerical: the gap changes with h and has a minimum at an intermediate h.
Expected if it is real: the gap is independent of h.
pc1_table1.py is not edited; its functions are imported unchanged.
"""
import importlib.util, sys, pathlib
spec = importlib.util.spec_from_file_location("pc1", pathlib.Path(__file__).with_name("pc1_table1.py"))
src = pathlib.Path(__file__).with_name("pc1_table1.py").read_text()
src = src.split('# Table I as printed')[0]          # function definitions only, no table run
ns = {}; exec(compile(src, "pc1_table1.py", "exec"), ns)
from mpmath import mpf
for b, m in [(1, 500), (5, 500), (10, 500), (1, 100)]:
    eB, hB = float(ns["Em_B"](mpf(b), m)), float(ns["Ehat_B"](mpf(b), m))
    row = []
    for h in (1e-3, 1e-4, 1e-5, 1e-6):
        def E(kind):
            return -(ns["lnZ_C"](b + h, m, kind) - ns["lnZ_C"](b - h, m, kind)) / (2*h)
        row.append(f"h={h:.0e}: {abs(E('prim')-eB):.1e}/{abs(E('jensen')-hB):.1e}")
    print(f"beta={b:2d} m={m:3d}  |C-B| for E_m/Ehat_m  " + "  ".join(row))
