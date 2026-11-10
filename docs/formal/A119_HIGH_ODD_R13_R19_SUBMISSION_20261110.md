# A119 high-contact odd boxes: r=13–19 kernel submission

**Date:** 2026-11-10. **Branch:** research/a115-a119-uniform-remainder-20261110.

This commit adds the last **seven** high-contact odd-parity rational
interval computations, one for each deficit r=13,...,19, with exact
`passes true r 0 1 = true` statements and `decide +kernel` proofs.
The s window is [129/1000,133/1000] and alpha is the unsplit
enlarged r-specific interval from `alphaBox`.

The historical Python Fraction checker reports 35/35, but a source
file containing these seven Lean proofs is only a **submission**.
The individual `leanchecker (PrecategoryFormal.A119OddR13R19)` job
and the build on the **exact committing SHA** must pass before these
boxes may be included in a Lean-certified count.

Submissions now cover all 35 original boxes: six r=4, four each at
r=5,6,7, ten at r=8,...,12 and seven odd-only at r=13,...,19.

**Still missing:** kernel replay for the newest modules; the
quantified finite-manifest union proof; the rational-to-real
extension; the exact A118-to-Xi-hat critical coefficient identity;
and the A115-to-A118 uniform asymptotic derivation. None of these
are established by successful finite arithmetic alone.

The coefficient describes a reduced two-active-band candidate
family, not a global F2/F3 optimizer, a pregeometry law, or a
certified original theorem. Record all failed and successful CI runs.
