#!/usr/bin/env python3
"""Build final.tex from final.md, per skills/log/reference/final-tex-template.tex.

This is a format conversion, not an edit. Every equation, number and sentence in
the output is the text of final.md, which is the text of answer-2.md. The only
content-level transformation is the removal of bold keyword openers at the start
of a paragraph, which CONVENTIONS.md §7 forbids in the final document; the words
themselves are kept. Everything else is markdown-to-LaTeX mechanics.
"""
import pathlib, re, subprocess, sys

HERE = pathlib.Path(__file__).resolve().parent
md = (HERE / 'final.md').read_text()

# ---------------------------------------------------------------- split off --
# The appendix becomes \lstinputlisting in the Code appendix, not inline text.
md_body, _appendix = md.split('## Appendix — verification code, verbatim', 1)

# Drop the markdown title and the front-matter table: they become \maketitle and
# the abstract in the template.
md_body = md_body.split('\n---\n', 1)[1] if '\n---\n' in md_body else md_body

# ------------------------------------------------------------- placeholders --
store = {}


def stash(tex):
    key = f"@@X{len(store):04d}@@"
    store[key] = tex
    return key


# display math -> equation / \[ \]
def repl_display(m):
    inner = m.group(1).strip()
    if '\\tag{' in inner:
        # \tag does not step the equation counter, so without an explicit step
        # every equation would claim the same hyperref destination.
        return ('\n\n' + stash('\\stepcounter{equation}\n\\begin{equation}\n'
                                + inner + '\n\\end{equation}') + '\n\n')
    return '\n\n' + stash('\\[\n' + inner + '\n\\]') + '\n\n'


md_body = re.sub(r'\$\$(.*?)\$\$', repl_display, md_body, flags=re.S)

# figures
def repl_img(m):
    return '\n\n' + stash(
        '\\begin{center}\n\\includegraphics[width=0.96\\linewidth]{%s}\n\\end{center}'
        % m.group(2)) + '\n\n'


md_body = re.sub(r'!\[([^\]]*)\]\(([^)]+)\)', repl_img, md_body)

# provenance tags at the start of a paragraph -> margin macros
TAGMAC = {'D': '\\Dtag{}', 'R': '\\Rtag{}', 'A': '\\Atag{}',
          'N': '\\Ntag{}', '?': '\\Qtag{}'}


def repl_tag(m):
    t = m.group(1)
    if t == 'V':
        return stash('\\Vtag{Folkers 2018, Thm 2.8 \\S2.4}') + ' '
    return stash(TAGMAC[t]) + ' '


md_body = re.sub(r'(?m)^`\[(D|R|A|N|V|\?)\]`\s+', repl_tag, md_body)

# bold keyword openers at the start of a paragraph: keep the words, drop the bold
md_body = re.sub(r'(?m)^(@@X\d{4}@@ )?\*\*([^*]{1,120}?)\*\*', r'\1\2', md_body)

# ------------------------------------------------------------------ pandoc ---
def pandoc(text, shift=-1):
    cmd = ['pandoc', '-f', 'markdown+tex_math_dollars+pipe_tables+raw_tex',
           '-t', 'latex', '--listings', f'--shift-heading-level-by={shift}',
           '--wrap=preserve']
    r = subprocess.run(cmd, input=text, capture_output=True, text=True)
    if r.returncode:
        sys.exit('pandoc failed: ' + r.stderr[:2000])
    return r.stdout


body = pandoc(md_body)

def strip_bold_openers(text):
    return re.sub(r'(?m)^\*\*([^*]{1,140}?)\*\*', r'\1', text)


prov = pandoc(strip_bold_openers((HERE / 'provenance.md').read_text()), shift=0)
indep = pandoc(strip_bold_openers((HERE / 'independence.md').read_text()), shift=0)

# restore the stashed LaTeX
for k, v in store.items():
    body = body.replace(k, v)

# pandoc escapes nothing inside our stashed blocks, but it can wrap a lone
# placeholder paragraph; make sure no placeholder survived anywhere.
for text, name in ((body, 'body'), (prov, 'prov'), (indep, 'indep')):
    left = re.findall(r'@@X\d{4}@@', text)
    if left:
        sys.exit(f'unsubstituted placeholders in {name}: {left[:5]}')

