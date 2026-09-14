# MISSING — audit prompt 1, as sent

**This file is a record of an absence, not a reconstruction.**

`templates/audit-prompt.md` v1.2 was the template in force. The prompt as
actually sent to the auditor — with its INPUTS block naming which files were
pasted, and any per-problem edits — was composed by the user in the auditor's
own context and was never pasted back into the solver's conversation.

What is known:

- The auditor returned a nine-pass report matching the v1.2 pass structure, so
  the template was substantially followed.
- Part A is in `audits/audit-report-1.md`, verbatim.
- Part B is in `prompts/corrector-prompt-1.md`, verbatim.
- The auditor's model and effort are user-reported in `meta.yaml`; the report
  carried no run header, which audit-prompt v1.3 would have required.

What is not known, and is not guessed here: which files were pasted into the
INPUTS block, whether the assets in `assets/code/` were provided to the auditor
or only the listings inside `answer-1.md`, and whether the prompt was edited.

The auditor's pass 6 states that it reviewed the solver's verification code, and
the report quotes a script of its own that it says it ran, so at minimum the
code listings reached it.
