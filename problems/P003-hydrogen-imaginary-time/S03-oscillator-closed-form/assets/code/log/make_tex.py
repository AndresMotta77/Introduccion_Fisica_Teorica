# make_tex.py -- build final/final.tex from final/final.md with the house template
# (log skill, reference/final-tex-template.tex). Body = final.md converted by pandoc with
# tags.lua. The template's placeholder body sections are replaced by final.md's own
# sections 2-9 (content is not rewritten). Preamble additions needed by pandoc's writer are
# marked. Run from tex/: python3 -I make_tex.py
import subprocess, pathlib, re
S = pathlib.Path('/home/claude/log/S03')
fm = (S/'final/final.md').read_text(encoding='utf-8')

def pandoc(md, shift):
    r = subprocess.run(["pandoc", "-f", "markdown", "-t", "latex", "--listings",
                        f"--shift-heading-level-by={shift}", "--lua-filter", "tags.lua"],
                       input=md, capture_output=True, text=True, check=True)
    return r.stdout

# header block of final.md: title, subtitle, banner (blockquote), derivation note
cut = fm.index("\n---\n")
head, body = fm[:cut], fm[cut + 5:]
banner_md = "\n".join(l[2:] for l in head.splitlines() if l.startswith("> "))
note_md = head[head.index("This document is"):].strip()
banner = pandoc(banner_md, 0)
note = pandoc(note_md, 0)
body_tex = pandoc(body, -1)

prov = (S/'sources/provenance.md').read_text(encoding='utf-8')
prov = prov[prov.index("\n") + 1:]                       # drop the "# Provenance ledger" line
indep = (S/'sources/independence.md').read_text(encoding='utf-8')
indep = indep[indep.index("\n") + 1:]
audit_md = """| Round | Artifact audited | Auditor (self-reported) | Verdict | Findings and disposition |
|---|---|---|---|---|
| 1 | `answers/answer-1.md` | Gemini; effort high; no code executed; no web | ACCEPT-WITH-FIXES | F1.1 (MINOR): partial. The defect (identity matrix printed as a wrong glyph) was accepted and fixed in answer-2; parts of the evidence and one suggested fix were rebutted. No auditor response. |
| 2 | `answers/answer-2.md` | none | not audited | The user closed the loop on 2026-11-13; gate `audit_trail_complete` failed. SR2.1 (NIT, solver-raised, PDF layout): deferred. |

The verbatim audit report is `audits/audit-report-1.md`. The corrector prompt is `prompts/corrector-prompt-1.md`, the solver's response is `audits/response-to-audit-1.md`, and every finding is listed in `audits/findings.yaml`.
"""
prov_tex = pandoc(prov, 0)
indep_tex = pandoc(indep, 0)
audit_tex = pandoc(audit_md, 0)

abstract = r"""The bridge-averaged slice weight $w(x,x';\tau)$ for the harmonic oscillator, defined by exponentiating the free-bridge average of $V$, is evaluated in closed form: $w=\rho_0\exp[-\tau(x^2+xx'+x'^2)/6-\tau^2/12]$. The closed-ring products of $w$ and of the primitive weight $\rho_0e^{-\tau V}$ are Gaussian integrals, diagonalised in ring Fourier modes. They give $\hat Z_m=e^{-\beta^2/12m}/[(\kappa+\tau/2)^m-(\kappa-\tau/2)^m]$ with $\kappa=\sqrt{1+\tau^2/12}$, and $Z_m=[2\sinh(m\operatorname{arcsinh}(\beta/2m))]^{-1}$; the thermal energies are tabulated against $\tfrac12\coth(\beta/2)$. The integral operator with kernel $w$ has eigenvalues $\lambda_n=e^{-\tau^2/12}(\kappa-\tau/2)^n/(\kappa+\tau/2)^{n+1}$ for all $\tau>0$ and loses positivity at $\tau=\sqrt6$. Its levels obey $E_n-(n+\tfrac12)=(2n+1)\tau^2/48-\tau^3/144+O(\tau^4)$, against $-(2n+1)\tau^2/48$ for the symmetric primitive kernel, and $\hat Z_m=\sum_n\lambda_n(\beta/m)^m$ links the two parts. Evidence: every closed form was checked by the solver's own code against a route that does not pass through it (quadrature of the definition, numerically assembled $m\times m$ matrices, grid diagonalisation, Mehler's formula), and the checks were re-run in round 2 with identical output. One audit round (Gemini, no code executed) returned ACCEPT-WITH-FIXES with a single presentation finding. The corrected answer, from which this document is derived, was not audited."""

