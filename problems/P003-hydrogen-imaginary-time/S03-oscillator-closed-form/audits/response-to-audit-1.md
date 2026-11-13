# Response to audit 1 — P003.S03

Verbatim §10 of `answers/answer-2.md` (round 2, 2026-11-13). Not reviewed by an auditor.

## 10. Response to audit 1

| Finding | Outcome | What changed | Where |
|---|---|---|---|
| F1.1 (MINOR) | partial: the defect is accepted and fixed; part of the evidence and one of the suggested fixes are rejected | `\mathbb 1` replaced by $\mathbf 1$ at all 8 occurrences; $\mathbf 1$ defined at first use and added to the symbol table; new check P1 | §2.2; §3.2 (the two sums before eq. (12), eq. (12), the $m=2$ item, eq. (19a)); §4.2; §4.3 (P1); §7; §8 |

### F1.1, accepted part

The defect is real. Under the house LaTeX template, the identity matrix printed as $\nVdash$ instead of a double-struck one. This affected eqs. (12) and (19a), the two sums just before (12), and the $m=2$ item. It happened silently: on answer-1, P1b reports 0 TeX errors and 0 missing characters, while P1a finds 8 hits.

The mechanism, read from the installed files:
- `amsfonts.sty` (line 108) declares `\mathbb` as the alphabet of the AMSb symbol font;
- that font has blackboard glyphs only in the uppercase-letter slots;
- the slot of the digit 1, "31, holds `\nVdash` (`amssymb.sty`, line 220).

I replaced every instance with $\mathbf 1$, which is the third option the finding supplies. `\mathbf` is a LaTeX kernel command, so it works under any package set; MathJax and KaTeX also support it, though I did not test a viewer. I also defined the symbol at first use and in the symbol table. Answer-1 used it without a definition, which is a separate omission of the same kind (Conventions §7).

After the change, P1a finds 0 hits in answer-2, and P1b compiles answer-2 under the house preamble with 0 errors and 0 missing characters.

### F1.1, rejected part, with evidence

1. The premise that the allowed packages are amsmath, physics and siunitx. The house template used by the `/log` step (log skill, `reference/final-tex-template.tex`) loads `\usepackage{amsmath,amssymb,amsthm,mathtools}`, then physics and siunitx. Neither prompt0 nor CONVENTIONS.md restricts packages.
2. The claim that amssymb is "loaded by `amsmath` or `physics`". Neither package loads it. `amsmath.sty` v2.17o requires only amstext, amsbsy and amsopn (lines 127–129). `physics.sty` requires only xparse and amsmath (lines 15–16). Under the package set the finding states, `\mathbb` is not defined at all, and the probe gives `Undefined control sequence`, not a wrong glyph.
3. The first suggested fix, `\mathbb{I}`. It renders correctly under the house template. Under the finding's own premise it would be an undefined control sequence, as would the `\mathbb R` and `\mathbb E` used elsewhere in the answer, which the finding did not flag. I chose $\mathbf 1$ because it is right under both readings. I also avoided a plain $I$, which already denotes the exponent $I(x,x';\tau)$ of eq. (8).
4. "An illegible glyph or a blank space." What is printed is a legible but wrong glyph, the relation symbol $\nVdash$. This makes the finding stronger, not weaker, since a reader can take it for an operator.

Consequence for the rest of the answer. Under the actual house template, the other amssymb constructs in the answer render correctly (probe and P1b): `\mathbb R`, `\mathbb E`, `\square`, `\lesssim`, `\gtrsim`. So no further change is needed. Had the finding's package set been the real one, all of them would have needed changing, and changing only the identity would not have satisfied the finding's own test.

### Solver-raised item, not acted on

SR2.1 (NIT, presentation, frozen sections). In the pandoc build under the house preamble, some displays and long table rows run into the right margin: eqs. (6), (13) and (14) are visibly cut, and the build log reports several overfull lines. In markdown they display normally. Fixing them means re-laying-out equations in frozen sections, so I raise the item for the next audit or for the `/log` step rather than editing.

### Changes outside F1.1

There are no changes to the mathematics, to any number, or to §§1, 3.1, 3.3, 3.4, 5, 6 and 9. §3.2 changed only in the identity-matrix notation and in the table caption, which now names the round-2 re-run. §2.2 gained one row. The header has a new paragraph describing round 2.

§4 changed only by the round-2 re-runs (new outputs, identical to round 1 apart from timing lines), by the rebuilt superseded scripts and their validation, and by the new P1 subsection. §7 has three updated or new rows, and §8 has four new Used entries, which are load-bearing only for this section.

### On the audit itself

The auditor reports that no code was executed. The executed verification is therefore still only mine, now re-run in round 2; Pass 6b recomputed $\hat Z_1$ analytically. An auditor-run re-implementation of C1 or B2 would still add independent evidence (§9, item 6).
