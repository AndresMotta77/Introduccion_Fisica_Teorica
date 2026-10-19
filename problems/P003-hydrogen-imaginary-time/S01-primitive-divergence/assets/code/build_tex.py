#!/usr/bin/env python3
"""Build final/final.tex from final/final.md, per skills/log/reference/final-tex-template.tex.

Usage (from the problem folder):  python assets/code/build_tex.py
Then, in final/:                  latexmk -pdf final.tex

This is a format conversion, not an edit. Every equation, number and sentence of
the body is the text of final.md, which is the text of answers/answer-2.md.
Provenance tags at the start of a paragraph or list item become margin notes, as
the template requires; tags in mid-sentence stay in the text. The abstract and
the audit-history appendix are the only prose written by /log, and they report
what is in the folder. Adapted from P002's build_tex.py.
"""
import pathlib, re, subprocess, sys

ROOT = pathlib.Path(__file__).resolve().parents[2]          # the problem folder
FINAL = ROOT / 'final'
TEMPLATE = pathlib.Path(sys.argv[1]) if len(sys.argv) > 1 else None

md = (FINAL / 'final.md').read_text()

# The front matter (title, table, gap list, gate banner) becomes \maketitle, the
# banner and the abstract; the body starts after the first horizontal rule.
front, body_md = md.split('\n---\n', 1)

store = {}
def stash(tex):
    key = f"@@X{len(store):04d}@@"
    store[key] = tex
    return key

# display math. Inline replacement (no added blank lines) keeps list items intact.
def repl_display(m):
    inner = m.group(1).strip()
    if '\\tag{' in inner:
        return stash('\\stepcounter{equation}\\begin{equation}\n' + inner + '\n\\end{equation}')
    return stash('\\[\n' + inner + '\n\\]')
body_md = re.sub(r'\$\$(.*?)\$\$', repl_display, body_md, flags=re.S)

# provenance tags at the start of a paragraph or list item -> margin notes
TAG = r'\[(D|S|V|R|N|A1?|\?)((?:, [^\]]*)?)\]'
def repl_tag(m):
    lead, t, extra = m.group(1), m.group(2), m.group(3)
    label = '[' + t + extra + ']'
    label = label.replace('_', '\\_')
    return lead + stash('\\tagmark{%s}' % label) + ' '
body_md = re.sub(r'(?m)^(\s*(?:[-*]|\d+\.)?\s*)' + TAG + r'\s+', repl_tag, body_md)

def pandoc(text, shift=-1):
    cmd = ['pandoc', '-f', 'markdown+tex_math_dollars+pipe_tables+raw_tex-smart',
           '-t', 'latex', '--listings', f'--shift-heading-level-by={shift}',
           '--wrap=preserve']
    r = subprocess.run(cmd, input=text, capture_output=True, text=True)
    if r.returncode:
        sys.exit('pandoc failed: ' + r.stderr[:2000])
    return r.stdout

body = pandoc(body_md)
for k, v in store.items():
    body = body.replace(k, v)
prov = pandoc((ROOT / 'sources' / 'provenance.md').read_text(), shift=0)
indep = pandoc((ROOT / 'sources' / 'independence.md').read_text(), shift=0)
for text, name in ((body, 'body'), (prov, 'prov'), (indep, 'indep')):
    left = re.findall(r'@@X\d{4}@@', text)
    if left:
        sys.exit(f'unsubstituted placeholders in {name}: {left[:5]}')
# drop the files' own top-level titles; the appendix supplies the heading
prov = re.sub(r'\\section\{Provenance ledger[^}]*\}(\\label\{[^}]*\})?', '', prov)
indep = re.sub(r'\\section\{Independence record[^}]*\}(\\label\{[^}]*\})?', '', indep)

