# MISSING — exploration

**Not run.**

`templates/exploration-prompt.md` v1.0 describes the step after the final
result: a third model generates research branches from the closed problem, each
recorded with difficulty, prerequisites, first step, expected obstruction, and
whether the literature has already done it. Branches then go into `index.yaml`
as a queue.

It was not run for P002, so `branches_queued` is empty.

The raw material is already written: `final/final.md` §Open questions lists six,
of which the first two are concrete and cheap:

1. The $O(\varepsilon^2)$ correction to the threshold, $c \to -0.4374 \approx
   -7/16$, observed numerically in check N4 and neither derived nor sourced.
2. Where the $O(\varepsilon^2)$ correction to $\Omega$ changes sign, observed at
   $\mu \approx 0.7$ at a single $\varepsilon$ in check N8.

Both are second-order averaging calculations with a numerical counterpart that
already exists in `assets/code/`, and the two must agree with each other, which
makes either one a self-checking exercise.
