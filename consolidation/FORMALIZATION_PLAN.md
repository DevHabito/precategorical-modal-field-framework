# Consolidation 1.0 — Lean 4 formalization roadmap

The goal of formalization is not to make the project look more rigorous. The goal is to expose missing definitions, hidden assumptions, type mismatches, and invalid inference chains to an independent proof kernel.

Lean verification certifies only that a formal conclusion follows from formal hypotheses. It does not certify novelty, empirical relevance, or that nature satisfies the hypotheses.

## Toolchain

Preferred stack:

- Lean 4;
- mathlib;
- `lake` project with pinned dependency versions;
- CI that runs `lake build` on every change to formal files;
- no `sorry` in files marked verified;
- generated finite certificates allowed only when their generator and checker are both documented.

## Formalization order

### F0 — definition sanity pilot

Formalize MF-R009, the non-injectivity of the minimum-representative quotient-poset code, using one explicit finite witness.

Purpose: validate the graph/SCC/quotient/code definitions before attempting a counting theorem.

Success criterion: a theorem with no `sorry` showing two distinct full structures map to the same representative code.

### F1 — first substantive target: MF-R008

Formalize the shifted-binomial count

\[
N_{\mathrm{rep}}(n)=\sum_{k=1}^{n}\binom{n-1}{k-1}p(k).
\]

The proof should isolate the combinatorial bijection rather than trust the Python enumerator.

Required components:

- finite labeled carrier;
- partition/SCC-block representation;
- distinguished minimum representative in each block;
- quotient partial order;
- precise code equivalence relation;
- proof that choosing the `k-1` non-distinguished minima contributes `binom(n-1,k-1)`;
- multiplication by the count `p(k)` of labeled quotient partial orders under the chosen convention;
- summation over `k`.

The formal theorem may treat `p(k)` abstractly first; a later module can connect it to an explicit finite enumeration definition.

### F2 — independent finite computation: MF-R011

Formalize the declared finite graph ensemble and edge-toggle operation. Use a decidable computation (`native_decide` or equivalent) to certify the exact small-n values, especially

\[
P_5=75/256.
\]

This should be independent of the existing Python enumeration implementation.

### F3 — exact dynamic non-closure: MF-R049

Formalize the explicit finite witness proving that mean plus one fixed-lambda entropic score does not determine the next score under the declared update.

Prefer a theorem over a minimal finite real/rational construction. Any use of `exp`/`log` should be isolated so that the counterexample does not inherit unnecessary analytic machinery.

### F4 — only after compression: optimization theorems

Do not formalize A112–A122 in chronological form. First rewrite them as C3/C4/C5 self-contained theorem packages. Then select small reusable lemmas:

- determinant/non-singularity lemmas;
- exact sign implications;
- one-variation consequences from adjacent nesting inequalities;
- rounding-phase sign-front lemma;
- interval/cell decomposition statements.

The final asymptotic theorems may require more mathlib infrastructure and are not the first formalization target.

## Independence policy

The Lean development should not import generated facts from the existing Python audits as axioms. Python may generate candidate witnesses or finite data, but Lean must check the mathematical statement from definitions.

For finite exhaustive claims, two implementations are preferred:

1. existing Python exact enumeration;
2. Lean decidable computation from independently written definitions.

Agreement is useful precisely because the implementations do not share the same code path.

## Directory target

When implementation begins, use

`formal/lean/`

with modules named by mathematical content rather than audit numbers, for example:

- `RepresentativeCode.lean`
- `RepresentativeCodeCount.lean`
- `EdgeToggleSensitivity.lean`
- `DynamicNonclosure.lean`

A-number provenance may appear in comments, not in theorem names.