template = (TEMPLATE or (ROOT.parents[2] / 'skills' / 'log' / 'reference' / 'final-tex-template.tex')).read_text()
pre, _ = template.split('\\title{', 1)
pre += r"""
% final.md carries answer-2's own section numbers, gaps included; LaTeX must not
% add a second, different set.
\setcounter{secnumdepth}{0}
\setcounter{tocdepth}{2}
% Line-breaking parameters only; they change no text. The overfull count for the
% latex_clean gate is measured with them in place.
\sloppy
\setlength{\emergencystretch}{3em}
\providecommand{\passthrough}[1]{#1}
\providecommand{\tightlist}{\setlength{\itemsep}{0pt}\setlength{\parskip}{0pt}}
% Characters that arrive verbatim from the answer and that pdflatex with
% T1/inputenc cannot set by itself. Declared, not edited out.
\usepackage{textcomp}
\DeclareUnicodeCharacter{2212}{\ensuremath{-}}
\DeclareUnicodeCharacter{207B}{\ensuremath{^{-}}}
\DeclareUnicodeCharacter{211D}{\ensuremath{\mathbb{R}}}
\DeclareUnicodeCharacter{2192}{\ensuremath{\to}}
\DeclareUnicodeCharacter{03B2}{\ensuremath{\beta}}
\DeclareUnicodeCharacter{0394}{\ensuremath{\Delta}}
\DeclareUnicodeCharacter{2265}{\ensuremath{\ge}}
\DeclareUnicodeCharacter{2229}{\ensuremath{\cap}}
\DeclareUnicodeCharacter{2208}{\ensuremath{\in}}
\DeclareUnicodeCharacter{221E}{\ensuremath{\infty}}
\DeclareUnicodeCharacter{27E8}{\ensuremath{\langle}}
\DeclareUnicodeCharacter{27E9}{\ensuremath{\rangle}}
\DeclareUnicodeCharacter{2248}{\ensuremath{\approx}}
\DeclareUnicodeCharacter{2264}{\ensuremath{\le}}
\DeclareUnicodeCharacter{03B7}{\ensuremath{\eta}}
\DeclareUnicodeCharacter{03C4}{\ensuremath{\tau}}
\lstset{columns=fullflexible,keepspaces=true}
"""

GATE_TEX = r"""
\begin{center}
\fbox{\parbox{0.93\linewidth}{\small
\textbf{Release gates: 3 of 14 failed.} Stamped here by \texttt{/log} per
\texttt{skills/log/SKILL.md} step 2, which requires a failed gate to be recorded
in \texttt{meta.yaml} and in a banner at the top of this document rather than
quietly fixed. The user closed the loop with these failures on record. None of the three
touches a derivation step or a number.

\smallskip
\texttt{no\_unflagged\_recall} --- fail. Two [R] tags are not in the Risk
register (\S7): the proton radius in \S4.1 item 6, and ``$R_{nl}(0)=0$ for
$l\ge1$'' in the coverage note of check C4. Neither is load-bearing. They are not
added here, because step~3 of the log skill forbids editing the final document.

\smallskip
\texttt{code\_audited} --- fail. The audit's pass~6 is one line (``Code was
audited by reading; execution not performed in this session''), and it reviews no
check for circularity, vacuity or laundered assumptions. Check C6, added in
round~2, was never seen by the auditor.

\smallskip
\texttt{latex\_clean} --- fail. This document compiles with no undefined
references, no undefined citations, no missing characters and no
\texttt{\textbackslash emph}, but two overfull boxes exceed 10\,pt: 39.1 and
34.8\,pt. They are the display equations (A3) and (B10), which are wider than the
text block. Both are typographic and are left as they are, for the same step-3
reason. Five overfull rows in the provenance table, which \texttt{/log} authors,
were cleared by widening its columns.

\smallskip
The other eleven gates pass.
}}
\end{center}
""".strip()

ABSTRACT = r"""
The time-sliced (primitive) trace $Z_N(\beta)=\operatorname{Tr}(e^{-\Delta\tau K}e^{-\Delta\tau V})^N$
for hydrogen, $K=-\frac12\nabla^2$, $V=-1/r$, is written as a $3N$-dimensional bead
integral with every prefactor, and is shown to be $+\infty$ for every $N\ge1$ and
every $\Delta\tau>0$. Two regions of configuration space are responsible. One is
any single bead approaching the nucleus, where $e^{\Delta\tau/r}$ is not
integrable. This divergence is specific to time slicing; the Gaussian kinetic
factors cannot compensate it, and with a cutoff they do not change its leading
growth. The other is the whole chain moving off to infinity, a divergence the
exact trace shares. In the continuum, the exact kernel is finite and continuous
everywhere, the nucleus included, because $-1/r$ is in the Kato class, while
$\operatorname{Tr}e^{-\beta H}$ is infinite for the large-volume reason alone. The
imaginary-time Trotter product formula requires both summands to be bounded
below, and $V$ is the one that is not. On the strength of the evidence: the
proofs are elementary and every inequality is written out. Five numerical checks
recompute quantities from the problem statement. Among them, the exact kernel at
the origin is obtained by two independent routes that agree to $5\times10^{-7}$.
The single audit round (Gemini, self-reported, with no code execution and no web
access) returned ACCEPT with one NIT. It did not recompute the load-bearing
divergence proofs, and two citations, Reed--Simon~I Theorem~VIII.31 and Simon 1982
Theorem~B.7.1, remain unverified against the books.
"""