# --------------------------------------------------------------- assemble ----
template = (HERE / 'final-tex-template.tex').read_text()
pre, _ = template.split('\\title{', 1)

# The section titles carry their own numbers ("3.3 Separation of ...") because
# final.md keeps answer-2's numbering, gaps included, so that every cross
# reference in the text and in sources/provenance.md still resolves. LaTeX must
# therefore not add a second, different set of numbers.
pre += '\n% final.md carries its own section numbers; do not add a second set.\n'
pre += '\\setcounter{secnumdepth}{0}\n'
pre += '\\setcounter{tocdepth}{2}\n'
# pandoc --listings emits \passthrough{\lstinline!...!} for inline code and
# defines \passthrough only in its own default template, which this document
# does not use.
pre += '\\providecommand{\\passthrough}[1]{#1}\n'
# The document quotes sources and program output verbatim, so a few characters
# arrive that pdflatex with T1/inputenc cannot set on its own. Declared rather
# than edited out of the quotations.
pre += '\\usepackage{textcomp}\n'
pre += '\\DeclareUnicodeCharacter{00A7}{\\S}\n'
pre += '\\DeclareUnicodeCharacter{00B0}{\\textdegree}\n'
pre += '\\DeclareUnicodeCharacter{2113}{\\ensuremath{\\ell}}\n'
pre += '\\DeclareUnicodeCharacter{2013}{--}\n'
pre += '\\DeclareUnicodeCharacter{03C9}{\\ensuremath{\\omega}}\n'
pre += '\\DeclareUnicodeCharacter{226A}{\\ensuremath{\\ll}}\n'
# one program-output listing contains a section sign
pre += '\\lstset{extendedchars=true,inputencoding=utf8,literate={§}{{\\S}}1}\n'
pre += '\\providecommand{\\tightlist}{\\setlength{\\itemsep}{0pt}\\setlength{\\parskip}{0pt}}\n'

ABSTRACT = r"""
A pendulum of length $l$ carrying a point mass $m$, with its pivot driven
vertically as $y_p(t)=A\cos\omega t$ with $A\ll l$, is stable in the inverted
position when $A^2\omega^2>2gl$, and then oscillates slowly about the vertical
at $\Omega=\sqrt{A^2\omega^2/2l^2-g/l}$. The mechanism is that the shaking
forces a fast wiggle $\xi=(A/l)\sin\Theta\cos\omega t$ whose amplitude grows
with the lean, in phase with the driving term that produces it; the product of
two quantities that each average to zero does not average to zero, and what
survives is a restoring torque. Equivalently, the mean kinetic energy stored in
the wiggle, $\tfrac14 mA^2\omega^2\sin^2\Theta$, acts as a potential hill at the
horizontal. The equation of motion is obtained from a Lagrangian and the slow
dynamics by two-timescale averaging. The result is not asserted on the strength
of that derivation alone: the equation of motion is checked symbolically from
the geometry and against an independently formulated Newtonian constrained
dynamics; the threshold is recomputed by exact Floquet theory, which contains no
averaging; and the frequency is recomputed twice, once as a period measured on
the exact nonlinear equation and once as a Floquet phase, both converging on the
closed form at the predicted second order in $A/l$. Every check is also run
against deliberately mutated versions of the claim, and the mutants are
rejected. The averaged results carry a relative error of order $(A/l)^2$, which
is measured rather than asserted.
"""

