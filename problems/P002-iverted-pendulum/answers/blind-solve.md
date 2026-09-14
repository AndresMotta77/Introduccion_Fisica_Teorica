# MISSING — blind solve, stage 0

**Not run.**

`templates/blind-solve-prompt.md` v1.0 describes an optional stage 0 in which
the auditor solves the problem cold from `prompts/prompt0.md` alone, before
seeing any solver output. It was not run for P002.

Consequence, stated plainly because it bears on how much the round-1 audit is
worth: the auditor read `answer-1.md` before forming any opinion of its own, so
its idea of what the answer should be was anchored on the answer it was
auditing. `claude/workflow-feedback.md` §2 is about exactly this. The audit
found two MINOR findings and no anchoring step the solver had not already
self-reported, which is the outcome that stage 0 is designed to make
interpretable and which, without stage 0, is not.
