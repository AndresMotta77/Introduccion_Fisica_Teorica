# Coverage note — c5_kato_class_run1_scipy.py

This is run 1 of check C5, the failed run. It used scipy QUADPACK and failed the comparison with the recalled Newton formula at |x|/delta = 0.99 (1.6e-7 against a tolerance of 1e-7), while QUADPACK issued non-convergence warnings. The bound check, which is the claim the derivation uses, passed at every point.

Output: `c5_kato_class_run1_scipy.out`. Run twice in round 1 and once in round 2, with byte-identical output. The only edit to the output is the removal of the absolute sandbox path in front of the script name in scipy's warning lines, which `answers/answer-2.md` §4.2 also states.

What the check would and would not have caught, the change made for run 2, and why: see `c5_kato_class.coverage.md`, which reproduces the answer's text for both runs.
