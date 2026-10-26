# P003 — Phase 1 presentation

A ten-minute talk on phase 1 of the project. Slides 2 to 9 follow the team's handwritten
notes (`../../S01-primitive-divergence/human/Integrales_de_Camino_de_Feynman_261017_174852_2.pdf`)
page by page: Feynman's path integral, its imaginary-time version, and the weight of the
Coulomb potential at the nucleus. Slides 10 to 15 present what S01 found when it checked
those pages.

The user asked for it on 2026-10-19 and revised it on 2026-10-26 to follow the notes more
closely. It was built by Claude (configured model `claude-opus-5-5`). It is not the "first
presentation" of PLAN step 2.4, which falls in week 6, at the end of phase 2.

## The deck

The deck is a Claude Slides artifact: https://claude.ai/artifact/8fj5V5Ph3ccNvbe6ybhNdp
(version 14 on 2026-10-26, 15 slides at 16:9). It is private to its owner until it is
shared from the page, and it can be downloaded from there as `.pptx` or PDF. Every slide
carries its explanation in the speaker notes. `speaker-notes.md` has a copy of all of them.

`artifact/` is a copy of the deck's own files as published in version 14: `deck.json` and
one HTML file per slide. In those files the images are addressed as `/_blob/<id>`, which
only resolves inside the artifact. The same images are in `equations/png/` and
`figure/fig_growth.png`.

| # | slide id | content | source |
|---|---|---|---|
| 1 | cover | title | — |
| 2 | feynman | time slicing, the discretised action, amplitudes, K(b, a) | notes p. 1 |
| 3 | gauss | Gaussian integrals, change of basis, det M = N for the free particle | notes p. 2 |
| 4 | free | the action expanded about the classical path; the free propagator | notes p. 3 |
| 5 | plan | E₀ from Z(β) after the Wick rotation; the trace as closed paths | notes p. 4 |
| 6 | imaginary | [K̂, V̂] ≠ 0; m segments; the Taylor argument; Û | notes p. 5 |
| 7 | beads | inserting the identity; Z₃ and Z_m; the matrix element of Û | notes p. 6 |
| 8 | action | S_m; the Euclidean action of hydrogen | notes p. 7 |
| 9 | weight | S_E,m; the unbounded potential weight; I(ε) = +∞; the four conclusions | notes pp. 8–9 |
| 10 | onebead | proof that the one-bead integral diverges; growth law; figure | `final.md` B.1, (B1)–(B6); check C1 |
| 11 | springs | the kinetic factors cannot compensate; the m-th power law | `final.md` B.2, (B7)–(B9), B.5, (B16); check C2 |
| 12 | continuum | Kato class; the exact kernel at the origin; the trace is infinite | `final.md` C.2–C.4, (C7); checks C4, C5 |
| 13 | trotter | the Trotter product formula and the hypothesis −1/r violates | `final.md` C.6, (C8)–(C9) |
| 14 | notes | what changed in the notes, H1 to H6 | `final.md` Part D |
| 15 | summary | summary and the next phase | — |

`final.md` is `../../S01-primitive-divergence/final/final.md`.

## Notation

Slides 2 to 9 use the notation of the notes: N slices of length ε and mass m in the
real-time part; m segments, Δβ = β/m, Δτ = ħΔβ, mass μ and k = e²/4πε₀ in the
imaginary-time part. Slides 10 to 15 use atomic units, a = Δτk/ħ (a = Δτ in atomic units),
and m for the number of beads. `final.md` writes N for the number of beads.

## Where the deck departs from the notes

Each of these is flagged on its slide, in muted text.

- Slide 7: the potential term is ΔβV(xⱼ), where p. 6 writes βV(xⱼ). Page 6's first line and
  p. 7 have it right.
- Slide 9: the discretised Euclidean action uses vector positions, |𝐫ⱼ₊₁ − 𝐫ⱼ|², where p. 8
  uses radial coordinates. Slide 8 writes the continuum action with |d𝐫/dτ|² for the same
  reason.
- Slide 9: item 1 on p. 9 reads "e^{a/r} → 0". The deck reads it as "the weight e^(a/r) is
  unbounded as r → 0". That is the reading of `final.md` Part D, which flags it as uncertain.

Two smaller changes are not flagged. Slide 4 writes the boundary condition as
z(tₐ) = z(t_b) = 0, where p. 3 writes z(tₐ) = z(t_b). Slide 3 writes out the last
difference term of the free-particle quadratic form, which p. 2 leaves to the dots.

## Numbers quoted on the slides

| on the slide | value | where it comes from |
|---|---|---|
| 10 | flat until η ≈ Δτ/15, then 33 orders of magnitude more by η = Δτ/100 | `figure/figure.out`: log₁₀ I = 0.782 at a/η = 15 and 33.547 at a/η = 100 |
| 11 | the springs remove 0.03 % for m = 2 at η = Δτ/80 | check C2 output: Δτ = 1, box radius 1.5, η = 0.0125, 1 − R = 3.21 × 10⁻⁴ |
| 12 | K₁(0,0) = 0.91957 | check C4 output, route (i): 0.9195694112 |
| 12 | a second route agrees to 5 × 10⁻⁷ | check C4 output: the Richardson-extrapolated box results differ from route (i) by at most 4.6 × 10⁻⁷ for τ = 0.5 to 4, and by 1.3 × 10⁻⁷ at τ = 1 |
| 12 | fourteen times the free value | check C4 output: ratio 14.4829 |

## Equations

Every equation on the slides was typeset by LaTeX and placed as an image.
`equations/equations.py` holds the LaTeX source of all 43, in slide order.
`equations/render.py` turns them into `equations/png/` at 480 dpi; the deck shows each
image at half its pixel size. It needs pdflatex with lmodern, amsmath, amssymb and xcolor,
pdftocairo from poppler, and Pillow. Run on 2026-10-26, it reproduced all 43 published
images pixel for pixel. `equations/sizes.json` has the pixel and display size of each.

## Figure

`figure/figure.py` computes the one-bead integral 4π∫_η^1 r² e^{a/r} dr by direct
quadrature at 40 digits (mpmath, the method of check C1), for a = Δτ = 0.1 and a/η from 1
to 100. It plots it against the growth law 4πη⁴e^{a/η}/a and the lower bound
(2πa³/3) ln(ε/η). Its printed values are in `figure/figure.out`.

The figure was computed for the deck after S01 closed. It is not one of S01's checks, and
no auditor has read it. It agrees with check C1, which tests the same law over a wider
range.

## Open items

- The cover still reads "[Team names]".
- The slide layout was spaced by estimated heights and has not been checked by rendering.
  Slides 10 and 13 are the closest to the footer.
- Slides 12 and 13 cite Simon 1982 and Reed–Simon I, Theorem VIII.31. Both are still
  `{ver: no}` in S01's sources.
