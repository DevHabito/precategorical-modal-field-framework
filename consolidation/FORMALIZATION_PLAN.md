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
- bundled `leanchecker` replay for each project module, sharded across CI runners so the independent replay is not hidden by build/runtime limits;
- generated finite certificates allowed only when their generator and checker are both documented.

## Formalization order

### F0 — definition sanity pilot — COMPLETE

Formalize MF-R009, the non-injectivity of the minimum-representative quotient-poset code, using one explicit finite witness.

Purpose: validate the graph/SCC/quotient/code definitions before attempting a counting theorem.

Completion status: the explicit two-graph witness is connected to `Relation.ReflTransGen` reachability, SCC minima, quotient orders, and the direct representative-code computation with no `sorry`.

### F1 — first substantive target: MF-R008 — COMPLETE

Formalized the shifted-binomial count

\[
N_{\mathrm{rep}}(n)=\sum_{k=1}^{n}\binom{n-1}{k-1}p(k).
\]

The completed proof does not trust the historical Python enumerator. It contains the following independent layers:

- a finite labeled ground carrier and the family of representative sets containing the distinguished label `0`;
- a proof that the `k`-representative fiber has cardinality `binom(n-1,k-1)`;
- an executable three-state encoding of antisymmetric relations on unordered pairs;
- exact Lean `native_decide` enumeration of the small labeled-poset counts `1,3,19,219,4231`;
- a semantic proof that the executable transitivity checker is equivalent to mathematical transitivity;
- an exact bijection between accepted three-state encodings and Boolean partial-order matrices;
- an explicit canonical MF-R008 code type whose cardinality is the fiber sum;
- a carrier-transport equivalence showing that the canonical `Fin k` presentation is exactly equivalent to the literal code `(S,P)` with `P` a partial order on the actual representative set `S`;
- the verified five-vertex conclusion `Nat.card (LiteralRepresentativeCode 4) = 5234`.

Verification status: the complete Lean library builds with the pinned Lean/mathlib environment, rejects `sorry`/`admit`, and every project module passes a bundled `leanchecker` kernel replay in the module-sharded CI.

Scope boundary: F1 proves the declared MF-R008 code/count theorem. It does not establish novelty, count full SCC memberships, or imply injectivity of the representative code.

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

The implementation lives under

`formal/lean/`

with modules named by mathematical content rather than audit numbers. Current modules include the representative-code witness, representative counting, poset enumeration/semantics/bijection, count bridge, and literal-code carrier equivalence. A-number provenance may appear in comments, not in theorem names.