AUDIT_HISTORY = r"""
One round. The solver produced \texttt{answers/answer-1.md}. The auditor returned
a ten-pass report with verdict ACCEPT and one finding. The solver then produced
\texttt{answers/answer-2.md}, from which this document is derived. The stopping
rule of CONVENTIONS \S6 was met at round~1, which returned no BLOCKER and no MAJOR.

The auditor was ``Gemini'' with effort ``high'', both self-reported in the report's
run header. It declared code execution: no, and web: no. The audit prompt
(\texttt{prompts/audit-prompt-1.md}) went out with its \texttt{[FOCUS]} block empty.

Finding F1.1, a NIT against Part C.3: the bound on the bound-state sum was asserted
without the step that justifies factoring out $e^{\tau/2}$. Accepted. The
term-by-term step was added, together with check C6, which tests the inequality
and its sharpness as $\tau\to0$. No finding was rebutted, so
\texttt{rebuttals\_upheld} is zero and carries no information here.

In its response the solver recorded four observations about the audit, contesting
no finding (\texttt{audits/findings.yaml}, S1.1 to S1.4):
\begin{itemize}
\item Pass~7 reports the citations as verified although the auditor had no web
access.
\item Pass~3 did not recompute the steps the result rests on most: (B7)--(B9),
(B12)--(B13), (B14)--(B16), Remark~B.6, and (C6)--(C7).
\item The corrector prompt asks both for a full rewrite and for the frozen sections
to be left alone. The solver treated the frozen list as controlling.
\item With one NIT open, CONVENTIONS \S5 allows either ACCEPT or ACCEPT-WITH-FIXES.
\end{itemize}

\texttt{answers/answer-2.md} was not itself audited. Its new material, the F1.1
step and check C6, has never been read by an auditor. That is recorded here rather
than resolved.
"""

SCRIPTS = ['c1_radial_growth', 'c2_collapse_N2', 'c3_chapman_kolmogorov',
           'c4_exact_kernel_origin', 'c5_kato_class_run1_scipy', 'c5_kato_class']
code_section = ['\\section{Code}\\label{app:code}',
                'Every script as executed in rounds 1 and 2. The scripts and their verbatim outputs are '
                'quoted in \\S4.2 above. The files are in \\texttt{assets/code/}, each with a \\texttt{.out} '
                'file holding its output and a \\texttt{.coverage.md} file stating what the check would and '
                'would not have caught. Check C6, added in round~2 for finding F1.1, is '
                '\\texttt{c6\\_f11\\_bound.py}; it is listed here because \\S10 of answer-2 is not '
                'reproduced in this document.', '']
for s in SCRIPTS + ['c6_f11_bound']:
    code_section.append('\\subsection{\\texttt{%s.py}}' % s.replace('_', '\\_'))
    if s != 'c6_f11_bound':
        code_section.append('Reproduced in \\S4.2.')
    else:
        code_section.append('\\lstinputlisting[language=Python]{../assets/code/%s.py}' % s)
        code_section.append('\\noindent Output (\\texttt{c6\\_f11\\_bound.out}):')
        code_section.append('\\lstinputlisting{../assets/code/%s.out}' % s)
    code_section.append('')

out = [
    pre,
    '\\title{P003.S01 --- Failure of the primitive path integral at $r=0$ for the Coulomb potential}',
    '\\author{Felipe Ospina \\\\ \\small Universidad Nacional de Colombia \\\\ '
    '\\small Solver: Claude Opus 5.5; auditor: Gemini; logged by \\texttt{/log} v1.6}',
    '\\date{2026-10-19}',
    '',
    '\\begin{document}',
    '\\maketitle',
    '',
    GATE_TEX,
    '',
    '\\begin{abstract}', ABSTRACT.strip(), '\\end{abstract}',
    '',
    '\\tableofcontents',
    '\\clearpage',
    '',
    body,
    '',
    '\\appendix',
    '',
    '\\section{Provenance}\\label{app:provenance}',
    'One row per tagged claim, built from the tags in the text. Generated from '
    '\\texttt{sources/provenance.md}.',
    '',
    '{\\small', prov, '}',
    '',
    '\\section{Independence record}\\label{app:independence}',
    indep,
    '',
    '\\section{Audit history}\\label{app:audit}',
    AUDIT_HISTORY.strip(),
    '',
    '\n'.join(code_section),
    '\\nocite{*}',
    '\\bibliographystyle{unsrtnat}',
    '\\bibliography{../sources/sources}',
    '',
    '\\end{document}',
    '',
]
tex = '\n'.join(out)
# CONVENTIONS §7 and the house style forbid \emph. pandoc emits \emph for every
# markdown italic; keep the words, drop the emphasis.
tex = re.sub(r'\\emph\{([^{}]*)\}', r'\1', tex)
assert '\\emph' not in tex, 'an \\emph survived'
(FINAL / 'final.tex').write_text(tex)
print('final.tex written:', len(tex), 'bytes')
