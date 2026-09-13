# Human attempt — v1.0

Written and committed **before** prompt0 is sent. That ordering is the whole
point, and git timestamps are what make it checkable.

## Why this comes first

In the workflow as originally drawn, the human node hung off the problem and led
nowhere: you choose a problem, and the models do the rest. A loop built that way
produces results you cannot vouch for.

This repository already does the right thing — problem 01 records a timed
twenty-minute attempt before any model was consulted. Formalising it does two
things. It gives the loop a prior that was not produced by a language model, so
when the model's answer differs from yours the difference is information. And it
records what you thought before you were anchored, which you cannot reconstruct
afterwards: once you have read a model's solution you no longer have access to
the version of yourself that had not.

## Structure

```markdown
# Human attempt — P###

Time spent: ⟨e.g. 20 min⟩, uninterrupted / interrupted
Date: ⟨⟩
Consulted: ⟨notes, textbook + locator, a classmate, nothing⟩

## How I read the problem
⟨What is being asked, in your own words. Where the statement is ambiguous.⟩

## Hypotheses I am using
⟨Numbered. These are the ones you will compare against the model's. State them
even when they feel obvious — "rolls without slipping" is a hypothesis.⟩

## Work
⟨Your derivation, or a scan. Incomplete is fine and expected.⟩

## Where I got stuck
⟨The specific obstruction. Not "I ran out of time" but what you could not get
past and what you would have needed.⟩

## My prediction
⟨Your answer, or your best guess, or the form you expect the answer to take.
Commit to something. A prediction you got wrong is worth more to you later than
no prediction.⟩

## Confidence
⟨0 to 1, in the prediction.⟩
```

## Rules

- Commit it before sending prompt0. The `human_attempt_first` gate checks the
  git history for this ordering.
- Do not edit it afterwards. If the model changes your mind, that belongs in the
  bitácora narrative, not here. This file is a record of a prior, and a prior
  edited after seeing the data is not a prior.
- An honest "I could not start" is a valid entry, with what blocked you.
- Scans go in `assets/figures/` and are linked from here.

## What it feeds

- prompt0 §3b, "my partial work, unverified" — copied from here, and the solver
  is instructed to treat it as a hypothesis and to say which steps are wrong.
- The comparison in `sources/independence.md`: your hypotheses against the ones
  the model used, which is the comparison problem 01 of this repository already
  makes by hand.
- `meta.yaml`: `human_attempt.prediction_correct`, and whether the model found an
  error in your work that you had not found.
