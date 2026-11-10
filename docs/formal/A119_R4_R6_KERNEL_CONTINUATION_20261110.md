# A119 rational box certification: r=4–6 continuation

**Recorded:** 10 November 2026  
**Working branch:** `research/a115-a119-uniform-remainder-20261110`  
**Source object:** reduced C2(k) A119 critical-substitution rational expression `criticalXiHat`.  
**Not claimed:** F2/F3 global optimality, a proof over real parameters, A115–A118 asymptotic equivalence, historical novelty or a physical principle.

## What is actually kernel checked

The Python Fraction certificate still has 35/35 positive exact rational interval boxes. Earlier Lean jobs certified two of those boxes, the r=4 upper halves (one even, one odd).

The new [A119R4Remaining.lean](../../formal/lean/PrecategoryFormal/A119R4Remaining.lean) checks the four other r=4 boxes with `decide +kernel`:

- even r=4, normalized alpha fractions [0,1/4] and [1/4,1/2];
- odd r=4, normalized alpha fractions [0,1/4] and [1/4,1/2].

GitHub Actions [run 42883385073](https://github.com/DevHabito/precategorical-modal-field-framework/actions/runs/42883385073) at commit `62d930d5c92f0231ac68dd1ae6294cd0332669ff` finished **30/30 SUCCESS**. Its `leanchecker (PrecategoryFormal.A119R4Remaining)` job passed. Counting all prior verified boxes, the confirmed result is **6/35 rational rectangles**.

The linked source `A119R4Remaining.lean` explicitly derives the conjunction of each parity's three kernel-checked Boolean interval evaluations. It does not trust a lower bound copied from Python.

## Stronger r=4 coverage gate

The separate [A119R4Coverage.lean](../../formal/lean/PrecategoryFormal/A119R4Coverage.lean) proves, assuming its checked dependencies, that the **entire enlarged r=4 alpha range** is positive on the rational s source window, with shared endpoints retained:

- even: 8 ≤ alpha ≤ 21/2;
- odd: 9 ≤ alpha ≤ 231/20;
- both: 129/1000 ≤ s ≤ 133/1000.

It uses the previously kernel-proved `quarter_half_split_covers` theorem and `certified_box_sound` to turn the six finite Boolean bounds into quantified statements. This module has compiled successfully. **Its individual leanchecker job must be checked on [run 42883765927](https://github.com/DevHabito/precategorical-modal-field-framework/actions/runs/42883765927) before claiming full-interval kernel replay.**

## New r=5 and r=6 attempts

- [A119R5Boxes.lean](../../formal/lean/PrecategoryFormal/A119R5Boxes.lean): four box calculations, each parity split into normalized alpha halves [0,1/2] and [1/2,1]. It additionally states the two full-cell rational consequences. Even alpha range [10,63/5]; odd alpha range [11,273/20]. [Latest submitted workflow 42884049414](https://github.com/DevHabito/precategorical-modal-field-framework/actions/runs/42884049414).
- [A119R6Boxes.lean](../../formal/lean/PrecategoryFormal/A119R6Boxes.lean): the analogous four kernel calculations at deficit 6. [Latest submitted workflow 42884588094](https://github.com/DevHabito/precategorical-modal-field-framework/actions/runs/42884588094).

These **eight** r=5 and r=6 calculations must **not be included** in the 6/35 confirmed count until each relevant individual module job succeeds. The Python 35-box test passing is a separate evidence tier.

## Why this structure matters

One large computation for 35 cases gives poor failure localization and may be costly to replay. Small named kernel proofs let a reviewer inspect exactly which rational box passed, which one failed to reduce, and whether the interval evaluator properly refused a denominator crossing zero. The computational method is ordinary rational inclusion interval arithmetic; no novelty credit should be claimed for it.

Kernel evaluation of an input formula does not prove the *derivation* of that formula from the original LP. The existing formally checked equality of the expression AST and `criticalXiHat` is necessary for this task, but A115–A118's cofactor-to-asymptotic chain remains a distinct, unclosed proof obligation.

## Next gates

1. Record exact build/replay status for r=4 coverage, r=5 and r=6 with run IDs and commit SHAs. Do not confuse workflow success at an earlier revision with a later branch head.
2. Continue with r=7 and the unsplit ranges r=8..12 (even) and r=8..19 (odd). There are 35 total rational rectangles.
3. Connect the full exact manifest to an explicit finite union proof. No gaps or lost endpoints.
4. Prove real-valued sound interval evaluation or a justified transfer to real parameters, preserving a strictly positive *uniform margin* and denominator nonvanishing.
5. Recheck the A119 high-deficit tail and A118 coefficient identification in the Lean kernel. Compare the actual theorem with full-text prior art before any novelty claim.

**Editorial judgment:** this checkpoint improves mechanical verification of a reduced rational sign lemma. It does not make A119 a finished or novel mathematical theorem.


## Verified r=4 coverage checkpoint

The full [GitHub Actions run 42883765927](https://github.com/DevHabito/precategorical-modal-field-framework/actions/runs/42883765927) completed **30/30 SUCCESS** at exact source commit \`72c12f7a8b2f8d57e16e9eb224543ee5f89e12d6\`. Its dedicated \`leanchecker (PrecategoryFormal.A119R4Coverage)\` job \`130068298976\` also passed. This lifts the six verified rational box calculations to two quantified rational-range theorems:

- even parity, r=4: for all rational s in [129/1000,133/1000] and rational alpha in [8,21/2], \`criticalXiHat s alpha false 4 > 0\`;
- odd parity, r=4: for the same rational source window and rational alpha in [9,231/20], \`criticalXiHat s alpha true 4 > 0\`.

The total count remains **6/35**; the coverage theorem does not create new boxes. The theorem does not quantify over real-valued s or alpha, nor does it establish F3 optimality.


## Verified r=5 kernel checkpoint (2026-11-10)

[Lean run 42884049414](https://github.com/DevHabito/precategorical-modal-field-framework/actions/runs/42884049414), source commit `e00892ba34ab502b8232f79c3331cc7e1e9739b9`, has **completed SUCCESS**, including `leanchecker (PrecategoryFormal.A119R5Boxes)`. The module verifies four direct interval evaluations, two per parity at r=5, and two resulting rational full-cell theorems using the half-interval coverage lemma. Thus the cumulative individually replayed box count is **10/35**: six r=4 plus four r=5.

The r=6 module and the r=7..12 modules were separately submitted in subsequent source commits and may be queued; they are **not counted** until their own run's relevant individual checker succeeds. Source commit `f1c63f4f907f56a74ebfe5115c0bf6b0c7de2eb7` submits 14 r=7..12 boxes (4 at r=7, 10 at r=8..12); [CI run 42886987495](https://github.com/DevHabito/precategorical-modal-field-framework/actions/runs/42886987495) is the corresponding run. Python Fraction originally certifies 35/35 independently, but is not a substitute for these Lean kernel checks.
