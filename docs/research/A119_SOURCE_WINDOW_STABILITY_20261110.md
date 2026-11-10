# A119 source-window robustness: exact interval stress, not an expanded theorem

**Date:** 2026-11-10
**Object:** the rational critical-substitution expression `Xi_hat` for the C2(k) reduced factor, **not** a full F2/F3 optimum.
**Evidence status:** the 35-box interval calculation was run locally with exact Python `fractions.Fraction`; the checked-in regression has an independent GitHub Actions job, whose result must be read separately.

## Frozen and expanded source windows

Keep beta=1/8, delta=1/1875, the original 25 even/odd deficit cases (r=4..12 even and r=4..19 odd), and the same three/two/one alpha subdivisions. The only changed input is the **entire source interval**:

| Source s window | Certified smallest interval lower endpoint | Interpretation |
|---|---|---|
| [129/1000,133/1000] | +0.10897635234978477... | Original 35-box positive certificate |
| [2577/20000,2663/20000] | +0.0028682145964118717... | Same 35 boxes remain strictly positive on a wider s window |
| [5153/40000,5327/40000] | -0.014769998385757625... | **Cannot certify** this larger window with the present 35 boxes |

The positive exact lower endpoint for the expanded interval is

[
\frac{71236007338704140184291611230761656680237}
{24836358976702853398583841218100200880000000}>0.
]

The negative *interval* lower endpoint for the widest interval is

[
-\frac{4518288062067068960278283117747144304408421689241}
{305909854832750130910735184846607522602622720000000}<0.
]

In all cases the worst box is **even parity, r=4, alpha-fraction [1/2,1]**. These rational fractions are outward inclusion bounds, not evaluations of Xi_hat at specific points. A negative lower enclosure does not mean the function is negative anywhere.

The reproducible test is [a119_compact_source_window_stress_20261110.py](../../audits/a119_compact_source_window_stress_20261110.py). It imports the repository's exact 35-box `calc`, recomputes all 35 endpoints and uses equality assertions for the expanded minimum. No floating-point comparison is used to establish any sign.

## Why this matters

The original frozen interval is **not mathematically distinguished by the 35-box positivity inequality alone**: at least this slightly larger, explicitly rational window is enclosed positively. That is a concrete robustness fact for the **critical rational expression**.

This is **not** a valid claim that A116-A119 has been proved on the larger source window. To promote that theorem, independently check every source-dependent ingredient, including:
- `beta<s<1/4`, `C>0`, `B<1`, and central denominator inequalities;
- A116 uniform channel estimates, their bounds and quantifiers;
- A117's positive entry and the exact half-open contact convention;
- A118 coefficient identity and uniform remainder on the new source window;
- A119 exclusion of all later deficit cells under new rational tail inequalities.

Also, a negative interval lower bound on the still wider window might be repaired by subdivision or a better analytic enclosure. It **cannot** be cited as a mathematical counterexample to `Xi_hat>0`.

## Reproducibility and publication

Keep the original 6,400-box and 35-box tests; add this sensitivity audit as a separate regression. The method is classical interval arithmetic. No originality claim, physical interpretation or universal LP-support conclusion follows.

New Lean module `PrecategoryFormal.A119CompactCertificate` is a first formalization gate for box counts, coverage and basic interval operations. It does not yet establish the 35 Xi_hat lower bounds in Lean. CI status must be recorded independently.


## Independently verified CI outcome

GitHub Actions [exact-arithmetic run 42866656323](https://github.com/DevHabito/precategorical-modal-field-framework/actions/runs/42866656323), source SHA \`08eb97a475eafad28249cbe5ada501e492d2bb02\`, completed with conclusion **success**. The actual \`exact-python\` job (ID \`130006685250\`) included a successful dedicated source-window step. Its decoded log printed the exact expanded-window minimum fraction above and confirmed the deliberately non-certifying control on the larger window. This was not inferred from an earlier local test.

Do not interpret this CI result as Lean verification, a proof of an expanded A116-A119 theorem, or historical novelty.
