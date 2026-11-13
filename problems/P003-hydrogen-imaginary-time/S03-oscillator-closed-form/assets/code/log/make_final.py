# make_final.py -- derive final/final.md, sources/independence.md (declaration and
# convergence-check parts) and audits/response-to-audit-1.md from answers/answer-2.md.
# The final document is answer-2 with sections moved out, not a rewrite. Every edit is an
# exact, asserted replacement; the list below is the complete list of changes.
#   1. header (title block and round-2 paragraph) replaced by the final header + gate banner;
#   2. section 1 (Prior-knowledge declaration) moved to sources/independence.md;
#   3. section 10 (Response to audit 1) moved to audits/response-to-audit-1.md;
#   4. two cross-references to section 10 redirected to that file.
# Run: python3 -I make_final.py answer-2.md S03
import sys, pathlib
src = pathlib.Path(sys.argv[1]).read_text(encoding='utf-8')
out = pathlib.Path(sys.argv[2])

def cut(text, start, end):
    i = text.index(start); j = text.index(end, i)
    assert text.count(start) == 1
    return text[:i], text[i:j], text[j:]

# 1. header
head_end = src.index("---\n\n## 1. Prior-knowledge declaration")
header_old = src[:head_end]
assert header_old.startswith("# P003.S03 — answer-2")

# 2. section 1
pre, sec1, rest = cut(src, "## 1. Prior-knowledge declaration", "---\n\n## 2. Setup")
# 3. section 10
k = rest.index("---\n\n## 10. Response to audit 1")
assert rest.count("## 10. Response to audit 1") == 1
body, sec10 = rest[:k], rest[k + len("---\n\n"):]
sec6 = body[body.index("## 6. Convergence check"):body.index("## 7. Risk register")]

# 4. cross-references
reps = [
    ("these are raised as SR2.1 in §10, not tested;",
     "these are raised as SR2.1 in the Response to audit 1 (`audits/response-to-audit-1.md`), not tested;"),
    ("These are load-bearing only for §10 (Response to audit 1).",
     "These are load-bearing only for the Response to audit 1 (`audits/response-to-audit-1.md`)."),
]
for a, b in reps:
    assert body.count(a) == 1, a
    body = body.replace(a, b)
assert "§10" not in body

header_new = """# P003.S03 — final

The harmonic oscillator under a bridge-averaged slice weight: closed form, partition functions, levels.

> Release gate failed: `audit_trail_complete`. answer-2, from which this document is derived, was not audited. Audit 1 (of answer-1) returned ACCEPT-WITH-FIXES with one MINOR finding, F1.1. answer-2 applies the fix, adds check P1 and contests part of the finding's evidence, and none of that was reviewed by an auditor. The user closed the loop on 2026-11-13 under the stopping rule of CONVENTIONS.md §6 (audit 1 raised no BLOCKER and no MAJOR).

This document is `answers/answer-2.md` (Claude Opus 5.5, round 2, 2026-11-13) with sections moved out by `assets/code/log/make_final.py`. Section numbers are those of answer-2. §1, the Prior-knowledge declaration, is in `sources/independence.md`, together with a copy of §6. §10, the Response to audit 1, is in `audits/response-to-audit-1.md`. The only other edits redirect two cross-references from §10 to that file.

"""
assert pre[head_end:] == "---\n\n"          # the separator before section 1 goes with it
final = header_new + body.rstrip("\n") + "\n"
(out / "final").mkdir(parents=True, exist_ok=True)
(out / "final" / "final.md").write_text(final, encoding='utf-8')
(out / "audits" / "response-to-audit-1.md").write_text(
    "# Response to audit 1 — P003.S03\n\nVerbatim §10 of `answers/answer-2.md` (round 2, 2026-11-13). Not reviewed by an auditor.\n\n"
    + sec10.rstrip("\n") + "\n", encoding='utf-8')
pathlib.Path("sec1_verbatim.md").write_text(sec1.rstrip("\n").rstrip("-").rstrip("\n") + "\n", encoding='utf-8')
pathlib.Path("sec6_verbatim.md").write_text(sec6.rstrip("\n").rstrip("-").rstrip("\n") + "\n", encoding='utf-8')
print("final.md:", len(final), "chars; header lines replaced:", header_old.count("\n"),
      "; sec1:", len(sec1), "chars; sec10:", len(sec10), "chars; cross-refs redirected:", len(reps))
