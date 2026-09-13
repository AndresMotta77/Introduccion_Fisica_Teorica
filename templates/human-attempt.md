# Human attempt — v1.1

Your own attempt at the problem, recorded before the model sees it. Recommended,
not required. Nothing in the workflow fails if it is missing, incomplete, or
never made it out of a notebook.

## Why it is worth recording

In the workflow as originally drawn, the human node hung off the problem and led
nowhere: you choose a problem, and the models do the rest. A loop built that way
produces results you cannot vouch for.

Recording your attempt does two things. It gives the loop a prior that was not
produced by a language model, so when the model's answer differs from yours the
difference is information rather than noise. And it preserves what you thought
before you were anchored, which you cannot reconstruct afterwards: once you have
read a model's solution you no longer have access to the version of yourself
that had not.

Neither of those depends on the format.

## Format: whatever it actually is

A photo of two handwritten pages is a perfectly good record. So is a scan, a
tablet sketch, a few lines of notes, or nothing at all with a sentence saying
you did not get started. Put images in `assets/figures/` and reference them from
`human/attempt.md`, or just drop them in `human/` directly if writing a file
around them is friction you would rather avoid.

Do not retype handwritten work into markdown for the sake of the template. The
transcription costs you time and adds a place for errors to enter. Transcribe
only the specific steps you want the model to check, and put those in prompt0
§3b.

## Structure, if you are writing text

Use as much of this as is useful and delete the rest.

```markdown
# Human attempt — P###

Time spent: ⟨e.g. 20 min⟩
Date: ⟨⟩
Consulted: ⟨notes, textbook + locator, a classmate, nothing⟩
Form: ⟨scan | notes | markdown | none⟩

## How I read the problem
⟨What is being asked, in your own words. Where the statement is ambiguous.⟩

## Hypotheses I am using
⟨Numbered. These are the ones worth comparing against the model's. State them
even when they feel obvious — "rolls without slipping" is a hypothesis.⟩

## Work
⟨Your derivation, or a link to the scan. Incomplete is fine and expected.⟩

## Where I got stuck
⟨The specific obstruction, if there was one.⟩

## My prediction
⟨Your answer, your best guess, or the form you expect the answer to take. Worth
committing to something: a prediction you got wrong is more useful later than no
prediction. Skip it if you have nothing.⟩

## Confidence
⟨0 to 1, in the prediction.⟩
```

## The one thing worth keeping straight

Whenever it was recorded, do not quietly revise it after reading the model's
answer. If you do revise it, or if you wrote it up afterwards from memory, note
that in `meta.yaml` under `human_attempt.recorded`. An attempt written after the
fact is still useful; one that is presented as a prior when it is not will
mislead you months later when you are trying to work out who found what.

## What it feeds

- prompt0 §3b, "my partial work, unverified" — whatever of it you want checked.
  The solver is instructed to treat it as a hypothesis and to say which steps
  are wrong.
- The comparison in `sources/independence.md`: your hypotheses against the ones
  the model used.
- `meta.yaml` under `human_attempt`, where every field may be `unknown`.