AUDIT_HISTORY = r"""
One round. The solver produced \texttt{answers/answer-1.md}; the auditor
returned a nine-pass report with verdict ACCEPT-WITH-FIXES and two findings,
both MINOR; the solver produced \texttt{answers/answer-2.md}, from which this
document is derived.

Auditor: Gemini 3.1 Pro Avanzado with the extended-reasoning option, effort
level unknown. Both are user-reported; the report carried no run header, and
neither value was guessed.

Finding F1.1, MINOR, against \S3.3: the size-counting table asserted
$\omega_0^2\ll\varepsilon^2\omega^2$ near threshold, which is false, since at
the boundary $\varepsilon^2\omega^2=2\omega_0^2$ exactly. Accepted in full.
\S3.3 was rewritten around $\mu=2gl/(A^2\omega^2)$, the same combination that
appears as $\cos\Theta_{\rm c}$ in eq.~(34), and the corrected counting now says
what it should: all three slow terms are of the same order and none may be
dropped. The false line was in the justification and not in a step, and nothing
downstream rested on it; had it been acted on, the averaged equation would have
lost gravity and there would have been no threshold at all.

Finding F1.2, MINOR, against \S4.3 and \S4.4: standard results invoked without
the provenance tags CONVENTIONS \S1 requires. Accepted, and answered by deriving
them rather than tagging them. The amplitude--frequency relation for a quartic
well is now derived by Lindstedt--Poincar\'e in \S3.9 and tested on its own in
check~N7; $\det M=1$ and the $|\operatorname{tr}M|<2$ criterion are derived in
\S4.4. Risk-register entry R2 was retired and R3 added for the one item that
remains recalled.

No finding was rebutted. Both were correct, so \texttt{rebuttals\_upheld} is
zero for this problem and carries no information about whether the solver would
have disagreed; \texttt{claude/workflow-feedback.md} \S5 is the reason that
count is tracked at all.

The solver raised one item against the audit rather than against a finding. The
audit's pass~6 reports \texttt{Exact: 4.2764} from a script it quotes; run
verbatim, that script prints \texttt{Exact: 4.2867}, and five integrators agree
on $\operatorname{tr}M=1.967843917562$. The audit's conclusion survives --- the
Floquet frequency does agree with the closed form to $O(\varepsilon^2)$ --- but
the sign of the deviation is reversed. The audit text is kept verbatim in
\texttt{audits/audit-report-1.md} with the correction appended as a note, since
a wrong number in an audit report is an accurate record of what the auditor
said. The method itself was adopted as check~N8, swept in $\varepsilon$, and
used to test N4 and N8 against each other.

\texttt{answers/answer-2.md} was not itself audited. The stopping rule in
CONVENTIONS \S6 was met at round~1, which returned no BLOCKER and no MAJOR, and
ACCEPT-WITH-FIXES means one further pass closes the MINORs; that pass is
answer-2. Its new material --- \S3.9, check~N7 and check~N8 --- has therefore
never been read by an auditor. Recorded here rather than resolved.
"""

SCRIPTS = ['check1_eom_symbolic', 'check2_newton_vs_lagrange', 'diag_set8',
           'check3_slow_frequency', 'check4_floquet_boundary',
           'check5_basin_and_ripple', 'check6_duffing_shift',
           'check7_floquet_frequency', 'figures']

code_section = ['\\section{Code}\\label{app:code}',
                'Every script as executed. Outputs are quoted verbatim in '
                '\\S4 above; the files themselves are '
                '\\texttt{assets/code/out\\_check*.txt}, each paired with a '
                '\\texttt{.coverage.md} stating what that check would and would '
                'not have caught.', '']
for s in SCRIPTS:
    code_section.append('\\subsection{\\texttt{%s.py}}' % s.replace('_', '\\_'))
    code_section.append('\\lstinputlisting[language=Python]{../assets/code/%s.py}' % s)
    code_section.append('')

out = [
    pre,
    '\\title{P002 --- Inverted pendulum with a vertically oscillating pivot}',
    '\\author{Felipe Ospina \\\\ \\small Universidad Nacional de Colombia}',
    '\\date{2026-09-14}',
    '',
    '\\begin{document}',
    '\\maketitle',
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
    '\\end{document}',
    '',
]
tex = '\n'.join(out)
# the provenance and independence appendices arrive with their own \section
# headings from pandoc; demote them so they sit under the appendix sections.
tex = tex.replace('\\section{Provenance ledger --- P002}', '')
tex = tex.replace('\\section{Independence record --- P002}', '')
# CONVENTIONS.md §7 forbids \emph in the final document, and the user's house
# style forbids it generally. pandoc emits \emph for every markdown italic.
# Work titles and the two defined terms of CONVENTIONS §3 are genuine italics
# and become \textit; emphasis inside prose is dropped, keeping the words.
KEEP_ITALIC = ['Mechanics', "Floquet's Theorem", 'Problem of the Week',
               'Used', 'Consulted']
def de_emph(m):
    inner = m.group(1)
    return ('\\textit{%s}' % inner) if inner in KEEP_ITALIC else inner
tex = re.sub(r'\\emph\{([^{}]*)\}', de_emph, tex)
assert '\\emph' not in tex, 'an \\emph survived'

(HERE / 'final.tex').write_text(tex)
print('final.tex written:', len(tex), 'bytes')
