# P003.S03 — The harmonic oscillator under a bridge-averaged slice weight: closed form and levels

**Date:** 2026-11-12
**Verdict:** ACCEPT-WITH-FIXES (audit 1, on answer-1; answer-2 applies the fix and was not audited)
**Rounds:** 1 audit round, 2 answers
**Status:** closed (2026-11-13)

## 1. The problem

<!-- Statement, verbatim. Image in assets/figures/ if there is one. -->

<!-- Filled by /log on 2026-11-13: §1 of prompts/prompt0.md, verbatim. The other sections are yours. -->

Take the one-dimensional oscillator $H = K + V$, $K = -\tfrac12\, d^2/dx^2$, $V(x) = \tfrac12 x^2$,
with $\hbar = M = \omega = 1$. Let $\rho_0(x, x'; t) = (2\pi t)^{-1/2} \exp\!\big(-(x - x')^2/2t\big)$ and
define, for a slice of length $\tau$,

$$
w(x, x'; \tau) = \rho_0(x, x'; \tau)\,
\exp\!\Big( -\int_0^\tau du\, \frac{1}{\rho_0(x, x'; \tau)} \int_{-\infty}^{\infty} dy\,
\rho_0(x, y; u)\, V(y)\, \rho_0(y, x'; \tau - u) \Big).
$$

(a) Evaluate $w$ in closed form, writing out every step of the $y$- and $u$-integrals.

(b) With $\tau = \beta/m$ and $x_{m+1} = x_1$, let

$$
\hat Z_m(\beta) = \int dx_1 \cdots dx_m \prod_{n=1}^{m} w(x_n, x_{n+1}; \tau), \qquad
Z_m(\beta) = \int dx_1 \cdots dx_m \prod_{n=1}^{m} \rho_0(x_n, x_{n+1}; \tau)\, e^{-\tau V(x_n)} .
$$

Derive both in closed form by diagonalising the quadratic forms, and the energies
$\hat E_m = -\partial_\beta \ln \hat Z_m$ and $E_m = -\partial_\beta \ln Z_m$. Evaluate them for
$\beta \in \{1, 5, 10\}$ and $m \in \{1, 10, 50, 100, 500\}$, and compare with the exact thermal
energy.

(c) $w$ is the kernel of an integral operator $T_\tau$ on $L^2(\mathbb R)$. Find its eigenvalues
$\lambda_n(\tau)$ in closed form for all $\tau > 0$, and compare $E_n(\tau) = -\tau^{-1} \ln \lambda_n(\tau)$
with the exact levels: give the leading terms of $E_n(\tau) - (n + \tfrac12)$ as $\tau \to 0$, for
every $n$. Do the same for the kernel of $e^{-\tau V/2} e^{-\tau K} e^{-\tau V/2}$. Say how (b) and
(c) are related, and check that they agree.

## 2. My first attempt

<!-- One paragraph, if you made one. Whatever form it took is in human/.
     Delete this section if there was no attempt. -->

## 3. First interaction with the AI

<!-- The prompt is in prompts/prompt0.md. Which model, which effort level,
     how long it took. The hypotheses it put on the table. -->

## 4. Audit

<!-- What the auditor found. Which findings were accepted, which were rebutted
     and upheld. -->

## 5. How the model handled being corrected

<!-- Your own read of the exchange, written after the loop closed. Nobody but
     you can write this section: it is a judgement about how the conversation
     went, not a fact recoverable from the files.

     Worth noting when it applies:
     - Did it concede anything without an argument, or concede a point you
       later decided was right after all?
     - Did it push back, and was the rebuttal any good?
     - Did any answer look retrieved rather than derived, and what gave it
       away?
     - Did a correction of yours send it somewhere worse?
     - Anything it did that you would not have predicted.

     One honest paragraph beats a checklist. Delete the section if nothing
     about the exchange was worth recording. -->

## 6. Reflection

<!-- What actually happened, in your own words. This section is the point of
     the logbook. -->

## 7. What this problem changed in the method

<!-- Only if something did. Delete this section otherwise. -->
