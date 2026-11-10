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
