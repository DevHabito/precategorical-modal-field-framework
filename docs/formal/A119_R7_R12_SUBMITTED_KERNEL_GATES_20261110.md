# A119: r=7 and r=8..12 rational box kernel-replay candidates

Date: 2026-11-10. Branch: research/a115-a119-uniform-remainder-20261110.

This checkpoint **submits** 14 more rational A119 critical Xi-hat
interval enclosures to the Lean kernel:
four r=7 half-interval boxes across both parities; and ten unsplit
r=8..12 boxes across both parities.

These new theorems invoke `decide +kernel` for the exact expression
evaluator. Their actual success must be independently established by
the run on the specific source commit and the individual
`PrecategoryFormal.A119R7Boxes` and
`PrecategoryFormal.A119R8R12Boxes` leanchecker jobs.

The r=7 module additionally claims complete two-part closed-interval
coverage (even alpha in [14,84/5], odd in [15,357/20]) for rational
s in [129/1000,133/1000]. No Python Fraction result is assumed in
the Lean proof term.

Historical independently certified rational boxes: r=4 six and
r=5 four (10 total). r=6 four remain a separate CI dependency at
the time of writing. **Do not add these new 14 boxes to the count
unless their individual kernel jobs pass.** Compilation alone and
a queue entry are not proof.

Proof boundary: `criticalXiHat` is the exact rational critical
expression imported from A119, *not* a Lean-derived global F2/F3
optimizer nor a Lean proof of the original A115-A118 asymptotics.
The claims currently quantify only over rational parameters, not reals.


## Verified individual Lean kernel jobs

The **exact** [GitHub Actions run 42886987495](https://github.com/DevHabito/precategorical-modal-field-framework/actions/runs/42886987495), at source SHA \`f1c63f4f907f56a74ebfe5115c0bf6b0c7de2eb7\`, has the following individually completed **SUCCESS** jobs:

- \`leanchecker (PrecategoryFormal.A119R7Boxes)\`, job \`130081937364\`: four split-box Boolean interval evaluations, two in each parity, and the r=7 rational alpha-coverage theorems.
- \`leanchecker (PrecategoryFormal.A119R8R12Boxes)\`, job \`130081937229\`: ten unsplit interval evaluations, even and odd for each r=8,...,12.

The project build at this same revision also succeeded. Along with the earlier r=4, r=5 and r=6 kernel checks (14 boxes), this establishes **28/35** complete rational box evaluations. **Do not count the seven odd r=13..19 boxes yet:** their dedicated module is submitted in source SHA \`e5031677683c7d51625c9359b63ac4a96bcfca5d\`, [workflow 42887340405](https://github.com/DevHabito/precategorical-modal-field-framework/actions/runs/42887340405), and must pass its own checker.

Operational note: the standard GitHub connector's first-page \`fetch_workflow_run_jobs\` result may omit matrix jobs after item 30; for these 38- and 39-job runs we inspected the **complete** REST \`/actions/runs/{id}/jobs?per_page=100\` response before asserting individual module status.

This is source-to-explicit-rational-function verification only, not a Lean real-variable theorem or a source-to-A118 asymptotic derivation.