preamble = r"""\documentclass[11pt,a4paper]{article}

\usepackage[T1]{fontenc}
\usepackage[utf8]{inputenc}
\usepackage{lmodern}
\usepackage[margin=1in,marginparwidth=1.1in]{geometry}
\usepackage{amsmath,amssymb,amsthm,mathtools}
\usepackage{physics}
\usepackage{siunitx}
\usepackage{graphicx}
\usepackage{booktabs}
\usepackage{longtable}
\usepackage{marginnote}
\usepackage{listings}
\usepackage[hidelinks]{hyperref}
\usepackage[numbers,sort&compress]{natbib}

% Provenance tags. These are the audit trail; do not strip them when converting
% from final.md. They are set small in the margin so the prose reads cleanly.
\newcommand{\tagmark}[1]{\marginnote{\scriptsize\ttfamily #1}}
\newcommand{\Dtag}{\tagmark{[D]}}   % derived here
\newcommand{\Stag}[1]{\tagmark{[S] #1}}  % standard result + locator
\newcommand{\Vtag}[1]{\tagmark{[V] #1}}  % verified against retrieved source
\newcommand{\Rtag}{\tagmark{[R]}}   % recalled, unverified
\newcommand{\Atag}{\tagmark{[A]}}   % assumption
\newcommand{\Ntag}{\tagmark{[N]}}   % numerical / symbolic check
\newcommand{\Qtag}{\tagmark{[?]}}   % low confidence

\lstset{basicstyle=\ttfamily\footnotesize,breaklines=true,frame=single,
        showstringspaces=false}

% ---- additions for pandoc's LaTeX writer (not in the house template) ----
\usepackage{array}
\providecommand{\tightlist}{\setlength{\itemsep}{0pt}\setlength{\parskip}{0pt}}
\newcommand{\passthrough}[1]{#1}
% final.md numbers its own sections (2.--9., kept from answer-2); suppress LaTeX numbering
\setcounter{secnumdepth}{0}
% ---- end of additions ----
"""

doc = preamble + r"""
\title{P003.S03 --- The harmonic oscillator under a bridge-averaged slice weight: closed form and levels}
\author{Solver: Claude Opus 5.5 (\texttt{claude-opus-5-5}). Auditor, round 1: Gemini.}
\date{Closed 2026-11-13}

\begin{document}
\maketitle

% Gate banner. Present only when a release gate failed; delete otherwise.
\noindent\fbox{\parbox{\dimexpr\linewidth-2\fboxsep-2\fboxrule}{%
""" + banner.strip() + r"""}}

\begin{abstract}
""" + abstract + r"""
\end{abstract}

""" + note.strip() + r"""

\tableofcontents

""" + body_tex + r"""

\appendix

\section{Appendix A. Provenance}\label{app:provenance}
One row per tagged claim. This table is generated from
\texttt{sources/provenance.md}.

""" + prov_tex + r"""

\section{Appendix B. Independence record}\label{app:independence}
""" + indep_tex + r"""

\section{Appendix C. Audit history}\label{app:audit}
""" + audit_tex + r"""

\section{Appendix D. Code}\label{app:code}
All verification scripts are reproduced verbatim, with their outputs, in Section 4. The scripts as executed, each with its output and coverage file, are in \texttt{assets/code/} (folders \texttt{round-1}, \texttt{round-2} and \texttt{log}).

\nocite{*}
\bibliographystyle{unsrtnat}
\bibliography{../sources/sources}

\end{document}
"""
(S/'final/final.tex').write_text(doc, encoding='utf-8')
print("final.tex:", len(doc), "chars;", doc.count("\\tagmark") + doc.count("tag{}"), "tag macros")
