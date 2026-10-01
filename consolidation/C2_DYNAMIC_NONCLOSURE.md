# C2 — exact dynamic non-closure of one fixed entropic score

**Source claim:** MF-R049  
**Consolidation target:** F3  
**Current status:** formalization active; end-to-end kernel gate not yet closed  
**Novelty status:** project-specific exact corollary with constructive witness; priority not certified

This note is the self-contained consolidation unit for the selected dynamic
non-closure result. Historical A34 material remains provenance.

## Box 1 — Hypotheses

Work with finite probability distributions on real scores. For a fixed
`lambda > 0`, define

\[
M_\lambda=\sum_i p_i e^{-\lambda q_i},
\qquad
Q_\lambda=-\frac1\lambda\log M_\lambda.
\]

Use the centered half-contraction

\[
q_i'=\bar q+\frac12(q_i-\bar q).
\]

The counterexample is allowed to use any finite support because the selected
claim concerns the unrestricted finite-distribution class.

## Preferred exact witness

Freeze

\[
\lambda=\log2,
\qquad
q=(0,2,4,6).
\]

Define

\[
p^+=\left(\frac{31}{80},\frac38,\frac7{80},\frac3{20}\right),
\]

\[
p^-=\left(\frac{33}{80},\frac9{40},\frac5{16},\frac1{20}\right).
\]

All entries are strictly positive and both vectors have total mass one.
Their common mean on support `(0,2,4,6)` is exactly

\[
\bar q=2.
\]

At `lambda=log 2`, the initial exponential moments are exactly

\[
M_\lambda(p^+)=M_\lambda(p^-)=\frac{313}{640}.
\]

Hence

\[
Q_{\log2}(p^+)=Q_{\log2}(p^-).
\]

Under the centered half-contraction, the support becomes exactly

\[
(1,2,3,4).
\]

At the same fixed observational parameter `lambda=log 2`, the next moments are

\[
M_\lambda'(p^+)=\frac{197}{640},
\qquad
M_\lambda'(p^-)=\frac{39}{128}=\frac{195}{640}.
\]

Therefore

\[
M_\lambda'(p^+)-M_\lambda'(p^-)=\frac1{320}>0.
\]

Because both next moments are positive, `log` is injective on them, and
`log 2 != 0`, it follows that

\[
Q_{\log2}'(p^+)\ne Q_{\log2}'(p^-).
\]

## Box 2 — Conclusion

There exist two strictly positive normalized four-point distributions with the
same mean and the same fixed entropic score `Q_{log 2}`, but with different next
`Q_{log 2}` values after the declared centered half-contraction.

Thus the macrostate

\[
(\bar q,Q_{\log2})
\]

is not dynamically closed on the unrestricted finite-distribution class under
that update.

This is an existence counterexample. It is sufficient to refute the universal
closure claim.

## Box 3 — Verification status

### Exact arithmetic

PASS for the frozen rational targets:

- both probability vectors are strictly positive;
- both masses are exactly `1`;
- both means are exactly `2`;
- both initial moments are exactly `313/640`;
- the updated support is exactly `(1,2,3,4)`;
- the next moments are exactly `197/640` and `39/128`;
- their difference is exactly `1/320`.

### Lean path

The active branch separates the proof into:

1. exact rational witness arithmetic;
2. a parameter-preserving direct witness at `lambda=log 2`;
3. small `Real.exp`/`Real.log` plumbing lemmas;
4. an end-to-end theorem connecting equal initial `(mean,Q)` to unequal next
   `Q` after the centered half-contraction.

**Promotion status: NOT YET COMPLETE.**

The result is not promoted to `END-TO-END LEAN/KERNEL PASS` until a clean pinned
`lake build`, proof-placeholder rejection, and every declared module-sharded
`leanchecker` replay pass on the final branch HEAD.

## Box 4 — Nonclaims

C2/MF-R049 does not establish:

- that no finite-dimensional closure can exist on restricted distribution
  families;
- that four support points are globally minimal;
- that the whole curve `lambda -> Q_lambda` is always the unique minimal state;
- a new general theorem resolving the moment-closure problem;
- a stochastic or physical evolution law;
- any empirical claim about nature;
- any bridge to RZS, spacetime, gravity, or quantum theory.

The exact result is narrower: one fixed entropic score together with the mean is
not sufficient to determine its own next value on the unrestricted finite class
under the stated centered contraction.
